# Control 4.6: Viva Insights — Copilot Impact Measurement — PowerShell Setup

Automation scripts for extracting and reporting on Copilot impact data from Viva Insights.

## Prerequisites

- **Modules:** `Microsoft.Graph`
- **Permissions:** Viva Insights Administrator, Reports.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Reports.Read.All", "User.Read.All"
```

## Scripts

### Script 1: Extract Copilot Usage Metrics for Impact Analysis

```powershell
# Extract Copilot usage data alongside collaboration metrics
$period = "D30"

# Get Copilot usage data
Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/getMicrosoft365CopilotUsageUserDetail(period='$period')" `
    -OutputFilePath "CopilotUsage_Impact_$(Get-Date -Format 'yyyyMMdd').csv"

# Get email activity for comparison
Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/getEmailActivityUserDetail(period='$period')" `
    -OutputFilePath "EmailActivity_$(Get-Date -Format 'yyyyMMdd').csv"

# Get Teams activity for comparison
Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/reports/getTeamsUserActivityUserDetail(period='$period')" `
    -OutputFilePath "TeamsActivity_$(Get-Date -Format 'yyyyMMdd').csv"

Write-Host "Impact analysis data extracted" -ForegroundColor Green
```

### Script 2: Copilot vs Non-Copilot User Comparison

```powershell
# Compare productivity metrics between Copilot and non-Copilot users
$copilotData = Import-Csv "CopilotUsage_Impact_$(Get-Date -Format 'yyyyMMdd').csv"
$emailData = Import-Csv "EmailActivity_$(Get-Date -Format 'yyyyMMdd').csv"

$copilotActiveUsers = ($copilotData | Where-Object { $_.'Last Activity Date' -ne '' }).'User Principal Name'

$copilotEmailStats = $emailData | Where-Object { $_.'User Principal Name' -in $copilotActiveUsers }
$nonCopilotEmailStats = $emailData | Where-Object { $_.'User Principal Name' -notin $copilotActiveUsers }

$comparison = [PSCustomObject]@{
    Metric               = "Avg Emails Sent"
    CopilotUsers         = [math]::Round(($copilotEmailStats | Measure-Object 'Send Count' -Average).Average, 1)
    NonCopilotUsers      = [math]::Round(($nonCopilotEmailStats | Measure-Object 'Send Count' -Average).Average, 1)
}

Write-Host "Copilot vs Non-Copilot User Comparison:" -ForegroundColor Cyan
$comparison | Format-Table -AutoSize
```

### Script 3: Copilot ROI Estimation Report

```powershell
# Estimate Copilot ROI based on usage data and assumed productivity gains
$copilotData = Import-Csv "CopilotUsage_Impact_$(Get-Date -Format 'yyyyMMdd').csv"
$activeUsers = ($copilotData | Where-Object { $_.'Last Activity Date' -ne '' }).Count
$totalLicensed = $copilotData.Count

# Assumptions (adjust per organization's analysis)
$monthlyLicenseCost = 30  # per user
$estimatedMinutesSavedPerWeek = 60  # per active user (conservative estimate)
$hourlyLaborCost = 75  # average fully-loaded cost

$monthlyLicenseSpend = $totalLicensed * $monthlyLicenseCost
$monthlyTimeSavings = $activeUsers * $estimatedMinutesSavedPerWeek * 4.33 / 60  # hours per month
$monthlyProductivityValue = $monthlyTimeSavings * $hourlyLaborCost

$roi = [PSCustomObject]@{
    ActiveUsers             = $activeUsers
    TotalLicensed           = $totalLicensed
    MonthlyLicenseCost      = "$" + $monthlyLicenseSpend.ToString("N0")
    EstimatedHoursSaved     = [math]::Round($monthlyTimeSavings, 0)
    EstimatedProductivityValue = "$" + $monthlyProductivityValue.ToString("N0")
    EstimatedROI            = "$" + ($monthlyProductivityValue - $monthlyLicenseSpend).ToString("N0")
}

Write-Host "Copilot ROI Estimation:" -ForegroundColor Cyan
$roi | Format-List
$roi | Export-Csv "CopilotROI_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Viva Insights Privacy Configuration Audit

```powershell
# Audit Viva Insights privacy and access settings
Write-Host "Viva Insights Privacy Configuration Audit:" -ForegroundColor Cyan
Write-Host "==========================================`n"
Write-Host "The following settings must be verified in the Viva Insights admin center:"
Write-Host "1. Minimum aggregation group size: [Verify >= 10]"
Write-Host "2. Manager insights: [Verify disabled or selective]"
Write-Host "3. Data access roles: [Verify restricted to authorized users]"
Write-Host "4. Data retention period: [Verify per organizational policy]"
Write-Host "`nNote: Viva Insights admin settings are primarily managed via the web portal."
Write-Host "PowerShell automation for these settings is limited."
Write-Host "`nReview at: https://insights.viva.office.com"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Impact data extraction | Monthly | Script 1 |
| User comparison analysis | Monthly | Script 2 |
| ROI estimation report | Quarterly | Script 3 |
| Privacy configuration audit | Quarterly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate impact measurement
- See [Troubleshooting](troubleshooting.md) for Viva Insights issues
