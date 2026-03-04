# Control 3.8: Model Risk Management Alignment (OCC 2011-12 / SR 11-7) — PowerShell Setup

Automation scripts for collecting AI inventory data, verifying the Copilot control environment, and exporting usage metrics that feed MRM ongoing monitoring per OCC 2011-12 and SR 11-7.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Directory.Read.All, Reports.Read.All, Purview Compliance Admin role
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession
Connect-MgGraph -Scopes "Directory.Read.All", "Reports.Read.All"
```

## Scripts

### Script 1: AI Inventory — Copilot Licensed Users by Department

```powershell
# Export all users with Microsoft 365 Copilot license, grouped by department
# Feeds MRM requirement: AI tool inventory (OCC 2011-12 Section III.A)
Connect-MgGraph -Scopes "Directory.Read.All"

$copilotSkuId = (Get-MgSubscribedSku |
    Where-Object SkuPartNumber -eq "MICROSOFT_365_COPILOT").SkuId

if (-not $copilotSkuId) {
    Write-Warning "MICROSOFT_365_COPILOT SKU not found in tenant subscriptions"
    return
}

$licensedUsers = Get-MgUser -All `
    -Property "DisplayName,Department,UserPrincipalName,AssignedLicenses,JobTitle" |
    Where-Object { $_.AssignedLicenses.SkuId -contains $copilotSkuId } |
    Select-Object DisplayName, Department, JobTitle, UserPrincipalName

Write-Host "Copilot Licensed Users: $($licensedUsers.Count)" -ForegroundColor Cyan

# Summary by department for AI inventory documentation
$licensedUsers | Group-Object Department |
    Select-Object @{N='Department';E={if ($_.Name) { $_.Name } else { '(Not Set)' }}},
        @{N='LicensedUsers';E={$_.Count}} |
    Sort-Object LicensedUsers -Descending |
    Format-Table -AutoSize

$licensedUsers |
    Export-Csv "CopilotInventory_ByDept_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "AI inventory export complete — attach to MRM documentation" -ForegroundColor Green
```

### Script 2: Control Environment Verification

```powershell
# Verify that required Copilot controls are active: audit logging, DLP, retention
# Feeds MRM requirement: Control environment documentation (OCC 2011-12 Section III.B)

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

# 1. Verify audit logging captures Copilot interactions
$startDate = (Get-Date).AddDays(-7)
$endDate = Get-Date

$auditTest = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 1

if ($auditTest) {
    Write-Host "[PASS] Copilot audit logging is active — records found in last 7 days" -ForegroundColor Green
} else {
    Write-Warning "[CHECK] No CopilotInteraction records in last 7 days — verify UAL is enabled and Copilot is in use"
}

# 2. Verify DLP policies cover Copilot
$dlpPolicies = Get-DlpCompliancePolicy | Where-Object { $_.Enabled -eq $true }
$copilotDlp = $dlpPolicies | Where-Object { $_.Name -match "Copilot|FSI" }

Write-Host "`nDLP Policies (active): $($dlpPolicies.Count) total, $($copilotDlp.Count) Copilot/FSI-related" -ForegroundColor Cyan
$copilotDlp | Select-Object Name, Mode, Enabled | Format-Table -AutoSize

# 3. Verify retention policies cover required locations
$retentionPolicies = Get-RetentionCompliancePolicy |
    Where-Object { $_.Enabled -eq $true }

Write-Host "Retention Policies (active): $($retentionPolicies.Count)" -ForegroundColor Cyan
$retentionPolicies | Select-Object Name,
    @{N='Exchange';E={$_.ExchangeLocation.Count -gt 0}},
    @{N='SharePoint';E={$_.SharePointLocation.Count -gt 0}},
    @{N='OneDrive';E={$_.OneDriveLocation.Count -gt 0}},
    @{N='TeamsChat';E={$_.TeamsChatLocation.Count -gt 0}},
    @{N='TeamsChannel';E={$_.TeamsChannelLocation.Count -gt 0}} |
    Format-Table -AutoSize

Write-Host "`nInclude output in MRM control environment section" -ForegroundColor Green
```

### Script 3: Copilot Usage Metrics Export (Graph API)

```powershell
# Export Copilot usage data for MRM ongoing monitoring
# Feeds MRM requirement: Ongoing monitoring plan (OCC 2011-12 Section III.C)
Connect-MgGraph -Scopes "Reports.Read.All"

# Summary usage report (available periods: D7, D30, D90, D180)
$summary = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/microsoft365CopilotUsageSummary(period='D30')"

$summary | ConvertTo-Json -Depth 5 |
    Out-File "CopilotUsageSummary_$(Get-Date -Format 'yyyyMMdd').json"
Write-Host "Usage summary exported (30-day period)" -ForegroundColor Cyan

# Per-user detail report (CSV download)
Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/getMicrosoft365CopilotUserDetailReport(period='D30')" `
    -OutputFilePath "CopilotUserDetail_$(Get-Date -Format 'yyyyMMdd').csv"
Write-Host "Per-user detail exported" -ForegroundColor Cyan

Write-Host "`nAttach usage reports to MRM periodic review documentation" -ForegroundColor Green
```

### Script 4: Risky AI Usage Alert Summary

```powershell
# Export Copilot audit data with risk indicators for MRM documentation
# Feeds MRM requirement: Risk indicators and escalation (OCC 2011-12 Section III.D)

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$events = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$parsed = $events | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date              = $_.CreationDate
        User              = $_.UserIds
        AppHost           = $data.AppHost
        Operation         = $_.Operations
        SensitivityLabels = ($data.AccessedResources.SensitivityLabelId |
            Where-Object { $_ }) -join "; "
        JailbreakDetected = ($data.Messages |
            Where-Object { $_.JailbreakDetected -eq $true }).Count -gt 0
    }
}

$riskyEvents = $parsed | Where-Object {
    $_.JailbreakDetected -eq $true -or $_.SensitivityLabels -ne ""
}

Write-Host "Copilot Interactions (Last 30 Days): $($parsed.Count)" -ForegroundColor Cyan
Write-Host "Events with risk indicators: $($riskyEvents.Count)" -ForegroundColor Yellow
Write-Host "  Jailbreak attempts: $(($parsed | Where-Object JailbreakDetected -eq $true).Count)"
Write-Host "  Accessed labeled content: $(($parsed | Where-Object { $_.SensitivityLabels -ne '' }).Count)"

$parsed | Export-Csv "CopilotAudit_MRM_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

# LIMITATION: DSPM for AI provides prompt/response content and oversharing alerts
# but has no PowerShell API — review manually at: Purview portal > DSPM for AI
# LIMITATION: IRM Risky AI usage alerts are portal-only — review at:
#   Purview portal > Insider Risk Management > Alerts
Write-Host "`nDSPM for AI and IRM alerts require manual review in the Purview portal" -ForegroundColor Yellow
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| AI inventory refresh | Quarterly | Script 1 |
| Control environment verification | Monthly | Script 2 |
| Usage metrics export | Monthly | Script 3 |
| Risky AI usage audit | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate model risk controls
- See [Troubleshooting](troubleshooting.md) for monitoring issues
