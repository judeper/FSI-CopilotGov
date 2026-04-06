# Control 4.9: Incident Reporting and Root Cause Analysis — PowerShell Setup

Automation scripts for detecting, reporting, and analyzing Copilot-related incidents.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Purview Compliance Admin, Security Administrator
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
# Generate a data-driven incident log from Copilot audit anomalies detected in Scripts 1-2
$incidentId = "INC-COPILOT-$(Get-Date -Format 'yyyyMMdd-HHmm')"

# Pull anomaly data from the most recent anomaly report
$anomalyReport = "CopilotAnomalyReport_$(Get-Date -Format 'yyyyMMdd').csv"
if (-not (Test-Path $anomalyReport)) {
    Write-Warning "Run Script 1 first to generate anomaly data. File not found: $anomalyReport"
    return
}

$anomalyData = Import-Csv $anomalyReport | Where-Object { $_.Anomaly -eq "HIGH VOLUME" }
if ($anomalyData.Count -eq 0) {
    Write-Host "No anomalous users found — no incident report generated." -ForegroundColor Green
    return
}

# Retrieve detailed audit records for flagged users
$startDate = (Get-Date).AddDays(-7)
$endDate = Get-Date
$affectedUsers = $anomalyData.User

$detailedEvents = foreach ($user in $affectedUsers) {
    Search-UnifiedAuditLog `
        -StartDate $startDate -EndDate $endDate `
        -RecordType CopilotInteraction `
        -UserIds $user -ResultSize 5000
}

# Parse accessed resources and sensitivity labels from AuditData
$resourceSummary = $detailedEvents | ForEach-Object {
    $audit = $_.AuditData | ConvertFrom-Json
    $audit.AccessedResources | ForEach-Object {
        [PSCustomObject]@{
            User              = $audit.UserId
            ResourceName      = $_.Name
            SensitivityLabelId = $_.SensitivityLabelId
            Timestamp         = $audit.CreationTime
        }
    }
}

$userSummary = $anomalyData | ForEach-Object {
    "- **$($_.User):** $($_.TotalEvents) events ($($_.AvgPerDay) avg/day)"
} | Out-String

$firstEvent = ($detailedEvents | Sort-Object CreationDate | Select-Object -First 1).CreationDate
$lastEvent = ($detailedEvents | Sort-Object CreationDate -Descending | Select-Object -First 1).CreationDate
$labeledResources = ($resourceSummary | Where-Object { $_.SensitivityLabelId }).Count
$totalResources = $resourceSummary.Count

$incidentLog = @"
# Copilot Incident Report
## Incident ID: $incidentId
## Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC")

### Detection Summary
- **Detection Method:** Automated anomaly detection (>100 Copilot events/day threshold)
- **Analysis Period:** $($startDate.ToString("yyyy-MM-dd")) to $($endDate.ToString("yyyy-MM-dd"))
- **Affected Users:** $($anomalyData.Count)
- **Total Flagged Events:** $(($anomalyData | Measure-Object TotalEvents -Sum).Sum)

### Affected Users
$userSummary

### Timeline
| Metric | Value |
|--------|-------|
| First flagged event | $firstEvent |
| Last flagged event | $lastEvent |
| Detection timestamp | $(Get-Date -Format "yyyy-MM-dd HH:mm:ss") |

### Accessed Resources
- **Total resources accessed:** $totalResources
- **Resources with sensitivity labels:** $labeledResources

### Root Cause Analysis
- **Root Cause:** [Pending investigation — review accessed resources for data exposure indicators]
- **Contributing Factors:** [Review user access scope and Copilot surface usage patterns]

### Corrective Actions
| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Review flagged user access logs | [Assign] | [Date] | Pending |
| Verify no sensitive data exposure | [Assign] | [Date] | Pending |

### Regulatory Notification Assessment
- **Notification Required:** [Under Review — assess accessed resources for NPI]
- **Applicable Regulation:** [e.g., SEC Reg S-P if NPI exposure confirmed]
"@

$incidentLog | Out-File "IncidentReport_$incidentId.md" -Encoding UTF8
$resourceSummary | Export-Csv "IncidentResources_$incidentId.csv" -NoTypeInformation
Write-Host "Incident report created: IncidentReport_$incidentId.md" -ForegroundColor Green
Write-Host "Resource detail exported: IncidentResources_$incidentId.csv" -ForegroundColor Green
```

### Script 4: Copilot Interaction Risk Analysis

```powershell
# Analyze CopilotInteraction audit records for risk indicators
$periods = @(30, 60, 90)
$trends = @()

foreach ($days in $periods) {
    $start = (Get-Date).AddDays(-$days)
    $end = Get-Date

    $copilotEvents = Search-UnifiedAuditLog `
        -StartDate $start -EndDate $end `
        -RecordType CopilotInteraction `
        -ResultSize 5000

    # Parse AuditData JSON for risk indicators
    $riskIndicators = $copilotEvents | ForEach-Object {
        $audit = $_.AuditData | ConvertFrom-Json
        $jailbreak = ($audit.Messages | Where-Object { $_.JailbreakDetected -eq $true }).Count
        $resourceCount = ($audit.AccessedResources | Measure-Object).Count
        $labeledCount = ($audit.AccessedResources | Where-Object { $_.SensitivityLabelId }).Count
        [PSCustomObject]@{
            User                = $_.UserIds
            Timestamp           = $_.CreationDate
            JailbreakDetected   = $jailbreak -gt 0
            AccessedResources   = $resourceCount
            LabeledResources    = $labeledCount
        }
    }

    $jailbreakCount = ($riskIndicators | Where-Object { $_.JailbreakDetected }).Count
    $highResourceEvents = ($riskIndicators | Where-Object { $_.AccessedResources -gt 10 }).Count
    $labeledAccessEvents = ($riskIndicators | Where-Object { $_.LabeledResources -gt 0 }).Count

    $trends += [PSCustomObject]@{
        Period              = "$days days"
        TotalInteractions   = $copilotEvents.Count
        JailbreakFlags      = $jailbreakCount
        HighResourceAccess  = $highResourceEvents
        LabeledFileAccess   = $labeledAccessEvents
        AvgPerWeek          = [math]::Round($copilotEvents.Count / ($days / 7), 1)
    }
}

Write-Host "Copilot Interaction Risk Trend Analysis:" -ForegroundColor Cyan
$trends | Format-Table -AutoSize

# Flag any jailbreak detections as high priority
$jailbreakTotal = ($trends | Measure-Object JailbreakFlags -Sum).Sum
if ($jailbreakTotal -gt 0) {
    Write-Warning "$jailbreakTotal jailbreak detection(s) found — review affected interactions immediately"
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Anomaly detection | Daily | Script 1 |
| DLP incident report | Weekly | Script 2 |
| Risk trend analysis | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate incident response
- See [Troubleshooting](troubleshooting.md) for incident management issues
