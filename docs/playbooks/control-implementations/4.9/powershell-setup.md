# Control 4.9: Incident Reporting and Root Cause Analysis — PowerShell Setup

Automation scripts for detecting, reporting, and analyzing Copilot-related incidents.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Compliance Administrator, Security Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All", "SecurityEvents.Read.All"
```

## Scripts

### Script 1: Copilot Anomaly Detection Report

```powershell
# Detect anomalous Copilot usage patterns that may indicate incidents
$startDate = (Get-Date).AddDays(-7)
$endDate = Get-Date

$copilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

# Identify users with unusually high interaction volume
$userActivity = $copilotEvents | Group-Object UserIds | ForEach-Object {
    [PSCustomObject]@{
        User           = $_.Name
        TotalEvents    = $_.Count
        AvgPerDay      = [math]::Round($_.Count / 7, 1)
        Anomaly        = if ($_.Count / 7 -gt 100) { "HIGH VOLUME" } else { "Normal" }
    }
} | Sort-Object TotalEvents -Descending

$anomalies = $userActivity | Where-Object { $_.Anomaly -eq "HIGH VOLUME" }

Write-Host "Copilot Usage Anomaly Report (Last 7 Days):" -ForegroundColor Cyan
if ($anomalies.Count -gt 0) {
    Write-Warning "$($anomalies.Count) users with anomalous Copilot usage detected"
    $anomalies | Format-Table -AutoSize
} else {
    Write-Host "No anomalous usage patterns detected" -ForegroundColor Green
}

$userActivity | Export-Csv "CopilotAnomalyReport_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: DLP Incident Report for Copilot

```powershell
# Report on DLP incidents triggered by Copilot interactions
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$dlpIncidents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType DLP `
    -ResultSize 5000

$copilotDLP = $dlpIncidents | Where-Object {
    $_.AuditData -like "*Copilot*" -or $_.AuditData -like "*CopilotInteraction*"
}

Write-Host "DLP Incidents Related to Copilot (Last 30 Days):" -ForegroundColor Cyan
Write-Host "Total DLP incidents: $($dlpIncidents.Count)"
Write-Host "Copilot-related DLP incidents: $($copilotDLP.Count)"

$copilotDLP | Select-Object CreationDate, UserIds, Operations |
    Export-Csv "CopilotDLPIncidents_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Incident Log Generator

```powershell
# Generate a structured incident log for Copilot-related events
$incidentId = "INC-COPILOT-$(Get-Date -Format 'yyyyMMdd-HHmm')"

$incidentLog = @"
# Copilot Incident Report
## Incident ID: $incidentId
## Date: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC")

### Incident Details
- **Category:** [Data Exposure / Content Accuracy / Compliance Violation / Unauthorized Usage / Service Disruption]
- **Severity:** [Critical / High / Medium / Low]
- **Detected By:** [Alert Policy / User Report / Audit Review]
- **Affected Users:** [Number and scope]
- **Affected Systems:** Microsoft 365 Copilot — [specific application]

### Timeline
| Time | Event |
|------|-------|
| [Detection time] | Incident detected |
| [Containment time] | Containment actions taken |
| [Resolution time] | Incident resolved |

### Root Cause Analysis
- **Root Cause:** [Describe the underlying cause]
- **Contributing Factors:** [List contributing factors]

### Corrective Actions
| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| [Immediate action] | [Owner] | [Date] | [Status] |
| [Preventive action] | [Owner] | [Date] | [Status] |

### Regulatory Notification Assessment
- **Notification Required:** [Yes / No / Under Review]
- **Regulation:** [Applicable regulation if notification required]
- **Notification Deadline:** [Date]
"@

$incidentLog | Out-File "IncidentReport_$incidentId.md" -Encoding UTF8
Write-Host "Incident report template created: $incidentId" -ForegroundColor Green
```

### Script 4: Incident Trend Analysis

```powershell
# Analyze Copilot incident trends over time
$periods = @(30, 60, 90)
$trends = @()

foreach ($days in $periods) {
    $start = (Get-Date).AddDays(-$days)
    $end = Get-Date

    $alerts = Search-UnifiedAuditLog `
        -StartDate $start -EndDate $end `
        -Operations "AlertTriggered" `
        -ResultSize 5000

    $copilotAlerts = $alerts | Where-Object { $_.AuditData -like "*Copilot*" }

    $trends += [PSCustomObject]@{
        Period        = "$days days"
        TotalAlerts   = $copilotAlerts.Count
        AvgPerWeek    = [math]::Round($copilotAlerts.Count / ($days / 7), 1)
    }
}

Write-Host "Copilot Incident Trend Analysis:" -ForegroundColor Cyan
$trends | Format-Table -AutoSize
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Anomaly detection | Daily | Script 1 |
| DLP incident report | Weekly | Script 2 |
| Incident trend analysis | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate incident response
- See [Troubleshooting](troubleshooting.md) for incident management issues
