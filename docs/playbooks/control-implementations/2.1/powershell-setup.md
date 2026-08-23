# Control 2.1: DLP Policies for Microsoft 365 Copilot Interactions — PowerShell Setup

PowerShell examples for creating and verifying the documented sensitivity-label exclusion rule for the **Microsoft 365 Copilot and Copilot Chat** DLP location.

## Prerequisites

- **Module:** `ExchangeOnlineManagement`
- **Permissions:** A role Microsoft documents for editing Copilot DLP policies, such as Purview Compliance Admin or Purview Information Protection Admin
- **PowerShell:** A version supported by the current Exchange Online Management module
- **Licensing:** An eligible Purview Information Protection and Governance entitlement for file/email exclusion

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Script 1: Create the Copilot Policy and Label-Exclusion Rule

```powershell
$policyName = "FSI-Copilot-DLP-Protection"
$labelDisplayName = "Highly Confidential"

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
    -Comment "Copilot policy for approved sensitivity-label exclusions" `
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
    -Name "Exclude highly confidential content from Copilot processing" `
    -Policy $policyName `
    -AdvancedRule $advancedRule `
    -RestrictAccess @(@{
        setting = "ExcludeContentProcessing"
        value = "Block"
    })
```

This is Microsoft's documented PowerShell pattern for sensitivity-label exclusion. The Copilot location also supports two SIT-based actions: **Processing prompts** (preview and rolling out) and **Performing Web Searches**, plus the preview **Email is received from > External users** condition with content-processing exclusion. Configure those rules in the Purview portal unless Microsoft documents the applicable `New-DlpComplianceRule` syntax for the module version in use; don't substitute generic `BlockAccess`, workload-specific threshold, or guessed `-M365CopilotLocation` parameters.

## Script 2: Verify the Copilot Policy and Rules

```powershell
$policyName = "FSI-Copilot-DLP-Protection"
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

## Script 3: Verify Sensitive Information Types

```powershell
$requiredSensitiveTypes = @(
    "U.S. Social Security Number (SSN)",
    "Credit Card Number",
    "U.S. Bank Account Number"
)

foreach ($type in $requiredSensitiveTypes) {
    $result = Get-DlpSensitiveInformationType |
        Where-Object Name -eq $type |
        Select-Object -First 1
    if ($result) {
        $result | Format-Table Name, Id, RecommendedConfidence -AutoSize
    } else {
        Write-Warning "Sensitive information type '$type' wasn't found."
    }
}
```

`Get-DlpSensitiveInformationTypeRulePackage` returns rule packages, not the individual sensitive information types used in policy rules.

## Script 4: Export Copilot Interaction Audit Evidence

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

## Operational Notes

- Policy changes can take up to four hours to apply.
- Sensitivity-label exclusion can leave the protected item visible as a citation.
- Copilot DLP doesn't scan the contents of files uploaded directly into prompts; it evaluates typed prompt text.
- Validate prompt blocking separately because that action is in preview and rolling out.

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate each supported DLP action
- See [Troubleshooting](troubleshooting.md) for enforcement issues
- Back to [Control 2.1](../../../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md)
