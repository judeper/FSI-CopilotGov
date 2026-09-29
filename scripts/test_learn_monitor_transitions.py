"""Focused tests for Learn-monitor content scoping and page-shape guards."""
from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import sys

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
FIXTURES_DIR = SCRIPTS_DIR / "fixtures" / "learn_monitor"
sys.path.insert(0, str(SCRIPTS_DIR))

import learn_monitor  # noqa: E402
import monitoring_shared  # noqa: E402


def _write_watchlist(path: Path, url: str, topic: str = "Tracked page") -> None:
    path.write_text(
        "\n".join(
            [
                "## Test Section",
                "",
                "| Topic | URL |",
                "|-------|-----|",
                f"| {topic} | [{url}]({url}) |",
                "",
            ]
        ),
        encoding="utf-8",
    )


def _args() -> SimpleNamespace:
    return SimpleNamespace(
        dry_run=False,
        limit=None,
        verbose=False,
        debug=False,
        url=None,
        config=None,
        validate=False,
    )


def _fixture(name: str) -> str:
    return (FIXTURES_DIR / name).read_text(encoding="utf-8")


def test_find_section_heading_ignores_empty_fragment_and_matches_real_heading_text():
    soup = monitoring_shared.BeautifulSoup(
        _fixture("conditional-access-overview-main.html"),
        "html.parser",
    )
    main = soup.find("main")

    heading = monitoring_shared._find_section_heading(main, "Common signals", "")

    assert heading is not None
    assert heading.get_text(" ", strip=True) == "Common signals"


def test_extract_section_from_heading_stops_at_wrapped_next_heading_on_real_fixture():
    soup = monitoring_shared.BeautifulSoup(
        _fixture("conditional-access-overview-main.html"),
        "html.parser",
    )
    main = soup.find("main")
    heading = monitoring_shared._find_section_heading(main, "Overview", "")
    assert heading is not None

    section = monitoring_shared._extract_section_from_heading(heading)

    assert "Overview" in section
    assert "Common signals" not in section


def test_extract_scoped_content_uses_real_sentinel_connector_block():
    url = (
        "https://learn.microsoft.com/en-us/azure/sentinel/"
        "data-connectors-reference#microsoft-365-formerly-office-365"
    )
    config = monitoring_shared.load_monitoring_config()

    snapshot = monitoring_shared.extract_learn_content_snapshot(
        url,
        _fixture("sentinel-connectors-subset.html"),
        config,
    )

    assert snapshot.content_scope == "section:Microsoft 365 (formerly, Office 365)"
    assert "The Microsoft 365 (formerly, Office 365) activity log connector" in snapshot.normalized_content
    assert "Airlock Digital" not in snapshot.normalized_content
    assert snapshot.warning is None


def test_extract_scoped_content_marks_missing_section_without_silent_success():
    url = "https://learn.microsoft.com/en-us/example/page#missing-section"
    config = {
        "learn": {
            "section_anchors": [
                {"url": url, "heading": "Missing section"}
            ]
        },
        "regulatory": {},
    }

    snapshot = monitoring_shared.extract_learn_content_snapshot(
        url,
        _fixture("sentinel-connectors-subset.html"),
        config,
    )

    assert snapshot.content_scope == "whole-page"
    assert snapshot.scope_missing is True
    assert snapshot.warning == (
        "Configured Learn section anchor not found for "
        "https://learn.microsoft.com/en-us/example/page#missing-section: "
        "Missing section"
    )


def test_run_monitor_skips_authorization_interstitial_and_preserves_baseline(
    monkeypatch,
    tmp_path,
    caplog,
):
    url = "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms"
    watchlist = tmp_path / "microsoft-learn-urls.md"
    state_path = tmp_path / "monitor-state.json"
    reports_dir = tmp_path / "reports"
    old_content = "\n".join(
        [
            "Connected platforms in Microsoft Agent 365",
            "Manage external platform connections",
        ]
    )
    state = {
        "version": 1,
        "sources": {
            "learn": {
                "last_run": "2026-09-28T00:00:00+00:00",
                "urls": {
                    url: {
                        "content_hash": monitoring_shared.compute_hash(old_content),
                        "normalized_content": old_content,
                        "content_scope": "whole-page",
                        "last_checked": "2026-09-28T00:00:00+00:00",
                        "last_status": 200,
                        "last_changed": "2026-09-28T00:00:00+00:00",
                        "topic": "Connected platforms",
                        "section": "Agent Governance",
                    }
                },
                "statistics": {},
            }
        },
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")
    _write_watchlist(watchlist, url, "Connected platforms")

    config = monitoring_shared.load_monitoring_config()
    html = _fixture("learn-auth-note-only.html")

    monkeypatch.setattr(learn_monitor, "WATCHLIST_PATH", watchlist)
    monkeypatch.setattr(learn_monitor, "STATE_FILE_PATH", state_path)
    monkeypatch.setattr(learn_monitor, "REPORTS_DIR", reports_dir)
    monkeypatch.setattr(learn_monitor.time, "sleep", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        learn_monitor,
        "fetch_page",
        lambda *_args, **_kwargs: {
            "url": url,
            "status_code": 200,
            "content": html,
            "content_type": "text/html",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        },
    )

    with caplog.at_level("WARNING"):
        with pytest.raises(SystemExit) as excinfo:
            learn_monitor._run_monitor(_args(), config)

    assert excinfo.value.code == 0
    saved = json.loads(state_path.read_text(encoding="utf-8"))
    saved_entry = saved["sources"]["learn"]["urls"][url]
    assert saved_entry["content_hash"] == monitoring_shared.compute_hash(old_content)
    assert saved_entry["normalized_content"] == old_content
    assert "Authorization interstitial" in caplog.text


def test_run_monitor_rescopes_legacy_sentinel_baseline_without_alerting(
    monkeypatch,
    tmp_path,
):
    url = (
        "https://learn.microsoft.com/en-us/azure/sentinel/"
        "data-connectors-reference#microsoft-365-formerly-office-365"
    )
    watchlist = tmp_path / "microsoft-learn-urls.md"
    state_path = tmp_path / "monitor-state.json"
    reports_dir = tmp_path / "reports"
    html = _fixture("sentinel-connectors-subset.html")
    _write_watchlist(watchlist, url, "Connect Microsoft 365 data")

    old_content = monitoring_shared.normalize_content(html)
    state = {
        "version": 1,
        "sources": {
            "learn": {
                "last_run": "2026-09-28T00:00:00+00:00",
                "urls": {
                    url: {
                        "content_hash": monitoring_shared.compute_hash(old_content),
                        "normalized_content": old_content,
                        "last_checked": "2026-09-28T00:00:00+00:00",
                        "last_status": 200,
                        "last_changed": "2026-09-28T00:00:00+00:00",
                        "topic": "Connect Microsoft 365 data",
                        "section": "Microsoft Sentinel",
                    }
                },
                "statistics": {},
            }
        },
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")

    config = monitoring_shared.load_monitoring_config()

    monkeypatch.setattr(learn_monitor, "WATCHLIST_PATH", watchlist)
    monkeypatch.setattr(learn_monitor, "STATE_FILE_PATH", state_path)
    monkeypatch.setattr(learn_monitor, "REPORTS_DIR", reports_dir)
    monkeypatch.setattr(learn_monitor.time, "sleep", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        learn_monitor,
        "fetch_page",
        lambda *_args, **_kwargs: {
            "url": url,
            "status_code": 200,
            "content": html,
            "content_type": "text/html",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        },
    )

    with pytest.raises(SystemExit) as excinfo:
        learn_monitor._run_monitor(_args(), config)

    assert excinfo.value.code == 0
    saved = json.loads(state_path.read_text(encoding="utf-8"))
    saved_entry = saved["sources"]["learn"]["urls"][url]
    assert saved_entry["content_scope"] == "section:Microsoft 365 (formerly, Office 365)"
    assert "The Microsoft 365 (formerly, Office 365) activity log connector" in saved_entry["normalized_content"]


def test_run_monitor_reports_missing_scoped_section_and_preserves_last_good_baseline(
    monkeypatch,
    tmp_path,
):
    url = (
        "https://learn.microsoft.com/en-us/azure/sentinel/"
        "data-connectors-reference#microsoft-365-formerly-office-365"
    )
    watchlist = tmp_path / "microsoft-learn-urls.md"
    state_path = tmp_path / "monitor-state.json"
    reports_dir = tmp_path / "reports"
    _write_watchlist(watchlist, url, "Connect Microsoft 365 data")
    config = monitoring_shared.load_monitoring_config()

    old_snapshot = monitoring_shared.extract_learn_content_snapshot(
        url,
        _fixture("sentinel-connectors-subset.html"),
        config,
    )
    missing_scope_html = _fixture("sentinel-connectors-subset.html").replace(
        "Microsoft 365 (formerly, Office 365)",
        "Microsoft 365 activity log",
        1,
    )
    state = {
        "version": 1,
        "sources": {
            "learn": {
                "last_run": "2026-09-28T00:00:00+00:00",
                "urls": {
                    url: {
                        "content_hash": monitoring_shared.compute_hash(old_snapshot.normalized_content),
                        "normalized_content": old_snapshot.normalized_content,
                        "content_scope": old_snapshot.content_scope,
                        "last_checked": "2026-09-28T00:00:00+00:00",
                        "last_status": 200,
                        "last_changed": "2026-09-28T00:00:00+00:00",
                        "topic": "Connect Microsoft 365 data",
                        "section": "Microsoft Sentinel",
                    }
                },
                "statistics": {},
            }
        },
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")

    monkeypatch.setattr(learn_monitor, "WATCHLIST_PATH", watchlist)
    monkeypatch.setattr(learn_monitor, "STATE_FILE_PATH", state_path)
    monkeypatch.setattr(learn_monitor, "REPORTS_DIR", reports_dir)
    monkeypatch.setattr(learn_monitor.time, "sleep", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        learn_monitor,
        "fetch_page",
        lambda *_args, **_kwargs: {
            "url": url,
            "status_code": 200,
            "content": missing_scope_html,
            "content_type": "text/html",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        },
    )

    with pytest.raises(SystemExit) as excinfo:
        learn_monitor._run_monitor(_args(), config)

    assert excinfo.value.code == 1
    saved = json.loads(state_path.read_text(encoding="utf-8"))
    saved_entry = saved["sources"]["learn"]["urls"][url]
    assert saved_entry["normalized_content"] == old_snapshot.normalized_content
    assert saved_entry["content_scope"] == old_snapshot.content_scope


def test_run_monitor_heals_old_interstitial_baseline_with_real_article(
    monkeypatch,
    tmp_path,
):
    url = "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms"
    watchlist = tmp_path / "microsoft-learn-urls.md"
    state_path = tmp_path / "monitor-state.json"
    reports_dir = tmp_path / "reports"
    _write_watchlist(watchlist, url, "Connected platforms")
    config = monitoring_shared.load_monitoring_config()
    interstitial = monitoring_shared.extract_learn_content_snapshot(
        url,
        _fixture("learn-auth-note-only.html"),
        config,
    )
    assert interstitial.page_shape == "Authorization interstitial"
    state = {
        "version": 1,
        "sources": {
            "learn": {
                "last_run": "2026-09-28T00:00:00+00:00",
                "urls": {
                    url: {
                        "content_hash": monitoring_shared.compute_hash(interstitial.normalized_content),
                        "normalized_content": interstitial.normalized_content,
                        "content_scope": interstitial.content_scope,
                        "last_checked": "2026-09-28T00:00:00+00:00",
                        "last_status": 200,
                        "last_changed": "2026-09-28T00:00:00+00:00",
                        "topic": "Connected platforms",
                        "section": "Agent Governance",
                    }
                },
                "statistics": {},
            }
        },
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")

    monkeypatch.setattr(learn_monitor, "WATCHLIST_PATH", watchlist)
    monkeypatch.setattr(learn_monitor, "STATE_FILE_PATH", state_path)
    monkeypatch.setattr(learn_monitor, "REPORTS_DIR", reports_dir)
    monkeypatch.setattr(learn_monitor.time, "sleep", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        learn_monitor,
        "fetch_page",
        lambda *_args, **_kwargs: {
            "url": url,
            "status_code": 200,
            "content": _fixture("connected-platforms-main.html"),
            "content_type": "text/html",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        },
    )

    with pytest.raises(SystemExit) as excinfo:
        learn_monitor._run_monitor(_args(), config)

    assert excinfo.value.code == 0
    saved = json.loads(state_path.read_text(encoding="utf-8"))
    assert "Connected platforms in Microsoft Agent 365" in saved["sources"]["learn"]["urls"][url]["normalized_content"]


def test_real_change_is_detected_after_temporary_interstitial_without_losing_baseline(
    monkeypatch,
    tmp_path,
):
    url = "https://learn.microsoft.com/en-us/microsoft-agent-365/admin/connected-platforms"
    watchlist = tmp_path / "microsoft-learn-urls.md"
    state_path = tmp_path / "monitor-state.json"
    reports_dir = tmp_path / "reports"
    _write_watchlist(watchlist, url, "Connected platforms")
    config = monitoring_shared.load_monitoring_config()
    baseline = monitoring_shared.extract_learn_content_snapshot(
        url,
        _fixture("connected-platforms-main.html"),
        config,
    )
    state = {
        "version": 1,
        "sources": {
            "learn": {
                "last_run": "2026-09-28T00:00:00+00:00",
                "urls": {
                    url: {
                        "content_hash": monitoring_shared.compute_hash(baseline.normalized_content),
                        "normalized_content": baseline.normalized_content,
                        "content_scope": baseline.content_scope,
                        "last_checked": "2026-09-28T00:00:00+00:00",
                        "last_status": 200,
                        "last_changed": "2026-09-28T00:00:00+00:00",
                        "topic": "Connected platforms",
                        "section": "Agent Governance",
                    }
                },
                "statistics": {},
            }
        },
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")
    responses = [
        _fixture("learn-auth-note-only.html"),
        _fixture("connected-platforms-main.html").replace(
            "Synchronization, management, and observability capabilities vary by platform.",
            "Synchronization, management, and observability capabilities are generally available by platform.",
            1,
        ),
    ]

    monkeypatch.setattr(learn_monitor, "WATCHLIST_PATH", watchlist)
    monkeypatch.setattr(learn_monitor, "STATE_FILE_PATH", state_path)
    monkeypatch.setattr(learn_monitor, "REPORTS_DIR", reports_dir)
    monkeypatch.setattr(learn_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    def _fake_fetch(*_args, **_kwargs):
        return {
            "url": url,
            "status_code": 200,
            "content": responses.pop(0),
            "content_type": "text/html",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(learn_monitor, "fetch_page", _fake_fetch)

    with pytest.raises(SystemExit) as first_run:
        learn_monitor._run_monitor(_args(), config)
    assert first_run.value.code == 0

    with pytest.raises(SystemExit) as second_run:
        learn_monitor._run_monitor(_args(), config)
    assert second_run.value.code == 1


def test_reappearing_scoped_section_compares_against_retained_baseline(
    monkeypatch,
    tmp_path,
):
    url = (
        "https://learn.microsoft.com/en-us/azure/sentinel/"
        "data-connectors-reference#microsoft-365-formerly-office-365"
    )
    watchlist = tmp_path / "microsoft-learn-urls.md"
    state_path = tmp_path / "monitor-state.json"
    reports_dir = tmp_path / "reports"
    _write_watchlist(watchlist, url, "Connect Microsoft 365 data")
    config = monitoring_shared.load_monitoring_config()
    baseline = monitoring_shared.extract_learn_content_snapshot(
        url,
        _fixture("sentinel-connectors-subset.html"),
        config,
    )
    state = {
        "version": 1,
        "sources": {
            "learn": {
                "last_run": "2026-09-28T00:00:00+00:00",
                "urls": {
                    url: {
                        "content_hash": monitoring_shared.compute_hash(baseline.normalized_content),
                        "normalized_content": baseline.normalized_content,
                        "content_scope": baseline.content_scope,
                        "last_checked": "2026-09-28T00:00:00+00:00",
                        "last_status": 200,
                        "last_changed": "2026-09-28T00:00:00+00:00",
                        "topic": "Connect Microsoft 365 data",
                        "section": "Microsoft Sentinel",
                    }
                },
                "statistics": {},
            }
        },
    }
    state_path.write_text(json.dumps(state), encoding="utf-8")
    responses = [
        _fixture("sentinel-connectors-subset.html").replace(
            "Microsoft 365 (formerly, Office 365)",
            "Microsoft 365 activity log",
            1,
        ),
        _fixture("sentinel-connectors-subset.html").replace(
            "The Microsoft 365 (formerly, Office 365) activity log connector provides insight into ongoing user activities.",
            "The Microsoft 365 (formerly, Office 365) activity log connector is generally available for ongoing user activities.",
            1,
        ),
    ]

    monkeypatch.setattr(learn_monitor, "WATCHLIST_PATH", watchlist)
    monkeypatch.setattr(learn_monitor, "STATE_FILE_PATH", state_path)
    monkeypatch.setattr(learn_monitor, "REPORTS_DIR", reports_dir)
    monkeypatch.setattr(learn_monitor.time, "sleep", lambda *_args, **_kwargs: None)

    def _fake_fetch(*_args, **_kwargs):
        return {
            "url": url,
            "status_code": 200,
            "content": responses.pop(0),
            "content_type": "text/html",
            "final_url": url,
            "was_redirected": False,
            "error": None,
        }

    monkeypatch.setattr(learn_monitor, "fetch_page", _fake_fetch)

    with pytest.raises(SystemExit) as missing_run:
        learn_monitor._run_monitor(_args(), config)
    assert missing_run.value.code == 1

    with pytest.raises(SystemExit) as changed_run:
        learn_monitor._run_monitor(_args(), config)
    assert changed_run.value.code == 1
