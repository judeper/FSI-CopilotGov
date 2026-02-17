# Control 2.7: Data Residency and Cross-Border Data Flow — PowerShell Setup

Automation scripts for verifying and monitoring data residency configurations.

## Prerequisites

- Microsoft Graph PowerShell SDK
- Global Reader or Global Administrator role

## Scripts

### Script 1: Tenant Data Location Report

```powershell
# Report tenant data locations for all workloads
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Identity.DirectoryManagement
Connect-MgGraph -Scopes "Organization.Read.All"

$org = Get-MgOrganization
Write-Host "=== Tenant Data Location Report ==="
Write-Host "Tenant: $($org.DisplayName)"
Write-Host "Country: $($org.CountryLetterCode)"
Write-Host "Preferred Data Location: $($org.PreferredDataLocation)"
Write-Host "Tenant Type: $($org.TenantType)"
Write-Host ""

# Check for Multi-Geo configuration
$dataLocations = $org.AssignedPlans | Where-Object {
    $_.Service -match "SharePoint|Exchange|Teams"
}

Write-Host "Data residency assessment generated. Verify specific workload locations in Admin Center."

$report = [PSCustomObject]@{
    TenantName     = $org.DisplayName
    Country        = $org.CountryLetterCode
    DataLocation   = $org.PreferredDataLocation
    AssessmentDate = Get-Date -Format "yyyy-MM-dd"
}

$report | ConvertTo-Json | Out-File "DataResidency_$(Get-Date -Format 'yyyyMMdd').json"
```

### Script 2: Multi-Geo User Location Audit

```powershell
# Audit user preferred data locations for Multi-Geo configurations
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Users
Connect-MgGraph -Scopes "User.Read.All"

$users = Get-MgUser -All -Property "displayName,userPrincipalName,preferredDataLocation,usageLocation"

$geoReport = $users | Group-Object PreferredDataLocation | ForEach-Object {
    [PSCustomObject]@{
        DataLocation = if ($_.Name) { $_.Name } else { "Default (not set)" }
        UserCount    = $_.Count
    }
} | Sort-Object UserCount -Descending

Write-Host "=== User Data Location Distribution ==="
$geoReport | Format-Table DataLocation, UserCount -AutoSize

$users | Select-Object DisplayName, UserPrincipalName, PreferredDataLocation, UsageLocation |
    Export-Csv "UserDataLocations_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Cross-Border Access Pattern Detection

```powershell
# Detect sign-ins from locations different from data residency
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Reports
Connect-MgGraph -Scopes "AuditLog.Read.All"

$signIns = Get-MgAuditLogSignIn -Top 1000 -OrderBy "createdDateTime desc" |
    Where-Object { $_.AppDisplayName -match "Copilot|Office|SharePoint|Teams" }

$crossBorder = @()
foreach ($signIn in $signIns) {
    $signInCountry = $signIn.Location.CountryOrRegion
    if ($signInCountry -and $signInCountry -ne "US") {  # Adjust base country as needed
        $crossBorder += [PSCustomObject]@{
            Date      = $signIn.CreatedDateTime
            User      = $signIn.UserPrincipalName
            App       = $signIn.AppDisplayName
            Country   = $signInCountry
            City      = $signIn.Location.City
            Status    = $signIn.Status.ErrorCode
        }
    }
}

Write-Host "Cross-border access events: $($crossBorder.Count)"
$crossBorder | Export-Csv "CrossBorderAccess_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| Data Location Report | Quarterly | Document data residency for compliance |
| User Geo Audit | Monthly | Verify user data location assignments |
| Cross-Border Detection | Weekly | Monitor for cross-border access patterns |

## Next Steps

- See [Verification & Testing](verification-testing.md) for residency validation
- See [Troubleshooting](troubleshooting.md) for residency issues
