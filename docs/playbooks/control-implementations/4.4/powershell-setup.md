# Control 4.4: Copilot in Viva Suite Governance — PowerShell Setup

Automation scripts for managing Copilot governance across the Microsoft Viva suite.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** Global Administrator or Viva Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "Organization.ReadWrite.All", "AuditLog.Read.All", "User.Read.All"
```

## Scripts

### Script 1: Viva Engage Copilot Usage Report

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

### Script 2: Viva Engage Communication Compliance Check

```powershell
# Verify communication compliance policies cover Viva Engage
$ccPolicies = Search-UnifiedAuditLog `
    -StartDate (Get-Date).AddDays(-30) -EndDate (Get-Date) `
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
```

### Script 3: Viva License and Feature Inventory

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

### Script 4: Viva Governance Configuration Snapshot

```powershell
# Capture a governance configuration snapshot for Viva suite
$snapshot = @"
# Viva Suite Governance Configuration Snapshot
## Date: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss UTC")

### Viva Engage
- Communication Compliance: Verify in Purview portal
- Data Retention: Verify retention policies include Yammer/Engage locations
- Copilot Features: Verify in Viva Engage Admin Center

### Viva Learning
- Content Sources: Verify approved content providers
- Compliance Training: Verify mandatory training requirements
- AI Recommendations: Verify in Viva Learning Admin

### Viva Goals
- Access Controls: Verify organizational hierarchy restrictions
- AI Features: Verify in Viva Goals Admin
- Data Boundaries: Verify Copilot content access scope

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
| Viva Copilot usage report | Monthly | Script 1 |
| Engage compliance check | Monthly | Script 2 |
| License inventory | Quarterly | Script 3 |
| Governance snapshot | Quarterly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate Viva governance
- See [Troubleshooting](troubleshooting.md) for Viva Copilot issues
