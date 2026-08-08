"""Regression tests for FINRA/Federal Register regulatory monitoring logic."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import regulatory_monitor  # noqa: E402

CONFIG_PATH = REPO_ROOT / "scripts" / "config" / "monitoring-config.yaml"


def _load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


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
                "abstract": "A regulatory notice with no special relevance.",
                "publication_date": "2026-07-27",
                "type": "NOTICE",
                "html_url": f"https://www.federalregister.gov/documents/{document_id}",
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


def test_federal_register_overlapping_pages_are_deduplicated():
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


def test_finra_notice_body_fallback_promotes_genai_notice_to_high(monkeypatch):
    config = _load_config()
    listing_html = """
    <html><body>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment</a>
    </body></html>
    """
    detail_html = """
    <html><body>
      <main>
        GenAI communication tools may be included in a reasonably designed supervisory system
        when firms vet, test, and continuously monitor for hallucination and data-protection risk.
      </main>
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


def test_finra_notice_body_fetch_failure_keeps_item_and_avoids_crash(monkeypatch):
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

    items = regulatory_monitor.fetch_finra_notices(
        session=object(),
        config=config,
        limit=1,
    )

    assert len(items) == 1
    assert items[0].classification == regulatory_monitor.CLASSIFICATION_MEDIUM
    assert items[0].abstract == ""


def test_finra_notice_body_fetch_uses_cache(monkeypatch):
    config = _load_config()
    listing_html = """
    <html><body>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment</a>
      <a href="/rules-guidance/notices/26-14">Regulatory Notice 26-14: Request for Comment (duplicate)</a>
    </body></html>
    """
    detail_html = """
    <html><body><main>GenAI monitoring language for notice 26-14.</main></body></html>
    """
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

    assert len(items) == 2
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
    field ordering (title|abstract|publication_date)."""
    item = _fed_item("alpha\n\nbeta   gamma")
    fp = regulatory_monitor._content_fingerprint(item)
    assert "alpha beta gamma" in fp
    assert fp.split("|")[2] == "2026-07-11"


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
