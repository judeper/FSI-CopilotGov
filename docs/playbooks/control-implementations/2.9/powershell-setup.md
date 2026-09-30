# Control 2.9: Defender for Cloud Apps — Copilot Session Controls — PowerShell Setup

Automation scripts for managing and monitoring Defender for Cloud Apps session controls.

## Prerequisites

- Microsoft Graph PowerShell SDK (optional, for supplemental exports)
- Security Administrator role
- Access to the Microsoft Defender portal for authoritative session-policy verification

## Scripts

> Microsoft Learn pages in scope for this control document session-policy configuration in the Defender portal rather than a PowerShell cmdlet surface. Use the scripts below for supplemental telemetry exports, and verify actual session-policy settings in **Microsoft Defender portal > Cloud Apps > Policies > Policy management**.

### Script 1: Supplemental XDR Alert Summary

```powershell
# Retrieve recent alerts that may be relevant to CA App Control, AI governance,
# or agent monitoring. This is supplemental telemetry only.
# The legacy /security/alerts API retires on October 15, 2026 and will stop
# returning data after that date, so use alerts_v2.
# Requires: Microsoft Graph SDK with SecurityAlert.Read.All

Import-Module Microsoft.Graph.Security
Connect-MgGraph -Scopes "SecurityAlert.Read.All"

$alerts = Get-MgSecurityAlertV2 -Top 200 -Sort "createdDateTime DESC" |
    Where-Object {
        $_.Title -match "Copilot|AI|session|SharePoint|OneDrive" -or
        $_.ServiceSource -eq "microsoftDefenderForCloudApps" -or
        $_.DetectionSource -in @("cloudAppSecurity", "appGovernancePolicy", "appGovernanceDetection")
    }

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

Write-Host "=== Cloud Apps / AI Governance Alerts (Supplemental) ==="
Write-Host "Total alerts: $($alertReport.Count)"
$alertReport | Format-Table Date, Title, Severity -AutoSize
$alertReport | Export-Csv "CloudAppsAlerts_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Browser-Session Sign-In Export

```powershell
# Export recent Microsoft 365 sign-ins as supplemental evidence for browser
# session review. Use MDCA policy reports for routed session matches.
# Requires: Microsoft Graph SDK with AuditLog.Read.All and Directory.Read.All

Import-Module Microsoft.Graph.Reports
Connect-MgGraph -Scopes "AuditLog.Read.All","Directory.Read.All"

$activities = Get-MgAuditLogSignIn -Top 1000 -Sort "createdDateTime DESC" |
    Where-Object {
        $_.AppDisplayName -match "Office|Microsoft 365|SharePoint|OneDrive|Teams"
    }

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

### Script 3: Portal Verification Checklist Export

```powershell
# Export a checklist of the portal locations that must be reviewed for this
# control because Microsoft documents them as the authoritative surfaces.

$checks = @(
    [PSCustomObject]@{
        Area = "Conditional Access App Control apps"
        Path = "Defender > Settings > Cloud Apps > Connected apps > Conditional Access App Control apps"
        Expectation = "Target Microsoft 365 web apps are enabled"
    }
    [PSCustomObject]@{
        Area = "Session policies"
        Path = "Defender > Cloud Apps > Policies > Policy management > Conditional Access"
        Expectation = "Monitor-only redirect validation plus detailed audit/block policies as applicable"
    }
    [PSCustomObject]@{
        Area = "Policy report"
        Path = "Defender > Cloud Apps > Policies > Policy management"
        Expectation = "Recent routed sign-ins and session-policy matches"
    }
    [PSCustomObject]@{
        Area = "Generative AI catalog"
        Path = "Defender > Cloud Apps > Cloud app catalog"
        Expectation = "Generative AI risk-score review documented"
    }
    [PSCustomObject]@{
        Area = "Cloud Discovery"
        Path = "Defender > Cloud Apps > Cloud discovery > Discovered apps"
        Expectation = "High-risk AI apps sanctioned or unsanctioned per policy"
    }
)

$checks | Format-Table Area, Path, Expectation -AutoSize
$checks | Export-Csv "CloudAppsPortalChecklist_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Alert Summary Review | Daily | Review and triage supplemental MDCA/XDR alerts |
| Sign-In Export | Weekly | Supplemental browser-session context |
| Portal Checklist Export | Weekly | Verify authoritative MDCA governance settings |

## Next Steps

- See [Verification & Testing](verification-testing.md) for session control validation
- See [Troubleshooting](troubleshooting.md) for session control issues
- Back to [Control 2.9](../../../controls/pillar-2-security/2.9-defender-cloud-apps.md)
