"""Manifest honesty invariants (issues #257 and #324).

The manifest must not claim more evidence automation than the collectors can
actually deliver, and must not advertise regulatory guidance that the control
doc has since superseded.

Issue #324 reconciled two independent derivations of the ``automation`` label
(PR #359 and PR #367) into a single canonical definition: a label is the
INTERSECTION of a contract-mapped collector and a wired evaluator. The
end-to-end assertions for that definition live in
:func:`test_full_automation_is_the_intersection_of_collector_and_evaluator`
and :func:`test_partial_automation_means_collector_without_evaluator`.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "assessment" / "manifest" / "controls.json"
CONTRACT = REPO_ROOT / "assessment" / "data" / "evidence-contract.json"

_spec = importlib.util.spec_from_file_location(
    "validate_manifest", REPO_ROOT / "scripts" / "validate_manifest.py"
)
validate_manifest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate_manifest)

_score_spec = importlib.util.spec_from_file_location(
    "score", REPO_ROOT / "assessment" / "engine" / "score.py"
)
score = importlib.util.module_from_spec(_score_spec)
_score_spec.loader.exec_module(score)


def _controls() -> list[dict]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def _contract_fields() -> dict[str, str]:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for m in data.get("mappings", []) or []:
        cid, field = m.get("controlId"), m.get("collectorField")
        if cid and field and cid not in out:
            out[cid] = field
    return out


def test_non_manual_automation_requires_a_collector_binding() -> None:
    contract = _contract_fields()
    overclaiming = [
        c["id"]
        for c in _controls()
        if c.get("automation") in ("full", "partial") and c["id"] not in contract
    ]
    assert not overclaiming, (
        "controls claim automated evidence with no evidence-contract mapping: "
        f"{overclaiming}"
    )


def test_collector_field_matches_the_evidence_contract() -> None:
    contract = _contract_fields()
    mismatched = {
        c["id"]: (c.get("collectorField"), contract.get(c["id"], ""))
        for c in _controls()
        if (c.get("collectorField") or "") != contract.get(c["id"], "")
    }
    assert not mismatched, f"collectorField disagrees with the contract: {mismatched}"


def test_validator_rejects_an_overclaimed_automation_label() -> None:
    errs = validate_manifest._validate_against_contract(
        [{"id": "9.9", "automation": "full", "collectorField": ""}], {}
    )
    assert any("must be 'manual'" in e for e in errs)


# ---------------------------------------------------------------------------
# Canonical automation taxonomy (issue #324) — reconciling PR #359 with PR #367
#
# full    = contract-mapped collector AND wired evaluator (the intersection)
# partial = contract-mapped collector, no wired evaluator
# manual  = neither
#
# Under-claiming is permitted (2.4 / 2.15 are mapped but stay manual because no
# trustworthy automated pass/fail exists); over-claiming is not.
# ---------------------------------------------------------------------------


def test_full_automation_is_the_intersection_of_collector_and_evaluator() -> None:
    contract = _contract_fields()
    offenders = {
        c["id"]: {
            "contract_mapped": c["id"] in contract,
            "checks": len(c.get("checks") or []),
        }
        for c in _controls()
        if c.get("automation") == "full"
        and not (c["id"] in contract and (c.get("checks") or []))
    }
    assert not offenders, (
        "automation='full' requires BOTH an evidence-contract mapping and a "
        f"non-empty checks[]; offenders: {offenders}"
    )


def test_partial_automation_means_collector_without_evaluator() -> None:
    """``partial`` must be contract-mapped; a wired evaluator makes it ``full``."""
    contract = _contract_fields()
    unmapped = [
        c["id"] for c in _controls()
        if c.get("automation") == "partial" and c["id"] not in contract
    ]
    assert not unmapped, f"partial controls with no contract mapping: {unmapped}"

    understated = [
        c["id"] for c in _controls()
        if c.get("automation") == "partial" and (c.get("checks") or [])
    ]
    assert not understated, (
        f"partial controls that already wire an evaluator: {understated} — "
        "these satisfy the intersection and should be labelled 'full'"
    )


def test_manual_automation_carries_no_wired_evaluator() -> None:
    wired = [
        c["id"] for c in _controls()
        if c.get("automation") == "manual" and (c.get("checks") or [])
    ]
    assert not wired, (
        f"manual controls that wire an evaluator: {wired} — a control the engine "
        "can evaluate must not be labelled 'manual'"
    )


def test_both_halves_of_the_definition_are_enforced_by_the_validator() -> None:
    """The two invariants must compose; neither alone defines ``full``."""
    # Half (B): a contract-mapped control with an empty checks[] is caught by
    # _validate_engine. Derive the fixture from a real 'full' control so the
    # test tracks the engine schema instead of duplicating it.
    donor = next(c for c in _controls() if c.get("automation") == "full")
    no_checks = dict(donor)
    no_checks["id"] = "9.9"
    no_checks["checks"] = []
    engine_errs = validate_manifest._validate_engine(no_checks)
    assert any("requires at least one entry in checks[]" in e for e in engine_errs), (
        f"expected the full-implies-checks invariant to fire; got: {engine_errs}"
    )

    # Half (A): wired checks[] but no contract mapping is caught by the
    # contract cross-check, so a control cannot buy 'full' with checks alone.
    contract_errs = validate_manifest._validate_against_contract(
        [{"id": "9.9", "automation": "full", "collectorField": ""}], {}
    )
    assert any("must be 'manual'" in e for e in contract_errs)


def test_documented_under_claims_stay_manual() -> None:
    """2.4 / 2.15 are contract-mapped yet deliberately manual (PR #359).

    They keep the contract's ``collectorField`` because the Graph collector
    really does emit that data — the label reflects the absence of a trusted
    pass/fail evaluator, not the absence of evidence.
    """
    contract = _contract_fields()
    by_id = {c["id"]: c for c in _controls()}
    for cid in ("2.4", "2.15"):
        c = by_id[cid]
        assert c["automation"] == "manual", f"{cid} must stay 'manual' (PR #359)"
        assert not (c.get("checks") or []), f"{cid} must have no wired evaluator"
        assert c.get("collectorField") == contract[cid], (
            f"{cid} must still advertise the contract's collector field"
        )


def test_validator_rejects_an_orphan_collector_field() -> None:
    errs = validate_manifest._validate_against_contract(
        [{"id": "9.9", "automation": "manual", "collectorField": "Ghost_Field"}], {}
    )
    assert any("disagrees with" in e for e in errs)


def test_collection_methods_resolve_only_to_real_collector_sources() -> None:
    """Methods with no collector must resolve to None, not borrow another source."""
    for method in ("M365Admin", "Teams", "VivaInsights", "Defender", "Manual"):
        assert score.COLLECTION_METHOD_SOURCE[method] is None, (
            f"{method} has no collector but resolves to "
            f"{score.COLLECTION_METHOD_SOURCE[method]!r}"
        )
    for method, src in score.COLLECTION_METHOD_SOURCE.items():
        if src is not None:
            assert src in score.SOURCE_FILENAMES, f"{method} -> unknown source {src!r}"


def test_manifest_collection_methods_are_known_tokens() -> None:
    unknown = {
        c["id"]: m
        for c in _controls()
        for m in (c.get("collection_methods") or [])
        if m not in score.COLLECTION_METHOD_SOURCE
    }
    assert not unknown, f"unknown collection_methods tokens: {unknown}"


def test_manual_controls_carry_an_assessor_question() -> None:
    """A manual control with no question is invisible to the engine's
    ``needs_manual`` flag, so downgrading automation must not lose the ask."""
    missing = [
        c["id"]
        for c in _controls()
        if c.get("automation") == "manual" and not (c.get("manual_question") or "").strip()
    ]
    assert not missing, f"manual controls without a manual_question: {missing}"


def test_model_risk_controls_tag_the_superseding_guidance() -> None:
    """3.8 / 3.8a docs cite SR 26-2 / OCC 2026-13; the manifest must say so."""
    by_id = {c["id"]: c for c in _controls()}
    for cid in ("3.8", "3.8a"):
        tags = set(by_id[cid].get("regulatory") or [])
        assert {"SR-26-2", "OCC-2026-13"} <= tags, (
            f"{cid} advertises superseded model-risk guidance only: {sorted(tags)}"
        )


def test_sr_11_7_is_always_paired_with_its_occ_counterpart() -> None:
    for c in _controls():
        tags = set(c.get("regulatory") or [])
        if "SR-11-7" in tags:
            assert "OCC-2011-12" in tags, (
                f"{c['id']} cites SR 11-7 without OCC Bulletin 2011-12"
            )
