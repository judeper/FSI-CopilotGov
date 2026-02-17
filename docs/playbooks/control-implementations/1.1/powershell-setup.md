# Control 1.1: Copilot Readiness Assessment and Data Hygiene — PowerShell Setup

Automation scripts for conducting Copilot readiness assessments and data hygiene evaluations at scale.

## Prerequisites

- PowerShell 7.x or later
- Microsoft Graph PowerShell SDK (`Microsoft.Graph`)
- SharePoint Online Management Shell (`Microsoft.Online.SharePoint.PowerShell`)
- Exchange Online Management module (`ExchangeOnlineManagement`)
- Global Reader or Security Reader role (minimum for assessment)

## Scripts

### Script 1: Tenant Readiness Assessment Report

```powershell
# Generate comprehensive Copilot readiness assessment
# Requires: Microsoft.Graph module with Sites.Read.All, Reports.Read.All

Import-Module Microsoft.Graph.Sites
Import-Module Microsoft.Graph.Reports

Connect-MgGraph -Scopes "Sites.Read.All","Reports.Read.All","User.Read.All"

$report = @{
    AssessmentDate = Get-Date -Format "yyyy-MM-dd"
    TotalSites = 0
    SitesWithOversharing = 0
    UnlabeledDocuments = 0
    PermissionAnomalies = 0
}

# Enumerate SharePoint sites and check sharing settings
$sites = Get-MgSite -All
$report.TotalSites = $sites.Count

foreach ($site in $sites) {
    $permissions = Get-MgSitePermission -SiteId $site.Id -ErrorAction SilentlyContinue
    $externalShares = $permissions | Where-Object {
        $_.GrantedToIdentities.Application -or $_.GrantedToIdentitiesV2.SiteUser.LoginName -like "*#ext#*"
    }
    if ($externalShares.Count -gt 0) {
        $report.SitesWithOversharing++
    }
}

$report | ConvertTo-Json | Out-File "CopilotReadinessReport_$(Get-Date -Format 'yyyyMMdd').json"
Write-Host "Readiness assessment complete. Results saved to JSON report."
```

### Script 2: Data Hygiene Scan — Stale and Overshared Content

```powershell
# Identify stale content and overshared sites for hygiene remediation
# Requires: SharePoint Online Management Shell

Import-Module Microsoft.Online.SharePoint.PowerShell

Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"

$results = @()
$sites = Get-SPOSite -Limit All -IncludePersonalSite $false

foreach ($site in $sites) {
    $siteDetail = Get-SPOSite -Identity $site.Url -Detailed
    $row = [PSCustomObject]@{
        Url                = $site.Url
        Title              = $site.Title
        SharingCapability  = $siteDetail.SharingCapability
        LastContentModified = $siteDetail.LastContentModifiedDate
        StorageUsageMB     = [math]::Round($siteDetail.StorageUsageCurrent, 2)
        IsStale            = ($siteDetail.LastContentModifiedDate -lt (Get-Date).AddDays(-180))
        IsOvershared       = ($siteDetail.SharingCapability -eq "ExternalUserAndGuestSharing")
    }
    $results += $row
}

$staleCount = ($results | Where-Object { $_.IsStale }).Count
$oversharedCount = ($results | Where-Object { $_.IsOvershared }).Count

Write-Host "Total sites: $($results.Count)"
Write-Host "Stale sites (>180 days): $staleCount"
Write-Host "Overshared sites: $oversharedCount"

$results | Export-Csv "DataHygieneScan_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Sensitivity Label Coverage Report

```powershell
# Report on sensitivity label adoption across the tenant
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$labelPolicies = Get-LabelPolicy
$labels = Get-Label

Write-Host "=== Sensitivity Label Coverage ==="
Write-Host "Active label policies: $($labelPolicies.Count)"
Write-Host "Published labels: $($labels.Count)"

foreach ($label in $labels) {
    Write-Host "  - $($label.DisplayName) | Priority: $($label.Priority) | Enabled: $($label.Enabled)"
}

# Export label configuration for documentation
$labels | Select-Object DisplayName, Priority, Enabled, ParentId, ContentType |
    Export-Csv "SensitivityLabelConfig_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Readiness Assessment | Weekly during pre-deployment | Track remediation progress |
| Data Hygiene Scan | Monthly | Identify new stale or overshared content |
| Label Coverage Report | Weekly | Monitor label adoption toward 85% target |

Configure scheduled tasks using Azure Automation or Windows Task Scheduler to run these scripts on the recommended cadence.

## Next Steps

- See [Verification & Testing](verification-testing.md) for validation procedures
- See [Troubleshooting](troubleshooting.md) for common script issues
