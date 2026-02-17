# Control 4.10: Business Continuity and Disaster Recovery — PowerShell Setup

Automation scripts for monitoring Copilot service health, testing business continuity procedures, and generating DR readiness reports.

## Prerequisites

- **Modules:** `Microsoft.Graph`
- **Permissions:** ServiceHealth.Read.All, Reports.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "ServiceHealth.Read.All", "ServiceMessage.Read.All"
```

## Scripts

### Script 1: Copilot Service Health Status Check

```powershell
# Check the health status of all Copilot-dependent services
$services = @(
    "Microsoft365Copilot",
    "Exchange Online",
    "SharePoint Online",
    "Microsoft Teams",
    "OfficeSuite"
)

$healthStatus = Get-MgServiceAnnouncementHealthOverview -All | Where-Object {
    $_.Service -in $services -or $_.Service -like "*Copilot*"
}

Write-Host "Copilot Service Dependency Health:" -ForegroundColor Cyan
foreach ($service in $healthStatus) {
    $color = if ($service.Status -eq "ServiceOperational") { "Green" } else { "Red" }
    Write-Host "  $($service.Service): $($service.Status)" -ForegroundColor $color
}

$healthStatus | Select-Object Service, Status |
    Export-Csv "CopilotServiceHealth_$(Get-Date -Format 'yyyyMMdd-HHmm').csv" -NoTypeInformation
```

### Script 2: Service Health Incident History

```powershell
# Report on recent service health incidents affecting Copilot dependencies
$startDate = (Get-Date).AddDays(-90)

$issues = Get-MgServiceAnnouncementIssue -All | Where-Object {
    $_.StartDateTime -gt $startDate -and
    ($_.Service -like "*Copilot*" -or $_.Service -like "*Teams*" -or
     $_.Service -like "*Exchange*" -or $_.Service -like "*SharePoint*")
}

Write-Host "Service Incidents (Last 90 Days):" -ForegroundColor Cyan
$issues | ForEach-Object {
    [PSCustomObject]@{
        Service     = $_.Service
        Title       = $_.Title
        StartTime   = $_.StartDateTime
        EndTime     = $_.EndDateTime
        Status      = $_.Status
        Impact      = $_.ImpactDescription
    }
} | Sort-Object StartTime -Descending | Format-Table Service, Title, StartTime, Status -AutoSize

$issues | Export-Csv "ServiceIncidentHistory_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: BCP Readiness Assessment

```powershell
# Generate a BCP readiness assessment for Copilot service dependencies
$assessment = @(
    [PSCustomObject]@{Category="Service Monitoring"; Status="Active"; LastTested=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Category="Fallback Procedures"; Status="Documented"; LastTested="Verify manually"},
    [PSCustomObject]@{Category="Communication Templates"; Status="Prepared"; LastTested="Verify manually"},
    [PSCustomObject]@{Category="RTO/RPO Defined"; Status="Documented"; LastTested="Verify manually"},
    [PSCustomObject]@{Category="DR Test Completed"; Status="Verify"; LastTested="Verify last test date"},
    [PSCustomObject]@{Category="Vendor SLA Reviewed"; Status="Verify"; LastTested="Verify review date"}
)

Write-Host "BCP Readiness Assessment — Copilot Services:" -ForegroundColor Cyan
$assessment | Format-Table -AutoSize

$incomplete = $assessment | Where-Object { $_.Status -eq "Verify" }
if ($incomplete) {
    Write-Warning "$($incomplete.Count) items require manual verification"
}

$assessment | Export-Csv "BCPReadiness_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Service Uptime Report

```powershell
# Calculate service uptime percentage for Copilot dependencies
$startDate = (Get-Date).AddDays(-30)
$totalHours = 30 * 24  # 720 hours

$issues = Get-MgServiceAnnouncementIssue -All | Where-Object {
    $_.StartDateTime -gt $startDate -and
    ($_.Service -like "*Copilot*" -or $_.Service -like "*Teams*" -or
     $_.Service -like "*Exchange*" -or $_.Service -like "*SharePoint*")
}

$downtimeHours = 0
foreach ($issue in $issues) {
    if ($issue.EndDateTime) {
        $duration = ($issue.EndDateTime - $issue.StartDateTime).TotalHours
        $downtimeHours += $duration
    }
}

$uptimePercentage = [math]::Round((($totalHours - $downtimeHours) / $totalHours) * 100, 3)

Write-Host "Service Uptime Report (Last 30 Days):" -ForegroundColor Cyan
Write-Host "Total hours: $totalHours"
Write-Host "Downtime hours: $([math]::Round($downtimeHours, 1))"
Write-Host "Uptime: $uptimePercentage%"
Write-Host "Incidents: $($issues.Count)"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Service health check | Every 15 minutes | Script 1 |
| Incident history report | Monthly | Script 2 |
| BCP readiness assessment | Quarterly | Script 3 |
| Uptime report | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate BCP/DR procedures
- See [Troubleshooting](troubleshooting.md) for service continuity issues
