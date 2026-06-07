"""MkDocs build hook — write /version.json for post-deploy smoke probing.

Writes ``version.json`` (containing the build SHA, framework version, and a
build timestamp) directly into the built site so the prod-smoke workflow can
poll the live site and confirm the correct commit was deployed.

Canonical version source: the repo-root ``VERSION`` file (single source of
truth).  If the file is missing the version falls back to ``"unknown"`` so
the build never fails on version-file issues alone.

Wire-up in ``mkdocs.yml``::

    hooks:
      - scripts/hooks/version_json.py
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _compute_sha() -> str:
    sha = os.environ.get("GITHUB_SHA")
    if sha:
        return sha
    try:
        return (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], stderr=subprocess.DEVNULL
            )
            .strip()
            .decode("ascii")
        )
    except Exception:
        return f"dev-{int(_dt.datetime.now(_dt.timezone.utc).timestamp())}"


def _read_version() -> str:
    version_file = REPO_ROOT / "VERSION"
    if not version_file.exists():
        return "unknown"
    raw = version_file.read_text(encoding="utf-8").strip()
    return raw or "unknown"


def on_post_build(config, **_kwargs):
    """Write version.json into the built site for smoke-probe use."""
    payload = {
        "version": _read_version(),
        "sha": _compute_sha(),
        "builtAt": _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    site_dir = Path(config["site_dir"])
    (site_dir / "version.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
