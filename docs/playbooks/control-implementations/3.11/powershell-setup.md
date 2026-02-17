# Control 3.11: Record Keeping and Books-and-Records Compliance — PowerShell Setup

Automation scripts for implementing and managing records management for Copilot-generated content.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`
- **Permissions:** Records Management Administrator, Compliance Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Create Regulatory Record Retention Labels

```powershell
# Create retention labels for books-and-records compliance
$labels = @(
    @{Name="SEC-17a4-Business-Communication-6yr"; Duration=2190; Description="SEC 17a-4 business communication records — 6 year retention"},
    @{Name="FINRA-4511-Client-Record-7yr"; Duration=2555; Description="FINRA 4511 client correspondence — 7 year retention"},
    @{Name="Investment-Recommendation-Record-7yr"; Duration=2555; Description="Investment recommendation records — 7 year retention"},
    @{Name="Marketing-Material-Record-3yr"; Duration=1095; Description="Marketing material records — 3 year retention"}
)

foreach ($label in $labels) {
    New-ComplianceTag `
        -Name $label.Name `
        -Comment $label.Description `
        -RetentionAction KeepAndDelete `
        -RetentionDuration $label.Duration `
        -RetentionType CreationAgeInDays `
        -IsRecordLabel $true `
        -Regulatory $true

    Write-Host "Created regulatory record label: $($label.Name)" -ForegroundColor Green
}
```

### Script 2: Publish Retention Labels to All Locations

```powershell
# Publish all regulatory record labels to relevant locations
$labelNames = @(
    "SEC-17a4-Business-Communication-6yr",
    "FINRA-4511-Client-Record-7yr",
    "Investment-Recommendation-Record-7yr",
    "Marketing-Material-Record-3yr"
)

New-RetentionCompliancePolicy `
    -Name "FSI-Regulatory-Record-Labels" `
    -RetentionComplianceTag $labelNames `
    -ExchangeLocation "All" `
    -SharePointLocation "All" `
    -OneDriveLocation "All" `
    -ModernGroupLocation "All" `
    -Enabled $true

Write-Host "Regulatory record labels published to all locations" -ForegroundColor Green
```

### Script 3: Enable Preservation Lock on Critical Policies

```powershell
# Enable Preservation Lock for SEC 17a-4(f) WORM compliance
# WARNING: Preservation Lock is IRREVERSIBLE — policy cannot be shortened or removed
$policyName = "FSI-Regulatory-Record-Labels"

Write-Warning "Preservation Lock is IRREVERSIBLE. The policy cannot be shortened or disabled after locking."
Write-Host "Policy: $policyName" -ForegroundColor Yellow
$confirm = Read-Host "Type 'CONFIRM' to enable Preservation Lock"

if ($confirm -eq "CONFIRM") {
    Set-RetentionCompliancePolicy `
        -Identity $policyName `
        -RestrictiveRetention $true
    Write-Host "Preservation Lock ENABLED on $policyName" -ForegroundColor Red
} else {
    Write-Host "Preservation Lock NOT enabled — operation cancelled" -ForegroundColor Yellow
}
```

### Script 4: Records Management Compliance Report

```powershell
# Generate a report of records management status across the tenant
$policies = Get-RetentionCompliancePolicy | Where-Object { $_.Name -like "*FSI*" -or $_.Name -like "*Record*" }

$report = foreach ($policy in $policies) {
    $rules = Get-RetentionComplianceRule -Policy $policy.Name
    [PSCustomObject]@{
        PolicyName       = $policy.Name
        Enabled          = $policy.Enabled
        RestrictiveRetention = $policy.RestrictiveRetention
        RetentionDays    = $rules.RetentionDuration
        IsRegulatory     = $rules.Regulatory
        DistributionStatus = $policy.DistributionStatus
    }
}

Write-Host "Records Management Policy Report:"
$report | Format-Table -AutoSize
$report | Export-Csv "RecordsManagement_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Label deployment verification | Monthly | Script 4 |
| New label creation | As needed | Script 1 |
| Preservation Lock review | Annually | Script 3 (verify) |
| Policy compliance report | Quarterly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate records management
- See [Troubleshooting](troubleshooting.md) for records management issues
