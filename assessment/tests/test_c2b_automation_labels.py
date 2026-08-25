"""Regression tests for C2b automation label corrections (OceanSquad issue #256).

Covers:
- Controls 2.4, 2.8, and 2.15 must be manual with no collection_methods
- Control 2.8 Customer Key evidence must use multi-workload policy/assignment
  cmdlets and keep Exchange-mailbox DEP evidence separate
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
CONTRACT = ROOT / "assessment" / "data" / "evidence-contract.json"
GRAPH_COLLECTOR = ROOT / "assessment" / "collectors" / "Collect-Graph.ps1"
CONTROL_28 = ROOT / "docs" / "controls" / "pillar-2-security" / "2.8-encryption.md"
PLAYBOOK_28 = ROOT / "docs" / "playbooks" / "control-implementations" / "2.8"
AUTHORED_CONTENT = ROOT / "assessment" / "manifest" / "authored_content.py"
MANIFEST_GENERATOR = ROOT / "assessment" / "manifest" / "generate_manifest.py"

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
# 2.8 — Encryption: must be manual
# ---------------------------------------------------------------------------

class TestControl28Encryption:
    def test_automation_is_manual(self):
        controls = _load_manifest()
        assert "2.8" in controls, "Control 2.8 not found in manifest"
        assert controls["2.8"]["automation"] == "manual", (
            "Control 2.8 must be manual — Graph organization metadata cannot "
            "demonstrate tenant-wide encryption"
        )

    def test_collection_methods_and_checks_are_empty(self):
        control = _load_manifest()["2.8"]
        assert control["collection_methods"] == [], (
            "Control 2.8 must not claim a collector-backed encryption check"
        )
        assert control["checks"] == [], (
            "Control 2.8 must not claim an automated encryption evaluator"
        )

    def test_manual_question_set(self):
        question = _load_manifest()["2.8"].get("manual_question")
        assert question and isinstance(question, str), (
            "Control 2.8 must retain an assessor question for its manual evidence"
        )

    def test_contract_and_graph_collector_do_not_claim_encryption_evidence(self):
        contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        mapped = [
            mapping for mapping in contract.get("mappings", [])
            if mapping.get("controlId") == "2.8"
        ]
        assert not mapped, (
            "Control 2.8 must not map unrelated Graph metadata as encryption evidence"
        )
        collector = GRAPH_COLLECTOR.read_text(encoding="utf-8")
        assert "tenant_security" + "_settings" not in collector
        assert "SecurityCompliance" + "NotificationPhones" not in collector

    def test_customer_key_evidence_is_multi_workload_and_exchange_scoped(self):
        required_sources = [
            CONTROL_28,
            PLAYBOOK_28 / "powershell-setup.md",
            PLAYBOOK_28 / "portal-walkthrough.md",
            PLAYBOOK_28 / "troubleshooting.md",
            PLAYBOOK_28 / "verification-testing.md",
            AUTHORED_CONTENT,
            MANIFEST_GENERATOR,
            MANIFEST,
        ]
        for source in required_sources:
            text = source.read_text(encoding="utf-8")
            assert "Get-M365DataAtRestEncryptionPolicy" in text, (
                f"{source} must name the multi-workload Customer Key policy cmdlet"
            )
            assert "Get-M365DataAtRestEncryptionPolicyAssignment" in text, (
                f"{source} must name the multi-workload Customer Key assignment cmdlet"
            )
            assert "multi-workload" in text.lower(), (
                f"{source} must state the multi-workload DEP scope"
            )

        for source in required_sources:
            text = source.read_text(encoding="utf-8")
            lower = text.lower()
            assert "Exchange-mailbox" in text, (
                f"{source} must distinguish Exchange-mailbox DEP evidence"
            )
            assert "Get-DataEncryptionPolicy" in text, (
                f"{source} must identify the Exchange-only DEP command"
            )
            assert any(
                phrase in lower
                for phrase in (
                    "cannot prove copilot",
                    "cannot satisfy copilot",
                    "cannot satisfy the copilot",
                    "cannot satisfy this test",
                    "cannot replace the multi-workload evidence",
                    "must not be used as evidence of copilot",
                    "not sufficient evidence for copilot",
                )
            ), (
                f"{source} must prohibit Exchange-only output from proving Copilot MDEP"
            )

    def test_customer_key_evidence_and_gesture_propagate_to_generated_manifest(self):
        manifest = _load_manifest()["2.8"]
        evidence = "\n".join(manifest.get("evidenceExpected", []))
        question = manifest.get("manual_question", "")
        assert "multi-workload" in evidence.lower()
        assert "Get-M365DataAtRestEncryptionPolicy" in evidence
        assert "Get-M365DataAtRestEncryptionPolicyAssignment" in evidence
        assert "Exchange-mailbox" in evidence
        assert "multi-workload" in question.lower()
        assert "Get-M365DataAtRestEncryptionPolicy" in question
        assert "Get-M365DataAtRestEncryptionPolicyAssignment" in question
        assert "Get-DataEncryptionPolicy" in question

        for source in [
            CONTROL_28,
            PLAYBOOK_28 / "portal-walkthrough.md",
            PLAYBOOK_28 / "verification-testing.md",
        ]:
            assert "/**" not in source.read_text(encoding="utf-8"), (
                f"{source} must use the literal '/' gesture, not '/**'"
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
