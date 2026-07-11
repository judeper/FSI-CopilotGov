"""Validation tests for monitoring keyword-to-control mappings."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
CONFIG_PATH = REPO_ROOT / "scripts" / "config" / "monitoring-config.yaml"
CONTROLS_PATH = REPO_ROOT / "assessment" / "manifest" / "controls.json"


def _load_manifest_titles() -> dict[str, str]:
    controls = json.loads(CONTROLS_PATH.read_text(encoding="utf-8"))
    return {control["id"]: control["title"] for control in controls}


def test_keyword_control_map_control_ids_exist_in_manifest():
    config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    manifest_titles = _load_manifest_titles()
    missing = []

    for entry in config.get("keyword_control_map", []):
        keyword = entry.get("keyword")
        for control in entry.get("controls", []):
            control_id = control.get("id")
            if control_id not in manifest_titles:
                missing.append(f"{keyword}: {control_id}")

    assert not missing, (
        "monitoring-config.yaml references control IDs missing from controls.json:\n"
        + "\n".join(missing)
    )


def test_keyword_control_map_control_names_match_manifest_titles():
    config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    manifest_titles = _load_manifest_titles()
    mismatches = []

    for entry in config.get("keyword_control_map", []):
        keyword = entry.get("keyword")
        for control in entry.get("controls", []):
            control_id = control.get("id")
            configured_name = control.get("name")
            expected = manifest_titles.get(control_id)
            if expected is None:
                continue
            if configured_name != expected:
                mismatches.append(
                    f"{keyword}: {control_id} -> '{configured_name}' != '{expected}'"
                )

    assert not mismatches, (
        "monitoring-config.yaml control names do not match controls.json titles:\n"
        + "\n".join(mismatches)
    )
