# Control 2.3: Conditional Access Policies for Copilot Workloads — PowerShell Setup

Automation scripts for managing Conditional Access policies governing Copilot access.

## Prerequisites

- Microsoft Graph PowerShell SDK (`Microsoft.Graph`)
- Conditional Access Administrator role
- Entra ID P1 or P2 license

## Scripts

### Script 1: Audit Copilot App ID in CA Policies

```powershell
# Verify the correct Enterprise Copilot Platform app ID in CA policies
# Correct ID: fb8d773d-7ef8-4ec0-a117-179f88add510
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Identity.SignIns
Connect-MgGraph -Scopes "Policy.Read.All"

$correctAppId = "fb8d773d-7ef8-4ec0-a117-179f88add510"
$policies = Get-MgIdentityConditionalAccessPolicy -All

Write-Host "=== CA Policies Referencing Copilot App ==="
foreach ($policy in $policies) {
    $includeApps = $policy.Conditions.Applications.IncludeApplications
    $excludeApps = $policy.Conditions.Applications.ExcludeApplications

    if ($includeApps -contains $correctAppId) {
        Write-Host "[INCLUDE] $($policy.DisplayName) — State: $($policy.State)"
    }
    if ($excludeApps -contains $correctAppId) {
        Write-Host "[EXCLUDE] $($policy.DisplayName) — State: $($policy.State)"
        Write-Host "  WARNING: Copilot is EXCLUDED from this policy — review before March 2026 enforcement"
    }
}

# Report policies with "All resources" + exclusions (March 2026 enforcement impact)
Write-Host "`n=== Policies with 'All Resources' + Exclusions (March 2026 Impact) ==="
foreach ($policy in $policies) {
    $includesAll = $policy.Conditions.Applications.IncludeApplications -contains "All"
    $hasExclusions = $policy.Conditions.Applications.ExcludeApplications.Count -gt 0
    if ($includesAll -and $hasExclusions) {
        Write-Host "REVIEW: $($policy.DisplayName)"
        Write-Host "  Excluded apps: $($policy.Conditions.Applications.ExcludeApplications -join ', ')"
    }
}
```

### Script 2: Export Conditional Access Policies

```powershell
# Export all Conditional Access policies for audit documentation
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Identity.SignIns
Connect-MgGraph -Scopes "Policy.Read.All"

$policies = Get-MgIdentityConditionalAccessPolicy -All

$policyReport = @()
foreach ($policy in $policies) {
    $policyReport += [PSCustomObject]@{
        Name           = $policy.DisplayName
        State          = $policy.State
        CreatedDate    = $policy.CreatedDateTime
        ModifiedDate   = $policy.ModifiedDateTime
        GrantControls  = ($policy.GrantControls.BuiltInControls -join ", ")
        SessionControls = if ($policy.SessionControls) { "Configured" } else { "None" }
        IncludeUsers   = ($policy.Conditions.Users.IncludeUsers -join ", ")
        IncludeApps    = ($policy.Conditions.Applications.IncludeApplications -join ", ")
        ExcludeApps    = ($policy.Conditions.Applications.ExcludeApplications -join ", ")
    }
}

Write-Host "=== Conditional Access Policies ==="
$policyReport | Format-Table Name, State, GrantControls -AutoSize
$policyReport | Export-Csv "ConditionalAccessPolicies_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Copilot Sign-In Analysis

```powershell
# Analyze sign-in logs for Copilot-related access patterns
# Requires: Microsoft Graph SDK with AuditLog.Read.All

Import-Module Microsoft.Graph.Reports
Connect-MgGraph -Scopes "AuditLog.Read.All"

$signIns = Get-MgAuditLogSignIn -Filter "appDisplayName eq 'Microsoft 365 Copilot'" `
    -Top 500 -OrderBy "createdDateTime desc"

$accessReport = @()
foreach ($signIn in $signIns) {
    $accessReport += [PSCustomObject]@{
        Date            = $signIn.CreatedDateTime
        User            = $signIn.UserPrincipalName
        Status          = $signIn.Status.ErrorCode
        DeviceCompliant = $signIn.DeviceDetail.IsCompliant
        DeviceManaged   = $signIn.DeviceDetail.IsManaged
        Location        = $signIn.Location.City
        MFASatisfied    = ($signIn.AuthenticationMethodsUsed.Count -gt 1)
        CAPolicy        = ($signIn.AppliedConditionalAccessPolicies | Select-Object -First 1).DisplayName
    }
}

Write-Host "Copilot sign-ins analyzed: $($accessReport.Count)"
$nonCompliant = ($accessReport | Where-Object { -not $_.DeviceCompliant }).Count
Write-Host "Non-compliant device sign-ins: $nonCompliant"

$accessReport | Export-Csv "CopilotSignIns_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Named Locations Configuration Audit

```powershell
# Audit named locations used in Conditional Access policies
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Identity.SignIns
Connect-MgGraph -Scopes "Policy.Read.All"

$locations = Get-MgIdentityConditionalAccessNamedLocation

$locationReport = @()
foreach ($loc in $locations) {
    $locationReport += [PSCustomObject]@{
        Name           = $loc.DisplayName
        Type           = $loc.AdditionalProperties["@odata.type"]
        IsTrusted      = $loc.AdditionalProperties["isTrusted"]
        CreatedDate    = $loc.CreatedDateTime
        ModifiedDate   = $loc.ModifiedDateTime
    }
}

$locationReport | Format-Table Name, Type, IsTrusted -AutoSize
$locationReport | Export-Csv "NamedLocations_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Copilot App ID Audit | Quarterly | Verify correct app ID in all CA policies; check for Copilot exclusions |
| Policy Export | Monthly | Document policy configurations for audit |
| Sign-In Analysis | Weekly | Monitor Copilot access patterns and compliance |
| Named Locations Audit | Quarterly | Verify location definitions are current |

## Next Steps

- See [Verification & Testing](verification-testing.md) for access control validation
- See [Troubleshooting](troubleshooting.md) for Conditional Access issues
