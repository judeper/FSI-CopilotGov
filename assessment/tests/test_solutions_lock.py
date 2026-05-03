"""Smoke test: solutions-lock + per-control mappings (Phase C1+C2)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
LOCK = ROOT / "assessment" / "data" / "solutions-lock.json"
MANIFEST = ROOT / "assessment" / "manifest" / "controls.json"

# Make scripts/ importable so we can assert against the canonical PINNED_REF
# constant rather than hardcoding a version string in the test.
sys.path.insert(0, str(ROOT / "scripts"))
import generate_solutions_lock  # noqa: E402

EXPECTED_SCHEMA = "0.1.0"
# Sister repo catalog currently lists both `19-copilot-tuning-governance`
# and `19-agent-lifecycle-governance` (a known sister-repo-internal
# duplicate, tracked as a follow-up). Update when sister deduplicates.
EXPECTED_SOLUTION_COUNT = 23
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


@pytest.fixture(scope="module")
def lock() -> dict:
    assert LOCK.exists(), f"{LOCK} not found — run scripts/generate_solutions_lock.py"
    return json.loads(LOCK.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def manifest() -> list[dict]:
    assert MANIFEST.exists(), f"{MANIFEST} not found"
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    return data


def test_lock_schema(lock: dict) -> None:
    assert lock["schemaVersion"] == EXPECTED_SCHEMA
    assert lock["source"]["repo"] == "judeper/FSI-CopilotGov-Solutions"
    assert lock["source"]["ref"] == generate_solutions_lock.PINNED_REF


def test_lock_has_all_solutions(lock: dict) -> None:
    sols = lock["solutions"]
    assert isinstance(sols, list)
    assert len(sols) == EXPECTED_SOLUTION_COUNT
    ids = [s["id"] for s in sols]
    assert len(set(ids)) == len(ids), "duplicate solution ids"
    for s in sols:
        assert SLUG_RE.match(s["id"]), s["id"]
        assert s["tier"] in (1, 2, 3), s
        assert s["name"] and s["version"] and s["domain"]
        assert s["url"].startswith("https://")


def test_every_control_has_solutions_key(manifest: list[dict]) -> None:
    for ctrl in manifest:
        assert "solutions" in ctrl, f"{ctrl.get('id')}: missing 'solutions' key"
        assert isinstance(ctrl["solutions"], list), ctrl.get("id")


def test_referential_integrity(lock: dict, manifest: list[dict]) -> None:
    lock_ids = {s["id"] for s in lock["solutions"]}
    dangling: list[tuple[str, str]] = []
    for ctrl in manifest:
        cid = ctrl.get("id", "?")
        for entry in ctrl["solutions"]:
            sid = entry if isinstance(entry, str) else entry.get("id")
            if sid and sid not in lock_ids:
                dangling.append((cid, sid))
    assert not dangling, f"controls reference solution ids absent from lock: {dangling}"


def test_primary_role_position(manifest: list[dict]) -> None:
    """First entry (when present) must be the primary solution."""
    for ctrl in manifest:
        sols = ctrl["solutions"]
        if not sols:
            continue
        first = sols[0]
        if isinstance(first, dict) and "role" in first:
            assert first["role"] == "primary", (ctrl["id"], first)
            for rest in sols[1:]:
                if isinstance(rest, dict) and "role" in rest:
                    assert rest["role"] == "supporting", (ctrl["id"], rest)


def test_bootstrap_roundtrip(tmp_path: Path) -> None:
    """Bootstrap-only path must produce byte-identical output for ``--check``.

    Pins the CI fix that lets ``generate_solutions_lock.py --check`` pass on
    runners that cannot reach the sister repo, so long as
    ``solutions-lock.bootstrap.json`` is a verbatim snapshot of a known-good
    lock. Regression guard: if a future change to the script causes
    bootstrap-derived output to diverge from the lock (e.g., always stamping
    ``kind: bootstrap``), this test will fail.
    """
    bootstrap = ROOT / "assessment" / "data" / "solutions-lock.bootstrap.json"
    if not bootstrap.exists():
        pytest.skip("no bootstrap file committed")

    # Bootstrap must mirror the lock so byte-equality holds.
    lock_text = LOCK.read_text(encoding="utf-8")
    bs_text = bootstrap.read_text(encoding="utf-8")
    assert bs_text == lock_text, (
        "bootstrap drifted from lock; regenerate with "
        "`Copy-Item assessment/data/solutions-lock.json "
        "assessment/data/solutions-lock.bootstrap.json` after lock changes."
    )

    # Force the script down the bootstrap path by pointing ``--sister-repo``
    # at a non-existent directory. ``DEFAULT_SISTER_REPO`` is captured at
    # module import, so an env-var override would be too late here.
    rc = generate_solutions_lock.main(
        ["--sister-repo", str(tmp_path / "no-sister-repo"), "--check"]
    )
    assert rc == 0, "bootstrap-only --check must succeed"
