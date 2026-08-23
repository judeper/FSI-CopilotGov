# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — PowerShell Setup

Automation scripts for implementing and monitoring privacy controls for consumer financial information when using Copilot, including incident response automation for the 72-hour vendor notification requirement under SEC Rule 248.30(a)(3).

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

### Script 5: Incident Response Timer and Notification Tracking (Rule 248.30(a)(3))

```powershell
# Track the 72-hour vendor notification window for Reg S-P compliance
# Run this script when a Copilot NPI incident is detected

param(
    [Parameter(Mandatory=$true)]
    [string]$IncidentDescription,

    [Parameter(Mandatory=$true)]
    [ValidateSet("Critical","High","Medium","Low")]
    [string]$Severity,

    [Parameter(Mandatory=$false)]
    [datetime]$DetectionTime = (Get-Date)
)

$incidentId = "REGSP-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
$notificationDeadline72hr = $DetectionTime.AddHours(72)
$notificationDeadline30day = $DetectionTime.AddDays(30)

$incidentRecord = [PSCustomObject]@{
    IncidentId            = $incidentId
    DetectedAt            = $DetectionTime.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    Severity              = $Severity
    Description           = $IncidentDescription
    InternalEscalationBy  = $DetectionTime.AddHours(4).ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    ExecutiveNotificationBy = $DetectionTime.AddHours(24).ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    VendorNotificationBy  = $notificationDeadline72hr.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")  # Rule 248.30(a)(3)
    CustomerNotificationBy = $notificationDeadline30day.ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ss 'UTC'")
    VendorNotified        = "PENDING"
    CustomerNotified      = "PENDING"
}

Write-Host "=== Reg S-P NPI Incident Tracker ===" -ForegroundColor Yellow
Write-Host "Incident ID: $incidentId" -ForegroundColor Cyan
Write-Host "Severity: $Severity" -ForegroundColor $(if ($Severity -eq "Critical") { "Red" } else { "Yellow" })
Write-Host ""
Write-Host "REQUIRED NOTIFICATION DEADLINES:"
Write-Host "  Internal escalation:    $($incidentRecord.InternalEscalationBy)"
Write-Host "  Executive notification: $($incidentRecord.ExecutiveNotificationBy)"
Write-Host "  Service-provider notification tracking: $($incidentRecord.VendorNotificationBy)  [Rule 248.30(a)(3) — 72-HOUR DEADLINE]" -ForegroundColor Red
Write-Host "  Customer notification:  $($incidentRecord.CustomerNotificationBy)  [30-day deadline]"
Write-Host ""
Write-Host "This tracker doesn't send a notification. Use the institution's approved incident workflow."
Write-Host "For Microsoft-determined service incidents, monitor designated tenant admin contacts and Microsoft 365 Service health."

$incidentRecord | Export-Csv "RegSP_Incident_$incidentId.csv" -NoTypeInformation
Write-Host "`nIncident record saved to: RegSP_Incident_$incidentId.csv" -ForegroundColor Green
```

**Usage example:**
```powershell
.\Script5-IncidentTracker.ps1 -IncidentDescription "Copilot Chat surfaced client SSN to unauthorized advisor" -Severity "Critical"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Copilot policy and rule verification | Weekly | Script 2 |
| NPI SIT verification | Quarterly | Script 3 |
| Copilot interaction audit export | Monthly | Script 4 |
| Incident response timer | On-demand (at incident detection) | Script 5 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate privacy protections
- See [Troubleshooting](troubleshooting.md) for privacy control issues
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
