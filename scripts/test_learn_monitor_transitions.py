"""Focused tests for Learn-monitor content scoping and page-shape guards."""
from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import sys

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
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


def test_extract_scoped_content_uses_configured_heading():
    url = (
        "https://learn.microsoft.com/en-us/azure/sentinel/"
        "data-connectors-reference#microsoft-365-formerly-office-365"
    )
    html = """
    <html>
      <body>
        <main>
          <h2 id="microsoft-365-formerly-office-365">Microsoft 365 (formerly Office 365)</h2>
          <p>Keep this section.</p>
          <h2 id="airlock-digital">Airlock Digital</h2>
          <p>Do not include this noisy connector.</p>
        </main>
      </body>
    </html>
    """
    config = {
        "learn": {
            "section_anchors": [
                {
                    "url": url,
                    "heading": "Microsoft 365 (formerly Office 365)",
                }
            ]
        },
        "regulatory": {},
    }

    snapshot = monitoring_shared.extract_learn_content_snapshot(url, html, config)

    assert snapshot.content_scope == "section:Microsoft 365 (formerly Office 365)"
    assert "Keep this section." in snapshot.normalized_content
    assert "Airlock Digital" not in snapshot.normalized_content
    assert snapshot.warning is None


def test_extract_scoped_content_falls_back_to_whole_page_when_anchor_missing():
    url = "https://learn.microsoft.com/en-us/example/page#missing-section"
    html = """
    <html>
      <body>
        <main>
          <h2 id="different-section">Different section</h2>
          <p>Keep monitoring the full page.</p>
        </main>
      </body>
    </html>
    """
    config = {
        "learn": {
            "section_anchors": [
                {"url": url, "heading": "Missing section"}
            ]
        },
        "regulatory": {},
    }

    snapshot = monitoring_shared.extract_learn_content_snapshot(url, html, config)

    assert snapshot.content_scope == "whole-page"
    assert "Keep monitoring the full page." in snapshot.normalized_content
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
    html = """
    <html>
      <body>
        <main>
          <p>Table of contents</p>
          <p>Access to this page requires authorization. You can try signing in or changing directories.</p>
          <p>remove connections when they're no longer needed.</p>
        </main>
      </body>
    </html>
    """

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


def test_run_monitor_rebaselines_when_section_scope_changes_without_alerting(
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
    html = """
    <html>
      <body>
        <main>
          <h2 id="microsoft-365-formerly-office-365">Microsoft 365 (formerly Office 365)</h2>
          <p>Stable connector text.</p>
          <h2 id="airlock-digital">Airlock Digital</h2>
          <ol>
            <li>Click Add connector.</li>
          </ol>
        </main>
      </body>
    </html>
    """
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
    assert saved_entry["content_scope"] == "section:Microsoft 365 (formerly Office 365)"
    assert saved_entry["normalized_content"] == "\n".join(
        [
            "Microsoft 365 (formerly Office 365)",
            "Stable connector text.",
        ]
    )
