# Control 2.4: Information Barriers for Copilot (Chinese Wall) — PowerShell Setup

Automation scripts for managing Information Barriers that enforce Chinese Wall restrictions.

## Prerequisites

- Security & Compliance PowerShell (`ExchangeOnlineManagement`)
- Compliance Administrator role
- Microsoft 365 E5 or E5 Compliance license

## Scripts

### Script 1: Create Information Barrier Segments

```powershell
# Define Information Barrier segments based on organizational divisions
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

# Create segments for FSI Chinese Wall divisions
New-OrganizationSegment -Name "InvestmentBanking" -UserGroupFilter "Department -eq 'Investment Banking'"
New-OrganizationSegment -Name "Research" -UserGroupFilter "Department -eq 'Research'"
New-OrganizationSegment -Name "Trading" -UserGroupFilter "Department -eq 'Trading'"
New-OrganizationSegment -Name "RetailBanking" -UserGroupFilter "Department -eq 'Retail Banking'"
New-OrganizationSegment -Name "Compliance" -UserGroupFilter "Department -eq 'Compliance'"

Write-Host "Segments created. Verify with: Get-OrganizationSegment | Format-Table Name, UserGroupFilter"
Get-OrganizationSegment | Format-Table Name, UserGroupFilter -AutoSize
```

### Script 2: Create and Apply Barrier Policies

```powershell
# Create Information Barrier policies for Chinese Wall enforcement
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

# Block Investment Banking <-> Research
New-InformationBarrierPolicy -Name "IB-Research Block" `
    -AssignedSegment "InvestmentBanking" `
    -SegmentsBlocked "Research" `
    -State Active
# IMPORTANT: Create the reciprocal policy (Research blocked from InvestmentBanking) to ensure bidirectional enforcement

# Block Investment Banking <-> Trading
New-InformationBarrierPolicy -Name "IB-Trading Block" `
    -AssignedSegment "InvestmentBanking" `
    -SegmentsBlocked "Trading" `
    -State Active
# IMPORTANT: Create the reciprocal policy (Trading blocked from InvestmentBanking) to ensure bidirectional enforcement

# Block Research <-> Trading
New-InformationBarrierPolicy -Name "Research-Trading Block" `
    -AssignedSegment "Research" `
    -SegmentsBlocked "Trading" `
    -State Active
# IMPORTANT: Create the reciprocal policy (Trading blocked from Research) to ensure bidirectional enforcement

# Apply all policies
Start-InformationBarrierPoliciesApplication
Write-Host "Policies created and application started. Monitor status with: Get-InformationBarrierPoliciesApplicationStatus"
```

### Script 3: Barrier Status and Compliance Report

```powershell
# Report on Information Barrier policy status and compliance
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$policies = Get-InformationBarrierPolicy
$segments = Get-OrganizationSegment
$appStatus = Get-InformationBarrierPoliciesApplicationStatus

Write-Host "=== Information Barrier Status Report ==="
Write-Host "Segments defined: $($segments.Count)"
Write-Host "Policies defined: $($policies.Count)"
Write-Host "Latest application status: $($appStatus.Status)"
Write-Host "Application date: $($appStatus.LastModifiedDate)"

$policyReport = @()
foreach ($policy in $policies) {
    $policyReport += [PSCustomObject]@{
        Name             = $policy.Name
        AssignedSegment  = $policy.AssignedSegment
        SegmentsBlocked  = ($policy.SegmentsBlocked -join ", ")
        State            = $policy.State
    }
}

$policyReport | Format-Table Name, AssignedSegment, SegmentsBlocked, State -AutoSize
$policyReport | Export-Csv "IBPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Barrier Status Check | Daily | Verify policies are active and applied |
| Segment Membership Audit | Monthly | Verify user segment assignments are accurate |
| Policy Compliance Report | Quarterly | Document barrier compliance for regulators |

## Next Steps

- See [Verification & Testing](verification-testing.md) for barrier validation
- See [Troubleshooting](troubleshooting.md) for barrier issues
