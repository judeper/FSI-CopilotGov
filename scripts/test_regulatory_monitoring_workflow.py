"""Workflow-structure regression tests for the Regulatory Monitor CI gate.

Guards the gap flagged in PR review: the regulatory-monitor classifier /
config regression tests (``scripts/test_regulatory_monitor.py``) and the
classification config they exercise (``scripts/config/monitoring-config.yaml``)
must be wired into the Regulatory Monitor workflow so a classification-pattern
regression cannot merge without CI actually running the tests. It also verifies
that the workflow shares the monitor's three-way exit contract, only writes PRs
for the findings code, and propagates source/execution failures. Pull-request
code remains isolated in a read-only job while scheduled/manual monitoring
retains the write permissions needed to open and supersede PRs.

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
import re
import sys

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "regulatory-monitoring.yml"
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import regulatory_monitor  # noqa: E402

MONITOR_TEST_FILE = "scripts/test_regulatory_monitor.py"
WORKFLOW_TEST_FILE = "scripts/test_regulatory_monitoring_workflow.py"
VALIDATION_JOB = "validate"
MONITOR_JOB = "monitor"
CLEAN_EXIT_CODE = str(regulatory_monitor.EXIT_CLEAN)
FAILURE_EXIT_CODE = str(regulatory_monitor.EXIT_FAILURE)
FINDINGS_EXIT_CODE = str(regulatory_monitor.EXIT_FINDINGS)

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


def _job(job_name: str) -> dict:
    return _workflow()["jobs"][job_name]


def _steps(job_name: str) -> list[dict]:
    return _job(job_name)["steps"]


def _step(job_name: str, step_name: str) -> dict:
    matches = [
        step
        for step in _steps(job_name)
        if step.get("name") == step_name
    ]
    assert len(matches) == 1, f"expected one {step_name!r} step in {job_name!r}"
    return matches[0]


def test_pr_triggers_cover_impl_config_and_tests() -> None:
    paths = set(_workflow()["on"]["pull_request"]["paths"])
    missing = REQUIRED_TRIGGER_PATHS - paths
    assert not missing, (
        f"regulatory-monitoring.yml PR path filter omits: {sorted(missing)}"
    )


def test_pr_validation_is_read_only_and_write_job_is_event_isolated() -> None:
    workflow = _workflow()
    validation_job = _job(VALIDATION_JOB)
    monitor_job = _job(MONITOR_JOB)

    assert workflow["permissions"] == {}
    assert validation_job["if"] == "github.event_name == 'pull_request'"
    assert validation_job["permissions"] == {"contents": "read"}

    assert monitor_job["if"] == (
        "github.event_name == 'schedule' || "
        "github.event_name == 'workflow_dispatch'"
    )
    assert monitor_job["permissions"] == {
        "contents": "write",
        "pull-requests": "write",
        "issues": "write",
    }


def test_checkouts_do_not_persist_credentials() -> None:
    for job_name in (VALIDATION_JOB, MONITOR_JOB):
        checkout_steps = [
            step
            for step in _steps(job_name)
            if step.get("uses", "").startswith("actions/checkout@")
        ]
        assert len(checkout_steps) == 1
        assert checkout_steps[0].get("with", {}).get("persist-credentials") == "false"


def test_pr_validation_runs_the_regulatory_monitor_pytest_file() -> None:
    pytest_steps = [
        step
        for step in _steps(VALIDATION_JOB)
        if "pytest" in step.get("run", "") and MONITOR_TEST_FILE in step.get("run", "")
    ]
    assert pytest_steps, (
        f"no CI step runs pytest against {MONITOR_TEST_FILE}; a classification "
        "regression could merge unvalidated"
    )
    assert _job(VALIDATION_JOB)["if"] == "github.event_name == 'pull_request'"


def test_dependencies_install_pytest_for_the_test_step() -> None:
    install_runs = " ".join(
        step.get("run", "")
        for step in _steps(VALIDATION_JOB)
        if "install" in step.get("name", "").lower()
    )
    assert "pytest" in install_runs, (
        "the workflow must install pytest so the regression tests can run "
        "(scripts/requirements.txt is runtime-only and omits pytest by convention)"
    )


def test_offline_dry_run_smoke_is_preserved() -> None:
    dry_run_steps = [
        step
        for step in _steps(VALIDATION_JOB)
        if "--dry-run" in step.get("run", "")
    ]
    assert dry_run_steps, (
        "the offline --dry-run smoke step must remain so PR validation needs no "
        "live network access or credentials"
    )
    assert _job(VALIDATION_JOB)["if"] == "github.event_name == 'pull_request'"


def test_monitor_step_enforces_three_way_exit_contract() -> None:
    monitor_step = _step(
        MONITOR_JOB,
        "Run Regulatory Monitor (scheduled / manual)",
    )
    run = monitor_step["run"]

    assert monitor_step.get("continue-on-error") is None
    assert FINDINGS_EXIT_CODE != "1"

    clean_branch = re.search(
        rf"(?ms)^\s*{re.escape(CLEAN_EXIT_CODE)}\)\s*(.*?)^\s*;;",
        run,
    )
    findings_branch = re.search(
        rf"(?ms)^\s*{re.escape(FINDINGS_EXIT_CODE)}\)\s*(.*?)^\s*;;",
        run,
    )
    failure_branch = re.search(
        rf"(?ms)^\s*{re.escape(FAILURE_EXIT_CODE)}\)\s*(.*?)^\s*;;",
        run,
    )

    assert clean_branch and "exit 0" in clean_branch.group(1)
    assert findings_branch and "report_file=" in findings_branch.group(1)
    assert "exit 0" in findings_branch.group(1)
    assert failure_branch and 'exit "$EXIT_CODE"' in failure_branch.group(1)
    assert 'exit "$EXIT_CODE"' in run.split("*)", maxsplit=1)[1]


def test_pr_write_path_is_gated_on_findings_exit() -> None:
    findings_condition = (
        f"steps.monitor.outputs.exit_code == '{FINDINGS_EXIT_CODE}'"
    )

    assert _step(MONITOR_JOB, "Detect state changes")["if"] == findings_condition

    for step_name in (
        "Generate GitHub App token",
        "Open / update PR with regulatory findings",
        "Close prior superseded Regulatory Monitor PRs",
    ):
        assert findings_condition in _step(MONITOR_JOB, step_name)["if"]


def test_pr_title_identifies_run_number_not_item_count() -> None:
    create_pr_steps = [
        step
        for step in _steps(MONITOR_JOB)
        if "create-pull-request" in step.get("uses", "")
    ]
    assert create_pr_steps, "the workflow must define its PR creation step"
    assert create_pr_steps[0]["with"]["title"] == (
        "Regulatory Monitor: new findings (run ${{ github.run_number }})"
    )
