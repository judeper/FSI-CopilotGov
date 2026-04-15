# Control 1.7: SharePoint Advanced Management Readiness — PowerShell Setup

Automation scripts for configuring and monitoring SharePoint Advanced Management features.

## Prerequisites

- SharePoint Online Management Shell (latest version)
- SharePoint Admin role
- Microsoft 365 Copilot license (includes SAM) or SharePoint Advanced Management add-on license active

## Scripts

### Script 1: Verify SAM Feature Availability

```powershell
# Check which SAM features are available and enabled
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$tenantSettings = Get-SPOTenant

Write-Host "=== SharePoint Advanced Management Status ==="
Write-Host "Restricted Search Mode: $(Get-SPOTenantRestrictedSearchMode -ErrorAction SilentlyContinue)"
Write-Host "Conditional Access Policy: $($tenantSettings.ConditionalAccessPolicy)"
Write-Host "Allow Downloading NonWeb Viewable: $($tenantSettings.AllowDownloadingNonWebViewableFiles)"
Write-Host "External Sharing: $($tenantSettings.SharingCapability)"
Write-Host "Default Sharing Link Type: $($tenantSettings.DefaultSharingLinkType)"
Write-Host "Site Creation Default: $($tenantSettings.SelfSiteCreationDisabled)"
```

### Script 2: Configure Site Lifecycle Policy

```powershell
# Set up site lifecycle management for inactive sites
# Requires: SharePoint Online Management Shell
# NOTE: Site lifecycle management is configured via SharePoint admin center >
# Policies > Site lifecycle management. No PowerShell cmdlet exists for
# inactivity threshold or notification settings.

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

# Site lifecycle policy must be configured in the admin portal:
#   SharePoint admin center > Policies > Site lifecycle management
#   - Set inactivity threshold (e.g., 180 days for FSI)
#   - Enable owner notifications
#   - Configure archival rules

Write-Host "Site lifecycle policy configuration:"
Write-Host "  Configure via: SharePoint admin center > Policies > Site lifecycle management"
Write-Host "  Recommended inactivity threshold: 180 days"
Write-Host "  Enable notifications: Yes"
Write-Host ""
Write-Host "Review inactive sites in SharePoint admin center > Sites > Active sites > Inactive filter"
```

### Script 3: Data Access Governance Report Export

```powershell
# Export data access governance report data for compliance documentation
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sites = Get-SPOSite -Limit All -IncludePersonalSite $false
$governanceReport = @()

foreach ($site in $sites) {
    $detail = Get-SPOSite -Identity $site.Url -Detailed
    $governanceReport += [PSCustomObject]@{
        Url                    = $site.Url
        Title                  = $site.Title
        Template               = $site.Template
        SharingCapability      = $detail.SharingCapability
        SensitivityLabel       = $detail.SensitivityLabel
        ConditionalAccessPolicy = $detail.ConditionalAccessPolicy
        RestrictContentOrg     = $detail.RestrictContentOrgWideSearch
        LastContentModified    = $detail.LastContentModifiedDate
        StorageMB              = [math]::Round($detail.StorageUsageCurrent, 2)
        IsInactive             = ($detail.LastContentModifiedDate -lt (Get-Date).AddDays(-180))
        LockState              = $detail.LockState
    }
}

$inactive = ($governanceReport | Where-Object IsInactive).Count
$sensitive = ($governanceReport | Where-Object { $_.SensitivityLabel -ne "" }).Count
$rcdEnabled = ($governanceReport | Where-Object { $_.RestrictContentOrg -eq $true }).Count

Write-Host "=== Data Access Governance Summary ==="
Write-Host "Total sites: $($governanceReport.Count)"
Write-Host "Inactive sites (>180 days): $inactive"
Write-Host "Labeled sites: $sensitive"
Write-Host "Sites with RCD enabled: $rcdEnabled"

$governanceReport | Export-Csv "DataAccessGovernance_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Configure Restricted Access Control on Sensitive Sites

```powershell
# Apply Restricted Access Control (RAC) to sites containing NPI or MNPI
# RAC enforces a maximum access boundary -- only security group members can access the site
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sensitiveSites = Import-Csv "SensitiveSites.csv"
# CSV must include columns: Url, RestrictedGroupId (the security group ID to enforce as the access boundary)

# Enable RAC at the tenant level (required before per-site RAC can be configured)
Set-SPOTenant -EnableRestrictedAccessControl $true

$configLog = @()

foreach ($site in $sensitiveSites) {
    try {
        # Enable Restricted Access Control with designated security group
        Set-SPOSite -Identity $site.Url `
            -RestrictedAccessControl $true `
            -RestrictedAccessControlGroups $site.RestrictedGroupId

        $configLog += [PSCustomObject]@{
            Url    = $site.Url
            Status = "RAC Configured"
            Group  = $site.RestrictedGroupId
            Date   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
        Write-Host "RAC enabled on $($site.Url)"
    } catch {
        $configLog += [PSCustomObject]@{
            Url    = $site.Url
            Status = "Failed: $($_.Exception.Message)"
            Group  = $site.RestrictedGroupId
            Date   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
        Write-Warning "Failed to configure RAC on $($site.Url): $($_.Exception.Message)"
    }
}

$configLog | Export-Csv "RACConfiguration_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "RAC configuration complete. $($configLog | Where-Object Status -eq 'RAC Configured' | Measure-Object | Select-Object -ExpandProperty Count) sites configured."
```

### Script 5: Bulk Configure Site-Level Access Policies

```powershell
# Apply conditional access and sharing restrictions to sensitive sites
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sensitiveSites = Import-Csv "SensitiveSites.csv"
$configLog = @()

foreach ($site in $sensitiveSites) {
    try {
        Set-SPOSite -Identity $site.Url `
            -SharingCapability "ExistingExternalUserSharingOnly" `
            -ConditionalAccessPolicy "AllowLimitedAccess" `
            -LimitedAccessFileType "WebPreviewableFiles"

        $configLog += [PSCustomObject]@{
            Url    = $site.Url
            Status = "Configured"
            Date   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
    } catch {
        $configLog += [PSCustomObject]@{
            Url    = $site.Url
            Status = "Failed: $($_.Exception.Message)"
            Date   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
    }
}

$configLog | Export-Csv "SAMSiteConfig_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| SAM Feature Verification | Monthly | Confirm all SAM features remain enabled |
| Inactive Site Review | Monthly | Identify and act on inactive sites |
| Data Access Governance Export | Quarterly | Generate compliance evidence reports including RCD status |
| RAC Group Membership Review | Quarterly (Regulated) | Verify security group membership for all RAC-enabled sites |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate SAM configuration
- See [Troubleshooting](troubleshooting.md) for SAM-related issues
- Back to [Control 1.7: SharePoint Advanced Management](../../../controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md)
