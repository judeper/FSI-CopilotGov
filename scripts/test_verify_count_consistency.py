"""Smoke test for ``scripts/verify_count_consistency.py``.

Confirms that:
1. The verifier executes against the live tree without error (regression guard
   for stdout-encoding crashes on Windows runners).
2. The current tree is clean (exit code 0) so future drift will be caught.

Intentionally minimal — the verifier itself is small and thoroughly exercised
in CI; this test is the local smoke check pytest picks up as part of the
``python -m pytest scripts -q`` sweep documented in AGENTS.md.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_count_consistency.py"


def test_verifier_runs_clean_on_current_tree() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    assert result.returncode == 0, (
        "verify_count_consistency reported drift on the live tree.\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
    assert "PASSED" in result.stdout, result.stdout


def test_verifier_lists_allowed_counts() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    # Allowed lists should always be present in the diagnostic header.
    assert "allowed:" in result.stdout
    assert "controls=" in result.stdout
    assert "playbooks=" in result.stdout
