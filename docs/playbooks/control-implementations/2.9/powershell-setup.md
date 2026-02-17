# Control 2.9: Defender for Cloud Apps — Copilot Session Controls — PowerShell Setup

Automation scripts for managing and monitoring Defender for Cloud Apps session controls.

## Prerequisites

- Microsoft Defender for Cloud Apps API access
- Security Administrator role
- API token configured for Defender for Cloud Apps

## Scripts

### Script 1: Defender for Cloud Apps Alert Summary

```powershell
# Retrieve recent Copilot-related alerts from Defender for Cloud Apps
# Requires: Microsoft Graph SDK with SecurityAlert permissions

Import-Module Microsoft.Graph.Security
Connect-MgGraph -Scopes "SecurityAlert.Read.All"

$alerts = Get-MgSecurityAlert -Top 100 -OrderBy "createdDateTime desc" |
    Where-Object { $_.Title -match "Copilot|Office 365|session" }

$alertReport = @()
foreach ($alert in $alerts) {
    $alertReport += [PSCustomObject]@{
        Date      = $alert.CreatedDateTime
        Title     = $alert.Title
        Severity  = $alert.Severity
        Status    = $alert.Status
        Category  = $alert.Category
    }
}

Write-Host "=== Copilot Session Alerts (Recent) ==="
Write-Host "Total alerts: $($alertReport.Count)"
$alertReport | Format-Table Date, Title, Severity -AutoSize
$alertReport | Export-Csv "CopilotAlerts_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Session Activity Export

```powershell
# Export Copilot session activity for compliance review
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Reports
Connect-MgGraph -Scopes "AuditLog.Read.All"

$startDate = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")

$activities = Get-MgAuditLogSignIn -Filter "appDisplayName eq 'Office 365' and createdDateTime ge $startDate" `
    -Top 1000 -OrderBy "createdDateTime desc"

$sessionReport = @()
foreach ($activity in $activities) {
    $sessionReport += [PSCustomObject]@{
        Date       = $activity.CreatedDateTime
        User       = $activity.UserPrincipalName
        App        = $activity.AppDisplayName
        Status     = $activity.Status.ErrorCode
        Location   = $activity.Location.City
        DeviceOS   = $activity.DeviceDetail.OperatingSystem
        RiskLevel  = $activity.RiskLevelDuringSignIn
    }
}

Write-Host "Session activities exported: $($sessionReport.Count)"
$sessionReport | Export-Csv "SessionActivity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Policy Compliance Status

```powershell
# Check Defender for Cloud Apps policy status
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Security
Connect-MgGraph -Scopes "Policy.Read.All"

Write-Host "=== Defender for Cloud Apps Policy Status ==="
Write-Host ""
Write-Host "Verify session policies in the Defender portal:"
Write-Host "  security.microsoft.com > Cloud Apps > Policies > Policy management"
Write-Host ""
Write-Host "Key policies to verify:"
Write-Host "  1. FSI Copilot Session Monitoring - Status: Active"
Write-Host "  2. Copilot Content Inspection - Status: Active"
Write-Host "  3. Sensitive Data Alert - Status: Active"
Write-Host ""
Write-Host "Run this check weekly to verify all governance policies remain active."
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Alert Summary Review | Daily | Review and triage session alerts |
| Activity Export | Weekly | Compliance documentation |
| Policy Status Check | Weekly | Verify governance policies are active |

## Next Steps

- See [Verification & Testing](verification-testing.md) for session control validation
- See [Troubleshooting](troubleshooting.md) for session control issues
