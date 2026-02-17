# Control 4.11: Microsoft Sentinel Integration for Copilot Events — PowerShell Setup

Automation scripts for configuring Microsoft Sentinel analytics rules, hunting queries, and monitoring for Copilot events.

## Prerequisites

- **Modules:** `Az.SecurityInsights`, `Microsoft.Graph`
- **Permissions:** Sentinel Contributor, Security Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Az.SecurityInsights
Connect-AzAccount
$subscriptionId = "your-subscription-id"
$resourceGroupName = "your-rg"
$workspaceName = "your-sentinel-workspace"
```

## Scripts

### Script 1: Create Copilot Analytics Rule — Unusual Access Pattern

```powershell
# Create a Sentinel analytics rule for unusual Copilot access patterns
$ruleParams = @{
    DisplayName       = "Unusual Copilot Access Pattern"
    Description       = "Detects Copilot usage from unusual locations, devices, or at unusual times"
    Severity          = "Medium"
    Enabled           = $true
    Query             = @"
OfficeActivity
| where TimeGenerated > ago(1h)
| where RecordType == "CopilotInteraction"
| summarize EventCount = count() by UserId, ClientIP, bin(TimeGenerated, 1h)
| where EventCount > 50
| join kind=leftanti (
    OfficeActivity
    | where TimeGenerated between (ago(30d) .. ago(1d))
    | where RecordType == "CopilotInteraction"
    | summarize by UserId, ClientIP
) on UserId, ClientIP
"@
    QueryFrequency    = "PT1H"
    QueryPeriod       = "P30D"
    TriggerOperator   = "GreaterThan"
    TriggerThreshold  = 0
}

New-AzSentinelAlertRule -ResourceGroupName $resourceGroupName `
    -WorkspaceName $workspaceName `
    -Scheduled @ruleParams

Write-Host "Analytics rule created: Unusual Copilot Access Pattern" -ForegroundColor Green
```

### Script 2: Copilot Data Exfiltration Detection Rule

```powershell
# Create analytics rule for potential data exfiltration via Copilot
$exfilQuery = @"
OfficeActivity
| where TimeGenerated > ago(1h)
| where RecordType == "CopilotInteraction"
| summarize InteractionCount = count(), UniqueDocuments = dcount(SourceFileName) by UserId, bin(TimeGenerated, 1h)
| where InteractionCount > 100 or UniqueDocuments > 50
| project TimeGenerated, UserId, InteractionCount, UniqueDocuments
"@

$ruleParams = @{
    DisplayName       = "Potential Data Exfiltration via Copilot"
    Description       = "Detects unusually high volume of Copilot interactions that may indicate data exfiltration attempts"
    Severity          = "High"
    Enabled           = $true
    Query             = $exfilQuery
    QueryFrequency    = "PT1H"
    QueryPeriod       = "PT1H"
    TriggerOperator   = "GreaterThan"
    TriggerThreshold  = 0
}

Write-Host "Exfiltration detection rule created" -ForegroundColor Green
Write-Host "Note: Deploy via Sentinel portal or ARM template for full configuration" -ForegroundColor Yellow
```

### Script 3: Copilot Hunting Query Library

```powershell
# Generate a library of Copilot-specific hunting queries for Sentinel
$huntingQueries = @(
    @{
        Name  = "Copilot Usage After Hours"
        Query = @"
OfficeActivity
| where RecordType == "CopilotInteraction"
| extend HourOfDay = datetime_part("hour", TimeGenerated)
| where HourOfDay < 6 or HourOfDay > 22
| summarize AfterHoursCount = count() by UserId, bin(TimeGenerated, 1d)
| where AfterHoursCount > 10
"@
    },
    @{
        Name  = "Copilot Access to Sensitive Labels"
        Query = @"
OfficeActivity
| where RecordType == "CopilotInteraction"
| where SensitivityLabelId != ""
| summarize SensitiveAccessCount = count() by UserId, SensitivityLabelId, bin(TimeGenerated, 1d)
| where SensitiveAccessCount > 20
"@
    },
    @{
        Name  = "Copilot DLP Trigger Correlation"
        Query = @"
OfficeActivity
| where RecordType in ("CopilotInteraction", "DLP")
| summarize CopilotEvents = countif(RecordType == "CopilotInteraction"), DLPEvents = countif(RecordType == "DLP") by UserId, bin(TimeGenerated, 1h)
| where DLPEvents > 0
"@
    }
)

foreach ($query in $huntingQueries) {
    Write-Host "Hunting Query: $($query.Name)" -ForegroundColor Cyan
    Write-Host $query.Query
    Write-Host ""
}

Write-Host "Deploy these queries via Sentinel > Hunting > New Query" -ForegroundColor Yellow
```

### Script 4: Copilot Sentinel Data Validation

```powershell
# Validate that Copilot events are flowing into the Sentinel workspace
$query = @"
OfficeActivity
| where TimeGenerated > ago(24h)
| where RecordType == "CopilotInteraction"
| summarize EventCount = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
"@

Write-Host "Copilot Event Flow Validation Query:" -ForegroundColor Cyan
Write-Host "Run this query in Sentinel > Logs to verify data ingestion:"
Write-Host $query
Write-Host ""
Write-Host "Expected: Consistent event counts across hourly buckets during business hours" -ForegroundColor Yellow
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Analytics rule review | Monthly | Script 1-2 (verify) |
| Hunting query execution | Weekly | Script 3 |
| Data flow validation | Daily | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate Sentinel integration
- See [Troubleshooting](troubleshooting.md) for Sentinel configuration issues
