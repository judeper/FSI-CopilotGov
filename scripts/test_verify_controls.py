"""Tests for ``scripts/verify_controls.py``.

Covers two things:

1. The pure ``verify_control`` function correctly separates missing *required*
   sections (errors) from missing *recommended* sections (warnings).
2. Regression guard for the reporting bug where the summary counted warnings
   (``Warnings: N``) but never printed which control/section triggered them:
   any counted warning must have a corresponding printed detail line, so the
   count and the emitted detail are never inconsistent.

Intentionally minimal, matching the style of the other ``scripts/test_*.py``
smoke tests picked up by ``python -m pytest scripts -q``.
"""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_controls.py"

_spec = importlib.util.spec_from_file_location("verify_controls", SCRIPT)
verify_controls = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(verify_controls)

_COMPLETE = """# Control X

Control ID: X.1
Pillar: 1
Last Verified: 2026-01-01

## Objective
## Why This Matters for FSI
## Control Description
## Verification Criteria
## Additional Resources
## Copilot Surface Coverage
## Governance Levels
## Setup & Configuration
## Financial Sector Considerations
"""


def test_complete_control_has_no_errors_or_warnings(tmp_path: Path) -> None:
    f = tmp_path / "complete.md"
    f.write_text(_COMPLETE, encoding="utf-8")
    errors, warnings = verify_controls.verify_control(str(f))
    assert errors == []
    assert warnings == []


def test_missing_recommended_section_is_a_warning_not_error(tmp_path: Path) -> None:
    body = _COMPLETE.replace("## Financial Sector Considerations\n", "")
    f = tmp_path / "recommended-missing.md"
    f.write_text(body, encoding="utf-8")
    errors, warnings = verify_controls.verify_control(str(f))
    assert errors == []
    assert any("Financial Sector Considerations" in w for w in warnings)


def test_missing_required_section_is_an_error(tmp_path: Path) -> None:
    body = _COMPLETE.replace("## Verification Criteria\n", "")
    f = tmp_path / "required-missing.md"
    f.write_text(body, encoding="utf-8")
    errors, warnings = verify_controls.verify_control(str(f))
    assert any("Verification Criteria" in e for e in errors)


def test_summary_warning_count_matches_printed_detail_lines() -> None:
    """Guard: the reported ``Warnings: N`` count must never exceed the number
    of printed warning detail lines. Prior to the fix the count was tracked but
    the detail lines were dropped, so a maintainer saw a bare count with no
    way to locate the offending control."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    m = re.search(r"^Warnings:\s*(\d+)", result.stdout, re.MULTILINE)
    assert m is not None, result.stdout
    reported = int(m.group(1))

    # Detail lines are the indented "  Missing recommended section: ..." entries
    # printed under each "WARNINGS in <file>:" header.
    printed = len(re.findall(r"^\s+Missing recommended section:", result.stdout, re.MULTILINE))
    assert printed == reported, (
        f"summary counted {reported} warning(s) but printed {printed} detail "
        f"line(s); counts and detail must stay in sync.\nstdout:\n{result.stdout}"
    )
