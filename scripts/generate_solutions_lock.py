#!/usr/bin/env python3
"""Generate ``assessment/data/solutions-lock.json`` from the sister repo.

The FSI-CopilotGov framework consumes automation solutions authored in
the companion ``FSI-CopilotGov-Solutions`` repo. This script reads that
sister repo's canonical ``solutions.json`` manifest from the configured
upstream branch and produces a committed lock file so framework builds are
reproducible even when the sister repo moves on. Refreshes resolve
``main`` from remote truth; checks validate the exact commit already
recorded in the committed lock.

Shape of the emitted lock:

.. code-block:: json

    {
      "schemaVersion": "0.2.0",
      "generatedAt": "<ISO UTC>",
      "source": {
        "repo": "judeper/FSI-CopilotGov-Solutions",
        "ref": "main",
        "commit": "<sha>"
      },
      "solutions": [ /* deep-copied from source */ ]
    }

The deep copy preserves every per-solution field, so schema 0.2.0 tier
metadata (``tiersSupported``, ``tierRecommended``, ``tierMaturity``,
``maturity``) is captured automatically without per-field handling.

The script is:

* **Configurable** — ``FSI_SOLUTIONS_REPO`` env var overrides the
  default temp cache under ``%TEMP%\\cgs-lock``. Explicit sister repos are
  never fetched; stale clones fail closed instead of silently supplying
  their local ``main``.
* **Graceful** — if the sister repo is not present, a bootstrap file
  at ``assessment/data/solutions-lock.bootstrap.json`` is used as a
  ``--check`` fallback (useful for CI or fresh checkouts). The bootstrap
  mirrors the lock shape — typically a verbatim snapshot of a known-good
  ``solutions-lock.json`` — so its ``source`` block (including
  ``kind: sister-repo``) round-trips byte-for-byte through ``--check``.
* **Idempotent** — pass ``--now <ISO timestamp>`` for byte-identical
  output in tests. When reading a lock file that already exists, the
  prior ``generatedAt`` is reused so re-running after a no-op change
  does not churn the commit.
"""
from __future__ import annotations

import argparse
import copy
import datetime as _dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK_OUT = ROOT / "assessment" / "data" / "solutions-lock.json"
BOOTSTRAP = ROOT / "assessment" / "data" / "solutions-lock.bootstrap.json"

DEFAULT_SISTER_REPO = (
    Path(os.environ["FSI_SOLUTIONS_REPO"])
    if os.environ.get("FSI_SOLUTIONS_REPO")
    else None
)
SISTER_REPO_SLUG = "judeper/FSI-CopilotGov-Solutions"
SISTER_REMOTE_URL = f"https://github.com/{SISTER_REPO_SLUG}.git"
# Sister manifest schema consumed by the framework. Bumped 0.1.0 -> 0.2.0
# when the sister repo added per-solution tier metadata (tiersSupported,
# tierRecommended, tierMaturity, maturity) between v0.7.0 and v0.8.0.
EXPECTED_SCHEMA = "0.2.0"
# The upstream ref that the framework targets. The scheduled drift workflow
# checks the sister repository's main branch, so the refresh generator must
# read the same ref to resolve reported drift without hand-editing the lock.
PINNED_REF = "main"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def _run(cwd: Path | None, *args: str) -> str | None:
    try:
        out = subprocess.check_output(
            [*args],
            cwd=str(cwd) if cwd is not None else None,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.decode("utf-8", errors="replace").strip() or None


def _run_ok(cwd: Path | None, *args: str) -> bool:
    try:
        subprocess.check_call(
            [*args],
            cwd=str(cwd) if cwd is not None else None,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return False
    return True


def _git(sister_repo: Path, *args: str) -> str | None:
    return _run(sister_repo, "git", *args)


def _is_sha(value: str | None) -> bool:
    return bool(isinstance(value, str) and SHA_RE.fullmatch(value))


def _require_sha(value: str | None, label: str) -> str:
    if not _is_sha(value):
        raise SystemExit(f"ERROR: {label} must be a 40-character commit SHA (got {value!r}).")
    return value


def _resolve_remote_ref(ref: str = PINNED_REF) -> str:
    """Resolve the remote commit SHA for ``ref`` from GitHub, not a local clone."""
    api = _run(None, "gh", "api", f"repos/{SISTER_REPO_SLUG}/commits/{ref}", "--jq", ".sha")
    if _is_sha(api):
        return api

    ls_remote = _run(None, "git", "ls-remote", SISTER_REMOTE_URL, ref)
    if ls_remote:
        sha = ls_remote.split()[0]
        if _is_sha(sha):
            return sha

    raise SystemExit(
        f"ERROR: could not resolve remote {SISTER_REPO_SLUG}@{ref}. "
        "Authenticate GitHub CLI or ensure git can reach the remote."
    )


def _resolve_local_ref(sister_repo: Path, ref: str = PINNED_REF) -> str | None:
    """Resolve the commit SHA of ``ref`` in a local sister repo.

    Uses ``rev-list -n 1`` so annotated tags dereference to their target
    commit (``rev-parse`` would return the tag object SHA instead).
    """
    return _git(sister_repo, "rev-list", "-n", "1", ref)


def _commit_exists(sister_repo: Path, commit: str) -> bool:
    return _run_ok(sister_repo, "git", "cat-file", "-e", f"{commit}^{{commit}}")


def _temp_cache_repo() -> Path:
    return Path(tempfile.gettempdir()) / "cgs-lock" / "FSI-CopilotGov-Solutions"


def _ensure_temp_cache() -> Path:
    """Fetch sister ``main`` into a private temp cache and return its path."""
    repo = _temp_cache_repo()
    if repo.exists() and not (repo / ".git").exists():
        shutil.rmtree(repo)
    repo.mkdir(parents=True, exist_ok=True)
    if not (repo / ".git").exists():
        if not _run_ok(repo, "git", "init"):
            raise SystemExit(f"ERROR: could not initialize temp sister cache at {repo}.")
        if not _run_ok(repo, "git", "remote", "add", "origin", SISTER_REMOTE_URL):
            raise SystemExit(f"ERROR: could not configure temp sister cache at {repo}.")

    fetched = _run_ok(
        repo,
        "git",
        "fetch",
        "--prune",
        "origin",
        f"+refs/heads/{PINNED_REF}:refs/remotes/origin/{PINNED_REF}",
    )
    if not fetched:
        raise SystemExit(
            f"ERROR: could not fetch {SISTER_REPO_SLUG}@{PINNED_REF} into temp cache {repo}."
        )
    return repo


def _read_solutions_json_at_commit(sister_repo: Path, commit: str) -> str:
    """Return raw ``solutions.json`` text for an exact commit SHA.

    The working tree and local branch name are intentionally ignored. If the
    repo does not contain ``commit``, generation fails closed rather than
    silently substituting local ``main``.
    """
    _require_sha(commit, "source.commit")
    if not sister_repo.exists():
        raise FileNotFoundError(sister_repo)
    if not _commit_exists(sister_repo, commit):
        raise SystemExit(
            f"ERROR: sister repo at {sister_repo} does not contain required commit "
            f"{commit}. Refusing to read local {PINNED_REF}; update that clone or omit "
            "--sister-repo so the generator can use its temp cache."
        )
    pinned = _git(sister_repo, "show", f"{commit}:solutions.json")
    if pinned is None:
        raise SystemExit(f"ERROR: {commit}:solutions.json is not readable in {sister_repo}.")
    return pinned


def _load_source_solutions(
    sister_repo: Path | None,
    target_commit: str,
    *,
    require_local_ref: bool,
    allow_bootstrap_on_fetch_error: bool,
) -> list[dict]:
    """Return solutions from the exact sister commit.

    Refreshes require an explicit local clone's ``main`` to equal the remote
    target; checks allow ``main`` to have moved and validate the recorded SHA.

    Raises ``FileNotFoundError`` if an explicit sister repo is missing.
    """
    target_commit = _require_sha(target_commit, "target commit")
    source_repo = sister_repo
    if source_repo is None:
        try:
            source_repo = _ensure_temp_cache()
        except SystemExit as exc:
            if allow_bootstrap_on_fetch_error:
                raise FileNotFoundError(_temp_cache_repo()) from exc
            raise

    if require_local_ref:
        local_ref = _resolve_local_ref(source_repo)
        if local_ref != target_commit:
            raise SystemExit(
                f"ERROR: local {source_repo}@{PINNED_REF} is {local_ref or '<missing>'}, "
                f"but remote {SISTER_REPO_SLUG}@{PINNED_REF} is {target_commit}. "
                "Refusing to generate from a stale or divergent local clone."
            )

    data = json.loads(_read_solutions_json_at_commit(source_repo, target_commit))
    sv = data.get("schemaVersion")
    if sv != EXPECTED_SCHEMA:
        raise SystemExit(
            f"ERROR: sister repo solutions.json schemaVersion is {sv!r}, "
            f"expected {EXPECTED_SCHEMA!r}."
        )
    sols = data.get("solutions")
    if not isinstance(sols, list) or not sols:
        raise SystemExit("ERROR: sister repo solutions.json has no solutions[].")
    return copy.deepcopy(sols)


def _load_bootstrap() -> tuple[list[dict], dict] | None:
    """Return ``(solutions, source)`` from the bootstrap, or ``None`` if absent.

    The bootstrap file mirrors the ``solutions-lock.json`` shape so it can be
    a verbatim snapshot of a known-good lock. ``source.kind`` is preserved
    when present so byte-for-byte ``--check`` succeeds in CI environments
    that cannot reach the sister repo.
    """
    if not BOOTSTRAP.exists():
        return None
    data = json.loads(BOOTSTRAP.read_text(encoding="utf-8"))
    sols = data.get("solutions") or []
    src = data.get("source") or {}
    return copy.deepcopy(sols), copy.deepcopy(src)


def _prior_generated_at(out_path: Path) -> str | None:
    if not out_path.exists():
        return None
    try:
        prior = json.loads(out_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    ts = prior.get("generatedAt")
    return ts if isinstance(ts, str) else None


def _recorded_commit(out_path: Path) -> str | None:
    if not out_path.exists():
        return None
    try:
        prior = json.loads(out_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    source = prior.get("source") if isinstance(prior, dict) else None
    commit = source.get("commit") if isinstance(source, dict) else None
    return commit if isinstance(commit, str) else None


def build_lock(
    sister_repo: Path | None,
    now: str | None,
    out_path: Path,
    *,
    check: bool = False,
) -> dict:
    if check and out_path.exists():
        target_commit = _require_sha(_recorded_commit(out_path), f"{out_path} source.commit")
        require_local_ref = False
    else:
        target_commit = _resolve_remote_ref(PINNED_REF)
        require_local_ref = sister_repo is not None

    try:
        solutions = _load_source_solutions(
            sister_repo,
            target_commit,
            require_local_ref=require_local_ref,
            allow_bootstrap_on_fetch_error=check and sister_repo is None,
        )
        source = {
            "repo": SISTER_REPO_SLUG,
            "ref": PINNED_REF,
            "commit": target_commit,
            "kind": "sister-repo",
        }
    except FileNotFoundError:
        if not check:
            raise SystemExit(
                f"ERROR: sister repo not found at {sister_repo}. Omit --sister-repo "
                "to use the temp cache, or point it at a clone that has remote main."
            )
        bootstrap = _load_bootstrap()
        if bootstrap is None:
            raise SystemExit(
                f"ERROR: sister repo not found at {sister_repo} and no "
                f"bootstrap file at {BOOTSTRAP}. Set FSI_SOLUTIONS_REPO "
                f"or provide a bootstrap lock."
            )
        solutions, bs_source = bootstrap
        # Preserve the bootstrap's recorded source so a snapshot of a
        # sister-repo-derived lock round-trips byte-for-byte through
        # ``--check``. Defaults fill in for older minimal bootstraps that
        # only carried ``commit``.
        bootstrap_commit = bs_source.get("commit") or ""
        if bootstrap_commit:
            _require_sha(bootstrap_commit, f"{BOOTSTRAP} source.commit")
        source = {
            "repo": bs_source.get("repo") or SISTER_REPO_SLUG,
            "ref": bs_source.get("ref") or PINNED_REF,
            "commit": bootstrap_commit,
            "kind": bs_source.get("kind") or "bootstrap",
        }
        print(f"WARN: using bootstrap lock ({BOOTSTRAP}) — sister repo not present.")

    if now is None:
        # For idempotency, reuse the prior timestamp when the payload is
        # otherwise unchanged. A first-ever write uses the current UTC
        # time.
        prior_ts = _prior_generated_at(out_path)
        now = prior_ts or _dt.datetime.now(_dt.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        )

    lock = {
        "schemaVersion": EXPECTED_SCHEMA,
        "generatedAt": now,
        "source": source,
        "solutions": solutions,
    }
    return lock


def _stable_dumps(payload: dict) -> str:
    """Serialize with sorted keys + 2-space indent for byte-identical output."""
    return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sister-repo",
        type=Path,
        default=DEFAULT_SISTER_REPO,
        help=(
            "Optional path to an existing FSI-CopilotGov-Solutions checkout. "
            "The generator never fetches this path; omit it to use the temp cache."
        ),
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=LOCK_OUT,
        help=f"Output path (default: {LOCK_OUT}).",
    )
    parser.add_argument(
        "--now",
        type=str,
        default=None,
        help="ISO UTC timestamp to stamp as generatedAt (for reproducible tests).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit non-zero if the emitted lock differs from --out.",
    )
    args = parser.parse_args(argv)

    lock = build_lock(args.sister_repo, args.now, args.out, check=args.check)
    payload = _stable_dumps(lock)

    existing = args.out.read_text(encoding="utf-8") if args.out.exists() else ""

    if args.check:
        if existing != payload:
            print(
                f"ERROR: {args.out} is out of date; re-run "
                f"'python scripts/generate_solutions_lock.py'.",
                file=sys.stderr,
            )
            return 1
        print(f"OK: {args.out} is up to date ({len(lock['solutions'])} solutions).")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(payload, encoding="utf-8")
    action = "unchanged" if existing == payload else "written"
    print(
        f"{action}: {args.out} ({len(lock['solutions'])} solutions, "
        f"ref={lock['source']['ref']}, commit={lock['source']['commit'][:12] or '<none>'})."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
