# Control 3.2: Data Retention Policies for Copilot Interactions — PowerShell Setup

Automation scripts for deploying and managing data retention policies governing Copilot interaction data and generated content.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph.Compliance`
- **Permissions:** Compliance Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Create Copilot Interaction Retention Policy

```powershell
# Create retention policy for Copilot interactions — 7-year retention for FSI
New-RetentionCompliancePolicy `
    -Name "FSI-Copilot-Interaction-Retention" `
    -Comment "Retains Copilot interaction data per FSI regulatory requirements" `
    -CopilotInteractionLocation "All" `
    -Enabled $true

New-RetentionComplianceRule `
    -Name "FSI-Copilot-Interaction-7yr" `
    -Policy "FSI-Copilot-Interaction-Retention" `
    -RetentionDuration 2555 `
    -RetentionComplianceAction KeepAndDelete `
    -RetentionDurationDisplayHint Years

Write-Host "Copilot interaction retention policy created: 7-year retention" -ForegroundColor Green
```

### Script 2: Create Content Retention Policies

```powershell
# Create retention policy for Copilot-generated content across workloads
New-RetentionCompliancePolicy `
    -Name "FSI-Copilot-Content-Retention" `
    -Comment "Retains Copilot-generated content in SPO, ODB, and EXO" `
    -SharePointLocation "All" `
    -ExchangeLocation "All" `
    -OneDriveLocation "All" `
    -Enabled $true

New-RetentionComplianceRule `
    -Name "FSI-Copilot-Content-7yr" `
    -Policy "FSI-Copilot-Content-Retention" `
    -RetentionDuration 2555 `
    -RetentionComplianceAction KeepAndDelete `
    -RetentionDurationDisplayHint Years

Write-Host "Content retention policy created: 7-year retention" -ForegroundColor Green
```

### Script 3: Report on Existing Retention Policies

```powershell
# Generate a report of all retention policies relevant to Copilot
$policies = Get-RetentionCompliancePolicy | Where-Object {
    $_.Name -like "*Copilot*" -or $_.CopilotInteractionLocation -ne $null
}

foreach ($policy in $policies) {
    $rules = Get-RetentionComplianceRule -Policy $policy.Name
    [PSCustomObject]@{
        PolicyName     = $policy.Name
        Enabled        = $policy.Enabled
        Locations      = ($policy.SharePointLocation + $policy.ExchangeLocation + $policy.CopilotInteractionLocation) -join ", "
        RetentionDays  = $rules.RetentionDuration
        Action         = $rules.RetentionComplianceAction
    }
} | Format-Table -AutoSize
```

### Script 4: Create Retention Label for Copilot Content

```powershell
# Create and publish a retention label for Copilot-generated content
New-ComplianceTag `
    -Name "Copilot-Generated-7yr-Retain" `
    -Comment "Retention label for Copilot-generated content in FSI environment" `
    -RetentionAction KeepAndDelete `
    -RetentionDuration 2555 `
    -RetentionType CreationAgeInDays `
    -IsRecordLabel $true

# Publish the label policy
New-RetentionCompliancePolicy `
    -Name "Publish-Copilot-Retention-Labels" `
    -RetentionComplianceTag "Copilot-Generated-7yr-Retain" `
    -SharePointLocation "All" `
    -ExchangeLocation "All" `
    -Enabled $true

Write-Host "Retention label created and published" -ForegroundColor Green
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Retention policy audit | Monthly | Script 3 |
| Policy configuration review | Quarterly | Scripts 1-2 (verify) |
| Label application report | Monthly | Script 4 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate retention policies
- See [Troubleshooting](troubleshooting.md) for retention policy issues
