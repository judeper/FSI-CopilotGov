# Control 2.11: Copilot Pages Security and Sharing Controls — PowerShell Setup

Automation scripts for managing and monitoring Copilot Pages security.

## Prerequisites

- SharePoint Online Management Shell
- Microsoft Graph PowerShell SDK
- SharePoint Administrator role

## Scripts

### Script 1: Copilot Pages Sharing Configuration Check

```powershell
# Verify sharing configuration for Copilot Pages storage
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$tenant = Get-SPOTenant
Write-Host "=== Copilot Pages Sharing Configuration ==="
Write-Host "Tenant sharing capability: $($tenant.SharingCapability)"
Write-Host "Default sharing link type: $($tenant.DefaultSharingLinkType)"
Write-Host "Default link permission: $($tenant.DefaultLinkPermission)"
Write-Host ""
Write-Host "Verify Pages-specific settings in Admin Center > Copilot > Pages"
Write-Host "Recommended: Sharing limited to 'Specific people', external sharing disabled"
```

### Script 2: Monitor Pages Activity in Audit Logs

```powershell
# Track Copilot Pages creation and sharing activity
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$pagesEvents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -FreeText "CopilotPage" -ResultSize 5000

$pagesReport = @()
foreach ($event in $pagesEvents) {
    $data = $event.AuditData | ConvertFrom-Json
    $pagesReport += [PSCustomObject]@{
        Date      = $event.CreationDate
        User      = $event.UserIds
        Operation = $event.Operations
        Detail    = $data.ObjectId
    }
}

Write-Host "Copilot Pages events (last 30 days): $($pagesReport.Count)"
$pagesReport | Group-Object Operation | Format-Table Name, Count -AutoSize
$pagesReport | Export-Csv "PagesActivity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Pages Sharing Audit

```powershell
# Audit sharing links on Copilot Pages content
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$sharingEvents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -Operations "SharingSet","SharingInvitationCreated","AnonymousLinkCreated" `
    -FreeText "CopilotPage" -ResultSize 1000

Write-Host "=== Pages Sharing Activity ==="
Write-Host "Sharing events (last 30 days): $($sharingEvents.Count)"

if ($sharingEvents.Count -gt 0) {
    foreach ($event in $sharingEvents) {
        $data = $event.AuditData | ConvertFrom-Json
        Write-Host "  $($event.CreationDate) | $($event.UserIds) | $($event.Operations)"
    }
}
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Pages Sharing Config Check | Monthly | Verify sharing settings remain restrictive |
| Pages Activity Monitor | Weekly | Track creation and sharing patterns |
| Pages Sharing Audit | Weekly | Detect inappropriate sharing of Pages content |

## Next Steps

- See [Verification & Testing](verification-testing.md) for Pages security validation
- See [Troubleshooting](troubleshooting.md) for Pages issues
