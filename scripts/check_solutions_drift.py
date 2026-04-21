#!/usr/bin/env python3
"""Detect drift between ``assessment/data/solutions-lock.json`` and the
upstream sister repo's ``solutions.json``.

The lock file is intentionally pinned to a specific ref of the sister
repo (``FSI-CopilotGov-Solutions``). This script compares the pinned
lock against whatever the sister repo currently has on disk and flags
differences so governance owners can decide when to re-pin.

Drift categories
----------------

* ``ADDED``           — solutions present upstream but missing in the lock.
* ``REMOVED``         — solutions present in the lock but missing upstream.
* ``VERSION_BUMP``    — same id in both, but ``version`` differs.
* ``FIELD_CHANGE``    — same id + version, but another compared field
  (``name``, ``summary``, ``domain``, ``url``, ``tier``, ``slug``,
  ``repoPath``) differs.
* ``COVERAGE_ORPHAN`` — solution in the lock but no control in the
  manifest references it.
* ``COVERAGE_DANGLING`` — a control in the manifest references a
  solution ID that is not in the lock. This is a hard error: the
  generator + validator prevent it, but we re-check at drift time.

Modes
-----

* ``--mode=full`` (default): report every category; exit 0 unless a
  dangling coverage reference is found.
* ``--mode=ci``: exit non-zero only on ``REMOVED`` or
  ``COVERAGE_DANGLING``. ``ADDED`` / ``VERSION_BUMP`` / ``FIELD_CHANGE``
  / ``COVERAGE_ORPHAN`` emit warnings (exit 0) because the lock is
  deliberately pinned.

Sister repo location is controlled by ``FSI_SOLUTIONS_REPO`` (matches
``generate_solutions_lock.py``).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LOCK_DEFAULT = ROOT / "assessment" / "data" / "solutions-lock.json"
MANIFEST_DEFAULT = ROOT / "assessment" / "manifest" / "controls.json"

DEFAULT_SISTER_REPO = Path(
    os.environ.get("FSI_SOLUTIONS_REPO", r"C:\dev\FSI-CopilotGov-Solutions")
)

COMPARED_FIELDS = ("name", "summary", "domain", "url", "tier", "slug", "repoPath")

# Exit codes
EXIT_OK = 0
EXIT_DRIFT = 1


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _solutions_by_id(items: list[dict]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for item in items or []:
        if isinstance(item, dict) and isinstance(item.get("id"), str):
            out[item["id"]] = item
    return out


def _parse_semver(v: str) -> tuple[int, int, int, str]:
    """Return a comparable tuple for a bare or pre-release semver.

    Pre-release suffix sorts lower than no-suffix per SemVer §11.
    """
    core = v
    pre = ""
    for sep in ("-", "+"):
        if sep in core:
            core, pre = core.split(sep, 1)
            break
    try:
        major, minor, patch = (int(p) for p in core.split("."))
    except (ValueError, AttributeError):
        return (0, 0, 0, v)
    # Empty pre-release sorts higher than any non-empty one.
    pre_key = pre if pre else "~"
    return (major, minor, patch, pre_key)


def _version_direction(old: str, new: str) -> str:
    if old == new:
        return "same"
    return "up" if _parse_semver(new) > _parse_semver(old) else "down"


def _manifest_coverage(manifest_path: Path) -> dict[str, list[str]]:
    """Return ``{solution_id: [control_id, ...]}`` references from the manifest."""
    coverage: dict[str, list[str]] = {}
    if not manifest_path.exists():
        return coverage
    data = _load_json(manifest_path)
    if not isinstance(data, list):
        return coverage
    for ctrl in data:
        if not isinstance(ctrl, dict):
            continue
        cid = str(ctrl.get("id", "?"))
        for entry in ctrl.get("solutions", []) or []:
            if isinstance(entry, str):
                sid = entry
            elif isinstance(entry, dict):
                sid = entry.get("id", "")
            else:
                continue
            if sid:
                coverage.setdefault(sid, []).append(cid)
    return coverage


def _upstream_path(sister_repo: Path) -> Path:
    return sister_repo / "solutions.json"


def compute_drift(
    lock: dict,
    upstream: dict,
    coverage: dict[str, list[str]],
) -> dict[str, list[dict]]:
    """Return a report dict keyed by drift category."""
    lock_by_id = _solutions_by_id(lock.get("solutions") or [])
    upstream_by_id = _solutions_by_id(upstream.get("solutions") or [])

    report: dict[str, list[dict]] = {
        "ADDED": [],
        "REMOVED": [],
        "VERSION_BUMP": [],
        "FIELD_CHANGE": [],
        "COVERAGE_ORPHAN": [],
        "COVERAGE_DANGLING": [],
    }

    for sid in sorted(set(upstream_by_id) - set(lock_by_id)):
        up = upstream_by_id[sid]
        report["ADDED"].append(
            {
                "id": sid,
                "version": up.get("version"),
                "name": up.get("name"),
            }
        )

    for sid in sorted(set(lock_by_id) - set(upstream_by_id)):
        lk = lock_by_id[sid]
        report["REMOVED"].append(
            {
                "id": sid,
                "version": lk.get("version"),
                "name": lk.get("name"),
            }
        )

    for sid in sorted(set(lock_by_id) & set(upstream_by_id)):
        lk = lock_by_id[sid]
        up = upstream_by_id[sid]
        old_v = lk.get("version", "")
        new_v = up.get("version", "")
        if old_v != new_v:
            report["VERSION_BUMP"].append(
                {
                    "id": sid,
                    "from": old_v,
                    "to": new_v,
                    "direction": _version_direction(old_v, new_v),
                }
            )
            continue
        changes: dict[str, dict] = {}
        for field in COMPARED_FIELDS:
            if lk.get(field) != up.get(field):
                changes[field] = {"from": lk.get(field), "to": up.get(field)}
        if changes:
            report["FIELD_CHANGE"].append({"id": sid, "changes": changes})

    # Coverage orphans: solutions in lock with no manifest reference.
    for sid in sorted(lock_by_id):
        if sid not in coverage:
            report["COVERAGE_ORPHAN"].append({"id": sid})

    # Coverage dangling: manifest references not in lock (should be zero).
    for sid in sorted(coverage):
        if sid not in lock_by_id:
            report["COVERAGE_DANGLING"].append(
                {"id": sid, "referencedBy": sorted(set(coverage[sid]))}
            )

    return report


def _summarize(report: dict[str, list[dict]]) -> dict[str, int]:
    return {k: len(v) for k, v in report.items()}


def _has_blocking(report: dict[str, list[dict]]) -> bool:
    return bool(report["COVERAGE_DANGLING"]) or bool(report["REMOVED"])


def _has_any(report: dict[str, list[dict]]) -> bool:
    return any(report[k] for k in report)


def _print_human(report: dict[str, list[dict]], *, mode: str, source: dict) -> None:
    counts = _summarize(report)
    print(f"Solutions drift report (mode={mode})")
    print(f"  Lock source : {source.get('repo')}@{source.get('ref')}")
    print(f"  Upstream    : {source.get('upstreamPath')}")
    print("  Summary     : " + ", ".join(f"{k}={v}" for k, v in counts.items()))

    def _section(label: str, rows: list[dict], fmt) -> None:
        if not rows:
            return
        print(f"\n{label} ({len(rows)})")
        for row in rows:
            print(f"  - {fmt(row)}")

    _section(
        "ADDED (upstream has new solutions not in lock)",
        report["ADDED"],
        lambda r: f"{r['id']} v{r.get('version')} — {r.get('name')}",
    )
    _section(
        "REMOVED (lock has solutions no longer upstream)",
        report["REMOVED"],
        lambda r: f"{r['id']} v{r.get('version')} — {r.get('name')}",
    )
    _section(
        "VERSION_BUMP",
        report["VERSION_BUMP"],
        lambda r: f"{r['id']}: {r['from']} -> {r['to']} ({r['direction']})",
    )

    def _fmt_field(r: dict) -> str:
        changes = ", ".join(
            f"{f}: {c['from']!r} -> {c['to']!r}" for f, c in r["changes"].items()
        )
        return f"{r['id']}: {changes}"

    _section("FIELD_CHANGE", report["FIELD_CHANGE"], _fmt_field)
    _section(
        "COVERAGE_ORPHAN (solution in lock but unreferenced by controls)",
        report["COVERAGE_ORPHAN"],
        lambda r: r["id"],
    )
    _section(
        "COVERAGE_DANGLING (control references a solution not in lock)",
        report["COVERAGE_DANGLING"],
        lambda r: f"{r['id']} referenced by {r['referencedBy']}",
    )

    if not _has_any(report):
        print("\nNo drift detected.")


def run(
    *,
    lock_path: Path,
    manifest_path: Path,
    sister_repo: Path,
    mode: str,
    emit_json: bool,
    stdout=sys.stdout,
    stderr=sys.stderr,
) -> int:
    if not lock_path.exists():
        print(f"ERROR: lock not found at {lock_path}", file=stderr)
        return EXIT_DRIFT
    upstream_path = _upstream_path(sister_repo)
    if not upstream_path.exists():
        print(
            f"ERROR: upstream solutions.json not found at {upstream_path}. "
            "Set FSI_SOLUTIONS_REPO to the sister repo checkout.",
            file=stderr,
        )
        return EXIT_DRIFT

    lock = _load_json(lock_path)
    upstream = _load_json(upstream_path)
    coverage = _manifest_coverage(manifest_path)

    report = compute_drift(lock, upstream, coverage)

    source = {
        "repo": (lock.get("source") or {}).get("repo"),
        "ref": (lock.get("source") or {}).get("ref"),
        "commit": (lock.get("source") or {}).get("commit"),
        "upstreamPath": str(upstream_path),
    }

    if emit_json:
        payload = {
            "mode": mode,
            "source": source,
            "summary": _summarize(report),
            "drift": report,
            "hasDrift": _has_any(report),
            "hasBlocking": _has_blocking(report),
        }
        print(json.dumps(payload, indent=2, sort_keys=True), file=stdout)
    else:
        _print_human(report, mode=mode, source=source)

    if mode == "ci":
        return EXIT_DRIFT if _has_blocking(report) else EXIT_OK
    # full mode: treat only dangling coverage refs as hard failure.
    return EXIT_DRIFT if report["COVERAGE_DANGLING"] else EXIT_OK


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lock", type=Path, default=LOCK_DEFAULT)
    parser.add_argument("--manifest", type=Path, default=MANIFEST_DEFAULT)
    parser.add_argument(
        "--sister-repo",
        type=Path,
        default=DEFAULT_SISTER_REPO,
        help="Path to the FSI-CopilotGov-Solutions checkout.",
    )
    parser.add_argument("--mode", choices=("full", "ci"), default="full")
    parser.add_argument(
        "--json",
        dest="emit_json",
        action="store_true",
        help="Emit a machine-readable JSON report instead of prose.",
    )
    args = parser.parse_args(argv)
    return run(
        lock_path=args.lock,
        manifest_path=args.manifest,
        sister_repo=args.sister_repo,
        mode=args.mode,
        emit_json=args.emit_json,
    )


if __name__ == "__main__":
    sys.exit(main())
