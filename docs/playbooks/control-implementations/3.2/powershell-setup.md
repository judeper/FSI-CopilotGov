# Control 3.2: Data Retention Policies for Copilot Interactions — PowerShell Setup

Automation scripts for deploying and managing data retention policies governing Copilot interaction data and generated content.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph.Compliance`
- **Permissions:** Purview Compliance Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Create Microsoft Copilot Experiences Retention Policy

```powershell
# Create retention policy targeting the Microsoft Copilot experiences location
# This is the primary retention target for M365 Copilot Chat history, meeting recaps,
# and Copilot interactions across Word/Excel/PowerPoint/Outlook/Teams
New-RetentionCompliancePolicy `
    -Name "FSI-Copilot-Experiences-Retention" `
    -Comment "Retains Microsoft Copilot experiences content per FSI regulatory requirements" `
    -CopilotLocation "All" `
    -Enabled $true

New-RetentionComplianceRule `
    -Name "FSI-Copilot-Experiences-3yr" `
    -Policy "FSI-Copilot-Experiences-Retention" `
    -RetentionDuration 1095 `
    -RetentionComplianceAction Keep `
    -RetentionDurationDisplayHint Years

Write-Host "Microsoft Copilot experiences retention policy created: 3-year retention" -ForegroundColor Green

# For regulated deployments requiring 6-year retention:
New-RetentionCompliancePolicy `
    -Name "FSI-Copilot-Experiences-Retention-6yr" `
    -Comment "6-year retention for Copilot experiences content per SEC Rule 17a-4(a)" `
    -CopilotLocation "All" `
    -Enabled $true

New-RetentionComplianceRule `
    -Name "FSI-Copilot-Experiences-6yr" `
    -Policy "FSI-Copilot-Experiences-Retention-6yr" `
    -RetentionDuration 2190 `
    -RetentionComplianceAction Keep `
    -RetentionDurationDisplayHint Years

Write-Host "6-year Copilot experiences retention policy created" -ForegroundColor Green
```

### Script 2: Create Content Retention Policies

```powershell
# Create retention policy for Copilot-generated content across workloads
New-RetentionCompliancePolicy `
    -Name "FSI-Copilot-Content-Retention" `
    -Comment "Retains Copilot-generated content in SPO, ODB, and EXO per SEC Rule 17a-4" `
    -SharePointLocation "All" `
    -ExchangeLocation "All" `
    -OneDriveLocation "All" `
    -Enabled $true

New-RetentionComplianceRule `
    -Name "FSI-Copilot-Content-6yr" `
    -Policy "FSI-Copilot-Content-Retention" `
    -RetentionDuration 2190 `
    -RetentionComplianceAction Keep `
    -RetentionDurationDisplayHint Years

Write-Host "Content retention policy created: 6-year retention" -ForegroundColor Green

# Create Teams retention policy to cover meeting recaps and chat summaries
New-RetentionCompliancePolicy `
    -Name "FSI-Copilot-Teams-Retention" `
    -Comment "Retains Teams messages including Copilot meeting recaps and summaries" `
    -TeamsChannelLocation "All" `
    -TeamsChatLocation "All" `
    -Enabled $true

New-RetentionComplianceRule `
    -Name "FSI-Copilot-Teams-3yr" `
    -Policy "FSI-Copilot-Teams-Retention" `
    -RetentionDuration 1095 `
    -RetentionComplianceAction Keep `
    -RetentionDurationDisplayHint Years

Write-Host "Teams retention policy created: 3-year retention" -ForegroundColor Green
```

### Script 3: Report on Existing Retention Policies

```powershell
# Generate a report of all retention policies relevant to Copilot
$policies = Get-RetentionCompliancePolicy | Where-Object {
    $_.Name -like "*Copilot*" -or $_.CopilotLocation -ne $null
}

foreach ($policy in $policies) {
    $rules = Get-RetentionComplianceRule -Policy $policy.Name
    [PSCustomObject]@{
        PolicyName        = $policy.Name
        Enabled           = $policy.Enabled
        DistributionStatus = $policy.DistributionStatus
        CopilotLocation   = $policy.CopilotLocation
        SharePointLocation = $policy.SharePointLocation
        ExchangeLocation  = $policy.ExchangeLocation
        TeamsLocation     = $policy.TeamsChannelLocation
        RetentionDays     = ($rules | Select-Object -First 1).RetentionDuration
        Action            = ($rules | Select-Object -First 1).RetentionComplianceAction
    }
} | Format-Table -AutoSize
```

### Script 4: Create Retention Label for Copilot Content

```powershell
# Create and publish a retention label for Copilot-generated regulatory records
New-ComplianceTag `
    -Name "FSI-Copilot-Regulatory-Record-6yr" `
    -Comment "Retention label for Copilot-generated regulatory records in FSI environment" `
    -RetentionAction Keep `
    -RetentionDuration 2190 `
    -RetentionType CreationAgeInDays `
    -IsRecordLabel $true

# Publish the label policy — include Microsoft Copilot experiences location
New-RetentionCompliancePolicy `
    -Name "Publish-Copilot-Retention-Labels" `
    -RetentionComplianceTag "FSI-Copilot-Regulatory-Record-6yr" `
    -SharePointLocation "All" `
    -ExchangeLocation "All" `
    -CopilotLocation "All" `
    -Enabled $true

Write-Host "Retention label created and published to Copilot experiences and other locations" -ForegroundColor Green
```

### Script 5: Verify Threaded Summary Retention Coverage

```powershell
# Check that both Teams and Copilot experiences locations are covered by retention
$teamsPolicies = Get-RetentionCompliancePolicy | Where-Object {
    $_.TeamsChannelLocation -ne $null -or $_.TeamsChatLocation -ne $null
}

$copilotExpPolicies = Get-RetentionCompliancePolicy | Where-Object {
    $_.CopilotLocation -ne $null
}

Write-Host "=== Threaded Summary Retention Coverage Check ===" -ForegroundColor Cyan
Write-Host "Teams retention policies (covers meeting content and embedded summaries): $($teamsPolicies.Count)" -ForegroundColor $(if ($teamsPolicies.Count -gt 0) { "Green" } else { "Red" })
Write-Host "Copilot experiences policies (covers Copilot-generated summaries): $($copilotExpPolicies.Count)" -ForegroundColor $(if ($copilotExpPolicies.Count -gt 0) { "Green" } else { "Red" })

if ($teamsPolicies.Count -eq 0) {
    Write-Warning "No Teams retention policy found — threaded summaries in Teams may not be retained"
}
if ($copilotExpPolicies.Count -eq 0) {
    Write-Warning "No Copilot experiences retention policy found — Copilot-generated summaries may not be retained"
}

# FINRA Rule 4511(c) requires preservation in format compliant with applicable regulations
# Both locations must be covered for complete threaded summary retention
```

### Script 6: Check Retention Policy Distribution Status

```powershell
# Verify all Copilot retention policies have distributed successfully
$allPolicies = Get-RetentionCompliancePolicy | Where-Object {
    $_.Name -like "*Copilot*"
}

$failedPolicies = $allPolicies | Where-Object { $_.DistributionStatus -ne "Success" }

if ($failedPolicies.Count -gt 0) {
    Write-Warning "The following retention policies have not distributed successfully:"
    $failedPolicies | Select-Object Name, DistributionStatus | Format-Table -AutoSize
} else {
    Write-Host "All Copilot retention policies distributed successfully" -ForegroundColor Green
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Retention policy audit | Monthly | Script 3 |
| Distribution status check | Weekly | Script 6 |
| Threaded summary coverage verification | Quarterly | Script 5 |
| Policy configuration review | Quarterly | Scripts 1-2 (verify) |
| Label application report | Monthly | Script 4 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate retention policies
- See [Troubleshooting](troubleshooting.md) for retention policy issues
- Back to [Control 3.2](../../../controls/pillar-3-compliance/3.2-data-retention-policies.md)
