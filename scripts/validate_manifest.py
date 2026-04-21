#!/usr/bin/env python3
"""Validate ``assessment/manifest/controls.json`` for FSI-CopilotGov.

Two layers of checks:

1. **Engine schema (always strict)** — id/title/pillar/source_file/
   automation/collection_methods/checks/zone_thresholds/manual_question
   structure, control count, ID uniqueness, source-file existence,
   pillar membership.

2. **SPA-extension schema (lenient)** — name, zonesApplicable, roles,
   regulatory, priority, yesBar, partialBar, noBar, verifyIn,
   verifyPowerShell, evidenceExpected, controlDocUrl, portalPlaybookUrl,
   collectorField, sectorYesBar, facilitatorNotes, solutions. These are
   harvested by ``scripts/harvest_manifest_extension.py`` (Phase A2);
   missing values are warnings unless ``--strict`` is passed.

Modes:

* default — engine errors fail; missing SPA fields are warnings.
* ``--strict`` — every missing SPA field is an error (Phase A2 done).
* ``--allow-todo`` — when ``--strict`` is on, ``TODO:`` placeholders in
  authored content fields are downgraded to warnings.

Exit code: 0 if no errors; 1 otherwise.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DEFAULT = ROOT / "assessment" / "manifest" / "controls.json"
DOCS_BASE = ROOT / "docs"

EXPECTED_COUNT = 58
EXPECTED_BY_PILLAR = {1: 16, 2: 16, 3: 13, 4: 13}
PILLARS = {1, 2, 3, 4}
AUTOMATION_VALUES = {"full", "partial", "manual"}

ENGINE_REQUIRED = (
    "id",
    "title",
    "pillar",
    "pillar_name",
    "source_file",
    "automation",
    "collection_methods",
    "checks",
    "zone_thresholds",
    "manual_question",
)

SPA_REQUIRED = (
    "name",
    "zonesApplicable",
    "roles",
    "regulatory",
    "priority",
    "yesBar",
    "partialBar",
    "noBar",
    "verifyIn",
    "verifyPowerShell",
    "evidenceExpected",
    "controlDocUrl",
    "portalPlaybookUrl",
    "collectorField",
    "sectorYesBar",
    "facilitatorNotes",
    "solutions",
)

PRIORITY_VALUES = {"critical", "high", "medium", "low"}
SECTORS = {
    "bank",
    "broker-dealer",
    "investment-adviser",
    "insurance-carrier",
    "insurance-wholesale",
    "credit-union",
    "holding-company",
    "other",
}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
URL_RE = re.compile(r"^https?://", re.IGNORECASE)
ZONE_KEY_RE = re.compile(r"^zone[123]$")


def _is_todo(v: Any) -> bool:
    return isinstance(v, str) and v.strip().startswith("TODO:")


def _validate_engine(c: dict) -> list[str]:
    errs: list[str] = []
    cid = c.get("id", "<missing-id>")

    for k in ENGINE_REQUIRED:
        if k not in c:
            errs.append(f"{cid}: engine field '{k}' missing")

    if errs:
        return errs

    if c["pillar"] not in PILLARS:
        errs.append(f"{cid}: pillar must be in {sorted(PILLARS)}")

    if c["automation"] not in AUTOMATION_VALUES:
        errs.append(
            f"{cid}: automation must be one of {sorted(AUTOMATION_VALUES)} "
            f"(got {c['automation']!r})"
        )

    methods = c["collection_methods"]
    if not isinstance(methods, list) or not all(isinstance(m, str) for m in methods):
        errs.append(f"{cid}: collection_methods must be a list of strings")

    src = c["source_file"]
    if not isinstance(src, str) or not src.startswith("docs/controls/"):
        errs.append(f"{cid}: source_file must start with 'docs/controls/'")
    elif not (DOCS_BASE.parent / src).exists():
        errs.append(f"{cid}: source_file does not exist on disk: {src}")

    checks = c["checks"]
    if not isinstance(checks, list):
        errs.append(f"{cid}: checks must be a list")
    else:
        for i, ch in enumerate(checks):
            if not isinstance(ch, dict):
                errs.append(f"{cid}: checks[{i}] must be an object")
                continue
            for sub in ("check_id", "description", "api_call", "pass_condition", "zone_required"):
                if sub not in ch:
                    errs.append(f"{cid}: checks[{i}].{sub} missing")
            zr = ch.get("zone_required")
            if not (isinstance(zr, list) and zr and all(z in (1, 2, 3) for z in zr)):
                errs.append(f"{cid}: checks[{i}].zone_required must be subset of [1,2,3]")

    zt = c["zone_thresholds"]
    if not isinstance(zt, dict):
        errs.append(f"{cid}: zone_thresholds must be an object")
    else:
        missing = {"zone1", "zone2", "zone3"} - set(zt.keys())
        if missing:
            errs.append(f"{cid}: zone_thresholds missing keys: {sorted(missing)}")
        for k, v in zt.items():
            if not ZONE_KEY_RE.match(k):
                errs.append(f"{cid}: zone_thresholds key {k!r} not in zone1/2/3")
                continue
            if not isinstance(v, dict):
                errs.append(f"{cid}: zone_thresholds.{k} must be an object")
                continue
            for sub in ("min_checks_passed", "maturity_score"):
                if sub not in v or not isinstance(v[sub], int):
                    errs.append(f"{cid}: zone_thresholds.{k}.{sub} missing/not int")

    mq = c["manual_question"]
    if mq is not None and not isinstance(mq, str):
        errs.append(f"{cid}: manual_question must be string or null")

    return errs


def _validate_spa(c: dict, strict: bool, allow_todo: bool) -> tuple[list[str], list[str]]:
    """Return (errs, warns). In non-strict mode all SPA findings are warnings."""
    errs: list[str] = []
    warns: list[str] = []
    cid = c.get("id", "<missing-id>")

    def add(msg: str, *, severity: str = "field") -> None:
        """severity 'field' = degraded by --strict; 'todo' = downgraded by --allow-todo."""
        if severity == "todo":
            if strict and not allow_todo:
                errs.append(msg)
            else:
                warns.append(msg)
            return
        # severity 'field'
        if strict:
            errs.append(msg)
        else:
            warns.append(msg)

    for k in SPA_REQUIRED:
        if k not in c:
            add(f"{cid}: SPA field '{k}' missing")

    if any(k not in c for k in SPA_REQUIRED):
        # Skip deep checks if structure incomplete
        return errs, warns

    z = c["zonesApplicable"]
    if not (isinstance(z, list) and z and all(v in (1, 2, 3) for v in z)):
        add(f"{cid}: zonesApplicable must be a non-empty subset of [1,2,3]")

    if not (isinstance(c["roles"], list) and c["roles"]):
        add(f"{cid}: roles must be a non-empty list")
    else:
        for r in c["roles"]:
            if _is_todo(r):
                add(f"{cid}: roles contains TODO entry", severity="todo")

    if not isinstance(c["regulatory"], list):
        add(f"{cid}: regulatory must be a list")

    p = c["priority"]
    if _is_todo(p):
        add(f"{cid}: priority is TODO", severity="todo")
    elif p not in PRIORITY_VALUES:
        add(f"{cid}: priority must be one of {sorted(PRIORITY_VALUES)} (got {p!r})")

    for k in ("yesBar", "partialBar", "noBar"):
        v = c[k]
        if not isinstance(v, str) or not v.strip():
            add(f"{cid}: {k} must be a non-empty string")
        elif _is_todo(v):
            add(f"{cid}: {k} is TODO", severity="todo")

    vi = c["verifyIn"]
    if not isinstance(vi, list):
        add(f"{cid}: verifyIn must be a list")
    else:
        for i, entry in enumerate(vi):
            if not isinstance(entry, dict):
                add(f"{cid}: verifyIn[{i}] must be an object")
                continue
            for sub in ("portal", "path", "url"):
                if sub not in entry or not isinstance(entry[sub], str):
                    add(f"{cid}: verifyIn[{i}].{sub} missing or not a string")
            if isinstance(entry.get("url"), str) and not URL_RE.match(entry["url"]):
                add(f"{cid}: verifyIn[{i}].url must be http(s)")

    if not isinstance(c["verifyPowerShell"], str):
        add(f"{cid}: verifyPowerShell must be a string")

    ee = c["evidenceExpected"]
    if not isinstance(ee, list) or not all(isinstance(x, str) for x in ee):
        add(f"{cid}: evidenceExpected must be a list of strings")

    for k in ("controlDocUrl", "portalPlaybookUrl"):
        v = c[k]
        if not isinstance(v, str) or not v.startswith("/"):
            add(f"{cid}: {k} must be a site-root path starting with /")
        elif _is_todo(v):
            add(f"{cid}: {k} is TODO", severity="todo")

    if not isinstance(c["collectorField"], str):
        add(f"{cid}: collectorField must be a string")

    syb = c["sectorYesBar"]
    if not isinstance(syb, dict):
        add(f"{cid}: sectorYesBar must be an object")
    else:
        missing = SECTORS - set(syb.keys())
        if missing:
            add(f"{cid}: sectorYesBar missing sectors: {sorted(missing)}")

    fn = c["facilitatorNotes"]
    if not isinstance(fn, dict):
        add(f"{cid}: facilitatorNotes must be an object")
    else:
        for sub in ("ask", "followUp"):
            if sub not in fn or not isinstance(fn[sub], str):
                add(f"{cid}: facilitatorNotes.{sub} missing or not a string")
            elif _is_todo(fn[sub]):
                add(f"{cid}: facilitatorNotes.{sub} is TODO", severity="todo")
        if "timeBudgetMinutes" not in fn or not isinstance(fn["timeBudgetMinutes"], int):
            add(f"{cid}: facilitatorNotes.timeBudgetMinutes missing/not int")

    sols = c["solutions"]
    if not isinstance(sols, list):
        add(f"{cid}: solutions must be a list")
    else:
        # Phase C2: solutions[] may be either bare string slugs
        # (legacy) or objects with {id, tier, role} referencing the
        # FSI-CopilotGov-Solutions lock.
        for i, s in enumerate(sols):
            if isinstance(s, str):
                if not SLUG_RE.match(s):
                    add(f"{cid}: solutions[{i}] = {s!r} must match {SLUG_RE.pattern}")
            elif isinstance(s, dict):
                sid = s.get("id")
                if not (isinstance(sid, str) and SLUG_RE.match(sid)):
                    add(
                        f"{cid}: solutions[{i}].id missing or not kebab-case "
                        f"(got {sid!r})"
                    )
                tier = s.get("tier")
                if tier is not None and tier not in (1, 2, 3):
                    add(
                        f"{cid}: solutions[{i}].tier must be int in (1,2,3) "
                        f"(got {tier!r})"
                    )
                role = s.get("role")
                if role is not None and role not in ("primary", "supporting"):
                    add(
                        f"{cid}: solutions[{i}].role must be "
                        f"'primary'|'supporting' (got {role!r})"
                    )
            else:
                add(
                    f"{cid}: solutions[{i}] must be a folder-name string "
                    f"or {{id,tier,role}} object"
                )

    return errs, warns


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=MANIFEST_DEFAULT)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Promote SPA-field-missing warnings to errors (Phase A2 done).",
    )
    parser.add_argument(
        "--allow-todo",
        action="store_true",
        help="In --strict mode, downgrade TODO: placeholders to warnings.",
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if not args.manifest.exists():
        print(f"ERROR: manifest not found at {args.manifest}", file=sys.stderr)
        return 2

    controls = json.loads(args.manifest.read_text(encoding="utf-8"))
    if not isinstance(controls, list):
        print("ERROR: manifest must be a JSON list", file=sys.stderr)
        return 2

    all_errors: list[str] = []
    all_warnings: list[str] = []

    if len(controls) != EXPECTED_COUNT:
        all_errors.append(f"expected {EXPECTED_COUNT} controls, got {len(controls)}")

    ids = [c.get("id") for c in controls]
    if len(set(ids)) != len(ids):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        all_errors.append(f"duplicate control ids: {dupes}")

    actual_by_pillar: dict[int, int] = {}
    for c in controls:
        if isinstance(c, dict) and isinstance(c.get("pillar"), int):
            actual_by_pillar[c["pillar"]] = actual_by_pillar.get(c["pillar"], 0) + 1
    for p, expected in EXPECTED_BY_PILLAR.items():
        if actual_by_pillar.get(p, 0) != expected:
            all_errors.append(
                f"pillar {p}: expected {expected} controls, got {actual_by_pillar.get(p, 0)}"
            )

    for c in controls:
        if not isinstance(c, dict):
            all_errors.append(f"non-object entry: {c!r}")
            continue
        all_errors.extend(_validate_engine(c))
        spa_errs, spa_warns = _validate_spa(c, strict=args.strict, allow_todo=args.allow_todo)
        all_errors.extend(spa_errs)
        all_warnings.extend(spa_warns)

    for w in all_warnings:
        print(f"WARN: {w}")
    for e in all_errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if all_errors:
        print(
            f"\nFAIL: {len(all_errors)} error(s), {len(all_warnings)} warning(s).",
            file=sys.stderr,
        )
        return 1

    if not args.quiet:
        print(
            f"OK: {len(controls)} controls validated "
            f"({len(all_warnings)} warning(s))."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
