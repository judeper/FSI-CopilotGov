#!/usr/bin/env python3
"""
Regulatory Monitoring Source Adapter for FSI-CopilotGov

Monitors regulatory changes from Federal Register API and FINRA notices page
that may require updates to the FSI-CopilotGov framework. This is a source
adapter for the unified monitoring framework - it uses shared utilities from
monitoring_shared.py.

Sources:
- Federal Register API (SEC, CFTC, OCC, Federal Reserve)
- FINRA Regulatory Notices (HTML scraping)

Usage:
    python scripts/regulatory_monitor.py [--dry-run] [--limit N] [--verbose] [--source SOURCE]

Exit Codes:
    0 - No new regulatory items detected
    3 - New regulatory items detected (triggers PR in CI)
    2 - Source or execution failure

Exit code 1 is deliberately not used for findings because Python uses it for
uncaught exceptions. The workflow treats every code except 0 and 3 as failure.

Environment Variables:
    REGULATORY_MONITOR_DEBUG=1  - Enable debug output
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from bisect import bisect_left, bisect_right
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from functools import lru_cache
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse, parse_qs

# Import shared monitoring framework
from monitoring_shared import (
    fetch_page,
    compute_hash,
    load_state,
    save_state_atomic,
    get_source_state,
    set_source_state,
    generate_report_header,
    generate_executive_summary,
    format_change_summary,
    write_report,
    load_monitoring_config,
    validate_config,
    DEFAULT_CONFIG_PATH,
    CLASSIFICATION_CRITICAL,
    CLASSIFICATION_HIGH,
    CLASSIFICATION_MEDIUM,
    CLASSIFICATION_NOISE,
)

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print(f"ERROR: Missing dependency: {e}")
    print("Install with: pip install requests beautifulsoup4")
    sys.exit(2)

# === Configuration ===
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / 'data'
REPORTS_DIR = PROJECT_ROOT / 'reports' / 'monitoring'
STATE_FILE = DATA_DIR / 'monitor-state.json'

# Exit-code contract. Keep findings away from Python's generic unhandled-
# exception code (1), so a crash can never be mistaken for monitor output.
EXIT_CLEAN = 0
EXIT_FAILURE = 2
EXIT_FINDINGS = 3

# Source keys for unified state file
SOURCE_KEY_FEDERAL_REGISTER = "regulatory-federal-register"
SOURCE_KEY_FINRA = "regulatory-finra"

# Federal Register API configuration
FEDERAL_REGISTER_API_BASE = "https://www.federalregister.gov/api/v1"

# FINRA notices page
FINRA_NOTICES_URL = "https://www.finra.org/rules-guidance/notices"

FEDERAL_REGISTER_DETAIL_FETCH_LIMIT: Optional[int] = None
FEDERAL_REGISTER_PAGE_SIZE = 100
FEDERAL_REGISTER_MAX_PAGES = 100
# Every eligible FINRA listing entry must be classified from its authoritative
# detail page before it can be returned to the state layer.  ``None`` means
# there is no production cap; an explicit limit is retained only as a test
# seam, and reaching it fails closed rather than baselining uninspected items.
FINRA_DETAIL_FETCH_LIMIT: Optional[int] = None
FALLBACK_TEXT_MAX_CHARS = 4000

# Change-detection fingerprint schema. Schema 1 (pre-versioning) hashed
# ``title|content|publication_date`` and is written as a bare ``sha256:`` digest.
# Schema 2 hashes ``title|report_text|authoritative_body|publication_date`` and
# is written with an explicit ``v2:`` tag so a stored digest always declares the
# layout it was produced under. Without that tag a comparison cannot tell a
# genuine content change from a schema change, which is how a changed late
# suffix was previously mistaken for a harmless legacy migration.
CONTENT_HASH_SCHEMA_VERSION = 2
CONTENT_HASH_SCHEMA_PREFIX = f"v{CONTENT_HASH_SCHEMA_VERSION}:"
LEGACY_CONTENT_HASH_SCHEMA_VERSION = 1
CONTENT_HASH_SCHEMA_PATTERN = re.compile(r"^v(\d+):")
FINRA_NOTICE_PATH_PATTERN = re.compile(
    r'^/rules-guidance/notices/(?:\d{2}-\d+|information-notice-\d{8})/?$',
    re.IGNORECASE,
)
# The notices listing itself (page 0 has no query; page N is ``?page=N``).
FINRA_LISTING_PATH_PATTERN = re.compile(
    r'^/rules-guidance/notices/?$',
    re.IGNORECASE,
)
# Hard bound on how many listing pages the crawler will follow. The live
# listing is ~92 pages; this leaves generous headroom while capping a hostile
# or malformed pager that would otherwise declare pages without end. Reaching
# it fails closed (see fetch_finra_notices) rather than baselining a partial
# crawl as complete.
FINRA_MAX_LISTING_PAGES = 200
# A leading ``/index.php`` front-controller segment is an accepted alias for
# the bare path ("/index.php/rules-guidance/notices/26-12" == the notice). It
# is stripped before path validation; a lookalike such as "/index.phpx/..." is
# not stripped (the ``(?=/)`` lookahead requires a following slash) and is
# rejected by the path patterns.
FINRA_INDEX_PHP_PREFIX_PATTERN = re.compile(r'(?i)^/index\.php(?=/)')
FINRA_NOTICE_ID_PATTERN = re.compile(
    r'/rules-guidance/notices/(\d{2})-(\d+)(?:[/?#]|$)',
    re.IGNORECASE,
)
FINRA_INFORMATION_NOTICE_DATE_PATTERN = re.compile(
    r'/rules-guidance/notices/information-notice-(\d{4})(\d{2})(\d{2})(?:[/?#]|$)',
    re.IGNORECASE,
)

# A 200 response is not proof that a notice body was served. FINRA (and the
# CDN in front of it) answers access-denied, bot-challenge, login, and
# not-found pages with a fully rendered ``<main>``. Accepting that chrome as
# authoritative notice text would baseline an uninspected notice, so the
# leading region of a candidate body is screened for these signatures.
FINRA_NON_NOTICE_LEAD_CHARS = 400
FINRA_NOTICE_SUBSTANTIAL_CHARS = 1500
FINRA_NON_NOTICE_PAGE_PATTERN = re.compile(
    r"(?:"
    r"access\s+(?:to\s+[\w\s]{0,40}\s+)?(?:is\s+|has\s+been\s+)?deni(?:ed|al)"
    r"|access\s+restricted|restricted\s+access"
    r"|(?:your\s+)?request\s+(?:was\s+|has\s+been\s+|is\s+)?(?:blocked|denied|rejected)"
    r"|you\s+(?:do\s+not|don't)\s+have\s+(?:permission|access)"
    r"|you\s+are\s+not\s+authoriz(?:ed|ation)"
    r"|(?:page|file|content|document)\s+(?:you\s+requested\s+)?"
    r"(?:could\s+not\s+be\s+found|was\s+not\s+found|not\s+found|is\s+unavailable)"
    r"|\b40[0-9]\b\s*(?:[-:|\u2013\u2014]|\berror\b|\bforbidden\b|\bnot\s+found\b)"
    r"|\berror\s*[-:|]?\s*40[0-9]\b|\bhttp\s+40[0-9]\b|\b403\s*forbidden\b"
    r"|(?:verify|confirm)\s+(?:that\s+)?you\s+are\s+(?:a\s+)?human"
    r"|\bcaptcha\b|security\s+check|are\s+you\s+a\s+robot"
    r"|checking\s+your\s+browser|unusual\s+traffic|automated\s+traffic"
    r"|enable\s+(?:javascript|cookies)"
    r"|(?:log|sign)\s*in\s+to\s+(?:continue|view|access|proceed|read)"
    r"|(?:login|log\s*in|sign[-\s]?in|authentication)\s+(?:is\s+)?required"
    r"|session\s+(?:has\s+)?(?:expired|timed\s+out)"
    r"|(?:service|site|page)\s+(?:is\s+)?(?:temporarily\s+)?unavailable"
    r"|rate\s+limit(?:ed|\s+exceeded)?"
    r"|maintenance\s+mode|under\s+maintenance"
    r")",
    re.IGNORECASE,
)
# Structure a real FINRA notice body carries. Used only as a safety valve so a
# long, genuinely structured notice that happens to quote one of the phrases
# above is not mistaken for an error page.
FINRA_NOTICE_STRUCTURE_PATTERN = re.compile(
    r"(?:\bsuggested\s+routing\b|\bkey\s+topics?\b|\bnotice\s+type\b"
    r"|\breferenced\s+rules?\b|\baction\s+requested\b"
    r"|\bquestions?\s+(?:concerning|regarding|about)\s+this\s+notice\b"
    r"|\b(?:regulatory|information)\s+notice\s+\d{2}-\d+\b"
    r"|\bmember\s+firms?\b|\bbroker[-\s]?dealers?\b|\bfinra\s+rule\s*\d)",
    re.IGNORECASE,
)


def _is_finra_non_notice_page_text(text: str) -> bool:
    """Return True when candidate text is error/challenge/login chrome."""
    if not text:
        return True
    if not FINRA_NON_NOTICE_PAGE_PATTERN.search(text[:FINRA_NON_NOTICE_LEAD_CHARS]):
        return False
    # A substantial, structurally recognisable notice that merely mentions one
    # of these phrases is still a notice.
    return not (
        len(text) >= FINRA_NOTICE_SUBSTANTIAL_CHARS
        and FINRA_NOTICE_STRUCTURE_PATTERN.search(text)
    )


# Some genuinely published FINRA notices carry no retrievable text. The live
# 1983 notices are the standing example: /rules-guidance/notices/83-16 renders
# a normal notice page whose body is the tombstone "NOT AVAILABLE AT THIS
# TIME" followed by page furniture ("Notice Comments"). That is not an error,
# a challenge, or a denial -- the source answers successfully and declares that
# the text does not exist online -- but it is equally not authoritative notice
# content, and hashing it would baseline a placeholder as if the notice had
# been read.
FINRA_NOTICE_UNAVAILABLE_PATTERN = re.compile(
    r"(?:"
    r"\bnot\s+available\s+(?:at\s+this\s+time|online|electronically|"
    r"in\s+(?:an?\s+)?(?:electronic|digital)\s+form(?:at)?|"
    r"(?:from|through|on)\s+(?:this\s+)?(?:site|website|page))"
    r"|\bunavailable\s+at\s+this\s+time\b"
    r"|\bnot\s+(?:currently|presently)\s+available\b"
    r"|\bno\s+longer\s+available\s+(?:online|electronically|on\s+this\s+site)\b"
    r"|\b(?:text|content|document|notice|version)\s+(?:of\s+this\s+notice\s+)?"
    r"(?:is\s+|are\s+)?(?:not\s+available|unavailable)\b"
    r")",
    re.IGNORECASE,
)


def _finra_notice_unavailable_reason(text: str) -> Optional[str]:
    """Return the tombstone phrase when a candidate body declares no content.

    Uses the same two-gate shape as the error/challenge screen: the
    declaration has to appear in the leading region, and a substantial,
    structurally recognisable notice that merely *mentions* unavailability
    (for example "the data are not available at this time") is still a notice.
    """
    if not text:
        return None
    match = FINRA_NOTICE_UNAVAILABLE_PATTERN.search(
        text[:FINRA_NON_NOTICE_LEAD_CHARS]
    )
    if not match:
        return None
    if (
        len(text) >= FINRA_NOTICE_SUBSTANTIAL_CHARS
        and FINRA_NOTICE_STRUCTURE_PATTERN.search(text)
    ):
        return None
    return match.group(0)


# Federal Register source documents interleave operative rule text with
# footnote blocks, bibliographies, and literature reviews, and a document can
# run to hundreds of thousands of characters. Position is not evidence of
# relevance -- operative requirements routinely appear late -- so no part of a
# document is discarded. Instead each candidate match is judged by the language
# immediately around it: an occurrence only stops counting when its context is
# unambiguously bibliographic AND carries no obligation language.
# Kept as a compatibility constant for callers that imported the old tuning
# knob.  Reference classification no longer uses a fixed-size window.
REFERENCE_CONTEXT_WINDOW_CHARS = 200

OPERATIVE_LANGUAGE_PATTERN = re.compile(
    r"\b(?:must|shall|may\s+not|is\s+required|are\s+required"
    r"|(?:would|will)\s+be\s+required|required\s+to"
    r"|requires?\s+(?:that|each|every|any|all|a|an|the)\b"
    r"|prohibit(?:s|ed|ing|ion)?|mandat(?:e|es|ed|ory)"
    r"|propos(?:e|es|ed|ing)\s+to\s+(?:require|amend|add|adopt|prohibit)"
    r"|obligated\s+to|obligations?\s+to|responsible\s+(?:for|to)"
    r"|responsibilit(?:y|ies)\s+to|dut(?:y|ies)\s+to"
    r"|compliance\s+date|effective\s+date)\b",
    re.IGNORECASE,
)

# Shared citation vocabulary. A research/study *subject* paired with a
# reporting verb marks a citing clause; the same building blocks drive both the
# reference-only detector and the citation-subject clause boundary so the two
# always agree on what counts as a citation.
_RESEARCHER_SUBJECT_NOUN = (
    r"(?:researchers?|scholars?|commentators?|academics?|economists?)"
)
_CITATION_REPORTING_VERB = (
    r"(?:discuss(?:es|ed)?|survey(?:s|ed)?|examin(?:e|es|ed)|analy[sz](?:e|es|ed)|"
    r"argu(?:e|es|ed)|find|finds|found|show(?:s|ed|n)?|observ(?:e|es|ed)|"
    r"note[sd]?|conclud(?:e|es|ed)|report(?:s|ed)?|document(?:s|ed)?|"
    r"suggest(?:s|ed)?|demonstrat(?:e|es|ed)|review(?:s|ed)?|propos(?:e|es|ed)|"
    r"describ(?:e|es|ed)|estimat(?:e|es|ed)|highlight(?:s|ed)?|explor(?:e|es|ed)|"
    r"present(?:s|ed)?|investigat(?:e|es|ed)|consider(?:s|ed)?|debat(?:e|es|ed)|"
    r"stud(?:y|ies|ied)|posit(?:s|ed)?|contend(?:s|ed)?|assess(?:es|ed)?|"
    r"evaluat(?:e|es|ed)|caution(?:s|ed)?|warn(?:s|ed)?|emphasiz(?:e|es|ed)|"
    r"theoriz(?:e|es|ed)|publish(?:es|ed)?)"
)
# A parenthetical publication year ("(2026)") is a strong author-date citation
# signal. Paired with a reporting verb it marks a citing clause even for a
# single lowercase surname the casing heuristic cannot see ("... and jones
# (2026) surveys artificial intelligence ...").
_CITATION_YEAR_PAREN = r"\(\d{4}[a-z]?\)"
_CITATION_AUTHOR_YEAR_SUBJECT = (
    r"[\w.'-]+(?:\s+(?:and|&)\s+[\w.'-]+)?(?:\s+et\s+al\.)?\s*"
    + _CITATION_YEAR_PAREN
)
_CITATION_RESEARCH_NOUN = (
    r"(?:" + _RESEARCHER_SUBJECT_NOUN + r"|analysts?|authors?|"
    r"stud(?:y|ies)|papers?|articles?|surveys?|literature|working\s+papers?)"
)
_CITATION_DETERMINER = (
    r"(?:the\s+|a\s+|an\s+|one\s+|another\s+|several\s+|recent\s+|prior\s+|"
    r"earlier\s+|many\s+|some\s+|numerous\s+|academic\s+|empirical\s+|"
    r"various\s+|two\s+|three\s+|four\s+)*"
)

# Proper-name attribution. A citation can name its source *before* the claim
# ("According to Jones (2026), artificial intelligence affects capital
# markets.") or trail it in parentheses ("... capital markets (Jones, 2026).").
# Neither shape has a reporting verb after the author-date token, so the
# author-date branch above cannot see them and the mention was read as the
# document's own assertion.
#
# Casing is unavailable (classification text is lowercased), so a proper name
# is recognised structurally: an attribution lead plus a parenthetical year, or
# a parenthetical "<name>, <year>" pair. The trailing parenthetical form
# deliberately *requires* the comma, because "(September 2026)" and
# "(effective 2027)" are dates, not citations.
_CITATION_NAME_TOKEN = r"[a-z][\w'\u2019-]*"
_CITATION_NAME_LIST = (
    _CITATION_NAME_TOKEN
    + r"(?:\s+(?:and|&)\s+" + _CITATION_NAME_TOKEN + r")?"
    + r"(?:\s*,?\s*et\s+al\.?)?"
)
_CITATION_ATTRIBUTION_VERB = (
    r"(?:reported|noted|observed|described|documented|discussed|shown|argued|"
    r"explained|summari[sz]ed|estimated|surveyed|reviewed|cited|quoted)"
)
_CITATION_ATTRIBUTION_LEAD = (
    r"(?:according\s+to|(?:as\s+)?" + _CITATION_ATTRIBUTION_VERB + r"\s+(?:in|by)"
    r"|as\s+cited\s+in|citing)"
)
_CITATION_ATTRIBUTION_SUBJECT = (
    r"(?:"
    # "according to Jones (2026)", "as reported by Smith and Lee (2025)",
    # "per Jones et al. (2026)".
    + r"(?:" + _CITATION_ATTRIBUTION_LEAD + r"|per)\s+"
    + _CITATION_NAME_LIST + r"\s*" + _CITATION_YEAR_PAREN
    + r"|"
    # "according to a recent study", "as documented in the literature".
    + _CITATION_ATTRIBUTION_LEAD + r"\s+" + _CITATION_DETERMINER
    + _CITATION_RESEARCH_NOUN
    + r")"
)
# Trailing parenthetical author-date: "(Jones, 2026)", "(Jones and Lee, 2026)",
# "(Jones et al., 2026)", "(Jones, 2026, p. 14)".
_CITATION_PARENTHETICAL = (
    r"\(\s*" + _CITATION_NAME_TOKEN
    + r"(?:\s+(?:and|&)\s+" + _CITATION_NAME_TOKEN + r")?"
    + r"(?:\s*,?\s*et\s+al\.?)?"
    + r"\s*,\s*(?:19|20)\d{2}[a-z]?"
    + r"(?:\s*[,;:]\s*(?:pp?\.\s*)?\d[\d\u2013-]*)?\s*\)"
)

REFERENCE_ONLY_PATTERN = re.compile(
    r"(?:\bsee\s+(?:also|generally|supra|infra)\b|\bsee,\s*e\.g\.|\bsupra\b|\bid\.\s|\bibid\b"
    r"|\bcf\.\s|\bet\s+al\.|\bavailable\s+at\b|https?://|\bwww\.|\bcit(?:ed|ing|ation)\b"
    r"|\b(?:an|another|one|a|the|this|these|those|recent|prior|earlier|academic|empirical|several)\s+"
    r"[a-z0-9 ,'-]{0,26}?(?:study|studies|paper|papers|article|articles|survey|working\s+paper)\b"
    r"|\bstudies\s+(?:have\s+)?(?:found|find|show|shown|suggest|document)"
    r"|\b" + _RESEARCHER_SUBJECT_NOUN + r"\b|\bthe\s+literature\b|\bjournal\b|\bworking\s+paper\b"
    # A researcher/study subject followed by a reporting verb is a citing
    # clause even without an article ("researchers document ...", "scholars
    # examine ...", "studies survey ..."). This mirrors the citation-subject
    # clause boundary so a clause it splits off is recognised here too.
    r"|\b" + _CITATION_RESEARCH_NOUN + r"\s+(?:et\s+al\.\s+)?(?:have\s+|has\s+|also\s+)?"
    + _CITATION_REPORTING_VERB
    # An author-date citation: a parenthetical year followed by a reporting
    # verb ("(2026) surveys ..."). Kept in sync with the citation-subject
    # clause boundary so a clause it splits off is recognised here too.
    + r"|" + _CITATION_YEAR_PAREN + r"\s+(?:have\s+|has\s+|also\s+)?"
    + _CITATION_REPORTING_VERB
    # Proper-name attribution, leading and trailing forms.
    + r"|\b" + _CITATION_ATTRIBUTION_SUBJECT
    + r"|" + _CITATION_PARENTHETICAL + r")",
    re.IGNORECASE,
)

# Anchored form used to re-attach a trailing author-date parenthetical to the
# clause it annotates after clause punctuation would have split it off.
TRAILING_PARENTHETICAL_CITATION_PATTERN = re.compile(
    r"\s*" + _CITATION_PARENTHETICAL, re.IGNORECASE
)

# Federal Register raw text separates footnote blocks from body text with a run
# of hyphens. Context must stop at that boundary, otherwise the citations in an
# adjacent footnote block would be read as the context of operative body text.
FOOTNOTE_BLOCK_DELIMITER_PATTERN = re.compile(r"-{5,}")

# A match's evidence is the complete sentence/clause that actually contains it.
# Require whitespace/end after sentence punctuation so periods in URLs and
# decimal values do not truncate the containing sentence prematurely. Federal
# Register footnote markers sit between the punctuation and its whitespace
# (for example ``tools.\451\ ``), so they are part of the boundary too.
SENTENCE_BOUNDARY_PATTERN = re.compile(
    r"[.;!?](?=(?:\s|\\\d+\\(?:\s|$)|$))"
)

# Obligation language binds the clause it sits in, not the whole sentence. A
# sentence such as "The Commission proposes to amend quarterly report
# deadlines, and a recent working paper on artificial intelligence is available
# at ..." carries a real obligation about reporting deadlines and a separate
# citation clause that merely names an AI paper. Splitting the sentence at
# clause punctuation (and at the conjunctions/relative pronouns that introduce
# a new clause) keeps the obligation attached to the clause it governs.
CLAUSE_BOUNDARY_PATTERN = re.compile(
    r"[,:()\[\]]|--+|\u2014|\u2013|\band\s+(?=(?:a|an|the|this|these|those)\b)",
    re.IGNORECASE,
)

# Citation/Latin abbreviations whose trailing period is part of the token, not
# a sentence terminator. Classification text is lowercased before it reaches
# the boundary scan, so these are matched in lowercase. "et al." is the
# load-bearing case: splitting the sentence at its period detaches an
# author-list citation from the artificial-intelligence mention it annotates
# and lets an unrelated operative duty ("Members must file annual reports")
# promote the citation to HIGH.
_CITATION_ABBREVIATION_TAILS = (
    "et al",
    "et seq",
    "e.g",
    "i.e",
    "cf",
    "ibid",
    "viz",
)

# A new *citation subject* opens a fresh clause even when only a plain
# conjunction separates it from a preceding operative duty about a different
# subject. Capitalization is unavailable (the text is lowercased), so the two
# recognised shapes key on citation markers instead of proper-noun casing:
#   * "<conj> <name words> et al." -- an author-list citation.
#   * "<conj> <research-noun subject> <reporting verb>" -- a study/researcher
#     led clause ("and researchers document ...", "because scholars observe").
# A bare coordinated predicate ("and govern", "and conduct annual studies") is
# NOT a new subject: its verb (or verb+object) follows the conjunction directly
# with no citing subject, so it stays welded to the operative duty and is
# preserved as HIGH. The reporting-verb and research-noun vocabularies are the
# shared blocks defined next to REFERENCE_ONLY_PATTERN.
_CITATION_CONJUNCTION = (
    r"(?:and|but|while|whereas|although|though|because|since|as|when|where)"
)
CITATION_SUBJECT_BOUNDARY_PATTERN = re.compile(
    r"(?:"
    r"\b" + _CITATION_CONJUNCTION + r"\s+"
    r"(?="
    r"(?:[\w.'-]+(?:\s+[\w.'-]+){0,3}?\s+et\s+al\.)"
    r"|"
    r"(?:" + _CITATION_DETERMINER
    + _CITATION_RESEARCH_NOUN + r"\s+(?:et\s+al\.\s+)?(?:have\s+|has\s+|also\s+)?"
    + _CITATION_REPORTING_VERB + r")"
    r"|"
    # "<name(s)> (2026) surveys ..." -- an author-date citation whose only
    # casing cue is unavailable in the lowercased text; the parenthetical year
    # plus a reporting verb identifies the citing subject.
    r"(?:" + _CITATION_AUTHOR_YEAR_SUBJECT
    + r"\s+(?:have\s+|has\s+|also\s+)?" + _CITATION_REPORTING_VERB + r")"
    r")"
    r"|"
    # A proper-name attribution ("..., according to Jones (2026), artificial
    # intelligence ...") also opens a citing clause. It is introduced by a
    # conjunction or by clause punctuation, and the comma that closes the
    # attribution must not trim the attribution off the claim it governs, so
    # the boundary is placed at the attribution itself.
    r"(?:(?<=[,;:(])\s*|\b" + _CITATION_CONJUNCTION + r"\s*,?\s+)"
    r"(?=" + _CITATION_ATTRIBUTION_SUBJECT + r")"
    r")",
    re.IGNORECASE,
)

# Electronic recordkeeping is intentionally implemented as readable semantic
# checks instead of a single configuration regex.  The obligation must connect
# a recordkeeping noun and a storage/maintenance action to electronic or digital
# storage in the same sentence/clause.
RECORDKEEPING_NOUN = (
    r"(?:records?|record[-\s]?keeping|books\s+and\s+records)"
)
RECORDKEEPING_ACTION = (
    r"(?:maintain(?:ed|s|ing)?|retain(?:ed|s|ing)?|"
    r"stor(?:e|ed|es|ing|age)|keep|keeps|kept|keeping|"
    r"preserv(?:e|ed|es|ing|ation)|archiv(?:e|ed|es|ing|al)|"
    r"transition(?:ed|s|ing)?|convert(?:ed|s|ing)?|"
    r"migrat(?:e|ed|es|ing)|retention)"
)
ELECTRONIC_STORAGE_LANGUAGE = (
    r"(?:electronically|digitally|machine[-\s]?readable|"
    r"in\s+(?:an?\s+)?(?:electronic|digital)\s+(?:form|format)|"
    r"(?:electronic|digital)\s+"
    r"(?:records?|record[-\s]?keeping|books\s+and\s+records|"
    r"systems?|storage|media|form|format))"
)
ELECTRONIC_RECORDKEEPING_NOUN = (
    r"(?:electronic|digital)\s+"
    r"(?:records?|record[-\s]?keeping|books\s+and\s+records|systems?)"
)
RECORDKEEPING_OBLIGATION = (
    r"(?:must|shall|is\s+required\s+to|are\s+required\s+to|"
    r"was\s+required\s+to|were\s+required\s+to|would\s+require|"
    r"will\s+require|required\s+to|requires?\s+to|"
    r"obligated\s+to|obligation\s+to|duty\s+to|"
    r"responsible\s+(?:for|to)|mandated\s+to)"
)
ELECTRONIC_RECORDKEEPING_PATTERNS = (
    re.compile(
        rf"\b{RECORDKEEPING_NOUN}\b"
        rf"(?:(?![.!?;]).){{0,100}}?\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,50}}?"
        rf"(?:to\s+)?(?:be\s+)?\b{RECORDKEEPING_ACTION}\b"
        rf"(?:(?![.!?;]).){{0,35}}?\b{ELECTRONIC_STORAGE_LANGUAGE}\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,45}}?"
        rf"(?:to\s+)?(?:be\s+)?\b{RECORDKEEPING_ACTION}\b"
        rf"(?:(?![.!?;]).){{0,35}}?\b{RECORDKEEPING_NOUN}\b"
        rf"(?:(?![.!?;]).){{0,35}}?\b{ELECTRONIC_STORAGE_LANGUAGE}\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,45}}?"
        rf"(?:to\s+)?(?:be\s+)?\b{RECORDKEEPING_ACTION}\b"
        rf"(?:(?![.!?;]).){{0,35}}?\b{ELECTRONIC_RECORDKEEPING_NOUN}\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,45}}?\b{RECORDKEEPING_NOUN}\b"
        rf"(?:(?![.!?;]).){{0,45}}?"
        rf"(?:to\s+)?(?:be\s+)?\b{RECORDKEEPING_ACTION}\b"
        rf"(?:(?![.!?;]).){{0,35}}?\b{ELECTRONIC_STORAGE_LANGUAGE}\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b{ELECTRONIC_RECORDKEEPING_NOUN}\b"
        rf"(?:(?![.!?;]).){{0,60}}?\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,45}}?"
        rf"(?:to\s+)?(?:be\s+)?"
        rf"\b(?:{RECORDKEEPING_ACTION}|implement(?:ed|s|ing)?)\b",
        re.IGNORECASE,
    ),
    # The existing electronic-storage state can precede the operative duty:
    # "Records maintained electronically must be retained."  Keep both the
    # preceding storage action and the following required action in the same
    # clause so an unrelated electronic noun cannot satisfy the rule.
    re.compile(
        rf"\b{RECORDKEEPING_NOUN}\b"
        rf"(?:(?![.!?;]).){{0,45}}?\b{RECORDKEEPING_ACTION}\b"
        rf"(?:(?![.!?;]).){{0,35}}?\b{ELECTRONIC_STORAGE_LANGUAGE}\b"
        rf"(?:(?![.!?;]).){{0,45}}?\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,35}}?"
        rf"\b(?:{RECORDKEEPING_ACTION}|implement(?:ed|s|ing)?)\b",
        re.IGNORECASE,
    ),
    # The electronic term can modify the storage verb instead of following it:
    # "Records must be electronically stored", "Firms must digitally archive
    # records". Every other pattern requires the electronic language *after*
    # the action, so this mandatory form was read as no obligation at all.
    re.compile(
        rf"\b{RECORDKEEPING_NOUN}\b"
        rf"(?:(?![.!?;]).){{0,100}}?\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,50}}?"
        rf"(?:to\s+)?(?:be\s+)?\b{ELECTRONIC_STORAGE_LANGUAGE}\b"
        rf"\s+(?:\w+\s+){{0,2}}?\b{RECORDKEEPING_ACTION}\b",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\b{RECORDKEEPING_OBLIGATION}\b"
        rf"(?:(?![.!?;]).){{0,45}}?"
        rf"(?:to\s+)?(?:be\s+)?\b{ELECTRONIC_STORAGE_LANGUAGE}\b"
        rf"\s+(?:\w+\s+){{0,2}}?\b{RECORDKEEPING_ACTION}\b"
        rf"(?:(?![.!?;]).){{0,35}}?\b{RECORDKEEPING_NOUN}\b",
        re.IGNORECASE,
    ),
)
OPTIONAL_OR_NEGATED_RECORDKEEPING = re.compile(
    r"\b(?:optional|optionally|permitted|may|can|could|might|"
    r"not\s+required|need\s+not|not\s+obligated|not\s+mandatory|"
    r"must\s+not|shall\s+not)\b",
    re.IGNORECASE,
)

# A permissive modal only defeats a storage mandate when it governs the
# *storage predicate*. "Records that may contain customer information must be
# retained electronically" is a mandate: "may" governs "contain", not the
# retention duty, and reading it as permissive turned a real electronic
# recordkeeping requirement into NOISE. "Records may be retained
# electronically" is genuinely permissive and must stay rejected.
PERMISSIVE_MODAL_PATTERN = re.compile(r"\b(?:may|can|could|might)\b", re.IGNORECASE)
STORAGE_PREDICATE_AFTER_MODAL = re.compile(
    rf"\s*(?:not\s+)?(?:also\s+)?(?:be\s+|been\s+|being\s+)?"
    rf"(?:\w+ly\s+)?(?:to\s+)?(?:be\s+)?"
    rf"(?:{RECORDKEEPING_ACTION}|{ELECTRONIC_STORAGE_LANGUAGE})\b",
    re.IGNORECASE,
)


def _mask_unbound_permissive_modals(clause: str) -> str:
    """Blank permissive modals that do not govern a storage predicate."""
    masked = clause
    for match in PERMISSIVE_MODAL_PATTERN.finditer(clause):
        if STORAGE_PREDICATE_AFTER_MODAL.match(clause, match.end()):
            continue
        masked = (
            masked[: match.start()]
            + " " * (match.end() - match.start())
            + masked[match.end():]
        )
    return masked

# Defect: a mandatory-sounding match can end exactly at the electronic term and
# hide the alternative that follows it ("Records must be retained either
# electronically or in paper form"). The complete local clause has to be read,
# because an electronic/paper disjunction means paper storage is still allowed
# and the clause is therefore not an electronic recordkeeping mandate.
ELECTRONIC_STORAGE_MENTION = re.compile(
    rf"\b{ELECTRONIC_STORAGE_LANGUAGE}\b",
    re.IGNORECASE,
)
PAPER_STORAGE_MENTION = re.compile(
    r"\b(?:paper|physical|hard[-\s]?copy|hardcopy|printed)\b",
    re.IGNORECASE,
)
# Wording between the electronic and paper terms that makes paper an accepted
# alternative rather than a replaced predecessor. Exception connectors such as
# "unless"/"except" introduce a permitted paper fallback ("maintained
# electronically unless retained in paper form"), so paper storage is still
# allowed and the clause is not an electronic-only mandate.
PAPER_ALTERNATIVE_CONNECTOR = re.compile(
    r"\b(?:or|and/or|either|alternativ\w*|option(?:al|ally|s)?|"
    r"may|might|can|could|permitted|permissible|elect|election|"
    r"choose|choice|whichever|unless|except(?:ing|ed)?)\b",
    re.IGNORECASE,
)
# Wording that shows paper is being displaced, so the electronic duty stands.
PAPER_REPLACEMENT_CONNECTOR = re.compile(
    r"\b(?:rather\s+than|instead\s+of|in\s+lieu\s+of|as\s+opposed\s+to|"
    r"in\s+place\s+of|replac\w*|supersed\w*|discontinu\w*|eliminat\w*|"
    r"prohibit\w*|no\s+longer|not|never|cannot|nor)\b",
    re.IGNORECASE,
)


def _clause_permits_paper_alternative(clause: str) -> bool:
    """Return True when a clause offers paper as an alternative to electronic.

    Both orderings are semantically identical and must be rejected:
    "retained either electronically or in paper form" and "retained either in
    paper form or electronically". A clause that *replaces* paper with an
    electronic duty ("maintained electronically rather than in paper form",
    "must be maintained electronically and not in paper form") is a genuine
    electronic-only mandate and is preserved.
    """
    electronic_spans = [match.span() for match in ELECTRONIC_STORAGE_MENTION.finditer(clause)]
    if not electronic_spans:
        return False

    for paper_match in PAPER_STORAGE_MENTION.finditer(clause):
        paper_start, paper_end = paper_match.span()
        for electronic_start, electronic_end in electronic_spans:
            if electronic_end <= paper_start:
                connector = clause[electronic_end:paper_start]
            elif paper_end <= electronic_start:
                connector = clause[paper_end:electronic_start]
            else:
                continue

            if PAPER_REPLACEMENT_CONNECTOR.search(connector):
                continue
            if PAPER_ALTERNATIVE_CONNECTOR.search(connector):
                return True

    return False


# A paper *prohibition* is the opposite of a paper alternative: it forbids
# paper storage, which reinforces (rather than negates) an electronic-only
# duty. The negation words that express it ("cannot", "may not", "must not",
# "shall not") also appear in OPTIONAL_OR_NEGATED_RECORDKEEPING, where they are
# meant to catch a negated *electronic* duty. When such a negation is bound to
# the paper term it must not be read as negating the electronic obligation, so
# the prohibition phrase is masked out before the optional/negated check runs.
_PAPER_TERM = (
    r"(?:paper|physical\s+(?:form|copy|copies|record\w*|storage)|"
    r"hard[-\s]?cop(?:y|ies)|hardcop(?:y|ies)|printed\s+(?:form|record\w*))"
)
PAPER_PROHIBITION_PATTERN = re.compile(
    r"(?:"
    r"\b(?:can\s*not|cannot|may\s+not|must\s+not|shall\s+not|should\s+not|"
    r"will\s+not|would\s+not|prohibited\s+from|barred\s+from|precluded\s+from|"
    r"forbidden\s+(?:from|to))"
    r"\s+(?:\w+\s+){0,4}?(?:on\s+|in\s+|to\s+|using\s+|via\s+|onto\s+)?" + _PAPER_TERM +
    r"|"
    + _PAPER_TERM + r"\s+(?:\w+\s+){0,3}?"
    r"(?:is|are|be|being|remains?|may|shall|can|will)?\s*"
    r"(?:not\s+)?"
    r"(?:prohibited|forbidden|barred|impermissible|disallowed|precluded|"
    r"not\s+permitted|not\s+allowed|no\s+longer\s+(?:permitted|allowed|accepted))"
    r")",
    re.IGNORECASE,
)


def _mask_paper_prohibition(clause: str) -> str:
    """Blank out explicit paper-prohibition phrases in a clause.

    A prohibition such as "records may not be retained on paper and must be
    maintained electronically" carries the negation on *paper*, not on the
    electronic duty. Removing the prohibition phrase keeps the affirmative
    electronic obligation intact while preventing its paper-bound negation from
    being mistaken for a negated electronic duty.
    """
    return PAPER_PROHIBITION_PATTERN.sub(" ", clause)

# Configure logging
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(verbose: bool = False) -> logging.Logger:
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if os.environ.get("REGULATORY_MONITOR_DEBUG") else (
        logging.INFO if verbose else logging.WARNING
    )

    logging.basicConfig(
        level=level,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    return logging.getLogger(__name__)


logger = logging.getLogger(__name__)


class FederalRegisterPaginationError(RuntimeError):
    """Raised when a paginated Federal Register response cannot be completed."""


class RequiredSourceTextError(RuntimeError):
    """Raised when authoritative text required for classification is unavailable."""


class FinraListingError(RuntimeError):
    """Raised when the FINRA notice listing cannot be fetched or verified."""


class FinraNoticeUnavailableError(RuntimeError):
    """Raised when FINRA answers successfully but declares no notice text.

    Deliberately *not* a :class:`RequiredSourceTextError`. A denial, challenge,
    or error page means the notice exists and we failed to read it, which is an
    integrity failure and fails the run closed. A tombstone means the source
    itself states there is no text to read (the live 1983 notices), which is a
    permanent, correct answer: failing the run closed on it would take FINRA
    monitoring down forever, so the notice is excluded from the baseline and
    reported separately while the source run completes.
    """


def _prepare_classification_text(text: str) -> str:
    """Normalize escaped line breaks in source text used for classification.

    Federal Register raw text sometimes carries literal ``\\n``/``\\r`` escape
    sequences that would otherwise weld two words together and hide a match.
    No part of the document is dropped: relevance is decided by context, not by
    position (see ``_is_reference_only_occurrence``).
    """
    text = text or ""
    return text.replace("\\r", " ").replace("\\n", " ")


def _is_citation_abbreviation_boundary(text: str, index: int) -> bool:
    """Return True when the punctuation at ``index`` is an abbreviation dot.

    Only ``.`` can be an abbreviation dot; ``;``/``!``/``?`` are always real
    boundaries. The dot is treated as part of a token (not a sentence
    terminator) when the text ending at it closes a known citation/Latin
    abbreviation that stands as its own token (e.g. the period in "et al.").

    Only the few characters immediately before the dot are inspected. The
    previous implementation lowercased ``text[:index]`` on every call, which is
    O(document) per boundary and made boundary indexing quadratic on a
    several-hundred-kilobyte Federal Register document.
    """
    if index < 0 or index >= len(text) or text[index] != ".":
        return False
    for abbr in _CITATION_ABBREVIATION_TAILS:
        token_start = index - len(abbr)
        if token_start < 0:
            continue
        if text[token_start:index].lower() != abbr:
            continue
        if token_start == 0 or not text[token_start - 1].isalnum():
            return True
    return False


def _real_sentence_boundaries(text: str, lo: int, hi: int):
    """Yield sentence-boundary matches in ``text[lo:hi]`` minus abbreviation dots."""
    for boundary in SENTENCE_BOUNDARY_PATTERN.finditer(text, lo, hi):
        if _is_citation_abbreviation_boundary(text, boundary.start()):
            continue
        yield boundary


# Number of distinct classification texts whose boundary offsets are kept
# resident. A document is scanned by ~35 classification patterns and ~24
# control keywords, and every match of every one of them needs the same
# boundaries, so the index has to survive across those calls. Four slots cover
# a title plus a body in both ``classify_regulatory_relevance`` and
# ``find_affected_controls_by_keywords`` without pinning many large documents
# in memory.
_BOUNDARY_INDEX_CACHE_SIZE = 8

# Diagnostic counter: how many times a boundary index was actually built. The
# performance regression asserts on this instead of on wall-clock alone, so the
# "index once, look up per match" property is machine-independent.
_BOUNDARY_INDEX_BUILDS = 0


class _TextBoundaryIndex:
    """Pre-computed footnote/sentence/clause boundary offsets for one text.

    Evidence scoping used to rescan the document for every candidate match:
    each occurrence walked every preceding footnote delimiter and every
    preceding sentence terminator from the start of the document. That is
    O(document x matches) and cost ~60s for a 790k-character body carrying 100
    bibliographic AI mentions.

    The boundaries are a property of the *text*, not of the match, so they are
    collected in one linear pass per pattern and each occurrence then resolves
    its own span with binary search (O(log n)). Semantics are unchanged: the
    same boundary positions are produced, only found differently.
    """

    __slots__ = (
        "length",
        "footnote_starts",
        "footnote_ends",
        "sentence_positions",
        "clause_starts",
        "clause_ends",
        "citation_starts",
        "citation_ends",
    )

    def __init__(self, text: str) -> None:
        global _BOUNDARY_INDEX_BUILDS
        _BOUNDARY_INDEX_BUILDS += 1

        self.length = len(text)
        self.footnote_starts: list[int] = []
        self.footnote_ends: list[int] = []
        for match in FOOTNOTE_BLOCK_DELIMITER_PATTERN.finditer(text):
            self.footnote_starts.append(match.start())
            self.footnote_ends.append(match.end())

        self.sentence_positions: list[int] = [
            boundary.start()
            for boundary in _real_sentence_boundaries(text, 0, len(text))
        ]

        self.clause_starts: list[int] = []
        self.clause_ends: list[int] = []
        for match in CLAUSE_BOUNDARY_PATTERN.finditer(text):
            self.clause_starts.append(match.start())
            self.clause_ends.append(match.end())

        self.citation_starts: list[int] = []
        self.citation_ends: list[int] = []
        for match in CITATION_SUBJECT_BOUNDARY_PATTERN.finditer(text):
            self.citation_starts.append(match.start())
            self.citation_ends.append(match.end())

    # -- span helpers -----------------------------------------------------
    def _footnote_segment(self, start: int, end: int) -> tuple[int, int]:
        """Return the footnote-delimited segment containing ``[start, end)``."""
        index = bisect_right(self.footnote_ends, start) - 1
        segment_start = self.footnote_ends[index] if index >= 0 else 0
        index = bisect_left(self.footnote_starts, end)
        segment_end = (
            self.footnote_starts[index]
            if index < len(self.footnote_starts)
            else self.length
        )
        return segment_start, segment_end

    def sentence_span(self, text: str, start: int, end: int) -> tuple[int, int]:
        segment_start, segment_end = self._footnote_segment(start, end)

        positions = self.sentence_positions
        index = bisect_left(positions, start) - 1
        if index >= 0 and positions[index] >= segment_start:
            segment_start = positions[index] + 1
        # A terminator sitting immediately before the match (no separating
        # whitespace) is a boundary for this occurrence even though the
        # document-wide scan does not treat it as one.
        if (
            start - 1 >= segment_start
            and start - 1 >= 0
            and text[start - 1] in ".;!?"
            and not _is_citation_abbreviation_boundary(text, start - 1)
        ):
            segment_start = start

        following = None
        index = bisect_left(positions, end)
        if index < len(positions) and positions[index] < segment_end:
            following = positions[index]
        tail = segment_end - 1
        if (
            tail >= end
            and tail < self.length
            and text[tail] in ".;!?"
            and not _is_citation_abbreviation_boundary(text, tail)
        ):
            following = tail if following is None else min(following, tail)
        if following is not None:
            segment_end = following

        return segment_start, segment_end

    def _last_boundary_end(
        self,
        starts: list[int],
        ends: list[int],
        lower: int,
        upper: int,
    ) -> Optional[int]:
        """End of the last match starting at/after ``lower`` and ending by ``upper``."""
        index = bisect_right(ends, upper) - 1
        if index < 0 or starts[index] < lower:
            return None
        return ends[index]

    def _first_boundary_start(
        self,
        starts: list[int],
        ends: list[int],
        lower: int,
        upper: int,
    ) -> Optional[int]:
        """Start of the first match beginning at/after ``lower``, ending by ``upper``."""
        index = bisect_left(starts, lower)
        if index >= len(starts) or ends[index] > upper:
            return None
        return starts[index]

    def clause_span(
        self,
        start: int,
        end: int,
        sentence_start: int,
        sentence_end: int,
    ) -> tuple[int, int]:
        clause_start, clause_end = sentence_start, sentence_end

        citation_start = self._last_boundary_end(
            self.citation_starts, self.citation_ends, sentence_start, start
        )
        if citation_start is not None:
            # A citation subject is a single clause. Punctuation inside it (a
            # parenthetical year "(2026)", an internal comma) must not trim its
            # markers ("et al.") off, so only clause boundaries at or before
            # the nearest citation subject apply.
            preceding_clause = self._last_boundary_end(
                self.clause_starts, self.clause_ends, sentence_start, citation_start
            )
            clause_start = max(
                sentence_start,
                citation_start,
                preceding_clause if preceding_clause is not None else sentence_start,
            )
        else:
            preceding_clause = self._last_boundary_end(
                self.clause_starts, self.clause_ends, sentence_start, start
            )
            if preceding_clause is not None:
                clause_start = preceding_clause

        following_clause = self._first_boundary_start(
            self.clause_starts, self.clause_ends, end, sentence_end
        )
        if following_clause is not None:
            clause_end = following_clause
        following_citation = self._first_boundary_start(
            self.citation_starts, self.citation_ends, end, sentence_end
        )
        if following_citation is not None:
            clause_end = min(clause_end, following_citation)

        return clause_start, clause_end


@lru_cache(maxsize=_BOUNDARY_INDEX_CACHE_SIZE)
def _boundary_index(text: str) -> _TextBoundaryIndex:
    """Return the (cached) boundary index for a classification text."""
    return _TextBoundaryIndex(text)


def _occurrence_sentence_span(text: str, start: int, end: int) -> tuple[int, int]:
    """Return the span of the sentence/clause that contains a match.

    Unlike the old fixed-size context window, this resolves the actual
    sentence/clause boundaries.  That matters for long sentences such as the
    2026-17183 citation sentence, where the literature marker can be more than
    200 characters before the artificial-intelligence occurrence. Citation
    abbreviation dots (``et al.``) are not treated as sentence terminators, so
    an author-list citation stays attached to the mention it annotates.

    Boundaries come from a per-text index (built once, binary-searched per
    occurrence) instead of a fresh document scan per match.
    """
    return _boundary_index(text).sentence_span(text, start, end)


def _occurrence_context(text: str, start: int, end: int) -> str:
    """Return the local context of a match, clipped to its own sentence/clause."""
    segment_start, segment_end = _occurrence_sentence_span(text, start, end)
    return text[segment_start:segment_end]


def _occurrence_clause(text: str, start: int, end: int) -> str:
    """Return the clause of the sentence that actually contains the match.

    A sentence can weld an obligation about one subject to a citation about
    another ("... proposes to amend quarterly report deadlines, and a recent
    working paper on artificial intelligence is available at ..."). Obligation
    language must be tied to the clause carrying the match, otherwise any
    unrelated duty in the sentence promotes a bibliographic mention.

    Besides clause punctuation, a new *citation subject* introduced by a plain
    conjunction ("... and Smith et al. discuss ...", "... because researchers
    document ...") opens a fresh clause. That trims a preceding operative duty
    about a different subject out of the citation's clause, while a coordinated
    predicate ("... monitor and govern ...") has no citing subject and stays
    joined so genuine operative duties are preserved.
    """
    sentence_start, sentence_end = _occurrence_sentence_span(text, start, end)
    clause_start, clause_end = _boundary_index(text).clause_span(
        start, end, sentence_start, sentence_end
    )
    # A trailing author-date parenthetical annotates the clause it directly
    # follows ("... adoption is uneven (Jones, 2026)."). Clause punctuation
    # would otherwise split the citation away from the only clause it can
    # possibly refer to, leaving the mention to be rescued by an unrelated duty
    # elsewhere in the sentence.
    trailing_citation = TRAILING_PARENTHETICAL_CITATION_PATTERN.match(text, clause_end)
    if trailing_citation:
        clause_end = trailing_citation.end()
    return text[clause_start:clause_end]


def _is_reference_only_occurrence(text: str, start: int, end: int) -> bool:
    """Return True when a match sits in bibliography/citation-only context.

    The check is deliberately asymmetric and fails open toward "operative":
    obligation language keeps the match, and a match is only discarded when its
    context carries an explicit citation or literature-review marker. Missing a
    genuine requirement is far worse than reporting an extra item, and inline
    footnote markers alone (``\\4\\``) are not treated as evidence because
    operative Federal Register text is full of them.

    Scope is asymmetric on purpose. Obligation language is read from the
    *clause* that contains the match, because a duty governs its own clause and
    not an unrelated neighbour in the same sentence. Citation markers are read
    from the containing sentence as well, because a citing sentence is
    bibliographic throughout ("Another study also found that ... the
    application of artificial intelligence tools."). A citation marker inside
    the match's own clause is decisive and is checked first.
    """
    clause = _occurrence_clause(text, start, end)
    if OPERATIVE_LANGUAGE_PATTERN.search(clause):
        return False
    if REFERENCE_ONLY_PATTERN.search(clause):
        return True

    window = _occurrence_context(text, start, end)
    if OPERATIVE_LANGUAGE_PATTERN.search(window):
        return False
    return bool(REFERENCE_ONLY_PATTERN.search(window))


def _search_operative_match(pattern: str, text: str, exclude_reference_only: bool):
    """Find the first match that is not a bibliography/citation-only mention."""
    if not exclude_reference_only:
        return re.search(pattern, text)

    for match in re.finditer(pattern, text):
        if not _is_reference_only_occurrence(text, match.start(), match.end()):
            return match
    return None


def _search_operative_match_in_segments(
    pattern: str,
    segments: tuple[str, ...],
    exclude_reference_only: bool,
):
    """Search each evidence field independently and return the first match.

    A pattern may never span two fields: the title and the authoritative body
    are separate pieces of evidence, and a match assembled from both is
    evidence of nothing.
    """
    for segment in segments:
        match = _search_operative_match(pattern, segment, exclude_reference_only)
        if match is not None:
            return match
    return None


def _classification_segments(*fields: str) -> tuple[str, ...]:
    """Return the independently analysed, lowercased evidence fields.

    Title and body used to be joined into one string
    (``f"{title.lower()} {body.lower()}"``) before any pattern ran. That single
    space is not a semantic boundary: it welded the end of the title to the
    start of the body, so an operative duty in a reporting *title* landed in
    the same sentence -- and therefore the same evidence window -- as a purely
    bibliographic AI mention at the head of the *body*, promoting it. Bounded
    patterns such as ``supervision.{0,80}(?:electronic|automated)`` could also
    take one term from each field and report a requirement that neither field
    states.

    Fields are therefore analysed separately and unconditionally. Every field
    is still analysed in full -- nothing is dropped, so operative language in
    *either* field is still detected -- but no match, context window, clause,
    or keyword hit can ever cross the boundary between them.
    """
    return tuple(field for field in fields if field)


def _has_electronic_recordkeeping_obligation(text: str) -> bool:
    """Return whether text contains a direct electronic recordkeeping duty.

    This intentionally requires one readable construction that ties together:
    a recordkeeping noun, an obligation, a storage/maintenance action, and
    electronic/digital storage language.  Each regex is bounded by sentence
    and semicolon clause terminators, so ``electronic communications`` or an
    unrelated electronic filing cannot satisfy a records obligation.  Clauses
    containing explicit optional, permissive, or negated wording are rejected,
    and the *complete* clause is inspected for an electronic-or-paper
    alternative (including exception forms such as "unless"/"except") so
    wording that continues past the matched span cannot smuggle a permitted
    paper option through.  A clause that *prohibits* paper ("cannot be retained
    on paper and must be maintained electronically") remains a mandate, and a
    permissive modal that governs something other than storage ("records that
    may contain customer information must be retained electronically") does not
    defeat the mandate it sits beside.
    """
    normalized = _prepare_classification_text(text)
    for clause in re.split(r"[.!?;]+", normalized):
        clause = re.sub(r"\s+", " ", clause).strip()
        if not clause:
            continue

        if _clause_permits_paper_alternative(clause):
            continue

        for pattern in ELECTRONIC_RECORDKEEPING_PATTERNS:
            match = pattern.search(clause)
            if not match:
                continue

            # A paper prohibition ("cannot/may not/must not ... on paper")
            # reinforces the electronic duty; mask it so its paper-bound
            # negation is not misread as a negated electronic obligation. A
            # permissive modal is only permissive when it binds the storage
            # predicate, so unbound modals are masked too.
            matched_text = _mask_unbound_permissive_modals(
                _mask_paper_prohibition(match.group(0))
            )
            if OPTIONAL_OR_NEGATED_RECORDKEEPING.search(matched_text):
                continue

            # A disclaimer before the obligation can turn an otherwise matching
            # noun/action sequence into a paper-only or permissive alternative.
            obligation = re.search(
                rf"\b{RECORDKEEPING_OBLIGATION}\b",
                matched_text,
                re.IGNORECASE,
            )
            if obligation:
                before_obligation = matched_text[:obligation.start()]
                if OPTIONAL_OR_NEGATED_RECORDKEEPING.search(before_obligation):
                    continue

            return True

    return False


def _parse_federal_register_metadata_int(
    data: dict,
    field: str,
    page: int,
    minimum: int,
) -> Optional[int]:
    """Parse a numeric pagination field and fail closed on malformed metadata."""
    raw_value = data.get(field)
    if raw_value is None:
        return None
    if isinstance(raw_value, bool):
        raise FederalRegisterPaginationError(
            f"Federal Register response field '{field}' was invalid on page {page}"
        )
    if isinstance(raw_value, float) and not raw_value.is_integer():
        raise FederalRegisterPaginationError(
            f"Federal Register response field '{field}' was invalid on page {page}"
        )
    try:
        value = int(raw_value)
    except (TypeError, ValueError) as exc:
        raise FederalRegisterPaginationError(
            f"Federal Register response field '{field}' was invalid on page {page}"
        ) from exc
    if value < minimum:
        raise FederalRegisterPaginationError(
            f"Federal Register response field '{field}' was invalid on page {page}"
        )
    return value


def _federal_register_document_identity(document: dict, page: int) -> str:
    """Return the state-compatible stable identity used to deduplicate a document."""
    document_number = str(document.get('document_number') or '').strip()
    if document_number:
        return document_number

    # The state layer uses the document URL when document_number is absent.
    fallback_url = str(document.get('html_url') or '').strip()
    if fallback_url:
        return fallback_url

    raise FederalRegisterPaginationError(
        f"Federal Register document on page {page} has no stable identity"
    )


def _federal_register_document_fingerprint(document: dict) -> str:
    """Return a stable fingerprint for duplicate substantive payload checks."""
    substantive_fields = (
        "title",
        "abstract",
        "publication_date",
        "type",
        "html_url",
        "raw_text_url",
        "agencies",
    )

    def normalize(value):
        if isinstance(value, str):
            return re.sub(r"\s+", " ", value).strip()
        if isinstance(value, list):
            return [normalize(entry) for entry in value]
        if isinstance(value, dict):
            return {
                key: normalize(value[key])
                for key in sorted(value)
            }
        return value

    payload = {
        field: normalize(document.get(field))
        for field in substantive_fields
    }
    return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


@dataclass
class RegulatoryItem:
    """Represents a regulatory document or notice."""
    source: str  # 'Federal Register' or 'FINRA'
    agency: str  # 'SEC', 'CFTC', 'OCC', 'Federal Reserve', 'FINRA'
    title: str
    url: str
    publication_date: str  # ISO format YYYY-MM-DD
    doc_type: Optional[str] = None  # 'RULE', 'PRORULE', 'NOTICE' (Federal Register only)
    abstract: str = ""
    # Complete normalized authoritative body used for classification and
    # change detection.  ``abstract`` remains the bounded report excerpt for
    # FINRA notices.
    content_text: str = ""
    document_id: str = ""  # Federal Register document number or FINRA URL
    publication_date_is_synthetic: bool = False
    classification: str = CLASSIFICATION_NOISE
    classification_reason: str = ""
    affected_controls: list = None

    def __post_init__(self):
        if self.affected_controls is None:
            self.affected_controls = []


def classify_regulatory_relevance(
    title: str,
    abstract: str,
    config: dict,
    exclude_reference_only: bool = False,
) -> tuple[str, str]:
    """
    Classify regulatory item for FSI Copilot governance relevance.

    Uses the unified 4-tier system (CRITICAL/HIGH/MEDIUM/NOISE) for consistency
    with Learn Monitor. Patterns are loaded from config.

    Args:
        title: Document title
        abstract: Document abstract
        config: Configuration dict with pattern definitions
        exclude_reference_only: Ignore matches whose surrounding context is a
            bibliography/citation/literature-review mention. Enable this for
            authoritative full-document source text; API abstracts are
            summaries and are always classified as written.

    Returns:
        tuple: (tier, reason)
    """
    # Handle None values
    title = title or ""
    abstract = abstract or ""
    # Federal Register raw text sometimes contains escaped line breaks. Treat
    # those as whitespace. The whole document is classified regardless of
    # length; relevance is judged per occurrence by context, never by position.
    classification_text = _prepare_classification_text(abstract)
    # Title and body are separate evidence and are analysed separately: no
    # pattern, evidence window, or clause may span the two (see
    # ``_classification_segments``).
    segments = _classification_segments(
        title.lower(), classification_text.lower()
    )

    # Get regulatory patterns from config
    regulatory_config = config.get('regulatory', {})

    # CRITICAL: Directly mentions AI agents, copilot, or automated advice in FSI context
    critical_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('critical_patterns', [])
    ]
    for pattern, reason in critical_patterns:
        if _search_operative_match_in_segments(
            pattern, segments, exclude_reference_only
        ):
            return (CLASSIFICATION_CRITICAL, reason)

    # HIGH: AI, ML, automation terms + FSI-specific requirements
    high_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('high_patterns', [])
    ]
    for pattern, reason in high_patterns:
        if _search_operative_match_in_segments(
            pattern, segments, exclude_reference_only
        ):
            return (CLASSIFICATION_HIGH, reason)

    if any(_has_electronic_recordkeeping_obligation(segment) for segment in segments):
        return (CLASSIFICATION_HIGH, "Electronic recordkeeping")

    # MEDIUM: General FSI regulations that may indirectly affect AI agents
    medium_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('medium_patterns', [])
    ]
    for pattern, reason in medium_patterns:
        if _search_operative_match_in_segments(
            pattern, segments, exclude_reference_only
        ):
            return (CLASSIFICATION_MEDIUM, reason)

    # NOISE: Everything else (general regulatory items with no FSI/AI relevance)
    return (CLASSIFICATION_NOISE, "No FSI Copilot governance relevance detected")


def find_affected_controls_by_keywords(
    title: str,
    abstract: str,
    config: dict,
    exclude_reference_only: bool = False,
) -> list[str]:
    """
    Find potentially affected controls based on keyword matching.

    Args:
        title: Document title
        abstract: Document abstract
        config: Configuration dict with keyword_control_map
        exclude_reference_only: Ignore keyword hits that only occur in
            bibliography/citation context, so a cited paper does not map a
            document onto controls it never touches.

    Returns:
        list: Control IDs (e.g., ['1.3', '1.5', '2.6'])
    """
    # Handle None values
    title = title or ""
    abstract = abstract or ""
    # Control mapping reads the same separated evidence fields as
    # classification: a keyword hit assembled across the title/body seam would
    # map a document onto controls that neither field supports.
    segments = _classification_segments(title.lower(), abstract.lower())
    affected = set()

    # Build keyword map from config
    keyword_map = {
        entry['keyword']: [c['id'] for c in entry['controls']]
        for entry in config.get('keyword_control_map', [])
    }

    for keyword, controls in keyword_map.items():
        # Use word boundary matching to avoid partial matches
        pattern = rf'\b{re.escape(keyword.lower())}\b'
        if _search_operative_match_in_segments(
            pattern, segments, exclude_reference_only
        ):
            affected.update(controls)

    return sorted(list(affected))


def _get_operational_settings(config: dict) -> tuple[int, int, float]:
    """Return request timeout, max retries, and request delay from config."""
    operational = config.get("operational", {})
    request_timeout = int(operational.get("request_timeout", 30))
    max_retries = int(operational.get("max_retries", 3))
    request_delay = float(operational.get("request_delay", 1.0))
    return request_timeout, max_retries, request_delay


def _extract_notice_body_text(html: str, selectors: list[str]) -> str:
    """Extract the complete normalized text of a notice body.

    The first selector that yields non-empty text wins; otherwise the page
    ``<body>`` is used. The full normalized text is returned with no length
    bound: classification must see the entire notice so a mandatory requirement
    that appears late in a long notice is never hidden. Callers that need a
    bounded presentation excerpt slice the result themselves.
    """
    soup = BeautifulSoup(html or "", "html.parser")

    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            text = re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip()
            if text:
                return text

    body = soup.find("body")
    if not body:
        return ""
    return re.sub(r"\s+", " ", body.get_text(" ", strip=True)).strip()


FEDERAL_REGISTER_NON_DOCUMENT_LEAD_CHARS = 600
FEDERAL_REGISTER_DOCUMENT_SUBSTANTIAL_CHARS = 2000
# A 200 response with a body is not proof that the authoritative document was
# served. Edge networks and portals answer denials, bot challenges, captchas,
# login walls, and not-found pages with HTTP 200 and a fully rendered body, and
# the previous extractor accepted any of them: the placeholder became the
# classification input *and* the change-detection fingerprint, so an
# uninspected document was baselined and the real body's later arrival looked
# like an ordinary edit.
FEDERAL_REGISTER_NON_DOCUMENT_PATTERN = re.compile(
    r"(?:"
    r"access\s+(?:to\s+[\w\s]{0,40}\s+)?(?:is\s+|has\s+been\s+)?deni(?:ed|al)"
    r"|access\s+restricted|restricted\s+access"
    r"|(?:your\s+)?request\s+(?:was\s+|has\s+been\s+|is\s+)?(?:blocked|denied|rejected)"
    r"|you\s+(?:do\s+not|don't)\s+have\s+(?:permission|access)"
    r"|you\s+are\s+not\s+authoriz(?:ed|ation)"
    r"|(?:page|file|content|document)\s+(?:you\s+requested\s+)?"
    r"(?:could\s+not\s+be\s+found|was\s+not\s+found|not\s+found|is\s+unavailable)"
    r"|\b40[0-9]\b\s*(?:[-:|\u2013\u2014]|\berror\b|\bforbidden\b|\bnot\s+found\b)"
    r"|\berror\s*[-:|]?\s*40[0-9]\b|\bhttp\s+40[0-9]\b|\b403\s*forbidden\b"
    r"|(?:log|sign)\s*in\s+to\s+(?:continue|view|access|proceed|read)"
    r"|(?:login|log\s*in|sign[-\s]?in|authentication)\s+(?:is\s+)?required"
    r"|session\s+(?:has\s+)?(?:expired|timed\s+out)"
    r"|(?:service|site|page)\s+(?:is\s+)?(?:temporarily\s+)?unavailable"
    r"|rate\s+limit(?:ed|\s+exceeded)?"
    r"|maintenance\s+mode|under\s+maintenance"
    r")",
    re.IGNORECASE,
)
# Signatures that never occur in a genuine Federal Register raw-text document
# and are therefore rejected wherever they appear, not just in the lead.
FEDERAL_REGISTER_CHALLENGE_PATTERN = re.compile(
    r"(?:"
    r"(?:verify|confirm)\s+(?:that\s+)?you\s+are\s+(?:a\s+)?human"
    r"|\bcaptcha\b|are\s+you\s+a\s+robot|checking\s+your\s+browser"
    r"|unusual\s+traffic|automated\s+traffic|bot\s+detection"
    r"|enable\s+(?:javascript|cookies)|cloudflare\s+ray\s+id"
    r"|ddos\s+protection|security\s+check\s+to\s+(?:continue|access)"
    r")",
    re.IGNORECASE,
)
# Structure an authoritative Federal Register document carries. Used only as a
# safety valve so a long, genuinely structured document that quotes one of the
# phrases above is not mistaken for an error page.
FEDERAL_REGISTER_DOCUMENT_STRUCTURE_PATTERN = re.compile(
    r"(?:\[federal\s+register|federal\s+register\s*/\s*vol|\[fr\s+doc"
    r"|\bbilling\s+code\b|\bsupplementary\s+information\b"
    r"|\bfor\s+further\s+information\s+contact\b"
    r"|\bagency:|\baction:|\bsummary:|\bdates:|\baddresses:"
    r"|\brelease\s+no\.|\bfile\s+no\.\s*s?r"
    r"|\b\d{1,3}\s+cfr\s+(?:part|chapter|\u00a7)"
    r"|\bcode\s+of\s+federal\s+regulations\b"
    r"|\bnotice\s+of\s+proposed\s+rulemaking\b"
    r"|\bself[-\s]regulatory\s+organizations?\b)",
    re.IGNORECASE,
)


def _is_federal_register_non_document_text(text: str) -> bool:
    """Return True when candidate raw text is error/challenge/login chrome.

    Deliberately asymmetric, because over-rejection is also a failure mode: a
    valid document that merely *mentions* one of these phrases (rulemakings
    about access controls, authentication, or captchas are routine) is kept
    when it is substantial and structurally recognisable as a Federal Register
    document.
    """
    if not text:
        return True
    if FEDERAL_REGISTER_NON_DOCUMENT_PATTERN.search(
        text[:FEDERAL_REGISTER_NON_DOCUMENT_LEAD_CHARS]
    ) or FEDERAL_REGISTER_CHALLENGE_PATTERN.search(text):
        return not (
            len(text) >= FEDERAL_REGISTER_DOCUMENT_SUBSTANTIAL_CHARS
            and FEDERAL_REGISTER_DOCUMENT_STRUCTURE_PATTERN.search(text)
        )
    return False


def _extract_federal_register_source_text(text: str) -> str:
    """Normalize and validate the authoritative Federal Register raw text.

    Returns an empty string for a body that is an access denial, bot
    challenge, captcha, login wall, error, or not-found page, so the caller
    fails closed with ``RequiredSourceTextError`` before anything is
    classified, hashed, or baselined.
    """
    soup = BeautifulSoup(text or "", "html.parser")
    preformatted_text = soup.find("pre")
    source_text = (
        preformatted_text.get_text(" ", strip=True)
        if preformatted_text
        else soup.get_text(" ", strip=True)
    )
    normalized = re.sub(r"\s+", " ", source_text).strip()
    if _is_federal_register_non_document_text(normalized):
        logger.warning(
            "Federal Register raw text was rejected as non-document content "
            "(access denial, challenge, login, or error page)"
        )
        return ""
    return normalized


def _extract_finra_notice_fallback_text(html: str) -> str:
    """Extract the complete normalized text of the FINRA notice body.

    Three independent gates must all pass before text is treated as
    authoritative notice content:

    1. *Structure.* The text must come from a notice article/body container
       (``[itemprop=articleBody]``, an ``article``/notice node, or a
       ``field--name-*body`` field, optionally scoped to ``main``). A non-empty
       ``<main>`` is **not** sufficient -- FINRA renders access-denied,
       bot-challenge, login, and not-found pages inside a populated ``<main>``,
       and accepting those would baseline an uninspected notice.
    2. *Content.* The candidate must not carry an access-denied, blocked,
       challenge/captcha, login, error, or not-found signature in its leading
       region (:func:`_is_finra_non_notice_page_text`).
    3. *Substance.* The candidate must not be a tombstone that declares no
       text exists ("NOT AVAILABLE AT THIS TIME"), which is a successful
       source answer but not notice content
       (:func:`_finra_notice_unavailable_reason`).

    A page with no surviving candidate returns an empty string. The caller
    then distinguishes the two empty cases with
    :func:`_finra_notice_unavailable_reason_from_html`: an error/challenge page
    fails the run closed, a tombstone is excluded from the baseline while the
    source run completes.
    """
    return _scan_finra_notice_body(html)[0]


def _finra_notice_unavailable_reason_from_html(html: str) -> Optional[str]:
    """Return the tombstone phrase when a notice page declares no content.

    Returns ``None`` when the page yields a real body, when nothing
    notice-shaped was found at all, or when any candidate looked like error /
    challenge / login chrome -- an integrity failure always outranks a
    tombstone, so those still fail the run closed.
    """
    text, reason, rejected_non_notice = _scan_finra_notice_body(html)
    if text or rejected_non_notice:
        return None
    return reason


def _extract_finra_notice_required_text(html: str) -> str:
    """Extractor for required FINRA bodies; raises on tombstone pages.

    Returning ``""`` here would make the caller raise
    :class:`RequiredSourceTextError` and fail the whole FINRA run closed. That
    is right for chrome (we could not read a notice that exists) and wrong for
    a tombstone (there is nothing to read, permanently), so the two empty
    cases are separated at the point where the HTML is still in hand.
    """
    text, reason, rejected_non_notice = _scan_finra_notice_body(html)
    if text:
        return text
    if reason and not rejected_non_notice:
        raise FinraNoticeUnavailableError(reason)
    return ""


def _scan_finra_notice_body(html: str) -> tuple[str, Optional[str], bool]:
    """Return ``(body_text, unavailable_reason, rejected_non_notice)``."""
    soup = BeautifulSoup(html or "", "html.parser")
    candidates: list[tuple[int, int, str]] = []
    rejected_non_notice = False
    unavailable_reason: Optional[str] = None
    excluded_parent_names = {
        "aside",
        "footer",
        "header",
        "nav",
        "noscript",
        "script",
        "style",
    }

    def normalized_node_text(node) -> str:
        text_parts = []
        for string in node.find_all(string=True):
            if any(
                parent.name in excluded_parent_names
                for parent in [string.parent, *string.parents]
                if parent is not None
            ):
                continue
            text_parts.append(str(string))
        return re.sub(r"\s+", " ", " ".join(text_parts)).strip()

    def add_candidate(node, score: int) -> None:
        nonlocal rejected_non_notice, unavailable_reason
        text = normalized_node_text(node)
        if not text:
            return
        # Error, challenge, denial, and login pages are page chrome, not
        # authoritative notice content, whatever container they render in.
        if _is_finra_non_notice_page_text(text):
            rejected_non_notice = True
            return
        # A tombstone body ("NOT AVAILABLE AT THIS TIME") is a successful
        # answer that declares there is no notice text; it is never treated as
        # authoritative content.
        reason = _finra_notice_unavailable_reason(text)
        if reason:
            if unavailable_reason is None:
                unavailable_reason = reason
            return
        candidates.append((score, len(text), text))

    # Explicit semantic article-body fields are the strongest signal.
    for selector in (
        "[itemprop='articleBody']",
        "article .notice-body",
        "article .field--name-field-notice-body",
        "article .field--name-field-body",
        "article .field--name-body",
        "article .field--name-body",
        ".node--type-finra-notice [class*='field--name-body']",
        ".node--type-regulatory-notice [class*='field--name-body']",
        ".node--type-notice [class*='field--name-body']",
        ".notice-detail [class*='field--name-body']",
        ".regulatory-notice [class*='field--name-body']",
    ):
        for node in soup.select(selector):
            add_candidate(node, 100)

    # A notice article/container is still authoritative when it has no
    # dedicated articleBody field; choose the longest scoped body if several
    # article-like nodes are present.
    for selector in (
        "article[class*='notice']",
        "article",
        ".node--type-finra-notice",
        ".node--type-regulatory-notice",
        ".node--type-notice",
        ".notice-detail",
        ".regulatory-notice",
    ):
        for node in soup.select(selector):
            add_candidate(node, 70)

    # Some FINRA templates expose the notice body field directly under main
    # without an article element. This stays scoped to a *body field*: a bare
    # ``main`` is never a notice body, and the whole document never is.
    for selector in (
        "main [itemprop='articleBody']",
        "main .notice-body",
        "main .field--name-field-notice-body",
        "main .field--name-field-body",
        "main .field--name-body",
    ):
        for node in soup.select(selector):
            add_candidate(node, 90)

    # A few older FINRA pages expose multiple generic body fields without a
    # semantic article wrapper. Treat the longest one as a low-confidence
    # fallback, never as a whole-document fallback.
    for node in soup.select("[class*='field--name-body']"):
        add_candidate(node, 40)

    if not candidates:
        if rejected_non_notice:
            logger.warning(
                "FINRA detail page carried no notice body: every candidate was "
                "an error, challenge, login, or not-found page"
            )
        elif unavailable_reason:
            logger.warning(
                "FINRA detail page declared no available notice text (%r)",
                unavailable_reason,
            )
        return "", unavailable_reason, rejected_non_notice
    _, _, text = max(candidates, key=lambda candidate: (candidate[0], candidate[1]))
    return text, unavailable_reason, rejected_non_notice


# Interstitial paths an edge network or portal redirects to when it refuses to
# serve the document. A 200 at one of these is never the authoritative source.
SOURCE_CHALLENGE_PATH_PATTERN = re.compile(
    r"(?:/cdn-cgi/|/__cf|/challenge|/captcha|/distil|/incapsula|/_incapsula"
    r"|/waf|/blocked|/denied|/access[-_]denied|/errors?(?:/|$)"
    r"|/login(?:/|$)|/signin(?:/|$)|/sign[-_]in(?:/|$)|/auth(?:/|$)"
    r"|/sessionexpired|/maintenance(?:/|$)|/404(?:/|$)|/403(?:/|$))",
    re.IGNORECASE,
)


def _source_origin_rejection_reason(
    requested_url: str, final_url: Optional[str]
) -> Optional[str]:
    """Return why a response's final origin is untrustworthy, else ``None``.

    Guards the case a status code cannot: a 200 that was actually served by a
    different host (or a challenge/login path) after redirects. Absence of
    ``final_url`` is treated as "no redirect happened", because no-information
    is not evidence of one.
    """
    if not final_url or final_url == requested_url:
        return None
    requested = urlparse(requested_url)
    final = urlparse(final_url)
    if final.scheme not in {"http", "https"}:
        return (
            f"final URL scheme {final.scheme or '(none)'!r} is not http(s): {final_url}"
        )
    if requested.scheme == "https" and final.scheme != "https":
        return f"redirect downgraded https to {final.scheme}: {final_url}"
    if (final.hostname or "").lower() != (requested.hostname or "").lower():
        return (
            f"redirected off-origin from {requested.hostname!r} to "
            f"{final.hostname!r}: {final_url}"
        )
    if SOURCE_CHALLENGE_PATH_PATTERN.search(final.path or ""):
        return f"redirected to a challenge/error path: {final_url}"
    return None


def _fetch_cached_fallback_text(
    *,
    url: str,
    session: requests.Session,
    cache: dict[str, str],
    request_delay: float,
    max_retries: int,
    extractor,
    required: bool = False,
    source_label: str = "detail",
) -> tuple[str, bool]:
    """Fetch fallback text once per URL and return (text, fetched_new)."""
    if not url:
        if required:
            raise RequiredSourceTextError(
                f"{source_label} URL was missing for required classification text"
            )
        return "", False

    if url in cache:
        cached_text = cache[url]
        if required and not cached_text:
            raise RequiredSourceTextError(
                f"{source_label} text was empty for {url}"
            )
        return cached_text, False

    if request_delay > 0:
        time.sleep(request_delay)

    result = fetch_page(url, session, max_retries=max_retries)
    if result["status_code"] != 200:
        message = (
            f"{source_label} fetch failed for {url} "
            f"(status={result['status_code']}, error={result.get('error')})"
        )
        if required:
            raise RequiredSourceTextError(message)
        logger.warning(message)
        cache[url] = ""
        return "", True

    origin_rejection = _source_origin_rejection_reason(url, result.get("final_url"))
    if origin_rejection:
        message = f"{source_label} fetch for {url} {origin_rejection}"
        if required:
            raise RequiredSourceTextError(message)
        logger.warning(message)
        cache[url] = ""
        return "", True

    fallback_text = extractor(result["content"])
    if required and not fallback_text:
        raise RequiredSourceTextError(
            f"{source_label} text was empty for {url}"
        )
    cache[url] = fallback_text
    return fallback_text, True


# Deterministic ordering of the four classification tiers. A higher number is
# strictly more severe. Used to merge the curated abstract classification with
# the authoritative full-text classification without ambiguity.
CLASSIFICATION_SEVERITY = {
    CLASSIFICATION_NOISE: 0,
    CLASSIFICATION_MEDIUM: 1,
    CLASSIFICATION_HIGH: 2,
    CLASSIFICATION_CRITICAL: 3,
}


def _classification_severity(classification: str) -> int:
    """Return the severity rank of a classification tier (unknown -> NOISE)."""
    return CLASSIFICATION_SEVERITY.get(classification, 0)


def _should_fetch_federal_register_detail(
    title: str,
    abstract: str,
    classification: str,
    doc_type: str,
) -> bool:
    """Every Federal Register item is classified against its authoritative body.

    A curated abstract is only a summary, so it can hide operative language at
    any tier -- including a CRITICAL abstract whose body carries a *different*
    requirement, and whose body must still be retained and hashed so a later
    body-only revision is observable. There is therefore no tier that skips the
    authoritative read.
    """
    return True


def _federal_register_authoritative_text_required(abstract_classification: str) -> bool:
    """Authoritative full text is mandatory for every Federal Register item.

    The previous best-effort rule let a MEDIUM/HIGH abstract be accepted and
    baselined when the authoritative read failed, which recorded a fingerprint
    over summary text and silently suppressed any later body change. An item
    whose authoritative body cannot be read is not classified, not hashed, and
    not baselined: the run fails closed with ``RequiredSourceTextError`` and the
    existing failure exit code.
    """
    return True


def _should_fetch_finra_notice_detail(title: str, url: str, classification: str) -> bool:
    """Return whether an eligible FINRA notice needs authoritative detail.

    Classification and title are deliberately not used as a shortcut.  A
    listing title is not authoritative notice content, and skipping a high
    title or an older/information notice would allow an uninspected item into
    the baseline.  URL eligibility is established by the listing parser.
    """
    return _canonical_finra_notice_url(url) is not None


def _canonical_finra_notice_url(raw_url: str) -> Optional[str]:
    """Return a stable FINRA notice URL for supported listing links.

    A leading ``/index.php`` front-controller segment is canonicalized away so
    ``/index.php/rules-guidance/notices/26-12`` resolves to the same accepted
    notice path. Off-origin hosts and lookalike prefixes (``/index.phpx/...``)
    are still rejected: the hostname allow-list and the path pattern are applied
    after the (slash-only) ``/index.php`` strip.
    """
    if not raw_url:
        return None

    candidate = urljoin(
        FINRA_NOTICES_URL.rstrip("/") + "/",
        str(raw_url).strip(),
    )
    parsed = urlparse(candidate)
    if parsed.scheme.lower() not in {"http", "https"}:
        return None
    if (parsed.hostname or "").lower() not in {"finra.org", "www.finra.org"}:
        return None

    path = re.sub(r"/+", "/", parsed.path or "/")
    path = FINRA_INDEX_PHP_PREFIX_PATTERN.sub("", path)
    if not FINRA_NOTICE_PATH_PATTERN.fullmatch(path):
        return None

    return f"https://www.finra.org{path.rstrip('/')}"


def _finra_listing_page_number(raw_url: str) -> Optional[int]:
    """Return the 0-indexed page for a same-origin notices *listing* link.

    Only same-origin links whose canonical path is the notices listing itself
    (after the shared ``/index.php`` strip) and that carry a non-negative
    ``page`` query parameter are recognised. Off-origin, lookalike, and
    notice-detail links return ``None`` so pagination can never follow a
    hostile href; the crawler constructs page URLs itself.
    """
    if not raw_url:
        return None

    candidate = urljoin(
        FINRA_NOTICES_URL.rstrip("/") + "/",
        str(raw_url).strip(),
    )
    parsed = urlparse(candidate)
    if parsed.scheme.lower() not in {"http", "https"}:
        return None
    if (parsed.hostname or "").lower() not in {"finra.org", "www.finra.org"}:
        return None

    path = re.sub(r"/+", "/", parsed.path or "/")
    path = FINRA_INDEX_PHP_PREFIX_PATTERN.sub("", path)
    if not FINRA_LISTING_PATH_PATTERN.fullmatch(path):
        return None

    values = parse_qs(parsed.query).get("page")
    if not values:
        return None
    try:
        page = int(values[0])
    except (TypeError, ValueError):
        return None
    if page < 0:
        return None
    return page


def _extract_finra_last_page(content: str | bytes) -> int:
    """Return the highest 0-indexed listing page declared by the pager.

    The FINRA pager only renders a sliding window of page numbers plus a
    "Last" link, so the maximum ``?page=N`` on any single page is a lower
    bound on the true last page. The crawler re-reads this on every page and
    keeps the running maximum, extending the crawl as later pages reveal
    higher numbers. Returns ``0`` when no pager is present (single-page
    listings and legacy fixtures), so only the base page is fetched.
    """
    soup = BeautifulSoup(content, "html.parser")
    last_page = 0
    for link in soup.find_all("a", href=True):
        page = _finra_listing_page_number(link.get("href", ""))
        if page is not None:
            last_page = max(last_page, page)
    return last_page


def _finra_link_quality(link) -> tuple[int, int]:
    """Rank duplicate anchors for the same notice (row-date presence, title length)."""
    title = re.sub(r"\s+", " ", link.get_text(" ", strip=True)).strip()
    row = link.find_parent("tr")
    has_row_date = int(bool(row and row.find("time", datetime=True)))
    return has_row_date, len(title)


def _extract_finra_notice_links(content: str | bytes) -> list:
    """Enumerate and deduplicate eligible links from a FINRA listing.

    FINRA renders notices in table rows/list items and may repeat the same
    detail URL in a title link and a secondary view link.  Filtering every
    anchor by the supported notice URL shapes avoids broad-container
    first-link loss while preserving DOM order and one link per notice.
    """
    soup = BeautifulSoup(content, "html.parser")
    links_by_url: dict[str, object] = {}

    scoped_links = []
    for container in soup.select(
        "table tr, .views-row, ul.notices-list li, ol.notices-list li, "
        "ul[class*='notice'] li, ol[class*='notice'] li"
    ):
        if container.find_parent("nav"):
            continue
        scoped_links.extend(container.find_all("a", href=True))

    # Older/simple fixtures and templates may not expose a recognizable row
    # class.  Fall back to all anchors only when no eligible row/list links were
    # found; URL filtering still limits the fallback to supported notice shapes.
    eligible_scoped_links = [
        link
        for link in scoped_links
        if _canonical_finra_notice_url(link.get("href", "")) is not None
    ]
    candidate_links = eligible_scoped_links or soup.find_all("a", href=True)
    for link in candidate_links:
        canonical_url = _canonical_finra_notice_url(link.get("href", ""))
        if canonical_url is None:
            continue

        existing = links_by_url.get(canonical_url)
        if existing is None or _finra_link_quality(link) > _finra_link_quality(existing):
            links_by_url[canonical_url] = link

    # Store the canonical URL on each selected tag for the caller.  Beautiful
    # Soup tags permit attributes, and this prevents a second URL normalization
    # pass from reintroducing query/fragment variants.
    selected = []
    for link in links_by_url.values():
        canonical_url = _canonical_finra_notice_url(link.get("href", ""))
        link["data-monitor-canonical-url"] = canonical_url
        selected.append(link)
    return selected


def fetch_federal_register_documents(
    session: requests.Session,
    since_date: str,
    config: dict,
    limit: Optional[int] = None,
    detail_fetch_limit: int = FEDERAL_REGISTER_DETAIL_FETCH_LIMIT,
) -> list[RegulatoryItem]:
    """
    Fetch documents from Federal Register API.

    Args:
        session: requests.Session instance
        since_date: ISO date string (YYYY-MM-DD) - fetch documents published on or after this date
        config: Configuration dict with federal_register settings
        limit: Maximum documents to fetch (for testing)
        detail_fetch_limit: Maximum detail pages to fetch for fallback text

    Returns:
        list[RegulatoryItem]: New regulatory items
    """
    items = []

    request_timeout, max_retries, request_delay = _get_operational_settings(config)

    # Get agencies and doc types from config
    fed_config = config.get('federal_register', {})
    agencies = [a['slug'] for a in fed_config.get('agencies', [])]
    doc_types = fed_config.get('document_types', ['RULE', 'PRORULE', 'NOTICE'])

    # Build agency short name map from config
    agency_short_map = {
        a['slug']: a.get('short_name', a['slug'])
        for a in fed_config.get('agencies', [])
    }

    # Build query parameters. Keep the page size below the API maximum so
    # pagination remains testable and a malformed response cannot create an
    # unbounded request loop.
    params = {
        'conditions[agencies][]': agencies,
        'conditions[type][]': doc_types,
        'conditions[publication_date][gte]': since_date,
        'per_page': FEDERAL_REGISTER_PAGE_SIZE,
        'order': 'newest',
        'fields[]': [
            'document_number',
            'title',
            'abstract',
            'publication_date',
            'type',
            'html_url',
            'raw_text_url',
            'agencies',
        ],
    }

    unique_documents: dict[str, dict] = {}
    page = 1
    total_pages = None
    reported_count = None
    expected_pages = None
    while page <= FEDERAL_REGISTER_MAX_PAGES:
        page_params = {**params, 'page': page}
        data = {}
        for attempt in range(max_retries):
            try:
                logger.info(
                    "Querying Federal Register API for documents since %s (page %s)...",
                    since_date,
                    page,
                )
                response = session.get(
                    f"{FEDERAL_REGISTER_API_BASE}/documents.json",
                    params=page_params,
                    timeout=request_timeout,
                )
                response.raise_for_status()
                data = response.json()
                break
            except requests.RequestException as e:
                if attempt == max_retries - 1:
                    logger.error(f"Federal Register API error: {e}")
                    raise FederalRegisterPaginationError(
                        f"Federal Register API request failed on page {page}"
                    ) from e
                sleep_seconds = request_delay if request_delay > 0 else (2 ** attempt)
                logger.warning(
                    "Federal Register API request failed (attempt %s/%s): %s; retrying in %.1fs",
                    attempt + 1,
                    max_retries,
                    e,
                    sleep_seconds,
                )
                time.sleep(sleep_seconds)
            except json.JSONDecodeError as e:
                logger.error(f"Federal Register API response parsing error: {e}")
                raise FederalRegisterPaginationError(
                    f"Federal Register API response parsing failed on page {page}"
                ) from e

        if not isinstance(data, dict):
            raise FederalRegisterPaginationError(
                f"Federal Register response was not an object on page {page}"
            )

        page_count = _parse_federal_register_metadata_int(data, 'count', page, 0)
        if page_count is None:
            raise FederalRegisterPaginationError(
                f"Federal Register response was missing 'count' on page {page}"
            )
        if reported_count is not None and page_count != reported_count:
            raise FederalRegisterPaginationError(
                "Federal Register response count changed during pagination"
            )
        reported_count = page_count

        # The production API omits results for a legitimate zero-result query.
        # For every non-zero count, results must be present before pagination
        # can advance; an empty or short response is safe only when count
        # proves that the complete result set has been collected.
        if 'results' not in data:
            if page_count != 0:
                raise FederalRegisterPaginationError(
                    f"Federal Register response was missing 'results' on page {page}"
                )
            page_documents = []
        else:
            page_documents = data['results']
            if not isinstance(page_documents, list):
                raise FederalRegisterPaginationError(
                    f"Federal Register response 'results' was not a list on page {page}"
                )
            if page_count == 0 and page_documents:
                raise FederalRegisterPaginationError(
                    f"Federal Register response had results with count 0 on page {page}"
                )

        page_total_pages = _parse_federal_register_metadata_int(
            data,
            'total_pages',
            page,
            0,
        )
        if page_total_pages is not None:
            page_total_pages = max(1, page_total_pages)
            if total_pages is not None and page_total_pages != total_pages:
                raise FederalRegisterPaginationError(
                    "Federal Register response total_pages changed during pagination"
                )
            total_pages = page_total_pages

        reported_page = _parse_federal_register_metadata_int(data, 'page', page, 1)
        if reported_page is not None and reported_page != page:
            raise FederalRegisterPaginationError(
                f"Federal Register response page metadata did not match requested page {page}"
            )

        if reported_count is not None:
            expected_pages = max(
                1,
                (reported_count + FEDERAL_REGISTER_PAGE_SIZE - 1)
                // FEDERAL_REGISTER_PAGE_SIZE,
            )
            if total_pages is not None and total_pages != expected_pages:
                raise FederalRegisterPaginationError(
                    "Federal Register pagination metadata was inconsistent with count"
                )

        known_final_page = (
            (total_pages is not None and page >= total_pages)
            or (total_pages is None and expected_pages is not None and page >= expected_pages)
            or (page == 1 and not page_documents and total_pages is None and expected_pages is None)
        )

        if not page_documents:
            if not known_final_page:
                raise FederalRegisterPaginationError(
                    f"Federal Register page {page} was empty before pagination completed"
                )
            if reported_count is not None and len(unique_documents) != reported_count:
                raise FederalRegisterPaginationError(
                    "Federal Register pagination collected an incomplete unique result set"
                )
            break

        for document in page_documents:
            if not isinstance(document, dict):
                raise FederalRegisterPaginationError(
                    f"Federal Register result was not an object on page {page}"
                )
            identity = _federal_register_document_identity(document, page)
            existing_document = unique_documents.get(identity)
            if existing_document is None:
                unique_documents[identity] = document
            elif _federal_register_document_fingerprint(existing_document) != _federal_register_document_fingerprint(document):
                raise FederalRegisterPaginationError(
                    f"Federal Register duplicate identity '{identity}' had conflicting "
                    f"substantive payloads on page {page}"
                )

        if total_pages and total_pages > FEDERAL_REGISTER_MAX_PAGES:
            logger.error(
                "Federal Register response requires %s pages, exceeding the %s-page safety bound",
                total_pages,
                FEDERAL_REGISTER_MAX_PAGES,
            )
            raise FederalRegisterPaginationError(
                "Federal Register pagination exceeded the configured safety bound"
            )

        # A caller-supplied limit deliberately requests a partial collection.
        if limit and len(unique_documents) >= limit:
            break

        if known_final_page:
            if reported_count is not None and len(unique_documents) != reported_count:
                raise FederalRegisterPaginationError(
                    "Federal Register pagination collected an incomplete unique result set"
                )
            break
        if (
            total_pages is None
            and expected_pages is None
            and len(page_documents) < FEDERAL_REGISTER_PAGE_SIZE
        ):
            raise FederalRegisterPaginationError(
                "Federal Register pagination completed without enough metadata "
                "to verify unique results"
            )

        page += 1
    else:
        raise FederalRegisterPaginationError(
            "Federal Register pagination reached the configured safety bound"
        )

    documents = list(unique_documents.values())
    logger.info(
        "Federal Register API returned %s documents across %s page(s)",
        len(documents),
        page,
    )

    # Apply limit if specified
    if limit:
        documents = documents[:limit]
        logger.info(f"Limited to {limit} documents for testing")

    detail_cache: dict[str, str] = {}
    detail_fetches = 0

    for doc in documents:
        # Extract agency names
        doc_agencies = doc.get('agencies', [])
        agency_slugs = [agency.get('slug', '') for agency in doc_agencies]
        agency_names = [agency.get('name', 'Unknown') for agency in doc_agencies]
        agency_name = ', '.join(agency_names) if agency_names else 'Unknown'

        # Map to canonical short names using config
        agency_short = 'Unknown'
        for slug in agency_slugs:
            if slug in agency_short_map:
                agency_short = agency_short_map[slug]
                break
        if agency_short == 'Unknown':
            agency_short = agency_name

        title = doc.get('title', 'Untitled')
        abstract = doc.get('abstract', '') or ''
        doc_type = doc.get('type', '')
        url = doc.get('html_url', '')

        tier, reason = classify_regulatory_relevance(title, abstract, config)
        abstract_tier = tier
        effective_text = abstract
        authoritative_body = ""
        used_source_text = False

        should_fetch_detail = _should_fetch_federal_register_detail(
            title=title,
            abstract=abstract,
            classification=abstract_tier,
            doc_type=doc_type,
        )
        authoritative_required = _federal_register_authoritative_text_required(
            abstract_tier
        )
        raw_text_url = doc.get('raw_text_url', '')
        fetch_budget_exhausted = (
            detail_fetch_limit is not None
            and raw_text_url not in detail_cache
            and detail_fetches >= detail_fetch_limit
        )
        # No item is classified or baselined without its authoritative body, so
        # exhausting the fetch budget before reaching it must fail closed
        # instead of accepting a summary-only record.
        if should_fetch_detail and fetch_budget_exhausted and authoritative_required:
            raise RequiredSourceTextError(
                "Federal Register authoritative-text fetch limit reached before "
                f"classification completed for {doc.get('document_number') or url}"
            )
        if should_fetch_detail and not fetch_budget_exhausted:
            fallback_text, fetched_new = _fetch_cached_fallback_text(
                url=raw_text_url,
                session=session,
                cache=detail_cache,
                request_delay=request_delay,
                max_retries=max_retries,
                extractor=_extract_federal_register_source_text,
                required=authoritative_required,
                source_label="Federal Register authoritative text",
            )
            if fetched_new:
                detail_fetches += 1
            if fallback_text:
                # The complete normalized authoritative body is always retained
                # and hashed, whichever tier ultimately wins. Change detection
                # must see the source of record even when the curated abstract
                # is the more severe classification evidence.
                authoritative_body = fallback_text
                source_tier, source_reason = classify_regulatory_relevance(
                    title,
                    fallback_text,
                    config,
                    exclude_reference_only=True,
                )
                # Deterministic precedence for *classification only*: the more
                # severe of the curated abstract and the authoritative body
                # wins, and ties go to the authoritative body (it is the source
                # of record). Because only a source tier that meets or exceeds
                # the abstract tier is adopted, a weaker authoritative read can
                # never downgrade legitimate abstract evidence.
                if _classification_severity(source_tier) >= _classification_severity(
                    abstract_tier
                ):
                    tier, reason = source_tier, source_reason
                    effective_text = fallback_text
                    used_source_text = True

        classification_text = _prepare_classification_text(effective_text)
        affected_controls = (
            find_affected_controls_by_keywords(
                title,
                classification_text,
                config,
                exclude_reference_only=used_source_text,
            )
            if tier in {CLASSIFICATION_CRITICAL, CLASSIFICATION_HIGH}
            else []
        )

        item = RegulatoryItem(
            source='Federal Register',
            agency=agency_short,
            title=title,
            url=url,
            publication_date=doc.get('publication_date', ''),
            doc_type=doc_type,
            abstract=effective_text,
            content_text=authoritative_body or effective_text,
            document_id=doc.get('document_number', ''),
            classification=tier,
            classification_reason=reason,
            affected_controls=affected_controls,
        )
        items.append(item)

    return items


def fetch_finra_notices(
    session: requests.Session,
    config: dict,
    limit: Optional[int] = None,
    detail_fetch_limit: Optional[int] = FINRA_DETAIL_FETCH_LIMIT,
    unavailable_notices: Optional[list[dict]] = None,
) -> list[RegulatoryItem]:
    """
    Scrape FINRA regulatory notices page.

    Args:
        session: requests.Session instance
        config: Configuration dict for classification
        limit: Maximum notices to fetch (for testing)
        detail_fetch_limit: Optional safety limit for tests.  Production uses
            ``None`` and fetches every eligible notice body.
        unavailable_notices: Optional ledger. Notices whose page declares no
            available text ("NOT AVAILABLE AT THIS TIME") are appended here and
            omitted from the returned items, so they are never classified,
            hashed, or baselined while the source run still completes.

    Returns:
        list[RegulatoryItem]: FINRA notices
    """
    items = []
    if unavailable_notices is None:
        unavailable_notices = []
    _, max_retries, request_delay = _get_operational_settings(config)

    logger.info(f"Fetching FINRA notices from {FINRA_NOTICES_URL}...")

    def _fetch_listing_page(page_index: int) -> str | bytes:
        """Fetch one listing page and return its validated content, failing closed."""
        page_url = (
            FINRA_NOTICES_URL
            if page_index == 0
            else f"{FINRA_NOTICES_URL}?page={page_index}"
        )
        try:
            result = fetch_page(page_url, session, max_retries=max_retries)
        except Exception as exc:
            raise FinraListingError(
                f"FINRA notices page request failed for page {page_index}"
            ) from exc

        if not isinstance(result, dict):
            raise FinraListingError(
                "FINRA notices page request returned an invalid result"
            )

        status_code = result.get('status_code')
        if status_code != 200:
            error_detail = result.get("error")
            logger.error(
                "FINRA notices page %s returned status %s", page_index, status_code
            )
            if error_detail:
                logger.error("FINRA notices fetch error: %s", error_detail)
            raise FinraListingError(
                f"FINRA notices page request failed with status {status_code} "
                f"for page {page_index}"
            )

        content = result.get('content')
        if not isinstance(content, (str, bytes)):
            raise FinraListingError(
                "FINRA notices page parsing failed: invalid content"
            )
        return content

    # Crawl every declared listing page. ``declared_last`` is the running
    # maximum last-page number the pager has advertised; because the pager
    # only shows a sliding window, later pages can raise it, extending the
    # crawl until the true final page is reached. The crawl fails closed on a
    # hostile/oversized pager, a duplicate (looping) page, and any declared
    # page that yields no notices, so a partial crawl is never baselined as
    # complete.
    collected: dict[str, object] = {}
    seen_fingerprints: dict[frozenset, int] = {}
    declared_last = 0
    page_index = 0
    pages_fetched = 0

    while True:
        content = _fetch_listing_page(page_index)
        pages_fetched += 1

        try:
            page_links = _extract_finra_notice_links(content)
        except Exception as exc:
            raise FinraListingError("FINRA notices page parsing failed") from exc

        try:
            page_last = _extract_finra_last_page(content)
        except Exception as exc:
            raise FinraListingError(
                "FINRA notices pagination parsing failed"
            ) from exc
        declared_last = max(declared_last, page_last)

        if declared_last >= FINRA_MAX_LISTING_PAGES:
            raise FinraListingError(
                "FINRA notices pagination exceeded the maximum of "
                f"{FINRA_MAX_LISTING_PAGES} pages (declared last page "
                f"{declared_last}); refusing to baseline a partial crawl"
            )

        if not page_links:
            if page_index == 0:
                raise FinraListingError(
                    "FINRA notices page returned no regulatory notice links"
                )
            raise FinraListingError(
                f"FINRA notices page {page_index} was declared by pagination "
                "but returned no notice links"
            )

        fingerprint = frozenset(
            link.get("data-monitor-canonical-url") for link in page_links
        )
        previous_page = seen_fingerprints.get(fingerprint)
        if previous_page is not None and previous_page != page_index:
            raise FinraListingError(
                f"FINRA notices pagination loop detected: page {page_index} "
                f"repeats the notices of page {previous_page}"
            )
        seen_fingerprints.setdefault(fingerprint, page_index)

        for link in page_links:
            canonical_url = link.get("data-monitor-canonical-url")
            existing = collected.get(canonical_url)
            if existing is None:
                collected[canonical_url] = link
            elif _finra_link_quality(link) > _finra_link_quality(existing):
                collected[canonical_url] = link

        if limit and len(collected) >= limit:
            break
        if page_index >= declared_last:
            break
        page_index += 1

    notice_links = list(collected.values())
    if not notice_links:
        raise FinraListingError(
            "FINRA notices page returned no regulatory notice links"
        )

    logger.info(
        "Found %s FINRA notice links across %s listing page(s)",
        len(notice_links),
        pages_fetched,
    )

    if limit:
        notice_links = notice_links[:limit]
        logger.info(f"Limited to {limit} notices for testing")

    detail_cache: dict[str, str] = {}
    unavailable_cache: dict[str, str] = {}
    detail_fetches = 0

    for link in notice_links:
        title = link.get_text(strip=True)
        url = link.get("data-monitor-canonical-url") or _canonical_finra_notice_url(
            link.get("href", "")
        )
        if url is None:
            # The helper already filters these, but fail closed if a caller
            # mutates a parsed tag between extraction and processing.
            raise FinraListingError(
                "FINRA notices page parsing failed: unsupported notice URL"
            )

        match = FINRA_NOTICE_ID_PATTERN.search(url)
        if match:
            year_short = match.group(1)
            notice_num = match.group(2)
            document_id = f"FINRA {year_short}-{notice_num}"
        else:
            document_id = url

        publication_date, publication_date_is_synthetic = (
            _derive_finra_publication_date(link, url)
        )

        tier, reason = classify_regulatory_relevance(title, "", config)
        # Classification and control mapping run against the COMPLETE normalized
        # notice body so a mandatory requirement that appears late in a long
        # notice cannot be truncated away. Only a bounded excerpt is stored on
        # the item for presentation in reports.
        notice_body_text = ""
        presentation_excerpt = ""

        should_fetch_detail = _should_fetch_finra_notice_detail(title, url, tier)
        fetch_limit_exhausted = (
            detail_fetch_limit is not None
            and detail_fetches >= detail_fetch_limit
        )
        if should_fetch_detail and fetch_limit_exhausted:
            raise RequiredSourceTextError(
                "FINRA authoritative notice body fetch limit reached before "
                f"classification completed for {url}"
            )
        if should_fetch_detail:
            if url in unavailable_cache:
                logger.warning(
                    "Skipping FINRA notice %s: source declares no notice text "
                    "(%s); excluded from classification and baseline",
                    document_id,
                    unavailable_cache[url],
                )
                unavailable_notices.append(
                    {
                        "document_id": document_id,
                        "title": title,
                        "url": url,
                        "reason": unavailable_cache[url],
                    }
                )
                continue
            try:
                fallback_text, fetched_new = _fetch_cached_fallback_text(
                    url=url,
                    session=session,
                    cache=detail_cache,
                    request_delay=request_delay,
                    max_retries=max_retries,
                    extractor=_extract_finra_notice_required_text,
                    required=True,
                    source_label="FINRA authoritative notice body",
                )
            except FinraNoticeUnavailableError as exc:
                # The source answered, and its answer is "there is no notice
                # text". Baselining the tombstone would fingerprint a
                # non-document as authoritative content; failing the run closed
                # would take FINRA monitoring down permanently for a condition
                # that will never clear. Drop the item, record it, continue.
                detail_fetches += 1
                unavailable_cache[url] = str(exc)
                unavailable_notices.append(
                    {
                        "document_id": document_id,
                        "title": title,
                        "url": url,
                        "reason": str(exc),
                    }
                )
                logger.warning(
                    "Skipping FINRA notice %s: source declares no notice text "
                    "(%s); excluded from classification and baseline",
                    document_id,
                    exc,
                )
                continue
            if fetched_new:
                detail_fetches += 1
            notice_body_text = fallback_text
            presentation_excerpt = fallback_text[:FALLBACK_TEXT_MAX_CHARS]
            # A FINRA notice body is authoritative full text, exactly like the
            # Federal Register raw document, so it gets the same reference-only
            # filtering: a notice that only *cites* an AI paper must not be
            # promoted, and must not be mapped onto controls it never touches.
            tier, reason = classify_regulatory_relevance(
                title,
                notice_body_text,
                config,
                exclude_reference_only=True,
            )

        affected_controls = find_affected_controls_by_keywords(
            title,
            notice_body_text,
            config,
            exclude_reference_only=bool(notice_body_text),
        )

        item = RegulatoryItem(
            source='FINRA',
            agency='FINRA',
            title=title,
            url=url,
            publication_date=publication_date,
            doc_type='NOTICE',
            abstract=presentation_excerpt,
            content_text=notice_body_text,
            document_id=document_id,
            publication_date_is_synthetic=publication_date_is_synthetic,
            classification=tier,
            classification_reason=reason,
            affected_controls=affected_controls,
        )
        items.append(item)

    return items


def _parse_finra_publication_date(raw_value: str) -> str:
    """Return an ISO date from FINRA metadata, or an empty string if invalid."""
    value = (raw_value or "").strip()
    if not value:
        return ""

    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return ""


def _derive_finra_publication_date(link, url: str) -> tuple[str, bool]:
    """Return ``(date, is_synthetic)`` for a FINRA notice.

    The listing's row-level ``time[datetime]`` value is authoritative. FINRA
    information-notice URLs also encode a full publication date. Older
    regulatory-notice URLs encode only a year, so their January 1 fallback
    remains explicitly synthetic; opaque URLs retain the observed run date as
    a display fallback, but synthetic dates are excluded from fingerprints.
    """
    row = link.find_parent("tr")
    if row:
        time_node = row.find("time", datetime=True)
        if time_node:
            publication_date = _parse_finra_publication_date(time_node.get("datetime", ""))
            if publication_date:
                return publication_date, False

    information_notice_match = FINRA_INFORMATION_NOTICE_DATE_PATTERN.search(url)
    if information_notice_match:
        compact_date = "".join(information_notice_match.groups())
        try:
            publication_date = datetime.strptime(compact_date, "%Y%m%d").date().isoformat()
            return publication_date, False
        except ValueError:
            logger.warning("FINRA information-notice URL contains an invalid date: %s", url)

    regulatory_notice_match = FINRA_NOTICE_ID_PATTERN.search(url)
    if regulatory_notice_match:
        return f"20{regulatory_notice_match.group(1)}-01-01", True

    return datetime.now(timezone.utc).strftime("%Y-%m-%d"), True


def _normalize_hash_field(text: str) -> str:
    """Collapse incidental whitespace for change-detection hashing.

    Federal Register abstracts (and fetched fallback bodies) churn cosmetically
    within the ``since_date`` window -- leading/trailing spaces, doubled spaces,
    and newline reflow -- without any substantive change. Hashing the raw text
    made those cosmetic edits flip the content hash and re-emit an otherwise
    unchanged item (observed: 17 Federal Register NOISE items re-reported). This
    normalization only strips/collapses whitespace; it does not lowercase, decode
    entities, or otherwise alter meaning, so a genuine wording change still
    produces a different hash and is still reported. Substantive relevance
    classification is computed separately (``classify_regulatory_relevance``) and
    is unaffected.
    """
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def _content_fingerprint(item: RegulatoryItem) -> str:
    """Hash every substantive field, including the complete authoritative body.

    Schema 2 layout: ``title|report_text|authoritative_body|publication_date``.

    ``abstract`` is the text shown in reports -- for FINRA a bounded excerpt of
    the notice, for Federal Register whichever text supplied the classification
    evidence. ``content_text`` is the complete normalized authoritative body and
    is hashed unconditionally, so a wording change after the excerpt bound (or a
    body revision behind an unchanged curated abstract) is always observable.
    Both are hashed because they can move independently. The ``abstract``
    fallback preserves compatibility for callers constructing legacy
    ``RegulatoryItem`` instances without ``content_text``.

    Synthetic FINRA dates are run metadata, not notice content. Keeping their
    field position but hashing an empty value preserves deterministic identity
    without allowing the daily fallback date to create false updates.
    """
    publication_date = (
        "" if item.publication_date_is_synthetic else item.publication_date
    )
    content_text = item.content_text or item.abstract
    return "|".join(
        _normalize_hash_field(part)
        for part in (item.title, item.abstract, content_text, publication_date)
    )


def _legacy_content_fingerprint(
    title: str,
    content: str,
    publication_date: str,
) -> str:
    """Rebuild a schema-1 fingerprint (``title|content|publication_date``)."""
    return "|".join(
        _normalize_hash_field(part)
        for part in (title, content, publication_date)
    )


def _schema_tagged_hash(fingerprint: str) -> str:
    """Return the stored form of a current-schema content hash."""
    return f"{CONTENT_HASH_SCHEMA_PREFIX}{compute_hash(fingerprint)}"


def _stored_hash_schema_version(stored_hash: str) -> int:
    """Return the schema version a stored entry declares.

    Untagged values are schema 1: they were written before the fingerprint
    layout was versioned, so their layout can only be inferred, never trusted.
    """
    match = CONTENT_HASH_SCHEMA_PATTERN.match(str(stored_hash or ""))
    if not match:
        return LEGACY_CONTENT_HASH_SCHEMA_VERSION
    try:
        return int(match.group(1))
    except ValueError:  # pragma: no cover - pattern guarantees digits
        return LEGACY_CONTENT_HASH_SCHEMA_VERSION


def _legacy_migration_hashes(
    source_key: str,
    item: RegulatoryItem,
    source_state: dict,
) -> set[str]:
    """Schema-1 hashes that *prove* the complete current content is unchanged.

    A legacy digest may only suppress a finding when it demonstrably covered
    the whole of the content now being compared. Two schema-1 shapes qualify:

    * the full-content fingerprint (schema 1 hashed ``content_text`` when the
      item carried one), and
    * for FINRA only, the pre-excerpt-fix fingerprint over the bounded
      ``abstract`` -- but *only* when that excerpt covers the complete body.
      FINRA's ``abstract`` is a deterministic prefix of ``content_text``, so an
      excerpt equal to the whole body proves the body, while a truncated
      excerpt proves nothing about the suffix and must not suppress anything.

    Everything else is unprovable and deliberately produces a one-time finding
    rather than a silent overwrite.
    """
    publication_date = (
        "" if item.publication_date_is_synthetic else item.publication_date
    )
    dates = {publication_date}
    contents = {item.content_text or item.abstract}

    if source_key == SOURCE_KEY_FINRA:
        # The pre-fix FINRA date fallback wrote a synthetic or run-date value
        # into the same field position.
        regulatory_notice_match = FINRA_NOTICE_ID_PATTERN.search(item.url or "")
        if regulatory_notice_match:
            dates.add(f"20{regulatory_notice_match.group(1)}-01-01")
        else:
            last_run_date = _parse_finra_publication_date(
                str(source_state.get("last_run") or "")
            )
            if last_run_date:
                dates.add(last_run_date)

        excerpt = item.abstract or ""
        body = item.content_text or item.abstract or ""
        if _normalize_hash_field(excerpt) == _normalize_hash_field(body):
            contents.add(excerpt)

    return {
        compute_hash(_legacy_content_fingerprint(item.title, content, date))
        for content in contents
        for date in dates
    }


def check_for_new_items(source_key: str, items: list[RegulatoryItem], source_state: dict) -> list[RegulatoryItem]:
    """
    Compare fetched items against source state to find new items.

    Args:
        source_key: Source key in unified state file
        items: List of fetched regulatory items
        source_state: Source-specific state dict

    Returns:
        list[RegulatoryItem]: New items not in state
    """
    new_items = []
    existing_entries = source_state.get('entries', {})

    for item in items:
        # Use document_id or URL as the key
        entry_key = item.document_id if item.document_id else item.url

        # Compute hash of the item content (whitespace-normalized so cosmetic
        # abstract churn within the since_date window does not re-emit an item).
        content_hash = _schema_tagged_hash(_content_fingerprint(item))

        # Check if this is a new item or changed item
        if entry_key not in existing_entries:
            logger.info(f"  New item: {item.title[:60]}... ({item.agency})")
            new_items.append(item)
            continue

        stored_hash = existing_entries[entry_key]
        if stored_hash == content_hash:
            continue

        stored_version = _stored_hash_schema_version(stored_hash)
        if stored_version < CONTENT_HASH_SCHEMA_VERSION and stored_hash in (
            _legacy_migration_hashes(source_key, item, source_state)
        ):
            # A legacy digest that provably covered the complete content: the
            # schema changed, the content did not. Migrate silently; the entry
            # is rewritten under the current schema by update_source_state.
            logger.info(
                "  Migrating schema-%s entry with unchanged content: %s",
                stored_version,
                entry_key,
            )
            continue

        # Either a genuine change, or a legacy digest that cannot prove the
        # complete content is unchanged. Surface it once rather than silently
        # overwriting a change that may hide behind a truncated legacy excerpt.
        logger.info(f"  Updated item: {item.title[:60]}... ({item.agency})")
        new_items.append(item)

    return new_items


def _sort_regulatory_items(items: list[RegulatoryItem]) -> list[RegulatoryItem]:
    """Return items in a stable source/date/identity order."""
    source_order = {"Federal Register": 0, "FINRA": 1}
    ordered = sorted(
        items,
        key=lambda item: (
            item.document_id or item.url,
            item.title,
            item.agency,
        ),
        reverse=True,
    )
    ordered = sorted(
        ordered,
        key=lambda item: item.publication_date or "",
        reverse=True,
    )
    return sorted(
        ordered,
        key=lambda item: source_order.get(item.source, len(source_order)),
    )


def update_source_state(source_key: str, items: list[RegulatoryItem], state: dict) -> None:
    """
    Update source state with new item hashes.

    Args:
        source_key: Source key in unified state file
        items: List of regulatory items to add to state
        state: Full state dict (modified in place)
    """
    source_state = get_source_state(state, source_key)
    entries = source_state.get('entries', {})

    for item in _sort_regulatory_items(items):
        entry_key = item.document_id if item.document_id else item.url
        entries[entry_key] = _schema_tagged_hash(_content_fingerprint(item))

    source_state['entries'] = entries
    source_state['last_run'] = datetime.now(timezone.utc).isoformat()

    set_source_state(state, source_key, source_state)


def _validate_report_counts(
    all_new_items: list[RegulatoryItem],
    source_counts: Optional[dict[str, dict[str, int]]],
) -> Optional[dict[str, int]]:
    """Validate fetched/new accounting before a report is written."""
    if source_counts is None:
        return None

    new_by_source: dict[str, int] = {}
    for item in all_new_items:
        new_by_source[item.source] = new_by_source.get(item.source, 0) + 1

    fetched_total = 0
    new_total = 0
    for source, counts in source_counts.items():
        if not isinstance(counts, dict):
            raise ValueError(f"Report counts for {source!r} must be an object")
        fetched = counts.get("fetched")
        new = counts.get("new")
        if (
            isinstance(fetched, bool)
            or isinstance(new, bool)
            or not isinstance(fetched, int)
            or not isinstance(new, int)
            or fetched < 0
            or new < 0
            or new > fetched
        ):
            raise ValueError(f"Invalid fetched/new report counts for {source!r}")
        expected_new = new_by_source.get(source, 0)
        if new != expected_new:
            raise ValueError(
                f"Report new count for {source!r} was {new}, "
                f"but {expected_new} new records were classified"
            )
        fetched_total += fetched
        new_total += new

    if set(new_by_source) - set(source_counts):
        raise ValueError("Report counts omitted a source with classified records")
    if new_total != len(all_new_items):
        raise ValueError(
            f"Report new count was {new_total}, "
            f"but {len(all_new_items)} records were classified"
        )

    return {
        "fetched": fetched_total,
        "new": new_total,
        "classified": len(all_new_items),
    }


def generate_regulatory_report(
    all_new_items: list[RegulatoryItem],
    report_path: Path,
    source_counts: Optional[dict[str, dict[str, int]]] = None,
) -> None:
    """
    Generate regulatory change report using shared report format helpers.

    Args:
        all_new_items: All new regulatory items from all sources
        report_path: Path to write report
    """
    report_counts = _validate_report_counts(all_new_items, source_counts)
    ordered_items = _sort_regulatory_items(all_new_items)

    # Categorize by classification tier
    critical_items = [item for item in ordered_items if item.classification == CLASSIFICATION_CRITICAL]
    high_items = [item for item in ordered_items if item.classification == CLASSIFICATION_HIGH]
    medium_items = [item for item in ordered_items if item.classification == CLASSIFICATION_MEDIUM]
    noise_items = [item for item in ordered_items if item.classification == CLASSIFICATION_NOISE]
    classified_count = len(critical_items) + len(high_items) + len(medium_items) + len(noise_items)
    if classified_count != len(all_new_items):
        raise ValueError("Report contains an item with an unknown classification")

    # Build report content
    lines = []

    # Header
    run_date = datetime.now(timezone.utc).isoformat(timespec='seconds')
    metadata = {
        "New Items": len(all_new_items),
        "Classified Items": classified_count,
        "Sources": "Federal Register (SEC, CFTC, OCC, Federal Reserve) + FINRA Regulatory Notices",
    }
    if report_counts is not None:
        metadata["Fetched Items"] = report_counts["fetched"]
        for source in sorted(source_counts):
            metadata[f"{source} Fetched"] = source_counts[source]["fetched"]
            metadata[f"{source} New"] = source_counts[source]["new"]

    lines.append(generate_report_header(
        title="Regulatory Monitor Report",
        run_date=run_date,
        metadata=metadata,
    ))

    # Executive summary
    lines.append(generate_executive_summary({
        'CRITICAL': len(critical_items),
        'HIGH': len(high_items),
        'MEDIUM': len(medium_items),
        'NOISE': len(noise_items),
    }))

    # Summary table (for CRITICAL + HIGH only, for quick scanning)
    priority_items = critical_items + high_items
    if priority_items:
        lines.append("## Summary (Quick Scan)\n")
        lines.append("| # | Source | Agency | Classification | Affected Controls | Action |\n")
        lines.append("|---|--------|--------|----------------|-------------------|--------|\n")

        for i, item in enumerate(priority_items, 1):
            # Shorten URL for table
            url_short = item.title[:40] + "..." if len(item.title) > 40 else item.title
            controls = ", ".join(item.affected_controls) if item.affected_controls else "None identified"
            action = "Review and update framework" if item.classification == CLASSIFICATION_CRITICAL else "Review"

            lines.append(f"| {i} | {item.source} | {item.agency} | {item.classification} | {controls} | {action} |\n")

        lines.append("\n")

    # CRITICAL items (detailed)
    if critical_items:
        lines.append("## CRITICAL Items\n")
        lines.append("These regulatory changes directly mention AI agents, copilot, or automated advice in FSI context.\n\n")

        for i, item in enumerate(critical_items, 1):
            lines.append(f"### {i}. [{item.title}]({item.url})\n\n")
            lines.append(f"- **Source:** {item.agency} via {item.source}\n")
            lines.append(f"- **Published:** {item.publication_date}\n")
            if item.doc_type:
                lines.append(f"- **Type:** {item.doc_type}\n")
            lines.append(f"- **Classification:** {item.classification} — {item.classification_reason}\n")

            if item.abstract:
                lines.append(f"- **Abstract:** {item.abstract[:500]}{'...' if len(item.abstract) > 500 else ''}\n")

            if item.affected_controls:
                lines.append(f"- **Potentially Affected Controls:**\n")
                for control in item.affected_controls:
                    lines.append(f"  - Control {control}\n")

            lines.append("\n")

    # HIGH items (detailed)
    if high_items:
        lines.append("## HIGH Priority Items\n")
        lines.append("These regulatory changes reference AI, ML, automation, or FSI-specific requirements relevant to Copilot governance.\n\n")

        for i, item in enumerate(high_items, 1):
            lines.append(f"### {i}. [{item.title}]({item.url})\n\n")
            lines.append(f"- **Source:** {item.agency} via {item.source}\n")
            lines.append(f"- **Published:** {item.publication_date}\n")
            if item.doc_type:
                lines.append(f"- **Type:** {item.doc_type}\n")
            lines.append(f"- **Classification:** {item.classification} — {item.classification_reason}\n")

            if item.abstract:
                lines.append(f"- **Abstract:** {item.abstract[:300]}{'...' if len(item.abstract) > 300 else ''}\n")

            if item.affected_controls:
                lines.append(f"- **Potentially Affected Controls:** {', '.join(item.affected_controls)}\n")

            lines.append("\n")

    # MEDIUM items (abbreviated)
    if medium_items:
        lines.append("## MEDIUM Priority Items\n")
        lines.append("General FSI regulations that may indirectly affect AI agent deployments.\n\n")

        for item in medium_items:
            lines.append(f"- [{item.title}]({item.url}) ({item.agency}, {item.publication_date})\n")

        lines.append("\n")

    # NOISE items (list only)
    if noise_items:
        lines.append("## NOISE Items\n")
        lines.append("Regulatory items with no FSI Copilot governance relevance.\n\n")

        for item in noise_items:
            lines.append(f"- [{item.title}]({item.url}) ({item.agency})\n")

        lines.append("\n")

    # Write report
    content = "".join(lines)
    write_report(content, REPORTS_DIR, report_path.name)
    logger.info(f"Report written to {report_path}")


def _run_monitor() -> int:
    """Execute the monitor and return a contract exit code."""
    parser = argparse.ArgumentParser(
        description="Monitor regulatory changes from Federal Register and FINRA"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Fetch and analyze without updating state file"
    )
    parser.add_argument(
        '--limit',
        type=int,
        help="Limit number of items per source (limited runs never update state)"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Enable verbose output"
    )
    parser.add_argument(
        '--source',
        choices=['federal-register', 'finra', 'all'],
        default='all',
        help="Which source(s) to monitor"
    )
    parser.add_argument(
        '--config',
        type=str,
        default=None,
        help='Path to config file (default: scripts/config/monitoring-config.yaml)'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate config file and exit without running'
    )

    args = parser.parse_args()

    # Setup logging
    global logger
    logger = setup_logging(verbose=args.verbose)

    # Load and validate config
    config_path = args.config or DEFAULT_CONFIG_PATH
    config = load_monitoring_config(config_path)

    if args.validate:
        is_valid, errors = validate_config(config)
        if is_valid:
            print(f"Config valid: {config_path}")
            return EXIT_CLEAN
        else:
            print(f"Config errors in {config_path}:")
            for err in errors:
                print(f"  - {err}")
            return EXIT_FAILURE

    logger.info("=== Regulatory Monitor ===")
    logger.info(f"Source: {args.source}")
    logger.info(f"Dry run: {args.dry_run}")
    logger.info(f"Config: {config_path}")
    if args.limit is not None:
        logger.info(f"Limit: {args.limit} items per source")
        logger.info("Limited run: state and watermark updates are disabled")

    # Ensure directories exist
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load unified state
    state = load_state(STATE_FILE)
    state_mutation_allowed = not args.dry_run and args.limit is None

    # Graceful degradation: --dry-run skips all network calls so the script
    # can be smoke-tested in CI environments without outbound access.
    if args.dry_run:
        logger.info("Dry run: skipping all network calls (offline mode)")
        print("INFO: regulatory_monitor dry-run — network calls skipped (offline mode).")
        return EXIT_CLEAN

    # Create session
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'FSI-CopilotGov-Regulatory-Monitor/1.0 (https://github.com/judeper/FSI-CopilotGov)'
    })

    all_new_items = []
    source_counts: dict[str, dict[str, int]] = {}

    # Fetch from Federal Register
    if args.source in ['federal-register', 'all']:
        logger.info("\n--- Federal Register ---")
        fed_state = get_source_state(state, SOURCE_KEY_FEDERAL_REGISTER)

        # Determine since_date (last check or 30 days ago)
        since_date = fed_state.get('last_checked')
        if not since_date:
            since_date = (datetime.now(timezone.utc) - timedelta(days=30)).strftime('%Y-%m-%d')
            logger.info(f"No prior state, fetching documents from last 30 days")
        else:
            logger.info(f"Fetching documents since {since_date}")

        fed_items = fetch_federal_register_documents(session, since_date, config, limit=args.limit)
        new_fed_items = check_for_new_items(SOURCE_KEY_FEDERAL_REGISTER, fed_items, fed_state)
        source_counts["Federal Register"] = {
            "fetched": len(fed_items),
            "new": len(new_fed_items),
        }

        logger.info(f"Federal Register: {len(new_fed_items)} new items")
        all_new_items.extend(new_fed_items)

        # Update state
        if state_mutation_allowed:
            update_source_state(SOURCE_KEY_FEDERAL_REGISTER, fed_items, state)
            # Update last_checked to today
            fed_state = get_source_state(state, SOURCE_KEY_FEDERAL_REGISTER)
            fed_state['last_checked'] = datetime.now(timezone.utc).strftime('%Y-%m-%d')
            set_source_state(state, SOURCE_KEY_FEDERAL_REGISTER, fed_state)

    # Fetch from FINRA
    if args.source in ['finra', 'all']:
        logger.info("\n--- FINRA Notices ---")
        finra_state = get_source_state(state, SOURCE_KEY_FINRA)

        finra_unavailable: list[dict] = []
        finra_items = fetch_finra_notices(
            session, config, limit=args.limit, unavailable_notices=finra_unavailable
        )
        new_finra_items = check_for_new_items(SOURCE_KEY_FINRA, finra_items, finra_state)
        source_counts["FINRA"] = {
            "fetched": len(finra_items),
            "new": len(new_finra_items),
            "unavailable": len(finra_unavailable),
        }
        if finra_unavailable:
            logger.warning(
                "FINRA: %s notice(s) excluded from the baseline because the "
                "source declares no available text: %s",
                len(finra_unavailable),
                ", ".join(
                    str(entry.get("document_id") or entry.get("url"))
                    for entry in finra_unavailable
                ),
            )

        logger.info(f"FINRA: {len(new_finra_items)} new items")
        all_new_items.extend(new_finra_items)

        # Update state
        if state_mutation_allowed:
            update_source_state(SOURCE_KEY_FINRA, finra_items, state)

    # Generate report if new items found
    if all_new_items:
        logger.info(f"\n=== {len(all_new_items)} total new regulatory items detected ===")

        report_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        report_path = REPORTS_DIR / f"regulatory-changes-{report_date}.md"

        generate_regulatory_report(
            all_new_items,
            report_path,
            source_counts=source_counts,
        )

        # Save state
        if state_mutation_allowed:
            save_state_atomic(state, STATE_FILE)
            logger.info(f"State updated: {STATE_FILE}")
        else:
            logger.info("State not updated (dry-run or limited run)")

        return EXIT_FINDINGS

    else:
        logger.info("\n=== No new regulatory items detected ===")

        # Save state even if no changes (updates last_run timestamps)
        if state_mutation_allowed:
            save_state_atomic(state, STATE_FILE)
        else:
            logger.info("State not updated (dry-run or limited run)")

        return EXIT_CLEAN


def main() -> int:
    """Run the monitor without allowing source/execution failures to escape."""
    try:
        return _run_monitor()
    except SystemExit as exc:
        if exc.code == EXIT_CLEAN:
            return EXIT_CLEAN
        logger.error("Monitor terminated before completion with exit code %s", exc.code)
        return EXIT_FAILURE
    except Exception as exc:
        logger.error("Fatal error: %s", exc)
        logger.debug("Traceback:", exc_info=True)
        return EXIT_FAILURE


if __name__ == '__main__':
    raise SystemExit(main())
