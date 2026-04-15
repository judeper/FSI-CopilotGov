# Control 3.7: Regulatory Reporting — PowerShell Setup

Automation scripts for generating regulatory reports that incorporate Copilot governance data and compliance metrics.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`, `ImportExcel`
- **Permissions:** Purview Compliance Admin, Reports.Read.All, Directory.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "Reports.Read.All", "Directory.Read.All"
```

## Scripts

### Script 1: Copilot Usage Summary via Graph API

```powershell
# Export Copilot usage summary and per-user detail from Graph reporting endpoints
# Supports D7, D30, D90, D180 reporting periods
# NOTE: Graph reporting URLs below require an authenticated session (Connect-MgGraph).
# They return HTTP 405 if accessed directly in a browser without authentication.
$period = "D30"

# Org-level usage summary
$summary = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/microsoft365CopilotUsageSummary(period='$period')"
$summary | ConvertTo-Json -Depth 5 | Out-File "CopilotUsageSummary_$period.json"

# Per-user detail report (returns CSV download)
Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/getMicrosoft365CopilotUserDetailReport(period='$period')" `
    -OutputFilePath "CopilotUserDetail_$period.csv"

Write-Host "Copilot usage reports exported for period $period" -ForegroundColor Green
Write-Host "  Summary: CopilotUsageSummary_$period.json"
Write-Host "  User detail: CopilotUserDetail_$period.csv"
```

### Script 2: Copilot Audit Log Export for Compliance Review

```powershell
# Export Copilot interactions from Unified Audit Log with parsed metadata
# RecordType CopilotInteraction covers all M365 Copilot surfaces
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$results = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

# Parse AuditData JSON for structured compliance export
$parsed = $results | ForEach-Object {
    $audit = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Timestamp         = $_.CreationDate
        User              = $_.UserIds
        Operation         = $_.Operations
        AppHost           = $audit.AppHost
        AccessedResources = ($audit.AccessedResources.Name -join "; ")
        SensitivityLabels = ($audit.AccessedResources.SensitivityLabelId -join "; ")
    }
}

$parsed | Export-Csv "CopilotAudit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Exported $($results.Count) Copilot audit records" -ForegroundColor Green
```

### Script 3: Copilot License Compliance by Department

```powershell
# Report Copilot license assignments by department using real SKU lookup
# Resolves MICROSOFT_365_COPILOT SKU ID from tenant subscriptions
$sku = (Get-MgSubscribedSku |
    Where-Object SkuPartNumber -eq "MICROSOFT_365_COPILOT").SkuId

if (-not $sku) {
    Write-Warning "MICROSOFT_365_COPILOT SKU not found in tenant subscriptions"
    return
}

$copilotUsers = Get-MgUser -All `
    -Property "DisplayName,Department,UserPrincipalName,AssignedLicenses" |
    Where-Object { $_.AssignedLicenses.SkuId -contains $sku }

# Per-user export
$copilotUsers |
    Select-Object DisplayName, Department, UserPrincipalName |
    Export-Csv "CopilotLicensees_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

# Department summary
$copilotUsers | Group-Object Department |
    Select-Object @{N="Department";E={if ($_.Name) {$_.Name} else {"(Unassigned)"}}}, Count |
    Sort-Object Count -Descending |
    Format-Table -AutoSize

Write-Host "Total Copilot-licensed users: $($copilotUsers.Count)" -ForegroundColor Green
```

### Script 4: Compliance Posture Validation

```powershell
# Validate that Copilot governance policies are deployed and active
# Queries live policy configuration instead of using static status values

# DLP policies targeting Copilot or FSI workloads
$dlpPolicies = Get-DlpCompliancePolicy |
    Where-Object { $_.Name -match "Copilot|FSI" -and $_.Enabled -eq $true }

# Retention policies
$retentionPolicies = Get-RetentionCompliancePolicy |
    Where-Object { $_.Enabled -eq $true }

# Communication compliance (supervision) policies
$commPolicies = Get-SupervisoryReviewPolicyV2

$scorecard = @()
$scorecard += [PSCustomObject]@{
    Control  = "DLP Policies"
    Count    = $dlpPolicies.Count
    Status   = if ($dlpPolicies.Count -gt 0) { "Active" } else { "Missing" }
    Policies = ($dlpPolicies.Name -join "; ")
}
$scorecard += [PSCustomObject]@{
    Control  = "Retention Policies"
    Count    = $retentionPolicies.Count
    Status   = if ($retentionPolicies.Count -gt 0) { "Active" } else { "Missing" }
    Policies = ($retentionPolicies.Name -join "; ")
}
$scorecard += [PSCustomObject]@{
    Control  = "Communication Compliance"
    Count    = $commPolicies.Count
    Status   = if ($commPolicies.Count -gt 0) { "Active" } else { "Missing" }
    Policies = ($commPolicies.Name -join "; ")
}

$scorecard | Format-Table Control, Count, Status -AutoSize
$scorecard | Export-Csv "ComplianceScorecard_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Scorecard reflects live policy configuration" -ForegroundColor Green
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Copilot usage summary export | Quarterly | Script 1 |
| Copilot audit log export | Monthly | Script 2 |
| License compliance by department | Quarterly | Script 3 |
| Compliance posture validation | Monthly | Script 4 |

## Limitations

- Graph usage reports (`microsoft365CopilotUsageSummary`) require `Reports.Read.All` and may take up to 48 hours to reflect recent activity
- `getMicrosoft365CopilotUserDetailReport` returns a CSV file download, not a JSON object — use `-OutputFilePath` to save
- UAL search results are capped at 5,000 records per query; use date-range batching or the Graph API audit query endpoint for larger environments
- DSPM for AI provides prompt/response content detail beyond UAL metadata, but has no PowerShell API — portal-only configuration
- `Get-SupervisoryReviewPolicyV2` requires E5 Compliance or Communication Compliance add-on license

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate reporting accuracy
- See [Troubleshooting](troubleshooting.md) for reporting issues
- Back to [Control 3.7](../../../controls/pillar-3-compliance/3.7-regulatory-reporting.md)
