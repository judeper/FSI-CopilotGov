# Control 4.12: Change Management for Copilot Feature Rollouts — PowerShell Setup

Automation scripts for monitoring Copilot feature changes, tracking rollouts, and generating change management reports.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** ServiceMessage.Read.All, AuditLog.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "ServiceMessage.Read.All", "AuditLog.Read.All"
```

## Scripts

### Script 1: Monitor Message Center for Copilot Updates

```powershell
# Retrieve Copilot-related Message Center announcements
$messages = Get-MgServiceAnnouncementMessage -All | Where-Object {
    $_.Title -like "*Copilot*" -or $_.Body.Content -like "*Copilot*"
} | Sort-Object StartDateTime -Descending | Select-Object -First 20

Write-Host "Recent Copilot Message Center Announcements:" -ForegroundColor Cyan
$messages | ForEach-Object {
    [PSCustomObject]@{
        Date     = $_.StartDateTime.ToString("yyyy-MM-dd")
        Category = $_.Category
        Title    = $_.Title.Substring(0, [Math]::Min($_.Title.Length, 80))
        ActionBy = $_.ActionRequiredByDateTime
    }
} | Format-Table -AutoSize

$messages | Select-Object StartDateTime, Category, Title, Severity |
    Export-Csv "CopilotMessageCenter_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Track Copilot Configuration Changes

```powershell
# Audit all Copilot-related configuration changes in the tenant
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$configChanges = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType AzureActiveDirectory `
    -ResultSize 5000

$copilotChanges = $configChanges | Where-Object {
    $_.AuditData -like "*Copilot*" -or
    $_.AuditData -like "*CopilotPolicy*" -or
    $_.Operations -like "*Set-*Copilot*"
}

Write-Host "Copilot Configuration Changes (Last 30 Days):" -ForegroundColor Cyan
Write-Host "Total changes detected: $($copilotChanges.Count)"

$copilotChanges | Select-Object CreationDate, UserIds, Operations |
    Format-Table -AutoSize

$copilotChanges | Export-Csv "CopilotConfigChanges_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Release Preference Verification

```powershell
# Verify the organization's release preference settings
$orgSettings = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/organization" `
    -OutputType PSObject

Write-Host "Organization Release Settings:" -ForegroundColor Cyan
Write-Host "Organization: $($orgSettings.value[0].displayName)"
Write-Host ""
Write-Host "Release preferences must be verified in the M365 Admin Center:"
Write-Host "  Path: Settings > Org settings > Organization profile > Release preferences"
Write-Host "  Recommended: Targeted release for selected users"
Write-Host ""
Write-Host "Verify the following:"
Write-Host "  1. Targeted release group includes the validation team"
Write-Host "  2. General release users do not receive new features until validated"
Write-Host "  3. Release preference was last reviewed within the past 90 days"
```

### Script 4: Change Management Compliance Report

```powershell
# Generate a change management compliance report
$reportDate = Get-Date -Format "yyyy-MM-dd"

$changes = @(
    [PSCustomObject]@{ChangeID="CHG-001"; Description="Enable Copilot in Excel"; Type="Normal"; CABApproved="Yes"; DateApplied=$reportDate; ImpactAssessment="Completed"},
    [PSCustomObject]@{ChangeID="CHG-002"; Description="Update DLP for Copilot"; Type="Normal"; CABApproved="Yes"; DateApplied=$reportDate; ImpactAssessment="Completed"},
    [PSCustomObject]@{ChangeID="CHG-003"; Description="New user onboarding to Copilot"; Type="Standard"; CABApproved="Pre-approved"; DateApplied=$reportDate; ImpactAssessment="N/A"}
)

Write-Host "Change Management Compliance Report:" -ForegroundColor Cyan
Write-Host "Report Date: $reportDate"
Write-Host ""
$changes | Format-Table -AutoSize

$unapproved = $changes | Where-Object { $_.CABApproved -eq "No" }
if ($unapproved) {
    Write-Warning "$($unapproved.Count) changes were applied without CAB approval"
} else {
    Write-Host "All changes are compliant with CAB approval requirements" -ForegroundColor Green
}

$changes | Export-Csv "ChangeManagementReport_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Message Center monitoring | Daily | Script 1 |
| Configuration change audit | Weekly | Script 2 |
| Release preference verification | Quarterly | Script 3 |
| Change management compliance report | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate change management
- See [Troubleshooting](troubleshooting.md) for change management issues
