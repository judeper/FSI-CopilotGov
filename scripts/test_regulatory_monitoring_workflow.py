"""Workflow-structure regression tests for the Regulatory Monitor CI gate.

Guards the gap flagged in PR review: the regulatory-monitor classifier /
config regression tests (``scripts/test_regulatory_monitor.py``) and the
classification config they exercise (``scripts/config/monitoring-config.yaml``)
must be wired into the Regulatory Monitor workflow so a classification-pattern
regression cannot merge without CI actually running the tests.

Mirrors the YAML-aware pattern in ``test_branch_protection_config.py``: the
workflow is parsed with ``yaml.BaseLoader`` so the ``on:`` mapping key stays the
string ``"on"`` instead of being coerced to the boolean ``True`` under YAML 1.1.
Asserting on the parsed structure (not raw text) keeps these checks robust to
formatting/ordering changes while still proving the trigger/command contract.

Picked up by ``python -m pytest scripts -q`` and by the Regulatory Monitor
workflow's own PR test step.
"""
from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "regulatory-monitoring.yml"

MONITOR_TEST_FILE = "scripts/test_regulatory_monitor.py"
WORKFLOW_TEST_FILE = "scripts/test_regulatory_monitoring_workflow.py"

# Changes to any of these must (re)trigger the Regulatory Monitor PR validation
# so config-only and test-only edits cannot bypass CI. Kept to the exact files
# the monitor and its tests consume -- no broad globs -- so unrelated repository
# changes do not spuriously trigger this workflow.
REQUIRED_TRIGGER_PATHS = {
    "scripts/regulatory_monitor.py",
    "scripts/monitoring_shared.py",
    "scripts/config/monitoring-config.yaml",
    MONITOR_TEST_FILE,
    WORKFLOW_TEST_FILE,
    "scripts/requirements.txt",
    ".github/workflows/regulatory-monitoring.yml",
}


def _workflow() -> dict:
    return yaml.load(WORKFLOW_PATH.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def _steps() -> list[dict]:
    return _workflow()["jobs"]["monitor"]["steps"]


def test_pr_triggers_cover_impl_config_and_tests() -> None:
    paths = set(_workflow()["on"]["pull_request"]["paths"])
    missing = REQUIRED_TRIGGER_PATHS - paths
    assert not missing, (
        f"regulatory-monitoring.yml PR path filter omits: {sorted(missing)}"
    )


def test_pr_validation_runs_the_regulatory_monitor_pytest_file() -> None:
    pytest_steps = [
        step
        for step in _steps()
        if "pytest" in step.get("run", "") and MONITOR_TEST_FILE in step.get("run", "")
    ]
    assert pytest_steps, (
        f"no CI step runs pytest against {MONITOR_TEST_FILE}; a classification "
        "regression could merge unvalidated"
    )
    # Must execute on pull_request events (the merge-gating path).
    assert any(
        "pull_request" in step.get("if", "") for step in pytest_steps
    ), "the regulatory-monitor pytest step is not gated to pull_request events"


def test_dependencies_install_pytest_for_the_test_step() -> None:
    install_runs = " ".join(
        step.get("run", "")
        for step in _steps()
        if "install" in step.get("name", "").lower()
    )
    assert "pytest" in install_runs, (
        "the workflow must install pytest so the regression tests can run "
        "(scripts/requirements.txt is runtime-only and omits pytest by convention)"
    )


def test_offline_dry_run_smoke_is_preserved() -> None:
    dry_run_steps = [
        step for step in _steps() if "--dry-run" in step.get("run", "")
    ]
    assert dry_run_steps, (
        "the offline --dry-run smoke step must remain so PR validation needs no "
        "live network access or credentials"
    )
    assert any(
        "pull_request" in step.get("if", "") for step in dry_run_steps
    ), "the --dry-run smoke must run on pull_request events"
