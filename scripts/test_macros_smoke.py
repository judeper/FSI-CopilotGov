"""Smoke test for scripts/macros_module.py — verifies mkdocs-macros entry point."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import SimpleNamespace

MODULE_PATH = Path(__file__).parent / "macros_module.py"


def _load_macros_module():
    spec = importlib.util.spec_from_file_location("macros_module", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["macros_module"] = module
    spec.loader.exec_module(module)
    return module


def test_define_env_sets_counts():
    macros = _load_macros_module()
    env = SimpleNamespace(variables={})
    macros.define_env(env)

    assert "counts" in env.variables
    assert "content_graph" in env.variables
    counts = env.variables["counts"]
    assert isinstance(counts, dict)
    # 'pillars' is invariant (always 4) and present in both real graph and fallback.
    assert "pillars" in counts


def test_define_env_exposes_playbook_classifications():
    macros = _load_macros_module()
    env = SimpleNamespace(variables={})
    macros.define_env(env)

    by_cat = env.variables["playbooks_by_category"]
    by_pillar = env.variables["playbooks_by_pillar"]

    assert isinstance(by_cat, dict)
    assert isinstance(by_pillar, dict)

    # control-implementations is the largest cross-cutting bucket once the
    # graph is populated; allow zero in fallback mode.
    counts = env.variables["counts"]
    if counts.get("playbooks_total", 0) > 0:
        assert "control-implementations" in by_cat
        assert sum(by_cat.values()) == counts["playbooks_total"]
        # Pillar buckets should map to 'pillar-1'..'pillar-4'.
        for key in by_pillar:
            assert key.startswith("pillar-")

