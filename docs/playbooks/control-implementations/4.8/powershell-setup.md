# Control 4.8: Cost Allocation and License Optimization — PowerShell Setup

Automation scripts for Copilot license management, cost allocation, and optimization reporting.

## Prerequisites

- **Modules:** `Microsoft.Graph`
- **Permissions:** License Administrator, Reports.Read.All, User.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "User.Read.All", "Reports.Read.All", "Organization.Read.All", "Directory.Read.All"
```

## Scripts

### Script 1: License Inventory and Cost Report

```powershell
# Generate a Copilot license inventory with cost allocation
$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -like "*Copilot*" }
$monthlyPerUserCost = 30  # Adjust per your agreement

foreach ($sku in $copilotSku) {
    $report = [PSCustomObject]@{
        SKU            = $sku.SkuPartNumber
        TotalPurchased = $sku.PrepaidUnits.Enabled
        Assigned       = $sku.ConsumedUnits
        Available      = $sku.PrepaidUnits.Enabled - $sku.ConsumedUnits
        MonthlyCost    = "$" + ($sku.ConsumedUnits * $monthlyPerUserCost).ToString("N0")
        AnnualCost     = "$" + ($sku.ConsumedUnits * $monthlyPerUserCost * 12).ToString("N0")
        Utilization    = "$([math]::Round(($sku.ConsumedUnits / [Math]::Max($sku.PrepaidUnits.Enabled,1)) * 100, 1))%"
    }

    Write-Host "Copilot License Inventory:" -ForegroundColor Cyan
    $report | Format-List
}
```

### Script 2: Department Chargeback Report

```powershell
# Generate department-level cost allocation for Copilot licenses
$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -like "*Copilot*" }
$allUsers = Get-MgUser -All -Property UserPrincipalName, Department, AssignedLicenses

$copilotUsers = $allUsers | Where-Object {
    $_.AssignedLicenses.SkuId -contains $copilotSku[0].SkuId
}

$monthlyPerUserCost = 30
$chargeback = $copilotUsers | Group-Object Department | ForEach-Object {
    [PSCustomObject]@{
        Department   = if ($_.Name) { $_.Name } else { "Unassigned" }
        LicenseCount = $_.Count
        MonthlyCost  = "$" + ($_.Count * $monthlyPerUserCost).ToString("N0")
        AnnualCost   = "$" + ($_.Count * $monthlyPerUserCost * 12).ToString("N0")
    }
} | Sort-Object { [int]($_.MonthlyCost -replace '[$,]','') } -Descending

Write-Host "Department Chargeback Report:" -ForegroundColor Cyan
$chargeback | Format-Table -AutoSize
$chargeback | Export-Csv "CopilotChargeback_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Underutilized License Detection

```powershell
# Identify Copilot licenses with no recent usage for reallocation
Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/getMicrosoft365CopilotUsageUserDetail(period='D30')" `
    -OutputFilePath "CopilotUsage_Optimization.csv"

$usageData = Import-Csv "CopilotUsage_Optimization.csv"
$inactive = $usageData | Where-Object { $_.'Last Activity Date' -eq '' }

Write-Host "Underutilized Copilot Licenses (No activity in 30 days):" -ForegroundColor Yellow
Write-Host "Total inactive licensed users: $($inactive.Count)"
Write-Host "Potential monthly savings: $($inactive.Count * 30) USD"

$inactive | Select-Object 'User Principal Name', 'Display Name' |
    Export-Csv "InactiveCopilotUsers_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: License Reallocation Script

```powershell
# Remove Copilot licenses from inactive users (requires approval workflow)
$inactiveUsers = Import-Csv "InactiveCopilotUsers_$(Get-Date -Format 'yyyyMMdd').csv"
$copilotSku = Get-MgSubscribedSku | Where-Object { $_.SkuPartNumber -like "*Copilot*" }

Write-Warning "This script will remove Copilot licenses from $($inactiveUsers.Count) inactive users."
$confirm = Read-Host "Type 'CONFIRM' to proceed"

if ($confirm -eq "CONFIRM") {
    $removedCount = 0
    foreach ($user in $inactiveUsers) {
        $params = @{
            AddLicenses = @()
            RemoveLicenses = @($copilotSku[0].SkuId)
        }
        Set-MgUserLicense -UserId $user.'User Principal Name' -BodyParameter $params
        $removedCount++
    }
    Write-Host "Removed licenses from $removedCount inactive users" -ForegroundColor Green
} else {
    Write-Host "Operation cancelled" -ForegroundColor Yellow
}
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| License inventory report | Monthly | Script 1 |
| Department chargeback | Monthly | Script 2 |
| Underutilization detection | Monthly | Script 3 |
| License reallocation | Quarterly (with approval) | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate cost allocation
- See [Troubleshooting](troubleshooting.md) for licensing issues
