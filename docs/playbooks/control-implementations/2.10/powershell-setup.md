# Control 2.10: Insider Risk Detection for Copilot Usage — PowerShell Setup

Automation scripts for monitoring and reporting on insider risk detection for Copilot.

## Prerequisites

- Exchange Online Management / Security & Compliance PowerShell
- Audit access for CopilotInteraction records
- Supported Insider Risk Management subscription and assigned licenses

## Scripts

> Microsoft Learn pages in scope for this control document Risky AI usage, Risky Agents, Policy indicators, data risk graph, and the Triage Agent primarily through the Microsoft Purview portal. Use the scripts below for audit-backed Copilot usage analysis, and verify IRM policy/template configuration in the Purview portal.

### Script 1: Copilot Interaction Audit Prerequisite Check

```powershell
# Audit prerequisite check: confirm CopilotInteraction records are present
# before relying on IRM workflows that correlate Copilot activity.
# Requires: Security & Compliance PowerShell / Exchange Online Management

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$events = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -Operations CopilotInteraction -ResultSize 5000

if ($events.Count -eq 5000) {
    Write-Warning "Search-UnifiedAuditLog returned the 5,000-row cap. Treat this as a spot-check only, not a complete export."
}

$summary = $events | Group-Object UserIds | ForEach-Object {
    [PSCustomObject]@{
        User       = $_.Name
        EventCount = $_.Count
        FirstEvent = ($_.Group | Sort-Object CreationDate | Select-Object -First 1).CreationDate
        LastEvent  = ($_.Group | Sort-Object CreationDate -Descending | Select-Object -First 1).CreationDate
    }
} | Sort-Object EventCount -Descending

Write-Host "=== CopilotInteraction Audit Summary ==="
Write-Host "Users with CopilotInteraction events: $($summary.Count)"
$summary | Format-Table User, EventCount, FirstEvent, LastEvent -AutoSize
$summary | Export-Csv "CopilotInteractionSummary_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Risk Signal Extraction from Copilot Audit Data

```powershell
# Extract audit properties that are useful during insider-risk review, such as
# AppHost, Bing web grounding, and jailbreak detection flags.
# The Copilot schema places AISystemPlugin, Messages, and AppHost under
# AuditData.CopilotEventData, while AppIdentity, Workload, and AgentId remain
# root-level audit properties.
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

function Get-PagedCopilotInteractionAudit {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [datetime]$StartDate,

        [Parameter(Mandatory)]
        [datetime]$EndDate,

        [timespan]$SegmentDuration = [timespan]::FromDays(1)
    )

    $records = [System.Collections.Generic.List[object]]::new()
    $seenRecordIds = [System.Collections.Generic.HashSet[string]]::new(
        [System.StringComparer]::OrdinalIgnoreCase
    )

    for ($segmentStart = $StartDate; $segmentStart -lt $EndDate; $segmentStart = $segmentEnd) {
        $segmentEnd = $segmentStart.Add($SegmentDuration)
        if ($segmentEnd -gt $EndDate) {
            $segmentEnd = $EndDate
        }

        $sessionId = "IRMCopilotAudit_$([guid]::NewGuid())"
        $pageNumber = 0
        $previousResultIndex = -1L
        $segmentResultCount = 0
        $segmentExhausted = $false

        do {
            $pageNumber++
            $page = @(
                Search-UnifiedAuditLog `
                    -StartDate $segmentStart `
                    -EndDate $segmentEnd `
                    -Operations CopilotInteraction `
                    -SessionId $sessionId `
                    -SessionCommand ReturnLargeSet `
                    -ResultSize 5000 `
                    -ErrorAction Stop
            )

            if ($page.Count -eq 0) {
                $segmentExhausted = $true
                break
            }

            $segmentResultCount += $page.Count
            $newRecordCount = 0

            foreach ($record in $page) {
                $auditData = $record.AuditData | ConvertFrom-Json
                $recordId = [string]$auditData.Id
                if ([string]::IsNullOrWhiteSpace($recordId)) {
                    throw "An audit record is missing AuditData.Id; safe deduplication is not possible."
                }

                if ($seenRecordIds.Add($recordId)) {
                    $records.Add(
                        [PSCustomObject]@{
                            Record    = $record
                            AuditData = $auditData
                        }
                    )
                    $newRecordCount++
                }
            }

            $lastResult = $page[-1]
            $hasResultIndex = $null -ne $lastResult.ResultIndex -and
                -not [string]::IsNullOrWhiteSpace([string]$lastResult.ResultIndex)
            $hasResultCount = $null -ne $lastResult.ResultCount -and
                -not [string]::IsNullOrWhiteSpace([string]$lastResult.ResultCount)

            if ($hasResultIndex) {
                $resultIndex = [long]$lastResult.ResultIndex
                if ($resultIndex -le $previousResultIndex -and $newRecordCount -eq 0) {
                    throw "Audit paging made no progress for $segmentStart to $segmentEnd."
                }
                $previousResultIndex = $resultIndex
            }

            $moreRecordsProperty = $lastResult.AuditSearchRequestMetadata.PSObject.Properties[
                "moreRecordsAvailable"
            ]
            if ($null -ne $moreRecordsProperty) {
                $segmentExhausted = -not [System.Convert]::ToBoolean(
                    $moreRecordsProperty.Value
                )
            }
            elseif ($hasResultIndex -and $hasResultCount) {
                $segmentExhausted = (
                    [long]$lastResult.ResultIndex -eq [long]$lastResult.ResultCount
                )
            }

            if (
                $segmentResultCount -ge 50000 -or
                ($hasResultCount -and [long]$lastResult.ResultCount -ge 50000)
            ) {
                throw (
                    "The $segmentStart to $segmentEnd segment reached the Exchange Online " +
                    "50,000-record session limit. Reduce SegmentDuration and rerun; " +
                    "this result cannot be represented as complete."
                )
            }

            if (-not $segmentExhausted -and $newRecordCount -eq 0) {
                throw "Audit paging returned only duplicate records before reporting exhaustion."
            }
        }
        while (-not $segmentExhausted)
    }

    return $records
}

$copilotEvents = @(
    Get-PagedCopilotInteractionAudit -StartDate $startDate -EndDate $endDate
)

$riskSignals = $copilotEvents | ForEach-Object {
    $record = $_.Record
    $audit = $_.AuditData
    $copilotEventData = $audit.CopilotEventData
    $usedWebSearch = @(
        $copilotEventData.AISystemPlugin | Where-Object { $_.Id -eq "BingWebSearch" }
    ).Count -gt 0
    $jailbreakDetected = @(
        $copilotEventData.Messages | Where-Object { $_.JailbreakDetected -eq $true }
    ).Count -gt 0
    [PSCustomObject]@{
        Date               = $record.CreationDate
        User               = $record.UserIds
        Workload           = $audit.Workload
        AppIdentity        = $audit.AppIdentity
        AppHost            = $copilotEventData.AppHost
        AgentId            = $audit.AgentId
        UsedWebSearch      = $usedWebSearch
        JailbreakDetected  = $jailbreakDetected
    }
}

Write-Host "=== Copilot Audit Risk Signals ==="
$riskSignals | Group-Object User | Sort-Object Count -Descending | Select-Object -First 20 |
    Format-Table Name, Count -AutoSize
$riskSignals | Export-Csv "CopilotAuditSignals_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Off-Hours Copilot Activity Report

```powershell
# Detect Copilot usage outside business hours
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-14)
$endDate = Get-Date

$events = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -Operations CopilotInteraction -ResultSize 5000

$offHours = @()
foreach ($event in $events) {
    $eventTime = [DateTime]$event.CreationDate
    $hour = $eventTime.Hour
    if ($hour -lt 7 -or $hour -gt 20) {
        $offHours += [PSCustomObject]@{
            Date = $event.CreationDate
            User = $event.UserIds
            Hour = $hour
        }
    }
}

Write-Host "Off-hours Copilot activity (before 7am or after 8pm): $($offHours.Count)"
$offHours | Export-Csv "OffHoursCopilot_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| CopilotInteraction Audit Prerequisite Check | Weekly | Confirm the Copilot audit prerequisite for IRM evidence review |
| Copilot Audit Risk Signals | Weekly | Review Bing web grounding and jailbreak-related audit indicators |
| Off-Hours Activity Report | Weekly | Flag off-hours access for review |

## Next Steps

- See [Verification & Testing](verification-testing.md) for insider risk validation
- See [Troubleshooting](troubleshooting.md) for insider risk issues
- Back to [Control 2.10](../../../controls/pillar-2-security/2.10-insider-risk-detection.md)
