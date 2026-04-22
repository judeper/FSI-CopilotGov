#!/usr/bin/env python3
"""Generate ``assessment/data/solutions-lock.json`` from the sister repo.

The FSI-CopilotGov framework consumes automation solutions authored in
the companion ``FSI-CopilotGov-Solutions`` repo. This script reads that
sister repo's canonical ``solutions.json`` manifest and produces a
committed lock file so framework builds are reproducible even when the
sister repo moves on.

Shape of the emitted lock:

.. code-block:: json

    {
      "schemaVersion": "0.1.0",
      "generatedAt": "<ISO UTC>",
      "source": {
        "repo": "judeper/FSI-CopilotGov-Solutions",
        "ref": "v0.5.0",
        "commit": "<sha>"
      },
      "solutions": [ /* deep-copied from source */ ]
    }

The script is:

* **Configurable** — ``FSI_SOLUTIONS_REPO`` env var overrides the
  default path ``C:\\dev\\FSI-CopilotGov-Solutions``.
* **Graceful** — if the sister repo is not present, a bootstrap file
  at ``assessment/data/solutions-lock.bootstrap.json`` is used as a
  fallback (useful for CI or fresh checkouts).
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
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK_OUT = ROOT / "assessment" / "data" / "solutions-lock.json"
BOOTSTRAP = ROOT / "assessment" / "data" / "solutions-lock.bootstrap.json"

DEFAULT_SISTER_REPO = Path(
    os.environ.get("FSI_SOLUTIONS_REPO", r"C:\dev\FSI-CopilotGov-Solutions")
)
SISTER_REPO_SLUG = "judeper/FSI-CopilotGov-Solutions"
EXPECTED_SCHEMA = "0.1.0"
# The pinned ref that the v1.4 framework targets. Update in lock-step
# with the sister repo release cadence.
PINNED_REF = "v0.5.0"


def _git(sister_repo: Path, *args: str) -> str | None:
    try:
        out = subprocess.check_output(
            ["git", *args],
            cwd=str(sister_repo),
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.decode("utf-8", errors="replace").strip() or None


def _resolve_commit(sister_repo: Path) -> str | None:
    """Resolve the commit SHA of the pinned ref in the sister repo.

    Uses ``rev-list -n 1`` so annotated tags dereference to their target
    commit (``rev-parse`` would return the tag object SHA instead).
    """
    return _git(sister_repo, "rev-list", "-n", "1", PINNED_REF)


def _load_source_solutions(sister_repo: Path) -> tuple[list[dict], str | None]:
    """Return (solutions list, resolved commit) from the sister repo.

    Raises ``FileNotFoundError`` if the sister repo is missing.
    """
    src = sister_repo / "solutions.json"
    if not src.exists():
        raise FileNotFoundError(src)
    data = json.loads(src.read_text(encoding="utf-8"))
    sv = data.get("schemaVersion")
    if sv != EXPECTED_SCHEMA:
        raise SystemExit(
            f"ERROR: sister repo solutions.json schemaVersion is {sv!r}, "
            f"expected {EXPECTED_SCHEMA!r}."
        )
    sols = data.get("solutions")
    if not isinstance(sols, list) or not sols:
        raise SystemExit("ERROR: sister repo solutions.json has no solutions[].")
    return copy.deepcopy(sols), _resolve_commit(sister_repo)


def _load_bootstrap() -> tuple[list[dict], str | None] | None:
    if not BOOTSTRAP.exists():
        return None
    data = json.loads(BOOTSTRAP.read_text(encoding="utf-8"))
    sols = data.get("solutions") or []
    commit = (data.get("source") or {}).get("commit")
    return copy.deepcopy(sols), commit


def _prior_generated_at(out_path: Path) -> str | None:
    if not out_path.exists():
        return None
    try:
        prior = json.loads(out_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    ts = prior.get("generatedAt")
    return ts if isinstance(ts, str) else None


def build_lock(
    sister_repo: Path,
    now: str | None,
    out_path: Path,
) -> dict:
    try:
        solutions, commit = _load_source_solutions(sister_repo)
        source_kind = "sister-repo"
    except FileNotFoundError:
        bootstrap = _load_bootstrap()
        if bootstrap is None:
            raise SystemExit(
                f"ERROR: sister repo not found at {sister_repo} and no "
                f"bootstrap file at {BOOTSTRAP}. Set FSI_SOLUTIONS_REPO "
                f"or provide a bootstrap lock."
            )
        solutions, commit = bootstrap
        source_kind = "bootstrap"
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
        "source": {
            "repo": SISTER_REPO_SLUG,
            "ref": PINNED_REF,
            "commit": commit or "",
            "kind": source_kind,
        },
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
        help=f"Path to the FSI-CopilotGov-Solutions checkout (default: {DEFAULT_SISTER_REPO}).",
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

    lock = build_lock(args.sister_repo, args.now, args.out)
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
