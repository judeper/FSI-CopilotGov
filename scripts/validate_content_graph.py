"""Validate the canonical content graph.

Loads `assessment/manifest/content-graph.json`, validates it against
`content-graph.schema.json`, and enforces business rules:

  * All 58 controls are present.
  * Control IDs are unique.
  * Every playbook ``control_refs`` entry points at a known control.
  * Every solution ``control_coverage`` entry points at a known control.
  * The ``counts`` block matches the actual list lengths.
  * Pillars are restricted to 1-4.

Exit code 0 on success, 1 on any failure (with clear error messages).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = REPO_ROOT / "assessment" / "manifest" / "content-graph.json"
SCHEMA_PATH = REPO_ROOT / "assessment" / "manifest" / "content-graph.schema.json"

EXPECTED_CONTROL_COUNT = 58


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_validate(graph: dict, schema: dict, errors: list[str]) -> None:
    try:
        import jsonschema  # type: ignore
    except ImportError:
        errors.append(
            "jsonschema is not installed; run `pip install -r scripts/requirements.txt`"
        )
        return
    validator = jsonschema.Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(graph), key=lambda e: list(e.absolute_path)):
        loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"schema: {loc}: {err.message}")


def validate(graph: dict, schema: dict) -> list[str]:
    errors: list[str] = []
    _schema_validate(graph, schema, errors)

    controls = graph.get("controls", [])
    playbooks = graph.get("playbooks", [])
    solutions = graph.get("solutions", [])
    counts = graph.get("counts", {})

    if len(controls) != EXPECTED_CONTROL_COUNT:
        errors.append(
            f"expected {EXPECTED_CONTROL_COUNT} controls, found {len(controls)}"
        )

    ids: list[str] = [c.get("id", "") for c in controls]
    seen: set[str] = set()
    dupes: set[str] = set()
    for cid in ids:
        if cid in seen:
            dupes.add(cid)
        seen.add(cid)
    if dupes:
        errors.append(f"duplicate control IDs: {sorted(dupes)}")

    for c in controls:
        pillar = c.get("pillar")
        if pillar not in (1, 2, 3, 4):
            errors.append(f"control {c.get('id')!r}: invalid pillar {pillar!r}")

    known_ids = set(ids)
    for pb in playbooks:
        for ref in pb.get("control_refs", []) or []:
            if ref not in known_ids:
                errors.append(
                    f"playbook {pb.get('path')!r}: unknown control_ref {ref!r}"
                )

    for sol in solutions:
        for ref in sol.get("control_coverage", []) or []:
            if ref not in known_ids:
                errors.append(
                    f"solution {sol.get('id')!r}: unknown control_coverage {ref!r}"
                )

    pb_ctrl = sum(1 for p in playbooks if p.get("type") == "control-implementation")
    pb_cross = sum(1 for p in playbooks if p.get("type") == "cross-cutting")
    expected_counts = {
        "controls": len(controls),
        "pillars": len({c.get("pillar") for c in controls}),
        "playbooks_total": len(playbooks),
        "playbooks_control": pb_ctrl,
        "playbooks_cross_cutting": pb_cross,
        "solutions": len(solutions),
    }
    for key, expected in expected_counts.items():
        actual = counts.get(key)
        if actual != expected:
            errors.append(f"counts.{key}: expected {expected}, got {actual}")

    return errors


def main() -> int:
    if not GRAPH_PATH.is_file():
        print(f"ERROR: missing {GRAPH_PATH}", file=sys.stderr)
        return 1
    if not SCHEMA_PATH.is_file():
        print(f"ERROR: missing {SCHEMA_PATH}", file=sys.stderr)
        return 1

    graph = _load_json(GRAPH_PATH)
    schema = _load_json(SCHEMA_PATH)
    errors = validate(graph, schema)

    if errors:
        print("Content graph validation FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    counts = graph.get("counts", {})
    print(
        "Content graph OK -- controls={controls} playbooks_total={playbooks_total} "
        "(control={playbooks_control}, cross_cutting={playbooks_cross_cutting}) "
        "solutions={solutions}".format(**counts)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
