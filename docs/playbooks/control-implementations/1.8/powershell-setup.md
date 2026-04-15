# Control 1.8: Information Architecture Review — PowerShell Setup

Automation scripts for analyzing and documenting the Microsoft 365 information architecture.

## Prerequisites

### Required Modules

- SharePoint Online Management Shell
- PnP PowerShell (see custom app registration below)
- Microsoft Graph PowerShell SDK
- SharePoint Admin role

### PnP PowerShell: Custom App Registration Required

The shared multi-tenant PnP Management Shell Entra ID app was retired on September 9, 2024. All PnP PowerShell scripts now require a tenant-specific Entra ID app registration. Complete this one-time setup before running any PnP scripts in this playbook.

```powershell
# One-time setup: Register a tenant-specific app for PnP PowerShell
Register-PnPEntraIDAppForInteractiveLogin `
    -ApplicationName "PnP Governance Shell - [YourOrg]" `
    -Tenant "yourorg.onmicrosoft.com" `
    -SharePointDelegated `
    -GraphDelegated `
    -Interactive
```

Save the returned Client ID — you will need it for all `Connect-PnPOnline` calls in this playbook. If you have already registered this app for another control (e.g., 1.6), you can use the same Client ID here.

## Scripts

### Script 1: Site Architecture Inventory

```powershell
# Generate comprehensive site architecture inventory
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sites = Get-SPOSite -Limit All -IncludePersonalSite Exclude
$inventory = @()

foreach ($site in $sites) {
    $detail = Get-SPOSite -Identity $site.Url -Detailed
    $inventory += [PSCustomObject]@{
        Url              = $site.Url
        Title            = $site.Title
        Template         = $site.Template
        HubSiteId        = $detail.HubSiteId
        IsHubSite        = $detail.IsHubSite
        SensitivityLabel = $detail.SensitivityLabel
        StorageMB        = [math]::Round($detail.StorageUsageCurrent, 2)
        LastModified     = $detail.LastContentModifiedDate
        Owner            = $detail.Owner
        GroupId          = $detail.GroupId
    }
}

$hubSites = ($inventory | Where-Object IsHubSite).Count
$orphaned = ($inventory | Where-Object { -not $_.IsHubSite -and $_.HubSiteId -eq "00000000-0000-0000-0000-000000000000" }).Count

Write-Host "=== Information Architecture Summary ==="
Write-Host "Total sites: $($inventory.Count)"
Write-Host "Hub sites: $hubSites"
Write-Host "Orphaned sites (no hub association): $orphaned"

$inventory | Export-Csv "SiteArchitecture.csv" -NoTypeInformation
```

### Script 2: Hub Site Relationship Map

```powershell
# Map hub site relationships for architecture documentation
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$hubSites = Get-SPOHubSite
$hubMap = @()

foreach ($hub in $hubSites) {
    $associatedSites = Get-SPOSite -Limit All | Where-Object {
        $_.HubSiteId -eq $hub.SiteId -and $_.Url -ne $hub.SiteUrl
    }
    $hubMap += [PSCustomObject]@{
        HubName          = $hub.Title
        HubUrl           = $hub.SiteUrl
        AssociatedCount  = $associatedSites.Count
        AssociatedSites  = ($associatedSites.Title -join "; ")
    }
}

$hubMap | Format-Table HubName, AssociatedCount -AutoSize
$hubMap | Export-Csv "HubSiteMap_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Content Type Usage Analysis

```powershell
# Analyze content type usage across sites
# Requires: PnP PowerShell with custom app registration (see Prerequisites)

Import-Module PnP.PowerShell

$targetSites = Import-Csv "SiteArchitecture.csv" | Select-Object -First 50
$contentTypeReport = @()
$clientId = "<your-app-id>"  # Client ID from Register-PnPEntraIDAppForInteractiveLogin

foreach ($site in $targetSites) {
    Connect-PnPOnline -Url $site.Url -ClientId $clientId -Interactive
    $contentTypes = Get-PnPContentType

    foreach ($ct in $contentTypes) {
        if (-not $ct.Hidden) {
            $contentTypeReport += [PSCustomObject]@{
                Site          = $site.Url
                ContentType   = $ct.Name
                Group         = $ct.Group
                ReadOnly      = $ct.ReadOnly
            }
        }
    }
    Disconnect-PnPOnline
}

$uniqueCTs = ($contentTypeReport | Select-Object -Unique ContentType).Count
Write-Host "Found $uniqueCTs unique content types across $($targetSites.Count) sites."
$contentTypeReport | Export-Csv "ContentTypeUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Site Architecture Inventory | Quarterly | Track architecture changes over time |
| Hub Site Relationship Map | Quarterly | Document hub associations for governance |
| Content Type Analysis | Annually | Verify content type consistency across the tenant |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate architecture
- See [Troubleshooting](troubleshooting.md) for architecture-related issues
- Back to [Control 1.8: Information Architecture Review](../../../controls/pillar-1-readiness/1.8-information-architecture-review.md)
