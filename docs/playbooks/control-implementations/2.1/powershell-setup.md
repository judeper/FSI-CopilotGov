# Control 2.1: DLP Policies for M365 Copilot Interactions — PowerShell Setup

Automation scripts for managing DLP policies that protect Copilot interactions. Control 2.1 requires separate DLP rules for label-based response blocking (Type 1), SIT-based prompt blocking (Type 2), and SIT-based web-search restriction (Type 3). Separate policies may be used when operationally needed.

## Prerequisites

- Security & Compliance PowerShell (`ExchangeOnlineManagement`)
- Purview Compliance Admin role
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
# Copilot DLP rule types must be configured as separate DLP rules. Sensitivity-label
# and SIT conditions cannot be combined within a single DLP rule, but separate rules
# may exist within the same policy.
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

### Script 2a: Create SIT-Based Web Search Restriction Policy (Type 3)

```powershell
# Create DLP policy for SIT-based web-search restriction in Copilot
# This policy prevents sensitive prompt data from being sent to external web search providers.
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

# Create the SIT-based web-search restriction policy (Type 3)
New-DlpCompliancePolicy -Name "FSI Copilot DLP - SIT-Based Web Search Restriction" `
    -Comment "Blocks external web-search grounding when user prompts contain FSI-sensitive information types" `
    -Mode "TestWithNotifications" `
    -M365CopilotLocation All

# Create DLP rule for sensitive information in prompts that would otherwise use web search.
# NOTE: Verify the exact action parameter mapping in your live tenant/module version.
# In the Purview portal, the action is:
# Prevent Copilot from processing content > Performing Web Searches.
New-DlpComplianceRule -Name "Restrict Web Search for Sensitive Copilot Prompts" `
    -Policy "FSI Copilot DLP - SIT-Based Web Search Restriction" `
    -ContentContainsSensitiveInformation @(
        @{ Name = "U.S. Social Security Number (SSN)"; MinCount = 1; MinConfidence = 85 },
        @{ Name = "Credit Card Number"; MinCount = 1; MinConfidence = 85 },
        @{ Name = "ABA Routing Number"; MinCount = 1; MinConfidence = 85 }
    ) `
    -BlockAccess $true `
    -NotifyUser "SiteAdmin","LastModifier" `
    -NotifyUserType "NotSet"

Write-Host "Type 3 (SIT-based web-search restriction) DLP policy created in test mode."
Write-Host "Validate that external web search is blocked while permitted internal grounding still works."
```

### Script 3: DLP Policy Status and Match Report

```powershell
# Report on all Copilot DLP policies - includes all Copilot DLP rule types
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

Write-Host "=== Copilot DLP Policies (All Copilot DLP Rule Types) ==="
$policyReport | Format-Table PolicyName, Mode, Enabled, RuleCount -AutoSize

# Verify all Copilot DLP rule types exist
$labelBasedExists = $policyReport | Where-Object PolicyName -match "Label-Based"
$sitBasedExists = $policyReport | Where-Object PolicyName -match "SIT-Based|Prompt"
$webSearchExists = $policyReport | Where-Object PolicyName -match "Web Search|Web-Search"
if (-not $labelBasedExists) { Write-Warning "MISSING: Label-Based Response Blocking policy not found" }
if (-not $sitBasedExists) { Write-Warning "MISSING: SIT-Based Prompt Blocking policy not found" }
if (-not $webSearchExists) { Write-Warning "MISSING: SIT-Based Web Search Restriction policy not found" }

$policyReport | Export-Csv "CopilotDLPPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: DLP Incident Report Export

```powershell
# Export DLP incident data for compliance review - covers all Copilot DLP rule types
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
$webSearchIncidents = $incidentReport | Where-Object PolicyName -match "Web Search|Web-Search"
Write-Host "  Label-based (Type 1) matches: $($labelBasedIncidents.Count)"
Write-Host "  SIT-based prompt (Type 2) matches: $($sitBasedIncidents.Count)"
Write-Host "  SIT-based web-search restriction (Type 3) matches: $($webSearchIncidents.Count)"

$incidentReport | Export-Csv "DLPIncidents_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Policy Status Check | Daily | Verify all Copilot DLP rule types remain active |
| Default Policy Review | Weekly (first 30 days) | Review simulation mode matches before enabling enforcement |
| Incident Report | Weekly | Review DLP matches by policy type for false positives |
| Policy Configuration Export | Monthly | Document policy settings for audit trail |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate all Copilot DLP rule types
- See [Troubleshooting](troubleshooting.md) for DLP policy issues, including guidance on why label-based and SIT-based policies cannot be combined
- Back to [Control 2.1](../../../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md)
