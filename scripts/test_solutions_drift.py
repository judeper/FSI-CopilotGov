"""Tests for ``scripts/check_solutions_drift.py``.

Each scenario builds a synthetic sister repo + lock + manifest on disk
and invokes the drift script as a subprocess to validate exit codes
and JSON output.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent / "check_solutions_drift.py"


def _sol(
    sid: str,
    *,
    version: str = "0.1.0",
    name: str | None = None,
    domain: str = "readiness-data",
    tier: int = 1,
) -> dict:
    return {
        "id": sid,
        "slug": sid,
        "tier": tier,
        "name": name or f"Solution {sid}",
        "version": version,
        "domain": domain,
        "summary": f"Summary for {sid}.",
        "repoPath": f"solutions/{sid}",
        "url": f"https://example.invalid/{sid}",
        "prerequisites": [],
        "verification": [],
    }


def _write(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _make_fixture(tmp_path: Path, lock_sols, upstream_sols, manifest_sols):
    sister = tmp_path / "sister"
    _write(sister / "solutions.json", {"schemaVersion": "0.1.0", "solutions": upstream_sols})
    lock_path = tmp_path / "solutions-lock.json"
    _write(
        lock_path,
        {
            "schemaVersion": "0.1.0",
            "generatedAt": "2026-04-21T22:00:40Z",
            "source": {
                "repo": "judeper/FSI-CopilotGov-Solutions",
                "ref": "v0.1.0-rc1",
                "commit": "",
            },
            "solutions": lock_sols,
        },
    )
    controls = [
        {"id": ctrl_id, "solutions": [{"id": sid, "tier": 1, "role": "primary"} for sid in sids]}
        for ctrl_id, sids in manifest_sols.items()
    ]
    manifest_path = tmp_path / "controls.json"
    _write(manifest_path, controls)
    return sister, lock_path, manifest_path


def _run(sister, lock_path, manifest_path, *args):
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--lock",
            str(lock_path),
            "--manifest",
            str(manifest_path),
            "--sister-repo",
            str(sister),
            "--json",
            *args,
        ],
        capture_output=True,
        text=True,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else None
    return proc, payload


def test_no_drift_clean(tmp_path: Path):
    sols = [_sol("01-alpha"), _sol("02-beta")]
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=sols,
        upstream_sols=[dict(s) for s in sols],
        manifest_sols={"1.1": ["01-alpha"], "1.2": ["02-beta"]},
    )
    proc, payload = _run(sister, lock, manifest, "--mode=full")
    assert proc.returncode == 0, proc.stderr
    assert payload["hasDrift"] is False
    assert payload["summary"]["COVERAGE_DANGLING"] == 0
    assert payload["summary"]["ADDED"] == 0

    proc_ci, payload_ci = _run(sister, lock, manifest, "--mode=ci")
    assert proc_ci.returncode == 0
    assert payload_ci["hasBlocking"] is False


def test_version_bump_warns_but_passes_ci(tmp_path: Path):
    lock_sols = [_sol("01-alpha", version="0.2.0")]
    upstream_sols = [_sol("01-alpha", version="0.3.0")]
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=lock_sols,
        upstream_sols=upstream_sols,
        manifest_sols={"1.1": ["01-alpha"]},
    )
    proc, payload = _run(sister, lock, manifest, "--mode=ci")
    assert proc.returncode == 0, proc.stderr
    assert payload["summary"]["VERSION_BUMP"] == 1
    bump = payload["drift"]["VERSION_BUMP"][0]
    assert bump["id"] == "01-alpha"
    assert bump["from"] == "0.2.0"
    assert bump["to"] == "0.3.0"
    assert bump["direction"] == "up"
    assert payload["hasBlocking"] is False


def test_coverage_dangling_blocks_ci(tmp_path: Path):
    lock_sols = [_sol("01-alpha")]
    upstream_sols = [_sol("01-alpha")]
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=lock_sols,
        upstream_sols=upstream_sols,
        # Manifest references a ghost solution id.
        manifest_sols={"1.1": ["01-alpha"], "1.2": ["99-ghost"]},
    )
    proc_ci, payload_ci = _run(sister, lock, manifest, "--mode=ci")
    assert proc_ci.returncode != 0
    assert payload_ci["summary"]["COVERAGE_DANGLING"] == 1
    dangling = payload_ci["drift"]["COVERAGE_DANGLING"][0]
    assert dangling["id"] == "99-ghost"
    assert dangling["referencedBy"] == ["1.2"]

    # Full mode also fails on dangling refs.
    proc_full, _ = _run(sister, lock, manifest, "--mode=full")
    assert proc_full.returncode != 0


def test_coverage_orphan_never_blocks(tmp_path: Path):
    # 02-beta is in the lock + upstream but no control references it.
    lock_sols = [_sol("01-alpha"), _sol("02-beta")]
    upstream_sols = [dict(s) for s in lock_sols]
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=lock_sols,
        upstream_sols=upstream_sols,
        manifest_sols={"1.1": ["01-alpha"]},
    )
    proc, payload = _run(sister, lock, manifest, "--mode=ci")
    assert proc.returncode == 0, proc.stderr
    assert payload["summary"]["COVERAGE_ORPHAN"] == 1
    assert payload["drift"]["COVERAGE_ORPHAN"][0]["id"] == "02-beta"
    assert payload["hasBlocking"] is False

    proc_full, payload_full = _run(sister, lock, manifest, "--mode=full")
    assert proc_full.returncode == 0
    assert payload_full["summary"]["COVERAGE_ORPHAN"] == 1


def test_removed_blocks_ci(tmp_path: Path):
    lock_sols = [_sol("01-alpha"), _sol("02-beta")]
    upstream_sols = [_sol("01-alpha")]  # 02-beta removed upstream
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=lock_sols,
        upstream_sols=upstream_sols,
        manifest_sols={"1.1": ["01-alpha"], "1.2": ["02-beta"]},
    )
    proc_ci, payload_ci = _run(sister, lock, manifest, "--mode=ci")
    assert proc_ci.returncode != 0
    assert payload_ci["summary"]["REMOVED"] == 1


def test_added_is_warning_only(tmp_path: Path):
    lock_sols = [_sol("01-alpha")]
    upstream_sols = [_sol("01-alpha"), _sol("02-beta")]
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=lock_sols,
        upstream_sols=upstream_sols,
        manifest_sols={"1.1": ["01-alpha"]},
    )
    proc, payload = _run(sister, lock, manifest, "--mode=ci")
    assert proc.returncode == 0, proc.stderr
    assert payload["summary"]["ADDED"] == 1
    assert payload["drift"]["ADDED"][0]["id"] == "02-beta"


def test_field_change_detected(tmp_path: Path):
    lock_sols = [_sol("01-alpha", name="Old Name")]
    upstream_sols = [_sol("01-alpha", name="New Name")]
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=lock_sols,
        upstream_sols=upstream_sols,
        manifest_sols={"1.1": ["01-alpha"]},
    )
    proc, payload = _run(sister, lock, manifest, "--mode=ci")
    assert proc.returncode == 0, proc.stderr
    assert payload["summary"]["FIELD_CHANGE"] == 1
    change = payload["drift"]["FIELD_CHANGE"][0]
    assert change["id"] == "01-alpha"
    assert "name" in change["changes"]
    assert change["changes"]["name"]["to"] == "New Name"


def test_human_readable_no_drift(tmp_path: Path):
    sols = [_sol("01-alpha")]
    sister, lock, manifest = _make_fixture(
        tmp_path,
        lock_sols=sols,
        upstream_sols=[dict(s) for s in sols],
        manifest_sols={"1.1": ["01-alpha"]},
    )
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--lock",
            str(lock),
            "--manifest",
            str(manifest),
            "--sister-repo",
            str(sister),
            "--mode=full",
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert "No drift detected." in proc.stdout


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
