# Control 1.5: Sensitivity Label Taxonomy Review — PowerShell Setup

Automation scripts for auditing and managing the sensitivity label taxonomy.

## Prerequisites

- Security & Compliance PowerShell module (`ExchangeOnlineManagement`)
- Information Protection Administrator or Purview Compliance Admin role
- Microsoft 365 E5 or E5 Compliance license

## Scripts

### Script 1: Export Complete Label Taxonomy

```powershell
# Export all sensitivity labels and their configurations for review
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$labels = Get-Label | Sort-Object Priority
$taxonomy = @()

foreach ($label in $labels) {
    $taxonomy += [PSCustomObject]@{
        DisplayName    = $label.DisplayName
        Name           = $label.Name
        Priority       = $label.Priority
        ParentLabel    = $label.ParentId
        Enabled        = $label.Enabled
        ContentType    = ($label.ContentType -join ", ")
        EncryptionEnabled = $label.EncryptionEnabled
        Tooltip        = $label.Tooltip
        Description    = $label.Comment
    }
}

$taxonomy | Format-Table DisplayName, Priority, Enabled, EncryptionEnabled -AutoSize
$taxonomy | Export-Csv "LabelTaxonomy_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Exported $($taxonomy.Count) labels to taxonomy report."
```

### Script 2: Label Policy Coverage Analysis

```powershell
# Analyze label policy coverage across user groups
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$policies = Get-LabelPolicy
$policyReport = @()

foreach ($policy in $policies) {
    $policyReport += [PSCustomObject]@{
        PolicyName    = $policy.Name
        Enabled       = $policy.Enabled
        Mode          = $policy.Mode
        Labels        = ($policy.Labels -join "; ")
        ExchangeLocation = ($policy.ExchangeLocation -join "; ")
        DefaultLabel  = $policy.DefaultLabelId
        MandatoryLabeling = $policy.MandatoryLabelingEnabled
    }
}

$policyReport | Format-Table PolicyName, Enabled, MandatoryLabeling -AutoSize
$policyReport | Export-Csv "LabelPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Exported $($policyReport.Count) label policies."
```

### Script 3: Auto-Labeling Policy Status Report

```powershell
# Report on auto-labeling policy status and simulation results
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$autoLabelPolicies = Get-AutoSensitivityLabelPolicy
$autoReport = @()

foreach ($policy in $autoLabelPolicies) {
    $rules = Get-AutoSensitivityLabelRule -Policy $policy.Name
    $autoReport += [PSCustomObject]@{
        PolicyName    = $policy.Name
        Enabled       = $policy.Enabled
        Mode          = $policy.Mode
        ApplyLabel    = $policy.ApplySensitivityLabel
        RuleCount     = $rules.Count
        Workloads     = ($policy.ExchangeLocation + $policy.SharePointLocation + $policy.OneDriveLocation) -join "; "
        SimulationMode = ($policy.Mode -eq "TestWithNotifications" -or $policy.Mode -eq "TestWithoutNotifications")
    }
}

Write-Host "=== Auto-Labeling Policy Status ==="
$autoReport | Format-Table PolicyName, Mode, SimulationMode, Enabled -AutoSize
$autoReport | Export-Csv "AutoLabelPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Label Adoption Metrics

```powershell
# View label adoption metrics for governance review
# Sensitivity label analytics are available in the Purview portal:
#   Microsoft Purview > Information Protection > Label Analytics
#
# The Graph API does not currently provide a PowerShell cmdlet for
# sensitivity label usage reporting. Use the Purview portal for:
#   - Label adoption rates across workloads
#   - Label coverage percentages by department
#   - Trends in auto-labeling vs. manual labeling

Write-Host "=== Label Adoption Metrics ==="
Write-Host "For label adoption analytics, use the Purview portal:"
Write-Host "  Microsoft Purview > Information Protection > Label Analytics"
Write-Host ""
Write-Host "Export label analytics reports from the portal for governance documentation."
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Taxonomy Export | Monthly | Track taxonomy changes and maintain audit trail |
| Policy Coverage Analysis | Quarterly | Verify all user groups have label access |
| Auto-Labeling Status Check | Weekly | Monitor auto-labeling policy health and mode |
| Adoption Metrics | Monthly | Track progress toward governance-level labeling targets (>50% Baseline, >75% Recommended, >90% Regulated) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate taxonomy configuration
- See [Troubleshooting](troubleshooting.md) for label management issues
- Back to [Control 1.5: Sensitivity Label Taxonomy Review](../../../controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md)
