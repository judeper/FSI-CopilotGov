# Control 4.7: Copilot Feedback and Telemetry Data Governance — PowerShell Setup

Automation scripts for configuring and auditing Copilot feedback and telemetry controls. Feedback policy settings are configurable via Microsoft Graph Beta cmdlets. Diagnostic data levels and connected experiences require Cloud Policy or Group Policy. Some settings remain portal-only — those are documented with their portal paths.

## Prerequisites

- **Modules:** `Microsoft.Graph.Beta.Reports`, `ExchangeOnlineManagement`
- **Permissions:** Entra Global Admin or M365 Global Admin (for feedback policy), Purview Compliance Admin (for audit log)
- **Licenses:** Microsoft 365 E5 or E5 Compliance (for audit log search)
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
# Graph API for feedback policy management (beta cmdlets)
Import-Module Microsoft.Graph.Beta.Reports
Connect-MgGraph -Scopes "OrgSettings-Microsoft365.ReadWrite.All"

# Security & Compliance for audit log search (Script 3)
Import-Module ExchangeOnlineManagement
Connect-IPPSSession
```

## Configurability Reference

Not all feedback and telemetry settings are PowerShell-configurable. The table below documents each setting's management path.

| Setting | Management Method | PowerShell Available | FSI Recommendation |
|---------|------------------|---------------------|-------------------|
| User feedback (thumbs up/down) | Graph Beta API | Yes — `Update-MgBetaAdminMicrosoft365AppsFeedbackPolicy` | Disabled |
| In-product surveys | Graph Beta API | Yes — `isReceiveSurveyEnabled` | Disabled |
| Email collection in feedback | Graph Beta API | Yes — `isEmailCollectionEnabled` | Disabled |
| Product research opt-in | Graph Beta API | Yes — `isProductResearchEnabled` | Disabled |
| Screenshot in feedback | Graph Beta API | Yes — `isScreenshotEnabled` | Disabled |
| Diagnostic data level | Cloud Policy / Group Policy | No — configure via M365 Apps Admin Center or GPO | Required (minimum) |
| Optional connected experiences | Cloud Policy / Group Policy | No — configure via M365 Apps Admin Center or GPO | Disabled |
| Copilot prompt history | Portal-only | No | Per organizational policy |
| Copilot model improvement opt-out | DPA contractual | No — not a tenant setting | Opt out via Microsoft DPA |

## Scripts

### Script 1: Audit and Configure Feedback Policy

Microsoft Graph Beta cmdlets control the tenant-wide feedback policy for Microsoft 365 apps including Copilot. For FSI environments, disabling all user-facing feedback channels helps limit data leaving the compliance boundary.

```powershell
# Audit and configure M365 feedback policy via Graph Beta API
# Note: These cmdlets are beta as of March 2026 — subject to change
# Requires: Microsoft.Graph.Beta.Reports module

# Retrieve current feedback policy settings
Write-Host "=== Current Feedback Policy Settings ===" -ForegroundColor Cyan
$currentPolicy = Get-MgBetaAdminMicrosoft365AppsFeedbackPolicy
$currentPolicy | Select-Object IsFeedbackEnabled, IsReceiveSurveyEnabled,
    IsEmailCollectionEnabled, IsProductResearchEnabled, IsScreenshotEnabled |
    Format-List

# Disable all user-facing feedback for FSI compliance
$params = @{
    isFeedbackEnabled        = $false
    isReceiveSurveyEnabled   = $false
    isEmailCollectionEnabled = $false
    isProductResearchEnabled = $false
    isScreenshotEnabled      = $false
}
Update-MgBetaAdminMicrosoft365AppsFeedbackPolicy -BodyParameter $params

Write-Host "Feedback policy updated — all user-facing feedback disabled" -ForegroundColor Green

# Verify the change
Write-Host "`n=== Updated Feedback Policy Settings ===" -ForegroundColor Cyan
Get-MgBetaAdminMicrosoft365AppsFeedbackPolicy |
    Select-Object IsFeedbackEnabled, IsReceiveSurveyEnabled,
        IsEmailCollectionEnabled, IsProductResearchEnabled, IsScreenshotEnabled |
    Format-List
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

### Script 4: Feedback Policy Verification Report

Generates a compliance-ready report combining the PowerShell-configurable feedback settings with documentation of portal-only and contractual controls. Organizations should verify the portal-only settings through manual review.

```powershell
# Generate feedback and telemetry governance verification report
# Combines automated checks (Graph API) with documented manual verification items

# Automated: Feedback policy via Graph Beta
$feedbackPolicy = Get-MgBetaAdminMicrosoft365AppsFeedbackPolicy

$automatedChecks = [PSCustomObject]@{
    Setting_IsFeedbackEnabled        = $feedbackPolicy.IsFeedbackEnabled
    Setting_IsReceiveSurveyEnabled   = $feedbackPolicy.IsReceiveSurveyEnabled
    Setting_IsEmailCollectionEnabled = $feedbackPolicy.IsEmailCollectionEnabled
    Setting_IsProductResearchEnabled = $feedbackPolicy.IsProductResearchEnabled
    Setting_IsScreenshotEnabled      = $feedbackPolicy.IsScreenshotEnabled
    CheckDate                        = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
}

Write-Host "=== Automated Feedback Policy Checks ===" -ForegroundColor Cyan
$automatedChecks | Format-List

# Flag non-compliant settings
$nonCompliant = @()
if ($feedbackPolicy.IsFeedbackEnabled) { $nonCompliant += "IsFeedbackEnabled is True" }
if ($feedbackPolicy.IsReceiveSurveyEnabled) { $nonCompliant += "IsReceiveSurveyEnabled is True" }
if ($feedbackPolicy.IsEmailCollectionEnabled) { $nonCompliant += "IsEmailCollectionEnabled is True" }
if ($feedbackPolicy.IsProductResearchEnabled) { $nonCompliant += "IsProductResearchEnabled is True" }
if ($feedbackPolicy.IsScreenshotEnabled) { $nonCompliant += "IsScreenshotEnabled is True" }

if ($nonCompliant.Count -gt 0) {
    Write-Warning "Non-compliant settings detected:"
    $nonCompliant | ForEach-Object { Write-Warning "  - $_" }
    Write-Host "Run Script 1 to remediate." -ForegroundColor Yellow
} else {
    Write-Host "All PowerShell-configurable feedback settings are disabled." -ForegroundColor Green
}

# Document portal-only items requiring manual verification
Write-Host "`n=== Manual Verification Required ===" -ForegroundColor Yellow
Write-Host @"
The following items are not verifiable via PowerShell:

1. Diagnostic data level (Cloud Policy / GPO)
   Verify at: config.office.com > Policy Management
   Expected: Required (minimum)

2. Optional connected experiences (Cloud Policy / GPO)
   Verify at: config.office.com > Policy Management
   Expected: Disabled

3. Copilot prompt history
   Verify at: M365 Admin Center > Copilot > Settings
   Expected: Per organizational policy

4. Copilot model improvement opt-out (DPA contractual)
   Verify with: Microsoft account team or DPA documentation
   Expected: Opted out for regulated workloads
"@

$automatedChecks | Export-Csv "FeedbackPolicyVerification_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Feedback policy verification | Monthly | Script 1 (verify section) |
| Copilot interaction audit | Monthly | Script 3 |
| Full governance verification report | Quarterly | Script 4 |
| Cloud Policy / GPO manual review | Semi-annually | Script 2 (manual steps) |

## Limitations

| Area | Detail |
|------|--------|
| Feedback cmdlets (beta) | `Update-MgBetaAdminMicrosoft365AppsFeedbackPolicy` is beta as of March 2026 — subject to breaking changes |
| Diagnostic data level | Not configurable via PowerShell — requires Cloud Policy (config.office.com) or Group Policy |
| Connected experiences | Not configurable via PowerShell — requires Cloud Policy or Group Policy |
| Copilot prompt history | Portal-only setting in M365 Admin Center > Copilot > Settings |
| Model improvement opt-out | Contractual control via Microsoft DPA — not a tenant admin setting |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate telemetry governance
- See [Troubleshooting](troubleshooting.md) for data governance issues
- Back to [Control 4.7](../../../controls/pillar-4-operations/4.7-feedback-telemetry.md)
