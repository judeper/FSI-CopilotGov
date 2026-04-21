#!/usr/bin/env python3
"""Validate ``assessment/data/solutions-lock.json``.

This file is produced by ``scripts/generate_solutions_lock.py`` from
the sister repo ``FSI-CopilotGov-Solutions``. It is committed in-repo
so framework builds are reproducible.

Rules enforced:

* top-level ``schemaVersion`` equals ``"0.1.0"``.
* top-level ``generatedAt`` is an ISO-8601 UTC timestamp.
* top-level ``source`` has ``repo``, ``ref``, ``commit`` (commit may
  be empty string if sister repo git metadata was unavailable).
* ``solutions`` is a non-empty list.
* every solution has required fields: ``id``, ``slug``, ``tier``
  (int in {1,2,3}), ``name``, ``version`` (bare semver),
  ``domain``, ``summary``, ``repoPath``, ``url``.
* IDs/slugs are unique and kebab-case.

Cross-check (warning only): every solution ID referenced by a control
in ``assessment/manifest/controls.json`` should resolve in the lock.

Exit code: 0 if lock is valid; 1 otherwise.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
LOCK_DEFAULT = ROOT / "assessment" / "data" / "solutions-lock.json"
MANIFEST_DEFAULT = ROOT / "assessment" / "manifest" / "controls.json"

EXPECTED_SCHEMA = "0.1.0"
ALLOWED_TIERS = {1, 2, 3}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
ISO_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

REQUIRED_SOLUTION_FIELDS = (
    "id",
    "slug",
    "tier",
    "name",
    "version",
    "domain",
    "summary",
    "repoPath",
    "url",
)


def _validate_solution(idx: int, body: Any) -> list[str]:
    errs: list[str] = []
    if not isinstance(body, dict):
        return [f"solutions[{idx}] must be an object"]
    sid = body.get("id", f"<#{idx}>")
    for f in REQUIRED_SOLUTION_FIELDS:
        if f not in body:
            errs.append(f"solutions[{sid}] missing field '{f}'")

    if "id" in body and not (isinstance(body["id"], str) and SLUG_RE.match(body["id"])):
        errs.append(f"solutions[{sid}].id must match {SLUG_RE.pattern}")
    if "slug" in body and not (
        isinstance(body["slug"], str) and SLUG_RE.match(body["slug"])
    ):
        errs.append(f"solutions[{sid}].slug must match {SLUG_RE.pattern}")
    if "id" in body and "slug" in body and body["id"] != body["slug"]:
        errs.append(f"solutions[{sid}].id and .slug must match")

    tier = body.get("tier")
    if tier not in ALLOWED_TIERS:
        errs.append(
            f"solutions[{sid}].tier must be int in {sorted(ALLOWED_TIERS)} (got {tier!r})"
        )
    ver = body.get("version")
    if not (isinstance(ver, str) and SEMVER_RE.match(ver)):
        errs.append(f"solutions[{sid}].version must be bare semver (got {ver!r})")
    url = body.get("url")
    if not (isinstance(url, str) and url.startswith(("http://", "https://"))):
        errs.append(f"solutions[{sid}].url must be http(s) (got {url!r})")
    repo_path = body.get("repoPath")
    if not (isinstance(repo_path, str) and repo_path):
        errs.append(f"solutions[{sid}].repoPath must be non-empty string")

    return errs


def _cross_check(lock_ids: set[str], manifest_path: Path) -> list[str]:
    if not manifest_path.exists():
        return []
    try:
        controls = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if not isinstance(controls, list):
        return []
    missing: dict[str, list[str]] = {}
    for ctrl in controls:
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
            if sid and sid not in lock_ids:
                missing.setdefault(sid, []).append(cid)
    return [
        f"solution {sid!r} referenced by controls {sorted(set(cs))} is not in the lock"
        for sid, cs in sorted(missing.items())
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lock", type=Path, default=LOCK_DEFAULT)
    parser.add_argument("--manifest", type=Path, default=MANIFEST_DEFAULT)
    args = parser.parse_args(argv)

    if not args.lock.exists():
        print(f"ERROR: lock not found at {args.lock}", file=sys.stderr)
        return 1

    try:
        lock = json.loads(args.lock.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"ERROR: lock is not valid JSON: {exc}", file=sys.stderr)
        return 1

    errs: list[str] = []

    sv = lock.get("schemaVersion")
    if sv != EXPECTED_SCHEMA:
        errs.append(f"schemaVersion must be {EXPECTED_SCHEMA!r} (got {sv!r})")

    ts = lock.get("generatedAt")
    if not (isinstance(ts, str) and ISO_UTC_RE.match(ts)):
        errs.append(f"generatedAt must be ISO-8601 UTC (got {ts!r})")

    src = lock.get("source")
    if not isinstance(src, dict):
        errs.append("source must be an object")
    else:
        for f in ("repo", "ref", "commit"):
            if f not in src or not isinstance(src[f], str):
                errs.append(f"source.{f} missing or not a string")

    sols = lock.get("solutions")
    lock_ids: set[str] = set()
    if not isinstance(sols, list) or not sols:
        errs.append("solutions must be a non-empty list")
    else:
        seen: set[str] = set()
        for idx, body in enumerate(sols):
            errs.extend(_validate_solution(idx, body))
            if isinstance(body, dict) and isinstance(body.get("id"), str):
                sid = body["id"]
                if sid in seen:
                    errs.append(f"solutions[{sid}] duplicate id")
                seen.add(sid)
                lock_ids.add(sid)

    warns = _cross_check(lock_ids, args.manifest)

    for w in warns:
        print(f"WARN: {w}")
    for e in errs:
        print(f"ERROR: {e}", file=sys.stderr)

    if errs:
        print(f"\nFAIL: {len(errs)} error(s), {len(warns)} warning(s).", file=sys.stderr)
        return 1

    print(
        f"OK: solutions-lock.json valid "
        f"({len(lock_ids)} solutions, {len(warns)} warning(s))."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
