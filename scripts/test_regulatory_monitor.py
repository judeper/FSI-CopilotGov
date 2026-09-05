"""Regression tests for FINRA/Federal Register regulatory monitoring logic."""
from __future__ import annotations

from copy import deepcopy
import json
import logging
import re
import sys
import time
from pathlib import Path

import pytest
import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import regulatory_monitor  # noqa: E402
import monitoring_shared  # noqa: E402

CONFIG_PATH = REPO_ROOT / "scripts" / "config" / "monitoring-config.yaml"


def _load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


# Neutral authoritative body served by the offline guard. Deliberately free of
# AI, automation, and recordkeeping vocabulary so it always classifies NOISE.
OFFLINE_AUTHORITATIVE_BODY = (
    "Offline placeholder authoritative source text for regression fixtures."
)


def _finra_notice_page(body: str, *, node_type: str = "notice") -> str:
    """Return live-shaped FINRA notice detail markup.

    A bare ``<main>`` is not a notice body: FINRA serves access-denied,
    challenge, login, and not-found pages inside a populated ``<main>``, so the
    extractor requires a notice article/body container. Valid fixtures use the
    real Drupal shape.
    """
    return (
        "<html><body><main>"
        f"<article class='node node--type-{node_type}'>"
        "<h1>Regulatory Notice</h1>"
        f"<div class='field field--name-body'>{body}</div>"
        "</article>"
        "</main></body></html>"
    )


def _with_finra_canonical(content, url):
    """Stamp a notice detail page with the ``rel=canonical`` live FINRA emits.

    Verified against production: ``https://www.finra.org/rules-guidance/
    notices/26-12`` returns ``<link rel="canonical" href="https://www.finra.org
    /rules-guidance/notices/26-12" />``. Detail identity now fails closed when
    a page declares nothing about itself, so a fixture that omits the canonical
    is not a "simpler" notice page -- it is an *unidentified* one, which is the
    exact condition the monitor must refuse. Stubs stamp it the way the source
    does rather than each test restating it.

    Only notice detail URLs are stamped, only when the fixture does not already
    declare an identity (so mismatch/redirect fixtures keep their own), and
    only for ``str`` content.
    """
    if not isinstance(content, str):
        return content
    canonical = regulatory_monitor._canonical_finra_notice_url(url)
    if canonical is None:
        return content
    if re.search(r"rel=[\"']canonical[\"']|og:url", content, re.IGNORECASE):
        return content
    tag = f'<link rel="canonical" href="{canonical}" />'
    if re.search(r"<head[^>]*>", content, re.IGNORECASE):
        return re.sub(r"(<head[^>]*>)", r"\1" + tag, content, count=1,
                      flags=re.IGNORECASE)
    if re.search(r"<html[^>]*>", content, re.IGNORECASE):
        return re.sub(r"(<html[^>]*>)", r"\1<head>" + tag + "</head>", content,
                      count=1, flags=re.IGNORECASE)
    return f"<head>{tag}</head>{content}"


@pytest.fixture(autouse=True)
def _offline_network_guard(monkeypatch):
    """Default every test to an offline, no-op network layer.

    Federal Register classification consults authoritative full text for
    *every* item and fails closed when that text is unavailable, so a fixture
    that builds documents without wiring a ``fetch_page`` stub would otherwise
    reach the real network -- or fail closed for the wrong reason. This
    provides a safe offline default: a valid 200 response carrying a neutral
    authoritative body with no AI or recordkeeping vocabulary, so it classifies
    NOISE and never raises or lowers a fixture's tier. Tests that exercise
    fetch behavior set their own ``fetch_page`` in the test body, which runs
    after this fixture and therefore overrides it.
    """

    def _offline_fetch_page(url, *_args, **_kwargs):
        return {
            "url": url,
            "status_code": 200,
            "content": (
                "<html><body><pre>"
                f"{OFFLINE_AUTHORITATIVE_BODY}"
                "</pre></body></html>"
            ),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", _offline_fetch_page)
    monkeypatch.setattr(
        regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None
    )


def test_exit_code_contract_is_unambiguous():
    assert regulatory_monitor.EXIT_CLEAN == 0
    assert regulatory_monitor.EXIT_FAILURE == 2
    assert regulatory_monitor.EXIT_FINDINGS == 3
    assert len({
        regulatory_monitor.EXIT_CLEAN,
        regulatory_monitor.EXIT_FAILURE,
        regulatory_monitor.EXIT_FINDINGS,
    }) == 3
    assert regulatory_monitor.EXIT_FINDINGS != 1


def test_federal_register_rule_2210_title_classifies_high_with_null_abstract():
    config = _load_config()
    title = (
        "Self-Regulatory Organizations; Financial Industry Regulatory Authority, Inc.; "
        "Notice of Partial Amendment No. 1 to Proposed Rule Change To Amend FINRA Rule 2210 "
        "(Communications With the Public)"
    )

    classification, _ = regulatory_monitor.classify_regulatory_relevance(title, "", config)

    assert classification in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }


@pytest.mark.parametrize(
    "text",
    (
        "The filing discusses automation of routine administrative processing.",
        "The report describes automation across several operational functions.",
    ),
)
def test_bare_automation_language_does_not_classify_high(text):
    config = _load_config()

    classification, _ = regulatory_monitor.classify_regulatory_relevance(
        "Administrative technology update",
        text,
        config,
    )

    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }


@pytest.mark.parametrize(
    "text",
    (
        "The rule establishes controls for automated trading systems.",
        "The proposal governs automated advice provided to investors.",
    ),
)
def test_fsi_automation_language_remains_high_priority(text):
    config = _load_config()

    classification, _ = regulatory_monitor.classify_regulatory_relevance(
        "Financial services automation requirements",
        text,
        config,
    )

    assert classification in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }


AI_VOCABULARY = (
    "ai agent",
    "agent ai",
    " ai ",
    "copilot",
    "artificial intelligence",
    "machine learning",
    "generative",
    "genai",
    "llm",
    "chatbot",
    "robo",
    "automated advice",
    "algorithm",
    "model risk",
)

# Long-source filler used to prove that classification is decided by context and
# not by position: 4,000 repeats is ~144,000 characters, far beyond the 68,000
# characters at which a genuine late requirement was previously lost, and beyond
# any prior positional bound.
LONG_SOURCE_FILLER = "Routine regulatory background text. " * 4000

FOOTNOTE_BLOCK = (
    " --------------------------------------------------------------------------- "
    "\\53\\ See supra note 45. \\54\\ See also Release No. 34-98765, available at "
    "https://www.sec.gov/rules/sro.htm. "
    "--------------------------------------------------------------------------- "
)


def _assert_free_of_ai_vocabulary(text: str) -> None:
    """Guard: a recordkeeping regression must not be able to pass via AI terms."""
    lowered = f" {text.lower()} "
    for token in AI_VOCABULARY:
        assert token not in lowered, f"sample text leaks AI vocabulary: {token!r}"


def test_reference_only_ai_mention_in_source_text_does_not_become_high():
    """A bibliography/literature-review mention is not an operative requirement.

    This is the exact 2026-17183 authoritative sentence: the literature marker
    is more than 200 characters before the AI occurrence, so a fixed context
    window cannot identify the citation-only clause.
    """
    config = _load_config()
    authoritative_citation_sentence = (
        "Another study also found that blockchain application was the most "
        "discussed topic in ICO whitepapers, followed by information on the "
        "network's development and discussions regarding data management and "
        r"the application of artificial \nintelligence tools.\451\ "
        "This study observed that ICO whitepapers distinctly entailed "
        "substantial discussions on decentralization and network building."
    )
    assert authoritative_citation_sentence.index("artificial") > 200
    detail_text = (
        "Regulation Crypto Assets describes offering and disclosure requirements. "
        + LONG_SOURCE_FILLER
        + authoritative_citation_sentence
    )

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulation Crypto Assets",
        detail_text,
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_NOISE
    assert "artificial intelligence" not in reason.lower()


def test_reference_sentence_stops_at_federal_register_footnote_marker():
    """A later operative sentence must not rescue a citation-only AI mention."""
    config = _load_config()
    detail_text = (
        "Another study also found that blockchain application was the most "
        "discussed topic in ICO whitepapers, followed by information on the "
        "network's development and discussions regarding data management and "
        r"the application of artificial \nintelligence tools.\451\ "
        "Members must retain records for three years."
    )

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulation Crypto Assets",
        detail_text,
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_NOISE
    assert "artificial intelligence" not in reason.lower()


def test_citation_only_copilot_mention_in_source_text_does_not_become_critical():
    """A footnote citation naming a product is a reference, not a requirement."""
    config = _load_config()
    detail_text = (
        "The proposal addresses trading halt procedures. "
        + LONG_SOURCE_FILLER
        + "\\77\\ See also Smith et al., Governance of Microsoft Copilot, "
        "Journal of Financial Regulation (2025), available at "
        "https://example.org/paper.pdf."
    )

    classification, _ = regulatory_monitor.classify_regulatory_relevance(
        "Notice of Filing of a Proposed Rule Change Regarding Trading Halts",
        detail_text,
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_NOISE


@pytest.mark.parametrize(
    "operative_sentence,expected_tier",
    [
        (
            "Each member must supervise the use of artificial intelligence in "
            "communications with customers.",
            regulatory_monitor.CLASSIFICATION_HIGH,
        ),
        (
            "A member firm shall document every copilot deployment used to "
            "generate customer-facing content.",
            regulatory_monitor.CLASSIFICATION_CRITICAL,
        ),
    ],
)
def test_operative_requirement_late_in_long_source_text_is_not_suppressed(
    operative_sentence,
    expected_tier,
):
    """Operative text must classify wherever it appears in the document.

    The prior positional bound truncated classification evidence, so a genuine
    requirement appearing beyond ~68,000 characters silently became NOISE.
    """
    config = _load_config()
    detail_text = (
        "This notice concerns exchange connectivity fees. "
        + LONG_SOURCE_FILLER
        + operative_sentence
    )
    assert len(detail_text) > 68_000

    classification, _ = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        detail_text,
        config,
        exclude_reference_only=True,
    )

    assert classification == expected_tier


def test_operative_requirement_survives_an_adjacent_footnote_block():
    """Citations in the neighbouring footnote block must not mute body text.

    Federal Register source text places footnote blocks immediately after the
    paragraph that cites them, so an unclipped context window would read
    ``See supra note 45`` as the context of operative language.
    """
    config = _load_config()
    detail_text = (
        "This notice concerns exchange connectivity fees. "
        + LONG_SOURCE_FILLER
        + "The Exchange believes members shall retain artificial intelligence "
        "supervisory evidence.\\53\\"
        + FOOTNOTE_BLOCK
    )

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        detail_text,
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "artificial intelligence" in reason.lower()


@pytest.mark.parametrize(
    "detail_text",
    [
        # Reviewer counterexample #1: an unrelated operative sentence
        # ("proposes to amend reporting deadlines") sits next to a separate,
        # citation-only sentence that merely names an AI paper. The obligation
        # belongs to the deadlines sentence, not the AI mention, so the AI
        # occurrence must be read as citation-only and suppressed.
        "The Commission proposes to amend reporting deadlines for covered "
        "filings. A recent working paper on artificial intelligence is "
        "available at https://example.org/ai-study.pdf.",
        # Same defect with the AI citation preceding the unrelated obligation.
        "A recent working paper on artificial intelligence is available at "
        "https://example.org/ai-study.pdf. The Commission proposes to amend "
        "reporting deadlines for covered filings.",
    ],
)
def test_unrelated_obligation_does_not_promote_adjacent_ai_citation(detail_text):
    """Obligation language in a neighbouring sentence must not rescue an
    AI mention that is itself only a citation (reviewer counterexample #1)."""
    config = _load_config()

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        detail_text,
        config,
        exclude_reference_only=True,
    )

    assert classification not in (
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    ), detail_text
    assert "artificial intelligence" not in reason.lower(), detail_text


@pytest.mark.parametrize(
    "detail_text",
    [
        # Reviewer counterexample #2: a genuine obligation to supervise AI,
        # followed by a citation in a separate sentence. The obligation and the
        # AI term share a sentence, so the match must survive.
        "Member firms have an obligation to supervise artificial intelligence "
        "systems. See Smith et al., AI Governance, Journal of Financial "
        "Regulation (2025), available at https://example.org/governance.pdf.",
        # Harder variant: the citation is comma-joined into the SAME clause as
        # the obligation. Only recognising "obligation to" as operative keeps
        # this HIGH; without it the citation marker would wrongly suppress a
        # real requirement.
        "Member firms have an obligation to supervise artificial intelligence "
        "systems, available at https://example.org/governance.pdf.",
        # Non-whitelisted obligation verbs that must also count as operative.
        "Broker-dealers are responsible for supervising artificial "
        "intelligence tools, see supra note 12.",
    ],
)
def test_obligation_language_keeps_ai_requirement_high(detail_text):
    """Operative obligation wording around an AI term must keep the match even
    when a citation shares the sentence (reviewer counterexample #2)."""
    config = _load_config()

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        detail_text,
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH, detail_text
    assert "artificial intelligence" in reason.lower(), detail_text


def test_classification_text_preparation_does_not_truncate():
    """Escaped line breaks are normalized; no source evidence is discarded."""
    body = "a" * 200_000
    source_text = body + r"\nrequirement"

    prepared = regulatory_monitor._prepare_classification_text(source_text)

    # Only the two-character ``\n`` escape collapses to a single space; every
    # other character of the source document survives.
    assert len(prepared) == len(source_text) - 1
    assert prepared.startswith(body)
    assert prepared.endswith(" requirement")


def test_generic_pra_electronic_submission_does_not_become_high():
    """2026-16876 shape: PRA boilerplate is not an operative recordkeeping change.

    The notice mentions a "recordkeeping requirement" in one clause and
    "automated electronic ... collection techniques" hundreds of characters
    later, with no obligation joining them.
    """
    config = _load_config()
    detail_text = (
        "The rules associated with this information collection include registration, "
        "reporting requirements, recordkeeping requirement, and third-party disclosure "
        "requirements. With respect to the collection of information, the Commission "
        "invites comments on: Whether the proposed collection of information is "
        "necessary for the proper performance of the functions of the Commission; The "
        "accuracy of the Commission's estimate of the burden of the proposed collection "
        "of information; Ways to enhance the quality, usefulness, and clarity of the "
        "information to be collected; and Ways to minimize the burden of collection of "
        "information on those who are to respond, including through the use of "
        "appropriate automated electronic, mechanical, or other technological collection "
        "techniques or other forms of information technology, e.g., permitting "
        "electronic submission of responses."
    )

    for exclude_reference_only in (False, True):
        classification, reason = regulatory_monitor.classify_regulatory_relevance(
            "Agency Information Collection Activities: Notice of Intent To Extend "
            "Collection 3038-0059: Part 41, Relating to Security Futures Products",
            detail_text,
            config,
            exclude_reference_only=exclude_reference_only,
        )

        assert classification == regulatory_monitor.CLASSIFICATION_NOISE
        assert "recordkeeping" not in reason.lower()


@pytest.mark.parametrize(
    "detail_text",
    [
        "Recordkeeping must transition to electronic systems by the compliance date.",
        "Records shall be maintained in electronic form for six years.",
        "All order records must be retained electronically by each member.",
        "All order records must be retained digitally by each member.",
        "Records must be kept electronically for the retention period.",
        "Each member must maintain electronic records of every covered order.",
        "Records maintained electronically must be retained for six years.",
        "Records maintained in electronic form shall be retained for six years.",
        "Electronic recordkeeping systems must be implemented by covered members.",
        "The proposed rule would require records to be preserved in electronic form.",
    ],
)
def test_electronic_recordkeeping_obligations_classify_high(detail_text):
    """Recordkeeping-only regressions: HIGH must be earned by the recordkeeping
    rule alone, with no AI/ML vocabulary anywhere in the sample."""
    config = _load_config()
    title = "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change"
    _assert_free_of_ai_vocabulary(f"{title} {detail_text}")

    for exclude_reference_only in (False, True):
        classification, reason = regulatory_monitor.classify_regulatory_relevance(
            title,
            detail_text,
            config,
            exclude_reference_only=exclude_reference_only,
        )

        assert classification == regulatory_monitor.CLASSIFICATION_HIGH, detail_text
        assert reason == "Electronic recordkeeping", detail_text


@pytest.mark.parametrize(
    "detail_text",
    [
        "Each member must retain records of every transaction for three years.",
        "Respondents must submit the required form electronically through the portal.",
        (
            "The proposed rule sets forth conditions for covered entities to deliver "
            "covered information to covered recipients electronically."
        ),
    ],
)
def test_recordkeeping_rule_requires_all_three_elements(detail_text):
    """Records alone, or an electronic medium alone, is not an electronic
    recordkeeping obligation."""
    config = _load_config()

    _, reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        detail_text,
        config,
    )

    assert reason != "Electronic recordkeeping", detail_text


@pytest.mark.parametrize(
    "detail_text",
    [
        # Reviewer counterexample: obligation and electronic language live in
        # different sentences, so they must not be joined into a recordkeeping
        # obligation.
        "Records must be retained for three years. Applications are submitted "
        "electronically through the portal.",
        # Same shape with a semicolon separating the clauses.
        "Firms must retain records; documents may be filed electronically.",
        # Electronic modifies an unrelated noun (communications), records are paper.
        "Firms must supervise electronic communications and keep paper records.",
        # Obligation + record in sentence one, electronic system in sentence two.
        "Members must retain records. Electronic systems are optional for other "
        "filings.",
        # Electronic records are explicitly optional; the operative duty is
        # instead to file paper copies.
        "Electronic records are optional, but firms must file paper copies.",
        # The electronic modifier belongs to communications, not record storage.
        "Members must retain records and use electronic communications.",
    ],
)
def test_recordkeeping_rule_does_not_cross_sentence_boundaries(detail_text):
    """Electronic/digital language in a different sentence than the records
    obligation must never promote to an electronic recordkeeping HIGH."""
    config = _load_config()

    for exclude_reference_only in (False, True):
        classification, reason = regulatory_monitor.classify_regulatory_relevance(
            "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
            detail_text,
            config,
            exclude_reference_only=exclude_reference_only,
        )

        assert reason != "Electronic recordkeeping", detail_text
        assert classification == regulatory_monitor.CLASSIFICATION_NOISE, detail_text


@pytest.mark.parametrize(
    "detail_text",
    [
        # Storage verb precedes the record, electronic adverb trails it.
        "Broker-dealers must preserve records digitally for the retention period.",
        # "books and records" phrasing.
        "Books and records must be maintained in electronic form.",
        "Each firm shall keep books and records in electronic format.",
    ],
)
def test_recordkeeping_rule_recognizes_additional_operative_phrasings(detail_text):
    """Same-sentence electronic recordkeeping obligations regulators actually
    write must still earn HIGH under the tightened rule."""
    config = _load_config()

    for exclude_reference_only in (False, True):
        classification, reason = regulatory_monitor.classify_regulatory_relevance(
            "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
            detail_text,
            config,
            exclude_reference_only=exclude_reference_only,
        )

        assert classification == regulatory_monitor.CLASSIFICATION_HIGH, detail_text
        assert reason == "Electronic recordkeeping", detail_text


def test_meaningful_electronic_recordkeeping_and_ai_remain_high():
    config = _load_config()
    detail_text = (
        "The proposed compute derivatives market uses processing power for "
        "large language models and the artificial intelligence economy. "
        "Covered firms must maintain electronic recordkeeping systems."
    )

    classification, _ = regulatory_monitor.classify_regulatory_relevance(
        "Request for Comment on the Listing of Compute Derivatives Contracts",
        detail_text,
        config,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH


def test_save_state_atomic_does_not_create_or_rewrite_runtime_backup(tmp_path):
    state_path = tmp_path / "monitor-state.json"
    backup_path = tmp_path / "monitor-state.json.backup"
    state_path.write_text('{"version": 0}', encoding="utf-8")
    backup_path.write_text("sentinel", encoding="utf-8")

    monitoring_shared.save_state_atomic(
        {"version": 1, "sources": {}},
        state_path,
    )

    assert backup_path.read_text(encoding="utf-8") == "sentinel"
    assert state_path.read_text(encoding="utf-8") == (
        '{\n  "version": 1,\n  "sources": {}\n}'
    )


class _FederalRegisterResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return self._payload


class _PagedFederalRegisterSession:
    def __init__(self, pages: dict[int, dict]):
        self.pages = pages
        self.calls: list[dict] = []

    def get(self, _url: str, *, params: dict, timeout: int) -> _FederalRegisterResponse:
        self.calls.append(dict(params))
        return _FederalRegisterResponse(self.pages[params["page"]])


def _federal_register_page(
    document_ids: list[str],
    total_pages: int = 2,
    count: int = 116,
    *,
    include_results: bool = True,
) -> dict:
    page = {
        "count": count,
        "total_pages": total_pages,
    }
    if include_results:
        page["results"] = [
            {
                "document_number": document_id,
                "title": f"Federal Register document {document_id}",
                "abstract": "A broker-dealer regulatory notice.",
                "publication_date": "2026-07-27",
                "type": "NOTICE",
                "html_url": f"https://www.federalregister.gov/documents/{document_id}",
                "raw_text_url": (
                    "https://www.federalregister.gov/documents/full_text/text/"
                    f"{document_id}.txt"
                ),
                "agencies": [
                    {
                        "slug": "securities-and-exchange-commission",
                        "name": "Securities and Exchange Commission",
                    }
                ],
            }
            for document_id in document_ids
        ]
    return page


def test_federal_register_fetch_processes_all_pages():
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    second_page_ids = [f"2026-{index:05d}" for index in range(101, 117)]
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids),
            2: _federal_register_page(second_page_ids),
        }
    )

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-07-24",
        config=config,
    )

    assert len(items) == 116
    assert items[-1].document_id == "2026-00116"
    assert [call["page"] for call in session.calls] == [1, 2]


def test_federal_register_production_zero_results_may_omit_results():
    config = _load_config()
    session = _PagedFederalRegisterSession({1: {"count": 0}})

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-07-24",
        config=config,
    )

    assert items == []
    assert [call["page"] for call in session.calls] == [1]


def _federal_register_source_text_page(
    *,
    document_id: str = "2026-16471",
    abstract=None,
) -> dict:
    return {
        "count": 1,
        "total_pages": 1,
        "results": [
            {
                "document_number": document_id,
                "title": "Administrative securities notice",
                "abstract": abstract,
                "publication_date": "2026-08-13",
                "type": "NOTICE",
                "html_url": (
                    "https://www.federalregister.gov/documents/2026/08/13/"
                    f"{document_id}/administrative-securities-notice"
                ),
                "raw_text_url": (
                    "https://www.federalregister.gov/documents/full_text/text/"
                    f"2026/08/13/{document_id}.txt"
                ),
                "agencies": [
                    {
                        "slug": "securities-and-exchange-commission",
                        "name": "Securities and Exchange Commission",
                    }
                ],
            }
        ],
    }


def test_disputed_federal_register_items_have_no_affected_controls(monkeypatch):
    config = _load_config()
    documents = [
        {
            "document_number": "2026-17183",
            "title": "Regulation Crypto Assets",
            "abstract": "Offering and disclosure requirements for crypto assets.",
            "publication_date": "2026-08-21",
            "type": "PRORULE",
            "html_url": "https://www.federalregister.gov/documents/2026-17183",
            "raw_text_url": "https://www.federalregister.gov/documents/full_text/text/2026/01/14/2026-17183.txt",
            "agencies": [{"slug": "securities-and-exchange-commission", "name": "SEC"}],
        },
        {
            "document_number": "2026-16876",
            "title": "Agency Information Collection Activities: Part 41",
            "abstract": "A proposed renewal of an information collection.",
            "publication_date": "2026-08-19",
            "type": "NOTICE",
            "html_url": "https://www.federalregister.gov/documents/2026-16876",
            "raw_text_url": "https://www.federalregister.gov/documents/full_text/text/2026/01/14/2026-16876.txt",
            "agencies": [{"slug": "commodity-futures-trading-commission", "name": "CFTC"}],
        },
    ]
    session = _PagedFederalRegisterSession(
        {1: {"count": 2, "total_pages": 1, "results": documents}}
    )
    detail_text = {
        documents[0]["raw_text_url"]: (
            "Regulation Crypto Assets describes offering requirements for an "
            "investment adviser. "
            + ("Routine regulatory text. " * 3000)
            + r"An unrelated cited study discusses artificial \nintelligence tools."
        ),
        documents[1]["raw_text_url"]: (
            "This information collection includes recordkeeping requirements. "
            + ("Routine PRA burden text. " * 40)
            + "Respondents may use automated electronic techniques, including "
            "electronic submission of responses."
        ),
    }

    def fake_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 200,
            "content": f"<html><body><pre>{detail_text[url]}</pre></body></html>",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-08-18",
        config=config,
    )

    assert {item.document_id: item.classification for item in items} == {
        "2026-17183": regulatory_monitor.CLASSIFICATION_MEDIUM,
        "2026-16876": regulatory_monitor.CLASSIFICATION_NOISE,
    }
    assert {item.document_id: item.affected_controls for item in items} == {
        "2026-17183": [],
        "2026-16876": [],
    }


def test_late_operative_ai_requirement_survives_full_pipeline(monkeypatch):
    """A genuine requirement deep in a long source document must still surface.

    This is the failure the positional bound introduced: the operative sentence
    sits past 68,000 characters, so truncated classification evidence turned a
    real Copilot/AI supervisory requirement into NOISE with no affected
    controls.
    """
    config = _load_config()
    document = {
        "document_number": "2026-99001",
        "title": "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        "abstract": None,
        "publication_date": "2026-08-24",
        "type": "PRORULE",
        "html_url": "https://www.federalregister.gov/documents/2026-99001",
        "raw_text_url": "https://www.federalregister.gov/documents/full_text/text/2026/01/14/2026-99001.txt",
        "agencies": [{"slug": "securities-and-exchange-commission", "name": "SEC"}],
    }
    session = _PagedFederalRegisterSession(
        {1: {"count": 1, "total_pages": 1, "results": [document]}}
    )
    source_text = (
        "This notice concerns exchange connectivity fees. "
        + LONG_SOURCE_FILLER
        + "Each member must supervise the use of artificial intelligence tools in "
        "communications with the public and must retain the resulting records "
        "electronically.\\53\\"
        + FOOTNOTE_BLOCK
    )
    assert len(source_text) > 68_000

    def fake_fetch_page(url, _session, max_retries=3):
        assert url == document["raw_text_url"]
        return {
            "url": url,
            "status_code": 200,
            "content": f"<html><body><pre>{source_text}</pre></body></html>",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-08-18",
        config=config,
    )

    assert len(items) == 1
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "artificial intelligence" in items[0].classification_reason.lower()
    assert items[0].affected_controls


def test_federal_register_medium_abstract_upgrades_on_authoritative_critical_body(
    monkeypatch,
):
    """A MEDIUM abstract must not cap classification: authoritative full text is
    consulted and a late CRITICAL operative requirement in the body wins.

    This is the reviewer defect -- the old rule only fetched authoritative text
    for blank/NOISE abstracts, so a MEDIUM abstract concealed HIGH/CRITICAL body
    language.
    """
    config = _load_config()
    document = {
        "document_number": "2026-90210",
        "title": "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        "abstract": "A broker-dealer regulatory notice concerning routine fees.",
        "publication_date": "2026-08-25",
        "type": "PRORULE",
        "html_url": "https://www.federalregister.gov/documents/2026-90210",
        "raw_text_url": "https://www.federalregister.gov/documents/full_text/text/2026/01/14/2026-90210.txt",
        "agencies": [{"slug": "securities-and-exchange-commission", "name": "SEC"}],
    }
    session = _PagedFederalRegisterSession(
        {1: {"count": 1, "total_pages": 1, "results": [document]}}
    )
    # The abstract alone classifies MEDIUM; a CRITICAL copilot requirement hides
    # well past the point a truncating/only-on-NOISE fetch would have reached.
    abstract_tier, _ = regulatory_monitor.classify_regulatory_relevance(
        document["title"], document["abstract"], config
    )
    assert abstract_tier == regulatory_monitor.CLASSIFICATION_MEDIUM

    source_text = (
        "This notice concerns exchange connectivity fees. "
        + LONG_SOURCE_FILLER
        + "A member firm shall document every copilot deployment and must "
        "supervise the use of artificial intelligence in communications with "
        "the public."
    )
    assert len(source_text) > 68_000

    def fake_fetch_page(url, _session, max_retries=3):
        assert url == document["raw_text_url"]
        return {
            "url": url,
            "status_code": 200,
            "content": f"<html><body><pre>{source_text}</pre></body></html>",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-08-18",
        config=config,
    )

    assert len(items) == 1
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_CRITICAL
    # The authoritative body is adopted as the effective text and drives controls.
    assert "copilot" in items[0].abstract.lower()
    assert items[0].affected_controls


def test_federal_register_medium_abstract_fetch_failure_fails_closed(
    monkeypatch,
):
    """A failed authoritative read must fail closed, not baseline the abstract.

    The reviewer rejected the previous best-effort rule: accepting a MEDIUM/HIGH
    abstract when the authoritative body could not be read recorded a
    fingerprint over summary text, so every later body-only revision was
    silently suppressed. An item whose authoritative body is unavailable is not
    classified and not baselined.
    """
    config = _load_config()
    document = {
        "document_number": "2026-90211",
        "title": "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        "abstract": "A broker-dealer regulatory notice concerning routine fees.",
        "publication_date": "2026-08-25",
        "type": "PRORULE",
        "html_url": "https://www.federalregister.gov/documents/2026-90211",
        "raw_text_url": "https://www.federalregister.gov/documents/full_text/text/2026/01/14/2026-90211.txt",
        "agencies": [{"slug": "securities-and-exchange-commission", "name": "SEC"}],
    }
    # Precondition: the curated abstract alone is MEDIUM, so this is exactly the
    # case the old best-effort rule would have accepted.
    abstract_tier, _ = regulatory_monitor.classify_regulatory_relevance(
        document["title"], document["abstract"], config
    )
    assert abstract_tier == regulatory_monitor.CLASSIFICATION_MEDIUM

    session = _PagedFederalRegisterSession(
        {1: {"count": 1, "total_pages": 1, "results": [document]}}
    )

    def failing_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 503,
            "content": "",
            "final_url": url,
            "was_redirected": False,
            "error": "service unavailable",
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", failing_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    with pytest.raises(
        regulatory_monitor.RequiredSourceTextError,
        match="authoritative text fetch failed",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-08-18",
            config=config,
        )


@pytest.mark.parametrize("abstract", [None, "Administrative procedural update."])
def test_federal_register_insufficient_text_fetches_full_text_and_classifies_medium(
    monkeypatch,
    abstract,
):
    config = _load_config()
    session = _PagedFederalRegisterSession(
        {1: _federal_register_source_text_page(abstract=abstract)}
    )
    raw_text_url = session.pages[1]["results"][0]["raw_text_url"]
    full_text = (
        "<html><body><pre>"
        + ("Unrelated preamble " * 400)
        + "broker-dealer requirements apply.</pre></body></html>"
    )
    fetched_urls = []

    def fake_fetch_page(url, _session, max_retries=3):
        fetched_urls.append(url)
        return {
            "url": url,
            "status_code": 200,
            "content": full_text,
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-08-13",
        config=config,
    )

    assert fetched_urls == [raw_text_url]
    assert "raw_text_url" in session.calls[0]["fields[]"]
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_MEDIUM
    assert "broker-dealer" in items[0].abstract
    assert "<pre>" not in items[0].abstract
    assert len(items[0].abstract) > regulatory_monitor.FALLBACK_TEXT_MAX_CHARS


@pytest.mark.parametrize(
    ("raw_text_url", "detail_fetch_limit", "expected_message"),
    [
        ("", None, "URL was missing"),
        (
            "https://www.federalregister.gov/documents/full_text/text/"
            "2026/08/13/2026-16471.txt",
            0,
            "fetch limit reached",
        ),
    ],
)
def test_federal_register_required_source_text_preconditions_fail_closed(
    monkeypatch,
    raw_text_url,
    detail_fetch_limit,
    expected_message,
):
    config = _load_config()
    page = _federal_register_source_text_page()
    page["results"][0]["raw_text_url"] = raw_text_url
    session = _PagedFederalRegisterSession({1: page})
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    with pytest.raises(
        regulatory_monitor.RequiredSourceTextError,
        match=expected_message,
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-08-13",
            config=config,
            detail_fetch_limit=detail_fetch_limit,
        )


def test_federal_register_required_source_text_fetch_failure_fails_closed(monkeypatch):
    config = _load_config()
    session = _PagedFederalRegisterSession(
        {1: _federal_register_source_text_page()}
    )

    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        lambda url, _session, max_retries=3: {
            "url": url,
            "status_code": 503,
            "content": "",
            "final_url": url,
            "was_redirected": False,
            "error": "service unavailable",
        },
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    with pytest.raises(
        regulatory_monitor.RequiredSourceTextError,
        match="authoritative text fetch failed",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-08-13",
            config=config,
        )


def test_federal_register_uncounted_empty_first_page_fails_closed():
    config = _load_config()
    session = _PagedFederalRegisterSession(
        {1: {"total_pages": 1, "results": []}}
    )

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="missing 'count'",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_uncounted_short_first_page_fails_closed():
    config = _load_config()
    short_page = _federal_register_page(
        ["2026-00001"],
        total_pages=2,
        count=1,
    )
    short_page.pop("count")
    session = _PagedFederalRegisterSession({1: short_page})

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="missing 'count'",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_later_page_items_are_written_to_state():
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    second_page_ids = [f"2026-{index:05d}" for index in range(101, 117)]
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids),
            2: _federal_register_page(second_page_ids),
        }
    )

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-07-24",
        config=config,
    )
    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
        items,
        state,
    )

    entries = regulatory_monitor.get_source_state(
        state,
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
    )["entries"]
    assert len(entries) == 116
    assert "2026-00116" in entries


def test_federal_register_empty_intermediate_page_fails_closed():
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids, total_pages=3, count=201),
            2: _federal_register_page([], total_pages=3, count=201),
        }
    )

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="empty before pagination completed",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_missing_results_page_fails_closed():
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    missing_results_page = _federal_register_page(
        [],
        total_pages=2,
        count=116,
        include_results=False,
    )
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids),
            2: missing_results_page,
        }
    )

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="missing 'results'",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_identical_overlapping_pages_are_deduplicated():
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    second_page_ids = [f"2026-{index:05d}" for index in range(100, 117)]
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids),
            2: _federal_register_page(second_page_ids),
        }
    )

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-07-24",
        config=config,
    )

    assert len(items) == 116
    assert len({item.document_id for item in items}) == 116
    assert [item.document_id for item in items[-17:]] == [
        f"2026-{index:05d}" for index in range(100, 117)
    ]


@pytest.mark.parametrize("field", ["title", "abstract"])
def test_federal_register_conflicting_duplicate_payload_fails_closed(field):
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    second_page_ids = [f"2026-{index:05d}" for index in range(100, 117)]
    second_page = _federal_register_page(second_page_ids)
    second_page["results"][0][field] = f"Changed substantive {field}"
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids),
            2: second_page,
        }
    )

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="conflicting substantive payloads",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_identity_falls_back_to_html_url():
    url = "https://www.federalregister.gov/documents/missing-number"

    assert regulatory_monitor._federal_register_document_identity(
        {"html_url": url},
        page=1,
    ) == url


def test_federal_register_incomplete_unique_count_fails_closed():
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    second_page_ids = [f"2026-{index:05d}" for index in range(100, 116)]
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids),
            2: _federal_register_page(second_page_ids),
        }
    )

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="incomplete unique result set",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_count_change_fails_closed():
    config = _load_config()
    first_page_ids = [f"2026-{index:05d}" for index in range(1, 101)]
    session = _PagedFederalRegisterSession(
        {
            1: _federal_register_page(first_page_ids, count=116),
            2: _federal_register_page(
                [f"2026-{index:05d}" for index in range(101, 117)],
                count=117,
            ),
        }
    )

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="count changed",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_inconsistent_total_pages_fails_closed():
    config = _load_config()
    page = _federal_register_page(
        [f"2026-{index:05d}" for index in range(1, 101)],
        total_pages=3,
        count=116,
    )
    session = _PagedFederalRegisterSession({1: page})

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="inconsistent with count",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_page_metadata_mismatch_fails_closed():
    config = _load_config()
    page = _federal_register_page(
        [f"2026-{index:05d}" for index in range(1, 101)],
        total_pages=1,
        count=100,
    )
    page["page"] = 2
    session = _PagedFederalRegisterSession({1: page})

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="page metadata",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_invalid_metadata_fails_closed():
    config = _load_config()
    page = _federal_register_page(
        [f"2026-{index:05d}" for index in range(1, 2)],
        total_pages=1,
        count=1.5,
    )
    session = _PagedFederalRegisterSession({1: page})

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="field 'count' was invalid",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def test_federal_register_missing_identity_fails_closed():
    config = _load_config()
    session = _PagedFederalRegisterSession(
        {
            1: {
                "count": 1,
                "total_pages": 1,
                "results": [{}],
            }
        }
    )

    with pytest.raises(
        regulatory_monitor.FederalRegisterPaginationError,
        match="no stable identity",
    ):
        regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-07-24",
            config=config,
        )


def _assert_finra_listing_failure_does_not_advance_state(
    monkeypatch,
    caplog,
    *,
    fetch_result: dict,
    expected_message: str,
    parser_failure: Exception | None = None,
) -> None:
    config = _load_config()
    initial_state = {
        "version": 1,
        "sources": {
            regulatory_monitor.SOURCE_KEY_FINRA: {
                "last_run": "2026-08-01T10:00:00+00:00",
                "entries": {"FINRA 26-01": "existing-hash"},
            }
        },
    }
    loaded_state = deepcopy(initial_state)
    save_calls = []

    class _Session:
        def __init__(self):
            self.headers = {}

    monkeypatch.setattr(
        regulatory_monitor,
        "load_monitoring_config",
        lambda _path: config,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "load_state",
        lambda _path: loaded_state,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "save_state_atomic",
        lambda *args: save_calls.append(args),
    )
    monkeypatch.setattr(regulatory_monitor.requests, "Session", _Session)
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        lambda _url, _session, max_retries=3: fetch_result,
    )
    if parser_failure is not None:
        def fail_parse(*_args, **_kwargs):
            raise parser_failure

        monkeypatch.setattr(regulatory_monitor, "BeautifulSoup", fail_parse)
    monkeypatch.setattr(
        regulatory_monitor.sys,
        "argv",
        ["regulatory_monitor.py", "--source", "finra"],
    )

    exit_code = regulatory_monitor.main()

    assert exit_code == regulatory_monitor.EXIT_FAILURE
    assert expected_message in caplog.text
    assert loaded_state == initial_state
    assert save_calls == []


def test_finra_listing_http_failure_fails_closed_without_state_advance(
    monkeypatch,
    caplog,
):
    _assert_finra_listing_failure_does_not_advance_state(
        monkeypatch,
        caplog,
        fetch_result={
            "url": regulatory_monitor.FINRA_NOTICES_URL,
            "status_code": 503,
            "content": "",
            "final_url": regulatory_monitor.FINRA_NOTICES_URL,
            "was_redirected": False,
            "error": "service unavailable",
        },
        expected_message="status 503",
    )


def test_finra_listing_rate_limit_failure_fails_closed_without_state_advance(
    monkeypatch,
    caplog,
):
    _assert_finra_listing_failure_does_not_advance_state(
        monkeypatch,
        caplog,
        fetch_result={
            "url": regulatory_monitor.FINRA_NOTICES_URL,
            "status_code": 429,
            "content": "",
            "final_url": regulatory_monitor.FINRA_NOTICES_URL,
            "was_redirected": False,
            "error": "HTTP 429 rate limit persisted after 3 attempts (waited 35s)",
        },
        expected_message="status 429",
    )


def test_finra_listing_parse_failure_fails_closed_without_state_advance(
    monkeypatch,
    caplog,
):
    _assert_finra_listing_failure_does_not_advance_state(
        monkeypatch,
        caplog,
        fetch_result={
            "url": regulatory_monitor.FINRA_NOTICES_URL,
            "status_code": 200,
            "content": "<html><body>unparseable listing</body></html>",
            "final_url": regulatory_monitor.FINRA_NOTICES_URL,
            "was_redirected": False,
            "error": None,
        },
        expected_message="parsing failed",
        parser_failure=ValueError("parser rejected listing"),
    )


def test_finra_listing_empty_result_fails_closed_without_state_advance(
    monkeypatch,
    caplog,
):
    _assert_finra_listing_failure_does_not_advance_state(
        monkeypatch,
        caplog,
        fetch_result={
            "url": regulatory_monitor.FINRA_NOTICES_URL,
            "status_code": 200,
            "content": (
                "<html><head>"
                '<link rel="canonical" href="https://www.finra.org/rules-guidance/notices" />'
                "</head><body><main><table class='notices-table'><tbody>"
                "</tbody></table><p>No notices rendered.</p>"
                "</main></body></html>"
            ),
            "final_url": regulatory_monitor.FINRA_NOTICES_URL,
            "was_redirected": False,
            "error": None,
        },
        expected_message="no regulatory notice links",
    )


@pytest.mark.parametrize(
    "fetch_error",
    [
        regulatory_monitor.FederalRegisterPaginationError(
            "Federal Register pagination failed closed"
        ),
        regulatory_monitor.RequiredSourceTextError(
            "Federal Register authoritative text fetch failed closed"
        ),
    ],
    ids=["pagination", "required-source-text"],
)
def test_federal_register_failure_maps_to_failure_exit_without_state_advance(
    monkeypatch,
    fetch_error,
):
    config = _load_config()
    initial_state = {
        "version": 1,
        "sources": {
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER: {
                "last_checked": "2026-08-01",
                "entries": {"2026-00001": "existing-hash"},
            }
        },
    }
    loaded_state = deepcopy(initial_state)
    save_calls = []

    class _Session:
        def __init__(self):
            self.headers = {}

    def fail_fetch(*_args, **_kwargs):
        raise fetch_error

    monkeypatch.setattr(
        regulatory_monitor,
        "load_monitoring_config",
        lambda _path: config,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "load_state",
        lambda _path: loaded_state,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "save_state_atomic",
        lambda *args: save_calls.append(args),
    )
    monkeypatch.setattr(regulatory_monitor.requests, "Session", _Session)
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_federal_register_documents",
        fail_fetch,
    )
    monkeypatch.setattr(
        regulatory_monitor.sys,
        "argv",
        ["regulatory_monitor.py", "--source", "federal-register"],
    )

    exit_code = regulatory_monitor.main()

    assert exit_code == regulatory_monitor.EXIT_FAILURE
    assert loaded_state == initial_state
    assert save_calls == []


def test_finra_notice_body_fallback_promotes_genai_notice_to_high(monkeypatch):
    config = _load_config()
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/26-14", "Regulatory Notice 26-14: Request for Comment")]
    )
    detail_html = _finra_notice_page(
        "GenAI communication tools may be included in a reasonably designed "
        "supervisory system when firms vet, test, and continuously monitor for "
        "hallucination and data-protection risk."
    )

    def fake_fetch_page(url, session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            return {
                "url": url,
                "status_code": 200,
                "content": listing_html,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(detail_html, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
        limit=1,
    )

    assert len(items) == 1
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "genai" in items[0].abstract.lower()


def test_finra_long_notice_late_mandatory_ai_requirement_elevates(monkeypatch):
    """A mandatory AI requirement past the presentation-excerpt bound in a long
    (>8k) notice must still elevate the notice to HIGH.

    Classification runs against the complete normalized body; only the stored
    abstract is bounded. The reviewer defect was that the fallback extractor
    truncated to FALLBACK_TEXT_MAX_CHARS before classification, so a late
    requirement silently vanished.
    """
    config = _load_config()
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/26-14", "Regulatory Notice 26-14: Request for Comment")]
    )
    # Neutral filler with no AI/recordkeeping vocabulary, long enough to push
    # the operative requirement well beyond the legacy 4000-char truncation.
    filler = (
        "The committee reviewed meeting logistics and calendar planning for "
        "upcoming member outreach sessions during the comment period. "
    ) * 90
    late_requirement = (
        "Member firms must supervise the use of artificial intelligence in all "
        "customer communications."
    )
    detail_html = _finra_notice_page(f"{filler}{late_requirement}")

    # Preconditions: the extracted body is long and the requirement lands past
    # the excerpt bound, so a truncating extractor would hide it.
    extracted = regulatory_monitor._extract_finra_notice_fallback_text(detail_html)
    assert len(extracted) > 8000
    assert extracted.lower().index("artificial intelligence") > (
        regulatory_monitor.FALLBACK_TEXT_MAX_CHARS
    )

    def fake_fetch_page(url, session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            return {
                "url": url,
                "status_code": 200,
                "content": listing_html,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(detail_html, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
        limit=1,
    )

    assert len(items) == 1
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH
    # The stored abstract stays a bounded excerpt that does not itself carry the
    # late requirement...
    assert len(items[0].abstract) <= regulatory_monitor.FALLBACK_TEXT_MAX_CHARS
    assert "artificial intelligence" not in items[0].abstract.lower()
    # ...proving classification could only have reached HIGH by reading the
    # complete body: the bounded excerpt alone does not classify HIGH.
    excerpt_tier, _ = regulatory_monitor.classify_regulatory_relevance(
        items[0].title, items[0].abstract, config
    )
    assert excerpt_tier != regulatory_monitor.CLASSIFICATION_HIGH


def test_finra_listing_enumerates_and_deduplicates_table_and_list_notice_links(
    monkeypatch,
):
    """Live-shaped table/list markup must yield every eligible notice once."""
    config = _load_config()
    listing_html = """
    <html><body>
      <nav><a href="/rules-guidance/notices">All notices</a></nav>
      <table class="views-table">
        <tbody>
          <tr class="views-row">
            <td><a href="/rules-guidance/notices/26-01">
              Regulatory Notice 26-01
            </a></td>
            <td><a href="/rules-guidance/notices/26-01?view=full">
              View notice
            </a></td>
          </tr>
          <tr class="views-row">
            <td><a href="https://www.finra.org/rules-guidance/notices/26-02/">
              Regulatory Notice 26-02
            </a></td>
          </tr>
        </tbody>
      </table>
      <ul class="notices-list">
        <li><a href="26-03">Regulatory Notice 26-03</a></li>
        <li><a href="/rules-guidance/notices/information-notice-20260803">
          Information Notice 8/3/26
        </a></li>
        <li><a href="/rules-guidance/notices/information-notice-20260803?dup=1">
          Information Notice 8/3/26 (duplicate)
        </a></li>
      </ul>
    </body></html>
    """
    detail_calls = []

    def fake_fetch_page(url, _session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            content = listing_html
        else:
            detail_calls.append(url)
            content = (
                "<html><body><article class='node--type-notice'>"
                "<div class='field--name-body'>Authoritative notice body.</div>"
                "</article></body></html>"
            )
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
    )

    expected_urls = {
        "https://www.finra.org/rules-guidance/notices/26-01",
        "https://www.finra.org/rules-guidance/notices/26-02",
        "https://www.finra.org/rules-guidance/notices/26-03",
        "https://www.finra.org/rules-guidance/notices/information-notice-20260803",
    }
    assert {item.url for item in items} == expected_urls
    assert len(items) == len(expected_urls)
    assert set(detail_calls) == expected_urls
    assert len(detail_calls) == len(expected_urls)


def test_finra_information_notice_body_evidence_is_classified(monkeypatch):
    """Information-notice URLs are eligible and use their authoritative body."""
    config = _load_config()
    listing_html = """
    <html><body><ul class="notices-list"><li>
      <a href="/rules-guidance/notices/information-notice-20260803">
        Information Notice 8/3/26
      </a>
    </li></ul></body></html>
    """
    detail_html = """
    <html><body><article class="node--type-notice">
      <div class="field--name-body">
        Members must supervise the use of artificial intelligence systems.
      </div>
    </article></body></html>
    """

    def fake_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(
                listing_html
                if url == regulatory_monitor.FINRA_NOTICES_URL
                else detail_html,
                url,
            ),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
    )

    assert len(items) == 1
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "artificial intelligence" in items[0].content_text.lower()
    assert "artificial intelligence" in items[0].abstract.lower()


def test_finra_fetches_more_than_twenty_generic_titles_and_reads_late_ai_body(
    monkeypatch,
):
    """The production path has no 20-item cap or title-based body shortcut."""
    config = _load_config()
    notice_ids = [f"26-{index:02d}" for index in range(1, 23)]
    listing_rows = "".join(
        f"<tr><td><a href='/rules-guidance/notices/{notice_id}'>"
        f"Listing entry {notice_id}</a></td></tr>"
        for notice_id in notice_ids
    )
    listing_html = (
        "<html><body><table class='views-table'><tbody>"
        + listing_rows
        + "</tbody></table></body></html>"
    )
    filler = (
        "The committee reviewed meeting logistics and calendar planning. "
    ) * 100
    late_requirement = (
        "Members must supervise the use of artificial intelligence in customer "
        "communications."
    )
    detail_bodies = {
        notice_id: (
            filler + late_requirement
            if notice_id == "26-22"
            else f"Routine authoritative body for {notice_id}."
        )
        for notice_id in notice_ids
    }
    detail_calls = []

    def fake_fetch_page(url, _session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            content = listing_html
        else:
            detail_calls.append(url)
            notice_id = url.rsplit("/", 1)[-1]
            content = (
                "<html><body><article class='node--type-notice'>"
                f"<div class='field--name-body'>{detail_bodies[notice_id]}</div>"
                "</article></body></html>"
            )
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
    )

    assert len(items) == 22
    assert len(detail_calls) == 22
    late_item = next(item for item in items if item.document_id == "FINRA 26-22")
    assert late_item.classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert len(late_item.abstract) <= regulatory_monitor.FALLBACK_TEXT_MAX_CHARS
    assert "artificial intelligence" not in late_item.abstract.lower()
    assert "artificial intelligence" in late_item.content_text.lower()


def test_finra_notice_body_parser_excludes_login_chrome_and_keeps_long_body():
    """The first generic body field can be login chrome, not notice content."""
    actual_body = (
        "Actual FINRA notice body. "
        + "The notice explains member procedures. " * 250
        + "Members must supervise artificial intelligence systems."
    )
    html = f"""
    <html><body>
      <div class="field field--name-body">
        Please log in to view this page.
      </div>
      <main>
        <article class="node node--type-notice">
          <h1>Regulatory Notice</h1>
          <div class="field field--name-body">{actual_body}</div>
        </article>
      </main>
    </body></html>
    """

    extracted = regulatory_monitor._extract_finra_notice_fallback_text(html)

    assert len(extracted) > 8000
    assert "Please log in" not in extracted
    assert extracted.startswith("Actual FINRA notice body.")
    assert "artificial intelligence systems" in extracted


def test_finra_detail_fetch_failure_does_not_advance_state(monkeypatch, caplog):
    """A failed detail read must return failure and leave the baseline intact."""
    config = _load_config()
    initial_state = {
        "version": 1,
        "sources": {
            regulatory_monitor.SOURCE_KEY_FINRA: {
                "last_run": "2026-08-01T10:00:00+00:00",
                "entries": {"FINRA 26-01": "existing-hash"},
            }
        },
    }
    loaded_state = deepcopy(initial_state)
    save_calls = []

    class _Session:
        def __init__(self):
            self.headers = {}

    listing_html = """
    <html><body><table><tbody><tr>
      <td><a href="/rules-guidance/notices/26-15">Listing entry</a></td>
    </tr></tbody></table></body></html>
    """

    def fake_fetch_page(url, _session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            return {
                "url": url,
                "status_code": 200,
                "content": listing_html,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        return {
            "url": url,
            "status_code": 503,
            "content": "",
            "final_url": url,
            "was_redirected": False,
            "error": "service unavailable",
        }

    monkeypatch.setattr(regulatory_monitor, "load_monitoring_config", lambda _path: config)
    monkeypatch.setattr(regulatory_monitor, "load_state", lambda _path: loaded_state)
    monkeypatch.setattr(
        regulatory_monitor,
        "save_state_atomic",
        lambda *args: save_calls.append(args),
    )
    monkeypatch.setattr(regulatory_monitor.requests, "Session", _Session)
    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        regulatory_monitor.sys,
        "argv",
        ["regulatory_monitor.py", "--source", "finra"],
    )

    exit_code = regulatory_monitor.main()

    assert exit_code == regulatory_monitor.EXIT_FAILURE
    assert "FINRA authoritative notice body fetch failed" in caplog.text
    assert loaded_state == initial_state
    assert save_calls == []


def test_finra_change_hash_uses_late_authoritative_body_not_excerpt():
    """Identical 4k excerpts with different late bodies are a change."""
    prefix = "Routine authoritative notice text. " * 180
    first_body = prefix + "Late section version one."
    updated_body = prefix + "Late section version two."
    assert first_body[:4000] == updated_body[:4000]

    def make_item(body: str) -> "regulatory_monitor.RegulatoryItem":
        return regulatory_monitor.RegulatoryItem(
            source="FINRA",
            agency="FINRA",
            title="Regulatory Notice 26-22",
            url="https://www.finra.org/rules-guidance/notices/26-22",
            publication_date="2026-08-22",
            doc_type="NOTICE",
            abstract=body[:regulatory_monitor.FALLBACK_TEXT_MAX_CHARS],
            content_text=body,
            document_id="FINRA 26-22",
            classification=regulatory_monitor.CLASSIFICATION_MEDIUM,
            classification_reason="Test",
            affected_controls=[],
        )

    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [make_item(first_body)],
        state,
    )
    source_state = regulatory_monitor.get_source_state(
        state,
        regulatory_monitor.SOURCE_KEY_FINRA,
    )

    changed = make_item(updated_body)
    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [changed],
        source_state,
    ) == [changed]


def test_finra_publication_date_uses_authoritative_listing_metadata(monkeypatch):
    config = _load_config()
    listing_html = """
    <html><body><div class="notices-view"><table><tbody><tr>
      <td><time datetime="2026-08-03T12:00:00Z">August 3, 2026</time></td>
      <td>
        <a href="/rules-guidance/notices/information-notice-20260803">
          Information Notice 8/3/26
        </a>
      </td>
    </tr></tbody></table></div></body></html>
    """
    detail_html = _finra_notice_page("Information notice body.")

    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        lambda url, _session, max_retries=3: (
            {
                "url": url,
                "status_code": 200,
                "content": listing_html,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
            if url == regulatory_monitor.FINRA_NOTICES_URL
            else {
                "url": url,
                "status_code": 200,
                "content": _with_finra_canonical(detail_html, url),
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        ),
    )

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
        limit=1,
    )

    assert len(items) == 1
    assert items[0].publication_date == "2026-08-03"
    assert items[0].publication_date_is_synthetic is False


def test_finra_publication_date_falls_back_to_authoritative_url():
    link = regulatory_monitor.BeautifulSoup(
        '<a href="/rules-guidance/notices/information-notice-20260803">'
        "Information Notice 8/3/26</a>",
        "html.parser",
    ).find("a")

    publication_date, is_synthetic = (
        regulatory_monitor._derive_finra_publication_date(
            link,
            "https://www.finra.org/rules-guidance/notices/"
            "information-notice-20260803",
        )
    )

    assert publication_date == "2026-08-03"
    assert is_synthetic is False


def _finra_information_notice(
    *,
    title: str = "Information Notice 8/3/26",
    abstract: str = "",
    publication_date: str,
    publication_date_is_synthetic: bool,
) -> "regulatory_monitor.RegulatoryItem":
    url = (
        "https://www.finra.org/rules-guidance/notices/"
        "information-notice-20260803"
    )
    return regulatory_monitor.RegulatoryItem(
        source="FINRA",
        agency="FINRA",
        title=title,
        url=url,
        publication_date=publication_date,
        doc_type="NOTICE",
        abstract=abstract,
        document_id=url,
        publication_date_is_synthetic=publication_date_is_synthetic,
        classification=regulatory_monitor.CLASSIFICATION_NOISE,
        affected_controls=[],
    )


def test_same_finra_notice_does_not_reappear_across_synthetic_daily_runs():
    august_9 = _finra_information_notice(
        publication_date="2026-08-09",
        publication_date_is_synthetic=True,
    )
    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [august_9],
        state,
    )
    source_state = regulatory_monitor.get_source_state(
        state,
        regulatory_monitor.SOURCE_KEY_FINRA,
    )

    august_10 = _finra_information_notice(
        publication_date="2026-08-10",
        publication_date_is_synthetic=True,
    )

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [august_10],
        source_state,
    ) == []


def test_changed_finra_notice_still_registers_with_synthetic_date():
    original = _finra_information_notice(
        publication_date="2026-08-09",
        publication_date_is_synthetic=True,
    )
    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [original],
        state,
    )
    source_state = regulatory_monitor.get_source_state(
        state,
        regulatory_monitor.SOURCE_KEY_FINRA,
    )

    changed = _finra_information_notice(
        title="Information Notice 8/3/26 — Updated Requirements",
        publication_date="2026-08-10",
        publication_date_is_synthetic=True,
    )

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [changed],
        source_state,
    ) == [changed]


def test_finra_legacy_daily_hash_migrates_without_false_finding():
    current = _finra_information_notice(
        publication_date="2026-08-03",
        publication_date_is_synthetic=False,
    )
    legacy_hash = regulatory_monitor.compute_hash(
        "Information Notice 8/3/26||2026-08-09"
    )
    source_state = {
        "entries": {current.document_id: legacy_hash},
        "last_run": "2026-08-09T10:20:45.080820+00:00",
    }

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [current],
        source_state,
    ) == []


def test_finra_notice_body_fetch_failure_fails_closed(monkeypatch):
    config = _load_config()
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/26-14", "Regulatory Notice 26-14: Request for Comment")]
    )

    def fake_fetch_page(url, session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            return {
                "url": url,
                "status_code": 200,
                "content": listing_html,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        return {
            "url": url,
            "status_code": 0,
            "content": "",
            "final_url": url,
            "was_redirected": False,
            "error": "offline",
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    with pytest.raises(
        regulatory_monitor.RequiredSourceTextError,
        match="FINRA authoritative notice body fetch failed",
    ):
        regulatory_monitor.fetch_finra_notices(
            session=object(),
            config=config,
            limit=1,
        )


def test_finra_notice_body_fetch_uses_cache(monkeypatch):
    config = _load_config()
    listing_html = _finra_listing_html(
        [
            ("/rules-guidance/notices/26-14", "Regulatory Notice 26-14: Request for Comment"),
            (
                "/rules-guidance/notices/26-14",
                "Regulatory Notice 26-14: Request for Comment (duplicate)",
            ),
        ]
    )
    detail_html = _finra_notice_page("GenAI monitoring language for notice 26-14.")
    detail_calls = {"count": 0}

    def fake_fetch_page(url, session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            return {
                "url": url,
                "status_code": 200,
                "content": listing_html,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        detail_calls["count"] += 1
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(detail_html, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
        limit=2,
    )

    assert len(items) == 1
    assert detail_calls["count"] == 1


def test_generate_regulatory_report_has_single_h1_heading(monkeypatch):
    item = regulatory_monitor.RegulatoryItem(
        source="Federal Register",
        agency="SEC",
        title="Sample Title",
        url="https://example.test/item",
        publication_date="2026-07-11",
        doc_type="NOTICE",
        abstract="Sample abstract",
        document_id="2026-00001",
        classification=regulatory_monitor.CLASSIFICATION_HIGH,
        classification_reason="Test",
        affected_controls=["3.5"],
    )
    captured = {}

    def fake_write_report(report_content, report_dir, filename):
        captured["content"] = report_content
        captured["report_dir"] = report_dir
        captured["filename"] = filename
        return report_dir / filename

    monkeypatch.setattr(regulatory_monitor, "write_report", fake_write_report)

    regulatory_monitor.generate_regulatory_report(
        all_new_items=[item],
        report_path=Path("regulatory-changes-test.md"),
    )

    content = captured["content"]
    assert content.count("# Regulatory Monitor Report") == 1
    assert content.startswith("# Regulatory Monitor Report\n")


def _fed_item(abstract: str, *, document_id: str = "2026-00042") -> "regulatory_monitor.RegulatoryItem":
    return regulatory_monitor.RegulatoryItem(
        source="Federal Register",
        agency="SEC",
        title="Self-Regulatory Organizations; Notice of Filing",
        url="https://www.federalregister.gov/documents/2026/07/11/2026-00042/notice",
        publication_date="2026-07-11",
        doc_type="NOTICE",
        abstract=abstract,
        document_id=document_id,
        classification=regulatory_monitor.CLASSIFICATION_NOISE,
        classification_reason="Test",
        affected_controls=[],
    )


def test_report_counts_and_order_match_classified_records(monkeypatch):
    fed_second = _fed_item("second", document_id="2026-00002")
    fed_second.title = "Title 2026-00002"
    fed_first = _fed_item("first", document_id="2026-00001")
    fed_first.title = "Title 2026-00001"
    items = [
        fed_second,
        regulatory_monitor.RegulatoryItem(
            source="FINRA",
            agency="FINRA",
            title="Information Notice",
            url="https://www.finra.org/rules-guidance/notices/26-14",
            publication_date="2026-07-11",
            doc_type="NOTICE",
            document_id="FINRA 26-14",
            classification=regulatory_monitor.CLASSIFICATION_NOISE,
            affected_controls=[],
        ),
        fed_first,
    ]
    captured = {}

    def fake_write_report(report_content, report_dir, filename):
        captured["content"] = report_content
        return report_dir / filename

    monkeypatch.setattr(regulatory_monitor, "write_report", fake_write_report)

    regulatory_monitor.generate_regulatory_report(
        items,
        report_path=Path("regulatory-changes-test.md"),
        source_counts={
            "Federal Register": {"fetched": 3, "new": 2},
            "FINRA": {"fetched": 1, "new": 1},
        },
    )

    content = captured["content"]
    assert "**Fetched Items:** 4" in content
    assert "**New Items:** 3" in content
    assert "**Classified Items:** 3" in content
    assert "**Federal Register Fetched:** 3" in content
    assert "**Federal Register New:** 2" in content
    assert content.index("2026-00002") < content.index("2026-00001")
    assert content.index("2026-00001") < content.index("Information Notice")


def test_report_count_mismatch_fails_before_write():
    item = _fed_item("new item")

    with pytest.raises(ValueError, match="new count"):
        regulatory_monitor.generate_regulatory_report(
            [item],
            report_path=Path("regulatory-changes-test.md"),
            source_counts={
                "Federal Register": {"fetched": 1, "new": 0},
            },
        )


def test_state_entry_order_is_independent_of_fetch_order():
    first = _fed_item("first", document_id="2026-00001")
    second = _fed_item("second", document_id="2026-00002")
    state_a: dict = {}
    state_b: dict = {}

    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
        [first, second],
        state_a,
    )
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
        [second, first],
        state_b,
    )

    entries_a = regulatory_monitor.get_source_state(
        state_a,
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
    )["entries"]
    entries_b = regulatory_monitor.get_source_state(
        state_b,
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
    )["entries"]
    assert list(entries_a) == list(entries_b)
    assert entries_a == entries_b


def test_change_hash_ignores_incidental_abstract_whitespace_churn():
    """A same-document item whose abstract differs only in whitespace/newline
    reflow must NOT be re-emitted -- this is the dedup/normalization gap that
    re-reported 17 Federal Register NOISE items."""
    original = _fed_item("The Commission is publishing this notice to solicit comments.")
    state: dict = {}
    regulatory_monitor.update_source_state("regulatory-federal", [original], state)
    source_state = regulatory_monitor.get_source_state(state, "regulatory-federal")

    churned = _fed_item(
        "  The Commission is publishing this   notice\nto solicit comments.  "
    )
    new_items = regulatory_monitor.check_for_new_items(
        "regulatory-federal", [churned], source_state
    )

    assert new_items == [], (
        "cosmetic whitespace churn should not re-emit an unchanged item"
    )


def test_change_hash_still_detects_substantive_abstract_change():
    """A genuine wording change to the abstract must still be reported so real
    regulatory updates are not silently dropped by the normalization."""
    original = _fed_item("The Commission is publishing this notice to solicit comments.")
    state: dict = {}
    regulatory_monitor.update_source_state("regulatory-federal", [original], state)
    source_state = regulatory_monitor.get_source_state(state, "regulatory-federal")

    updated = _fed_item(
        "The Commission is publishing this notice to APPROVE the proposed rule change."
    )
    new_items = regulatory_monitor.check_for_new_items(
        "regulatory-federal", [updated], source_state
    )

    assert len(new_items) == 1
    assert new_items[0].document_id == "2026-00042"


def test_content_fingerprint_normalizes_whitespace_only():
    """The fingerprint collapses whitespace but preserves substantive text and
    the schema-2 field ordering
    (title|report_text|authoritative_body|publication_date)."""
    item = _fed_item("alpha\n\nbeta   gamma")
    fp = regulatory_monitor._content_fingerprint(item)
    assert "alpha beta gamma" in fp
    assert fp.split("|") == [
        "Self-Regulatory Organizations; Notice of Filing",
        "alpha beta gamma",
        "alpha beta gamma",
        "2026-07-11",
    ]


def test_state_entries_declare_the_current_hash_schema():
    """Stored digests carry an explicit schema tag.

    Without it a comparison cannot tell a fingerprint-layout change from a
    content change, which is how a changed late suffix was previously mistaken
    for a harmless legacy migration.
    """
    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
        [_fed_item("An abstract")],
        state,
    )
    entries = regulatory_monitor.get_source_state(
        state,
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
    )["entries"]

    stored = entries["2026-00042"]
    assert stored.startswith(regulatory_monitor.CONTENT_HASH_SCHEMA_PREFIX)
    assert regulatory_monitor._stored_hash_schema_version(stored) == (
        regulatory_monitor.CONTENT_HASH_SCHEMA_VERSION
    )
    # A pre-versioning entry is recognised as legacy, never as current.
    assert regulatory_monitor._stored_hash_schema_version(
        "sha256:" + "0" * 64
    ) == regulatory_monitor.LEGACY_CONTENT_HASH_SCHEMA_VERSION


def test_limited_cli_run_does_not_mutate_entries_or_watermark(monkeypatch):
    config = _load_config()
    initial_state = {
        "version": 1,
        "sources": {
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER: {
                "last_checked": "2026-08-01",
                "entries": {},
            }
        },
    }
    loaded_state = {
        "version": initial_state["version"],
        "sources": {
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER: {
                "last_checked": "2026-08-01",
                "entries": {},
            }
        },
    }
    save_calls = []

    class _Session:
        def __init__(self):
            self.headers = {}

    monkeypatch.setattr(
        regulatory_monitor,
        "load_monitoring_config",
        lambda _path: config,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "load_state",
        lambda _path: loaded_state,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "save_state_atomic",
        lambda *args: save_calls.append(args),
    )
    monkeypatch.setattr(
        regulatory_monitor.requests,
        "Session",
        _Session,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_federal_register_documents",
        lambda _session, _since_date, _config, limit=None: [
            _fed_item("A newly fetched item")
        ],
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "generate_regulatory_report",
        lambda *_args, **_kwargs: None,
    )
    monkeypatch.setattr(
        regulatory_monitor.sys,
        "argv",
        ["regulatory_monitor.py", "--source", "federal-register", "--limit", "1"],
    )

    exit_code = regulatory_monitor.main()

    assert exit_code == regulatory_monitor.EXIT_FINDINGS
    assert loaded_state == initial_state
    assert save_calls == []


def test_main_returns_clean_exit_when_no_findings(monkeypatch):
    config = _load_config()
    loaded_state = {
        "version": 1,
        "sources": {
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER: {
                "last_checked": "2026-08-01",
                "entries": {},
            }
        },
    }
    save_calls = []
    report_calls = []

    class _Session:
        def __init__(self):
            self.headers = {}

    monkeypatch.setattr(
        regulatory_monitor,
        "load_monitoring_config",
        lambda _path: config,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "load_state",
        lambda _path: loaded_state,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "save_state_atomic",
        lambda *args: save_calls.append(args),
    )
    monkeypatch.setattr(regulatory_monitor.requests, "Session", _Session)
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_federal_register_documents",
        lambda _session, _since_date, _config, limit=None: [],
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "generate_regulatory_report",
        lambda *_args, **_kwargs: report_calls.append((_args, _kwargs)),
    )
    monkeypatch.setattr(
        regulatory_monitor.sys,
        "argv",
        ["regulatory_monitor.py", "--source", "federal-register"],
    )

    exit_code = regulatory_monitor.main()

    assert exit_code == regulatory_monitor.EXIT_CLEAN
    assert len(save_calls) == 1
    assert report_calls == []


def test_dry_run_does_not_mutate_state(monkeypatch):
    config = _load_config()
    initial_state = {
        "version": 1,
        "sources": {
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER: {
                "last_checked": "2026-08-01",
                "entries": {},
            }
        },
    }
    loaded_state = {
        "version": initial_state["version"],
        "sources": {
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER: {
                "last_checked": "2026-08-01",
                "entries": {},
            }
        },
    }
    save_calls = []

    monkeypatch.setattr(
        regulatory_monitor,
        "load_monitoring_config",
        lambda _path: config,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "load_state",
        lambda _path: loaded_state,
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "save_state_atomic",
        lambda *args: save_calls.append(args),
    )
    monkeypatch.setattr(
        regulatory_monitor.sys,
        "argv",
        ["regulatory_monitor.py", "--source", "federal-register", "--dry-run"],
    )

    exit_code = regulatory_monitor.main()

    assert exit_code == regulatory_monitor.EXIT_CLEAN
    assert loaded_state == initial_state
    assert save_calls == []


# --- Securities-law electronic delivery ("Regulation E-Delivery") classification ---
# Grounding: Federal Register document 2026-14679, SEC proposed rule
# "Electronic Delivery of Information Under the Federal Securities Laws"
# (published 2026-07-21). It is a general FSI regulatory change to how covered
# information is delivered to broker-dealer/adviser/investment-company recipients,
# so it must surface at MEDIUM (awareness-only). It has no AI/automation nexus,
# so it must NOT be elevated to HIGH/CRITICAL.
ELECTRONIC_DELIVERY_TITLE = (
    "Electronic Delivery of Information Under the Federal Securities Laws"
)
ELECTRONIC_DELIVERY_ABSTRACT = (
    "The Securities and Exchange Commission is proposing Regulation E-Delivery. "
    "The proposed rule sets forth conditions for covered entities to deliver "
    "covered information to covered recipients electronically, and establishes "
    "conditions under which delivery requirements under the Federal securities "
    "laws would be considered satisfied by electronic delivery."
)


def test_electronic_delivery_title_classifies_medium_with_null_abstract():
    """The 2026-14679 title alone (null abstract) must classify MEDIUM. Prior to
    the added pattern this returned NOISE, which baselined the document in
    monitor state and suppressed it from future review."""
    config = _load_config()

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        ELECTRONIC_DELIVERY_TITLE, "", config
    )

    assert classification == regulatory_monitor.CLASSIFICATION_MEDIUM
    assert "delivery" in reason.lower()


def test_electronic_delivery_abstract_classifies_medium():
    """A securities-law e-delivery item classifies MEDIUM via the abstract too
    (e.g., "electronic delivery" / "Regulation E-Delivery" wording)."""
    config = _load_config()

    classification, _ = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing",
        ELECTRONIC_DELIVERY_ABSTRACT,
        config,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_MEDIUM


def test_ordinary_delivery_phrases_remain_noise():
    """The pattern requires "electronic" adjacent to "delivery" (or the
    "e-delivery" shorthand); ordinary delivery/settlement/logistics language
    must stay NOISE so the fix does not broadly match unrelated items."""
    config = _load_config()
    noise_titles = [
        "Physical delivery of commodities under futures contracts",
        "Delivery versus payment settlement of securities",
        "Order regarding delivery points and delivery months for natural gas",
        "Same-day parcel delivery service logistics",
        "Electronic funds transfer for member delivery of collateral",
    ]
    for title in noise_titles:
        classification, _ = regulatory_monitor.classify_regulatory_relevance(
            title, "", config
        )
        assert classification == regulatory_monitor.CLASSIFICATION_NOISE, title


def test_electronic_delivery_does_not_override_high_or_critical():
    """HIGH/CRITICAL precedence is unchanged: an AI/automation nexus alongside
    electronic delivery still classifies at the higher tier, never MEDIUM."""
    config = _load_config()

    critical, _ = regulatory_monitor.classify_regulatory_relevance(
        "Electronic Delivery of Information by an AI Agent Under the Securities Laws",
        "",
        config,
    )
    assert critical == regulatory_monitor.CLASSIFICATION_CRITICAL

    high, _ = regulatory_monitor.classify_regulatory_relevance(
        "Electronic Delivery of Disclosures Generated Using Artificial Intelligence",
        "",
        config,
    )
    assert high == regulatory_monitor.CLASSIFICATION_HIGH


# ---------------------------------------------------------------------------
# Reviewer-mandated adversarial regressions for the five integrity defects.
#
# Each block is written to fail against the pre-fix behaviour, not merely to
# describe the fix. Where a defect had a "looks fine" failure mode (a silent
# overwrite, an accepted error page, a suppressed finding), the test asserts
# the observable consequence, not the internal helper.
# ---------------------------------------------------------------------------


def _fr_document(
    document_id: str,
    *,
    title: str = "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
    abstract: str = "A broker-dealer regulatory notice.",
    publication_date: str = "2026-08-21",
    doc_type: str = "PRORULE",
    agency_slug: str = "securities-and-exchange-commission",
    agency_name: str = "SEC",
) -> dict:
    return {
        "document_number": document_id,
        "title": title,
        "abstract": abstract,
        "publication_date": publication_date,
        "type": doc_type,
        "html_url": f"https://www.federalregister.gov/documents/{document_id}",
        "raw_text_url": (
            "https://www.federalregister.gov/documents/full_text/text/"
            f"{document_id}.txt"
        ),
        "agencies": [{"slug": agency_slug, "name": agency_name}],
    }


def _fr_body_session(document: dict, body: str, monkeypatch):
    """Wire a single-document listing plus a 200 authoritative body fetch."""
    session = _PagedFederalRegisterSession(
        {1: {"count": 1, "total_pages": 1, "results": [document]}}
    )
    requested: list[str] = []

    def fake_fetch_page(url, _session, max_retries=3):
        requested.append(url)
        return {
            "url": url,
            "status_code": 200,
            "content": f"<html><body><pre>{body}</pre></body></html>",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)
    return session, requested


# --- Defect 1: Federal Register authoritative body integrity ---------------


def test_federal_register_critical_abstract_still_fetches_authoritative_body(
    monkeypatch,
):
    """A CRITICAL abstract must not short-circuit the authoritative read.

    Pre-fix, a CRITICAL abstract skipped the detail fetch entirely, so the
    baseline hash covered a curated summary and every later body revision was
    invisible. The classification outcome is not the point -- the retained and
    hashed evidence is.
    """
    config = _load_config()
    document = _fr_document(
        "2026-91001",
        abstract=(
            "The Commission proposes requirements for Microsoft 365 Copilot "
            "deployments used by registered broker-dealers."
        ),
    )
    abstract_tier, _ = regulatory_monitor.classify_regulatory_relevance(
        document["title"], document["abstract"], config
    )
    assert abstract_tier == regulatory_monitor.CLASSIFICATION_CRITICAL

    body = (
        "Authoritative body text for 2026-91001. Each member firm shall "
        "supervise every copilot deployment used to prepare customer "
        "communications and shall retain the resulting records."
    )
    session, requested = _fr_body_session(document, body, monkeypatch)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session, since_date="2026-08-18", config=config
    )

    assert len(items) == 1
    assert document["raw_text_url"] in requested, "authoritative body was not fetched"
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_CRITICAL
    assert "Authoritative body text for 2026-91001" in items[0].content_text
    # The complete body -- not just the abstract -- is what gets hashed.
    assert "Authoritative body text for 2026-91001" in (
        regulatory_monitor._content_fingerprint(items[0])
    )


def test_federal_register_unchanged_abstract_with_changed_late_body_is_a_finding(
    monkeypatch,
):
    """Same abstract, revised body late in the document -> a finding.

    This is the concrete harm of not hashing the authoritative body: a silent
    substantive revision behind an untouched curated abstract.
    """
    config = _load_config()
    document = _fr_document("2026-91002")
    filler = "Routine regulatory background text. " * 400
    first_body = f"Authoritative body. {filler}The compliance date is March 1, 2027."
    second_body = f"Authoritative body. {filler}The compliance date is June 1, 2027."

    session, _ = _fr_body_session(document, first_body, monkeypatch)
    first = regulatory_monitor.fetch_federal_register_documents(
        session=session, since_date="2026-08-18", config=config
    )
    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, first, state
    )
    source_state = regulatory_monitor.get_source_state(
        state, regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER
    )

    session, _ = _fr_body_session(document, second_body, monkeypatch)
    second = regulatory_monitor.fetch_federal_register_documents(
        session=session, since_date="2026-08-18", config=config
    )

    assert first[0].abstract != "" and second[0].abstract == first[0].abstract, (
        "the curated abstract must be identical for this test to be meaningful"
    )
    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, second, source_state
    ) == second

    # ...and a re-run of the same body is stable, so this is not just churn.
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, second, state
    )
    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
        second,
        regulatory_monitor.get_source_state(
            state, regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER
        ),
    ) == []


def test_federal_register_body_is_hashed_even_when_abstract_sets_severity(
    monkeypatch,
):
    """Severity merge is classification-only; retention is unconditional.

    The abstract wins the tier here (the body is neutral), which is exactly the
    branch where the old code discarded the body. The body must still be
    retained and hashed.
    """
    config = _load_config()
    document = _fr_document(
        "2026-91003",
        abstract=(
            "The Commission proposes supervisory requirements for artificial "
            "intelligence tools that each member firm must implement."
        ),
    )
    neutral_body = (
        "Table of contents. Paperwork Reduction Act statement. "
        "Regulatory flexibility certification. Statutory authority citation."
    )
    session, _ = _fr_body_session(document, neutral_body, monkeypatch)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session, since_date="2026-08-18", config=config
    )

    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert items[0].abstract == document["abstract"], "abstract evidence was lost"
    assert "Paperwork Reduction Act statement" in items[0].content_text
    fingerprint = regulatory_monitor._content_fingerprint(items[0])
    assert "artificial intelligence tools" in fingerprint
    assert "Paperwork Reduction Act statement" in fingerprint


def test_federal_register_fetch_failure_is_not_baselined(monkeypatch):
    """A failed authoritative read leaves no state entry behind."""
    config = _load_config()
    document = _fr_document("2026-91004")
    session = _PagedFederalRegisterSession(
        {1: {"count": 1, "total_pages": 1, "results": [document]}}
    )

    def failing_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 403,
            "content": "",
            "final_url": url,
            "was_redirected": False,
            "error": "forbidden",
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", failing_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-18", config=config
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )

    assert state == {}, "a failed authoritative read must not advance state"


# --- Defect 2: FINRA non-notice / error-page rejection ---------------------


FINRA_NON_NOTICE_FIXTURES = {
    "access_denied": (
        "<html><body><main><article class='node node--type-page'>"
        "<div class='field field--name-body'><h1>Access Denied</h1>"
        "<p>You do not have permission to access this page.</p>"
        "</div></article></main></body></html>"
    ),
    "request_blocked": (
        "<html><body><main><article class='node node--type-notice'>"
        "<div class='field field--name-body'><h1>Request Blocked</h1>"
        "<p>Your request has been blocked. Reference #18.2b3c4d5e.</p>"
        "</div></article></main></body></html>"
    ),
    "captcha_challenge": (
        "<html><body><main><article class='node node--type-notice'>"
        "<div class='field field--name-body'><h1>Verify you are human</h1>"
        "<p>Please complete the security check to continue.</p>"
        "</div></article></main></body></html>"
    ),
    "login_wall": (
        "<html><body><main><article class='node node--type-notice'>"
        "<div class='field field--name-body'>Please log in to view this page. "
        "Sign in to continue to the requested notice.</div>"
        "</article></main></body></html>"
    ),
    "not_found": (
        "<html><body><main><article class='node node--type-page'>"
        "<div class='field field--name-body'><h1>Page not found</h1>"
        "<p>The page you requested could not be found.</p>"
        "</div></article></main></body></html>"
    ),
    # The reviewer's core objection: a populated <main> is not a notice body.
    "bare_main_chrome": (
        "<html><body><main>Rules &amp; Guidance. Notices. Rulebook. "
        "Contact FINRA. This page could not be displayed.</main></body></html>"
    ),
    "bare_main_plausible_prose": (
        "<html><body><main>Member firms must supervise the use of artificial "
        "intelligence in all customer communications.</main></body></html>"
    ),
}


@pytest.mark.parametrize("fixture_name", sorted(FINRA_NON_NOTICE_FIXTURES))
def test_finra_non_notice_pages_yield_no_body_text(fixture_name):
    """Every 200-status non-notice shape extracts nothing.

    ``bare_main_plausible_prose`` is the adversarial case: the text reads like a
    real requirement, so only the *structural* gate can reject it. Accepting it
    would let page chrome or a templated block be baselined as notice content.
    """
    assert regulatory_monitor._extract_finra_notice_fallback_text(
        FINRA_NON_NOTICE_FIXTURES[fixture_name]
    ) == ""


@pytest.mark.parametrize("fixture_name", sorted(FINRA_NON_NOTICE_FIXTURES))
def test_finra_two_hundred_status_error_pages_fail_closed(fixture_name, monkeypatch):
    """A 200 error/challenge page raises rather than advancing state.

    Status code alone proves nothing here: all of these are served with HTTP
    200, which is precisely why the old ``<main>``-is-enough rule baselined
    them.
    """
    config = _load_config()
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/26-14", "Regulatory Notice 26-14: Request for Comment")]
    )
    detail_html = FINRA_NON_NOTICE_FIXTURES[fixture_name]

    def fake_fetch_page(url, session, max_retries=3):
        content = (
            listing_html if url == regulatory_monitor.FINRA_NOTICES_URL else detail_html
        )
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_finra_notices(
            session=object(), config=config, limit=1
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FINRA, items, state
        )

    assert state == {}, "an error page must not be baselined as notice content"


def test_finra_live_shaped_valid_notice_still_succeeds(monkeypatch):
    """The gate must not be a blanket rejection: a real notice still lands."""
    config = _load_config()
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/26-14", "Regulatory Notice 26-14: Request for Comment")]
    )
    body = (
        "Summary: Member firms must supervise the use of artificial intelligence "
        "in all customer communications and must retain supervisory evidence."
    )
    detail_html = _finra_notice_page(body)

    def fake_fetch_page(url, session, max_retries=3):
        content = (
            listing_html if url == regulatory_monitor.FINRA_NOTICES_URL else detail_html
        )
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(), config=config, limit=1
    )

    assert len(items) == 1
    assert "supervise the use of artificial intelligence" in items[0].content_text
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH


def test_finra_substantial_notice_survives_incidental_challenge_wording():
    """The rejection signature must not eat genuine notices.

    A real notice can legitimately say "security check" or "log in to the FINRA
    Gateway". The safety valve keeps a long, structurally valid notice that
    happens to contain such wording.
    """
    body = (
        "Suggested Routing: Compliance, Legal, Senior Management. Member firms "
        "must complete a security check before onboarding and may log in to the "
        "FINRA Gateway to file. "
        + ("This notice explains member supervisory procedures in detail. " * 60)
    )
    extracted = regulatory_monitor._extract_finra_notice_fallback_text(
        _finra_notice_page(body)
    )
    assert "Suggested Routing" in extracted
    assert len(extracted) > regulatory_monitor.FINRA_NOTICE_SUBSTANTIAL_CHARS


# --- Defect 3: citation-only AI filtering ---------------------------------


REFERENCE_ONLY_SENTENCES = {
    "obligation_then_citation": (
        "The Commission proposes to amend quarterly report deadlines for covered "
        "filings, and a recent working paper on artificial intelligence is "
        "available at https://example.org/ai-study.pdf."
    ),
    "citation_then_obligation": (
        "A recent working paper on artificial intelligence is available at "
        "https://example.org/ai-study.pdf, and the Commission proposes to amend "
        "quarterly report deadlines for covered filings."
    ),
    "obligation_then_supra_note": (
        "Each registrant must file the annual report within 60 days, see supra "
        "note 14 discussing artificial intelligence in capital markets."
    ),
    "obligation_then_journal_survey": (
        "Each registrant must file the annual report within 60 days, and Smith "
        "et al. survey artificial intelligence in the Journal of Financial "
        "Regulation."
    ),
    "obligation_then_academic_study": (
        "Each registrant must file the annual report within 60 days, and a "
        "recent academic study of artificial intelligence in capital markets is "
        "available at https://example.org/ai.pdf."
    ),
}


@pytest.mark.parametrize("case", sorted(REFERENCE_ONLY_SENTENCES))
def test_unrelated_obligation_beside_ai_citation_stays_non_high(case):
    """An obligation elsewhere in the sentence must not activate the citation.

    Pre-fix the filter asked "does this sentence contain obligation language?"
    -- so any duty anywhere in the sentence rescued a purely bibliographic AI
    mention. The duty must bind the AI-bearing clause itself.
    """
    config = _load_config()
    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        REFERENCE_ONLY_SENTENCES[case],
        config,
        exclude_reference_only=True,
    )
    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, (classification, reason)
    assert "artificial intelligence" not in reason.lower()


def test_operative_ai_duty_survives_intervening_clause():
    """Fail-open guard: a real duty separated by an appositive stays HIGH.

    This is the cost side of narrowing the scope -- if the clause split were
    naive, this genuine requirement would be filtered out as a citation.
    """
    config = _load_config()
    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10",
        "Members must, in accordance with Rule 3110, supervise artificial "
        "intelligence tools used for customer communications.",
        config,
        exclude_reference_only=True,
    )
    assert classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "artificial intelligence" in reason.lower()


def _finra_pipeline(body: str, monkeypatch, *, link_text: str):
    config = _load_config()
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/26-14", link_text)]
    )
    detail_html = _finra_notice_page(body)

    def fake_fetch_page(url, session, max_retries=3):
        content = (
            listing_html if url == regulatory_monitor.FINRA_NOTICES_URL else detail_html
        )
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)
    return regulatory_monitor.fetch_finra_notices(
        session=object(), config=config, limit=1
    )


def test_finra_body_with_only_an_ai_citation_stays_non_high(monkeypatch):
    """Reference-only filtering was previously Federal Register-only.

    A FINRA notice whose sole AI mention is a bibliographic citation must not
    be promoted, and must map no controls.
    """
    body = (
        "This notice reminds members of quarterly filing schedules and fee "
        "obligations. See Smith et al., Governance of Artificial Intelligence in "
        "Broker-Dealers, Journal of Financial Regulation (2025), available at "
        "https://example.org/ai-paper.pdf."
    )
    items = _finra_pipeline(
        body, monkeypatch, link_text="Regulatory Notice 26-14: Filing Schedules"
    )

    assert len(items) == 1
    assert items[0].classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }
    assert "artificial intelligence" not in items[0].classification_reason.lower()
    assert items[0].affected_controls == [], (
        "control mapping must apply the same reference-only filter as "
        "classification, or a citation silently maps governance controls"
    )


def test_finra_genuine_operative_ai_requirement_remains_high(monkeypatch):
    """The FINRA filter must not suppress real requirements."""
    body = (
        "Member firms must supervise the use of artificial intelligence in all "
        "customer communications and must retain supervisory evidence for the "
        "period required by the applicable books and records rules."
    )
    items = _finra_pipeline(
        body, monkeypatch, link_text="Regulatory Notice 26-14: Request for Comment"
    )

    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "artificial intelligence" in items[0].classification_reason.lower()
    assert items[0].affected_controls, "a genuine AI requirement must map controls"


def test_federal_register_genuine_operative_ai_requirement_remains_high(monkeypatch):
    """The 2026-17163 contract shape: a real AI reference stays HIGH."""
    config = _load_config()
    document = _fr_document(
        "2026-17163",
        title="Request for Comment on the Listing of Compute Derivatives Contracts",
        abstract="A request for comment on compute derivatives contracts.",
        agency_slug="commodity-futures-trading-commission",
        agency_name="CFTC",
    )
    body = (
        "The Commission requests comment on contracts referencing compute "
        "capacity. A designated contract market must describe how artificial "
        "intelligence workloads determine the deliverable supply, and shall "
        "maintain records supporting that determination."
    )
    session, _ = _fr_body_session(document, body, monkeypatch)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session, since_date="2026-08-18", config=config
    )

    assert items[0].classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "artificial intelligence" in items[0].classification_reason.lower()
    assert items[0].affected_controls


def test_federal_register_critical_copilot_requirement_remains_critical(monkeypatch):
    config = _load_config()
    document = _fr_document("2026-91005")
    body = (
        "A member firm shall document every Microsoft 365 Copilot deployment "
        "used to generate customer-facing content, and must preserve those "
        "records."
    )
    session, _ = _fr_body_session(document, body, monkeypatch)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session, since_date="2026-08-18", config=config
    )

    assert items[0].classification == regulatory_monitor.CLASSIFICATION_CRITICAL


# --- Defect 4: electronic-or-paper alternatives ---------------------------


ELECTRONIC_ALTERNATIVE_SENTENCES = [
    "Records must be retained either electronically or in paper form.",
    "Records must be retained either in paper form or electronically.",
    "Records must be maintained electronically or in paper form.",
    "Firms may maintain records in paper form or electronically.",
    "Each member shall preserve the records in electronic format or in hard copy.",
    "Books and records may be kept in hard copy or in electronic format.",
]

ELECTRONIC_MANDATE_SENTENCES = [
    "Records must be maintained electronically rather than in paper form.",
    "Records must be maintained electronically and not in paper form.",
    "All order records must be retained electronically by each member.",
    "Books and records must be preserved in electronic format.",
    "Records shall be maintained in electronic form for six years.",
    "Recordkeeping must transition to electronic systems by the compliance date.",
]


@pytest.mark.parametrize("sentence", ELECTRONIC_ALTERNATIVE_SENTENCES)
def test_electronic_or_paper_alternative_is_not_an_electronic_mandate(sentence):
    """Both orderings of the alternative must be rejected.

    A one-directional scan ("is paper mentioned after electronic?") passes the
    canonical phrasing and fails the reversed one, which is the same defect
    wearing a different hat.
    """
    assert regulatory_monitor._has_electronic_recordkeeping_obligation(sentence) is False
    config = _load_config()
    classification, _ = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        sentence,
        config,
    )
    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, sentence


@pytest.mark.parametrize("sentence", ELECTRONIC_MANDATE_SENTENCES)
def test_mandatory_electronic_only_recordkeeping_is_preserved(sentence):
    """Rejecting alternatives must not cost genuine electronic-only mandates.

    "rather than"/"and not" mention paper precisely to exclude it -- the
    replacement reading, not the alternative reading.
    """
    assert regulatory_monitor._has_electronic_recordkeeping_obligation(sentence) is True
    config = _load_config()
    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change",
        sentence,
        config,
    )
    assert classification == regulatory_monitor.CLASSIFICATION_HIGH, sentence
    assert reason == "Electronic recordkeeping"


def test_electronic_alternative_in_one_clause_does_not_suppress_a_separate_mandate():
    """Scoping is per-clause, so a nearby alternative must not disarm a real
    mandate elsewhere in the same document."""
    text = (
        "Correspondence may be delivered electronically or in paper form. "
        "All order audit trail records must be retained electronically."
    )
    assert regulatory_monitor._has_electronic_recordkeeping_obligation(text) is True


# --- Defect 5: legacy FINRA excerpt-hash migration ------------------------


def _finra_item_with_body(body: str, *, title: str = "Regulatory Notice 26-14"):
    url = "https://www.finra.org/rules-guidance/notices/26-14"
    excerpt = body[: regulatory_monitor.FALLBACK_TEXT_MAX_CHARS]
    return regulatory_monitor.RegulatoryItem(
        source="FINRA",
        agency="FINRA",
        title=title,
        url=url,
        publication_date="2026-08-03",
        doc_type="NOTICE",
        abstract=excerpt,
        content_text=body,
        document_id=url,
        publication_date_is_synthetic=False,
        classification=regulatory_monitor.CLASSIFICATION_NOISE,
        affected_controls=[],
    )


def _long_finra_body(suffix: str) -> str:
    """A body longer than the legacy excerpt bound, differing only at the end."""
    prefix = "Regulatory Notice 26-14 supervisory guidance. " * 150
    assert len(prefix) > regulatory_monitor.FALLBACK_TEXT_MAX_CHARS
    return f"{prefix}{suffix}"


def test_legacy_excerpt_hash_with_changed_late_suffix_reports_a_finding():
    """The core defect: a truncated legacy digest cannot prove the suffix.

    The stored schema-1 hash covered only the first
    ``FALLBACK_TEXT_MAX_CHARS`` characters. A revision after that bound
    reproduces the identical legacy digest, so treating a legacy match as
    "harmless migration" silently overwrote a real change. Unprovable means
    report once, not suppress.
    """
    original = _finra_item_with_body(_long_finra_body("The compliance date is March 1, 2027."))
    revised = _finra_item_with_body(_long_finra_body("The compliance date is June 1, 2027."))
    assert original.abstract == revised.abstract, (
        "the legacy excerpt must be identical, or this test proves nothing"
    )

    legacy_hash = regulatory_monitor.compute_hash(
        regulatory_monitor._legacy_content_fingerprint(
            original.title, original.abstract, original.publication_date
        )
    )
    assert regulatory_monitor._stored_hash_schema_version(legacy_hash) == (
        regulatory_monitor.LEGACY_CONTENT_HASH_SCHEMA_VERSION
    )
    source_state = {
        "entries": {revised.document_id: legacy_hash},
        "last_run": "2026-08-09T10:20:45.080820+00:00",
    }

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA, [revised], source_state
    ) == [revised]


def test_legacy_migration_finding_does_not_repeat_under_the_new_schema():
    """One-time only: after the run rewrites the entry, the noise stops."""
    revised = _finra_item_with_body(_long_finra_body("The compliance date is June 1, 2027."))
    legacy_hash = regulatory_monitor.compute_hash(
        regulatory_monitor._legacy_content_fingerprint(
            revised.title, revised.abstract, revised.publication_date
        )
    )
    state = {
        "sources": {
            regulatory_monitor.SOURCE_KEY_FINRA: {
                "entries": {revised.document_id: legacy_hash},
                "last_run": "2026-08-09T10:20:45.080820+00:00",
            }
        }
    }

    first_run = regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA,
        [revised],
        regulatory_monitor.get_source_state(
            state, regulatory_monitor.SOURCE_KEY_FINRA
        ),
    )
    assert first_run == [revised]

    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FINRA, [revised], state
    )
    stored = regulatory_monitor.get_source_state(
        state, regulatory_monitor.SOURCE_KEY_FINRA
    )["entries"][revised.document_id]
    assert stored.startswith(regulatory_monitor.CONTENT_HASH_SCHEMA_PREFIX)

    for _ in range(3):
        assert regulatory_monitor.check_for_new_items(
            regulatory_monitor.SOURCE_KEY_FINRA,
            [revised],
            regulatory_monitor.get_source_state(
                state, regulatory_monitor.SOURCE_KEY_FINRA
            ),
        ) == []


def test_legacy_excerpt_covering_the_whole_body_migrates_silently():
    """Compatibility side: a provable legacy digest must not flood the report.

    When the notice is shorter than the excerpt bound, the legacy hash covered
    the complete body, so the schema change is demonstrably content-neutral.
    """
    body = "Short FINRA notice body that fits well inside the excerpt bound."
    item = _finra_item_with_body(body)
    assert item.abstract == item.content_text

    legacy_hash = regulatory_monitor.compute_hash(
        regulatory_monitor._legacy_content_fingerprint(
            item.title, item.abstract, item.publication_date
        )
    )
    source_state = {
        "entries": {item.document_id: legacy_hash},
        "last_run": "2026-08-09T10:20:45.080820+00:00",
    }

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA, [item], source_state
    ) == []


def test_legacy_schema_match_is_rejected_when_content_actually_changed():
    """A provable-shape legacy hash still loses to a genuine content change."""
    stored_item = _finra_item_with_body("Short FINRA notice body.")
    legacy_hash = regulatory_monitor.compute_hash(
        regulatory_monitor._legacy_content_fingerprint(
            stored_item.title, stored_item.abstract, stored_item.publication_date
        )
    )
    changed = _finra_item_with_body("Short FINRA notice body, as amended.")
    source_state = {
        "entries": {changed.document_id: legacy_hash},
        "last_run": "2026-08-09T10:20:45.080820+00:00",
    }

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FINRA, [changed], source_state
    ) == [changed]


def test_federal_register_legacy_abstract_only_entry_surfaces_one_time_finding():
    """A schema-1 digest that never saw the body cannot prove it is unchanged.

    Schema 1 hashed whichever text was adopted for the report. Where that was
    the curated abstract, the authoritative body was outside the digest
    entirely, so silence would be an assertion the data cannot support. The
    honest outcome is one re-baseline finding, then stability.
    """
    item = regulatory_monitor.RegulatoryItem(
        source="Federal Register",
        agency="SEC",
        title="Self-Regulatory Organizations; Notice of Filing",
        url="https://www.federalregister.gov/documents/2026-00042/notice",
        publication_date="2026-07-11",
        doc_type="NOTICE",
        abstract="A broker-dealer regulatory notice.",
        content_text="The complete authoritative body text of the filing.",
        document_id="2026-00042",
        classification=regulatory_monitor.CLASSIFICATION_NOISE,
        classification_reason="Test",
        affected_controls=[],
    )
    legacy_hash = regulatory_monitor.compute_hash(
        regulatory_monitor._legacy_content_fingerprint(
            item.title, item.abstract, item.publication_date
        )
    )
    state = {
        "sources": {
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER: {
                "entries": {item.document_id: legacy_hash},
                "last_run": "2026-08-26T10:24:01+00:00",
            }
        }
    }

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
        [item],
        regulatory_monitor.get_source_state(
            state, regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER
        ),
    ) == [item]

    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, [item], state
    )
    for _ in range(3):
        assert regulatory_monitor.check_for_new_items(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER,
            [item],
            regulatory_monitor.get_source_state(
                state, regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER
            ),
        ) == []


def test_federal_register_legacy_entry_that_already_covered_the_body_is_silent():
    """Migration noise is bounded, not blanket.

    Where schema 1 already hashed the authoritative body (the body supplied the
    classification evidence, so it was the text stored), the schema change is
    demonstrably content-neutral and must migrate silently. Without this the
    fix would trade a silent-overwrite defect for a full re-baseline flood.
    """
    body = "The complete authoritative body text of the filing."
    item = regulatory_monitor.RegulatoryItem(
        source="Federal Register",
        agency="SEC",
        title="Self-Regulatory Organizations; Notice of Filing",
        url="https://www.federalregister.gov/documents/2026-00043/notice",
        publication_date="2026-07-11",
        doc_type="NOTICE",
        abstract=body,
        content_text=body,
        document_id="2026-00043",
        classification=regulatory_monitor.CLASSIFICATION_NOISE,
        classification_reason="Test",
        affected_controls=[],
    )
    legacy_hash = regulatory_monitor.compute_hash(
        regulatory_monitor._legacy_content_fingerprint(
            item.title, body, item.publication_date
        )
    )
    source_state = {
        "entries": {item.document_id: legacy_hash},
        "last_run": "2026-08-26T10:24:01+00:00",
    }

    assert regulatory_monitor.check_for_new_items(
        regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, [item], source_state
    ) == []


def test_committed_state_is_legacy_schema_and_is_read_as_such():
    """The real committed baseline is schema 1 and must be recognised as such.

    Guards against a migration that silently assumes the shipped state was
    written under the current layout.
    """
    import json

    state_path = REPO_ROOT / "data" / "monitor-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    entries = state["sources"][regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER]["entries"]
    assert entries, "committed Federal Register baseline is empty"
    assert all(
        regulatory_monitor._stored_hash_schema_version(value)
        == regulatory_monitor.LEGACY_CONTENT_HASH_SCHEMA_VERSION
        for value in entries.values()
    )


# --- Acceptance contracts pinned to the committed Aug-26 artefacts ---------


def test_committed_august_26_report_preserves_acceptance_contracts():
    """The corrected report is the contract; regressions must not silently
    invalidate it."""
    report = (
        REPO_ROOT / "reports" / "monitoring" / "regulatory-changes-2026-08-26.md"
    ).read_text(encoding="utf-8")

    high_section = report.split("## HIGH Priority Items", 1)[1].split("\n## ", 1)[0]
    medium_section = report.split("## MEDIUM Priority Items", 1)[1].split("\n## ", 1)[0]
    noise_section = report.split("## NOISE", 1)[1]

    assert "| HIGH Changes | 1 |" in report
    # 2026-17163: the single genuine HIGH, kept.
    assert "2026-17163" in high_section
    assert "**Classification:** HIGH — References artificial intelligence" in high_section
    # 2026-17183: demoted, and with no fabricated AI rationale anywhere.
    assert "2026-17183" not in high_section
    assert "2026-17183" in medium_section
    # 2026-16876: PRA boilerplate stays NOISE.
    assert "2026-16876" not in high_section
    assert "2026-16876" not in medium_section
    assert "2026-16876" in noise_section


@pytest.mark.parametrize(
    "fixture_name", ["access_denied", "request_blocked", "captcha_challenge", "bare_main_plausible_prose"]
)
def test_finra_error_detail_page_maps_to_failure_exit_without_state_advance(
    fixture_name, monkeypatch, caplog
):
    """End-to-end: a 200 error page exits 2 and leaves state untouched.

    The unit-level rejection is only half the contract. What matters
    operationally is that the run reports failure through the existing exit-code
    semantics instead of quietly writing a new baseline.
    """
    config = _load_config()
    initial_state = {
        "version": 1,
        "sources": {
            regulatory_monitor.SOURCE_KEY_FINRA: {
                "last_run": "2026-08-01T10:00:00+00:00",
                "entries": {"FINRA 26-01": "existing-hash"},
            }
        },
    }
    loaded_state = deepcopy(initial_state)
    save_calls: list = []
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/26-14", "Regulatory Notice 26-14: Request for Comment")]
    )
    detail_html = FINRA_NON_NOTICE_FIXTURES[fixture_name]

    class _Session:
        def __init__(self):
            self.headers = {}

    def fake_fetch_page(url, _session, max_retries=3):
        content = (
            listing_html if url == regulatory_monitor.FINRA_NOTICES_URL else detail_html
        )
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(
        regulatory_monitor, "load_monitoring_config", lambda _path: config
    )
    monkeypatch.setattr(regulatory_monitor, "load_state", lambda _path: loaded_state)
    monkeypatch.setattr(
        regulatory_monitor, "save_state_atomic", lambda *args: save_calls.append(args)
    )
    monkeypatch.setattr(regulatory_monitor.requests, "Session", _Session)
    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)
    monkeypatch.setattr(
        regulatory_monitor.sys,
        "argv",
        ["regulatory_monitor.py", "--source", "finra"],
    )

    exit_code = regulatory_monitor.main()

    assert exit_code == regulatory_monitor.EXIT_FAILURE
    assert loaded_state == initial_state
    assert save_calls == []


# ===========================================================================
# Revision-6 adversarial regressions
#   Finding 1: FINRA listing pagination completeness + link canonicalization
#   Finding 2: electronic-recordkeeping polarity (paper permission vs paper
#              prohibition)
#   Finding 3: citation clause boundaries (author-date / researcher-led /
#              subordinate citations vs operative coordinated duties)
# Live-shaped fixtures. Each test proves a specific release-blocking defect is
# repaired and bounds its fail-open/fail-closed cost.
# ===========================================================================

_SRO_TITLE = (
    "Self-Regulatory Organizations; Notice of Filing of a Proposed Rule Change"
)


def _finra_listing_page_html(notice_hrefs, *, last_page=0, window_pages=None):
    """Return live-shaped FINRA notices *listing* markup.

    Mirrors the real Drupal listing: notices rendered as table rows (a title
    link plus a ``<time>`` cell) and, when paginated, a ``<nav>`` pager. The
    live pager renders only a sliding window of ``?page=N`` links plus a "Last"
    link, so two shapes are supported:

    * ``last_page > 0`` (window_pages is None): a short window plus an explicit
      "Last" link to ``?page={last_page}`` -- the real pager, where page 0 does
      reveal the true last page.
    * ``window_pages`` given: only those numbered links and no "Last" link -- a
      degraded/hostile pager that never advertises the true last, exercising the
      crawler's running-maximum page discovery.
    """
    rows = "".join(
        (
            "<tr><td class='views-field views-field-title'>"
            f"<a href=\"{href}\">Regulatory Notice "
            f"{href.rstrip('/').rsplit('/', 1)[-1]}</a></td>"
            "<td class='views-field views-field-field-date'>"
            "<time datetime='2026-08-01'>August 1, 2026</time></td></tr>"
        )
        for href in notice_hrefs
    )
    table = f"<table class='notices-table'><tbody>{rows}</tbody></table>"

    pager = ""
    if window_pages is not None:
        window = "".join(
            f"<li class='pager__item'><a href=\"?page={n}\">Page {n + 1}</a></li>"
            for n in window_pages
        )
        pager = (
            "<nav aria-labelledby='pagination-heading' role='navigation'>"
            f"<ul class='pagination js-pager__items'>{window}</ul></nav>"
        )
    elif last_page > 0:
        window = "".join(
            f"<li class='pager__item'><a href=\"?page={n}\">Page {n + 1}</a></li>"
            for n in range(1, min(last_page, 3) + 1)
        )
        pager = (
            "<nav aria-labelledby='pagination-heading' role='navigation'>"
            "<ul class='pagination js-pager__items'>"
            f"{window}"
            "<li class='pager__item pager__item--last'>"
            f"<a href=\"/rules-guidance/notices?page={last_page}\" rel='last'>"
            "Last &raquo;</a></li></ul></nav>"
        )
    return f"<html><body><main>{table}{pager}</main></body></html>"


def _finra_multipage_fetch(
    pages,
    *,
    record=None,
    detail_body="Neutral supervisory guidance for member firms.",
):
    """Build a ``fetch_page`` stub serving a multi-page FINRA listing.

    ``pages`` maps a 0-indexed listing page to its HTML. Page 0 is served for
    the bare ``FINRA_NOTICES_URL`` (backward compatibility with the single-page
    mocks), page N for ``?page=N``. Any other URL is a notice detail page. A
    listing page absent from ``pages`` returns HTTP 404 so a "declared but
    failing" page can be exercised. When given, ``record`` accumulates every
    requested URL for fetch-count assertions.
    """
    detail_html = _finra_notice_page(detail_body)
    prefix = f"{regulatory_monitor.FINRA_NOTICES_URL}?page="

    def fake_fetch_page(url, session, max_retries=3):
        if record is not None:
            record.append(url)
        page_index = None
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            page_index = 0
        elif url.startswith(prefix):
            try:
                page_index = int(url[len(prefix):])
            except ValueError:
                page_index = None
        if page_index is not None:
            content = pages.get(page_index)
            if content is None:
                return {
                    "url": url,
                    "status_code": 404,
                    "content": "",
                    "final_url": url,
                    "was_redirected": False,
                    "error": "not found",
                }
            return {
                "url": url,
                "status_code": 200,
                "content": content,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(detail_html, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    return fake_fetch_page


def _run_finra_crawl(monkeypatch, pages, *, record=None, limit=None):
    config = _load_config()
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _finra_multipage_fetch(pages, record=record),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)
    return regulatory_monitor.fetch_finra_notices(
        session=object(), config=config, limit=limit, detail_fetch_limit=None
    )


def _finra_listing_urls(record):
    base = regulatory_monitor.FINRA_NOTICES_URL
    return [u for u in record if u == base or u.startswith(f"{base}?page=")]


# --- Finding 1: pagination completeness --------------------------------------


def test_finra_pagination_discovers_page_two_notices(monkeypatch):
    """Notices on listing page 1 (the second page) must be discovered.

    The reviewer defect fetched only listing page 1, silently dropping every
    notice on pages 2..92.
    """
    pages = {
        0: _finra_listing_page_html(
            ["/rules-guidance/notices/26-100"], last_page=1
        ),
        1: _finra_listing_page_html(
            ["/rules-guidance/notices/26-200"], last_page=1
        ),
    }
    items = _run_finra_crawl(monkeypatch, pages)
    urls = {item.url for item in items}
    assert "https://www.finra.org/rules-guidance/notices/26-100" in urls
    assert "https://www.finra.org/rules-guidance/notices/26-200" in urls


def test_finra_pagination_completes_full_92_page_style_crawl(monkeypatch):
    """A 92-page listing must be crawled to the final page, not truncated.

    Every page advertises the true last page (0-indexed 91 == 92 pages). The
    crawl must fetch all 92 pages and collect every notice.
    """
    pages = {
        p: _finra_listing_page_html(
            [f"/rules-guidance/notices/26-{p + 100}"], last_page=91
        )
        for p in range(92)
    }
    record = []
    items = _run_finra_crawl(monkeypatch, pages, record=record)

    assert len(items) == 92
    assert len(_finra_listing_urls(record)) == 92
    assert f"{regulatory_monitor.FINRA_NOTICES_URL}?page=91" in record
    assert "https://www.finra.org/rules-guidance/notices/26-191" in {
        item.url for item in items
    }


def test_finra_pagination_follows_sliding_window_to_true_last_page(monkeypatch):
    """The live pager shows only a window; the running maximum must complete it.

    No single page reveals the true last page: each renders a small window whose
    maximum is only two pages ahead and there is no "Last" link. The crawl must
    still extend page-by-page to the real final page, or older eligible notices
    are silently skipped.
    """
    true_last = 10
    pages = {}
    for p in range(true_last + 1):
        window = list(range(max(0, p - 1), min(true_last, p + 2) + 1))
        pages[p] = _finra_listing_page_html(
            [f"/rules-guidance/notices/26-{p + 100}"], window_pages=window
        )
    # Precondition: page 0 only advertises up to page 2, never the true last.
    assert "page=10" not in pages[0]

    record = []
    items = _run_finra_crawl(monkeypatch, pages, record=record)
    assert len(items) == true_last + 1
    assert f"{regulatory_monitor.FINRA_NOTICES_URL}?page={true_last}" in record
    assert "https://www.finra.org/rules-guidance/notices/26-110" in {
        item.url for item in items
    }


def test_finra_pagination_deduplicates_notices_across_pages(monkeypatch):
    """A notice repeated across pages is collected exactly once."""
    pages = {
        0: _finra_listing_page_html(
            [
                "/rules-guidance/notices/26-100",
                "/rules-guidance/notices/26-200",
            ],
            last_page=1,
        ),
        1: _finra_listing_page_html(
            [
                "/rules-guidance/notices/26-200",
                "/rules-guidance/notices/26-300",
            ],
            last_page=1,
        ),
    }
    items = _run_finra_crawl(monkeypatch, pages)
    urls = [item.url for item in items]
    assert len(urls) == len(set(urls))
    assert sorted(set(urls)) == [
        "https://www.finra.org/rules-guidance/notices/26-100",
        "https://www.finra.org/rules-guidance/notices/26-200",
        "https://www.finra.org/rules-guidance/notices/26-300",
    ]


def test_finra_pagination_loop_is_detected_and_fails_closed(monkeypatch):
    """A pager repeating an earlier page's notices must raise, not loop.

    Fail-closed: identical content at a new page index must never be baselined
    as a completed crawl.
    """
    pages = {
        0: _finra_listing_page_html(
            ["/rules-guidance/notices/26-100"], last_page=1
        ),
        1: _finra_listing_page_html(
            ["/rules-guidance/notices/26-100"], last_page=1
        ),
    }
    with pytest.raises(regulatory_monitor.FinraListingError, match="loop"):
        _run_finra_crawl(monkeypatch, pages)


def test_finra_pagination_missing_declared_page_fails_closed(monkeypatch):
    """A declared page that yields no notices must raise (incomplete crawl)."""
    pages = {
        0: _finra_listing_page_html(
            ["/rules-guidance/notices/26-100"], last_page=1
        ),
        1: (
            "<html><head>"
            '<link rel="canonical" href="https://www.finra.org/rules-guidance/notices" />'
            "</head><body><main><table class='notices-table'>"
            "<tbody></tbody></table></main></body></html>"
        ),
    }
    with pytest.raises(regulatory_monitor.FinraListingError, match="declared"):
        _run_finra_crawl(monkeypatch, pages)


def test_finra_pagination_failing_declared_page_fails_closed(monkeypatch):
    """A declared page returning a non-200 must raise (no partial baseline)."""
    # Page 1 is declared by page 0's pager but absent from the fixture -> 404.
    pages = {
        0: _finra_listing_page_html(
            ["/rules-guidance/notices/26-100"], last_page=1
        ),
    }
    with pytest.raises(regulatory_monitor.FinraListingError):
        _run_finra_crawl(monkeypatch, pages)


def test_finra_pagination_hostile_unbounded_pager_is_bounded(monkeypatch):
    """A pager declaring an enormous last page raises before crawling it.

    Bounded safety against hostile/infinite pagination: reaching the page cap
    fails closed after a single fetch instead of issuing thousands of requests.
    """
    pages = {
        0: _finra_listing_page_html(
            ["/rules-guidance/notices/26-100"], last_page=999
        ),
    }
    record = []
    with pytest.raises(regulatory_monitor.FinraListingError, match="maximum"):
        _run_finra_crawl(monkeypatch, pages, record=record)
    assert len(_finra_listing_urls(record)) == 1


def test_finra_index_php_links_canonicalized_lookalikes_rejected(monkeypatch):
    """`/index.php/...` notice links canonicalize; lookalikes/off-origin rejected.

    The live listing exposes `/index.php/rules-guidance/notices/26-12` links;
    dropping them loses eligible notices. A lookalike `/index.phpx/...` prefix
    and an off-origin host must NOT be accepted (no origin/path broadening),
    and the detail fetch must use the canonical URL, never the alias.
    """
    pages = {
        0: _finra_listing_page_html(
            [
                "/index.php/rules-guidance/notices/26-12",
                "/index.phpx/rules-guidance/notices/26-99",
                "https://finra.org.attacker.example/rules-guidance/notices/26-77",
            ],
            last_page=0,
        ),
    }
    record = []
    items = _run_finra_crawl(monkeypatch, pages, record=record)
    urls = {item.url for item in items}
    assert urls == {"https://www.finra.org/rules-guidance/notices/26-12"}
    assert not any("index.php" in u for u in urls)
    assert not any("26-99" in u for u in urls)
    assert not any("26-77" in u for u in urls)
    assert "https://www.finra.org/rules-guidance/notices/26-12" in record
    assert not any("index.php" in u for u in record)


def test_finra_link_canonicalization_unit_matrix():
    """Direct accept/reject coverage of the canonicalizer and listing recogniser."""
    accept = {
        "/index.php/rules-guidance/notices/26-12":
            "https://www.finra.org/rules-guidance/notices/26-12",
        "/rules-guidance/notices/26-06":
            "https://www.finra.org/rules-guidance/notices/26-06",
        "https://www.finra.org/index.php/rules-guidance/notices/"
        "information-notice-20260114":
            "https://www.finra.org/rules-guidance/notices/"
            "information-notice-20260114",
        "/INDEX.PHP/rules-guidance/notices/26-01":
            "https://www.finra.org/rules-guidance/notices/26-01",
    }
    for raw, want in accept.items():
        assert regulatory_monitor._canonical_finra_notice_url(raw) == want, raw

    reject = [
        "/index.phpx/rules-guidance/notices/26-12",
        "/rules-guidance/notices/index.php/26-12",
        "https://finra.org.attacker.example/rules-guidance/notices/26-12",
        "https://notfinra.org/rules-guidance/notices/26-12",
        "//index.php//rules-guidance//notices//26-04",
    ]
    for raw in reject:
        assert regulatory_monitor._canonical_finra_notice_url(raw) is None, raw

    assert (
        regulatory_monitor._finra_listing_page_number(
            "/rules-guidance/notices?page=5"
        )
        == 5
    )
    assert (
        regulatory_monitor._finra_listing_page_number(
            "/index.php/rules-guidance/notices?page=91"
        )
        == 91
    )
    assert (
        regulatory_monitor._finra_listing_page_number(
            "/rules-guidance/notices/26-12?page=3"
        )
        is None
    )
    assert (
        regulatory_monitor._finra_listing_page_number(
            "https://evil.example/rules-guidance/notices?page=2"
        )
        is None
    )
    assert (
        regulatory_monitor._finra_listing_page_number(
            "/rules-guidance/notices?page=-4"
        )
        is None
    )


# --- Finding 2: electronic-recordkeeping polarity ----------------------------

_RECORDKEEPING_PAPER_PERMITTED = [
    # The reviewer's false-HIGH counterexample.
    "Records must be maintained electronically unless retained in paper form.",
    "Records must be maintained electronically except where paper copies are "
    "required.",
    "Records may be maintained electronically or retained in paper form.",
    "Records must be maintained electronically, or alternatively retained in "
    "paper form.",
    "Firms may keep records electronically; paper copies are also permitted.",
    "Either electronic or paper records may be maintained by the member.",
]


@pytest.mark.parametrize("detail_text", _RECORDKEEPING_PAPER_PERMITTED)
def test_recordkeeping_paper_permitted_is_not_electronic_mandate(detail_text):
    """False-HIGH repair: an electronic option that still permits paper (via
    unless/except/or/either/also-permitted) is not a mandatory electronic
    recordkeeping duty."""
    config = _load_config()
    for exclude_reference_only in (False, True):
        classification, reason = regulatory_monitor.classify_regulatory_relevance(
            _SRO_TITLE,
            detail_text,
            config,
            exclude_reference_only=exclude_reference_only,
        )
        assert reason != "Electronic recordkeeping", detail_text
        assert classification == regulatory_monitor.CLASSIFICATION_NOISE, detail_text


_RECORDKEEPING_PAPER_PROHIBITED = [
    # The reviewer's false-NOISE counterexample.
    "Records cannot be retained on paper and must be maintained electronically.",
    "Records may not be retained on paper and must be maintained "
    "electronically.",
    "Records must not be retained on paper and must be maintained "
    "electronically.",
    "Records shall not be retained in paper form and must be preserved "
    "electronically.",
    "Paper records are prohibited, and all records must be maintained "
    "electronically.",
]


@pytest.mark.parametrize("detail_text", _RECORDKEEPING_PAPER_PROHIBITED)
def test_recordkeeping_paper_prohibited_stays_electronic_mandate(detail_text):
    """False-NOISE repair: prohibiting paper (cannot/may not/must not/shall
    not/prohibited) while mandating electronic storage is an electronic
    recordkeeping HIGH, not permissive language."""
    config = _load_config()
    for exclude_reference_only in (False, True):
        classification, reason = regulatory_monitor.classify_regulatory_relevance(
            _SRO_TITLE,
            detail_text,
            config,
            exclude_reference_only=exclude_reference_only,
        )
        assert classification == regulatory_monitor.CLASSIFICATION_HIGH, detail_text
        assert reason == "Electronic recordkeeping", detail_text


def test_recordkeeping_polarity_preserves_prior_positive_and_negative():
    """Guard both directions: an unconditional electronic mandate stays HIGH and
    an explicitly optional electronic record stays NOISE."""
    config = _load_config()
    positive = (
        "All books and records must be preserved in an electronic storage medium."
    )
    negative = "Electronic records are optional, but firms must file paper copies."
    pc, pr = regulatory_monitor.classify_regulatory_relevance(
        _SRO_TITLE, positive, config
    )
    nc, nr = regulatory_monitor.classify_regulatory_relevance(
        _SRO_TITLE, negative, config
    )
    assert (pc, pr) == (
        regulatory_monitor.CLASSIFICATION_HIGH,
        "Electronic recordkeeping",
    )
    assert nr != "Electronic recordkeeping"
    assert nc == regulatory_monitor.CLASSIFICATION_NOISE


# --- Finding 3: citation clause boundaries -----------------------------------

_CITATION_NON_HIGH = {
    "and_smith_et_al_discuss": (
        "Members must file annual reports and Smith et al. discuss artificial "
        "intelligence in capital markets."
    ),
    "and_single_author_year": (
        "Members must file annual reports and Jones (2026) surveys artificial "
        "intelligence in capital markets."
    ),
    "and_two_authors_year": (
        "Members must file annual reports and Smith and Lee (2025) examine "
        "artificial intelligence adoption."
    ),
    "and_researchers_examine": (
        "Members must file annual reports and researchers examine artificial "
        "intelligence adoption."
    ),
    "and_scholars_debate": (
        "Members must file annual reports and scholars debate artificial "
        "intelligence governance."
    ),
    "and_economists_study": (
        "Members must file annual reports and economists study artificial "
        "intelligence in markets."
    ),
    "and_commentators_caution": (
        "Members must file annual reports and commentators caution about "
        "artificial intelligence risk."
    ),
    "and_recent_study_examines": (
        "Members must file annual reports and a recent study examines "
        "artificial intelligence in capital markets."
    ),
    "because_researchers_survey": (
        "Members must file annual reports because researchers survey artificial "
        "intelligence adoption."
    ),
    "although_smith_et_al": (
        "Members must file annual reports although Smith et al. discuss "
        "artificial intelligence."
    ),
    "while_economists_study": (
        "Members must file annual reports while economists study artificial "
        "intelligence in markets."
    ),
}


@pytest.mark.parametrize("case", sorted(_CITATION_NON_HIGH))
def test_citation_led_clause_beside_unrelated_duty_stays_non_high(case):
    """A citing subject -- author-date "(2026) surveys", `et al.`, or a
    researcher-led clause, coordinated or subordinate -- opens a fresh clause,
    so an unrelated duty elsewhere in the sentence cannot promote the
    bibliographic AI mention to HIGH."""
    config = _load_config()
    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10",
        _CITATION_NON_HIGH[case],
        config,
        exclude_reference_only=True,
    )
    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, (case, classification, reason)
    assert "artificial intelligence" not in reason.lower()


_CITATION_OPERATIVE_HIGH = {
    "monitor_and_govern": (
        "Members must monitor and govern artificial intelligence systems."
    ),
    "supervise_and_govern": (
        "Members must supervise and govern artificial intelligence tools."
    ),
    "review_and_study": (
        "Members must review and study artificial intelligence systems."
    ),
    "monitor_and_conduct_studies": (
        "Members must monitor and conduct annual studies of artificial "
        "intelligence systems."
    ),
    "duty_with_intervening_reference": (
        "Members must, in accordance with Rule 3110, supervise artificial "
        "intelligence tools used for customer communications."
    ),
}


@pytest.mark.parametrize("case", sorted(_CITATION_OPERATIVE_HIGH))
def test_operative_coordinated_ai_duty_stays_high(case):
    """The cost guard: a coordinated predicate ("and govern", "and study",
    "and conduct annual studies") has no citing subject and must remain an
    operative AI duty (HIGH), never mis-split as a citation."""
    config = _load_config()
    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10",
        _CITATION_OPERATIVE_HIGH[case],
        config,
        exclude_reference_only=True,
    )
    assert classification == regulatory_monitor.CLASSIFICATION_HIGH, case

# ---------------------------------------------------------------------------
# Finding 1 -- FINRA tombstone notices must never be baselined
# ---------------------------------------------------------------------------

# The live example is /rules-guidance/notices/83-16, whose notice body is the
# literal string below. It is served with HTTP 200 inside a normal notice
# article, so neither the status code nor the container shape distinguishes it
# from a real notice.
FINRA_LIVE_TOMBSTONE_BODY = "NOT AVAILABLE AT THIS TIME Notice Comments"

FINRA_TOMBSTONE_BODIES = {
    "live_83_16": FINRA_LIVE_TOMBSTONE_BODY,
    "sentence_case": "This notice is not available at this time.",
    "no_longer_online": "The notice is no longer available online.",
    "text_of_notice_unavailable": "The text of this notice is not available.",
    "not_currently_available": "This notice is not currently available.",
    "unavailable_at_this_time": "Notice text unavailable at this time.",
    "not_available_online": "This notice is not available online.",
    "not_available_electronically": "This notice is not available electronically.",
}


def _finra_listing_html(entries: list[tuple[str, str]]) -> str:
    """Build a FINRA listing page from ``(href, link text)`` pairs.

    Rows are rendered as real listing rows. The extractor no longer has an
    all-anchor fallback, because that fallback is what let a same-origin
    article that merely links to notices be read as a complete listing, so a
    fixture of bare floating anchors is no longer a "simple listing" -- it is a
    page with no listing rows at all, which the monitor must now reject.
    """
    rows = "".join(
        f"<tr><td class='views-field views-field-title'>"
        f"<a href='{href}'>{label}</a></td></tr>"
        for href, label in entries
    )
    return (
        "<html><head>"
        '<link rel="canonical" href="https://www.finra.org/rules-guidance/notices" />'
        "</head><body><main>"
        f"<table class='notices-table'><tbody>{rows}</tbody></table>"
        "</main></body></html>"
    )


def _finra_routing_fetch(listing_html: str, detail_by_url: dict[str, str]):
    """Return a ``fetch_page`` stub serving a listing and per-URL detail pages."""

    def fake_fetch_page(url, session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            content = listing_html
        else:
            content = _with_finra_canonical(detail_by_url[url], url)
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    return fake_fetch_page


@pytest.mark.parametrize("fixture_name", sorted(FINRA_TOMBSTONE_BODIES))
def test_finra_tombstone_body_is_never_authoritative_text(fixture_name):
    """A tombstone is a *successful* answer that declares there is no text.

    The old extractor returned it as the notice body, so a placeholder became
    both the classification input and the change-detection fingerprint.
    """
    html = _finra_notice_page(FINRA_TOMBSTONE_BODIES[fixture_name])

    text, reason, rejected_non_notice = regulatory_monitor._scan_finra_notice_body(
        html
    )

    assert text == "", (fixture_name, text)
    assert reason, fixture_name
    assert rejected_non_notice is False, (
        "a tombstone is not error/challenge chrome and must be classified "
        "separately from it"
    )
    with pytest.raises(regulatory_monitor.FinraNoticeUnavailableError):
        regulatory_monitor._extract_finra_notice_required_text(html)


def test_finra_tombstone_is_not_a_required_source_text_error():
    """Deliberate type split.

    ``RequiredSourceTextError`` means "the notice exists and we could not read
    it" and fails the run closed. A tombstone means "there is nothing to read",
    permanently, so it must not be able to take FINRA monitoring down forever.
    """
    assert not issubclass(
        regulatory_monitor.FinraNoticeUnavailableError,
        regulatory_monitor.RequiredSourceTextError,
    )


def test_finra_live_83_16_tombstone_excluded_while_run_completes(monkeypatch):
    """End-to-end proof for the reviewer's exact case.

    Notice 83-16's live tombstone must not be classified, hashed, or
    baselined, the surrounding source run must still complete, and a real
    notice in the same run must still land.
    """
    config = _load_config()
    tombstone_url = "https://www.finra.org/rules-guidance/notices/83-16"
    valid_url = "https://www.finra.org/rules-guidance/notices/26-14"
    listing_html = _finra_listing_html(
        [
            ("/rules-guidance/notices/83-16", "Notice to Members 83-16"),
            (
                "/rules-guidance/notices/26-14",
                "Regulatory Notice 26-14: Request for Comment",
            ),
        ]
    )
    detail_by_url = {
        tombstone_url: _finra_notice_page(FINRA_LIVE_TOMBSTONE_BODY),
        valid_url: _finra_notice_page(
            "Summary: Member firms must supervise the use of artificial "
            "intelligence in all customer communications and must retain "
            "supervisory evidence."
        ),
    }

    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _finra_routing_fetch(listing_html, detail_by_url),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    unavailable: list[dict] = []
    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
        unavailable_notices=unavailable,
    )

    assert [item.document_id for item in items] == ["FINRA 26-14"], (
        "the tombstoned notice must be excluded from the returned items"
    )
    assert [entry["document_id"] for entry in unavailable] == ["FINRA 83-16"]
    assert unavailable[0]["reason"] == "NOT AVAILABLE AT THIS TIME"
    assert unavailable[0]["url"] == tombstone_url

    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FINRA, items, state
    )
    entries = regulatory_monitor.get_source_state(
        state, regulatory_monitor.SOURCE_KEY_FINRA
    )["entries"]
    assert set(entries) == {"FINRA 26-14"}, (
        "a tombstone must never receive a content fingerprint"
    )
    assert FINRA_LIVE_TOMBSTONE_BODY not in json.dumps(state)


def test_finra_tombstone_only_run_completes_without_baselining(monkeypatch):
    """A run whose only notice is a tombstone completes and baselines nothing.

    Fail-closed would be the wrong choice here: the 1983 tombstones are
    permanent, so raising would disable FINRA monitoring for good.
    """
    config = _load_config()
    tombstone_url = "https://www.finra.org/rules-guidance/notices/83-16"
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/83-16", "Notice to Members 83-16")]
    )

    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _finra_routing_fetch(
            listing_html,
            {tombstone_url: _finra_notice_page(FINRA_LIVE_TOMBSTONE_BODY)},
        ),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    unavailable: list[dict] = []
    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
        unavailable_notices=unavailable,
    )

    assert items == []
    assert len(unavailable) == 1

    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FINRA, items, state
    )
    assert (
        regulatory_monitor.get_source_state(
            state, regulatory_monitor.SOURCE_KEY_FINRA
        )["entries"]
        == {}
    )


def test_finra_tombstone_is_reported_not_silently_dropped(monkeypatch, caplog):
    """Exclusion must be visible: silence would hide a shrinking corpus."""
    config = _load_config()
    tombstone_url = "https://www.finra.org/rules-guidance/notices/83-16"
    listing_html = _finra_listing_html(
        [("/rules-guidance/notices/83-16", "Notice to Members 83-16")]
    )

    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _finra_routing_fetch(
            listing_html,
            {tombstone_url: _finra_notice_page(FINRA_LIVE_TOMBSTONE_BODY)},
        ),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    with caplog.at_level(logging.WARNING, logger=regulatory_monitor.logger.name):
        regulatory_monitor.fetch_finra_notices(session=object(), config=config)

    assert any(
        "FINRA 83-16" in record.getMessage()
        and "no notice text" in record.getMessage()
        for record in caplog.records
    ), caplog.text


def test_finra_error_page_outranks_tombstone_and_still_fails_closed(monkeypatch):
    """Ambiguity resolves toward integrity failure, not toward "no content".

    If a page carries both denial chrome and tombstone wording we cannot tell
    whether real text is being withheld, so the run fails closed.
    """
    config = _load_config()
    detail_url = "https://www.finra.org/rules-guidance/notices/26-14"
    listing_html = _finra_listing_html(
        [
            (
                "/rules-guidance/notices/26-14",
                "Regulatory Notice 26-14: Request for Comment",
            )
        ]
    )
    both_html = (
        "<html><body><main>"
        "<article class='node node--type-page'>"
        "<div class='field field--name-body'><h1>Access Denied</h1>"
        "<p>You do not have permission to access this page.</p></div>"
        "</article>"
        "<article class='node node--type-notice'>"
        "<div class='field field--name-body'>NOT AVAILABLE AT THIS TIME</div>"
        "</article>"
        "</main></body></html>"
    )

    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _finra_routing_fetch(listing_html, {detail_url: both_html}),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_finra_notices(
            session=object(), config=config
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FINRA, items, state
        )

    assert state == {}


def test_finra_substantial_notice_mentioning_unavailability_survives():
    """The tombstone screen must not eat notices that discuss availability.

    Real notices legitimately say things like "the data are not available at
    this time", so the same substantial-and-structured safety valve used for
    the error screen applies here.
    """
    body = (
        "Suggested Routing: Compliance, Legal, Operations. Certain trade "
        "reporting statistics are not available at this time and will be "
        "published later. "
        + ("Member firms must retain the supervisory records described here. " * 60)
    )
    text, reason, rejected = regulatory_monitor._scan_finra_notice_body(
        _finra_notice_page(body)
    )

    assert reason is None
    assert rejected is False
    assert "Member firms must retain the supervisory records" in text


# ---------------------------------------------------------------------------
# Finding 2 -- Federal Register challenge/error bodies and final origin
# ---------------------------------------------------------------------------

FEDERAL_REGISTER_NON_DOCUMENT_BODIES = {
    "access_denied": (
        "Access Denied. You do not have permission to access this document "
        "on this server."
    ),
    "verify_human": (
        "Please verify you are a human before continuing to "
        "federalregister.gov."
    ),
    "captcha": "Security check. Complete the CAPTCHA below to continue.",
    "request_blocked": (
        "Your request was blocked by our security service. Ray ID 8f0a."
    ),
    "checking_browser": (
        "Checking your browser before accessing the site. This process is "
        "automatic."
    ),
    "login_required": (
        "Log in to continue. Authentication required to view this document."
    ),
    "error_403": "Error 403 - Forbidden. The requested resource is not accessible.",
    "not_found_404": "404 Not Found. The page you requested could not be found.",
    "cloudflare_interstitial": (
        "Attention Required! Cloudflare Ray ID: 7d2c1. Please enable "
        "JavaScript and cookies to continue."
    ),
    "service_unavailable": (
        "Service temporarily unavailable. Please try again later."
    ),
    "not_authorized": "You are not authorized to view this document.",
    "session_expired": "Your session has expired. Sign in to continue.",
}


def _federal_register_text_fetch(body: str, *, final_url=None):
    """Return a ``fetch_page`` stub serving ``body`` as the raw-text document."""

    def fake_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 200,
            "content": f"<html><body><pre>{body}</pre></body></html>",
            "final_url": url if final_url is None else final_url,
            "was_redirected": final_url is not None and final_url != url,
            "error": None,
        }

    return fake_fetch_page


@pytest.mark.parametrize("fixture_name", sorted(FEDERAL_REGISTER_NON_DOCUMENT_BODIES))
def test_federal_register_two_hundred_challenge_bodies_fail_closed(
    fixture_name, monkeypatch
):
    """HTTP 200 is not proof the authoritative document was served.

    Edge networks answer denials, bot challenges, captchas, login walls, and
    not-found pages with 200 and a full body. The old extractor accepted any of
    them, so the placeholder became the classification input *and* the
    change-detection fingerprint.
    """
    config = _load_config()
    session = _PagedFederalRegisterSession({1: _federal_register_source_text_page()})
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _federal_register_text_fetch(
            FEDERAL_REGISTER_NON_DOCUMENT_BODIES[fixture_name]
        ),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-08-13",
            config=config,
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )

    assert state == {}, "a challenge/error body must not advance source state"


FEDERAL_REGISTER_BAD_ORIGINS = {
    "off_origin_host": "https://cdn.example.test/2026-16471.txt",
    "subdomain_drift": "https://mirror.federalregister.gov/2026-16471.txt",
    "https_downgrade": (
        "http://www.federalregister.gov/documents/full_text/text/"
        "2026/08/13/2026-16471.txt"
    ),
    "challenge_path": "https://www.federalregister.gov/cdn-cgi/challenge-platform/x",
    "login_path": "https://www.federalregister.gov/login?next=/documents",
    "captcha_path": "https://www.federalregister.gov/captcha",
    "error_path": "https://www.federalregister.gov/errors/403",
    "non_http_scheme": "ftp://www.federalregister.gov/2026-16471.txt",
}


@pytest.mark.parametrize("fixture_name", sorted(FEDERAL_REGISTER_BAD_ORIGINS))
def test_federal_register_untrusted_final_origin_fails_closed(
    fixture_name, monkeypatch
):
    """Validate where the bytes finally came from, not just the status code.

    A 200 served after a redirect to another host, a downgraded scheme, or an
    interstitial path is not the authoritative document, and the body alone can
    be perfectly innocuous.
    """
    config = _load_config()
    session = _PagedFederalRegisterSession({1: _federal_register_source_text_page()})
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _federal_register_text_fetch(
            "Members must retain electronic communications records.",
            final_url=FEDERAL_REGISTER_BAD_ORIGINS[fixture_name],
        ),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session,
            since_date="2026-08-13",
            config=config,
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )

    assert state == {}


def test_federal_register_same_origin_redirect_is_accepted(monkeypatch):
    """The origin gate must not reject ordinary same-host path redirects.

    The redirect target deliberately preserves the document identity
    (``2026-16471``) while changing the path *shape*: finding 5 binds the
    authoritative-text URL to the requested document, so a redirect may move
    between accepted endpoint shapes but may not change which document is
    being read.
    """
    config = _load_config()
    session = _PagedFederalRegisterSession({1: _federal_register_source_text_page()})
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _federal_register_text_fetch(
            "Members must retain electronic communications records.",
            final_url=(
                "https://www.federalregister.gov/documents/2026/08/13/"
                "2026-16471.txt"
            ),
        ),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-08-13",
        config=config,
    )

    assert len(items) == 1
    assert "electronic communications records" in items[0].content_text


def test_federal_register_long_document_survives_incidental_challenge_words(
    monkeypatch,
):
    """The cost guard for finding 2.

    Rulemakings about access controls, captchas, and authentication routinely
    quote the exact phrases the screen looks for. A substantial, structurally
    recognisable Federal Register document must survive them, otherwise the
    fix converts an integrity hole into a run-wide outage.
    """
    config = _load_config()
    body = (
        "[Federal Register Volume 91, Number 12] SECURITIES AND EXCHANGE "
        "COMMISSION AGENCY: Securities and Exchange Commission. ACTION: Final "
        "rule. SUMMARY: The Commission is adopting rules addressing access "
        "denied events, captcha deployment, verify you are a human challenges, "
        "and login required workflows at registered broker-dealers. "
        "SUPPLEMENTARY INFORMATION: "
        + ("Member firms must retain the associated records electronically. " * 60)
        + "[FR Doc. 2026-16471 Filed 8-12-26; 8:45 am] BILLING CODE 8011-01-P"
    )
    assert len(body) >= regulatory_monitor.FEDERAL_REGISTER_DOCUMENT_SUBSTANTIAL_CHARS

    session = _PagedFederalRegisterSession({1: _federal_register_source_text_page()})
    monkeypatch.setattr(
        regulatory_monitor, "fetch_page", _federal_register_text_fetch(body)
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session,
        since_date="2026-08-13",
        config=config,
    )

    assert len(items) == 1
    assert "BILLING CODE" in items[0].content_text
    assert items[0].classification in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }


def test_federal_register_short_valid_document_is_not_rejected():
    """Short administrative notices carry no FR header and must still pass.

    A hard structural requirement would fail closed on every legitimate short
    document, so structure is only a safety valve, never an entry condition.
    """
    extracted = regulatory_monitor._extract_federal_register_source_text(
        "<html><body><pre>SECURITIES AND EXCHANGE COMMISSION Release No. "
        "34-99999; File No. SR-FINRA-2026-001 Notice of Filing of a Proposed "
        "Rule Change.</pre></body></html>"
    )

    assert extracted.startswith("SECURITIES AND EXCHANGE COMMISSION")


def test_source_origin_rejection_reason_matrix():
    """Direct unit coverage of the origin rule, including its exemptions."""
    reason_for = regulatory_monitor._source_origin_rejection_reason
    requested = "https://www.federalregister.gov/a.txt"

    assert reason_for(requested, requested) is None
    assert reason_for(requested, None) is None, (
        "absence of redirect information is not evidence of a redirect"
    )
    assert reason_for(requested, "") is None
    assert reason_for(requested, "https://www.federalregister.gov/b.txt") is None
    assert reason_for(requested, "https://WWW.FederalRegister.GOV/a.txt") is None
    assert reason_for(requested, "https://evil.test/a.txt")
    assert reason_for(requested, "http://www.federalregister.gov/a.txt")
    assert reason_for(requested, "file:///c:/a.txt")
    assert reason_for(requested, "https://www.federalregister.gov/cdn-cgi/x")


# ---------------------------------------------------------------------------
# Finding 3 -- title and body are separate evidence fields
# ---------------------------------------------------------------------------


def test_reviewer_case_operative_title_does_not_promote_citation_only_body():
    """The reviewer's exact case.

    Concatenating title and body with one space let "Members must report
    suspicious activity" sit in the same sentence window as the body's opening
    citation, so an unrelated reporting duty in the *title* promoted a purely
    bibliographic AI mention in the *body*.
    """
    config = _load_config()
    title = "Members must report suspicious activity"
    body = (
        "According to Jones (2026), artificial intelligence affects capital "
        "markets."
    )

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        title, body, config, exclude_reference_only=True
    )
    controls = regulatory_monitor.find_affected_controls_by_keywords(
        title, body, config, exclude_reference_only=True
    )

    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, (classification, reason)
    assert "artificial intelligence" not in reason.lower()
    assert controls == []


@pytest.mark.parametrize(
    ("title", "body"),
    [
        (
            "Members must supervise artificial intelligence systems",
            "Routine administrative matter.",
        ),
        (
            "Quarterly administrative notice",
            "Members must supervise artificial intelligence systems.",
        ),
    ],
    ids=["operative_in_title", "operative_in_body"],
)
def test_operative_ai_language_detected_in_either_field(title, body):
    """Separation must not become blindness: either field alone still counts."""
    config = _load_config()

    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        title, body, config, exclude_reference_only=True
    )
    controls = regulatory_monitor.find_affected_controls_by_keywords(
        title, body, config, exclude_reference_only=True
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert controls


@pytest.mark.parametrize(
    ("title", "body"),
    [
        ("Notice regarding supervision", "Electronic filing deadlines change."),
        ("Guidance from FINRA", "Retail communications standards are unchanged."),
    ],
    ids=["supervision_electronic", "finra_retail_communications"],
)
def test_windowed_patterns_cannot_span_the_title_body_boundary(title, body):
    """``.{0,80}`` windows in the config must not straddle two fields.

    ``supervision.{0,80}(?:electronic|...)`` and the FINRA/retail-communications
    pattern each matched by taking one term from the title and one from the
    body, which is evidence that exists in neither field.
    """
    config = _load_config()

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        title, body, config, exclude_reference_only=True
    )

    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, (classification, reason)


def test_windowed_pattern_still_matches_within_one_field():
    """The same window must still work when both terms are in one field."""
    config = _load_config()

    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Quarterly notice",
        "Firms must update supervision of electronic systems.",
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH


def test_classification_segments_never_concatenate_fields():
    """Structural guard: the segments are the fields, not a joined string."""
    segments = regulatory_monitor._classification_segments("a title", "a body")

    assert list(segments) == ["a title", "a body"]
    assert not any("a title a body" in segment for segment in segments)


# ---------------------------------------------------------------------------
# Finding 4 -- proper-name attribution citations
# ---------------------------------------------------------------------------

_ATTRIBUTION_NON_HIGH = {
    "according_to_author_year": (
        "According to Jones (2026), artificial intelligence affects capital "
        "markets."
    ),
    "according_to_author_et_al": (
        "According to Smith et al. (2025), artificial intelligence adoption is "
        "uneven."
    ),
    "as_reported_by": (
        "As reported by Chen (2024), artificial intelligence changes market "
        "structure."
    ),
    "as_noted_by": (
        "As noted by Jones (2026), artificial intelligence affects capital "
        "markets."
    ),
    "as_described_in": (
        "As described in Jones (2026), artificial intelligence affects capital "
        "markets."
    ),
    "per_two_authors": (
        "Per Smith and Lee (2026), artificial intelligence affects liquidity."
    ),
    "according_to_a_recent_study": (
        "According to a recent study, artificial intelligence affects capital "
        "markets."
    ),
    "according_to_researchers": (
        "According to researchers, artificial intelligence affects capital "
        "markets."
    ),
    "mid_sentence_after_semicolon": (
        "Members must file annual reports; according to Jones (2026), "
        "artificial intelligence affects capital markets."
    ),
    "mid_sentence_after_comma": (
        "Members must file annual reports, and according to Jones (2026), "
        "artificial intelligence affects capital markets."
    ),
    "trailing_parenthetical": (
        "Members must file annual reports, and artificial intelligence "
        "adoption is uneven (Jones, 2026)."
    ),
    "trailing_parenthetical_et_al": (
        "Members must file annual reports, while artificial intelligence "
        "adoption is uneven (Smith et al., 2025)."
    ),
    "trailing_parenthetical_two_authors": (
        "Members must file annual reports, and artificial intelligence changes "
        "liquidity (Smith and Lee, 2026)."
    ),
    "trailing_parenthetical_with_page": (
        "Members must file annual reports, and artificial intelligence changes "
        "liquidity (Jones, 2026, p. 14)."
    ),
    "trailing_parenthetical_own_sentence": (
        "Members must file annual reports. Artificial intelligence adoption is "
        "uneven (Jones, 2026)."
    ),
}


@pytest.mark.parametrize("case", sorted(_ATTRIBUTION_NON_HIGH))
def test_proper_name_attribution_stays_non_high(case):
    """Casing is unavailable (the text is lowercased), so a proper name has to
    be recognised structurally: an attribution lead plus a parenthetical year,
    or a trailing "(Name, Year)" pair."""
    config = _load_config()
    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10",
        _ATTRIBUTION_NON_HIGH[case],
        config,
        exclude_reference_only=True,
    )

    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, (case, classification, reason)
    assert "artificial intelligence" not in reason.lower()


_ATTRIBUTION_OPERATIVE_HIGH = {
    "operative_after_attribution": (
        "According to Jones (2026), members must supervise artificial "
        "intelligence systems."
    ),
    "operative_in_attributed_clause": (
        "As reported by Chen (2024), firms shall retain artificial "
        "intelligence model records."
    ),
    "operative_with_trailing_citation": (
        "Members must supervise artificial intelligence systems (Jones, 2026)."
    ),
    "operative_after_comma_with_citation": (
        "Firms file reports, and members must supervise artificial "
        "intelligence systems (Jones, 2026)."
    ),
}


@pytest.mark.parametrize("case", sorted(_ATTRIBUTION_OPERATIVE_HIGH))
def test_operative_language_in_attributed_clause_takes_precedence(case):
    """Attribution never outranks a duty in the AI-bearing clause."""
    config = _load_config()
    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10",
        _ATTRIBUTION_OPERATIVE_HIGH[case],
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH, case


_NON_CITATION_PARENTHETICALS = {
    "bare_date": "Members must supervise artificial intelligence systems (September 2026).",
    "effective_year": "Firms shall govern artificial intelligence tools (effective 2027).",
    "release_number": (
        "Members must govern artificial intelligence tools (Release No. 34-99999)."
    ),
    "cfr_citation": (
        "Members must retain artificial intelligence records (17 CFR 240.17a-4)."
    ),
}


@pytest.mark.parametrize("case", sorted(_NON_CITATION_PARENTHETICALS))
def test_date_and_reference_parentheticals_are_not_author_date_citations(case):
    """The trailing form deliberately requires "<name>, <year>".

    "(September 2026)" and "(effective 2027)" are dates, not citations, and
    treating them as citations would suppress genuine operative duties.
    """
    config = _load_config()
    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10",
        _NON_CITATION_PARENTHETICALS[case],
        config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH, case


# ---------------------------------------------------------------------------
# Finding 5 -- mandatory electronic recordkeeping forms
# ---------------------------------------------------------------------------

_RECORDKEEPING_MANDATORY = {
    "electronic_modifier_before_store": (
        "Records must be electronically stored for six years."
    ),
    "electronic_modifier_before_maintain": (
        "Records must be electronically maintained by each member firm."
    ),
    "electronic_modifier_before_preserve": (
        "Records shall be electronically preserved in a non-rewriteable format."
    ),
    "electronic_modifier_after_obligation": (
        "Each member must electronically preserve all communications records."
    ),
    "permissive_word_in_subject_clause": (
        "Records that may contain customer information must be retained "
        "electronically."
    ),
    "permissive_word_in_relative_clause": (
        "Books and records that may be requested must be preserved in "
        "electronic format."
    ),
    "plain_mandatory": (
        "Broker-dealers must retain records electronically for six years."
    ),
    "shall_maintain_electronic_form": (
        "Firms shall maintain records in electronic form."
    ),
    "required_to_be_stored": "Records are required to be stored electronically.",
    "paper_prohibited": (
        "Paper records are prohibited; records must be stored electronically."
    ),
    "may_not_paper_must_electronic": (
        "Records may not be maintained on paper and must be retained "
        "electronically."
    ),
}


@pytest.mark.parametrize("case", sorted(_RECORDKEEPING_MANDATORY))
def test_mandatory_electronic_recordkeeping_forms_are_detected(case):
    """Two repairs are covered here.

    The electronic term can *modify* the storage verb rather than follow it
    ("must be electronically stored"), and a permissive word inside a subject
    or relative clause ("records that **may** contain customer information")
    does not make the storage duty optional -- only a permissive word bound to
    the storage predicate does.
    """
    assert regulatory_monitor._has_electronic_recordkeeping_obligation(
        _RECORDKEEPING_MANDATORY[case]
    ), case


_RECORDKEEPING_NOT_MANDATORY = {
    "may_be_stored": "Records may be stored electronically.",
    "may_retain_if_they_choose": (
        "Firms may retain records in electronic format if they choose."
    ),
    "electronic_or_paper": "Records may be maintained electronically or on paper.",
    "optional": "Electronic storage of records is optional.",
    "paper_alternative": (
        "Records must be retained; electronic storage is permitted as an "
        "alternative to paper."
    ),
    "permitted_to_store": "Firms are permitted to store records electronically.",
    "retention_without_electronic": "Records must be retained for six years.",
    "discussion_only": "Electronic communications are discussed in the release.",
    "paper_form_alternative": (
        "Records may be kept in paper form as an alternative to electronic "
        "storage."
    ),
    "does_not_require": "The rule does not require electronic recordkeeping.",
    "need_not": "Firms need not store records electronically.",
    "at_firm_option": "Electronic storage is available at the firm's option.",
    "nothing_requires": (
        "Nothing in this rule requires records to be stored electronically."
    ),
}


@pytest.mark.parametrize("case", sorted(_RECORDKEEPING_NOT_MANDATORY))
def test_permissive_and_paper_alternative_recordkeeping_stays_negative(case):
    """The polarity guard: binding permissive words to the storage predicate
    must not turn optional or paper-alternative language into an obligation."""
    assert not regulatory_monitor._has_electronic_recordkeeping_obligation(
        _RECORDKEEPING_NOT_MANDATORY[case]
    ), case


def test_permissive_modal_mask_only_clears_storage_bound_modals():
    """Unit-level proof of the masking rule.

    The mask removes permissive modals that are *not* bound to a storage
    predicate so the whole-match optional/negated scan stops firing on them,
    and leaves the storage-bound ones in place so genuine "may be stored"
    remains optional.
    """
    mask = regulatory_monitor._mask_unbound_permissive_modals

    masked_subject = mask(
        "records that may contain customer information must be retained "
        "electronically"
    )
    assert "may contain" not in masked_subject
    assert "must be retained" in masked_subject

    masked_storage = mask("records may be stored electronically")
    assert "may be stored" in masked_storage


# ---------------------------------------------------------------------------
# Finding 6 -- boundary indexing: same semantics, linear cost
# ---------------------------------------------------------------------------


def _reference_sentence_span(text: str, start: int, end: int) -> tuple[int, int]:
    """Pre-index implementation, copied verbatim as a differential oracle.

    This is the code the index replaced: it rescans every preceding footnote
    delimiter and every preceding sentence terminator from offset 0 for *each*
    match, which is what made classification quadratic.
    """
    preceding_delimiters = list(
        regulatory_monitor.FOOTNOTE_BLOCK_DELIMITER_PATTERN.finditer(text, 0, start)
    )
    segment_start = preceding_delimiters[-1].end() if preceding_delimiters else 0
    following_delimiter = regulatory_monitor.FOOTNOTE_BLOCK_DELIMITER_PATTERN.search(
        text, end
    )
    segment_end = following_delimiter.start() if following_delimiter else len(text)

    preceding_boundaries = list(
        regulatory_monitor._real_sentence_boundaries(text, segment_start, start)
    )
    if preceding_boundaries:
        segment_start = preceding_boundaries[-1].end()

    following_boundary = next(
        regulatory_monitor._real_sentence_boundaries(text, end, segment_end), None
    )
    if following_boundary:
        segment_end = following_boundary.start()

    return segment_start, segment_end


def _reference_clause_span(text: str, start: int, end: int) -> tuple[int, int]:
    """Pre-index clause resolution, copied verbatim as a differential oracle."""
    sentence_start, sentence_end = _reference_sentence_span(text, start, end)
    clause_start, clause_end = sentence_start, sentence_end

    clause_boundaries = [
        boundary.end()
        for boundary in regulatory_monitor.CLAUSE_BOUNDARY_PATTERN.finditer(
            text, sentence_start, start
        )
    ]
    citation_starts = [
        boundary.end()
        for boundary in regulatory_monitor.CITATION_SUBJECT_BOUNDARY_PATTERN.finditer(
            text, sentence_start, start
        )
    ]
    if citation_starts:
        citation_start = max(citation_starts)
        clause_start = max(
            [sentence_start, citation_start]
            + [cb for cb in clause_boundaries if cb <= citation_start]
        )
    elif clause_boundaries:
        clause_start = max(clause_boundaries)

    following_clause_boundary = regulatory_monitor.CLAUSE_BOUNDARY_PATTERN.search(
        text, end, sentence_end
    )
    if following_clause_boundary:
        clause_end = following_clause_boundary.start()
    following_citation_subject = (
        regulatory_monitor.CITATION_SUBJECT_BOUNDARY_PATTERN.search(
            text, end, sentence_end
        )
    )
    if following_citation_subject:
        clause_end = min(clause_end, following_citation_subject.start())

    return clause_start, clause_end


_BOUNDARY_ORACLE_CORPUS = [
    "Members must file annual reports and Smith et al. discuss artificial "
    "intelligence in capital markets.",
    "The Commission proposes to amend deadlines, and a recent working paper on "
    "artificial intelligence is available at https://example.test/paper.pdf.",
    "According to Jones (2026), artificial intelligence affects capital markets.",
    "Firms must supervise artificial intelligence tools.\\451\\ See also Smith, "
    "supra note 3.",
    "Text before.\n-------------------\nFootnote block cites artificial "
    "intelligence research; see also id. Text after.",
    "Members must monitor and govern artificial intelligence systems (September "
    "2026); firms shall retain artificial intelligence records.",
    "artificial intelligence",
    "Artificial intelligence. Artificial intelligence; artificial intelligence!",
    "A sentence ending in an abbreviation such as e.g. artificial intelligence "
    "adoption, i.e. the deployment of models, is common.",
    "(Artificial intelligence) -- artificial intelligence [artificial "
    "intelligence] artificial intelligence, artificial intelligence: end.",
    "Multiple---dashes and \u2014em dashes\u2014around artificial intelligence "
    "mentions, because researchers document adoption.",
    "No terminator at all and artificial intelligence sits at the very end",
    "artificial intelligence at the very start and members must retain records.",
]


@pytest.mark.parametrize("corpus_index", range(len(_BOUNDARY_ORACLE_CORPUS)))
def test_boundary_index_matches_pre_index_reference_implementation(corpus_index):
    """Differential test: the optimisation must not change any boundary.

    The performance repair is only acceptable if it is semantics-preserving, so
    every occurrence in an adversarial corpus is resolved by both the old
    rescan-per-match code and the indexed code and the spans are compared
    directly.
    """
    text = _BOUNDARY_ORACLE_CORPUS[corpus_index].lower()
    index = regulatory_monitor._boundary_index(text)

    probes = [
        (match.start(), match.end())
        for match in re.finditer(r"artificial intelligence|records|reports", text)
    ]
    assert probes, "corpus entry must contain at least one probe occurrence"

    for start, end in probes:
        expected_sentence = _reference_sentence_span(text, start, end)
        actual_sentence = regulatory_monitor._occurrence_sentence_span(
            text, start, end
        )
        assert actual_sentence == expected_sentence, (text[start:end], start)

        sentence_start, sentence_end = actual_sentence
        assert index.clause_span(
            start, end, sentence_start, sentence_end
        ) == _reference_clause_span(text, start, end), (text[start:end], start)


def _large_citation_body(mentions: int) -> str:
    """Deterministic large body: filler sentences plus N citation sentences."""
    filler = "The Commission proposes to amend quarterly report deadlines. " * 125
    unit = filler + (
        "Members must file annual reports and Smith et al. discuss artificial "
        "intelligence in capital markets. "
    )
    return unit * mentions


def test_boundary_index_is_built_once_per_text_not_once_per_match():
    """Operation-count regression: the machine-independent half of the guard.

    The old code rescanned the document from offset 0 for every candidate
    match. Here the number of index builds must stay constant when the number
    of matches quadruples, which is the property that removes the quadratic
    term. Wall-clock alone would be a flaky proxy for it.
    """
    config = _load_config()
    builds_by_size = {}

    for mentions in (100, 400):
        text = _large_citation_body(mentions)
        regulatory_monitor._boundary_index.cache_clear()
        before = regulatory_monitor._BOUNDARY_INDEX_BUILDS
        regulatory_monitor.classify_regulatory_relevance(
            "Regulatory Notice 26-10", text, config, exclude_reference_only=True
        )
        regulatory_monitor.find_affected_controls_by_keywords(
            "Regulatory Notice 26-10", text, config, exclude_reference_only=True
        )
        builds_by_size[mentions] = (
            regulatory_monitor._BOUNDARY_INDEX_BUILDS - before
        )

    assert builds_by_size[100] == builds_by_size[400], builds_by_size
    assert builds_by_size[100] <= 4, (
        "one index per distinct text (title and body), reused across "
        "classification and control matching",
        builds_by_size,
    )


def test_large_document_classification_completes_in_seconds():
    """Wall-clock regression on a real-size body (~770k characters).

    Measured on this corpus: ~184s before the repair (classification ~101s,
    control mapping ~84s) and ~1.1s after. The ceiling is set an order of
    magnitude above the observed cost so a slow CI machine cannot make it
    flaky, while still failing loudly if the quadratic behaviour returns.
    """
    config = _load_config()
    text = _large_citation_body(100)
    assert len(text) > 750_000

    regulatory_monitor._boundary_index.cache_clear()
    started = time.perf_counter()
    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10", text, config, exclude_reference_only=True
    )
    controls = regulatory_monitor.find_affected_controls_by_keywords(
        "Regulatory Notice 26-10", text, config, exclude_reference_only=True
    )
    elapsed = time.perf_counter() - started

    assert elapsed < 20.0, f"classification took {elapsed:.1f}s on {len(text)} chars"
    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, "the large corpus is bibliographic; semantics must be unchanged"
    assert controls == []


# ===========================================================================
# Release review round 8 -- adversarial coverage for the seven findings
# ===========================================================================


# --- Finding 1: FINRA notice slug eligibility -------------------------------
#
# Live-verified on 2026 with HEAD requests against www.finra.org: each of these
# single-segment slugs answers 200. The previous eligibility rule accepted only
# ``NN-NNN`` and ``information-notice-YYYYMMDD``, so entire authoritative
# families were silently dropped from the crawl -- a completeness failure that
# looked like a clean run.
FINRA_LIVE_NOTICE_SLUGS = (
    "26-12",
    "26-1",
    "26-100",
    "trade-reporting-notice-20260114",
    "special-notice-031726",
    "information-notice-20260114",
    "regulatory-notice-20260114",
    "election-notice-031726",
)


@pytest.mark.parametrize("slug", FINRA_LIVE_NOTICE_SLUGS)
def test_finra_live_notice_family_slugs_are_eligible(slug):
    """Every live notice family shape must canonicalize, not be dropped."""
    expected = f"https://www.finra.org/rules-guidance/notices/{slug}"

    assert regulatory_monitor._canonical_finra_notice_url(
        f"/rules-guidance/notices/{slug}"
    ) == expected
    assert regulatory_monitor._canonical_finra_notice_url(expected) == expected
    # The legacy Drupal front-controller prefix is the same document.
    assert regulatory_monitor._canonical_finra_notice_url(
        f"https://www.finra.org/index.php/rules-guidance/notices/{slug}"
    ) == expected
    assert regulatory_monitor._canonical_finra_notice_url(
        f"/index.php/rules-guidance/notices/{slug}/"
    ) == expected


FINRA_REJECTED_NOTICE_URLS = (
    # Traversal, encoded traversal, and separator smuggling.
    "/rules-guidance/notices/../../etc/passwd",
    "/rules-guidance/notices/..%2f..%2fetc%2fpasswd",
    "/rules-guidance/notices/%2e%2e/26-12",
    "/rules-guidance/notices/26-12/../../admin",
    "/rules-guidance/notices/26-12%2f..",
    "/rules-guidance/notices/.",
    "/rules-guidance/notices/..",
    "/rules-guidance/notices/sub/26-12",
    "/rules-guidance/notices/26-12/attachment",
    r"/rules-guidance/notices/26-12\..\admin",
    # Lookalike and off-origin hosts.
    "https://finra.org.attacker.example/rules-guidance/notices/26-12",
    "https://www.finra.org.evil.test/rules-guidance/notices/26-12",
    "https://notfinra.org/rules-guidance/notices/26-12",
    "https://www-finra.org/rules-guidance/notices/26-12",
    "https://finra.org@attacker.example/rules-guidance/notices/26-12",
    "https://user:pass@www.finra.org/rules-guidance/notices/26-12",
    "https://www.finra.org:8443/rules-guidance/notices/26-12",
    # Non-https schemes are not aliases of the authoritative document.
    "http://www.finra.org/rules-guidance/notices/26-12",
    "ftp://www.finra.org/rules-guidance/notices/26-12",
    "javascript:alert('/rules-guidance/notices/26-12')",
    "data:text/html,/rules-guidance/notices/26-12",
    # Not the notices tree at all.
    "https://www.finra.org/rules-guidance/rulebooks/26-12",
    "https://www.finra.org/rules-guidance/notices",
    "https://www.finra.org/index.phpx/rules-guidance/notices/26-12",
    "https://www.finra.org/rules-guidance/notices/index.php/26-12",
    # Slug shapes that are not notices.
    "/rules-guidance/notices/notice",
    "/rules-guidance/notices/2026-annual-report",
    "/rules-guidance/notices/trade-reporting-notice-2026011",
    "/rules-guidance/notices/trade-reporting-notice-",
    "/rules-guidance/notices/-notice-20260114",
    "/rules-guidance/notices/trade_reporting_notice_20260114",
    "/rules-guidance/notices/26-",
    "/rules-guidance/notices/26-12345",
)


@pytest.mark.parametrize("candidate", FINRA_REJECTED_NOTICE_URLS)
def test_finra_unsafe_or_foreign_urls_are_rejected(candidate):
    """Broadening the family rule must not broaden what counts as authoritative."""
    assert regulatory_monitor._canonical_finra_notice_url(candidate) is None


def test_finra_notice_slug_safety_gate_is_syntactic_before_family_matching():
    """Traversal is refused by shape, not by an allow-list of known families."""
    assert regulatory_monitor._is_safe_finra_notice_slug("26-12")
    assert regulatory_monitor._is_safe_finra_notice_slug(
        "trade-reporting-notice-20260114"
    )
    for unsafe in (
        "..",
        ".",
        "26-12/..",
        "26-12%2e%2e",
        "26 12",
        "26-12\t",
        "26--12",
        "-26-12",
        "26-12-",
        "a" * 65,
        "",
    ):
        assert not regulatory_monitor._is_safe_finra_notice_slug(unsafe), unsafe


def test_finra_live_family_notices_are_crawled_classified_and_hashed(monkeypatch):
    """End-to-end: a live-shaped listing of every family yields operative items.

    Eligibility is only half the fix. The families must survive discovery,
    detail fetching, classification, and body hashing, otherwise "eligible"
    would still mean "silently absent from the baseline".
    """
    hrefs = [f"/rules-guidance/notices/{slug}" for slug in FINRA_LIVE_NOTICE_SLUGS]
    pages = {0: _finra_listing_page_html(hrefs)}
    config = _load_config()
    operative_body = (
        "Member firms must supervise artificial intelligence tools used to "
        "generate customer communications and must retain the resulting "
        "records in an electronic format for six years."
    )
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _finra_multipage_fetch(pages, detail_body=operative_body),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    items = regulatory_monitor.fetch_finra_notices(
        session=object(), config=config, limit=None, detail_fetch_limit=None
    )

    urls = {item.url for item in items}
    for slug in FINRA_LIVE_NOTICE_SLUGS:
        assert f"https://www.finra.org/rules-guidance/notices/{slug}" in urls

    hashes = set()
    for item in items:
        assert item.classification == regulatory_monitor.CLASSIFICATION_HIGH, item.url
        assert operative_body in item.content_text
        hashes.add(
            regulatory_monitor._schema_tagged_hash(
                regulatory_monitor._content_fingerprint(item)
            )
        )
    assert len(hashes) == len(items), "each notice hashes under its own identity"

    state: dict = {}
    regulatory_monitor.update_source_state(
        regulatory_monitor.SOURCE_KEY_FINRA, items, state
    )
    entries = state["sources"][regulatory_monitor.SOURCE_KEY_FINRA]["entries"]
    assert len(entries) == len(FINRA_LIVE_NOTICE_SLUGS)
    assert all(
        digest.startswith(regulatory_monitor.CONTENT_HASH_SCHEMA_PREFIX)
        for digest in entries.values()
    )


# --- Finding 2: FINRA listing/detail trust ----------------------------------


FINRA_DENIAL_LISTING_BODIES = {
    "pardon_our_interruption": (
        "<html><head><title>Pardon Our Interruption</title></head><body>"
        "<h1>Pardon Our Interruption</h1>"
        "<p>As you were browsing something about your browser made us think "
        "you were a bot.</p>"
    ),
    "sorry_blocked": (
        "<html><head><title>Access to this page has been denied</title></head>"
        "<body><h1>Sorry, you have been blocked</h1>"
        "<p>You are unable to access finra.org</p>"
    ),
    "just_a_moment": (
        "<html><head><title>Just a moment...</title></head><body>"
        "<h1>Just a moment...</h1>"
        "<p>Checking if the site connection is secure. Cloudflare Ray ID: "
        "8f2b1c9d0e7a4c11</p>"
    ),
    "bot_detection": (
        "<html><head><title>Bot detection</title></head><body>"
        "<h1>Additional security check is required</h1>"
        "<p>Please enable JavaScript and cookies to continue.</p>"
    ),
    "access_denied": (
        "<html><head><title>Access Denied</title></head><body>"
        "<h1>Access Denied</h1><p>You do not have permission to access this "
        "document on this server.</p>"
    ),
}


def _finra_denial_listing_html(kind: str) -> str:
    """A denial page that still renders real notice links in its navigation.

    This is the shape that made the anchor fallback dangerous: a blocked
    response is not an empty response, and its site chrome links to genuine
    notice URLs. Parsing it produced a plausible, short, *silently incomplete*
    crawl.
    """
    navigation = (
        "<nav class='site-nav'><ul>"
        "<li><a href='/rules-guidance/notices/26-01'>Regulatory Notice 26-01</a></li>"
        "<li><a href='/rules-guidance/notices/26-02'>Regulatory Notice 26-02</a></li>"
        "<li><a href='/rules-guidance/notices'>All Notices</a></li>"
        "</ul></nav>"
    )
    return FINRA_DENIAL_LISTING_BODIES[kind] + navigation + "</body></html>"


@pytest.mark.parametrize("kind", sorted(FINRA_DENIAL_LISTING_BODIES))
def test_finra_denial_listing_fails_closed_and_is_never_crawled(monkeypatch, kind):
    """A 200 denial listing must abort the run, not become a complete crawl."""
    config = _load_config()
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)
    requested: list[str] = []

    def fake_fetch_page(url, _session, max_retries=3):
        requested.append(url)
        return {
            "url": url,
            "status_code": 200,
            "content": _finra_denial_listing_html(kind),
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)

    with pytest.raises(regulatory_monitor.FinraListingError):
        regulatory_monitor.fetch_finra_notices(
            session=object(), config=config, limit=None, detail_fetch_limit=None
        )

    assert requested == [regulatory_monitor.FINRA_NOTICES_URL], (
        "no notice detail page may be fetched from a denial listing",
        requested,
    )


def test_finra_denial_listing_navigation_links_are_not_a_crawl():
    """The unit-level guarantee behind the fail-closed listing behaviour."""
    html = _finra_denial_listing_html("pardon_our_interruption")

    assert regulatory_monitor._finra_listing_denial_reason(html)
    # The links really are there -- the screen is what stops them being used.
    assert "26-01" in html


def test_finra_off_origin_two_hundred_listing_fails_closed(monkeypatch):
    """A 200 served from another origin is not the FINRA notices listing."""
    config = _load_config()
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    def fake_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 200,
            "content": _finra_listing_page_html(
                ["/rules-guidance/notices/26-01"]
            ),
            "final_url": "https://cdn.attacker.example/rules-guidance/notices",
            "was_redirected": True,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)

    with pytest.raises(regulatory_monitor.FinraListingError) as excinfo:
        regulatory_monitor.fetch_finra_notices(
            session=object(), config=config, limit=None, detail_fetch_limit=None
        )
    assert "listing" in str(excinfo.value).lower()


def test_finra_listing_url_validation_covers_request_and_response():
    """Both ends of the hop are validated, not just the one we control."""
    assert (
        regulatory_monitor._finra_listing_url_rejection_reason(
            regulatory_monitor.FINRA_NOTICES_URL, "requested"
        )
        is None
    )
    assert (
        regulatory_monitor._finra_listing_url_rejection_reason(
            f"{regulatory_monitor.FINRA_NOTICES_URL}?page=7", "requested"
        )
        is None
    )
    for bad in (
        "http://www.finra.org/rules-guidance/notices",
        "https://cdn.attacker.example/rules-guidance/notices",
        "https://www.finra.org/rules-guidance/notices/26-01",
        "https://www.finra.org.evil.test/rules-guidance/notices",
        "https://www.finra.org:8443/rules-guidance/notices",
    ):
        assert regulatory_monitor._finra_listing_url_rejection_reason(bad, "x"), bad


def test_finra_detail_denial_beside_unrelated_article_fails_closed():
    """A surviving unrelated article is not evidence the notice was served."""
    html = (
        "<html><head><title>Access Denied</title></head><body>"
        "<main><div class='field field--name-body'>"
        "Access Denied. You do not have permission to access this document on "
        "this server."
        "</div></main>"
        "<article class='node node--type-notice'>"
        "<div class='field field--name-body'>"
        + ("Unrelated surviving article about membership dues and fees. " * 80)
        + "</div></article>"
        "</body></html>"
    )

    text, _reason, rejected = regulatory_monitor._scan_finra_notice_body(html)

    assert rejected is True
    assert text == "", "denial chrome outranks a neighbouring article"
    assert regulatory_monitor._extract_finra_notice_required_text(html) == ""
    assert regulatory_monitor._extract_finra_notice_fallback_text(html) == ""


def test_finra_detail_login_chrome_below_a_real_article_still_returns_the_body():
    """The inverse must keep working: subordinate chrome does not fail closed.

    Failing closed on *any* rejected candidate would take FINRA monitoring down
    on ordinary pages whose low-confidence generic field is login chrome, so the
    rule is container authority, not mere presence.
    """
    body = (
        "Actual FINRA notice body. "
        + "The notice explains member supervisory procedures. " * 220
    )
    html = (
        "<html><body>"
        "<div class='field field--name-body'>Please log in to view this page.</div>"
        "<main><article class='node node--type-notice'>"
        f"<div class='field field--name-body'>{body}</div>"
        "</article></main></body></html>"
    )

    extracted = regulatory_monitor._extract_finra_notice_fallback_text(html)

    assert "Actual FINRA notice body." in extracted


def test_finra_detail_identity_mismatch_fails_closed():
    """A 200 rendering *a* notice is not proof it rendered *this* notice."""
    body = "Member firms must supervise artificial intelligence tools. " * 40
    html = (
        "<html><head>"
        "<link rel='canonical' href='https://www.finra.org/rules-guidance/notices/26-99'/>"
        "</head><body><main><article class='node node--type-notice'>"
        f"<div class='field field--name-body'>{body}</div>"
        "</article></main></body></html>"
    )
    requested = "https://www.finra.org/rules-guidance/notices/26-12"

    assert regulatory_monitor._finra_detail_identity_mismatch(html, requested)
    assert (
        regulatory_monitor._extract_finra_notice_required_text(
            html, expected_url=requested
        )
        == ""
    )
    # The same page served under its own URL is fine.
    assert regulatory_monitor._extract_finra_notice_required_text(
        html, expected_url="https://www.finra.org/rules-guidance/notices/26-99"
    )


def test_finra_detail_identity_declaring_a_foreign_url_fails_closed():
    """An identity that is not a supported notice URL is a mismatch too."""
    body = "Member firms must retain records electronically. " * 40
    html = (
        "<html><head>"
        "<meta property='og:url' content='https://cdn.attacker.example/26-12'/>"
        "</head><body><main><article class='node node--type-notice'>"
        f"<div class='field field--name-body'>{body}</div>"
        "</article></main></body></html>"
    )

    assert regulatory_monitor._finra_detail_identity_mismatch(
        html, "https://www.finra.org/rules-guidance/notices/26-12"
    )


def test_finra_detail_without_declared_identity_fails_closed():
    """Superseded contract, deliberately inverted.

    This test previously asserted that a page declaring nothing about itself
    "is not a mismatch", on the belief that live notices often omit
    ``rel=canonical``. That belief is wrong -- production
    ``https://www.finra.org/rules-guidance/notices/26-12`` serves
    ``<link rel="canonical" href="https://www.finra.org/rules-guidance/
    notices/26-12" />`` -- and the belief was load-bearing for a real defect:
    an unidentified body was stored, hashed, and baselined under the requested
    notice's key. Absence of identity is now a refusal.
    """
    body = "Member firms must retain records electronically. " * 40
    html = _finra_notice_page(body)

    reason = regulatory_monitor._finra_detail_identity_mismatch(
        html, "https://www.finra.org/rules-guidance/notices/26-12"
    )
    assert reason and "no canonical/og identity" in reason
    assert (
        regulatory_monitor._extract_finra_notice_required_text(
            html, expected_url="https://www.finra.org/rules-guidance/notices/26-12"
        )
        == ""
    )


def test_finra_detail_heading_identity_is_the_only_accepted_fallback():
    """The documented strong fallback: exactly one designation, and it matches.

    A page that declares no URL identity may still have named itself
    unambiguously. Exactly one distinct notice designation in title/og:title/h1
    that *is* the requested slug is accepted; a different one is a mismatch;
    more than one is ambiguous and fails closed.
    """
    body = "Member firms must retain records electronically. " * 40

    def page(heading):
        return (
            "<html><body><main><article class='node node--type-notice'>"
            f"<h1>{heading}</h1>"
            f"<div class='field field--name-body'>{body}</div>"
            "</article></main></body></html>"
        )

    requested = "https://www.finra.org/rules-guidance/notices/26-12"

    assert (
        regulatory_monitor._finra_detail_identity_mismatch(
            page("Regulatory Notice 26-12"), requested
        )
        is None
    )
    assert regulatory_monitor._extract_finra_notice_required_text(
        page("Regulatory Notice 26-12"), expected_url=requested
    )

    wrong = regulatory_monitor._finra_detail_identity_mismatch(
        page("Regulatory Notice 26-99"), requested
    )
    assert wrong and "26-99" in wrong

    ambiguous = regulatory_monitor._finra_detail_identity_mismatch(
        page("Regulatory Notice 26-12 supersedes Regulatory Notice 26-04"),
        requested,
    )
    assert ambiguous and "unambiguous notice designations" in ambiguous

    # The numbered-variant slug is comparable through the same rule.
    assert (
        regulatory_monitor._finra_detail_identity_mismatch(
            page("Notice to Members 88-81a"),
            "https://www.finra.org/rules-guidance/notices/88-81a",
        )
        is None
    )
    # 88-81 and 88-81a are different notices and must not satisfy each other.
    assert regulatory_monitor._finra_detail_identity_mismatch(
        page("Notice to Members 88-81"),
        "https://www.finra.org/rules-guidance/notices/88-81a",
    )


# --- Finding 3: Federal Register authoritative-text URL trust ---------------


FEDERAL_REGISTER_REJECTED_TEXT_URLS = {
    "http_scheme": "http://www.federalregister.gov/documents/full_text/text/a.txt",
    "no_scheme": "//www.federalregister.gov/documents/full_text/text/a.txt",
    "file_scheme": "file:///etc/passwd",
    "ipv4_literal": "https://127.0.0.1/documents/full_text/text/a.txt",
    "ipv4_public_literal": "https://93.184.216.34/documents/full_text/text/a.txt",
    "ipv4_metadata": "https://169.254.169.254/documents/full_text/text/a.txt",
    "ipv6_literal": "https://[::1]/documents/full_text/text/a.txt",
    "localhost": "https://localhost/documents/full_text/text/a.txt",
    "localhost_suffix": "https://api.localhost/documents/full_text/text/a.txt",
    "credentials": (
        "https://user:pass@www.federalregister.gov/documents/full_text/text/a.txt"
    ),
    "credential_at_trick": (
        "https://www.federalregister.gov@attacker.example/documents/full_text/"
        "text/a.txt"
    ),
    "alternate_port": (
        "https://www.federalregister.gov:8443/documents/full_text/text/a.txt"
    ),
    "lookalike_suffix": (
        "https://federalregister.gov.attacker.example/documents/full_text/text/a.txt"
    ),
    "lookalike_hyphen": (
        "https://federalregister-gov.attacker.example/documents/full_text/text/a.txt"
    ),
    "lookalike_subdomain_word": (
        "https://notfederalregister.gov/documents/full_text/text/a.txt"
    ),
    "fragment": (
        "https://www.federalregister.gov/documents/full_text/text/a.txt#frag"
    ),
    "traversal": (
        "https://www.federalregister.gov/documents/full_text/text/../../secret"
    ),
    "encoded_traversal": (
        "https://www.federalregister.gov/documents/full_text/text/%2e%2e/secret"
    ),
    "challenge_path": "https://www.federalregister.gov/cdn-cgi/challenge",
    "login_path": "https://www.federalregister.gov/login",
    "unrelated_path": "https://www.federalregister.gov/search",
    # Finding 5. The API documents endpoint is the *metadata* record, not the
    # document's authoritative text: the live endpoint answers
    # ``application/json`` describing the document, and its ``.txt`` sibling
    # answers HTTP 500 with a JSON error body. Classifying or hashing either
    # would baseline a summary as the source of record, so both shapes are off
    # the allow-list entirely and cost no request.
    "api_metadata_json": (
        "https://www.federalregister.gov/api/v1/documents/2026-17183.json"
    ),
    "api_metadata_txt": (
        "https://www.federalregister.gov/api/v1/documents/2026-17183.txt"
    ),
    "api_metadata_bare": (
        "https://www.federalregister.gov/api/v1/documents/2026-17183"
    ),
    # Finding 5. PDF is a binary rendering. ``Response.text`` decodes it into
    # mojibake that still passes the substantial-text screens and would be
    # hashed as if it were the document.
    "gpo_pdf": "https://www.gpo.gov/fdsys/pkg/FR-2026-01-14/pdf/2026-17183.pdf",
    "govinfo_pdf": (
        "https://www.govinfo.gov/content/pkg/FR-2026-01-14/pdf/2026-17183.pdf"
    ),
    "full_text_pdf_branch": (
        "https://www.federalregister.gov/documents/full_text/pdf/2026/01/14/"
        "2026-17183.pdf"
    ),
    # A permitted path shape that still names a binary/metadata payload.
    "text_branch_pdf_extension": (
        "https://www.federalregister.gov/documents/full_text/text/2026/01/14/"
        "2026-17183.pdf"
    ),
    "text_branch_json_extension": (
        "https://www.federalregister.gov/documents/full_text/text/2026/01/14/"
        "2026-17183.json"
    ),
    "gpo_mods_metadata": (
        "https://www.govinfo.gov/content/pkg/FR-2026-01-14/mods/2026-17183.xml"
    ),
    "empty": "",
    "whitespace_padded": (
        " https://www.federalregister.gov/documents/full_text/text/a.txt"
    ),
    "not_a_string": None,
}

FEDERAL_REGISTER_ACCEPTED_TEXT_URLS = (
    "https://www.federalregister.gov/documents/full_text/text/2026-17183.txt",
    "https://federalregister.gov/documents/full_text/xml/2026-17183.xml",
    "https://www.federalregister.gov/documents/full_text/text/2026/01/14/a.txt",
    "https://www.federalregister.gov/documents/full_text/html/2026/01/14/"
    "2026-17183.htm",
    "https://www.federalregister.gov/documents/2026/01/14/2026-17183.txt",
    "https://www.govinfo.gov/content/pkg/FR-2026-01-14/html/2026-17183.htm",
    "https://www.gpo.gov/fdsys/pkg/FR-2026-01-14/xml/2026-17183.xml",
    "https://www.gpo.gov/fdsys/pkg/FR-2026-01-14/text/2026-17183",
)


@pytest.mark.parametrize(
    "case", sorted(FEDERAL_REGISTER_REJECTED_TEXT_URLS), ids=str
)
def test_federal_register_text_url_allowlist_rejects_untrusted_urls(case):
    reason = regulatory_monitor._federal_register_text_url_rejection_reason(
        FEDERAL_REGISTER_REJECTED_TEXT_URLS[case]
    )
    assert reason, case


@pytest.mark.parametrize("url", FEDERAL_REGISTER_ACCEPTED_TEXT_URLS)
def test_federal_register_text_url_allowlist_accepts_authoritative_urls(url):
    assert (
        regulatory_monitor._federal_register_text_url_rejection_reason(url) is None
    ), url


@pytest.mark.parametrize(
    "case", sorted(FEDERAL_REGISTER_REJECTED_TEXT_URLS), ids=str
)
def test_federal_register_untrusted_text_url_is_never_requested(monkeypatch, case):
    """SSRF proof: the request must not be issued at all, and state must not move.

    Rejecting after the fetch would already have contacted the attacker-chosen
    host, which is the whole exposure. The assertion is therefore on the
    absence of a request, not on the absence of a result.
    """
    config = _load_config()
    document = _fr_document("2026-17183")
    document["raw_text_url"] = FEDERAL_REGISTER_REJECTED_TEXT_URLS[case]
    session = _PagedFederalRegisterSession(
        {1: {"count": 1, "total_pages": 1, "results": [document]}}
    )
    requested: list[str] = []

    def fake_fetch_page(url, _session, max_retries=3):
        requested.append(url)
        raise AssertionError(f"unexpected request to {url}")

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-18", config=config
        )

    assert requested == [], (case, requested)


def test_federal_register_valid_text_url_is_still_fetched(monkeypatch):
    """The allow-list must not break the authoritative read it protects."""
    config = _load_config()
    document = _fr_document("2026-17183")
    body = (
        "Authoritative body. Each member firm shall supervise every copilot "
        "deployment and shall retain the resulting records."
    )
    session, requested = _fr_body_session(document, body, monkeypatch)

    items = regulatory_monitor.fetch_federal_register_documents(
        session=session, since_date="2026-08-18", config=config
    )

    assert requested == [document["raw_text_url"]]
    assert items and items[0].content_text


def test_federal_register_final_url_is_revalidated_after_the_fetch(monkeypatch):
    """A redirect can land anywhere; the destination is checked, not assumed."""
    config = _load_config()
    document = _fr_document("2026-17183")
    session = _PagedFederalRegisterSession(
        {1: {"count": 1, "total_pages": 1, "results": [document]}}
    )

    def fake_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 200,
            "content": "<html><body><pre>Body text.</pre></body></html>",
            "final_url": "https://cdn.attacker.example/full_text/a.txt",
            "was_redirected": True,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-18", config=config
        )


FEDERAL_REGISTER_CHALLENGE_BODIES = {
    "pardon_our_interruption": (
        "Pardon Our Interruption. As you were browsing, something about your "
        "browser made us think you were a bot."
    ),
    "sorry_blocked": (
        "Sorry, you have been blocked. You are unable to access "
        "federalregister.gov."
    ),
    "just_a_moment": (
        "Just a moment... Checking if the site connection is secure. "
        "Cloudflare Ray ID: 8f2b1c9d0e7a4c11"
    ),
    "bot_detection": (
        "Bot detection triggered. Additional security check is required. "
        "Please enable JavaScript and cookies to continue."
    ),
    "attention_required": (
        "Attention Required! Cloudflare Ray ID: 91ab22cd33ef4455. Why have I "
        "been blocked?"
    ),
    "one_more_step": (
        "One more step. Please complete the security check to access "
        "federalregister.gov."
    ),
    "verifying_human": (
        "Verifying you are human. This may take a few seconds. Performance & "
        "security by Cloudflare."
    ),
    "request_unsuccessful": (
        "Request unsuccessful. Incapsula incident ID: 1234-567890123456789-123"
    ),
}


@pytest.mark.parametrize("case", sorted(FEDERAL_REGISTER_CHALLENGE_BODIES))
def test_federal_register_challenge_bodies_fail_closed_without_state_advance(
    monkeypatch, case
):
    """An interstitial is not a document; it must never become the baseline."""
    config = _load_config()
    document = _fr_document("2026-17183")
    session, _requested = _fr_body_session(
        document, FEDERAL_REGISTER_CHALLENGE_BODIES[case], monkeypatch
    )
    state: dict = {}

    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-18", config=config
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )

    assert state == {}


def test_federal_register_challenge_signatures_do_not_eat_valid_documents():
    """Counterexample: the words also occur innocently in real documents.

    An over-broad signature would fail the run closed on genuine text, which is
    the same outage the challenge screen is meant to prevent -- just triggered
    by the source being correct instead of blocked.
    """
    incidental = (
        "The Commission will pause for a moment to address comments received "
        "during the comment period. One commenter asked whether a bot may be "
        "used to prepare filings, and whether a firm is blocked from using "
        "automated tools. The Commission notes that a security check of each "
        "system is required at least annually. "
        + (
            "Each member firm shall supervise the deployment and shall retain "
            "the resulting records for six years. " * 40
        )
    )

    assert not regulatory_monitor._is_federal_register_non_document_text(incidental)


# --- Finding 4: citation forms ----------------------------------------------


@pytest.mark.parametrize(
    "text",
    (
        'The staff stated that "firms must retain records." Artificial '
        "intelligence is discussed in a recent working paper (Smith, Jones, "
        "and Lee, 2026).",
        "The order requires supervision of trading [emphasis added]. "
        "Artificial intelligence is described in a working paper (Smith, "
        "Jones, and Lee, 2026).",
        "Members must file annual reports. Smith, Jones, and Lee (2026) "
        "survey artificial intelligence adoption in capital markets.",
        "Members must file annual reports. Smith, Jones, Lee, and Chen (2026) "
        "survey artificial intelligence adoption in capital markets.",
        'The rule text says "members shall file reports.") Artificial '
        "intelligence adoption is uneven (Smith, Jones, and Lee, 2026).",
    ),
)
def test_multi_author_citations_after_closing_punctuation_are_not_operative(text):
    """A quoted/bracketed duty must not leak into the citation sentence."""
    config = _load_config()

    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing", text, config,
        exclude_reference_only=True,
    )

    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, text


@pytest.mark.parametrize(
    "text",
    (
        "Member firms must supervise artificial intelligence systems used for "
        "recommendations.",
        'The rule states that "firms must supervise artificial intelligence '
        'tools." Firms should review the guidance.',
        "Smith, Jones, and Lee (2026) surveyed the market, and member firms "
        "must supervise artificial intelligence tools used for "
        "recommendations.",
        "According to Smith, Jones, and Lee (2026), adoption is uneven, but "
        "each member firm shall retain artificial intelligence supervisory "
        "records.",
    ),
)
def test_multi_author_support_does_not_suppress_real_duties(text):
    """Precedence is preserved: an operative duty still outranks a citation."""
    config = _load_config()

    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing", text, config,
        exclude_reference_only=True,
    )

    assert classification == regulatory_monitor.CLASSIFICATION_HIGH, (text, reason)


def test_sentence_boundary_matches_closing_quotes_and_brackets():
    """The boundary must be recognised, and must still consume one character."""
    for text in (
        'firms must retain records." next sentence',
        "firms must retain records.) next sentence",
        "firms must retain records.] next sentence",
        "firms must retain records.\u201d next sentence",
    ):
        match = regulatory_monitor.SENTENCE_BOUNDARY_PATTERN.search(text)
        assert match, text
        assert match.end() == match.start() + 1, text
        assert text[match.start()] == "."

    # Decimals, section numbers, and URLs are still not sentence ends.
    for text in ("rule 17a-4(f)(3)", "12.5 percent", "https://www.finra.org/x"):
        for match in regulatory_monitor.SENTENCE_BOUNDARY_PATTERN.finditer(text):
            assert match.start() == len(text) - 1, (text, match.start())


def test_citation_name_series_accepts_comma_separated_authors():
    pattern = re.compile(regulatory_monitor._CITATION_PARENTHETICAL, re.IGNORECASE)
    for citation in (
        "(smith, 2026)",
        "(smith and lee, 2026)",
        "(smith, jones, and lee, 2026)",
        "(smith, jones, lee, and chen, 2026)",
        "(smith, jones & lee, 2026)",
        "(smith et al., 2026)",
    ):
        assert pattern.search(citation), citation

    # A date parenthetical is still not a citation.
    for non_citation in ("(september 2026)", "(effective 2027)", "(2026)"):
        assert not pattern.search(non_citation), non_citation


# --- Findings 5 and 6: recordkeeping qualifier and subject binding ----------


RECORDKEEPING_NON_HIGH_SENTENCES = (
    "Firms are not required to store records electronically.",
    "Firms are not required to maintain books and records in an electronic "
    "format.",
    "Records must be retained for six years, and electronic storage is an "
    "optional method.",
    "Records must be stored electronically, although the storage method is "
    "optional.",
    "Although the storage method is optional, records must be stored "
    "electronically.",
    "Records must be stored electronically, but paper copies are also "
    "permitted.",
    "Records must be stored electronically or alternatively retained in paper "
    "form.",
    "Records may be retained electronically.",
    "Records must be retained either electronically or in paper form.",
    "Firms need not store records electronically.",
)

RECORDKEEPING_HIGH_SENTENCES = (
    "Books and records must be stored electronically, while employee "
    "handbooks may be printed on paper.",
    "Books and records must be stored electronically, while marketing "
    "brochures may be distributed on paper.",
    "Books and records must be stored electronically, while training manuals "
    "may be issued in printed form.",
    "Member firms must maintain books and records in an electronic format.",
    "Records must be maintained electronically rather than in paper form.",
    "Records may not be retained on paper and must be maintained "
    "electronically.",
    "Records that may contain customer information must be retained "
    "electronically.",
    "Records must be stored electronically, and firms must not alter them.",
    "Records must be preserved in a machine-readable format for six years.",
)


@pytest.mark.parametrize("sentence", RECORDKEEPING_NON_HIGH_SENTENCES)
def test_qualified_storage_language_is_not_an_electronic_mandate(sentence):
    """Qualifiers bind the storage predicate even when outside the match span."""
    assert not regulatory_monitor._has_electronic_recordkeeping_obligation(sentence)


@pytest.mark.parametrize("sentence", RECORDKEEPING_HIGH_SENTENCES)
def test_mandatory_storage_language_remains_an_electronic_mandate(sentence):
    """A permission granted to a different subject cannot cancel this duty."""
    assert regulatory_monitor._has_electronic_recordkeeping_obligation(sentence)


@pytest.mark.parametrize("sentence", RECORDKEEPING_HIGH_SENTENCES)
def test_mandatory_storage_language_classifies_high(sentence):
    config = _load_config()

    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10", sentence, config, exclude_reference_only=True
    )

    assert classification in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }, sentence


def test_paper_permission_for_a_different_subject_does_not_travel_backwards():
    """The exact reviewer counterexample, at unit level."""
    sentence = (
        "Books and records must be stored electronically, while employee "
        "handbooks may be printed on paper."
    )
    clause = re.sub(r"\s+", " ", sentence.rstrip(".")).strip()
    match = None
    for pattern in regulatory_monitor.ELECTRONIC_RECORDKEEPING_PATTERNS:
        match = pattern.search(clause)
        if match:
            break
    assert match is not None

    local = regulatory_monitor._local_storage_clause(
        clause, match.start(), match.end()
    )

    assert "employee handbooks" not in local
    assert regulatory_monitor._segment_opens_different_subject(
        "while employee handbooks may be printed on paper"
    )
    assert not regulatory_monitor._segment_opens_different_subject(
        "although the storage method is optional"
    )
    assert not regulatory_monitor._segment_opens_different_subject(
        "but paper copies are also permitted"
    )
    assert not regulatory_monitor._segment_opens_different_subject(
        "or alternatively retained in paper form"
    )


def test_unbound_negation_does_not_defeat_a_storage_mandate():
    """"must not" bound to something else is not a negated storage duty."""
    masked = regulatory_monitor._mask_unbound_negations(
        "records must be stored electronically and firms must not alter them"
    )
    assert "must not" not in masked

    bound = regulatory_monitor._mask_unbound_negations(
        "firms are not required to store records electronically"
    )
    assert "not required" in bound


# --- Finding 7: many mentions in one long sentence --------------------------


def _single_sentence_mention_corpus(mentions: int) -> str:
    """One ~770k-character sentence carrying ``mentions`` AI mentions.

    Deliberately free of clause punctuation and sentence terminators, so every
    mention resolves to the *same* full-document span. Boundary indexing alone
    does not help here: the index is built once, but the span was re-sliced and
    re-scanned once per mention, which is the residual O(document x mentions)
    term the reviewer found.
    """
    filler = "the commission discusses market structure considerations at length "
    parts = []
    for _ in range(mentions):
        parts.append(filler * 180)
        parts.append("artificial intelligence adoption is described at length ")
    return (
        "the commission notes that "
        + "".join(parts)
        + "as summarized in a recent working paper on the topic."
    )


def test_many_mentions_in_one_long_sentence_scale_near_linearly():
    """Operation-count regression that a fast machine cannot mask.

    Measured on this corpus (775,503 characters, one sentence, 64 mentions):
    56.6s and 154,612,736 scanned characters without span memoisation versus
    0.9s and 3,101,904 scanned characters with it. The character counter is the
    machine-independent evidence; the wall-clock ceiling is the user-visible
    contract.
    """
    config = _load_config()
    text = _single_sentence_mention_corpus(64)
    assert len(text) > 750_000
    assert len(re.findall(r"[.;!?](?=\s|$)", text)) == 1, "must be one sentence"
    assert len(re.findall("artificial intelligence", text)) == 64

    regulatory_monitor._boundary_index.cache_clear()
    regulatory_monitor._SPAN_MARKER_SCANS = 0
    regulatory_monitor._SPAN_MARKER_CHARS = 0
    builds_before = regulatory_monitor._BOUNDARY_INDEX_BUILDS

    started = time.perf_counter()
    classification, _reason = regulatory_monitor.classify_regulatory_relevance(
        "Self-Regulatory Organizations; Notice of Filing",
        text,
        config,
        exclude_reference_only=True,
    )
    controls = regulatory_monitor.find_affected_controls_by_keywords(
        "Self-Regulatory Organizations; Notice of Filing",
        text,
        config,
        exclude_reference_only=True,
    )
    elapsed = time.perf_counter() - started

    assert elapsed < 10.0, (
        f"classification+control mapping took {elapsed:.1f}s for 64 mentions "
        f"in one {len(text)}-character sentence"
    )
    assert regulatory_monitor._BOUNDARY_INDEX_BUILDS - builds_before <= 4
    assert regulatory_monitor._SPAN_MARKER_CHARS < 8 * len(text), (
        "span scanning must not repeat per mention",
        regulatory_monitor._SPAN_MARKER_CHARS,
        len(text),
    )
    assert regulatory_monitor._SPAN_MARKER_SCANS <= 16, (
        "distinct spans, not mentions, bound the number of marker scans",
        regulatory_monitor._SPAN_MARKER_SCANS,
    )
    assert classification not in {
        regulatory_monitor.CLASSIFICATION_HIGH,
        regulatory_monitor.CLASSIFICATION_CRITICAL,
    }
    assert controls == []


def test_span_marker_cost_does_not_grow_with_mention_count():
    """The defining property: fixed input, more mentions, same scanning cost."""
    costs = {}
    for mentions in (16, 64):
        text = _single_sentence_mention_corpus(64)
        regulatory_monitor._boundary_index.cache_clear()
        regulatory_monitor._SPAN_MARKER_CHARS = 0
        occurrences = list(re.finditer("artificial intelligence", text))[:mentions]
        for occurrence in occurrences:
            regulatory_monitor._is_reference_only_occurrence(
                text, occurrence.start(), occurrence.end()
            )
        costs[mentions] = regulatory_monitor._SPAN_MARKER_CHARS

    assert costs[16] == costs[64], costs


def test_span_memoisation_preserves_per_occurrence_verdicts():
    """Caching must not change a single verdict.

    The cache is keyed by span, so a stale or over-shared entry would silently
    reclassify mentions. Every occurrence is compared against a scan of exactly
    the same span computed without the cache.
    """
    text = (
        "Members must file annual reports and Smith, Jones, and Lee (2026) "
        "discuss artificial intelligence in capital markets. Each member firm "
        "shall supervise artificial intelligence tools used for "
        "recommendations. Artificial intelligence is surveyed in a recent "
        "working paper. According to Smith, Jones, and Lee (2026), artificial "
        "intelligence adoption is uneven."
    )
    regulatory_monitor._boundary_index.cache_clear()

    for occurrence in re.finditer(
        "artificial intelligence", text, re.IGNORECASE
    ):
        start, end = occurrence.span()
        index = regulatory_monitor._boundary_index(text)
        clause_start, clause_end = regulatory_monitor._occurrence_clause_span(
            text, start, end
        )
        sentence_start, sentence_end = (
            regulatory_monitor._occurrence_sentence_span(text, start, end)
        )
        clause = text[clause_start:clause_end]
        sentence = text[sentence_start:sentence_end]

        if regulatory_monitor.OPERATIVE_LANGUAGE_PATTERN.search(clause):
            expected = False
        elif regulatory_monitor.REFERENCE_ONLY_PATTERN.search(clause):
            expected = True
        elif regulatory_monitor.OPERATIVE_LANGUAGE_PATTERN.search(sentence):
            expected = False
        else:
            expected = bool(
                regulatory_monitor.REFERENCE_ONLY_PATTERN.search(sentence)
            )

        assert (
            regulatory_monitor._is_reference_only_occurrence(text, start, end)
            is expected
        ), (text[start:end], start)
        assert index is regulatory_monitor._boundary_index(text)


def test_legitimate_finra_listing_is_not_flagged_as_a_denial():
    """Counterexample: the denial screen must not close the source it guards.

    A screen that fires on real listings would be indistinguishable from the
    outage it prevents, so the passing case is asserted explicitly rather than
    left implicit in the crawl tests.
    """
    html = _finra_listing_page_html(
        [f"/rules-guidance/notices/26-{n:02d}" for n in range(1, 26)],
        last_page=3,
    )

    assert regulatory_monitor._finra_listing_denial_reason(html) is None


def test_finra_notice_body_mentioning_interstitial_words_survives():
    """Incidental wording is not a challenge signature.

    "just a moment", "bot", and "blocked" all occur in ordinary regulatory
    prose. Only branded/unambiguous signatures, or ambiguous ones in the lead
    region of a short page, may reject a body.
    """
    body = (
        "Members asked the staff to pause for a moment on the question of "
        "whether a bot may submit orders and whether an account can be "
        "blocked. "
        + (
            "Member firms must supervise every automated tool used to prepare "
            "customer communications and must retain the resulting records. "
            * 40
        )
    )

    text, reason, rejected = regulatory_monitor._scan_finra_notice_body(
        _finra_notice_page(body)
    )

    assert reason is None
    assert rejected is False
    assert "Member firms must supervise every automated tool" in text


# --- Release review 9: adversarial regression suite --------------------------
#
# One block per finding. Every case here is shaped from what the live sources
# actually serve, verified during this revision:
#
#   * The FINRA notices listing is 92 pages and publishes 3,575 distinct notice
#     slugs. Exactly one of them carries a letter suffix (``88-81a``), and the
#     longest digit run after ``NN-`` is 3.
#   * Every listing page -- including ``?page=7`` -- serves
#     ``<link rel="canonical" href="https://www.finra.org/rules-guidance/notices" />``
#     with no ``page`` component, and does *not* redirect.
#   * ``https://www.finra.org/rules-guidance/notices/26-12`` serves
#     ``<link rel="canonical" href=".../notices/26-12" />``.
#   * ``https://www.federalregister.gov/api/v1/documents/<n>.json`` answers 200
#     ``application/json`` with a metadata record, and the ``.txt`` shape of
#     that same API answers **HTTP 500** with a JSON error body -- it is not an
#     authoritative text endpoint at all.


# --- Finding 1: bounded numbered-variant slugs ------------------------------


FINRA_NUMBERED_VARIANT_ACCEPTED = (
    # The only letter-suffixed slug in the entire live listing.
    "88-81a",
    # Companion notice, plus the plain shapes that dominate the listing.
    "88-81",
    "26-12",
    "97-1",
    "11-123",
)

FINRA_NUMBERED_VARIANT_REJECTED = (
    # Two letters exceeds the bound proven by the listing scan.
    "88-81ab",
    # Digit run longer than any live slug.
    "88-81234",
    # Lookalike suffixes: a real notice never publishes these.
    "88-81a-comments",
    "88-81a1",
    "88-81-a",
    "88-a",
    "888-81a",
    "8-81a",
    # Traversal and encoded traversal, with and without the suffix.
    "..",
    "%2e%2e",
    "88-81a%2f..",
    "88-81a/..",
    "../88-81a",
    "88-81a.",
)


@pytest.mark.parametrize("slug", FINRA_NUMBERED_VARIANT_ACCEPTED)
def test_finra_numbered_variant_slugs_accepted(slug):
    assert regulatory_monitor._is_safe_finra_notice_slug(slug), slug
    assert (
        regulatory_monitor._canonical_finra_notice_url(
            f"https://www.finra.org/rules-guidance/notices/{slug}"
        )
        == f"https://www.finra.org/rules-guidance/notices/{slug}"
    )


@pytest.mark.parametrize("slug", FINRA_NUMBERED_VARIANT_REJECTED)
def test_finra_numbered_variant_lookalikes_rejected(slug):
    assert not regulatory_monitor._is_safe_finra_notice_slug(slug), slug
    assert (
        regulatory_monitor._canonical_finra_notice_url(
            f"https://www.finra.org/rules-guidance/notices/{slug}"
        )
        is None
    ), slug


def test_finra_numbered_variant_suffix_bound_is_one_letter():
    """The bound is a fact about the source, not a taste.

    A 92-page crawl of the live listing enumerated 3,575 notice slugs; exactly
    one (``88-81a``) carries a letter suffix and it is a single letter. Widening
    the bound would admit lookalikes with no live counterpart, so the constant
    is asserted rather than left as a comment.
    """
    assert regulatory_monitor.FINRA_NOTICE_NUMBERED_SUFFIX_MAX_LETTERS == 1


def test_finra_numbered_variant_yields_its_own_document_id():
    """``88-81a`` must key on itself, not collapse onto ``88-81``.

    The id is the change-detection key. If the variant fell back to a
    URL-derived id, or worse resolved to ``FINRA 88-81``, the two notices --
    both of which are live -- would share or swap baselines.
    """

    def document_id(url):
        match = regulatory_monitor.FINRA_NOTICE_ID_PATTERN.search(url)
        return f"FINRA {match.group(1)}-{match.group(2)}" if match else url

    variant = document_id("https://www.finra.org/rules-guidance/notices/88-81a")
    base = document_id("https://www.finra.org/rules-guidance/notices/88-81")
    assert variant == "FINRA 88-81a"
    assert base == "FINRA 88-81"
    assert variant != base


def test_finra_slug_case_and_whitespace_are_normalised_not_slug_gate_bypasses():
    """Two layers, deliberately different, and both must be understood.

    ``_is_safe_finra_notice_slug`` is strict: it accepts only the exact
    lowercase published token, so uppercase and trailing whitespace fail it.
    ``_canonical_finra_notice_url`` normalises a *URL* first -- unquoting and
    case-folding the path -- and then applies that same strict gate to the
    normalised slug. The result is a fixed canonical string, so a variant-cased
    href cannot produce a second key for the same notice; what it cannot do is
    smuggle a shape the slug gate rejects.
    """
    assert not regulatory_monitor._is_safe_finra_notice_slug("88-81A")
    assert not regulatory_monitor._is_safe_finra_notice_slug("88-81a ")
    canonical = "https://www.finra.org/rules-guidance/notices/88-81a"
    for variant in ("88-81A", "88-81a ", "88-81a"):
        assert (
            regulatory_monitor._canonical_finra_notice_url(
                f"https://www.finra.org/rules-guidance/notices/{variant}"
            )
            == canonical
        ), variant
    # Normalisation is not permission: a rejected shape stays rejected.
    for variant in ("88-81AB", "88-81A-COMMENTS"):
        assert (
            regulatory_monitor._canonical_finra_notice_url(
                f"https://www.finra.org/rules-guidance/notices/{variant}"
            )
            is None
        ), variant


# --- Finding 2: listing pagination and page identity ------------------------


FINRA_MARKET_NEWS_ARTICLE = """
<html><head>
  <link rel="canonical" href="https://www.finra.org/media-center/newsreleases/ai-supervision"/>
</head><body><main>
  <article class="node node--type-news">
    <h1>FINRA highlights supervisory expectations</h1>
    <p>The release discusses
      <a href="/rules-guidance/notices/26-12">Regulatory Notice 26-12</a> and
      <a href="/rules-guidance/notices/26-13">Regulatory Notice 26-13</a>.</p>
  </article>
</main></body></html>
"""


def test_finra_market_news_article_is_never_a_listing():
    """The exact shape the removed all-anchor fallback promoted to a crawl.

    This page is same-origin, HTTP 200, carries no denial vocabulary, and links
    to two *real* notices from ordinary prose. Under the fallback it produced a
    complete two-notice "listing", and the run looked clean while 3,573 notices
    silently ceased to exist. Both gates must now reject it.
    """
    assert regulatory_monitor._extract_finra_notice_links(
        FINRA_MARKET_NEWS_ARTICLE
    ) == []
    reason = regulatory_monitor._finra_listing_identity_rejection_reason(
        FINRA_MARKET_NEWS_ARTICLE, 0
    )
    assert reason and "not the FINRA notices listing" in reason


def test_finra_listing_without_identity_or_rows_fails_closed():
    """Neither self-declared identity nor a recognised row: refuse."""
    page = "<html><body><a href='/rules-guidance/notices/26-12'>26-12</a></body></html>"
    assert regulatory_monitor._extract_finra_notice_links(page) == []
    reason = regulatory_monitor._finra_listing_identity_rejection_reason(page, 0)
    assert reason and "no recognised notice rows" in reason


def test_finra_listing_rows_without_identity_are_accepted():
    """Recognised containers are the documented alternative to declared identity."""
    page = (
        "<html><body><main><table class='notices-table'><tbody><tr>"
        "<td><a href='/rules-guidance/notices/26-12'>Regulatory Notice 26-12</a></td>"
        "</tr></tbody></table></main></body></html>"
    )
    assert regulatory_monitor._finra_listing_identity_rejection_reason(page, 0) is None
    assert len(regulatory_monitor._extract_finra_notice_links(page)) == 1


@pytest.mark.parametrize(
    "requested_page,final_url,should_reject",
    [
        # The live source: page 7 answers as page 7 and does not redirect.
        (7, "https://www.finra.org/rules-guidance/notices?page=7", False),
        # The finding's case: page 7 reported as page 1.
        (7, "https://www.finra.org/rules-guidance/notices?page=1", True),
        # Page 7 clamped to the bare listing (page 0).
        (7, "https://www.finra.org/rules-guidance/notices", True),
        (7, "https://www.finra.org/rules-guidance/notices?page=0", True),
        # Page 0 is the bare listing; an explicit page=0 is the same page.
        (0, "https://www.finra.org/rules-guidance/notices", False),
        (0, "https://www.finra.org/rules-guidance/notices?page=0", False),
        # ...but page 0 must not be satisfied by any other page.
        (0, "https://www.finra.org/rules-guidance/notices?page=1", True),
        # A non-numeric page declaration is not the requested page.
        (7, "https://www.finra.org/rules-guidance/notices?page=seven", True),
        # Off-path and off-origin remain rejected.
        (7, "https://www.finra.org/rules-guidance/rules?page=7", True),
        (7, "https://finra.org.attacker.test/rules-guidance/notices?page=7", True),
    ],
)
def test_finra_listing_page_identity_is_exact(requested_page, final_url, should_reject):
    reason = regulatory_monitor._finra_listing_url_rejection_reason(
        final_url, "listing response", expected_page=requested_page
    )
    assert bool(reason) is should_reject, (requested_page, final_url, reason)


def test_finra_listing_page_seven_reported_as_page_one_fails_the_crawl(monkeypatch):
    """End to end: a clamped page must not be recorded as fetched.

    Page 0's pager declares a last page of 7. The stub answers the page-7
    request from page 1 -- a real edge-clamp behaviour. Before, the path check
    passed, page 1's notices were re-collected, and the crawl was baselined as
    covering all eight pages.
    """
    pages = {
        index: _finra_listing_page_html(
            [f"/rules-guidance/notices/26-{index:02d}"],
            last_page=7,
        )
        for index in range(8)
    }
    prefix = f"{regulatory_monitor.FINRA_NOTICES_URL}?page="

    def fake_fetch_page(url, _session, max_retries=3):
        if url.startswith(prefix) and url[len(prefix):] == "7":
            # The clamp: page 7 is answered from page 1.
            return {
                "url": url,
                "status_code": 200,
                "content": pages[1],
                "final_url": f"{prefix}1",
                "was_redirected": True,
                "error": None,
            }
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            content, final = pages[0], url
        elif url.startswith(prefix):
            content, final = pages[int(url[len(prefix):])], url
        else:
            content, final = _finra_notice_page("Neutral supervisory guidance."), url
        return {
            "url": url,
            "status_code": 200,
            "content": _with_finra_canonical(content, url),
            "final_url": final,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.FinraListingError, match="page 7"):
        items = regulatory_monitor.fetch_finra_notices(
            session=object(), config=_load_config()
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FINRA, items, state
        )
    assert state == {}


def test_finra_listing_declaring_a_different_page_fails_closed():
    """A body that names itself as another page is rejected even on a good URL."""
    page = (
        "<html><head>"
        '<link rel="canonical" href="https://www.finra.org/rules-guidance/notices?page=1"/>'
        "</head><body><main><table class='notices-table'><tbody><tr>"
        "<td><a href='/rules-guidance/notices/26-12'>Regulatory Notice 26-12</a></td>"
        "</tr></tbody></table></main></body></html>"
    )
    reason = regulatory_monitor._finra_listing_identity_rejection_reason(page, 7)
    assert reason and "declares itself as page 1" in reason
    # The live shape -- a page-less canonical -- stays acceptable on every page.
    live = page.replace("/rules-guidance/notices?page=1", "/rules-guidance/notices")
    assert regulatory_monitor._finra_listing_identity_rejection_reason(live, 7) is None


# --- Finding 3: detail identity ---------------------------------------------


def test_finra_detail_redirect_to_another_notice_fails_closed(monkeypatch):
    """26-12 must never be baselined from 26-99's body.

    The redirect target is a perfectly valid notice URL, which is exactly why
    the old "is it *a* notice URL" check passed it. Two independent gates now
    catch it: the final URL is not the requested notice, and the served page
    declares itself as 26-99.
    """
    requested = "https://www.finra.org/rules-guidance/notices/26-12"
    other = "https://www.finra.org/rules-guidance/notices/26-99"

    assert regulatory_monitor._finra_detail_url_rejection_reason(other) is None, (
        "precondition: the redirect target is a valid notice URL, so only an "
        "identity-bound check can reject it"
    )
    reason = regulatory_monitor._finra_detail_url_rejection_reason(
        other, expected_url=requested
    )
    assert reason and "26-99" in reason and "26-12" in reason

    listing = _finra_listing_html([("/rules-guidance/notices/26-12", "Notice 26-12")])
    foreign_body = (
        "<html><head>"
        f'<link rel="canonical" href="{other}"/>'
        "</head><body><main><article class='node node--type-notice'>"
        "<div class='field field--name-body'>"
        + ("Members must supervise artificial intelligence tools. " * 40)
        + "</div></article></main></body></html>"
    )

    def fake_fetch_page(url, _session, max_retries=3):
        if url == regulatory_monitor.FINRA_NOTICES_URL:
            return {
                "url": url,
                "status_code": 200,
                "content": listing,
                "final_url": url,
                "was_redirected": False,
                "error": None,
            }
        return {
            "url": url,
            "status_code": 200,
            "content": foreign_body,
            "final_url": other,
            "was_redirected": True,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_finra_notices(
            session=object(), config=_load_config(), limit=1
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FINRA, items, state
        )

    assert state == {}, "another notice's body must never be stored under 26-12"


def test_finra_detail_body_of_another_notice_is_never_stored_under_the_key():
    """Same host, same URL, no redirect -- only the declared identity differs.

    This is the cache-poisoning shape: the transport is blameless, the body is
    a genuine notice, and it is simply the wrong one.
    """
    body = "Members must supervise artificial intelligence tools. " * 40
    html = (
        "<html><head>"
        '<link rel="canonical" href="https://www.finra.org/rules-guidance/notices/26-99"/>'
        "</head><body><main><article class='node node--type-notice'>"
        f"<div class='field field--name-body'>{body}</div>"
        "</article></main></body></html>"
    )
    assert (
        regulatory_monitor._extract_finra_notice_required_text(
            html, expected_url="https://www.finra.org/rules-guidance/notices/26-12"
        )
        == ""
    )
    assert regulatory_monitor._extract_finra_notice_required_text(
        html, expected_url="https://www.finra.org/rules-guidance/notices/26-99"
    )


# --- Finding 4: branded/interstitial denial cannot be padded away -----------


REVIEW9_PADDED_DENIAL_BODIES = {
    # Each body leads with an unmistakable denial and is then padded with
    # authoritative-looking vocabulary far past any structural threshold.
    "access_denied": "Access Denied. You do not have permission to access this page. ",
    "cloudflare_ray": (
        "Attention Required! Cloudflare Ray ID: 8f21ab99c0e1. Please enable "
        "JavaScript and cookies to continue. "
    ),
    "just_a_moment": "Just a moment... Checking your browser before accessing. ",
    "verify_human": "Please verify you are a human to continue. ",
    "request_blocked": "Request blocked. Your request has been blocked by our security service. ",
    "captcha": "Complete the CAPTCHA to continue to the requested page. ",
}

REVIEW9_FINRA_PADDING = (
    "Suggested Routing Compliance Legal Operations Senior Management. "
    "Key Topics Artificial Intelligence Supervision Recordkeeping. "
    "Notice Type Guidance. Referenced Rules FINRA Rule 3110, FINRA Rule 4511. "
    "SUMMARY Member firms must supervise the use of artificial intelligence. "
) * 40

REVIEW9_FR_PADDING = (
    "[Federal Register Volume 91, Number 155] AGENCY: Securities and Exchange "
    "Commission. ACTION: Final rule. SUMMARY: The Commission is adopting rules "
    "under FINRA Rule 3110 governing recordkeeping. DATES: Effective October 1. "
) * 40


@pytest.mark.parametrize("fixture_name", sorted(REVIEW9_PADDED_DENIAL_BODIES))
def test_padded_denial_is_rejected_by_both_screens(fixture_name):
    """Padding a denial with authoritative tokens must not launder it.

    The exception for genuinely incidental wording is *ordered*: an
    authoritative document publishes its citation block before it ever
    discusses denials. A challenge page can only append boilerplate after its
    denial, so the prefix stays empty and no amount of padding helps.
    """
    denial = REVIEW9_PADDED_DENIAL_BODIES[fixture_name]
    for padding in (REVIEW9_FINRA_PADDING, REVIEW9_FR_PADDING):
        body = denial + padding
        assert regulatory_monitor._is_finra_non_notice_page_text(body), (
            fixture_name,
            "finra",
        )
        assert regulatory_monitor._is_federal_register_non_document_text(body), (
            fixture_name,
            "fr",
        )


@pytest.mark.parametrize("fixture_name", sorted(REVIEW9_PADDED_DENIAL_BODIES))
def test_padded_denial_fails_the_finra_pipeline_without_state_advance(
    fixture_name, monkeypatch
):
    body = REVIEW9_PADDED_DENIAL_BODIES[fixture_name] + REVIEW9_FINRA_PADDING
    listing = _finra_listing_html([("/rules-guidance/notices/26-12", "Notice 26-12")])
    detail = (
        "<html><head>"
        '<link rel="canonical" href="https://www.finra.org/rules-guidance/notices/26-12"/>'
        "</head><body><main><article class='node node--type-notice'>"
        f"<div class='field field--name-body'>{body}</div>"
        "</article></main></body></html>"
    )

    def fake_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 200,
            "content": listing if url == regulatory_monitor.FINRA_NOTICES_URL else detail,
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_finra_notices(
            session=object(), config=_load_config(), limit=1
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FINRA, items, state
        )
    assert state == {}, fixture_name


@pytest.mark.parametrize("fixture_name", sorted(REVIEW9_PADDED_DENIAL_BODIES))
def test_padded_denial_fails_the_federal_register_pipeline_without_state_advance(
    fixture_name, monkeypatch
):
    body = REVIEW9_PADDED_DENIAL_BODIES[fixture_name] + REVIEW9_FR_PADDING
    session = _PagedFederalRegisterSession({1: _federal_register_source_text_page()})
    monkeypatch.setattr(
        regulatory_monitor, "fetch_page", _federal_register_text_fetch(body)
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-13", config=_load_config()
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )
    assert state == {}, fixture_name


def test_incidental_denial_wording_after_self_identification_still_survives():
    """The structural exception is narrow, not absent.

    A real rulemaking that *regulates* access-denial events names them in its
    SUMMARY -- but only after publishing its citation block. That ordering is
    the discriminator, and it must keep working or the cost guard is lost.
    """
    body = (
        "[Federal Register Volume 91, Number 155] AGENCY: Securities and "
        "Exchange Commission. ACTION: Final rule. SUMMARY: The Commission is "
        "adopting rules addressing access denied events, captcha deployment, "
        "and verify you are a human challenges on member portals. "
    ) + ("Supplementary information continues at length. " * 200)
    assert not regulatory_monitor._is_federal_register_non_document_text(body)


# --- Finding 5: Federal Register authoritative-text allowlist ---------------


def test_federal_register_api_json_is_rejected_without_any_fetch(monkeypatch):
    """The live metadata endpoint must be refused before the network is touched.

    ``/api/v1/documents/<n>.json`` answers 200 ``application/json`` with an
    abstract-and-links record. Decoded, it reads like prose and would have been
    classified and hashed as the source of record. It is rejected on the URL
    alone, so no request is issued and no state advances.
    """
    fetches: list = []

    def recording_fetch(url, _session, max_retries=3):
        fetches.append(url)
        raise AssertionError(f"no fetch may be issued for {url}")

    document = _federal_register_source_text_page()
    document["results"][0]["raw_text_url"] = (
        "https://www.federalregister.gov/api/v1/documents/2026-16471.json"
    )
    session = _PagedFederalRegisterSession({1: document})
    monkeypatch.setattr(regulatory_monitor, "fetch_page", recording_fetch)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-13", config=_load_config()
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )

    assert fetches == [], "a disallowed source-text URL must never be requested"
    assert state == {}


@pytest.mark.parametrize(
    "raw_text_url",
    [
        # Live API shapes -- metadata, not authoritative text.
        "https://www.federalregister.gov/api/v1/documents/2026-16471.json",
        "https://www.federalregister.gov/api/v1/documents/2026-16471.txt",
        "https://www.federalregister.gov/api/v1/documents/2026-16471",
        # PDF renderings -- not parseable authoritative text.
        "https://www.federalregister.gov/documents/full_text/pdf/2026/08/13/2026-16471.pdf",
        "https://www.govinfo.gov/content/pkg/FR-2026-08-13/pdf/2026-16471.pdf",
        "https://www.federalregister.gov/documents/full_text/text/2026/08/13/2026-16471.pdf",
        # GPO metadata rendering.
        "https://www.govinfo.gov/content/pkg/FR-2026-08-13/mods/2026-16471.xml",
    ],
)
def test_federal_register_disallowed_text_urls_are_rejected(raw_text_url):
    assert regulatory_monitor._federal_register_text_url_rejection_reason(
        raw_text_url, "2026-16471"
    ), raw_text_url


@pytest.mark.parametrize(
    "raw_text_url",
    [
        "https://www.federalregister.gov/documents/full_text/text/2026/08/13/2026-16471.txt",
        "https://www.federalregister.gov/documents/full_text/html/2026/08/13/2026-16471.html",
        "https://www.federalregister.gov/documents/full_text/xml/2026/08/13/2026-16471.xml",
        "https://www.govinfo.gov/content/pkg/FR-2026-08-13/html/2026-16471.htm",
    ],
)
def test_federal_register_allowed_text_urls_are_accepted(raw_text_url):
    assert (
        regulatory_monitor._federal_register_text_url_rejection_reason(
            raw_text_url, "2026-16471"
        )
        is None
    ), raw_text_url


def test_federal_register_text_url_for_another_document_is_rejected():
    """Identity is the terminal filename stem, not "appears somewhere"."""
    assert regulatory_monitor._federal_register_text_url_rejection_reason(
        "https://www.federalregister.gov/documents/full_text/text/2026/08/13/2026-99999.txt",
        "2026-16471",
    )
    # A directory/package segment must not stand in for the document itself.
    assert regulatory_monitor._federal_register_text_url_rejection_reason(
        "https://www.federalregister.gov/documents/full_text/text/2026-16471/2026-99999.txt",
        "2026-16471",
    )


@pytest.mark.parametrize(
    "content_type,should_reject",
    [
        ("text/plain; charset=utf-8", False),
        ("text/html; charset=utf-8", False),
        ("application/xml", False),
        ("text/xml", False),
        (None, False),  # "where available" -- absence cannot fail the run
        ("application/json", True),
        ("application/pdf", True),
        ("image/png", True),
    ],
)
def test_federal_register_content_type_validation(content_type, should_reject):
    reason = regulatory_monitor._federal_register_content_type_rejection_reason(
        content_type,
        "https://www.federalregister.gov/documents/full_text/text/2026/08/13/2026-16471.txt",
    )
    assert bool(reason) is should_reject, (content_type, reason)


def test_federal_register_json_content_type_fails_closed_mid_flight(monkeypatch):
    """An allowed URL that answers JSON is still refused.

    URL shape is a promise, not proof: an edge rewrite can answer the ``.txt``
    path with the metadata record. The transport's own declaration is checked
    before anything is parsed or hashed.
    """
    session = _PagedFederalRegisterSession({1: _federal_register_source_text_page()})

    def fake_fetch_page(url, _session, max_retries=3):
        return {
            "url": url,
            "status_code": 200,
            "content": '{"abstract": "Members must supervise artificial intelligence."}',
            "final_url": url,
            "was_redirected": False,
            "error": None,
            "content_type": "application/json",
        }

    monkeypatch.setattr(regulatory_monitor, "fetch_page", fake_fetch_page)
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-13", config=_load_config()
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )
    assert state == {}


def test_federal_register_redirect_to_another_document_fails_closed(monkeypatch):
    """A same-host redirect that changes the document is not a benign redirect."""
    session = _PagedFederalRegisterSession({1: _federal_register_source_text_page()})
    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        _federal_register_text_fetch(
            "AGENCY: Securities and Exchange Commission. SUMMARY: Members must "
            "supervise artificial intelligence. " * 20,
            final_url=(
                "https://www.federalregister.gov/documents/full_text/text/"
                "2026/08/13/2026-99999.txt"
            ),
        ),
    )
    monkeypatch.setattr(regulatory_monitor.time, "sleep", lambda *_a, **_k: None)

    state: dict = {}
    with pytest.raises(regulatory_monitor.RequiredSourceTextError):
        items = regulatory_monitor.fetch_federal_register_documents(
            session=session, since_date="2026-08-13", config=_load_config()
        )
        regulatory_monitor.update_source_state(
            regulatory_monitor.SOURCE_KEY_FEDERAL_REGISTER, items, state
        )
    assert state == {}


# --- Finding 6: multiword and organizational citation authors ---------------


REVIEW9_CITATION_ONLY_CLAUSES = (
    "(van der Waals, 2026)",
    "(de la Cruz and Jones, 2026)",
    "(von Neumann et al., 2026)",
    "(Government Accountability Office, 2026)",
    "(Federal Reserve Bank of New York, 2026)",
    "(Office of Thrift Supervision, 2026)",
    "(Board of Governors of the Federal Reserve System, 2026)",
    "according to van der Waals (2026)",
    "according to the Government Accountability Office (2026)",
    "as reported by the Federal Reserve Bank of New York (2026)",
    "as described in van der Waals (2026)",
    # Prior single-token behaviour must be untouched.
    "(Jones, 2026)",
    "(Smith and Jones, 2026)",
    "(Smith, Jones, and Lee, 2026)",
    "(Jones et al., 2026)",
)

REVIEW9_NOT_CITATIONS = (
    "(as amended by commission, 2026)",
    "(effective January 1, 2026)",
    "(September 2026)",
    "(as amended, 2026)",
    "(revised 2026)",
    "(see 17 CFR 240.17a-4)",
)


@pytest.mark.parametrize("clause", REVIEW9_CITATION_ONLY_CLAUSES)
def test_multiword_and_organizational_authors_are_recognised(clause):
    assert regulatory_monitor.REFERENCE_ONLY_PATTERN.search(clause.lower()), clause


@pytest.mark.parametrize("clause", REVIEW9_NOT_CITATIONS)
def test_non_author_parentheticals_are_not_citations(clause):
    assert not regulatory_monitor.REFERENCE_ONLY_PATTERN.search(clause.lower()), clause


@pytest.mark.parametrize("author", [
    "van der Waals",
    "the Government Accountability Office",
    "the Federal Reserve Bank of New York",
])
def test_operative_language_outranks_organizational_citation(author, monkeypatch):
    """Precedence is unchanged: a duty is a duty even beside a citation.

    ``_is_reference_only_occurrence`` consults ``has_operative`` first and
    short-circuits, so widening the author grammar cannot suppress a real
    obligation. That ordering is what bounds the blast radius of this change.
    """
    config = _load_config()
    classification, reason = regulatory_monitor.classify_regulatory_relevance(
        "Regulatory Notice 26-10",
        f"Members must supervise artificial intelligence tools ({author}, 2026).",
        config,
        exclude_reference_only=True,
    )
    assert classification == regulatory_monitor.CLASSIFICATION_HIGH
    assert "artificial intelligence" in reason.lower()


def test_organizational_author_grammar_does_not_backtrack():
    """Atomic grouping, not a nested quantifier.

    The name unit became a bounded multiword run, which is the classic shape
    for catastrophic backtracking. Growth must stay linear; an exponential
    regex here would be a denial of service against the monitor itself.
    """
    import time as _time

    timings = []
    for width in (40, 80, 160, 320):
        hostile = "(" + " ".join(["accountability"] * width) + " 2026"
        start = _time.perf_counter()
        regulatory_monitor.REFERENCE_ONLY_PATTERN.search(hostile)
        timings.append(_time.perf_counter() - start)
    assert max(timings) < 0.5, timings
    # Doubling the input must not more than quadruple the time.
    assert timings[-1] < max(timings[0], 1e-4) * 40, timings


# --- Finding 7: recordkeeping semantic binding ------------------------------


REVIEW9_RECORDKEEPING_HIGH = (
    # (a) "permitted" modifies the repository, not the obligation.
    "Records must be stored electronically in a permitted repository.",
    "Books and records must be stored electronically in a permitted repository.",
    "Records must be stored electronically in a permissible format.",
    "Records must be preserved electronically on an approved platform.",
    # (b) conjunction-led subject change with no punctuation at all.
    "Books and records must be stored electronically while employee handbooks "
    "may be printed on paper",
    "Books and records must be stored electronically whereas marketing "
    "brochures may be printed on paper",
    # The punctuated form must keep working too.
    "Books and records must be stored electronically, while employee handbooks "
    "may be printed on paper",
    # Prior positives.
    "Books and records must be preserved electronically.",
    "Records must be maintained electronically rather than in paper form.",
    "Records that may contain customer information must be retained electronically.",
)

REVIEW9_RECORDKEEPING_NON_HIGH = (
    # (c) a conditional paper fallback is not an electronic-only mandate.
    "Records must be retained electronically or, if not feasible, in paper form",
    "Records must be retained electronically or, where not practicable, in paper form",
    # The concessive form still names paper as the alternative subject.
    "Records must be stored electronically although paper copies may also be retained",
    # Prior negatives.
    "Records may be retained electronically.",
    "Firms are not required to store records electronically.",
    "Records must be stored electronically unless retained in paper form",
    "Records may be stored electronically where permitted.",
    "Records must be stored electronically if permitted by the firm.",
    "Although the storage method is optional, records must be stored electronically",
    "Records must be stored electronically, although the storage method is optional",
)


@pytest.mark.parametrize("text", REVIEW9_RECORDKEEPING_HIGH)
def test_recordkeeping_obligation_survives_qualifiers(text):
    assert regulatory_monitor._has_electronic_recordkeeping_obligation(text), text


@pytest.mark.parametrize("text", REVIEW9_RECORDKEEPING_NON_HIGH)
def test_recordkeeping_alternatives_are_not_obligations(text):
    assert not regulatory_monitor._has_electronic_recordkeeping_obligation(text), text


def test_attributive_permission_is_masked_but_predicative_is_not():
    """The distinction is grammatical position, not vocabulary.

    "a permitted repository" describes where the duty must be discharged;
    "is permitted" describes whether there is a duty at all. Masking the word
    everywhere would erase real permissions; masking it nowhere demoted a real
    mandate.
    """
    attributive = "Records must be stored electronically in a permitted repository."
    assert "permitted" not in regulatory_monitor._mask_attributive_permissions(
        attributive
    )
    for predicative in (
        "Electronic storage is permitted where feasible.",
        "Records may be stored electronically if permitted.",
        "Paper retention is not permitted.",
    ):
        assert "permitted" in regulatory_monitor._mask_attributive_permissions(
            predicative
        ), predicative


def test_conjunction_split_requires_a_new_statement():
    """"and" must not fragment a compound subject.

    "Books and records" is one subject. If the segmenter split on every
    conjunction, the duty would lose its subject and the sentence would stop
    being a recordkeeping obligation at all.
    """
    clause = "books and records must be stored electronically"
    assert len(regulatory_monitor._storage_clause_segments(clause)) == 1
    split = (
        "books and records must be stored electronically while handbooks may "
        "be printed on paper"
    )
    assert len(regulatory_monitor._storage_clause_segments(split)) == 2


def test_comma_delimited_conditional_does_not_read_as_paper_replacement():
    """The 'not' in ", if not feasible," qualifies feasibility, nothing else."""
    assert regulatory_monitor._clause_permits_paper_alternative(
        "records must be retained electronically or, if not feasible, in paper form"
    )
    # An undelimited exception keeps its connector and is still an alternative.
    assert regulatory_monitor._clause_permits_paper_alternative(
        "records must be stored electronically unless retained in paper form"
    )
    # A genuine replacement is still a replacement.
    assert not regulatory_monitor._clause_permits_paper_alternative(
        "records must be maintained electronically rather than in paper form"
    )
