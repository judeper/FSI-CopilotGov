# Control 2.5: Data Minimization and Grounding Scope — PowerShell Setup

Automation scripts for implementing and monitoring data minimization controls for Copilot.

## Prerequisites

- SharePoint Online Management Shell
- Microsoft Graph PowerShell SDK
- SharePoint Administrator role

## Scripts

### Script 1: Grounding Scope Inventory

```powershell
# Generate inventory of content accessible to Copilot for grounding
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

# Check if RSS is enabled (primary grounding control)
$rssMode = Get-SPOTenantRestrictedSearchMode -ErrorAction SilentlyContinue

if ($rssMode.Mode -eq "Restricted") {
    $allowedSites = Get-SPOTenantRestrictedSearchAllowedList
    Write-Host "RSS Mode: Restricted — $($allowedSites.Count) sites in grounding scope"
    $allowedSites | ForEach-Object { Write-Host "  $_" }
} else {
    $allSites = Get-SPOSite -Limit All -IncludePersonalSite $false
    Write-Host "RSS Mode: Not Restricted — ALL $($allSites.Count) sites in grounding scope"
    Write-Host "WARNING: Data minimization requires RSS or alternative scoping controls."
}
```

### Script 2: Content Volume Analysis by Scope

```powershell
# Analyze content volume within the Copilot grounding scope
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$allowedSites = Get-SPOTenantRestrictedSearchAllowedList -ErrorAction SilentlyContinue
$scopeAnalysis = @()
$totalStorageMB = 0

foreach ($siteUrl in $allowedSites) {
    $site = Get-SPOSite -Identity $siteUrl -Detailed -ErrorAction SilentlyContinue
    if ($site) {
        $totalStorageMB += $site.StorageUsageCurrent
        $scopeAnalysis += [PSCustomObject]@{
            Url              = $siteUrl
            Title            = $site.Title
            StorageMB        = [math]::Round($site.StorageUsageCurrent, 2)
            SensitivityLabel = $site.SensitivityLabel
            LastModified     = $site.LastContentModifiedDate
        }
    }
}

Write-Host "=== Grounding Scope Analysis ==="
Write-Host "Sites in scope: $($scopeAnalysis.Count)"
Write-Host "Total content volume: $([math]::Round($totalStorageMB / 1024, 2)) GB"

$scopeAnalysis | Export-Csv "GroundingScope_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Data Minimization Compliance Check

```powershell
# Verify data minimization controls are in place
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$checks = @()
$rssMode = Get-SPOTenantRestrictedSearchMode -ErrorAction SilentlyContinue

$checks += [PSCustomObject]@{
    Control  = "Restricted SharePoint Search"
    Status   = if ($rssMode.Mode -eq "Restricted") { "PASS" } else { "FAIL" }
    Detail   = "RSS Mode: $($rssMode.Mode)"
}

$tenant = Get-SPOTenant
$checks += [PSCustomObject]@{
    Control  = "External Sharing Restricted"
    Status   = if ($tenant.SharingCapability -ne "ExternalUserAndGuestSharing") { "PASS" } else { "FAIL" }
    Detail   = "Sharing: $($tenant.SharingCapability)"
}

Write-Host "=== Data Minimization Compliance ==="
$checks | Format-Table Control, Status, Detail -AutoSize
$checks | Export-Csv "DataMinimizationCheck_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Grounding Scope Inventory | Monthly | Track what content Copilot can access |
| Content Volume Analysis | Quarterly | Monitor scope growth for governance review |
| Compliance Check | Weekly | Verify minimization controls remain active |

## Next Steps

- See [Verification & Testing](verification-testing.md) for minimization validation
- See [Troubleshooting](troubleshooting.md) for scope issues
