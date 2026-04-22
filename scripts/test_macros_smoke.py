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
