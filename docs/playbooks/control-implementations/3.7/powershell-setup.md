# Control 3.7: Regulatory Reporting — PowerShell Setup

Automation scripts for generating regulatory reports that incorporate Copilot governance data and compliance metrics.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`, `ImportExcel`
- **Permissions:** Compliance Administrator, AuditLog.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "AuditLog.Read.All", "Reports.Read.All"
```

## Scripts

### Script 1: Generate Copilot Governance Summary Report

```powershell
# Consolidated report of Copilot governance metrics for regulatory submissions
$reportDate = Get-Date -Format "yyyy-MM-dd"
$startDate = (Get-Date).AddDays(-90)
$endDate = Get-Date

# Gather Copilot interaction counts
$copilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction -ResultSize 5000

# Gather compliance policy matches
$policyMatches = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionPolicyMatch" -ResultSize 5000

# Gather DLP events related to Copilot
$dlpEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType DLP -ResultSize 5000

$report = [PSCustomObject]@{
    ReportDate             = $reportDate
    ReportingPeriod        = "Last 90 Days"
    TotalCopilotInteractions = $copilotEvents.Count
    UniqueUsers            = ($copilotEvents | Select-Object -Unique UserIds).Count
    PolicyMatches          = $policyMatches.Count
    DLPIncidents           = $dlpEvents.Count
}

$report | Export-Csv "RegulatoryReport_$reportDate.csv" -NoTypeInformation
Write-Host "Regulatory report generated: RegulatoryReport_$reportDate.csv" -ForegroundColor Green
```

### Script 2: FINRA 3120 Supervisory Control Report Data

```powershell
# Extract data for FINRA Rule 3120 annual supervisory control report
$startDate = (Get-Date).AddYears(-1)
$endDate = Get-Date

$reviewActions = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionReviewAction" -ResultSize 5000

$controlReport = [PSCustomObject]@{
    ReportingPeriod        = "$($startDate.ToString('yyyy-MM-dd')) to $($endDate.ToString('yyyy-MM-dd'))"
    TotalReviews           = $reviewActions.Count
    ApprovedItems          = ($reviewActions | Where-Object { $_.AuditData -like "*Approve*" }).Count
    EscalatedItems         = ($reviewActions | Where-Object { $_.AuditData -like "*Escalate*" }).Count
    ResolvedViolations     = ($reviewActions | Where-Object { $_.AuditData -like "*Violation*" }).Count
}

$controlReport | Format-List
$controlReport | Export-Csv "FINRA3120_Report_$(Get-Date -Format 'yyyy').csv" -NoTypeInformation
```

### Script 3: AI Tool Inventory Report

```powershell
# Generate an inventory of Copilot features in use across the organization
$copilotLicenses = Get-MgUser -Filter "assignedLicenses/any()" -All |
    Where-Object { $_.AssignedLicenses.SkuId -contains "copilot-sku-id" }

$inventory = [PSCustomObject]@{
    AIToolName       = "Microsoft 365 Copilot"
    Vendor           = "Microsoft Corporation"
    LicensedUsers    = $copilotLicenses.Count
    DeploymentDate   = "2025-01-15"
    GovernanceStatus = "Active — Controls 3.1-3.13 implemented"
    RiskRating       = "Medium — supervised usage with controls"
    LastAssessment   = (Get-Date -Format "yyyy-MM-dd")
}

$inventory | Format-List
$inventory | Export-Csv "AIToolInventory_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "AI tool inventory exported" -ForegroundColor Green
```

### Script 4: Compliance Scorecard Generator

```powershell
# Generate a compliance scorecard for executive and regulatory reporting
$controls = @(
    @{Control="3.1"; Name="Audit Logging"; Status="Implemented"},
    @{Control="3.2"; Name="Data Retention"; Status="Implemented"},
    @{Control="3.3"; Name="eDiscovery"; Status="Implemented"},
    @{Control="3.4"; Name="Comm Compliance"; Status="Implemented"},
    @{Control="3.5"; Name="FINRA 2210"; Status="Implemented"},
    @{Control="3.6"; Name="Supervision"; Status="Implemented"},
    @{Control="3.7"; Name="Reg Reporting"; Status="In Progress"}
)

$scorecard = $controls | ForEach-Object {
    [PSCustomObject]@{
        Control = $_.Control
        Name    = $_.Name
        Status  = $_.Status
        LastVerified = (Get-Date -Format "yyyy-MM-dd")
    }
}

$scorecard | Format-Table -AutoSize
$scorecard | Export-Csv "ComplianceScorecard_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Governance summary report | Quarterly | Script 1 |
| FINRA 3120 data extract | Annually | Script 2 |
| AI tool inventory update | Quarterly | Script 3 |
| Compliance scorecard | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate reporting accuracy
- See [Troubleshooting](troubleshooting.md) for reporting issues
