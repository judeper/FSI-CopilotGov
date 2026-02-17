# Control 2.10: Insider Risk Detection for Copilot Usage — PowerShell Setup

Automation scripts for monitoring and reporting on insider risk detection for Copilot.

## Prerequisites

- Security & Compliance PowerShell
- Insider Risk Management Administrator role
- Microsoft 365 E5 Compliance license

## Scripts

### Script 1: Insider Risk Policy Status Report

```powershell
# Check insider risk policy configurations and status
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$policies = Get-InsiderRiskPolicy -ErrorAction SilentlyContinue

if ($policies) {
    Write-Host "=== Insider Risk Policies ==="
    foreach ($policy in $policies) {
        Write-Host "Policy: $($policy.Name)"
        Write-Host "  Enabled: $($policy.Enabled)"
        Write-Host "  Template: $($policy.InsiderRiskPolicyTemplate)"
        Write-Host "  Created: $($policy.CreatedDate)"
        Write-Host ""
    }
} else {
    Write-Host "No insider risk policies found. Configure policies in Microsoft Purview."
}
```

### Script 2: Copilot Usage Anomaly Detection

```powershell
# Detect anomalous Copilot usage patterns from audit logs
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$copilotEvents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -RecordType "CopilotInteraction" -ResultSize 5000

$userActivity = $copilotEvents | Group-Object UserIds | ForEach-Object {
    [PSCustomObject]@{
        User         = $_.Name
        EventCount   = $_.Count
        FirstEvent   = ($_.Group | Sort-Object CreationDate | Select-Object -First 1).CreationDate
        LastEvent    = ($_.Group | Sort-Object CreationDate -Descending | Select-Object -First 1).CreationDate
    }
} | Sort-Object EventCount -Descending

# Identify outliers (users with activity > 2x average)
$avgActivity = ($userActivity | Measure-Object -Property EventCount -Average).Average
$outliers = $userActivity | Where-Object { $_.EventCount -gt ($avgActivity * 2) }

Write-Host "=== Copilot Usage Anomaly Report ==="
Write-Host "Total users: $($userActivity.Count)"
Write-Host "Average interactions: $([math]::Round($avgActivity, 1))"
Write-Host "Outlier users (>2x average): $($outliers.Count)"

if ($outliers.Count -gt 0) {
    $outliers | Format-Table User, EventCount -AutoSize
}

$userActivity | Export-Csv "CopilotUsageAnalysis_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Off-Hours Copilot Activity Report

```powershell
# Detect Copilot usage outside business hours
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-14).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$events = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -RecordType "CopilotInteraction" -ResultSize 5000

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
| Policy Status Report | Weekly | Verify insider risk policies are active |
| Usage Anomaly Detection | Weekly | Identify unusual Copilot usage patterns |
| Off-Hours Activity Report | Weekly | Flag off-hours access for review |

## Next Steps

- See [Verification & Testing](verification-testing.md) for insider risk validation
- See [Troubleshooting](troubleshooting.md) for insider risk issues
