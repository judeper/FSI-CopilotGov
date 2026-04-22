"""mkdocs-macros entry point: exposes content-graph counts as template variables.

Loaded by mkdocs-macros-plugin during ``mkdocs build`` / ``mkdocs serve``. Reads the
canonical content graph (produced by ``scripts/build_content_graph.py``) and exposes
its ``counts`` namespace plus the full graph as Jinja variables, so markdown can
reference e.g. ``{{ counts.controls }}`` instead of hand-typing integers that drift.

Also exposes derived ``playbooks_by_category`` and ``playbooks_by_pillar`` mappings
so navigation/index pages can render category/pillar breakdowns without duplicating
classification logic in template code.

If the graph file is not yet present (first-time setup or local dev before the
graph builder has run), a safe fallback with zeroed counts is used so the docs
site still builds.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

GRAPH_PATH = Path(__file__).parent.parent / "assessment" / "manifest" / "content-graph.json"

_FALLBACK_GRAPH = {
    "counts": {
        "controls": 0,
        "playbooks_total": 0,
        "playbooks_control": 0,
        "playbooks_cross_cutting": 0,
        "solutions": 0,
        "pillars": 4,
    }
}

_CONTROL_DIR_RE = re.compile(r"control-implementations/([0-9]+\.[0-9]+[a-z]?)/")


def _control_to_pillar(graph: dict) -> dict[str, int]:
    return {c["id"]: c.get("pillar") for c in graph.get("controls", [])}


def _build_classifications(graph: dict) -> tuple[dict, dict]:
    """Return (by_category, by_pillar) counters keyed by string for template use."""
    by_category: Counter = Counter()
    by_pillar: Counter = Counter()
    cmap = _control_to_pillar(graph)
    for pb in graph.get("playbooks", []) or []:
        ptype = pb.get("type")
        if ptype == "control-implementation":
            by_category["control-implementations"] += 1
            m = _CONTROL_DIR_RE.search(pb.get("path", ""))
            if m:
                pillar = cmap.get(m.group(1))
                if pillar:
                    by_pillar[f"pillar-{pillar}"] += 1
        elif ptype == "cross-cutting":
            cat = pb.get("category") or "uncategorized"
            by_category[cat] += 1
    return dict(sorted(by_category.items())), dict(sorted(by_pillar.items()))


def define_env(env):
    """Hook called by mkdocs-macros-plugin during build."""
    if GRAPH_PATH.exists():
        graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    else:
        graph = _FALLBACK_GRAPH

    by_category, by_pillar = _build_classifications(graph)

    env.variables["counts"] = graph.get("counts", _FALLBACK_GRAPH["counts"])
    env.variables["content_graph"] = graph
    env.variables["playbooks_by_category"] = by_category
    env.variables["playbooks_by_pillar"] = by_pillar

