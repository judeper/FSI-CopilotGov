from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import merge_authored_content as merger  # noqa: E402


FORCED_45_FIELDS = (
    "verifyIn",
    "verifyPowerShell",
    "evidenceExpected",
    "facilitatorNotes",
)


FORCED_415_FIELDS = (
    "yesBar",
    "partialBar",
    "noBar",
    "sectorYesBar",
    "verifyIn",
    "evidenceExpected",
    "facilitatorNotes",
    "collectorField",
)


FORCED_311_FIELDS = (
    "yesBar",
    "evidenceExpected",
    "sectorYesBar",
)


def _load_authored() -> dict[str, dict]:
    authored_path = REPO_ROOT / "assessment" / "manifest" / "authored_content.py"
    spec = importlib.util.spec_from_file_location("authored_content", authored_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.AUTHORED


def _load_manifest_control(control_id: str) -> dict:
    manifest_path = REPO_ROOT / "assessment" / "manifest" / "controls.json"
    controls = json.loads(manifest_path.read_text(encoding="utf-8"))
    return next(control for control in controls if control.get("id") == control_id)


def _apply_overlay(control: dict, overlay: dict) -> dict:
    merged = json.loads(json.dumps(control))
    for key, override_value in overlay.items():
        existing = merged.get(key)
        force_replace = merger._should_force_replace(merged.get("id"), key)
        merged[key] = merger._merge_value(
            existing, override_value, force_replace=force_replace
        )
    return merged


def test_415_forced_fields_in_manifest_match_authored_source():
    authored_415 = _load_authored()["4.15"]
    manifest_415 = _load_manifest_control("4.15")

    for field in FORCED_415_FIELDS:
        assert manifest_415[field] == authored_415[field]


def test_45_forced_fields_in_manifest_match_authored_source():
    authored_45 = _load_authored()["4.5"]
    manifest_45 = _load_manifest_control("4.5")

    for field in FORCED_45_FIELDS:
        assert manifest_45[field] == authored_45[field]


def test_415_forced_fields_do_not_contain_obsolete_frontier_default_guidance():
    manifest_415 = _load_manifest_control("4.15")
    payload = json.dumps(
        {field: manifest_415.get(field) for field in FORCED_415_FIELDS},
        ensure_ascii=False,
    ).lower()

    for banned in (
        "frontier",
        "default-all",
        "default of all users",
        "deployment/pinning",
    ):
        assert banned not in payload


def test_control_scoped_force_replace_does_not_overwrite_unrelated_controls():
    stale_45 = {
        "id": "4.5",
        "verifyPowerShell": "stale command",
        "evidenceExpected": ["legacy"],
    }
    overlay_45 = {
        "verifyPowerShell": "Get-MgBetaReportMicrosoft365CopilotUsageUserDetail ...",
        "evidenceExpected": ["new"],
    }
    merged_45 = _apply_overlay(stale_45, overlay_45)
    assert merged_45["verifyPowerShell"] == "Get-MgBetaReportMicrosoft365CopilotUsageUserDetail ..."
    assert merged_45["evidenceExpected"] == ["new"]

    stale_415 = {
        "id": "4.15",
        "yesBar": "stale 4.15 guidance",
        "facilitatorNotes": {"ask": "stale", "followUp": "stale"},
        "collectorField": "M365Admin_CoworkGovernance",
    }
    overlay_415 = {
        "yesBar": "fresh 4.15 guidance",
        "facilitatorNotes": {"ask": "fresh", "followUp": "fresh"},
        "collectorField": "",
    }
    merged_415 = _apply_overlay(stale_415, overlay_415)
    assert merged_415["yesBar"] == "fresh 4.15 guidance"
    assert merged_415["facilitatorNotes"] == {"ask": "fresh", "followUp": "fresh"}
    assert merged_415["collectorField"] == ""

    unrelated_414 = {
        "id": "4.14",
        "yesBar": "existing authoritative guidance",
        "collectorField": "M365Admin_ScoutAccess",
    }
    overlay_414 = {"yesBar": "new guidance", "collectorField": ""}
    merged_414 = _apply_overlay(unrelated_414, overlay_414)
    assert merged_414["yesBar"] == "existing authoritative guidance"
    assert merged_414["collectorField"] == "M365Admin_ScoutAccess"


def test_311_forced_fields_in_manifest_match_authored_source():
    authored_311 = _load_authored()["3.11"]
    manifest_311 = _load_manifest_control("3.11")

    for field in FORCED_311_FIELDS:
        assert manifest_311[field] == authored_311[field]


def test_311_forced_fields_carry_corrected_sec_citation():
    manifest_311 = _load_manifest_control("3.11")
    payload = json.dumps(
        {field: manifest_311.get(field) for field in FORCED_311_FIELDS},
        ensure_ascii=False,
    )
    # The corrected Rule 17a-4(f)(2) citation and its SEC adopting release
    # must be propagated from authored_content.py into controls.json.
    assert "17a-4(f)(2)" in payload
    assert "34-96034" in payload
    # The pre-correction pinpoint must not reappear in the generated manifest.
    assert "(f)(2)(ii)(A)" not in payload


def test_311_force_replace_is_scoped_to_listed_fields_only():
    stale_311 = {
        "id": "3.11",
        "yesBar": "stale 3.11 yes bar",
        "partialBar": "hand-edited 3.11 partial bar that must survive",
    }
    overlay_311 = {
        "yesBar": "corrected 3.11 yes bar per Rule 17a-4(f)(2)",
        "partialBar": "authored partial bar that must NOT win",
    }
    merged_311 = _apply_overlay(stale_311, overlay_311)
    # yesBar is in the 3.11 force set -> authored content wins.
    assert merged_311["yesBar"] == "corrected 3.11 yes bar per Rule 17a-4(f)(2)"
    # partialBar is NOT in the 3.11 force set -> an authoritative hand edit
    # must be preserved (proves the force set is narrowly scoped).
    assert merged_311["partialBar"] == "hand-edited 3.11 partial bar that must survive"
