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

# --- Configurable assumptions — update these to reflect current pricing and org estimates ---
# $costPerUser: M365 Copilot license cost per user/month. Verify at https://www.microsoft.com/en-us/microsoft-365/copilot
$costPerUser = 30
# $estimatedTimeSavedMinPerWeek: Estimated minutes saved per active user per week. Adjust based on org survey data or Viva Insights time-saved metrics.
$estimatedTimeSavedMinPerWeek = 60
# $hourlyLaborCost: Average fully-loaded labor cost per hour for your organization.
$hourlyLaborCost = 75

$monthlyLicenseSpend = $totalLicensed * $costPerUser
$monthlyTimeSavings = $activeUsers * $estimatedTimeSavedMinPerWeek * 4.33 / 60  # hours per month
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
# What IS available via PowerShell: Copilot Dashboard usage summary via Graph API
Write-Host "Viva Insights Privacy Configuration Audit:" -ForegroundColor Cyan
Write-Host "==========================================`n"

# Retrieve Copilot usage summary from Viva Insights Copilot Dashboard
Write-Host "--- Copilot Usage Summary (Graph API) ---" -ForegroundColor Yellow
try {
    $usageSummary = Invoke-MgGraphRequest -Method GET `
        -Uri "https://graph.microsoft.com/v1.0/reports/microsoft365CopilotUsageSummary(period='D30')"
    $usageSummary | ConvertTo-Json -Depth 5 | Out-File "VivaInsights_CopilotSummary_$(Get-Date -Format 'yyyyMMdd').json"
    Write-Host "  Copilot usage summary exported successfully" -ForegroundColor Green
} catch {
    Write-Warning "  Unable to retrieve Copilot usage summary: $($_.Exception.Message)"
}

# Note: Viva Insights admin settings (minimum group size, manager insights, data access roles,
# data retention) are portal-only — no PowerShell cmdlets are available for these controls.
# Default minimum aggregation group size is 10 (recommended FSI minimum: 10–25).
Write-Host "`n--- Settings Requiring Portal Verification ---" -ForegroundColor Yellow
Write-Host "  Portal: insights.viva.cloud.microsoft > Copilot Dashboard"
Write-Host "  Admin:  M365 Admin Center > Viva > Viva Insights > Settings"
Write-Host ""
$portalChecks = @(
    [PSCustomObject]@{ Setting="Minimum aggregation group size"; Expected=">= 10"; Status="Verify in portal" }
    [PSCustomObject]@{ Setting="Manager insights"; Expected="Disabled or selective"; Status="Verify in portal" }
    [PSCustomObject]@{ Setting="Data access roles"; Expected="Restricted to authorized users"; Status="Verify in portal" }
    [PSCustomObject]@{ Setting="Data retention period"; Expected="Per organizational policy"; Status="Verify in portal" }
)
$portalChecks | Format-Table -AutoSize
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
