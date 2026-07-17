Set-StrictMode -Version Latest

function Get-CopilotActivityRequiredColumns {
    return @(
        'TimeGenerated',
        'RecordType',
        'ActorUserId',
        'ActorName',
        'SrcIpAddr',
        'Workload',
        'AIModelName',
        'LLMEventData'
    )
}

function Get-CopilotActivitySchemaQuery {
    return @'
CopilotActivity
| getschema
'@.Trim()
}

function Get-CopilotActivityDataQuery {
    return @'
CopilotActivity
| where TimeGenerated > ago(7d)
| where RecordType == "CopilotInteraction"
| project TimeGenerated, RecordType, ActorUserId, ActorName, SrcIpAddr, Workload, AIModelName, LLMEventData
| order by TimeGenerated desc
| take 200
'@.Trim()
}

function Convert-CopilotActivityResultsToRows {
    param(
        [Parameter()]
        [object]$Results
    )

    if ($null -eq $Results) {
        return @()
    }

    if ($Results -is [System.Collections.IEnumerable] -and -not ($Results -is [string])) {
        return @(
            $Results | Where-Object { $null -ne $_ }
        )
    }

    return @($Results)
}

function Get-CopilotActivityForbiddenEvidenceFields {
    return @(
        'SampleRows',
        'Rows',
        'RawRows',
        'Results'
    )
}

function Get-CopilotActivityDataMinimizationNote {
    return 'Collector persists aggregate metadata only (status, counts, schema/query metadata). Raw CopilotActivity row payloads containing ActorUserId, ActorName, SrcIpAddr, or LLMEventData are not written to evidence output.'
}

function Get-CopilotActivitySchemaColumnNames {
    param(
        [Parameter()]
        [object[]]$SchemaRows
    )

    if (-not $SchemaRows) {
        return @()
    }

    $names = [System.Collections.Generic.List[string]]::new()
    foreach ($row in $SchemaRows) {
        if ($null -eq $row) {
            continue
        }

        $columnName = $null
        if ($row.PSObject.Properties['ColumnName']) {
            $columnName = [string]$row.ColumnName
        }
        elseif ($row.PSObject.Properties['Name']) {
            $columnName = [string]$row.Name
        }
        elseif ($row.PSObject.Properties['Column']) {
            $columnName = [string]$row.Column
        }

        if (-not [string]::IsNullOrWhiteSpace($columnName) -and -not $names.Contains($columnName)) {
            $names.Add($columnName) | Out-Null
        }
    }

    return @($names)
}

function Get-CopilotActivityMissingColumns {
    param(
        [Parameter()]
        [string[]]$AvailableColumns
    )

    $available = @($AvailableColumns)
    return @(
        Get-CopilotActivityRequiredColumns |
            Where-Object { $_ -notin $available }
    )
}

function Get-CopilotActivityFailureStatus {
    param(
        [Parameter()]
        [AllowEmptyString()]
        [string]$Message
    )

    if ([string]::IsNullOrWhiteSpace($Message)) {
        return 'query_failure'
    }

    $normalized = $Message.ToLowerInvariant()
    $tableUnavailablePatterns = @(
        'failed to resolve table',
        'does not refer to any known table',
        'name ''copilotactivity'' does not refer',
        'table ''copilotactivity'' was not found',
        'unknown table',
        'could not resolve table'
    )

    foreach ($pattern in $tableUnavailablePatterns) {
        if ($normalized -match $pattern) {
            return 'table_or_connector_unavailable'
        }
    }

    $permissionPatterns = @(
        'forbidden',
        'not authorized',
        'unauthorized',
        'authorization',
        'permission',
        'access denied',
        'insufficient privileges'
    )

    foreach ($pattern in $permissionPatterns) {
        if ($normalized -match $pattern) {
            return 'permission_failure'
        }
    }

    return 'query_failure'
}

function Get-CopilotActivityAssessmentStatus {
    param(
        [Parameter()]
        [int]$RowCount
    )

    if ($RowCount -gt 0) {
        return 'records_found'
    }

    return 'no_records'
}
