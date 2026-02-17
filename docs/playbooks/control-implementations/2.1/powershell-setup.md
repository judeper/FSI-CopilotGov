# Control 2.1: DLP Policies for M365 Copilot Interactions — PowerShell Setup

Automation scripts for managing DLP policies that protect Copilot interactions.

## Prerequisites

- Security & Compliance PowerShell (`ExchangeOnlineManagement`)
- Compliance Administrator role
- Microsoft 365 E5 or E5 Compliance license

## Scripts

### Script 1: Create Copilot DLP Policy

```powershell
# Create a DLP policy targeting Copilot interactions for FSI sensitive data
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

# Create the DLP policy
New-DlpCompliancePolicy -Name "FSI Copilot DLP - Financial Data" `
    -Comment "Protects sensitive financial data in Copilot interactions" `
    -Mode "TestWithNotifications" `
    -ExchangeLocation "All" `
    -SharePointLocation "All" `
    -OneDriveLocation "All"

# Create DLP rule for SSN detection
New-DlpComplianceRule -Name "Block SSN in Copilot" `
    -Policy "FSI Copilot DLP - Financial Data" `
    -ContentContainsSensitiveInformation @{
        Name = "U.S. Social Security Number (SSN)"
        MinCount = 1
        MinConfidence = 85
    } `
    -BlockAccess $true `
    -NotifyUser "SiteAdmin","LastModifier" `
    -NotifyUserType "NotSet"

Write-Host "DLP policy created in test mode. Review matches before enabling enforcement."
```

### Script 2: DLP Policy Status and Match Report

```powershell
# Report on DLP policy matches for Copilot-related policies
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

Write-Host "=== Copilot DLP Policies ==="
$policyReport | Format-Table PolicyName, Mode, Enabled, RuleCount -AutoSize
$policyReport | Export-Csv "CopilotDLPPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: DLP Incident Report Export

```powershell
# Export DLP incident data for compliance review
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
$incidentReport | Export-Csv "DLPIncidents_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Policy Status Check | Daily | Verify DLP policies remain active |
| Incident Report | Weekly | Review DLP matches for false positives |
| Policy Configuration Export | Monthly | Document policy settings for audit trail |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate DLP effectiveness
- See [Troubleshooting](troubleshooting.md) for DLP policy issues
