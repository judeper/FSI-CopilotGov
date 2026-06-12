"""Smoke test for ``scripts/verify_version_stamps.py``.

Confirms that:
1. The verifier executes against the live tree without error.
2. The current tree is clean (exit code 0 under ``--check``) so future
   footer-version drift will be caught.
3. The canonical version reported matches the repo-root ``VERSION`` file.

Intentionally minimal -- mirrors ``scripts/test_verify_count_consistency.py``;
this is the local smoke check pytest picks up as part of the
``python -m pytest assessment/tests scripts -q`` sweep documented in AGENTS.md.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_version_stamps.py"
VERSION_FILE = REPO_ROOT / "VERSION"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def test_verifier_passes_check_on_current_tree() -> None:
    result = _run("--check")
    assert result.returncode == 0, (
        "verify_version_stamps reported drift on the live tree.\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
    assert "PASS:" in result.stdout, result.stdout


def test_verifier_reports_canonical_version() -> None:
    canonical = VERSION_FILE.read_text(encoding="utf-8").strip()
    result = _run()
    assert f"Canonical version (from VERSION): {canonical}" in result.stdout, (
        result.stdout
    )
    # At least one page must carry the footer stamp, otherwise the gate is a
    # no-op and the wiring is broken.
    assert "OK (footer matches):" in result.stdout, result.stdout
