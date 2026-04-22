"""mkdocs-macros entry point: exposes content-graph counts as template variables.

Loaded by mkdocs-macros-plugin during ``mkdocs build`` / ``mkdocs serve``. Reads the
canonical content graph (produced by ``scripts/build_content_graph.py``) and exposes
its ``counts`` namespace plus the full graph as Jinja variables, so markdown can
reference e.g. ``{{ counts.controls }}`` instead of hand-typing integers that drift.

If the graph file is not yet present (first-time setup or local dev before the
graph builder has run), a safe fallback with zeroed counts is used so the docs
site still builds.
"""
from __future__ import annotations

import json
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


def define_env(env):
    """Hook called by mkdocs-macros-plugin during build."""
    if GRAPH_PATH.exists():
        graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    else:
        graph = _FALLBACK_GRAPH

    env.variables["counts"] = graph.get("counts", _FALLBACK_GRAPH["counts"])
    env.variables["content_graph"] = graph
