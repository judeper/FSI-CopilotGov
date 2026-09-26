"""Tests for ``scripts/generate_solutions_lock.py`` determinism."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import generate_solutions_lock  # noqa: E402


def _git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        [
            "git",
            "-c",
            "user.name=Test User",
            "-c",
            "user.email=test@example.invalid",
            *args,
        ],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


def _write_solutions(repo: Path, version: str) -> None:
    payload = {
        "schemaVersion": generate_solutions_lock.EXPECTED_SCHEMA,
        "solutions": [
            {
                "id": "01-alpha",
                "slug": "01-alpha",
                "version": version,
            }
        ],
    }
    (repo / "solutions.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _commit_solutions(repo: Path, version: str) -> str:
    _write_solutions(repo, version)
    _git(repo, "add", "solutions.json")
    _git(repo, "commit", "-m", f"solutions {version}")
    return _git(repo, "rev-parse", "HEAD")


def _make_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "sister"
    repo.mkdir()
    _git(repo, "init", "-b", "main")
    return repo


def test_refresh_records_remote_main_sha(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    repo = _make_repo(tmp_path)
    _commit_solutions(repo, "0.1.0")
    head = _commit_solutions(repo, "0.2.0")
    monkeypatch.setattr(generate_solutions_lock, "_resolve_remote_ref", lambda ref: head)

    lock = generate_solutions_lock.build_lock(
        repo,
        "2026-09-26T19:00:00Z",
        tmp_path / "solutions-lock.json",
    )

    assert lock["source"]["ref"] == "main"
    assert lock["source"]["commit"] == head
    assert len(lock["source"]["commit"]) == 40
    assert lock["solutions"][0]["version"] == "0.2.0"


def test_refresh_rejects_stale_explicit_sister_clone(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    repo = _make_repo(tmp_path)
    _commit_solutions(repo, "0.1.0")
    stale = tmp_path / "stale-sister"
    shutil.copytree(repo, stale)
    remote_head = _commit_solutions(repo, "0.2.0")
    monkeypatch.setattr(generate_solutions_lock, "_resolve_remote_ref", lambda ref: remote_head)

    with pytest.raises(SystemExit, match="Refusing to generate from a stale"):
        generate_solutions_lock.build_lock(
            stale,
            "2026-09-26T19:00:00Z",
            tmp_path / "solutions-lock.json",
        )


def test_check_uses_recorded_sha_not_current_local_main(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    repo = _make_repo(tmp_path)
    recorded = _commit_solutions(repo, "0.1.0")
    monkeypatch.setattr(generate_solutions_lock, "_resolve_remote_ref", lambda ref: recorded)
    lock_path = tmp_path / "solutions-lock.json"
    lock = generate_solutions_lock.build_lock(
        repo,
        "2026-09-26T19:00:00Z",
        lock_path,
    )
    lock_path.write_text(generate_solutions_lock._stable_dumps(lock), encoding="utf-8")

    _commit_solutions(repo, "0.2.0")

    rc = generate_solutions_lock.main(
        ["--sister-repo", str(repo), "--out", str(lock_path), "--check"]
    )

    assert rc == 0
