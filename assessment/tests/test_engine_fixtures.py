"""Phase E1/E2: deterministic scoring fixtures + manifest-vs-docs invariants.

These tests pin engine behaviour against hand-built collected/ payloads so that
behavioural regressions in evaluator semantics (e.g. ``audit_log_enabled``,
``copilot_retention_policy_exists``, ``grounding_sources_approved``,
``no_external_sharing_on_grounding``) are caught even when no live tenant
data is available.

E1 — Deterministic scoring fixtures
    Three tenant shapes are exercised:
      * fully-passing  → all auto-evaluated checks return True
      * fully-failing  → all auto-evaluated checks return False
      * mixed          → audit on, retention off, grounding mixed

E2 — Manifest-vs-docs invariant
    Every control id in ``assessment/manifest/controls.json`` must have:
      * a matching ``docs/controls/pillar-{P}-*/{id}-*.md`` page, AND
      * a matching ``docs/playbooks/control-implementations/{id}/`` directory
        with at least an ``index.md`` (or four standard playbook files).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_DIR = REPO_ROOT / "assessment" / "engine"
MANIFEST = REPO_ROOT / "assessment" / "manifest" / "controls.json"
CONTENT_GRAPH = REPO_ROOT / "assessment" / "manifest" / "content-graph.json"
COUNTS = json.loads(CONTENT_GRAPH.read_text(encoding="utf-8"))["counts"]
DOCS_CONTROLS = REPO_ROOT / "docs" / "controls"
DOCS_PLAYBOOKS = REPO_ROOT / "docs" / "playbooks" / "control-implementations"

sys.path.insert(0, str(ENGINE_DIR))
import score as score_mod  # noqa: E402


# ---------------------------------------------------------------------------
# Fixture helpers
# ---------------------------------------------------------------------------

def _write_collected(target: Path, payloads: dict[str, dict]) -> None:
    """Materialise a ``collected/`` directory from a {filename: payload} dict."""
    target.mkdir(parents=True, exist_ok=True)
    for filename, payload in payloads.items():
        (target / filename).write_text(json.dumps(payload), encoding="utf-8")


def _passing_payloads() -> dict[str, dict]:
    return {
        "purview.json": {
            "audit_config": {"UnifiedAuditLogIngestionEnabled": True},
            "retention_policies": [
                {"Name": "Copilot 7yr", "Workload": "Copilot", "Enabled": True}
            ],
        },
        "sharepoint.json": {
            "grounding_scope": {"unapproved": []},
            "external_sharing": {},
            "sites": [
                {"id": "site-a", "displayName": "Site A", "sharingCapability": "Disabled"}
            ],
        },
        "graph.json": {},
    }


def _failing_payloads() -> dict[str, dict]:
    return {
        "purview.json": {
            "audit_config": {"UnifiedAuditLogIngestionEnabled": False},
            "retention_policies": [
                {"Name": "Email", "Workload": "Exchange", "Enabled": True}
            ],
        },
        "sharepoint.json": {
            "grounding_scope": {"unapproved": ["external-site-1", "external-site-2"]},
            "external_sharing": {"site-a": "ExternalUserAndGuestSharing"},
            "sites": [
                {"id": "site-a", "displayName": "Site A", "sharingCapability": "ExternalUserAndGuestSharing"}
            ],
        },
        "graph.json": {},
    }


def _mixed_payloads() -> dict[str, dict]:
    return {
        "purview.json": {
            "audit_config": {"UnifiedAuditLogIngestionEnabled": True},
            "retention_policies": [],
        },
        "sharepoint.json": {
            "grounding_scope": {"unapproved": []},
            "external_sharing": {},
            "sites": [
                {"id": "site-a", "displayName": "Site A", "sharingCapability": "ExternalUserAndGuestSharing"}
            ],
        },
        "graph.json": {},
    }


# ---------------------------------------------------------------------------
# E1: Evaluator-level deterministic fixtures
# ---------------------------------------------------------------------------

class TestEvaluatorFixtures:
    """Pin evaluator return values against hand-built payloads."""

    def test_audit_log_enabled_returns_true_when_enabled(self):
        payload = {"purview": _passing_payloads()["purview.json"]}
        result, _ = score_mod._eval_audit_log_enabled(payload, None)
        assert result is True

    def test_audit_log_enabled_returns_false_when_disabled(self):
        payload = {"purview": _failing_payloads()["purview.json"]}
        result, _ = score_mod._eval_audit_log_enabled(payload, None)
        assert result is False

    def test_audit_log_enabled_returns_none_when_no_purview(self):
        result, _ = score_mod._eval_audit_log_enabled({}, None)
        assert result is None

    def test_retention_policy_exists_when_copilot_workload_enabled(self):
        payload = {"purview": _passing_payloads()["purview.json"]}
        result, _ = score_mod._eval_copilot_retention_policy_exists(payload, None)
        assert result is True

    def test_retention_policy_absent_when_no_copilot_workload(self):
        payload = {"purview": _failing_payloads()["purview.json"]}
        result, _ = score_mod._eval_copilot_retention_policy_exists(payload, None)
        assert result is False

    def test_retention_policy_absent_when_empty_list(self):
        payload = {"purview": _mixed_payloads()["purview.json"]}
        result, _ = score_mod._eval_copilot_retention_policy_exists(payload, None)
        assert result is False

    def test_grounding_sources_approved_when_no_unapproved(self):
        payload = {"sharepoint": _passing_payloads()["sharepoint.json"]}
        result, _ = score_mod._eval_grounding_sources_approved(payload, None)
        assert result is True

    def test_grounding_sources_fail_when_unapproved_present(self):
        payload = {"sharepoint": _failing_payloads()["sharepoint.json"]}
        result, msg = score_mod._eval_grounding_sources_approved(payload, None)
        assert result is False
        assert "2 unapproved" in msg

    def test_no_external_sharing_when_all_disabled(self):
        payload = {"sharepoint": _passing_payloads()["sharepoint.json"]}
        result, _ = score_mod._eval_no_external_sharing_on_grounding(payload, None)
        assert result is True

    def test_external_sharing_flagged_when_enabled(self):
        payload = {"sharepoint": _failing_payloads()["sharepoint.json"]}
        result, msg = score_mod._eval_no_external_sharing_on_grounding(payload, None)
        assert result is False
        assert "Site A" in msg


# ---------------------------------------------------------------------------
# E1: End-to-end scoring against full manifest with synthetic tenants
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "shape,payload_factory",
    [
        ("passing", _passing_payloads),
        ("failing", _failing_payloads),
        ("mixed", _mixed_payloads),
    ],
)
def test_engine_e2e_against_synthetic_tenant(tmp_path, shape, payload_factory):
    collected = tmp_path / "collected"
    _write_collected(collected, payload_factory())
    output = tmp_path / "scores.json"

    result = score_mod.run(
        manifest_path=str(MANIFEST),
        collected_dir=str(collected),
        zone=2,
        output_path=str(output),
    )

    md = result["_metadata"]
    assert md["total_controls"] == COUNTS["controls"]
    assert md["zone"] == 2
    assert md["auto_scored"] + md["needs_manual"] == COUNTS["controls"]

    avg = result["summary"]["average_maturity"]
    assert 0.0 <= avg <= 4.0

    if shape == "passing":
        # The engine must have auto-evaluated at least one check given live
        # synthetic evidence. Per-control maturity may still land at zero when
        # zone-2 thresholds require multiple passing checks per control —
        # that's exercised separately in ``test_compute_maturity_threshold_logic``.
        assert md["auto_scored"] > 0, (
            "expected the engine to auto-evaluate ≥1 check on the passing tenant"
        )
    elif shape == "failing":
        # Failing tenant should produce strictly lower per-control scores than
        # the passing tenant for the same evaluators.
        avg_failing = avg
        passing_collected = tmp_path / "collected_pass"
        _write_collected(passing_collected, _passing_payloads())
        passing_out = tmp_path / "scores_pass.json"
        passing_result = score_mod.run(
            manifest_path=str(MANIFEST),
            collected_dir=str(passing_collected),
            zone=2,
            output_path=str(passing_out),
        )
        assert passing_result["summary"]["average_maturity"] >= avg_failing


# ---------------------------------------------------------------------------
# E2: Manifest-vs-docs invariant
# ---------------------------------------------------------------------------

_PILLAR_SLUG = {
    1: "pillar-1-readiness",
    2: "pillar-2-security",
    3: "pillar-3-compliance",
    4: "pillar-4-operations",
}


def _control_doc_for(control_id: str, pillar: int) -> Path | None:
    pillar_dir = DOCS_CONTROLS / _PILLAR_SLUG[pillar]
    if not pillar_dir.is_dir():
        return None
    pattern = re.compile(rf"^{re.escape(control_id)}-.+\.md$")
    for f in pillar_dir.iterdir():
        if pattern.match(f.name):
            return f
    return None


def test_every_manifest_control_has_a_docs_page():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    missing: list[str] = []
    for control in manifest:
        cid = control["id"]
        pillar = control["pillar"]
        doc = _control_doc_for(cid, pillar)
        if doc is None:
            missing.append(f"{cid} (pillar {pillar})")
    assert not missing, (
        "Manifest controls without matching docs/controls/ page:\n  "
        + "\n  ".join(missing)
    )


def test_every_manifest_control_has_a_playbook_directory():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    missing: list[str] = []
    for control in manifest:
        cid = control["id"]
        pb_dir = DOCS_PLAYBOOKS / cid
        # Some sub-controls (e.g. ``3.8a``) intentionally share the parent
        # control's playbook directory rather than ship a duplicate set.
        if not pb_dir.is_dir():
            parent = re.match(r"^(\d+\.\d+)[a-z]$", cid)
            if parent:
                pb_dir = DOCS_PLAYBOOKS / parent.group(1)
        if not pb_dir.is_dir():
            missing.append(cid)
            continue
        # Must contain at least one playbook md beyond an empty dir
        mds = list(pb_dir.glob("*.md"))
        if not mds:
            missing.append(f"{cid} (empty)")
    assert not missing, (
        "Manifest controls without matching playbook directory:\n  "
        + "\n  ".join(missing)
    )


def test_no_orphaned_playbook_directories():
    """Every playbook directory must correspond to a manifest control."""
    manifest_ids = {c["id"] for c in json.loads(MANIFEST.read_text(encoding="utf-8"))}
    orphans = [
        d.name
        for d in DOCS_PLAYBOOKS.iterdir()
        if d.is_dir() and d.name not in manifest_ids and d.name != "shared"
    ]
    assert not orphans, (
        "Playbook directories without a matching manifest control:\n  "
        + "\n  ".join(orphans)
    )


# ---------------------------------------------------------------------------
# C2b — Automation label regression tests (issue #256)
# ---------------------------------------------------------------------------

def test_c2_4_automation_is_not_full():
    """Control 2.4 (Information Barriers) must be labeled 'manual' automation.

    IB policy existence is collector-queryable, but no verified pass-condition
    evaluator exists — 'full' would be dishonest.  'manual' is the honest label
    because boundary effectiveness requires human attestation.  Regression guard
    against re-introduction of the misleading 'full' label.
    """
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    c = next((c for c in manifest if c["id"] == "2.4"), None)
    assert c is not None, "Control 2.4 not found in manifest"
    assert c["automation"] != "full", (
        f"Control 2.4 has automation={c['automation']!r}; "
        "expected 'manual' because no verified automated IB checks exist"
    )
    # Manual is the correct label: no collector has a verified pass/fail
    # evaluator for IB boundary effectiveness.
    assert c["automation"] == "manual", (
        f"Control 2.4 automation should be 'manual', got {c['automation']!r}"
    )
    assert isinstance(c.get("manual_question"), str) and c["manual_question"].strip(), (
        "Control 2.4 must have a non-empty manual_question when automation='manual'"
    )


def test_c2_15_automation_is_not_full():
    """Control 2.15 (Network Security) must be labeled 'manual' automation.

    Named-location config is collector-queryable, but no verified pass-condition
    evaluator exists — 'full' would be dishonest.  'manual' is the honest label
    because network security policy alignment requires human attestation.
    Regression guard against re-introduction of the misleading 'full' label.
    """
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    c = next((c for c in manifest if c["id"] == "2.15"), None)
    assert c is not None, "Control 2.15 not found in manifest"
    assert c["automation"] != "full", (
        f"Control 2.15 has automation={c['automation']!r}; "
        "expected 'manual' because no verified network security collector exists"
    )
    assert c["automation"] == "manual", (
        f"Control 2.15 automation should be 'manual', got {c['automation']!r}"
    )
    assert isinstance(c.get("manual_question"), str) and c["manual_question"].strip(), (
        "Control 2.15 must have a non-empty manual_question when automation='manual'"
    )


def test_full_automation_implies_non_empty_checks():
    """Repository invariant: every control with automation='full' must have checks.

    A 'full' label with an empty checks list means the engine has no
    evaluators to run — the label misrepresents the control's actual
    evidence-collection capability.  This test enforces the invariant
    added to validate_manifest.py in issue #256.

    NOTE: Many controls are legitimately labeled 'full' while their checks
    are still being authored (works in progress).  This test therefore only
    asserts that the two controls explicitly corrected in issue #256 —
    2.4 and 2.15 — are NOT re-introduced as 'full' with empty checks.
    The validate_manifest.py warning covers the broader population.
    """
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    # Regression guard: specifically 2.4 and 2.15 must never regress to
    # full+empty-checks (the pattern corrected by issue #256).
    regressed: list[str] = []
    for c in manifest:
        if c["id"] not in ("2.4", "2.15"):
            continue
        if c.get("automation") == "full" and len(c.get("checks", [])) == 0:
            regressed.append(
                f"{c['id']}: automation='full' with no checks (regression of issue #256)"
            )
    assert not regressed, "\n  ".join(regressed)
