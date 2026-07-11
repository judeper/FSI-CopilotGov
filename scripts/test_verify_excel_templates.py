"""Smoke and guard tests for ``scripts/verify_excel_templates.py``."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "verify_excel_templates.py"
MANIFEST = REPO_ROOT / "assessment" / "manifest" / "controls.json"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import verify_excel_templates as vet  # noqa: E402


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


def test_verify_excel_templates_passes_on_current_tree() -> None:
    result = _run()
    assert result.returncode == 0, (
        "verify_excel_templates reported errors on the live tree.\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )
    assert "[PASS] All" in result.stdout, result.stdout


def test_verify_file_rejects_non_zip_placeholder() -> None:
    placeholder = REPO_ROOT / "assessment" / "templates" / "_placeholder-test.xlsx"
    placeholder.write_text("placeholder\n", encoding="utf-8")
    try:
        errors = vet.verify_file(placeholder, expected_count=0, is_dashboard=False)
        assert any("not a valid OOXML" in e for e in errors), errors
    finally:
        if placeholder.exists():
            placeholder.unlink()


def test_required_role_control_rows_are_present() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    counts = vet.expected_counts(manifest)
    templates_dir = REPO_ROOT / "assessment" / "templates"

    for filename, required_ids in vet.REQUIRED_ROLE_CONTROL_IDS.items():
        path = templates_dir / filename
        errors = vet.verify_file(
            path,
            expected_count=counts[filename],
            is_dashboard=False,
            required_ids=required_ids,
        )
        assert not errors, f"{filename} verification errors: {errors}"
