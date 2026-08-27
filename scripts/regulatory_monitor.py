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
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

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
FINRA_NOTICE_PATH_PATTERN = re.compile(
    r'^/rules-guidance/notices/(?:\d{2}-\d+|information-notice-\d{8})/?$',
    re.IGNORECASE,
)
FINRA_NOTICE_ID_PATTERN = re.compile(
    r'/rules-guidance/notices/(\d{2})-(\d+)(?:[/?#]|$)',
    re.IGNORECASE,
)
FINRA_INFORMATION_NOTICE_DATE_PATTERN = re.compile(
    r'/rules-guidance/notices/information-notice-(\d{4})(\d{2})(\d{2})(?:[/?#]|$)',
    re.IGNORECASE,
)

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

REFERENCE_ONLY_PATTERN = re.compile(
    r"(?:\bsee\s+(?:also|generally|supra|infra)\b|\bsee,\s*e\.g\.|\bsupra\b|\bid\.\s|\bibid\b"
    r"|\bcf\.\s|\bet\s+al\.|\bavailable\s+at\b|https?://|\bwww\.|\bcit(?:ed|ing|ation)\b"
    r"|\b(?:an|another|one|a|the|this|these|those|recent|prior|earlier|academic|empirical|several)\s+"
    r"[a-z ,'-]{0,26}?(?:study|studies|paper|papers|article|articles|survey|working\s+paper)\b"
    r"|\bstudies\s+(?:have\s+)?(?:found|find|show|shown|suggest|document)"
    r"|\bresearchers?\b|\bthe\s+literature\b|\bjournal\b|\bworking\s+paper\b)",
    re.IGNORECASE,
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
)
OPTIONAL_OR_NEGATED_RECORDKEEPING = re.compile(
    r"\b(?:optional|optionally|permitted|may|can|could|might|"
    r"not\s+required|need\s+not|not\s+obligated|not\s+mandatory|"
    r"must\s+not|shall\s+not|paper|physical|hard[-\s]?copy)\b",
    re.IGNORECASE,
)

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


def _prepare_classification_text(text: str) -> str:
    """Normalize escaped line breaks in source text used for classification.

    Federal Register raw text sometimes carries literal ``\\n``/``\\r`` escape
    sequences that would otherwise weld two words together and hide a match.
    No part of the document is dropped: relevance is decided by context, not by
    position (see ``_is_reference_only_occurrence``).
    """
    text = text or ""
    return text.replace("\\r", " ").replace("\\n", " ")


def _occurrence_context(text: str, start: int, end: int) -> str:
    """Return the local context of a match, clipped to its own sentence/clause.

    Unlike the old fixed-size context window, this scans to the actual
    sentence/clause boundaries.  That matters for long sentences such as the
    2026-17183 citation sentence, where the literature marker can be more than
    200 characters before the artificial-intelligence occurrence.
    """
    preceding_delimiters = list(
        FOOTNOTE_BLOCK_DELIMITER_PATTERN.finditer(text, 0, start)
    )
    segment_start = (
        preceding_delimiters[-1].end() if preceding_delimiters else 0
    )
    following_delimiter = FOOTNOTE_BLOCK_DELIMITER_PATTERN.search(text, end)
    segment_end = (
        following_delimiter.start() if following_delimiter else len(text)
    )

    preceding_boundaries = list(
        SENTENCE_BOUNDARY_PATTERN.finditer(text, segment_start, start)
    )
    if preceding_boundaries:
        segment_start = preceding_boundaries[-1].end()

    following_boundary = SENTENCE_BOUNDARY_PATTERN.search(
        text, end, segment_end
    )
    if following_boundary:
        segment_end = following_boundary.start()

    return text[segment_start:segment_end]


def _is_reference_only_occurrence(text: str, start: int, end: int) -> bool:
    """Return True when a match sits in bibliography/citation-only context.

    The check is deliberately asymmetric and fails open toward "operative":
    any obligation language in the containing sentence/clause keeps the match,
    and a match is only discarded when that complete clause carries an explicit
    citation or literature-review marker. Missing a genuine requirement is far
    worse than reporting an extra item, and inline footnote markers alone
    (``\\4\\``) are not treated as evidence because operative Federal Register
    text is full of them.
    """
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


def _has_electronic_recordkeeping_obligation(text: str) -> bool:
    """Return whether text contains a direct electronic recordkeeping duty.

    This intentionally requires one readable construction that ties together:
    a recordkeeping noun, an obligation, a storage/maintenance action, and
    electronic/digital storage language.  Each regex is bounded by sentence
    and semicolon clause terminators, so ``electronic communications`` or an
    unrelated electronic filing cannot satisfy a records obligation.  Clauses
    containing explicit optional, permissive, negated, or paper-only wording
    are rejected.
    """
    normalized = _prepare_classification_text(text)
    for clause in re.split(r"[.!?;]+", normalized):
        clause = re.sub(r"\s+", " ", clause).strip()
        if not clause:
            continue

        for pattern in ELECTRONIC_RECORDKEEPING_PATTERNS:
            match = pattern.search(clause)
            if not match:
                continue

            matched_text = match.group(0)
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
    combined = f"{title.lower()} {classification_text.lower()}"

    # Get regulatory patterns from config
    regulatory_config = config.get('regulatory', {})

    # CRITICAL: Directly mentions AI agents, copilot, or automated advice in FSI context
    critical_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('critical_patterns', [])
    ]
    for pattern, reason in critical_patterns:
        if _search_operative_match(pattern, combined, exclude_reference_only):
            return (CLASSIFICATION_CRITICAL, reason)

    # HIGH: AI, ML, automation terms + FSI-specific requirements
    high_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('high_patterns', [])
    ]
    for pattern, reason in high_patterns:
        if _search_operative_match(pattern, combined, exclude_reference_only):
            return (CLASSIFICATION_HIGH, reason)

    if _has_electronic_recordkeeping_obligation(combined):
        return (CLASSIFICATION_HIGH, "Electronic recordkeeping")

    # MEDIUM: General FSI regulations that may indirectly affect AI agents
    medium_patterns = [
        (p['pattern'], p['reason'])
        for p in regulatory_config.get('medium_patterns', [])
    ]
    for pattern, reason in medium_patterns:
        if _search_operative_match(pattern, combined, exclude_reference_only):
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
    combined = f"{title.lower()} {abstract.lower()}"
    affected = set()

    # Build keyword map from config
    keyword_map = {
        entry['keyword']: [c['id'] for c in entry['controls']]
        for entry in config.get('keyword_control_map', [])
    }

    for keyword, controls in keyword_map.items():
        # Use word boundary matching to avoid partial matches
        pattern = rf'\b{re.escape(keyword.lower())}\b'
        if _search_operative_match(pattern, combined, exclude_reference_only):
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


def _extract_federal_register_source_text(text: str) -> str:
    """Normalize the authoritative Federal Register raw-text document."""
    soup = BeautifulSoup(text or "", "html.parser")
    preformatted_text = soup.find("pre")
    source_text = (
        preformatted_text.get_text(" ", strip=True)
        if preformatted_text
        else soup.get_text(" ", strip=True)
    )
    return re.sub(r"\s+", " ", source_text).strip()


def _extract_finra_notice_fallback_text(html: str) -> str:
    """Extract the complete normalized text of the FINRA notice body.

    FINRA pages can contain a login or access-message ``field--name-body``
    before the actual notice article.  Never select the first generic body
    field: prefer semantic article-body/notice-body fields, then scoped fields
    inside a notice article or ``main`` element.  A page without one of those
    scoped containers returns an empty string so the caller fails closed.
    """
    soup = BeautifulSoup(html or "", "html.parser")
    candidates: list[tuple[int, int, str]] = []
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
        text = normalized_node_text(node)
        if not text:
            return
        # A short access/login message is page chrome, not authoritative notice
        # content.  It must not win over a scoped notice candidate.
        if re.search(
            r"\b(?:please\s+)?(?:log\s*in|sign\s*in|login)\b",
            text,
            re.IGNORECASE,
        ) and (len(text) < 500 or score <= 40):
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

    # Some FINRA templates expose the notice directly under main without an
    # article element.  Keep this fallback scoped to main and its body fields;
    # never fall back to the entire document body.
    for selector in (
        "main [itemprop='articleBody']",
        "main .notice-body",
        "main .field--name-field-notice-body",
        "main .field--name-field-body",
        "main .field--name-body",
    ):
        for node in soup.select(selector):
            add_candidate(node, 90)
    for node in soup.select("main"):
        add_candidate(node, 60)

    # A few older FINRA pages expose multiple generic body fields without a
    # semantic article wrapper. Treat the longest non-login body field as a
    # low-confidence fallback, never as a whole-document fallback.
    for node in soup.select("[class*='field--name-body']"):
        add_candidate(node, 40)

    if not candidates:
        return ""
    _, _, text = max(candidates, key=lambda candidate: (candidate[0], candidate[1]))
    return text


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
    """Consult authoritative full text for any item that could still change tier.

    A curated abstract is only a summary, so a MEDIUM (or even NOISE) abstract
    can hide HIGH/CRITICAL operative language in the body. The only tier that
    cannot be raised is CRITICAL -- it is the ceiling -- so authoritative text
    is fetched for every classification except CRITICAL.
    """
    return classification != CLASSIFICATION_CRITICAL


def _federal_register_authoritative_text_required(abstract_classification: str) -> bool:
    """Whether authoritative full text is mandatory (fail closed) for an item.

    When the abstract yields no usable signal (NOISE/blank) there is no curated
    evidence to fall back on, so classification cannot proceed without the
    authoritative body and must fail closed if it is unavailable. When the
    abstract already carries curated MEDIUM/HIGH evidence, the authoritative
    fetch is best-effort: it may only ever raise the tier, never downgrade it,
    and a fetch failure leaves the abstract classification intact.
    """
    return abstract_classification == CLASSIFICATION_NOISE


def _should_fetch_finra_notice_detail(title: str, url: str, classification: str) -> bool:
    """Return whether an eligible FINRA notice needs authoritative detail.

    Classification and title are deliberately not used as a shortcut.  A
    listing title is not authoritative notice content, and skipping a high
    title or an older/information notice would allow an uninspected item into
    the baseline.  URL eligibility is established by the listing parser.
    """
    return _canonical_finra_notice_url(url) is not None


def _canonical_finra_notice_url(raw_url: str) -> Optional[str]:
    """Return a stable FINRA notice URL for supported listing links."""
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
    if not FINRA_NOTICE_PATH_PATTERN.fullmatch(path):
        return None

    return f"https://www.finra.org{path.rstrip('/')}"


def _extract_finra_notice_links(content: str | bytes) -> list:
    """Enumerate and deduplicate eligible links from a FINRA listing.

    FINRA renders notices in table rows/list items and may repeat the same
    detail URL in a title link and a secondary view link.  Filtering every
    anchor by the supported notice URL shapes avoids broad-container
    first-link loss while preserving DOM order and one link per notice.
    """
    soup = BeautifulSoup(content, "html.parser")
    links_by_url: dict[str, object] = {}

    def link_quality(link) -> tuple[int, int]:
        title = re.sub(r"\s+", " ", link.get_text(" ", strip=True)).strip()
        row = link.find_parent("tr")
        has_row_date = int(
            bool(row and row.find("time", datetime=True))
        )
        return has_row_date, len(title)

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
        if existing is None or link_quality(link) > link_quality(existing):
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
        # A NOISE/blank abstract cannot be classified without the authoritative
        # body, so exhausting the fetch budget before reaching it must fail
        # closed. A MEDIUM/HIGH abstract already carries curated evidence, so a
        # best-effort fetch that cannot run simply leaves that evidence in place.
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
                source_tier, source_reason = classify_regulatory_relevance(
                    title,
                    fallback_text,
                    config,
                    exclude_reference_only=True,
                )
                # Deterministic precedence: the more severe of the curated
                # abstract and the authoritative body wins, and ties go to the
                # authoritative body (it is the source of record). Because only a
                # source tier that meets or exceeds the abstract tier is adopted,
                # a failed or weaker authoritative read can never downgrade
                # legitimate abstract evidence.
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
            content_text=effective_text,
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
) -> list[RegulatoryItem]:
    """
    Scrape FINRA regulatory notices page.

    Args:
        session: requests.Session instance
        config: Configuration dict for classification
        limit: Maximum notices to fetch (for testing)
        detail_fetch_limit: Optional safety limit for tests.  Production uses
            ``None`` and fetches every eligible notice body.

    Returns:
        list[RegulatoryItem]: FINRA notices
    """
    items = []
    _, max_retries, request_delay = _get_operational_settings(config)

    logger.info(f"Fetching FINRA notices from {FINRA_NOTICES_URL}...")
    try:
        result = fetch_page(FINRA_NOTICES_URL, session, max_retries=max_retries)
    except Exception as exc:
        raise FinraListingError("FINRA notices page request failed") from exc

    if not isinstance(result, dict):
        raise FinraListingError("FINRA notices page request returned an invalid result")

    status_code = result.get('status_code')
    if status_code != 200:
        error_detail = result.get("error")
        logger.error(f"FINRA notices page returned status {status_code}")
        if error_detail:
            logger.error("FINRA notices fetch error: %s", error_detail)
        raise FinraListingError(
            f"FINRA notices page request failed with status {status_code}"
        )

    content = result.get('content')
    if not isinstance(content, (str, bytes)):
        raise FinraListingError("FINRA notices page parsing failed: invalid content")

    try:
        notice_links = _extract_finra_notice_links(content)
    except Exception as exc:
        raise FinraListingError("FINRA notices page parsing failed") from exc

    if not notice_links:
        raise FinraListingError(
            "FINRA notices page returned no regulatory notice links"
        )

    logger.info(f"Found {len(notice_links)} FINRA notice links")

    if limit:
        notice_links = notice_links[:limit]
        logger.info(f"Limited to {limit} notices for testing")

    detail_cache: dict[str, str] = {}
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
            fallback_text, fetched_new = _fetch_cached_fallback_text(
                url=url,
                session=session,
                cache=detail_cache,
                request_delay=request_delay,
                max_retries=max_retries,
                extractor=_extract_finra_notice_fallback_text,
                required=True,
                source_label="FINRA authoritative notice body",
            )
            if fetched_new:
                detail_fetches += 1
            notice_body_text = fallback_text
            presentation_excerpt = fallback_text[:FALLBACK_TEXT_MAX_CHARS]
            tier, reason = classify_regulatory_relevance(
                title, notice_body_text, config
            )

        affected_controls = find_affected_controls_by_keywords(
            title, notice_body_text, config
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
    """Hash the complete normalized content, not the report excerpt.

    FINRA items keep a bounded ``abstract`` for report readability, while
    ``content_text`` retains the complete authoritative body.  Hashing the
    latter makes wording changes after character 4000 observable.  The
    ``abstract`` fallback preserves compatibility for callers constructing
    legacy ``RegulatoryItem`` instances without ``content_text``.

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
        for part in (item.title, content_text, publication_date)
    )


def _legacy_finra_content_hashes(
    item: RegulatoryItem,
    source_state: dict,
) -> set[str]:
    """Return hashes emitted by the pre-fix FINRA date fallback behavior."""
    legacy_dates = set()

    regulatory_notice_match = FINRA_NOTICE_ID_PATTERN.search(item.url or "")
    if regulatory_notice_match:
        legacy_dates.add(f"20{regulatory_notice_match.group(1)}-01-01")
    else:
        last_run_date = _parse_finra_publication_date(
            str(source_state.get("last_run") or "")
        )
        if last_run_date:
            legacy_dates.add(last_run_date)

    return {
        compute_hash("|".join(
            _normalize_hash_field(part)
            for part in (item.title, item.abstract, legacy_date)
        ))
        for legacy_date in legacy_dates
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
        content_hash = compute_hash(_content_fingerprint(item))

        # Check if this is a new item or changed item
        if entry_key not in existing_entries:
            logger.info(f"  New item: {item.title[:60]}... ({item.agency})")
            new_items.append(item)
        elif (
            existing_entries[entry_key] != content_hash
            and (
                source_key != SOURCE_KEY_FINRA
                or existing_entries[entry_key]
                not in _legacy_finra_content_hashes(item, source_state)
            )
        ):
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
        entries[entry_key] = compute_hash(_content_fingerprint(item))

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

        finra_items = fetch_finra_notices(session, config, limit=args.limit)
        new_finra_items = check_for_new_items(SOURCE_KEY_FINRA, finra_items, finra_state)
        source_counts["FINRA"] = {
            "fetched": len(finra_items),
            "new": len(new_finra_items),
        }

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
