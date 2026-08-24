# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — PowerShell Setup

Automation scripts for implementing and monitoring privacy controls for consumer financial information when using Copilot, including local intake and timing evidence for the provider-to-institution notification requirement in SEC Rule 248.30(a)(5).

## Prerequisites

- **Module:** `ExchangeOnlineManagement`
- **Permissions:** A role Microsoft documents for editing Copilot DLP policies, such as Purview Compliance Admin or Purview Information Protection Admin
- **PowerShell:** A version supported by the current Exchange Online Management module

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Create DLP Policy for Consumer Financial Information

```powershell
$policyName = "FSI-RegSP-Copilot-Privacy-Protection"
$labelDisplayName = "Confidential - Client NPI"

$label = Get-Label |
    Where-Object DisplayName -eq $labelDisplayName |
    Select-Object -First 1
if (-not $label) {
    throw "Required sensitivity label '$labelDisplayName' wasn't found."
}

$locations = @'
[{
  "Workload": "Applications",
  "Location": "470f2276-e011-4e9d-a6ec-20768be3a4b0",
  "Inclusions": [{"Type": "Tenant", "Identity": "All"}]
}]
'@

New-DlpCompliancePolicy `
    -Name $policyName `
    -Comment "Copilot policy for approved NPI safeguards" `
    -Locations $locations `
    -EnforcementPlanes @("CopilotExperiences") `
    -Mode TestWithoutNotifications

$advancedRule = @{
    Version = "1.0"
    Condition = @{
        Operator = "And"
        SubConditions = @(
            @{
                ConditionName = "ContentContainsSensitiveInformation"
                Value = @(
                    @{
                        groups = @(
                            @{
                                Operator = "Or"
                                labels = @(
                                    @{
                                        name = $label.Guid.ToString()
                                        type = "Sensitivity"
                                    }
                                )
                                name = "Default"
                            }
                        )
                    }
                )
            }
        )
    }
} | ConvertTo-Json -Depth 100

New-DlpComplianceRule `
    -Name "Exclude labeled client NPI from Copilot processing" `
    -Policy $policyName `
    -AdvancedRule $advancedRule `
    -RestrictAccess @(@{
        setting = "ExcludeContentProcessing"
        value = "Block"
    })
```

This uses Microsoft's documented PowerShell pattern for sensitivity-label exclusion. The Copilot location also supports two SIT-based actions: **Processing prompts** (preview and rolling out) and **Performing Web Searches**, plus the preview **Email is received from > External users** condition with content-processing exclusion. Configure those rules in the Purview portal unless Microsoft documents the applicable `New-DlpComplianceRule` syntax for the module version in use; don't substitute generic `BlockAccess` or volume-threshold actions from other DLP workloads.

### Script 2: Verify Copilot Policy and Rules

```powershell
$policyName = "FSI-RegSP-Copilot-Privacy-Protection"
$copilotLocationId = "470f2276-e011-4e9d-a6ec-20768be3a4b0"

$policy = Get-DlpCompliancePolicy -Identity $policyName
if (-not $policy) {
    throw "Policy '$policyName' wasn't returned."
}
if (-not ($policy.EnforcementPlanes -contains "CopilotExperiences")) {
    throw "Policy is missing the CopilotExperiences enforcement plane."
}
if ([string]$policy.Locations -notmatch [regex]::Escape($copilotLocationId)) {
    throw "Policy is missing the Microsoft 365 Copilot and Copilot Chat location."
}

$policy | Format-List Name, Mode, Enabled, Locations, EnforcementPlanes
Get-DlpComplianceRule -Policy $policyName |
    Format-Table Name, Disabled, Priority -AutoSize
```

Don't require a top-level `Workload` property from `Get-DlpCompliancePolicy`; Microsoft documents `Workload: "Applications"` inside the `Locations` JSON.

### Script 3: Verify NPI Sensitive Information Types

```powershell
$sensitiveTypes = @(
    "U.S. Social Security Number (SSN)",
    "Credit Card Number",
    "U.S. Bank Account Number",
    "U.S. Individual Taxpayer Identification Number (ITIN)"
)

foreach ($type in $sensitiveTypes) {
    $result = Get-DlpSensitiveInformationType |
        Where-Object Name -eq $type |
        Select-Object -First 1
    if ($result) {
        $result | Format-Table Name, Id, RecommendedConfidence -AutoSize
    } else {
        Write-Warning "Sensitive information type '$type' wasn't found."
    }
}

Write-Host "`nReview aggregate classifications at:" -ForegroundColor Yellow
Write-Host "Purview > Solutions > Information Protection > Explorers > Data explorer"
```

`Get-DlpSensitiveInformationTypeRulePackage` returns rule packages, not the individual sensitive information types used in policy rules.

### Script 4: Export Copilot Interaction Audit Evidence

```powershell
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$copilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -Operations CopilotInteraction `
    -ResultSize 5000

$copilotEvents |
    Select-Object CreationDate, UserIds, Operations, AuditData |
    Export-Csv "CopilotInteraction_Audit_$(Get-Date -Format 'yyyyMMdd').csv" `
        -NoTypeInformation

Write-Host "Exported $($copilotEvents.Count) CopilotInteraction records."
```

Use **Purview > Data Loss Prevention > Alerts** for DLP alert investigation and **Purview > Solutions > DSPM > Discover > Activity explorer > AI activities** for sensitive interaction details. Viewing prompt and response bodies requires the additional content-viewer permissions Microsoft documents.

### Script 5: Service-Provider Intake and Separate Notification Clocks (Rule 248.30(a)(5))

```powershell
# Record a provider-to-institution notice for Reg S-P evidence.
# The 72-hour timing evaluation starts when the service provider becomes aware
# of a qualifying breach in a customer-information system it maintains.
# This local tracker neither sends notices nor substitutes for legal review.

param(
    [Parameter(Mandatory=$true)]
    [string]$IncidentDescription,

    [Parameter(Mandatory=$true)]
    [ValidateSet("Critical","High","Medium","Low")]
    [string]$Severity,

    [Parameter(Mandatory=$true)]
    [string]$ServiceProvider,

    [Parameter(Mandatory=$true)]
    [datetime]$ProviderAwarenessTime,

    [Parameter(Mandatory=$true)]
    [datetime]$InstitutionReceiptTime,

    [Parameter(Mandatory=$true)]
    [datetime]$InstitutionAwarenessTime,

    [Parameter(Mandatory=$true)]
    [string]$ProviderReportedScope,

    [Parameter(Mandatory=$false)]
    [ValidateSet("Pending investigation","Notification required","Notification not required")]
    [string]$AffectedIndividualNotificationStatus = "Pending investigation",

    [Parameter(Mandatory=$false)]
    [datetime]$InstitutionResponseInitiatedTime = (Get-Date)
)

$incidentId = "REGSP-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
$providerNotificationDue = $ProviderAwarenessTime.AddHours(72)
$affectedIndividualNotificationDue = $InstitutionAwarenessTime.AddDays(30)

$providerNotificationSlaEvaluation = if ($InstitutionReceiptTime -le $providerNotificationDue) {
    "MET: institution receipt was on or before the provider-awareness deadline."
} else {
    "LATE: institution receipt was after the provider-awareness deadline."
}

$incidentRecord = [PSCustomObject]@{
    IncidentId                              = $incidentId
    Severity                                = $Severity
    Description                             = $IncidentDescription
    ServiceProvider                         = $ServiceProvider
    ProviderNotificationDirection           = "Provider to institution"
    ProviderAwarenessAt                     = $ProviderAwarenessTime.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    InstitutionReceiptAt                    = $InstitutionReceiptTime.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    ProviderNotificationDueBy               = $providerNotificationDue.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    ProviderNotificationSlaEvaluation       = $providerNotificationSlaEvaluation
    ProviderReportedScope                   = $ProviderReportedScope
    InstitutionAwarenessAt                  = $InstitutionAwarenessTime.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    InstitutionResponseInitiatedAt          = $InstitutionResponseInitiatedTime.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    AffectedIndividualNotificationStatus    = $AffectedIndividualNotificationStatus
    AffectedIndividualNotificationDueBy     = $affectedIndividualNotificationDue.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
}

Write-Host "=== Reg S-P NPI Incident Tracker ===" -ForegroundColor Yellow
Write-Host "Incident ID: $incidentId" -ForegroundColor Cyan
Write-Host "Severity: $Severity" -ForegroundColor $(if ($Severity -eq "Critical") { "Red" } else { "Yellow" })
Write-Host ""
Write-Host "SERVICE PROVIDER -> INSTITUTION (Rule 248.30(a)(5)):"
Write-Host "  Provider awareness:     $($incidentRecord.ProviderAwarenessAt)"
Write-Host "  Institution receipt:    $($incidentRecord.InstitutionReceiptAt)"
Write-Host "  Provider deadline:      $($incidentRecord.ProviderNotificationDueBy)  [72 hours from provider awareness]"
Write-Host "  Timing evaluation:      $($incidentRecord.ProviderNotificationSlaEvaluation)"
Write-Host "  Provider-reported scope: $($incidentRecord.ProviderReportedScope)"
Write-Host ""
Write-Host "INSTITUTION RESPONSE PROGRAM (Rule 248.30(a)(3)):"
Write-Host "  Institution awareness:  $($incidentRecord.InstitutionAwarenessAt)"
Write-Host "  Response initiated:     $($incidentRecord.InstitutionResponseInitiatedAt)"
Write-Host ""
Write-Host "AFFECTED-INDIVIDUAL NOTIFICATION (Rule 248.30(a)(4)):"
Write-Host "  Status:                 $($incidentRecord.AffectedIndividualNotificationStatus)"
Write-Host "  Planning deadline:      $($incidentRecord.AffectedIndividualNotificationDueBy)  [only if notice is required]"
Write-Host ""
Write-Host "This tracker does not send a notification or make the Rule 248.30(a)(4) determination."
Write-Host "Do not use the institution's detection time as the Rule 248.30(a)(5) 72-hour trigger."
Write-Host "Use the institution's approved incident workflow and retain the supporting evidence."

$incidentRecord | Export-Csv "RegSP_Incident_$incidentId.csv" -NoTypeInformation
Write-Host "`nIncident record saved to: RegSP_Incident_$incidentId.csv" -ForegroundColor Green
```

**Usage example:**
```powershell
.\Script5-IncidentTracker.ps1 `
    -IncidentDescription "Provider reported unauthorized access to a Copilot customer-information system" `
    -Severity "Critical" `
    -ServiceProvider "Contoso service provider" `
    -ProviderAwarenessTime "2026-08-24T09:00:00Z" `
    -InstitutionReceiptTime "2026-08-24T11:00:00Z" `
    -InstitutionAwarenessTime "2026-08-24T11:00:00Z" `
    -ProviderReportedScope "Potential exposure of customer account records; investigation ongoing"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Copilot policy and rule verification | Weekly | Script 2 |
| NPI SIT verification | Quarterly | Script 3 |
| Copilot interaction audit export | Monthly | Script 4 |
| Service-provider intake and notification timing evidence | On-demand (on provider notice or institution awareness) | Script 5 |

## Regulatory Basis

- [SEC Rule 248.30 — current regulatory text](https://www.ecfr.gov/current/title-17/chapter-II/part-248/section-248.30)
- [SEC Final Rule — Regulation S-P Amendments (Release No. 34-100155)](https://www.sec.gov/files/rules/final/2024/34-100155.pdf)
- [Federal Register — Regulation S-P, 89 FR 47688 (June 3, 2024), document 2024-11116](https://www.federalregister.gov/documents/2024/06/03/2024-11116/regulation-s-p-privacy-of-consumer-financial-information-and-safeguarding-customer-information)

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate privacy protections
- See [Troubleshooting](troubleshooting.md) for privacy control issues
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
