# Control 1.4: Semantic Index Governance — PowerShell Setup

Automation scripts for managing and monitoring the Microsoft 365 Semantic Index governance.

## Prerequisites

- Microsoft Graph PowerShell SDK (`Microsoft.Graph`)
- SharePoint Online Management Shell
- Entra Global Admin or Search Administrator role
- Microsoft 365 Copilot licenses in the tenant

## Scripts

### Script 1: SharePoint Scope Review Report

```powershell
# Generate a SharePoint inventory for semantic-index governance review.
# Note: Get-MgSite alone doesn't tell you whether a site is excluded from
# Microsoft Search or whether RCD is enabled. Searchability and RCD must be
# validated through SharePoint settings or SPO admin cmdlets separately.
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Reports
Import-Module Microsoft.Graph.Sites

Connect-MgGraph -Scopes "Reports.Read.All","Sites.Read.All"

$report = @{
    GeneratedDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    SharePointSites = @{
        Total = 0
        InventoriedForReview = 0
    }
}

# Count SharePoint sites for governance review
$sites = Get-MgSite -All
$report.SharePointSites.Total = $sites.Count

foreach ($site in $sites) {
    $siteDetail = Get-MgSite -SiteId $site.Id -Property "sharepointIds,displayName"
    # TODO: Add org-specific enrichment for site searchability and RCD state
    # from SharePoint administration sources. Those controls are separate from
    # the Microsoft Graph site inventory and can't be inferred here.
    $report.SharePointSites.InventoriedForReview++
}

Write-Host "=== SharePoint Scope Review Report ==="
Write-Host "Total SharePoint sites: $($report.SharePointSites.Total)"
Write-Host "Sites inventoried for review: $($report.SharePointSites.InventoriedForReview)"

$report | ConvertTo-Json -Depth 3 | Out-File "SharePointScopeReview_$(Get-Date -Format 'yyyyMMdd').json"
```

### Script 2: SharePoint Governance Review Inventory

```powershell
# Inventory SharePoint sites to inform searchability and discoverability
# governance decisions. Sensitivity labels can prioritize review, but they do
# not by themselves determine whether a site is in the Microsoft Search index.
# Requires: SharePoint Online Management Shell, Exchange Online Management

Import-Module Microsoft.Online.SharePoint.PowerShell
Import-Module ExchangeOnlineManagement

Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"
Connect-ExchangeOnline

# SharePoint site inventory with sensitivity context
$spoSites = Get-SPOSite -Limit All -IncludePersonalSite $false
$inventory = @()

foreach ($site in $spoSites) {
    $detail = Get-SPOSite -Identity $site.Url -Detailed
    $inventory += [PSCustomObject]@{
        Source            = "SharePoint"
        Url               = $site.Url
        Title             = $site.Title
        Template          = $site.Template
        SensitivityLabel  = $detail.SensitivityLabel
        StorageMB         = [math]::Round($detail.StorageUsageCurrent, 2)
        LastModified      = $detail.LastContentModifiedDate
        # NOTE: SensitivityLabel returns a GUID, not a display name.
        # Resolve GUID to name via: Get-Label | Select DisplayName, Guid
        # Replace the GUID below with your "Highly Confidential" label GUID.
        GovernanceReviewRecommendation = $(if ($detail.SensitivityLabel -match "<your-highly-confidential-label-guid>") { "Review site searchability and discoverability controls" } else { "Review with business owner" })
    }
}

$inventory | Export-Csv "SharePointGovernanceReview_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Inventoried $($inventory.Count) SharePoint sites for governance review."
```

### Script 3: Monitor Copilot Query Patterns

```powershell
# Review Copilot usage patterns to identify index governance concerns
# Requires: ExchangeOnlineManagement module with Compliance Search role

Import-Module ExchangeOnlineManagement

Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("yyyy-MM-ddTHH:mm:ss")
$endDate = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ss")

# Pull Copilot activity from unified audit log
$auditLogs = Search-UnifiedAuditLog -RecordType CopilotInteraction `
    -StartDate $startDate -EndDate $endDate `
    -ResultSize 1000

$usageSummary = $auditLogs | Group-Object -Property UserIds |
    Select-Object @{N='User';E={$_.Name}}, @{N='QueryCount';E={$_.Count}} |
    Sort-Object QueryCount -Descending

Write-Host "=== Copilot Usage Summary (Last 30 Days) ==="
Write-Host "Unique users: $($usageSummary.Count)"
Write-Host "Total queries: $(($usageSummary | Measure-Object -Property QueryCount -Sum).Sum)"

$usageSummary | Export-Csv "CopilotUsageSummary_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| SharePoint Scope Review Report | Monthly | Track SharePoint sites that need searchability and discoverability review |
| SharePoint Governance Review Inventory | Quarterly | Support governance review of searchability, RCD, and related scope decisions |
| Copilot Query Pattern Review | Monthly | Identify anomalous usage patterns for governance review |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate index governance controls
- See [Troubleshooting](troubleshooting.md) for index-related issues
