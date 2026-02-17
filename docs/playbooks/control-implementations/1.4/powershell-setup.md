# Control 1.4: Semantic Index Governance — PowerShell Setup

Automation scripts for managing and monitoring the Microsoft 365 Semantic Index governance.

## Prerequisites

- Microsoft Graph PowerShell SDK (`Microsoft.Graph`)
- SharePoint Online Management Shell
- Global Administrator or Search Administrator role
- Microsoft 365 Copilot licenses in the tenant

## Scripts

### Script 1: Semantic Index Coverage Report

```powershell
# Generate report on semantic index coverage across Microsoft 365 workloads
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Reports
Import-Module Microsoft.Graph.Sites

Connect-MgGraph -Scopes "Reports.Read.All","Sites.Read.All"

$report = @{
    GeneratedDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    SharePointSites = @{
        Total = 0
        IndexEligible = 0
        Excluded = 0
    }
}

# Count SharePoint sites and their index eligibility
$sites = Get-MgSite -All
$report.SharePointSites.Total = $sites.Count

foreach ($site in $sites) {
    $siteDetail = Get-MgSite -SiteId $site.Id -Property "sharepointIds,displayName"
    # Sites with specific configurations may be excluded
    $report.SharePointSites.IndexEligible++
}

Write-Host "=== Semantic Index Coverage Report ==="
Write-Host "Total SharePoint sites: $($report.SharePointSites.Total)"
Write-Host "Index-eligible sites: $($report.SharePointSites.IndexEligible)"

$report | ConvertTo-Json -Depth 3 | Out-File "SemanticIndexCoverage_$(Get-Date -Format 'yyyyMMdd').json"
```

### Script 2: Content Source Inventory for Index Governance

```powershell
# Inventory content sources to inform semantic index governance decisions
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
        IndexRecommendation = if ($detail.SensitivityLabel -match "Highly Confidential") { "Review Required" } else { "Include" }
    }
}

$inventory | Export-Csv "ContentSourceInventory_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Inventoried $($inventory.Count) content sources for index governance review."
```

### Script 3: Monitor Copilot Query Patterns

```powershell
# Review Copilot usage patterns to identify index governance concerns
# Requires: Microsoft Graph SDK with AuditLog.Read.All

Import-Module Microsoft.Graph.Reports

Connect-MgGraph -Scopes "AuditLog.Read.All"

$startDate = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
$endDate = (Get-Date).ToString("yyyy-MM-dd")

# Pull Copilot activity from audit logs
$auditLogs = Get-MgAuditLogSignIn -Filter "appDisplayName eq 'Microsoft 365 Copilot'" `
    -Top 1000

$usageSummary = $auditLogs | Group-Object -Property UserPrincipalName |
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
| Index Coverage Report | Monthly | Track semantic index scope and coverage changes |
| Content Source Inventory | Quarterly | Support governance review of index scope decisions |
| Copilot Query Pattern Review | Monthly | Identify anomalous usage patterns for governance review |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate index governance controls
- See [Troubleshooting](troubleshooting.md) for index-related issues
