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

CONFIG_PATH = REPO_ROOT / "scripts" / "config" / "monitoring-config.yaml"


def _load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


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

    monkeypatch.setattr(
        regulatory_monitor,
        "fetch_page",
        lambda url, _session, max_retries=3: {
            "url": url,
            "status_code": 200,
            "content": listing_html,
            "final_url": url,
            "was_redirected": False,
            "error": None,
        },
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
    field ordering (title|abstract|publication_date)."""
    item = _fed_item("alpha\n\nbeta   gamma")
    fp = regulatory_monitor._content_fingerprint(item)
    assert "alpha beta gamma" in fp
    assert fp.split("|")[2] == "2026-07-11"


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
