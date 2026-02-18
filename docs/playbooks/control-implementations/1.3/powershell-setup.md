# Control 1.3: Restricted SharePoint Search and Restricted Content Discovery — PowerShell Setup

Automation scripts for managing Restricted SharePoint Search (RSS) and Restricted Content Discovery (RCD) at scale.

## Prerequisites

- SharePoint Online Management Shell (`Microsoft.Online.SharePoint.PowerShell`)
- SharePoint Administrator role
- SharePoint Advanced Management (SAM) license active in tenant — included with Microsoft 365 Copilot licenses at no additional cost
- Approved sites list in CSV format (for RSS)
- List of sites to exclude from Copilot discovery (for RCD)

## Scripts

### Script 1: Enable Restricted SharePoint Search (RSS)

```powershell
# Enable RSS and verify the setting
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell

Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

# Enable Restricted SharePoint Search
Set-SPOTenantRestrictedSearchMode -Mode Restricted

# Verify the setting
$mode = Get-SPOTenantRestrictedSearchMode
Write-Host "Restricted SharePoint Search mode: $($mode.Mode)"
```

### Script 2: Bulk Add Sites to Allowed List

```powershell
# Add approved sites to the RSS allowed list from CSV
# CSV format: Url (one column with site URLs)
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$approvedSites = Import-Csv "ApprovedSites.csv"
$results = @()

foreach ($site in $approvedSites) {
    try {
        Add-SPOTenantRestrictedSearchAllowedList -SiteUrl $site.Url
        $results += [PSCustomObject]@{
            Url    = $site.Url
            Status = "Added"
            Date   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
        Write-Host "Added: $($site.Url)" -ForegroundColor Green
    } catch {
        $results += [PSCustomObject]@{
            Url    = $site.Url
            Status = "Failed: $($_.Exception.Message)"
            Date   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
        Write-Host "Failed: $($site.Url) - $($_.Exception.Message)" -ForegroundColor Red
    }
}

$results | Export-Csv "RSSAllowedList_Changes_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "`nTotal: $($results.Count) | Added: $(($results | Where-Object Status -eq 'Added').Count)"
```

### Script 3: Audit and Export Current Allowed List

```powershell
# Export the current RSS allowed sites list for audit and review
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$allowedSites = Get-SPOTenantRestrictedSearchAllowedList

$auditReport = @()
foreach ($siteUrl in $allowedSites) {
    $siteDetail = Get-SPOSite -Identity $siteUrl -Detailed -ErrorAction SilentlyContinue
    $auditReport += [PSCustomObject]@{
        Url               = $siteUrl
        Title             = $siteDetail.Title
        SharingCapability = $siteDetail.SharingCapability
        SensitivityLabel  = $siteDetail.SensitivityLabel
        Owner             = $siteDetail.Owner
        LastModified      = $siteDetail.LastContentModifiedDate
    }
}

$auditReport | Export-Csv "RSSAllowedList_Audit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Exported $($auditReport.Count) allowed sites to audit report."
```

### Script 4: Remove Sites from Allowed List

```powershell
# Remove sites from the RSS allowed list (e.g., during quarterly review)
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sitesToRemove = Import-Csv "SitesToRemove.csv"

foreach ($site in $sitesToRemove) {
    try {
        Remove-SPOTenantRestrictedSearchAllowedList -SiteUrl $site.Url
        Write-Host "Removed: $($site.Url)" -ForegroundColor Yellow
    } catch {
        Write-Host "Failed to remove: $($site.Url) - $($_.Exception.Message)" -ForegroundColor Red
    }
}
```

### Script 5: Enable Restricted Content Discovery (RCD) on Specific Sites

```powershell
# Enable RCD on specific sites to exclude them from Copilot discovery
# RCD excludes sites from Copilot grounding while leaving direct user access unchanged
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

# Enable RCD on a single site
$siteUrl = "https://<tenant>.sharepoint.com/sites/<sensitive-site>"
Set-SPOSite -Identity $siteUrl -RestrictContentOrgWideSearch $true
Write-Host "RCD enabled for: $siteUrl" -ForegroundColor Green

# Verify the setting
$site = Get-SPOSite -Identity $siteUrl
Write-Host "RestrictContentOrgWideSearch: $($site.RestrictContentOrgWideSearch)"
```

### Script 6: Bulk Enable RCD from CSV

```powershell
# Bulk enable RCD on multiple sites from a CSV list
# CSV format: Url,Reason (two columns)
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$sitesToRestrict = Import-Csv "RCDSites.csv"
$rcdLog = @()

foreach ($site in $sitesToRestrict) {
    try {
        Set-SPOSite -Identity $site.Url -RestrictContentOrgWideSearch $true
        $rcdLog += [PSCustomObject]@{
            Url     = $site.Url
            Reason  = $site.Reason
            Status  = "RCD Enabled"
            Date    = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
        Write-Host "RCD enabled: $($site.Url)" -ForegroundColor Green
    } catch {
        $rcdLog += [PSCustomObject]@{
            Url     = $site.Url
            Reason  = $site.Reason
            Status  = "Failed: $($_.Exception.Message)"
            Date    = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        }
        Write-Host "Failed: $($site.Url)" -ForegroundColor Red
    }
}

$rcdLog | Export-Csv "RCDConfiguration_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "RCD configured on $($rcdLog.Where({$_.Status -eq 'RCD Enabled'}).Count) sites."
```

### Script 7: Audit RCD Configuration Across All Sites

```powershell
# Audit which sites have RCD enabled for governance review
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell
Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$allSites = Get-SPOSite -Limit All -IncludePersonalSite $false
$rcdEnabledSites = @()

foreach ($site in $allSites) {
    $detail = Get-SPOSite -Identity $site.Url -ErrorAction SilentlyContinue
    if ($detail.RestrictContentOrgWideSearch -eq $true) {
        $rcdEnabledSites += [PSCustomObject]@{
            Url   = $site.Url
            Title = $site.Title
            Owner = $detail.Owner
        }
    }
}

Write-Host "Sites with RCD enabled: $($rcdEnabledSites.Count)"
$rcdEnabledSites | Export-Csv "RCDAudit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| RSS Allowed List Audit Export | Monthly | Generate audit trail of allowed sites |
| RCD Configuration Audit | Monthly | Confirm which sites have RCD enabled and review for accuracy |
| Governance Review Report | Quarterly | Support governance committee review of RSS allowed list and RCD exclusion list |
| RSS Mode Verification | Weekly | Confirm RSS remains enabled and has not been toggled off |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate search restrictions
- See [Troubleshooting](troubleshooting.md) for common RSS configuration issues
