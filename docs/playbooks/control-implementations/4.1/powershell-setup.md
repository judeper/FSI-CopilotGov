# Control 4.1: Copilot Admin Settings and Feature Management — PowerShell Setup

Automation scripts for managing Copilot Control System administrative settings, feature controls, and license assignments.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** Global Administrator, Copilot Administrator, or Microsoft 365 Service Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Policy.ReadWrite.All", "User.ReadWrite.All", "Organization.ReadWrite.All"

Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Report on Current Copilot License Assignments

```powershell
# Report on Copilot license assignments across the organization
$copilotSkuName = "Microsoft_365_Copilot"
$allUsers = Get-MgUser -All -Property UserPrincipalName, DisplayName, AssignedLicenses, Department

$copilotUsers = $allUsers | Where-Object {
    $_.AssignedLicenses.SkuId -contains (Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -eq $copilotSkuName }).SkuId
}

Write-Host "Copilot License Assignment Report:" -ForegroundColor Cyan
Write-Host "Total Copilot licenses assigned: $($copilotUsers.Count)"

$byDepartment = $copilotUsers | Group-Object { $_.Department } |
    Select-Object @{N='Department'; E={$_.Name}}, @{N='LicenseCount'; E={$_.Count}} |
    Sort-Object LicenseCount -Descending

$byDepartment | Format-Table -AutoSize
$copilotUsers | Select-Object UserPrincipalName, DisplayName, Department |
    Export-Csv "CopilotLicenses_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Assign Copilot Licenses to Approved Group

```powershell
# Assign Copilot licenses to members of the approved deployment group
$groupId = "approved-copilot-group-id"
$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -eq "Microsoft_365_Copilot" }

$groupMembers = Get-MgGroupMember -GroupId $groupId -All
$assignedCount = 0

foreach ($member in $groupMembers) {
    $user = Get-MgUser -UserId $member.Id -Property AssignedLicenses
    $hasLicense = $user.AssignedLicenses.SkuId -contains $copilotSku.SkuId

    if (-not $hasLicense) {
        $params = @{
            AddLicenses = @(@{ SkuId = $copilotSku.SkuId })
            RemoveLicenses = @()
        }
        Set-MgUserLicense -UserId $member.Id -BodyParameter $params
        $assignedCount++
    }
}

Write-Host "Copilot licenses assigned to $assignedCount new users" -ForegroundColor Green
```

### Script 3: Audit Copilot Configuration Changes

```powershell
# Track administrative changes to Copilot Control System settings
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$configChanges = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "Set-CopilotPolicy", "Update-CopilotSettings" `
    -ResultSize 5000

Write-Host "Copilot Control System Configuration Changes (Last 30 Days): $($configChanges.Count)"
$configChanges | Select-Object CreationDate, UserIds, Operations |
    Format-Table -AutoSize
$configChanges | Export-Csv "CopilotConfigChanges_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Feature Enablement Status Report

```powershell
# Report on Copilot Control System feature enablement across the tenant
$features = @(
    @{Feature="Copilot in Word"; Setting="WordCopilotEnabled"},
    @{Feature="Copilot in Excel"; Setting="ExcelCopilotEnabled"},
    @{Feature="Copilot in PowerPoint"; Setting="PowerPointCopilotEnabled"},
    @{Feature="Copilot in Outlook"; Setting="OutlookCopilotEnabled"},
    @{Feature="Copilot in Teams"; Setting="TeamsCopilotEnabled"},
    @{Feature="Web Grounding"; Setting="WebGroundingEnabled"},
    @{Feature="Plugin Access"; Setting="PluginAccessEnabled"}
)

Write-Host "Copilot Control System Feature Enablement Report:" -ForegroundColor Cyan
Write-Host "Note: Verify settings in M365 Admin Center > Copilot > Settings"
Write-Host "PowerShell cmdlets for Copilot policy management continue to expand."
$features | ForEach-Object {
    [PSCustomObject]@{
        Feature = $_.Feature
        Setting = $_.Setting
        Status  = "Verify in Admin Center > Copilot"
    }
} | Format-Table -AutoSize
```

### Script 5: Verify Baseline Security Mode Status

```powershell
# Report on Copilot Control System security configuration baseline
# Baseline Security Mode settings are managed via the Admin Center; this script
# validates the security posture by querying related DLP and CA policies.

# Check if Conditional Access policies covering Copilot-licensed users are enabled
$caPolicies = Get-MgIdentityConditionalAccessPolicy -All | Where-Object {
    $_.State -eq "enabled" -and $_.DisplayName -like "*Copilot*"
}

Write-Host "Active Conditional Access Policies covering Copilot:" -ForegroundColor Cyan
if ($caPolicies.Count -eq 0) {
    Write-Host "WARNING: No Copilot-specific CA policies found. Verify Baseline Security Mode is enabled." -ForegroundColor Yellow
} else {
    $caPolicies | Select-Object DisplayName, State | Format-Table -AutoSize
}

# Report Copilot admin role assignments
$copilotAdminRole = Get-MgDirectoryRole | Where-Object { $_.DisplayName -eq "Copilot Administrator" }
if ($copilotAdminRole) {
    $copilotAdmins = Get-MgDirectoryRoleMember -DirectoryRoleId $copilotAdminRole.Id
    Write-Host "`nCopilot Administrator role assignments: $($copilotAdmins.Count)" -ForegroundColor Cyan
    $copilotAdmins | ForEach-Object {
        $user = Get-MgUser -UserId $_.Id -Property DisplayName, UserPrincipalName -ErrorAction SilentlyContinue
        if ($user) { Write-Host "  - $($user.DisplayName) ($($user.UserPrincipalName))" }
    }
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| License assignment report | Monthly | Script 1 |
| Group-based license assignment | As needed | Script 2 |
| Configuration change audit | Weekly | Script 3 |
| Feature enablement review | Monthly | Script 4 |
| Security baseline verification | Monthly | Script 5 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate Copilot Control System settings
- See [Troubleshooting](troubleshooting.md) for configuration issues
