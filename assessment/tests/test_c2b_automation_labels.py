"""Regression tests for C2b automation label corrections (OceanSquad issue #256).

Covers:
- Controls 2.4 and 2.15 must be manual with no collection_methods
- The full-automation-implies-checks invariant (honest-label invariant)
- Controls 1.3, 2.12, 3.1, 3.2 must be full with non-empty checks
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "assessment" / "manifest" / "controls.json"
VALIDATE = ROOT / "scripts" / "validate_manifest.py"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_manifest() -> dict[str, dict]:
    """Return controls indexed by id."""
    with MANIFEST.open(encoding="utf-8") as fh:
        data = json.load(fh)
    controls = data if isinstance(data, list) else data.get("controls", [])
    return {c["id"]: c for c in controls if "id" in c}


def _validate_engine(c: dict) -> list[str]:
    """Import and call the engine validator from validate_manifest.py."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("validate_manifest", VALIDATE)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod._validate_engine(c)


# ---------------------------------------------------------------------------
# 2.4 — Information Barriers: must be manual
# ---------------------------------------------------------------------------

class TestControl24InformationBarriers:
    def test_automation_is_manual(self):
        controls = _load_manifest()
        assert "2.4" in controls, "Control 2.4 not found in manifest"
        assert controls["2.4"]["automation"] == "manual", (
            "Control 2.4 must be manual — no verified automated IB checks exist"
        )

    def test_collection_methods_empty(self):
        controls = _load_manifest()
        assert controls["2.4"]["collection_methods"] == [], (
            "Control 2.4 must have empty collection_methods (no collector implemented)"
        )

    def test_manual_question_set(self):
        controls = _load_manifest()
        mq = controls["2.4"].get("manual_question")
        assert mq and isinstance(mq, str), (
            "Control 2.4 must have a manual_question for facilitator use"
        )

    def test_checks_empty(self):
        controls = _load_manifest()
        assert controls["2.4"]["checks"] == [], (
            "Control 2.4 must have no automated checks (none are verified)"
        )


# ---------------------------------------------------------------------------
# 2.15 — Network Security: must be manual
# ---------------------------------------------------------------------------

class TestControl215NetworkSecurity:
    def test_automation_is_manual(self):
        controls = _load_manifest()
        assert "2.15" in controls, "Control 2.15 not found in manifest"
        assert controls["2.15"]["automation"] == "manual", (
            "Control 2.15 must be manual — no verified network security collector exists"
        )

    def test_collection_methods_empty(self):
        controls = _load_manifest()
        assert controls["2.15"]["collection_methods"] == [], (
            "Control 2.15 must have empty collection_methods"
        )

    def test_manual_question_set(self):
        controls = _load_manifest()
        mq = controls["2.15"].get("manual_question")
        assert mq and isinstance(mq, str), (
            "Control 2.15 must have a manual_question for facilitator use"
        )

    def test_checks_empty(self):
        controls = _load_manifest()
        assert controls["2.15"]["checks"] == [], (
            "Control 2.15 must have no automated checks (none are verified)"
        )


# ---------------------------------------------------------------------------
# Full-automation-implies-checks invariant
# ---------------------------------------------------------------------------

class TestFullAutomationImpliesChecksInvariant:
    """The invariant must reject full+empty-checks and accept full+non-empty-checks."""

    _MINIMAL_VALID_FULL = {
        "id": "test-full-valid",
        "title": "Test control",
        "pillar": 1,
        "automation": "full",
        "source_file": "docs/controls/pillar-1-access-governance/1.1-user-access-provisioning.md",
        "collection_methods": ["Graph_API"],
        "checks": [
            {
                "check_id": "test-check-1",
                "description": "Test check",
                "api_call": "Get-AdminAuditLogConfig",
                "pass_condition": "audit_log_enabled",
                "zone_required": [1, 2, 3],
            }
        ],
        "zone_thresholds": {
            "zone1": {"min_checks_passed": 1, "maturity_score": 1},
            "zone2": {"min_checks_passed": 1, "maturity_score": 2},
            "zone3": {"min_checks_passed": 1, "maturity_score": 4},
        },
        "manual_question": None,
    }

    _MINIMAL_FULL_NO_CHECKS = {
        "id": "test-full-no-checks",
        "title": "Test control",
        "pillar": 1,
        "automation": "full",
        "source_file": "docs/controls/pillar-1-access-governance/1.1-user-access-provisioning.md",
        "collection_methods": ["Graph_API"],
        "checks": [],
        "zone_thresholds": {
            "zone1": {"min_checks_passed": 0, "maturity_score": 0},
            "zone2": {"min_checks_passed": 0, "maturity_score": 0},
            "zone3": {"min_checks_passed": 0, "maturity_score": 0},
        },
        "manual_question": None,
    }

    def test_invariant_rejects_full_with_empty_checks(self):
        errs = _validate_engine(self._MINIMAL_FULL_NO_CHECKS)
        invariant_errs = [e for e in errs if "full" in e and "checks" in e]
        assert invariant_errs, (
            "Validator must produce an error when automation='full' and checks=[]"
        )

    def test_invariant_passes_with_checks(self):
        errs = _validate_engine(self._MINIMAL_VALID_FULL)
        invariant_errs = [e for e in errs if "full" in e and "checks" in e]
        assert not invariant_errs, (
            f"Validator must not flag automation='full' when checks is non-empty; got: {invariant_errs}"
        )

    def test_all_manifest_full_controls_have_checks(self):
        """Ensure no manifest control has automation=full with empty checks[]."""
        controls = _load_manifest()
        violations = [
            cid
            for cid, c in controls.items()
            if c.get("automation") == "full" and c.get("checks") == []
        ]
        assert not violations, (
            f"Controls with automation='full' and empty checks[]: {violations}. "
            "Correct the automation label to 'partial' or add verified checks."
        )


# ---------------------------------------------------------------------------
# 1.3, 2.12, 3.1, 3.2 — must be full with non-empty checks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("cid,evaluator", [
    ("1.3",  "grounding_sources_approved"),
    ("2.12", "no_external_sharing_on_grounding"),
    ("3.1",  "audit_log_enabled"),
    ("3.2",  "copilot_retention_policy_exists"),
])
def test_verified_full_controls_have_checks(cid: str, evaluator: str):
    controls = _load_manifest()
    assert cid in controls, f"Control {cid} not found in manifest"
    c = controls[cid]
    assert c["automation"] == "full", f"Control {cid} should be automation='full'"
    checks = c.get("checks", [])
    assert checks, f"Control {cid} must have at least one check entry"
    conditions = [ch.get("pass_condition") for ch in checks]
    assert evaluator in conditions, (
        f"Control {cid} check must use pass_condition={evaluator!r}; got {conditions}"
    )
