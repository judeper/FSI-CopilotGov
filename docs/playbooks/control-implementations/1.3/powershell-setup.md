# Control 1.3: Restricted SharePoint Search Configuration — PowerShell Setup

Automation scripts for managing Restricted SharePoint Search (RSS) allowed site lists at scale.

## Prerequisites

- SharePoint Online Management Shell (`Microsoft.Online.SharePoint.PowerShell`)
- SharePoint Administrator role
- SharePoint Advanced Management license active in tenant
- Approved sites list in CSV format

## Scripts

### Script 1: Enable Restricted SharePoint Search

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

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Allowed List Audit Export | Monthly | Generate audit trail of allowed sites |
| Governance Review Report | Quarterly | Support governance committee review of allowed list |
| RSS Mode Verification | Weekly | Confirm RSS remains enabled and has not been toggled off |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate search restrictions
- See [Troubleshooting](troubleshooting.md) for common RSS configuration issues
