"""Validation tests for monitoring keyword-to-control mappings."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import pytest
import yaml

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

import monitoring_shared  # noqa: E402

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


def test_learn_url_control_map_control_ids_exist_in_manifest():
    config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    manifest_titles = _load_manifest_titles()
    missing = []

    for entry in config.get("learn", {}).get("url_control_map", []):
        url = entry.get("url")
        for control_id in entry.get("controls", []):
            if control_id not in manifest_titles:
                missing.append(f"{url}: {control_id}")

    assert not missing, (
        "learn.url_control_map references control IDs missing from controls.json:\n"
        + "\n".join(missing)
    )


def test_load_monitoring_config_fails_fast_for_unknown_learn_override_control(tmp_path, capsys):
    config = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    config["learn"]["url_control_map"] = list(config["learn"].get("url_control_map", []))
    config["learn"]["url_control_map"].append(
        {
            "url": "https://learn.microsoft.com/en-us/example/bad",
            "controls": ["9.99"],
        }
    )
    temp_config = tmp_path / "monitoring-config.yaml"
    temp_config.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")

    with pytest.raises(SystemExit) as excinfo:
        monitoring_shared.load_monitoring_config(temp_config)

    assert excinfo.value.code == 2
    captured = capsys.readouterr()
    assert "learn.url_control_map" in captured.out
    assert "9.99" in captured.out
