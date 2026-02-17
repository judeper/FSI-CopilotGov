# Control 4.1: Copilot Admin Settings and Feature Management — PowerShell Setup

Automation scripts for managing Copilot administrative settings, feature controls, and license assignments.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** Global Administrator or Microsoft 365 Service Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Policy.ReadWrite.All", "User.ReadWrite.All", "Organization.ReadWrite.All"
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
# Track administrative changes to Copilot settings
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$configChanges = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "Set-CopilotPolicy", "Update-CopilotSettings" `
    -ResultSize 5000

Write-Host "Copilot Configuration Changes (Last 30 Days): $($configChanges.Count)"
$configChanges | Select-Object CreationDate, UserIds, Operations |
    Format-Table -AutoSize
$configChanges | Export-Csv "CopilotConfigChanges_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Feature Enablement Status Report

```powershell
# Report on Copilot feature enablement across the tenant
$features = @(
    @{Feature="Copilot in Word"; Setting="WordCopilotEnabled"},
    @{Feature="Copilot in Excel"; Setting="ExcelCopilotEnabled"},
    @{Feature="Copilot in PowerPoint"; Setting="PowerPointCopilotEnabled"},
    @{Feature="Copilot in Outlook"; Setting="OutlookCopilotEnabled"},
    @{Feature="Copilot in Teams"; Setting="TeamsCopilotEnabled"},
    @{Feature="Web Grounding"; Setting="WebGroundingEnabled"},
    @{Feature="Plugin Access"; Setting="PluginAccessEnabled"}
)

Write-Host "Copilot Feature Enablement Report:" -ForegroundColor Cyan
Write-Host "Note: Verify settings in M365 Admin Center > Settings > Copilot"
Write-Host "PowerShell cmdlets for Copilot policy management are being expanded by Microsoft."
$features | ForEach-Object {
    [PSCustomObject]@{
        Feature = $_.Feature
        Setting = $_.Setting
        Status  = "Verify in Admin Center"
    }
} | Format-Table -AutoSize
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| License assignment report | Monthly | Script 1 |
| Group-based license assignment | As needed | Script 2 |
| Configuration change audit | Weekly | Script 3 |
| Feature enablement review | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate Copilot settings
- See [Troubleshooting](troubleshooting.md) for configuration issues
