"""Regression tests for FINRA/Federal Register regulatory monitoring logic."""
from __future__ import annotations

from copy import deepcopy
import sys
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
            "raw_text_url": "https://example.test/2026-17183.txt",
            "agencies": [{"slug": "securities-and-exchange-commission", "name": "SEC"}],
        },
        {
            "document_number": "2026-16876",
            "title": "Agency Information Collection Activities: Part 41",
            "abstract": "A proposed renewal of an information collection.",
            "publication_date": "2026-08-19",
            "type": "NOTICE",
            "html_url": "https://www.federalregister.gov/documents/2026-16876",
            "raw_text_url": "https://example.test/2026-16876.txt",
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
        "raw_text_url": "https://example.test/2026-99001.txt",
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
        "raw_text_url": "https://example.test/2026-90210.txt",
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
        "raw_text_url": "https://example.test/2026-90211.txt",
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
            "content": "<html><body><p>No notices rendered.</p></body></html>",
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
    listing_html = """
    <html><body>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment</a>
    </body></html>
    """
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
            "content": detail_html,
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
    listing_html = """
    <html><body>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment</a>
    </body></html>
    """
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
            "content": detail_html,
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
            "content": content,
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
            "content": listing_html if url == regulatory_monitor.FINRA_NOTICES_URL else detail_html,
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
            "content": content,
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
                "content": detail_html,
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
    listing_html = """
    <html><body>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment</a>
    </body></html>
    """

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
    listing_html = """
    <html><body>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment</a>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment (duplicate)</a>
    </body></html>
    """
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
            "content": detail_html,
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
        "raw_text_url": f"https://example.test/{document_id}.txt",
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
    listing_html = (
        "<html><body>"
        "<a href='/rules-guidance/notices/26-14'>Regulatory Notice 26-14: "
        "Request for Comment</a></body></html>"
    )
    detail_html = FINRA_NON_NOTICE_FIXTURES[fixture_name]

    def fake_fetch_page(url, session, max_retries=3):
        content = (
            listing_html if url == regulatory_monitor.FINRA_NOTICES_URL else detail_html
        )
        return {
            "url": url,
            "status_code": 200,
            "content": content,
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
    listing_html = (
        "<html><body>"
        "<a href='/rules-guidance/notices/26-14'>Regulatory Notice 26-14: "
        "Request for Comment</a></body></html>"
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
            "content": content,
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
    listing_html = (
        "<html><body>"
        f"<a href='/rules-guidance/notices/26-14'>{link_text}</a>"
        "</body></html>"
    )
    detail_html = _finra_notice_page(body)

    def fake_fetch_page(url, session, max_retries=3):
        content = (
            listing_html if url == regulatory_monitor.FINRA_NOTICES_URL else detail_html
        )
        return {
            "url": url,
            "status_code": 200,
            "content": content,
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
    listing_html = (
        "<html><body>"
        "<a href='/rules-guidance/notices/26-14'>Regulatory Notice 26-14: "
        "Request for Comment</a></body></html>"
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
            "content": content,
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
