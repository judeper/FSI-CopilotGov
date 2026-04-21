"""Smoke tests for the FSI-CopilotGov assessment engine.

These tests verify that ``assessment/engine/score.py``:

* loads the live ``assessment/manifest/controls.json`` manifest
* runs end-to-end against an empty collected/ directory
* scores all 58 controls without crashing
* produces a well-formed scores.json envelope

A separate test suite (extensible) covers per-evaluator semantics with
hand-built fixtures.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_DIR = REPO_ROOT / "assessment" / "engine"
MANIFEST = REPO_ROOT / "assessment" / "manifest" / "controls.json"

sys.path.insert(0, str(ENGINE_DIR))
import score as score_mod  # noqa: E402


def test_manifest_exists_and_has_58_controls():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) == 58


@pytest.mark.parametrize("zone", [1, 2, 3])
def test_engine_runs_against_empty_collected_dir(tmp_path, zone):
    collected = tmp_path / "collected"
    collected.mkdir()
    output = tmp_path / "scores.json"

    result = score_mod.run(
        manifest_path=str(MANIFEST),
        collected_dir=str(collected),
        zone=zone,
        output_path=str(output),
    )

    assert output.is_file()
    assert result["_metadata"]["total_controls"] == 58
    assert result["_metadata"]["zone"] == zone
    # All controls scored; auto+manual must equal total
    assert (
        result["_metadata"]["auto_scored"]
        + result["_metadata"]["needs_manual"]
        == 58
    )
    # Average maturity is a float in [0, 4]
    avg = result["summary"]["average_maturity"]
    assert 0.0 <= avg <= 4.0
    # Per-pillar distribution is exactly 16/16/13/13
    by_pillar = result["summary"]["by_pillar"]
    assert by_pillar["1"]["controls"] == 16
    assert by_pillar["2"]["controls"] == 16
    assert by_pillar["3"]["controls"] == 13
    assert by_pillar["4"]["controls"] == 13


def test_engine_handles_envelope_shape(tmp_path):
    """The engine must accept both a flat-list manifest and an envelope shape."""
    envelope = {
        "version": "test-1.0",
        "controls": [
            {
                "id": "1.1",
                "title": "Test",
                "pillar": 1,
                "pillar_name": "Readiness",
                "automation": "manual",
                "checks": [],
                "collection_methods": [],
                "zone_thresholds": {
                    "zone1": {"min_checks_passed": 0, "maturity_score": 0},
                    "zone2": {"min_checks_passed": 0, "maturity_score": 0},
                    "zone3": {"min_checks_passed": 0, "maturity_score": 0},
                },
            }
        ],
    }
    manifest = tmp_path / "envelope.json"
    manifest.write_text(json.dumps(envelope), encoding="utf-8")
    collected = tmp_path / "collected"
    collected.mkdir()
    output = tmp_path / "scores.json"

    result = score_mod.run(
        manifest_path=str(manifest),
        collected_dir=str(collected),
        zone=1,
        output_path=str(output),
    )
    assert result["_metadata"]["total_controls"] == 1
    assert result["_metadata"]["manifest_version"] == "test-1.0"


def test_compute_maturity_threshold_logic():
    thresholds = {
        "zone1": {"min_checks_passed": 0, "maturity_score": 1},
        "zone2": {"min_checks_passed": 3, "maturity_score": 2},
        "zone3": {"min_checks_passed": 5, "maturity_score": 3},
    }
    score, label, _ = score_mod.compute_maturity(2, 2, thresholds)
    assert score == 0  # below threshold
    score, label, _ = score_mod.compute_maturity(3, 2, thresholds)
    assert score == 2
    assert label == "Recommended"
    score, _, _ = score_mod.compute_maturity(5, 3, thresholds)
    assert score == 3
