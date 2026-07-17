from __future__ import annotations

import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HELPER = REPO_ROOT / "assessment" / "collectors" / "Collect-Sentinel.CopilotActivity.ps1"
COLLECTOR = REPO_ROOT / "assessment" / "collectors" / "Collect-Sentinel.ps1"


def _run_helper(expression: str) -> str:
    helper_path = str(HELPER).replace("'", "''")
    command = f"& {{ . '{helper_path}'; {expression} }}"
    result = subprocess.run(
        ["pwsh", "-NoProfile", "-NonInteractive", "-Command", command],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    return result.stdout.strip()


def test_query_text_uses_copilotactivity_with_documented_projection():
    query = _run_helper("Get-CopilotActivityDataQuery")
    assert "CopilotActivity" in query
    assert 'RecordType == "CopilotInteraction"' in query
    assert "| project TimeGenerated, RecordType, ActorUserId, ActorName, SrcIpAddr, Workload, AIModelName, LLMEventData" in query


def test_required_columns_and_schema_miss_detection():
    required = json.loads(
        _run_helper("@(Get-CopilotActivityRequiredColumns) | ConvertTo-Json -Compress")
    )
    assert required == [
        "TimeGenerated",
        "RecordType",
        "ActorUserId",
        "ActorName",
        "SrcIpAddr",
        "Workload",
        "AIModelName",
        "LLMEventData",
    ]

    missing = json.loads(
        _run_helper(
            "$available = @('TimeGenerated','RecordType','ActorUserId'); "
            "@(Get-CopilotActivityMissingColumns -AvailableColumns $available) | ConvertTo-Json -Compress"
        )
    )
    assert "ActorName" in missing
    assert "LLMEventData" in missing


def test_classifies_unavailable_table_and_query_failures():
    unavailable = _run_helper(
        "Get-CopilotActivityFailureStatus -Message \"Failed to resolve table or column expression named 'CopilotActivity'\""
    )
    assert unavailable == "table_or_connector_unavailable"

    permission = _run_helper(
        "Get-CopilotActivityFailureStatus -Message \"Forbidden: Principal is not authorized to query this table.\""
    )
    assert permission == "permission_failure"

    generic = _run_helper(
        "Get-CopilotActivityFailureStatus -Message \"Query could not be parsed near token '|'\""
    )
    assert generic == "query_failure"


def test_distinguishes_empty_and_valid_copilotactivity_rows():
    no_records = _run_helper("Get-CopilotActivityAssessmentStatus -RowCount 0")
    assert no_records == "no_records"

    has_records = _run_helper("Get-CopilotActivityAssessmentStatus -RowCount 3")
    assert has_records == "records_found"


def test_null_results_guard_does_not_create_single_null_row():
    empty_count = _run_helper(
        "@(Convert-CopilotActivityResultsToRows -Results $null).Count"
    )
    assert empty_count == "0"

    mixed_count = _run_helper(
        "$rows = @(Convert-CopilotActivityResultsToRows -Results @($null, [pscustomobject]@{RecordType='CopilotInteraction'})); "
        "$rows.Count"
    )
    assert mixed_count == "1"


def test_data_minimization_contract_blocks_raw_row_fields():
    forbidden_fields = json.loads(
        _run_helper("@(Get-CopilotActivityForbiddenEvidenceFields) | ConvertTo-Json -Compress")
    )
    assert "SampleRows" in forbidden_fields
    assert "RawRows" in forbidden_fields

    minimization_note = _run_helper("Get-CopilotActivityDataMinimizationNote")
    assert "aggregate metadata only" in minimization_note
    assert "ActorUserId" in minimization_note
    assert "LLMEventData" in minimization_note

    collector_text = COLLECTOR.read_text(encoding="utf-8")
    assert "SampleRows" not in collector_text
