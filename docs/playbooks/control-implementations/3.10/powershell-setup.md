# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — PowerShell Setup

Automation scripts for implementing and monitoring privacy controls for consumer financial information when using Copilot.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph`
- **Permissions:** Compliance Administrator, Information Protection Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "InformationProtectionPolicy.ReadWrite.All", "AuditLog.Read.All"
```

## Scripts

### Script 1: Create DLP Policy for Consumer Financial Information

```powershell
# Create DLP policy protecting consumer financial data in Copilot interactions
New-DlpCompliancePolicy `
    -Name "FSI-RegSP-Copilot-Privacy-Protection" `
    -Comment "Protects consumer financial information per SEC Reg S-P" `
    -ExchangeLocation "All" `
    -SharePointLocation "All" `
    -OneDriveLocation "All" `
    -TeamsLocation "All" `
    -Mode Enable

# Rule for low-volume NPI detection
New-DlpComplianceRule `
    -Name "RegSP-LowVolume-NPI-Warn" `
    -Policy "FSI-RegSP-Copilot-Privacy-Protection" `
    -ContentContainsSensitiveInformation @(
        @{Name="U.S. Social Security Number (SSN)"; minCount="1"; maxCount="9"},
        @{Name="Credit Card Number"; minCount="1"; maxCount="9"},
        @{Name="U.S. Bank Account Number"; minCount="1"; maxCount="9"}
    ) `
    -NotifyUser Owner `
    -NotifyUserType Sender

# Rule for high-volume NPI detection
New-DlpComplianceRule `
    -Name "RegSP-HighVolume-NPI-Block" `
    -Policy "FSI-RegSP-Copilot-Privacy-Protection" `
    -ContentContainsSensitiveInformation @(
        @{Name="U.S. Social Security Number (SSN)"; minCount="10"},
        @{Name="Credit Card Number"; minCount="10"},
        @{Name="U.S. Bank Account Number"; minCount="10"}
    ) `
    -BlockAccess $true `
    -NotifyUser Owner, SiteAdmin

Write-Host "Reg S-P DLP policy created with low and high volume rules" -ForegroundColor Green
```

### Script 2: DLP Incident Report for Privacy Violations

```powershell
# Generate a report of DLP incidents involving consumer financial data
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$dlpIncidents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType DLP `
    -ResultSize 5000

$npiIncidents = $dlpIncidents | Where-Object {
    $_.AuditData -like "*SSN*" -or
    $_.AuditData -like "*Credit Card*" -or
    $_.AuditData -like "*Bank Account*"
}

Write-Host "Reg S-P Privacy Incident Summary (Last 30 Days):"
Write-Host "Total DLP incidents: $($dlpIncidents.Count)"
Write-Host "NPI-related incidents: $($npiIncidents.Count)"

$npiIncidents | Select-Object CreationDate, UserIds, Operations |
    Export-Csv "RegSP_PrivacyIncidents_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Content Explorer NPI Location Report

```powershell
# Identify locations containing consumer financial information
$sensitiveTypes = @(
    "U.S. Social Security Number (SSN)",
    "Credit Card Number",
    "U.S. Bank Account Number",
    "U.S. Individual Taxpayer Identification Number (ITIN)"
)

foreach ($type in $sensitiveTypes) {
    $results = Get-DlpSensitiveInformationTypeRulePackage |
        Where-Object { $_.Name -like "*$type*" }
    Write-Host "SIT: $type — Rule Package: $($results.Name)" -ForegroundColor Cyan
}

Write-Host "`nUse Content Explorer in the Purview portal to identify NPI locations." -ForegroundColor Yellow
Write-Host "Path: Purview > Data classification > Content explorer > Sensitive info types"
```

### Script 4: Privacy Control Compliance Scorecard

```powershell
# Generate Reg S-P compliance scorecard for Copilot privacy controls
$scorecard = @(
    [PSCustomObject]@{Control="DLP for NPI"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Information Barriers"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Sensitivity Labels"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Access Controls"; Status="Active"; LastVerified=(Get-Date -Format "yyyy-MM-dd")},
    [PSCustomObject]@{Control="Privacy Impact Assessment"; Status="Completed"; LastVerified=(Get-Date -Format "yyyy-MM-dd")}
)

Write-Host "Reg S-P Privacy Control Scorecard:"
$scorecard | Format-Table -AutoSize
$scorecard | Export-Csv "RegSP_Scorecard_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| DLP incident report | Weekly | Script 2 |
| NPI location assessment | Quarterly | Script 3 |
| Privacy control scorecard | Monthly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate privacy protections
- See [Troubleshooting](troubleshooting.md) for privacy control issues
