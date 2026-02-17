# Control 4.7: Copilot Feedback and Telemetry Data Governance — PowerShell Setup

Automation scripts for configuring and auditing Copilot feedback and telemetry data governance.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** Global Administrator, Privacy Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Organization.ReadWrite.All", "Policy.ReadWrite.All"
```

## Scripts

### Script 1: Audit Current Diagnostic Data Settings

```powershell
# Report on current diagnostic data and telemetry configuration
$orgSettings = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/organization" `
    -OutputType PSObject

Write-Host "Organization Telemetry Configuration:" -ForegroundColor Cyan
Write-Host "Organization: $($orgSettings.value[0].displayName)"
Write-Host "Tenant ID: $($orgSettings.value[0].id)"
Write-Host ""
Write-Host "Diagnostic Data and Feedback Settings:"
Write-Host "Review the following in M365 Admin Center > Settings > Org settings:"
Write-Host "  - Microsoft 365 Apps diagnostic data level"
Write-Host "  - Copilot feedback collection"
Write-Host "  - Connected experiences settings"
Write-Host ""
Write-Host "Note: Many telemetry settings are managed via M365 Admin Center or Group Policy."
```

### Script 2: Monitor Copilot Feedback Events

```powershell
# Search for Copilot feedback events in the audit log
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$feedbackEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "CopilotFeedback" `
    -ResultSize 5000

Write-Host "Copilot Feedback Events (Last 30 Days):" -ForegroundColor Cyan
Write-Host "Total feedback events: $($feedbackEvents.Count)"

if ($feedbackEvents.Count -gt 0) {
    $feedbackSummary = $feedbackEvents | Group-Object {
        ($_.AuditData | ConvertFrom-Json).FeedbackType
    } | Select-Object @{N='FeedbackType'; E={$_.Name}}, @{N='Count'; E={$_.Count}}

    $feedbackSummary | Format-Table -AutoSize
}

$feedbackEvents | Export-Csv "CopilotFeedback_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Configure Cloud Policy for Diagnostic Data Level

```powershell
# Use Microsoft 365 Cloud Policy to set diagnostic data levels
# Note: Cloud Policy configuration is primarily done via the M365 Apps Admin Center
# This script documents the policy settings for audit purposes

$policySettings = @"
# Microsoft 365 Apps Diagnostic Data Policy Configuration
## Date: $(Get-Date -Format "yyyy-MM-dd")

### Recommended Settings for FSI Environments

| Policy Setting | Value | Rationale |
|---------------|-------|-----------|
| Configure diagnostic data level | Required | Minimum data collection for regulated environment |
| Allow optional connected experiences | Disabled | Prevents unnecessary data sharing |
| Allow connected experiences (all) | Enabled (required only) | Essential service functionality |
| Copilot feedback | Enabled (internal) | Supports model quality monitoring |

### Group Policy Paths
- Computer Configuration > Admin Templates > Microsoft Office 2016 > Privacy > Trust Center
  - Configure the level of client software diagnostic data: Required
  - Allow the use of additional optional connected experiences: Disabled
"@

$policySettings | Out-File "DiagnosticDataPolicy_$(Get-Date -Format 'yyyyMMdd').md" -Encoding UTF8
Write-Host "Policy documentation generated" -ForegroundColor Green
```

### Script 4: Data Processing Agreement Review Tracker

```powershell
# Track Microsoft DPA review status for Copilot data processing
$dpaTracker = [PSCustomObject]@{
    AgreementType    = "Microsoft Data Processing Addendum (DPA)"
    CurrentVersion   = "January 2024"
    LastReviewed     = (Get-Date -Format "yyyy-MM-dd")
    ReviewedBy       = "Privacy Officer"
    NextReviewDue    = (Get-Date).AddMonths(12).ToString("yyyy-MM-dd")
    CopilotSpecific  = "Reviewed for Copilot data handling provisions"
    DataResidency    = "Verified data processing in specified region"
    SubProcessors    = "Microsoft sub-processor list reviewed"
}

Write-Host "Data Processing Agreement Review Status:" -ForegroundColor Cyan
$dpaTracker | Format-List
$dpaTracker | Export-Csv "DPAReview_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Diagnostic data audit | Quarterly | Script 1 |
| Feedback event monitoring | Monthly | Script 2 |
| Policy documentation update | Semi-annually | Script 3 |
| DPA review tracking | Annually | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate telemetry governance
- See [Troubleshooting](troubleshooting.md) for data governance issues
