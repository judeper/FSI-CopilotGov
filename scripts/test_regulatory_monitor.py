"""Regression tests for FINRA/Federal Register regulatory monitoring logic."""
from __future__ import annotations

import sys
from pathlib import Path

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
