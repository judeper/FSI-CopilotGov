"""Smoke test: build and validate the canonical content graph."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = REPO_ROOT / "assessment" / "manifest" / "content-graph.json"
BUILD_SCRIPT = REPO_ROOT / "scripts" / "build_content_graph.py"
VALIDATE_SCRIPT = REPO_ROOT / "scripts" / "validate_content_graph.py"

EXPECTED = {
    "controls": 63,
    "pillars": 4,
    "by_pillar": {"1": 16, "2": 17, "3": 15, "4": 15},
    "playbooks_total": 268,
    "playbooks_control": 249,
    "playbooks_cross_cutting": 19,
    "solutions": 23,
}


def _run(script: Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(script), *extra],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def test_build_content_graph_emits_expected_counts() -> None:
    # Use --check (non-mutating): it asserts the committed graph matches a fresh
    # filesystem walk without rewriting the tracked file, so running the test
    # suite never dirties the working tree. The committed graph is then the
    # subject of the explicit-literal tripwire below.
    result = _run(BUILD_SCRIPT, "--check")
    assert result.returncode == 0, (
        f"committed content-graph.json is stale or build failed: "
        f"{result.stderr}\n{result.stdout}"
    )
    assert GRAPH_PATH.is_file(), "content-graph.json was not written"

    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    counts = graph["counts"]
    for key, expected in EXPECTED.items():
        assert counts.get(key) == expected, (
            f"counts.{key}: expected {expected}, got {counts.get(key)}"
        )


def test_validate_content_graph_passes() -> None:
    result = _run(VALIDATE_SCRIPT)
    assert result.returncode == 0, (
        f"validation failed: {result.stderr}\n{result.stdout}"
    )
