# Control 4.7: Copilot Feedback and Telemetry Data Governance — PowerShell Setup

Automation references for configuring and auditing Copilot feedback and telemetry controls. Microsoft Learn documents feedback/survey controls through Cloud Policy service or Group Policy, while diagnostic data levels and connected experiences also require Cloud Policy or Group Policy. Tenant-specific Graph surfaces can change, so treat any Graph feedback-policy automation as tenant-verified rather than authoritative.

## Prerequisites

- **Modules:** `Microsoft.Graph.Authentication`, `ExchangeOnlineManagement` (for organization context and audit-log review only)
- **Permissions:** Entra Global Admin or M365 Global Admin (for policy evidence), Purview Compliance Admin (for audit log)
- **Licenses:** Microsoft 365 E5 or E5 Compliance (for audit log search)
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
# Graph is used here only for organization context; feedback/survey policies are verified through Cloud Policy or Group Policy evidence.
Import-Module Microsoft.Graph.Authentication
Connect-MgGraph -Scopes "Organization.Read.All"

# Security & Compliance for audit log search (Script 3)
Import-Module ExchangeOnlineManagement
Connect-IPPSSession
```

## Configurability Reference

Not all feedback and telemetry settings are PowerShell-configurable. The table below documents each setting's management path.

| Setting | Management Method | PowerShell Available | FSI Recommendation |
|---------|------------------|---------------------|-------------------|
| User feedback (thumbs up/down) | Cloud Policy / Group Policy | Tenant-verified only | Firm-defined |
| In-product surveys | Cloud Policy / Group Policy | Tenant-verified only | Firm-defined |
| Follow-up contact / email collection | Cloud Policy / Group Policy | Tenant-verified only | Disabled for regulated populations unless approved |
| Feedback portal / product research participation | Cloud Policy where available | Tenant-verified only | Disabled unless approved |
| Screenshots, attachments, logs, content samples | Cloud Policy / Group Policy | Tenant-verified only | Disabled for regulated populations unless approved |
| Diagnostic data level | Cloud Policy / Group Policy | No — configure via Cloud Policy or GPO | Required unless justified |
| Optional connected experiences | Cloud Policy / Group Policy | No — configure via Cloud Policy or GPO | Disabled unless justified |
| Copilot prompt history | Portal-only | No | Per organizational policy |
| Copilot model improvement opt-out | DPA contractual | No — not a tenant setting | Verify through Microsoft DPA / account team |

## Scripts

### Script 1: Feedback Policy Manual Evidence Checklist

Use Cloud Policy service or Group Policy to manage feedback and survey controls for Microsoft 365 apps and Copilot. This script records the required evidence checklist; it does not claim to configure feedback settings through Graph.

```powershell
$checks = @(
    [PSCustomObject]@{ Setting = 'Allow users to submit feedback to Microsoft'; Expected = 'Firm-defined'; Evidence = 'Cloud Policy/GPO screenshot or export' }
    [PSCustomObject]@{ Setting = 'Allow users to receive and respond to in-product surveys'; Expected = 'Firm-defined'; Evidence = 'Cloud Policy/GPO screenshot or export' }
    [PSCustomObject]@{ Setting = 'Allow users to include screenshots and attachments'; Expected = 'Disabled unless approved'; Evidence = 'Cloud Policy/GPO screenshot or export' }
    [PSCustomObject]@{ Setting = 'Allow users to include log files and relevant content samples'; Expected = 'Disabled unless approved'; Evidence = 'Cloud Policy/GPO screenshot or export' }
    [PSCustomObject]@{ Setting = 'Allow Microsoft to follow up on feedback submitted by users'; Expected = 'Disabled unless approved'; Evidence = 'Cloud Policy/GPO screenshot or export' }
)
$checks | Format-Table -AutoSize
$checks | Export-Csv "FeedbackPolicyManualChecks_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Diagnostic Data and Connected Experiences Reference

Diagnostic data levels and connected experience controls are managed via Microsoft 365 Cloud Policy or Group Policy — not PowerShell cmdlets. This script documents the recommended GPO paths and validates that org-level settings are accessible.

```powershell
# Document diagnostic data and connected experience settings
# These settings are NOT configurable via PowerShell — use Cloud Policy or GPO
# This script validates org connectivity and documents the configuration paths

# Verify org context
$org = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/organization" `
    -OutputType PSObject

Write-Host "=== Organization Context ===" -ForegroundColor Cyan
Write-Host "Organization: $($org.value[0].displayName)"
Write-Host "Tenant ID: $($org.value[0].id)"

Write-Host "`n=== Diagnostic Data — Configuration Paths (Not PowerShell) ===" -ForegroundColor Yellow
Write-Host @"

The following settings require Cloud Policy or Group Policy configuration:

1. Diagnostic data level
   Cloud Policy: config.office.com > Customization > Policy Management
   GPO: Computer Config > Admin Templates > Microsoft Office 2016 > Privacy > Trust Center
        > Configure the level of client software diagnostic data sent to Microsoft
   FSI value: Required (minimum collection)

2. Optional connected experiences
   Cloud Policy: Same path as above
   GPO: Computer Config > Admin Templates > Microsoft Office 2016 > Privacy > Trust Center
        > Allow the use of additional optional connected experiences in Office
   FSI value: Disabled

3. Copilot prompt history
   Portal-only: M365 Admin Center > Copilot > Settings > Prompt history
   No PowerShell cmdlet available

4. Copilot model improvement opt-out
   This is a contractual control managed via the Microsoft Data Processing Agreement (DPA).
   It is not a tenant admin setting — organizations should verify opt-out status with their
   Microsoft account team or through the DPA amendment process.
"@
```

### Script 3: Copilot Interaction Audit for Telemetry Governance

This script searches the Unified Audit Log for Copilot interaction events to support telemetry governance reviews. It reports on Copilot usage patterns across apps, which helps verify that feedback and data controls are functioning as intended.

```powershell
# Search Copilot interaction events in the Unified Audit Log
# Requires: ExchangeOnlineManagement module, Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$copilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

Write-Host "=== Copilot Interaction Events (Last 30 Days) ===" -ForegroundColor Cyan
Write-Host "Total events: $($copilotEvents.Count)"

if ($copilotEvents.Count -gt 0) {
    # Parse and summarize by app surface
    $parsed = $copilotEvents | ForEach-Object {
        $auditData = $_.AuditData | ConvertFrom-Json
        [PSCustomObject]@{
            Date      = $_.CreationDate
            User      = $_.UserIds
            Operation = $_.Operations
            AppHost   = $auditData.AppHost
        }
    }

    Write-Host "`nCopilot usage by application:" -ForegroundColor Cyan
    $parsed | Group-Object AppHost |
        Select-Object @{N='Application';E={$_.Name}}, @{N='Events';E={$_.Count}} |
        Sort-Object Events -Descending |
        Format-Table -AutoSize

    $parsed | Export-Csv "CopilotInteractions_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
} else {
    Write-Host "No Copilot interaction events found in the audit log for this period."
}
```

### Script 4: Feedback and Telemetry Verification Report

Generates a compliance-ready manual verification report combining Cloud Policy/GPO evidence requirements with portal-only and contractual controls.

```powershell
$manualChecks = @(
    [PSCustomObject]@{ Control = 'Feedback policies'; Expected = 'Cloud Policy/GPO evidence attached'; Status = 'Manual verification required' }
    [PSCustomObject]@{ Control = 'Diagnostic data level'; Expected = 'Required unless firm-approved exception'; Status = 'Manual verification required' }
    [PSCustomObject]@{ Control = 'Optional connected experiences'; Expected = 'Disabled unless firm-approved exception'; Status = 'Manual verification required' }
    [PSCustomObject]@{ Control = 'Copilot prompt history'; Expected = 'Per organizational policy'; Status = 'Manual verification required' }
    [PSCustomObject]@{ Control = 'DPA/model-improvement posture'; Expected = 'Reviewed with legal/privacy or Microsoft account team'; Status = 'Manual verification required' }
)
$manualChecks | Format-Table -AutoSize
$manualChecks | Export-Csv "FeedbackTelemetryManualChecks_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Feedback policy evidence review | Monthly | Script 1 |
| Copilot interaction audit | Monthly | Script 3 |
| Full governance verification report | Quarterly | Script 4 |
| Cloud Policy / GPO manual review | Semi-annually | Script 2 (manual steps) |

## Limitations

| Area | Detail |
|------|--------|
| Diagnostic data level | Not configurable via PowerShell — requires Cloud Policy (config.office.com) or Group Policy |
| Connected experiences | Not configurable via PowerShell — requires Cloud Policy or Group Policy |
| Copilot prompt history | Portal-only setting in M365 Admin Center > Copilot > Settings |
| Model improvement opt-out | Contractual control via Microsoft DPA — not a tenant admin setting |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate telemetry governance
- See [Troubleshooting](troubleshooting.md) for data governance issues
- Back to [Control 4.7](../../../controls/pillar-4-operations/4.7-feedback-telemetry.md)
