# Control 4.8: Cost Allocation and License Optimization — PowerShell Setup

Automation scripts for Copilot license management, cost allocation, pay-as-you-go (PAYG) cost monitoring, budget cap configuration, and optimization reporting.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `Az.CostManagement`, `Az.Billing`
- **Permissions:** License Administrator, Reports.Read.All, User.Read.All, Azure Cost Management Contributor (for PAYG monitoring)
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
# Connect to Microsoft Graph for license and usage data
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "User.Read.All", "Reports.Read.All", "Organization.Read.All", "Directory.Read.All"

# Connect to Azure for PAYG cost monitoring (if PAYG billing is enabled)
Import-Module Az.CostManagement
Import-Module Az.Billing
Connect-AzAccount  # Authenticate with Billing Administrator or Cost Management Contributor role
```

## Scripts

### Script 1: PAYG Cost Monitoring — Monthly Billing Report

```powershell
# Monitor pay-as-you-go Copilot Chat costs from Azure Commerce billing
# Requires: Az.CostManagement module, Cost Management Reader or Contributor role on Azure subscription
# Note: Replace $SubscriptionId with your organization's Azure subscription ID

$SubscriptionId = "<your-subscription-id>"
$StartDate = (Get-Date -Day 1).ToString("yyyy-MM-dd")   # First day of current month
$EndDate = (Get-Date).ToString("yyyy-MM-dd")             # Today

# Retrieve PAYG Copilot Chat costs for the current billing month
$costData = Get-AzConsumptionUsageDetail `
    -SubscriptionId $SubscriptionId `
    -StartDate $StartDate `
    -EndDate $EndDate

# Filter for Copilot Chat metered billing
$copilotPaygCosts = $costData | Where-Object {
    $_.ServiceName -like "*Copilot*" -or $_.MeterName -like "*Copilot*"
}

if ($copilotPaygCosts.Count -gt 0) {
    $totalCost = ($copilotPaygCosts | Measure-Object -Property PretaxCost -Sum).Sum
    Write-Host "PAYG Copilot Chat Costs — Current Month ($StartDate to $EndDate):" -ForegroundColor Cyan
    Write-Host "Total PAYG cost: `$$([math]::Round($totalCost, 2)) USD"
    Write-Host "Estimated messages at `$0.01/message: $([math]::Round($totalCost / 0.01, 0))"

    # Group by department tag
    $bydept = $copilotPaygCosts | Group-Object { $_.Tags['Department'] } | ForEach-Object {
        [PSCustomObject]@{
            Department = if ($_.Name) { $_.Name } else { "Untagged" }
            Cost       = [math]::Round(($_.Group | Measure-Object PretaxCost -Sum).Sum, 2)
        }
    } | Sort-Object Cost -Descending

    Write-Host ""
    Write-Host "PAYG Cost by Department:" -ForegroundColor Yellow
    $bydept | Format-Table -AutoSize
    $bydept | Export-Csv "PAYGCopilotCost_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
} else {
    Write-Host "No PAYG Copilot Chat charges found for the current billing period." -ForegroundColor Green
    Write-Host "Either PAYG is not enabled, or no metered usage has occurred this month."
}
```

### Script 2: Configure PAYG Budget Cap via Azure Cost Management

```powershell
# Configure or verify PAYG budget caps for Copilot Chat spending
# Requires: Az.CostManagement module, Cost Management Contributor role
# Note: Replace scope and amounts per your organization's approved budget authority

param(
    [string]$SubscriptionId = "<your-subscription-id>",
    [string]$DepartmentName = "Finance",        # Department name for budget tracking
    [decimal]$MonthlyBudgetLimit = 500.00,      # Monthly budget cap in USD — adjust per approval
    [string]$AlertRecipient = "itfinance@contoso.com"
)

$budgetName = "CopilotPAYG-$DepartmentName"
$scope = "/subscriptions/$SubscriptionId"

# Create or update a budget with 80% and 100% alert thresholds
$budget = @{
    Name        = $budgetName
    Amount      = $MonthlyBudgetLimit
    TimeGrain   = "Monthly"
    TimePeriod  = @{
        StartDate = (Get-Date -Day 1).ToString("yyyy-MM-ddTHH:mm:ssZ")
        EndDate   = (Get-Date).AddYears(1).ToString("yyyy-MM-ddTHH:mm:ssZ")
    }
    Notifications = @{
        Alert80Pct = @{
            Enabled       = $true
            Operator      = "GreaterThan"
            Threshold     = 80
            ContactEmails = @($AlertRecipient)
            ThresholdType = "Actual"
        }
        Alert100Pct = @{
            Enabled       = $true
            Operator      = "GreaterThan"
            Threshold     = 100
            ContactEmails = @($AlertRecipient)
            ThresholdType = "Actual"
        }
    }
}

try {
    New-AzConsumptionBudget `
        -Name $budgetName `
        -Amount $MonthlyBudgetLimit `
        -Category Cost `
        -TimeGrain Monthly `
        -StartDate (Get-Date -Day 1) `
        -EndDate (Get-Date).AddYears(1) `
        -Scope $scope
    Write-Host "Budget '$budgetName' configured: `$$MonthlyBudgetLimit/month with 80%/100% alerts to $AlertRecipient" -ForegroundColor Green
} catch {
    Write-Warning "Budget configuration failed: $($_.Exception.Message)"
    Write-Host "Manual action: Configure budget cap in Azure Portal > Cost Management > Budgets"
}
```

### Script 3: PAYG Cost Anomaly Detection

```powershell
# Detect unusual PAYG Copilot Chat spending patterns
# Compares current month spending rate to previous month baseline
# Requires: Az.CostManagement module

$SubscriptionId = "<your-subscription-id>"

# Get current month and previous month costs
$currentStart = (Get-Date -Day 1).ToString("yyyy-MM-dd")
$currentEnd   = (Get-Date).ToString("yyyy-MM-dd")
$prevStart    = (Get-Date -Day 1).AddMonths(-1).ToString("yyyy-MM-dd")
$prevEnd      = (Get-Date -Day 1).AddDays(-1).ToString("yyyy-MM-dd")

$currentCosts = Get-AzConsumptionUsageDetail -SubscriptionId $SubscriptionId -StartDate $currentStart -EndDate $currentEnd |
    Where-Object { $_.ServiceName -like "*Copilot*" -or $_.MeterName -like "*Copilot*" }

$prevCosts = Get-AzConsumptionUsageDetail -SubscriptionId $SubscriptionId -StartDate $prevStart -EndDate $prevEnd |
    Where-Object { $_.ServiceName -like "*Copilot*" -or $_.MeterName -like "*Copilot*" }

$currentTotal = ($currentCosts | Measure-Object PretaxCost -Sum).Sum
$prevTotal    = ($prevCosts | Measure-Object PretaxCost -Sum).Sum

# Normalize current month to full-month run rate
$daysInMonth  = [int](Get-Date -Day 1).AddMonths(1).AddDays(-1).Day
$dayOfMonth   = (Get-Date).Day
$runRate      = if ($dayOfMonth -gt 0) { ($currentTotal / $dayOfMonth) * $daysInMonth } else { 0 }

Write-Host "PAYG Copilot Chat Anomaly Detection:" -ForegroundColor Cyan
Write-Host "  Previous month actual: `$$([math]::Round($prevTotal, 2))"
Write-Host "  Current month to-date: `$$([math]::Round($currentTotal, 2))"
Write-Host "  Current month run rate: `$$([math]::Round($runRate, 2))"

if ($prevTotal -gt 0) {
    $changePercent = [math]::Round((($runRate - $prevTotal) / $prevTotal) * 100, 1)
    Write-Host "  Month-over-month change (run rate): $changePercent%"

    if ($changePercent -gt 50) {
        Write-Warning "ANOMALY DETECTED: PAYG costs trending $changePercent% higher than last month. Investigate unusual usage."
    } elseif ($changePercent -gt 20) {
        Write-Host "  Warning: PAYG costs trending $changePercent% higher — review for expected growth vs. unexpected usage." -ForegroundColor Yellow
    } else {
        Write-Host "  Cost trend within normal range." -ForegroundColor Green
    }
} else {
    Write-Host "  No previous month baseline — first month of PAYG billing." -ForegroundColor Yellow
}
```

### Script 4: License Inventory and Cost Report

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

### Script 5: Department Chargeback Report

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

### Script 6: Underutilized License Detection

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

### Script 7: License Reallocation Script

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
| PAYG monthly billing report | Monthly | Script 1 |
| PAYG budget cap configuration | One-time setup, update quarterly | Script 2 |
| PAYG cost anomaly detection | Monthly | Script 3 |
| License inventory report | Monthly | Script 4 |
| Department chargeback (per-seat) | Monthly | Script 5 |
| Underutilization detection | Monthly | Script 6 |
| License reallocation | Quarterly (with approval) | Script 7 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate cost allocation
- See [Troubleshooting](troubleshooting.md) for licensing issues
