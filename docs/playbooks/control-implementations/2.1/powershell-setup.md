# Control 2.1: DLP Policies for M365 Copilot Interactions — PowerShell Setup

Automation scripts for managing DLP policies that protect Copilot interactions. Control 2.1 requires two separate DLP policies — scripts are provided for both the label-based response blocking policy (Type 1) and the SIT-based prompt blocking policy (Type 2).

## Prerequisites

- Security & Compliance PowerShell (`ExchangeOnlineManagement`)
- Compliance Administrator role
- Microsoft 365 E5 or E5 Compliance license

## Scripts

### Script 1: Create Label-Based Response Blocking Policy (Type 1)

```powershell
# Create DLP policy for label-based response blocking in Copilot
# This policy blocks Copilot from surfacing Highly Confidential labeled content
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

# Create the label-based DLP policy (Type 1)
New-DlpCompliancePolicy -Name "FSI Copilot DLP - Label-Based Response Blocking" `
    -Comment "Blocks Copilot from surfacing Highly Confidential and MNPI labeled content in responses" `
    -Mode "TestWithNotifications" `
    -M365CopilotLocation All

# Create DLP rule for Highly Confidential label
# NOTE: Verify -ContentContainsSensitivityLabels syntax against your live tenant —
# parameter name and hashtable structure may vary by module version.
New-DlpComplianceRule -Name "Block HC Label in Copilot Response" `
    -Policy "FSI Copilot DLP - Label-Based Response Blocking" `
    -ContentContainsSensitivityLabel @{
        LabelName = "Highly Confidential"
        IncludeSubLabels = $true
    } `
    -BlockAccess $true `
    -NotifyUser "SiteAdmin","LastModifier" `
    -GenerateIncidentReport "SiteAdmin" `
    -IncidentReportContent "All"

Write-Host "Type 1 (label-based) DLP policy created in test mode."
Write-Host "Review matches before enabling enforcement."
```

### Script 2: Create SIT-Based Prompt Blocking Policy (Type 2)

```powershell
# Create DLP policy for SIT-based prompt blocking in Copilot
# This policy blocks Copilot from processing prompts containing sensitive data
# These two policy types must be configured as separate DLP rules — they cannot be
# combined within a single DLP rule, but may exist as separate rules within the same policy
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

# Create the SIT-based prompt blocking policy (Type 2)
New-DlpCompliancePolicy -Name "FSI Copilot DLP - SIT-Based Prompt Blocking" `
    -Comment "Blocks Copilot from processing user prompts containing FSI-sensitive information types" `
    -Mode "TestWithNotifications" `
    -M365CopilotLocation All

# Create DLP rule for SSN detection in prompts
New-DlpComplianceRule -Name "Block SSN in Copilot Prompt" `
    -Policy "FSI Copilot DLP - SIT-Based Prompt Blocking" `
    -ContentContainsSensitiveInformation @{
        Name = "U.S. Social Security Number (SSN)"
        MinCount = 1
        MinConfidence = 85
    } `
    -BlockAccess $true `
    -NotifyUser "SiteAdmin","LastModifier" `
    -NotifyUserType "NotSet"

# Create DLP rule for credit card detection in prompts
New-DlpComplianceRule -Name "Block Credit Card in Copilot Prompt" `
    -Policy "FSI Copilot DLP - SIT-Based Prompt Blocking" `
    -ContentContainsSensitiveInformation @{
        Name = "Credit Card Number"
        MinCount = 1
        MinConfidence = 85
    } `
    -BlockAccess $true `
    -NotifyUser "SiteAdmin","LastModifier" `
    -NotifyUserType "NotSet"

# Create DLP rule for ABA routing number detection in prompts
New-DlpComplianceRule -Name "Block ABA Routing in Copilot Prompt" `
    -Policy "FSI Copilot DLP - SIT-Based Prompt Blocking" `
    -ContentContainsSensitiveInformation @{
        Name = "ABA Routing Number"
        MinCount = 1
        MinConfidence = 85
    } `
    -BlockAccess $true `
    -NotifyUser "SiteAdmin","LastModifier" `
    -NotifyUserType "NotSet"

Write-Host "Type 2 (SIT-based prompt blocking) DLP policy created in test mode."
Write-Host "This is a separate policy from the label-based policy - both are required."
```

### Script 3: DLP Policy Status and Match Report

```powershell
# Report on all Copilot DLP policies - includes both policy types
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$policies = Get-DlpCompliancePolicy | Where-Object { $_.Name -match "Copilot|FSI" }

$policyReport = @()
foreach ($policy in $policies) {
    $rules = Get-DlpComplianceRule -Policy $policy.Name
    $policyReport += [PSCustomObject]@{
        PolicyName  = $policy.Name
        Mode        = $policy.Mode
        Enabled     = $policy.Enabled
        RuleCount   = $rules.Count
        Priority    = $policy.Priority
        Created     = $policy.CreationDate
    }
}

Write-Host "=== Copilot DLP Policies (Both Policy Types) ==="
$policyReport | Format-Table PolicyName, Mode, Enabled, RuleCount -AutoSize

# Verify both policy types exist
$labelBasedExists = $policyReport | Where-Object PolicyName -match "Label-Based"
$sitBasedExists = $policyReport | Where-Object PolicyName -match "SIT-Based|Prompt"
if (-not $labelBasedExists) { Write-Warning "MISSING: Label-Based Response Blocking policy not found" }
if (-not $sitBasedExists) { Write-Warning "MISSING: SIT-Based Prompt Blocking policy not found" }

$policyReport | Export-Csv "CopilotDLPPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: DLP Incident Report Export

```powershell
# Export DLP incident data for compliance review - covers both policy types
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30).ToString("MM/dd/yyyy")
$endDate = (Get-Date).ToString("MM/dd/yyyy")

$incidents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -RecordType "DlpAll" -ResultSize 1000

$incidentReport = @()
foreach ($incident in $incidents) {
    $data = $incident.AuditData | ConvertFrom-Json
    $incidentReport += [PSCustomObject]@{
        Date          = $incident.CreationDate
        User          = $incident.UserIds
        Operation     = $incident.Operations
        PolicyName    = $data.PolicyDetails.PolicyName
        SensitiveInfo = ($data.SensitiveInfoDetectionIsIncluded -join ", ")
        Action        = $data.Actions
    }
}

Write-Host "DLP incidents in last 30 days: $($incidentReport.Count)"

# Separate incidents by policy type for reporting
$labelBasedIncidents = $incidentReport | Where-Object PolicyName -match "Label-Based"
$sitBasedIncidents = $incidentReport | Where-Object PolicyName -match "SIT-Based|Prompt"
Write-Host "  Label-based (Type 1) matches: $($labelBasedIncidents.Count)"
Write-Host "  SIT-based prompt (Type 2) matches: $($sitBasedIncidents.Count)"

$incidentReport | Export-Csv "DLPIncidents_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Policy Status Check | Daily | Verify both DLP policy types remain active |
| Default Policy Review | Weekly (first 30 days) | Review simulation mode matches before enabling enforcement |
| Incident Report | Weekly | Review DLP matches by policy type for false positives |
| Policy Configuration Export | Monthly | Document policy settings for audit trail |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate both DLP policy types
- See [Troubleshooting](troubleshooting.md) for DLP policy issues, including guidance on why label-based and SIT-based policies cannot be combined
