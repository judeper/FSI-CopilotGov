"""Tests for monitoring_shared.find_affected_controls.

Verifies that the URL-to-doc mapping scans BOTH control-implementation
playbooks and the cross-cutting playbook folders (governance-operations,
compliance-and-audit, incident-and-risk, regulatory-modules, getting-started).
The cross-cutting scan was previously missing, leaving those playbooks
invisible to the Learn/regulatory monitors.
"""
from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import monitoring_shared  # noqa: E402


def _write(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def _make_docs(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    url = "https://learn.microsoft.com/en-us/example/page"

    # A control that cites the URL.
    _write(
        docs / "controls" / "pillar-2-security" / "2.1-example.md",
        f"# 2.1 Example Control\n\nSee {url} for details.\n",
    )
    # A control-implementation playbook that cites the URL.
    _write(
        docs / "playbooks" / "control-implementations" / "2.1" / "portal-walkthrough.md",
        f"# Portal walkthrough\n\n{url}\n",
    )
    # A cross-cutting playbook that cites the URL.
    _write(
        docs / "playbooks" / "governance-operations" / "ops-guide.md",
        f"# Ops guide\n\nReference: {url}\n",
    )
    # A nested cross-cutting playbook that cites the URL.
    _write(
        docs / "playbooks" / "compliance-and-audit" / "nested" / "audit.md",
        f"# Audit\n\n{url}\n",
    )
    # A playbook that does NOT cite the URL (must be excluded).
    _write(
        docs / "playbooks" / "governance-operations" / "unrelated.md",
        "# Unrelated\n\nNothing relevant here.\n",
    )
    return docs


def test_finds_control_and_all_playbook_kinds(tmp_path):
    docs = _make_docs(tmp_path)
    url = "https://learn.microsoft.com/en-us/example/page"

    result = monitoring_shared.find_affected_controls(url, docs)

    # Control match.
    assert any(c["control_id"] == "2.1" for c in result["controls"])

    paths = {p["file_path"].replace("\\", "/") for p in result["playbooks"]}
    # control-implementation playbook.
    assert "playbooks/control-implementations/2.1/portal-walkthrough.md" in paths
    # cross-cutting (flat).
    assert "playbooks/governance-operations/ops-guide.md" in paths
    # cross-cutting (nested, via rglob).
    assert "playbooks/compliance-and-audit/nested/audit.md" in paths
    # non-citing playbook excluded.
    assert "playbooks/governance-operations/unrelated.md" not in paths


def test_portal_walkthrough_is_critical(tmp_path):
    docs = _make_docs(tmp_path)
    url = "https://learn.microsoft.com/en-us/example/page"

    result = monitoring_shared.find_affected_controls(url, docs)
    pw = next(
        p for p in result["playbooks"]
        if p["file_path"].replace("\\", "/").endswith("2.1/portal-walkthrough.md")
    )
    assert pw["priority"] == monitoring_shared.CLASSIFICATION_CRITICAL


def test_no_match_returns_empty(tmp_path):
    docs = _make_docs(tmp_path)
    result = monitoring_shared.find_affected_controls(
        "https://learn.microsoft.com/en-us/not/cited", docs
    )
    assert result == {"controls": [], "playbooks": []}


def _assert_cowork_variants_map(url_variant: str) -> None:
    result = monitoring_shared.find_affected_controls(url_variant, REPO_ROOT / "docs")

    control_ids = {c["control_id"] for c in result["controls"]}
    assert "4.15" in control_ids

    paths = {p["file_path"].replace("\\", "/") for p in result["playbooks"]}
    expected = {
        "playbooks/control-implementations/4.15/portal-walkthrough.md",
        "playbooks/control-implementations/4.15/powershell-setup.md",
        "playbooks/control-implementations/4.15/troubleshooting.md",
        "playbooks/control-implementations/4.15/verification-testing.md",
    }
    assert expected.issubset(paths)


def test_cowork_url_variants_map_to_control_and_playbooks():
    variants = [
        "https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-admin-governance",
        "https://LEARN.MICROSOFT.COM/en-us/microsoft-365/copilot/cowork/cowork-admin-governance",
        "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance/",
        "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance#overview",
    ]
    for url_variant in variants:
        _assert_cowork_variants_map(url_variant)


def test_canonicalizer_accepts_scheme_less_learn_url():
    assert monitoring_shared._canonicalize_reference_url(
        "learn.microsoft.com/en-us/example/page"
    ) == "learn.microsoft.com/example/page"


def test_canonicalizer_does_not_treat_embedded_learn_host_as_learn_url():
    assert monitoring_shared._canonicalize_reference_url(
        "example.com/learn.microsoft.com/en-us/example/page"
    ) == "https://example.com/learn.microsoft.com/en-us/example/page"
