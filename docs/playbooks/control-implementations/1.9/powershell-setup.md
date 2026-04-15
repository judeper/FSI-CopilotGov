# Control 1.9: License Planning and Assignment Strategy — PowerShell Setup

Automation scripts for managing Microsoft 365 Copilot license assignments and utilization tracking.

## Prerequisites

- Microsoft Graph PowerShell SDK (`Microsoft.Graph`)
- License Administrator or Entra Global Admin role
- Microsoft 365 Copilot SKU provisioned in tenant

## Scripts

### Script 1: License Inventory and Availability Report

```powershell
# Generate comprehensive license inventory report including Frontline SKUs
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Users
Import-Module Microsoft.Graph.Identity.DirectoryManagement
Connect-MgGraph -Scopes "Organization.Read.All","User.Read.All"

$subscribedSkus = Get-MgSubscribedSku
$licenseReport = @()

foreach ($sku in $subscribedSkus) {
    $licenseReport += [PSCustomObject]@{
        SkuPartNumber = $sku.SkuPartNumber
        SkuId         = $sku.SkuId
        Total         = $sku.PrepaidUnits.Enabled
        Assigned      = $sku.ConsumedUnits
        Available     = $sku.PrepaidUnits.Enabled - $sku.ConsumedUnits
    }
}

Write-Host "=== License Inventory ==="
# Include Frontline (F1/F3) SKUs alongside E3/E5 and Copilot SKUs
$licenseReport | Where-Object { $_.SkuPartNumber -match "Copilot|SPE_E5|SPE_E3|AAD_PREMIUM|FRONTLINE|M365_F1|M365_F3" } |
    Format-Table SkuPartNumber, Total, Assigned, Available -AutoSize

$licenseReport | Export-Csv "LicenseInventory_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Copilot License Assignment via Group

```powershell
# Assign Copilot licenses to a security group
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Groups
Import-Module Microsoft.Graph.Identity.DirectoryManagement
Connect-MgGraph -Scopes "Group.ReadWrite.All","Organization.Read.All"

$groupName = "Copilot-Pilot-Users"
$group = Get-MgGroup -Filter "displayName eq '$groupName'"

# Get the Copilot SKU ID
$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -match "Microsoft_365_Copilot" }

if ($copilotSku -and $group) {
    $licenseAssignment = @{
        AddLicenses = @(@{SkuId = $copilotSku.SkuId})
        RemoveLicenses = @()
    }
    Set-MgGroupLicense -GroupId $group.Id -BodyParameter $licenseAssignment
    Write-Host "Copilot license assigned to group: $groupName"
} else {
    Write-Host "Error: Copilot SKU or group not found." -ForegroundColor Red
}
```

### Script 3: License Utilization and Inactive User Report

```powershell
# Identify Copilot-licensed users who may be inactive
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Users
Import-Module Microsoft.Graph.Reports
Import-Module Microsoft.Graph.Identity.DirectoryManagement
Connect-MgGraph -Scopes "User.Read.All","AuditLog.Read.All"

$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -match "Microsoft_365_Copilot" }
$allUsers = Get-MgUser -All -Property "displayName,userPrincipalName,assignedLicenses,signInActivity"

$copilotUsers = $allUsers | Where-Object {
    $_.AssignedLicenses.SkuId -contains $copilotSku.SkuId
}

$utilizationReport = @()
foreach ($user in $copilotUsers) {
    $lastSignIn = $user.SignInActivity.LastSignInDateTime
    $daysSinceSignIn = if ($lastSignIn) { ((Get-Date) - $lastSignIn).Days } else { 999 }

    $utilizationReport += [PSCustomObject]@{
        DisplayName     = $user.DisplayName
        UPN             = $user.UserPrincipalName
        LastSignIn      = $lastSignIn
        DaysSinceSignIn = $daysSinceSignIn
        IsInactive      = ($daysSinceSignIn -gt 30)
    }
}

$inactive = ($utilizationReport | Where-Object IsInactive).Count
Write-Host "Copilot licensed users: $($utilizationReport.Count)"
Write-Host "Inactive (>30 days): $inactive"

$utilizationReport | Export-Csv "CopilotUtilization_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Frontline License Assignment Report

```powershell
# Identify Frontline (F1/F3) users and their Copilot add-on status
# Requires: Microsoft Graph SDK

Import-Module Microsoft.Graph.Users
Import-Module Microsoft.Graph.Identity.DirectoryManagement
Connect-MgGraph -Scopes "User.Read.All","Organization.Read.All"

$allSkus = Get-MgSubscribedSku
# Frontline base SKU patterns (F1: M365_F1, F3: M365_F3 or similar)
$frontlineSkuIds = ($allSkus | Where-Object { $_.SkuPartNumber -match "M365_F1|M365_F3|FRONTLINE" }).SkuId
$copilotSkuId    = ($allSkus | Where-Object { $_.SkuPartNumber -match "Microsoft_365_Copilot" }).SkuId

$allUsers = Get-MgUser -All -Property "displayName,userPrincipalName,assignedLicenses,department"

$frontlineReport = @()
foreach ($user in $allUsers) {
    $hasFrontline = ($user.AssignedLicenses.SkuId | Where-Object { $frontlineSkuIds -contains $_ }).Count -gt 0
    $hasCopilot   = $copilotSkuId -and ($user.AssignedLicenses.SkuId -contains $copilotSkuId)

    if ($hasFrontline) {
        $frontlineReport += [PSCustomObject]@{
            DisplayName     = $user.DisplayName
            UPN             = $user.UserPrincipalName
            Department      = $user.Department
            HasFrontlineSKU = $hasFrontline
            HasCopilotAddOn = $hasCopilot
        }
    }
}

Write-Host "=== Frontline Users Copilot Status ==="
Write-Host "Frontline users total: $($frontlineReport.Count)"
Write-Host "Frontline users with Copilot add-on: $(($frontlineReport | Where-Object HasCopilotAddOn).Count)"
$frontlineReport | Format-Table DisplayName, Department, HasFrontlineSKU, HasCopilotAddOn -AutoSize
$frontlineReport | Export-Csv "FrontlineCopilotStatus_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| License Inventory | Monthly | Track license consumption and availability (including Frontline SKUs) |
| Utilization Report | Monthly | Identify inactive users for license reclamation |
| Assignment Verification | After each deployment wave | Confirm successful license assignments |
| Frontline Copilot Report | Quarterly | Confirm Frontline add-on assignments are accurate and governance policies are applied |
| PAYG Usage Review | Monthly | Review Azure Cost Management for PAYG Copilot Chat spend against budget limits |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate license strategy
- See [Troubleshooting](troubleshooting.md) for license assignment issues
- Back to [Control 1.9](../../../controls/pillar-1-readiness/1.9-license-planning.md)
