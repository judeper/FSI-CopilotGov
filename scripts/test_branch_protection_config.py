"""Regression checks for docs-autonomy branch protection and CI coverage."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROTECTION_PATH = REPO_ROOT / ".github" / "branch-protection.json"
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "docs-validation.yml"
DOCS_PATH_REGEX = (
    r"^(docs/|README\.md$|AGENTS\.md$|SCOPE\.md$|VERSION$|mkdocs\.yml$|"
    r"overrides/|requirements\.txt$|scripts/|assessment/(manifest|data|templates)/|"
    r"data/monitor-state\.json$|\.github/branch-protection\.json$|"
    r"\.github/copilot-instructions\.md$|\.github/instructions/|"
    r"\.github/workflows/)"
)


def _workflow() -> dict:
    return yaml.load(WORKFLOW_PATH.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def test_branch_protection_is_autonomous_and_non_deadlocking() -> None:
    protection = json.loads(PROTECTION_PATH.read_text(encoding="utf-8"))

    assert protection == {
        "required_status_checks": {
            "strict": True,
            "contexts": ["mkdocs-strict"],
        },
        "enforce_admins": True,
        "required_pull_request_reviews": None,
        "restrictions": None,
        "required_linear_history": False,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "required_conversation_resolution": False,
        "lock_branch": False,
        "allow_fork_syncing": False,
    }


def test_required_context_is_base_controlled_and_always_triggered() -> None:
    workflow = _workflow()
    trigger = workflow["on"]

    assert set(trigger) == {"pull_request_target"}
    assert trigger["pull_request_target"] == {"branches": ["main"]}
    assert workflow["permissions"] == {
        "contents": "read",
        "pull-requests": "read",
    }

    job = workflow["jobs"]["mkdocs-strict"]
    assert job["name"] == "mkdocs-strict"
    assert "if" not in job
    assert job["env"]["DOCS_PATH_REGEX"] == DOCS_PATH_REGEX

    steps = {step.get("name"): step for step in job["steps"]}
    assert steps["Non-documentation PR shim"]["if"] == (
        "steps.scope.outputs.docs != 'true'"
    )
    checkout = steps["Checkout PR head without credentials"]
    assert checkout["if"] == "steps.scope.outputs.docs == 'true'"
    assert checkout["with"]["ref"] == "${{ github.event.pull_request.head.sha }}"
    assert checkout["with"]["persist-credentials"] == "false"


def test_docs_scope_and_deterministic_validation_contract() -> None:
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    workflow = _workflow()
    assert workflow["jobs"]["mkdocs-strict"]["env"]["DOCS_PATH_REGEX"] == DOCS_PATH_REGEX

    for command in (
        "pytest scripts/test_branch_protection_config.py -q",
        "python scripts/verify_controls.py",
        "python scripts/verify_language_rules.py",
        "python scripts/verify_regulatory_citations.py",
        "python scripts/verify_commercial_scope.py",
        "python scripts/build_content_graph.py",
        "python scripts/validate_content_graph.py",
        "python scripts/verify_readme_counts.py",
        "python scripts/verify_count_consistency.py",
        "python scripts/verify_version_stamps.py --check",
        "python scripts/validate_manifest.py --strict --allow-todo",
        "python scripts/verify_excel_templates.py",
        "mkdocs build --strict",
        "python scripts/verify_build_output.py site",
        "python scripts/verify_meta_tags.py site/",
        "python scripts/verify_doc_links.py site --json _broken-links.json",
        "python scripts/verify_learn_url_health.py",
    ):
        assert command in text


def test_docs_scope_distinguishes_docs_from_non_docs() -> None:
    for path in (
        "docs/index.md",
        "README.md",
        "scripts/verify_controls.py",
        "assessment/manifest/controls.json",
        ".github/branch-protection.json",
        ".github/workflows/docs-validation.yml",
    ):
        assert re.search(DOCS_PATH_REGEX, path), path

    for path in (
        "assessment/engine/score.py",
        "assessment/tests/test_engine.py",
        "tests/spa/d1-smoke.test.mjs",
        "package-lock.json",
        "LICENSE",
    ):
        assert not re.search(DOCS_PATH_REGEX, path), path


def test_flaky_external_link_check_is_not_required() -> None:
    protection = json.loads(PROTECTION_PATH.read_text(encoding="utf-8"))
    required = protection["required_status_checks"]["contexts"]

    assert "markdown-link-check" not in required
    assert "control-consistency" not in required
