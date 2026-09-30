# Control 4.4: Copilot in Viva Suite Governance — PowerShell Setup

Automation scripts for managing Copilot governance across the Microsoft Viva suite, including Copilot Chat analytics reporting and Engage-to-Teams integration compliance verification.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** Entra Global Admin or Viva Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Organization.ReadWrite.All", "AuditLog.Read.All", "User.Read.All", "Reports.Read.All"
```

## Scripts

### Script 1: Copilot Chat Activity Summary for Licensed Users

```powershell
# Report Copilot Chat activity from the Microsoft 365 Copilot usage-detail CSV.
# This report includes only Microsoft 365 Copilot-licensed users.
# Department isn't included in the v1 usage-detail columns; for a department
# view, join these rows to Get-MgUser -Property Department separately.
# Requires: Microsoft Graph Scopes — Reports.Read.All, Organization.Read.All
# Note: Viva Insights Copilot Chat analytics respect configured minimum group size thresholds

# Retrieve Copilot Chat usage detail (aggregated at tenant level)
# Use report version v1 so the CSV header remains "Copilot Chat Last Activity Date".
$reportUri = "https://graph.microsoft.com/v1.0/copilot/reports/getMicrosoft365CopilotUsageUserDetail(period='D30',version='v1')"
Invoke-MgGraphRequest -Method GET -Uri $reportUri -OutputFilePath "CopilotChatUsage_$(Get-Date -Format 'yyyyMMdd').csv"

$usageData = @(Import-Csv "CopilotChatUsage_$(Get-Date -Format 'yyyyMMdd').csv")
$copilotChatActivityColumn = 'Copilot Chat Last Activity Date'

if (-not $usageData -or $usageData.Count -eq 0) {
    throw "The Copilot usage report returned zero rows. Verify that Microsoft 365 Copilot-licensed users have activity in the selected period."
}

if (-not ($usageData[0].PSObject.Properties.Name -contains $copilotChatActivityColumn)) {
    $availableHeaders = $usageData[0].PSObject.Properties.Name -join ", "
    throw "Expected CSV header '$copilotChatActivityColumn' was not found. Available headers: $availableHeaders"
}

$activeUsers = @($usageData | Where-Object {
    $_.$copilotChatActivityColumn -and $_.$copilotChatActivityColumn -ne ''
}).Count
$totalLicensed = @($usageData).Count

$summary = [PSCustomObject]@{
    ReportScope             = "Microsoft 365 Copilot-licensed users"
    LicensedUsers           = $totalLicensed
    ActiveCopilotChatUsers  = $activeUsers
    AdoptionRate            = if ($totalLicensed -gt 0) { "$([math]::Round($activeUsers / $totalLicensed * 100, 1))%" } else { "N/A" }
}

Write-Host "Copilot Chat Activity Summary (Last 30 Days):" -ForegroundColor Cyan
$summary | Format-Table -AutoSize
$summary | Export-Csv "CopilotChatActivitySummary_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Note: The Graph usage-detail API returns Microsoft 365 Copilot-licensed users only. Join to Microsoft Graph user profiles if you need department-level reporting." -ForegroundColor Yellow
```

### Script 2: Configure Copilot Chat Analytics Reporting Scope and Privacy Thresholds

```powershell
# Query current Viva Insights privacy configuration for Copilot Chat analytics
# Requires: Viva Insights Administrator role or Entra Global Admin
# Note: Full privacy threshold configuration is completed via the Viva Insights Admin portal
#       (insights.viva.office.com > Admin > Privacy settings). This script validates current state.

# Retrieve Viva Insights organizational configuration
$insightsConfig = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/organization" | Select-Object -ExpandProperty value

Write-Host "Tenant ID: $($insightsConfig[0].Id)" -ForegroundColor Cyan
Write-Host ""
Write-Host "Viva Insights Copilot Chat Analytics Privacy Validation:" -ForegroundColor Cyan
Write-Host "  Minimum group size: Review in Viva Insights Admin portal > Privacy settings"
Write-Host "  Recommended FSI minimum: 25 users per department for Copilot Chat analytics"
Write-Host ""

# Check Copilot Chat usage report availability
try {
    $testUri = "https://graph.microsoft.com/v1.0/copilot/reports/getMicrosoft365CopilotUsageUserDetail(period='D7',version='v1')"
    Invoke-MgGraphRequest -Method GET -Uri $testUri -OutputFilePath "$env:TEMP\CopilotTest.csv"
    $testData = Import-Csv "$env:TEMP\CopilotTest.csv"
    Write-Host "Copilot Chat usage reporting: ACTIVE ($($testData.Count) records in past 7 days)" -ForegroundColor Green
    Remove-Item "$env:TEMP\CopilotTest.csv" -Force
} catch {
    Write-Warning "Copilot Chat usage reporting may not be enabled or license may not be assigned."
    Write-Host "Action required: Enable Copilot Chat analytics in Viva Insights Admin portal." -ForegroundColor Yellow
}
```

### Script 3: Viva Engage Copilot Usage Report

```powershell
# Report on Copilot usage within Viva Engage
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$engageEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$vivaEvents = $engageEvents | Where-Object {
    $_.AuditData -like "*Viva*" -or $_.AuditData -like "*Engage*" -or $_.AuditData -like "*Yammer*"
}

Write-Host "Viva Suite Copilot Usage (Last 30 Days):"
Write-Host "Total Viva-related Copilot events: $($vivaEvents.Count)"

$vivaEvents | Select-Object CreationDate, UserIds, Operations |
    Export-Csv "VivaCopilotUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Viva Engage Communication Compliance and Teams Integration Check

```powershell
# Verify communication compliance policies cover Viva Engage and the Engage-to-Teams integration
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

# Check for Engage/Yammer policy matches
$ccPolicies = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -Operations "SupervisionPolicyMatch" `
    -ResultSize 5000

$engageMatches = $ccPolicies | Where-Object {
    $_.AuditData -like "*Yammer*" -or $_.AuditData -like "*Engage*"
}

Write-Host "Communication Compliance Coverage for Viva Engage (Last 30 Days):"
Write-Host "Policy matches from Engage: $($engageMatches.Count)"

if ($engageMatches.Count -eq 0) {
    Write-Warning "No compliance matches detected from Viva Engage — verify policy scope includes Engage"
}

# Check for Teams policy matches — Engage content surfacing in Teams should also appear here
$teamsMatches = $ccPolicies | Where-Object {
    $_.AuditData -like "*Teams*"
}

Write-Host ""
Write-Host "Teams Communication Compliance matches (Last 30 Days): $($teamsMatches.Count)"
Write-Host ""
Write-Host "Engage-to-Teams Integration Retention Policy Check:" -ForegroundColor Cyan

# Verify retention policies include both Yammer and Teams locations
$retentionPolicies = Get-RetentionCompliancePolicy | Where-Object {
    $_.Enabled -eq $true
}

$engageRetentionPolicies = $retentionPolicies | Where-Object {
    $_.YammerLocation -ne $null -and $_.YammerLocation -ne ""
}

$teamsRetentionPolicies = $retentionPolicies | Where-Object {
    $_.TeamsChannelLocation -ne $null -and $_.TeamsChannelLocation -ne ""
}

Write-Host "Active retention policies covering Viva Engage (Yammer): $($engageRetentionPolicies.Count)"
Write-Host "Active retention policies covering Teams channels: $($teamsRetentionPolicies.Count)"

if ($engageRetentionPolicies.Count -eq 0) {
    Write-Warning "No active retention policies found for Viva Engage — verify Yammer location is included in retention policy."
}
if ($teamsRetentionPolicies.Count -eq 0) {
    Write-Warning "No active retention policies for Teams channels — Engage content surfacing in Teams may not be retained."
}
```

### Script 5: Viva License and Feature Inventory

```powershell
# Report on Viva suite license assignments and feature availability
$vivaSkus = Get-MgSubscribedSku | Where-Object {
    $_.SkuPartNumber -like "*VIVA*" -or $_.SkuPartNumber -like "*Engage*"
}

$inventory = $vivaSkus | ForEach-Object {
    [PSCustomObject]@{
        SKU          = $_.SkuPartNumber
        TotalUnits   = $_.PrepaidUnits.Enabled
        AssignedUnits = $_.ConsumedUnits
        Available    = $_.PrepaidUnits.Enabled - $_.ConsumedUnits
    }
}

Write-Host "Viva License Inventory:" -ForegroundColor Cyan
$inventory | Format-Table -AutoSize
$inventory | Export-Csv "VivaLicenses_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 6: Viva Governance Configuration Snapshot

```powershell
# Capture a governance configuration snapshot for Viva suite
$snapshot = @"
# Viva Suite Governance Configuration Snapshot
## Date: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC")

### Viva Insights — Copilot Chat Analytics
- Copilot Chat usage reporting: Verify enabled in Viva Insights Admin portal > Advanced Insights
- Minimum group size: Verify set to 25+ for regulated departments
- Department dashboards: Verify analyst access configured for business unit leaders

### Viva Engage
- Communication Compliance: Verify in Purview portal — scope includes Yammer and Teams locations
- Data Retention: Verify retention policies include Yammer/Engage locations
- Engage-to-Teams Integration: Verify Teams retention and CC policies cover surfaced Engage content
- Copilot Features: Verify in Viva Engage Admin Center

### Viva Learning
- Content Sources: Verify approved content providers
- Compliance Training: Verify mandatory training requirements
- AI Recommendations: Verify in Viva Learning Admin

### Viva Goals
- Product status: Retired December 31, 2025
- Evidence: Verify historical data export or migration record
- Current scope: No live Copilot configuration

### Viva Connections
- Dashboard Content: Verify sensitivity label compliance
- News Handling: Verify Copilot content surfacing rules
"@

$snapshot | Out-File "VivaGovernanceSnapshot_$(Get-Date -Format 'yyyyMMdd').md" -Encoding UTF8
Write-Host "Governance snapshot generated" -ForegroundColor Green
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Copilot Chat department adoption report | Monthly | Script 1 |
| Copilot Chat analytics privacy validation | Quarterly | Script 2 |
| Viva Copilot usage report | Monthly | Script 3 |
| Engage compliance and Teams integration check | Monthly | Script 4 |
| License inventory | Quarterly | Script 5 |
| Governance snapshot | Quarterly | Script 6 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate Viva governance
- See [Troubleshooting](troubleshooting.md) for Viva Copilot issues
- Back to [Control 4.4](../../../controls/pillar-4-operations/4.4-viva-suite-governance.md)
