#!/usr/bin/env python3
"""Overlay hand-authored manifest content from authored_content.py.

Reads ``assessment/manifest/controls.json`` and applies the field
overrides from ``assessment/manifest/authored_content.AUTHORED``.

Replacement rules:

* **Scalar fields** (str/int/list) are replaced when:
    - the manifest field is missing, OR
    - the manifest value starts with ``TODO:`` (case-insensitive), OR
    - for lists, the manifest value is empty.

* **dict fields** (sectorYesBar, facilitatorNotes) are merged
  per-key with the same TODO-replacement rule.

The merge **never** overwrites a value that has been hand-edited away
from the TODO default. Re-running this script after authored_content.py
is updated is safe.

Run from the repo root::

    python scripts/merge_authored_content.py
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "assessment" / "manifest" / "controls.json"
AUTHORED_PY = ROOT / "assessment" / "manifest" / "authored_content.py"

# Fields in this set are ALWAYS replaced by authored content, even when
# the existing manifest value is non-empty and not a TODO marker. Use
# sparingly: this is for fields where authored_content.py is the
# canonical source of truth (e.g. `solutions` is driven by the
# FSI-CopilotGov-Solutions sister repo, so hand edits in the manifest
# must not silently override later corrections).
_REPLACE_FIELDS: set[str] = {"solutions"}


def _is_todo(v: Any) -> bool:
    return isinstance(v, str) and v.strip().lower().startswith("todo:")


def _is_authoritative(existing: Any) -> bool:
    """Return True if `existing` is hand-edited content we should preserve."""
    if existing is None:
        return False
    if _is_todo(existing):
        return False
    if isinstance(existing, list) and not existing:
        return False
    if isinstance(existing, str) and not existing.strip():
        return False
    return True


def _load_authored() -> dict[str, dict]:
    spec = importlib.util.spec_from_file_location("authored_content", AUTHORED_PY)
    if spec is None or spec.loader is None:
        raise SystemExit(f"ERROR: cannot load {AUTHORED_PY}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "AUTHORED", {})


def _merge_value(existing: Any, override: Any, *, force_replace: bool = False) -> Any:
    """Return the value to write back: existing if authoritative, else override.

    When ``force_replace`` is True, the override always wins (used for
    fields listed in ``_REPLACE_FIELDS``).
    """
    if force_replace:
        return override
    if _is_authoritative(existing):
        # Only descend into dicts (so individual sectorYesBar / facilitatorNotes
        # keys can be filled in even if the dict already exists).
        if isinstance(existing, dict) and isinstance(override, dict):
            out = dict(existing)
            for k, v in override.items():
                out[k] = _merge_value(existing.get(k), v)
            return out
        return existing
    return override


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: manifest not found at {MANIFEST}", file=sys.stderr)
        return 2
    if not AUTHORED_PY.exists():
        print(f"ERROR: authored_content.py not found at {AUTHORED_PY}", file=sys.stderr)
        return 2

    controls = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(controls, list):
        print("ERROR: manifest is not a JSON list", file=sys.stderr)
        return 2

    authored = _load_authored()
    if not authored:
        print("WARN: AUTHORED dict is empty; nothing to merge.", file=sys.stderr)

    overlay_by_id = authored
    touched_count = 0
    fields_overlaid = 0
    fields_preserved = 0

    for ctrl in controls:
        cid = ctrl.get("id")
        overlay = overlay_by_id.get(cid)
        if not overlay:
            continue
        before = json.dumps(ctrl, sort_keys=True)
        for key, override_value in overlay.items():
            existing = ctrl.get(key)
            force_replace = key in _REPLACE_FIELDS
            new_value = _merge_value(existing, override_value, force_replace=force_replace)
            if new_value is not existing:
                if existing is None or _is_todo(existing) or (
                    isinstance(existing, list) and not existing
                ) or force_replace:
                    fields_overlaid += 1
                ctrl[key] = new_value
            elif _is_authoritative(existing) and not isinstance(existing, dict):
                fields_preserved += 1
        if json.dumps(ctrl, sort_keys=True) != before:
            touched_count += 1

    MANIFEST.write_text(
        json.dumps(controls, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Overlaid authored content into {touched_count} of {len(controls)} controls "
        f"({fields_overlaid} fields written, {fields_preserved} authoritative fields preserved)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
