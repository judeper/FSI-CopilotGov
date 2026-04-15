# Control 4.5: Copilot Usage Analytics and Adoption Reporting — PowerShell Setup

Automation scripts for generating Copilot usage analytics and adoption reports.

## Prerequisites

- **Modules:** `Microsoft.Graph`
- **Permissions:** Reports.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Reports.Read.All"
```

## Scripts

### Script 1: Copilot Usage Summary Report

```powershell
# Generate Copilot usage summary from Microsoft Graph reports
$period = "D30"  # D7, D30, D90, D180

$usageReport = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/getMicrosoft365CopilotUsageUserDetail(period='$period')" `
    -OutputFilePath "CopilotUsageDetail_$(Get-Date -Format 'yyyyMMdd').csv"

Write-Host "Copilot usage detail report downloaded" -ForegroundColor Green

# Parse the CSV for summary statistics
$data = Import-Csv "CopilotUsageDetail_$(Get-Date -Format 'yyyyMMdd').csv"
$totalUsers = $data.Count
$activeUsers = ($data | Where-Object { $_.'Last Activity Date' -ne '' }).Count

Write-Host "`nCopilot Adoption Summary ($period):" -ForegroundColor Cyan
Write-Host "Total licensed users: $totalUsers"
Write-Host "Active users: $activeUsers"
Write-Host "Adoption rate: $([math]::Round(($activeUsers / [Math]::Max($totalUsers,1)) * 100, 1))%"
```

### Script 2: Usage by Application Report

```powershell
# Break down Copilot usage by application
$data = Import-Csv "CopilotUsageDetail_$(Get-Date -Format 'yyyyMMdd').csv"

$appUsage = @(
    [PSCustomObject]@{App="Word"; Users=($data | Where-Object { $_.'Word Copilot Last Activity Date' -ne '' }).Count},
    [PSCustomObject]@{App="Excel"; Users=($data | Where-Object { $_.'Excel Copilot Last Activity Date' -ne '' }).Count},
    [PSCustomObject]@{App="PowerPoint"; Users=($data | Where-Object { $_.'PowerPoint Copilot Last Activity Date' -ne '' }).Count},
    [PSCustomObject]@{App="Outlook"; Users=($data | Where-Object { $_.'Outlook Copilot Last Activity Date' -ne '' }).Count},
    [PSCustomObject]@{App="Teams"; Users=($data | Where-Object { $_.'Teams Copilot Last Activity Date' -ne '' }).Count}
)

Write-Host "Copilot Usage by Application:" -ForegroundColor Cyan
$appUsage | Sort-Object Users -Descending | Format-Table -AutoSize
$appUsage | Export-Csv "CopilotUsageByApp_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Department-Level Adoption Report

```powershell
# Generate department-level Copilot adoption metrics
$data = Import-Csv "CopilotUsageDetail_$(Get-Date -Format 'yyyyMMdd').csv"

# Enrich with department data from Entra ID
$enriched = $data | ForEach-Object {
    $user = Get-MgUser -UserId $_.'User Principal Name' -Property Department -ErrorAction SilentlyContinue
    [PSCustomObject]@{
        User       = $_.'User Principal Name'
        Department = $user.Department
        Active     = $_.'Last Activity Date' -ne ''
    }
}

$deptAdoption = $enriched | Group-Object Department | ForEach-Object {
    $total = $_.Count
    $active = ($_.Group | Where-Object { $_.Active }).Count
    [PSCustomObject]@{
        Department    = $_.Name
        Licensed      = $total
        Active        = $active
        AdoptionRate  = "$([math]::Round(($active / [Math]::Max($total,1)) * 100, 1))%"
    }
} | Sort-Object { [int]($_.AdoptionRate -replace '%','') } -Descending

Write-Host "Department Adoption Report:" -ForegroundColor Cyan
$deptAdoption | Format-Table -AutoSize
$deptAdoption | Export-Csv "CopilotAdoptionByDept_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Adoption Trend Analysis

```powershell
# Compare adoption across multiple time periods
$periods = @("D7", "D30", "D90")
$trends = @()

foreach ($period in $periods) {
    $report = Invoke-MgGraphRequest -Method GET `
        -Uri "https://graph.microsoft.com/v1.0/reports/getMicrosoft365CopilotUsageUserDetail(period='$period')" `
        -OutputFilePath "temp_$period.csv"

    $data = Import-Csv "temp_$period.csv"
    $total = $data.Count
    $active = ($data | Where-Object { $_.'Last Activity Date' -ne '' }).Count

    $trends += [PSCustomObject]@{
        Period       = $period
        Licensed     = $total
        Active       = $active
        AdoptionRate = "$([math]::Round(($active / [Math]::Max($total,1)) * 100, 1))%"
    }
}

Write-Host "Adoption Trend Analysis:" -ForegroundColor Cyan
$trends | Format-Table -AutoSize
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Usage summary report | Weekly | Script 1 |
| Application usage breakdown | Monthly | Script 2 |
| Department adoption report | Monthly | Script 3 |
| Trend analysis | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate analytics
- See [Troubleshooting](troubleshooting.md) for reporting issues
- Back to [Control 4.5](../../../controls/pillar-4-operations/4.5-usage-analytics.md)
