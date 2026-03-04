# Control 4.10: Business Continuity and Disaster Recovery — PowerShell Setup

Automation scripts for monitoring Copilot service health, testing business continuity procedures, and generating DR readiness reports.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** ServiceHealth.Read.All, Reports.Read.All, Compliance Administrator (for DLP/UAL checks)
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
# Automated BCP readiness assessment for Copilot service dependencies
Write-Host "BCP Readiness Assessment — Copilot Services:" -ForegroundColor Cyan
Write-Host "=============================================`n"

$assessment = @()

# --- Automated Check: UAL enabled ---
try {
    Connect-ExchangeOnline -ShowBanner:$false
    $ualConfig = Get-AdminAuditLogConfig
    $ualStatus = if ($ualConfig.UnifiedAuditLogIngestionEnabled) { "Enabled" } else { "NOT ENABLED" }
    $assessment += [PSCustomObject]@{
        Category="Unified Audit Log"; Check="UAL ingestion enabled"; Status=$ualStatus;
        Method="Automated"; Detail="Get-AdminAuditLogConfig"
    }
} catch {
    $assessment += [PSCustomObject]@{
        Category="Unified Audit Log"; Check="UAL ingestion enabled"; Status="ERROR";
        Method="Automated"; Detail=$_.Exception.Message
    }
}

# --- Automated Check: Copilot-related DLP policies exist ---
try {
    $dlpPolicies = Get-DlpCompliancePolicy | Where-Object {
        $_.Name -like "*Copilot*" -or $_.Name -like "*AI*" -or $_.Name -like "*FSI*"
    }
    $dlpStatus = if ($dlpPolicies.Count -gt 0) { "$($dlpPolicies.Count) policy(ies) found" } else { "NO POLICIES FOUND" }
    $assessment += [PSCustomObject]@{
        Category="DLP for Copilot"; Check="Copilot/AI DLP policies configured"; Status=$dlpStatus;
        Method="Automated"; Detail=($dlpPolicies.Name -join ", ")
    }
} catch {
    $assessment += [PSCustomObject]@{
        Category="DLP for Copilot"; Check="Copilot/AI DLP policies configured"; Status="ERROR";
        Method="Automated"; Detail=$_.Exception.Message
    }
}

# --- Automated Check: Copilot service health ---
try {
    $copilotHealth = Get-MgServiceAnnouncementHealthOverview -All | Where-Object {
        $_.Service -like "*Copilot*"
    }
    foreach ($svc in $copilotHealth) {
        $assessment += [PSCustomObject]@{
            Category="Service Health"; Check="$($svc.Service) status"; Status=$svc.Status;
            Method="Automated"; Detail="Get-MgServiceAnnouncementHealthOverview"
        }
    }
} catch {
    $assessment += [PSCustomObject]@{
        Category="Service Health"; Check="Copilot service status"; Status="ERROR";
        Method="Automated"; Detail=$_.Exception.Message
    }
}

# --- Automated Check: Active Copilot service incidents ---
try {
    $activeIncidents = Get-MgServiceAnnouncementIssue -All | Where-Object {
        $_.Service -like "*Copilot*" -and $_.Status -ne "Resolved"
    }
    if ($activeIncidents.Count -gt 0) {
        foreach ($incident in $activeIncidents) {
            $assessment += [PSCustomObject]@{
                Category="Active Incidents"; Check=$incident.Title; Status=$incident.Status;
                Method="Automated"; Detail="Started: $($incident.StartDateTime)"
            }
        }
    } else {
        $assessment += [PSCustomObject]@{
            Category="Active Incidents"; Check="Copilot service incidents"; Status="None active";
            Method="Automated"; Detail="Get-MgServiceAnnouncementIssue"
        }
    }
} catch {
    $assessment += [PSCustomObject]@{
        Category="Active Incidents"; Check="Copilot service incidents"; Status="ERROR";
        Method="Automated"; Detail=$_.Exception.Message
    }
}

# --- Manual items (structured output) ---
$manualItems = @(
    [PSCustomObject]@{
        Category="DR Testing"; Check="Disaster recovery test completed"; Status="Manual verification required";
        Method="Manual"; Detail="Verify last DR test date and results with BCP team"
    },
    [PSCustomObject]@{
        Category="Backup Verification"; Check="Backup and restore procedures validated"; Status="Manual verification required";
        Method="Manual"; Detail="Confirm backup scope includes Copilot-adjacent data (Exchange, SharePoint, OneDrive)"
    },
    [PSCustomObject]@{
        Category="Fallback Procedures"; Check="Copilot-unavailable fallback documented"; Status="Manual verification required";
        Method="Manual"; Detail="Verify documented procedures for operating without Copilot during outages"
    },
    [PSCustomObject]@{
        Category="Vendor SLA"; Check="Microsoft SLA reviewed for Copilot services"; Status="Manual verification required";
        Method="Manual"; Detail="Verify SLA terms reviewed within last 12 months"
    }
)
$assessment += $manualItems

# Display results
$assessment | Format-Table Category, Check, Status, Method -AutoSize

$manualCount = ($assessment | Where-Object { $_.Method -eq "Manual" }).Count
$failedAuto = ($assessment | Where-Object { $_.Method -eq "Automated" -and $_.Status -match "NOT|ERROR|NO " }).Count
if ($manualCount -gt 0) {
    Write-Warning "$manualCount item(s) require manual verification"
}
if ($failedAuto -gt 0) {
    Write-Warning "$failedAuto automated check(s) returned issues — review above"
}

$assessment | Export-Csv "BCPReadiness_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Service Uptime and Active Incident Report

```powershell
# Calculate service uptime percentage for Copilot dependencies and check active incidents
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

# Check for active (unresolved) incidents affecting Copilot services
Write-Host "`nActive Copilot Service Incidents:" -ForegroundColor Yellow
$activeIncidents = Get-MgServiceAnnouncementIssue -All | Where-Object {
    $_.Status -ne "Resolved" -and
    ($_.Service -like "*Copilot*" -or $_.Service -like "*Teams*" -or
     $_.Service -like "*Exchange*" -or $_.Service -like "*SharePoint*")
}

if ($activeIncidents.Count -gt 0) {
    Write-Warning "$($activeIncidents.Count) active incident(s) detected"
    $activeIncidents | Select-Object Id, Service, Title, Status, StartDateTime |
        Format-Table -AutoSize
} else {
    Write-Host "  No active incidents affecting Copilot dependencies" -ForegroundColor Green
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Service health check | Every 15 minutes | Script 1 |
| Incident history report | Monthly | Script 2 |
| BCP readiness assessment | Quarterly | Script 3 |
| Uptime and incident report | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate BCP/DR procedures
- See [Troubleshooting](troubleshooting.md) for service continuity issues
