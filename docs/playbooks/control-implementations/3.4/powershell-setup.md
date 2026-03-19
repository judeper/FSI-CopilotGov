# Control 3.4: Communication Compliance Monitoring — PowerShell Setup

Automation scripts for deploying and managing communication compliance policies that monitor Copilot-assisted communications, including reporting on IRM integration status and indicator flow.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement` (Security & Compliance PowerShell)
- **Permissions:** Compliance Administrator or Communication Compliance Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Inventory Microsoft Purview Communication Compliance Policies

```powershell
# Retrieve existing communication compliance (supervisory review) policies
# Communication compliance is managed via Security & Compliance PowerShell,
# not via the Microsoft Graph API

$policies = Get-SupervisoryReviewPolicyV2

if ($policies.Count -eq 0) {
    Write-Host "No communication compliance policies found." -ForegroundColor Yellow
    Write-Host "Create policies in the Microsoft Purview compliance portal under Communication Compliance."
} else {
    Write-Host "Communication Compliance Policies:" -ForegroundColor Green
    $policies | Select-Object Name, Enabled, CreatedBy, LastModifiedDateTime |
        Format-Table -AutoSize
}
```

### Script 2: Generate Communication Compliance Review Report

```powershell
# Report on communication compliance review items and status
$startDate = (Get-Date).AddDays(-30).ToString("yyyy-MM-dd")
$endDate = (Get-Date).ToString("yyyy-MM-dd")

# Search audit log for communication compliance actions
$reviewActions = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -RecordType ComplianceSuperVisionExchange `
    -ResultSize 5000

$summary = $reviewActions | Group-Object Operations | Select-Object @{
    N='Action'; E={$_.Name}}, @{N='Count'; E={$_.Count}}

Write-Host "Communication Compliance Activity Summary (Last 30 Days):"
$summary | Format-Table -AutoSize

# Export detailed report
$reviewActions | Select-Object CreationDate, UserIds, Operations, AuditData |
    Export-Csv "CommComplianceReport_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Monitor Policy Match Volume

```powershell
# Track the volume of communication compliance policy matches over time
$periods = @(7, 14, 30, 90)
$results = @()

foreach ($days in $periods) {
    $start = (Get-Date).AddDays(-$days)
    $end = Get-Date

    $matches = Search-UnifiedAuditLog `
        -StartDate $start -EndDate $end `
        -Operations "SupervisionPolicyMatch" `
        -ResultSize 5000

    $results += [PSCustomObject]@{
        Period       = "$days days"
        TotalMatches = $matches.Count
        AvgPerDay    = [math]::Round($matches.Count / $days, 1)
    }
}

Write-Host "Policy Match Trend Analysis:"
$results | Format-Table -AutoSize
```

### Script 4: Verify IRM Integration — Check for CC Indicators in IRM Audit Log

```powershell
# Verify that Communication Compliance violations are generating IRM risk indicators
# This confirms the CC-to-IRM integration is functioning
$startDate = (Get-Date).AddDays(-7)
$endDate = Get-Date

# Check for IRM risk events sourced from Communication Compliance
$irmCcEvents = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -RecordType SecurityComplianceInsights `
    -ResultSize 5000 |
    Where-Object { $_.AuditData -like "*CommunicationCompliance*" }

if ($irmCcEvents.Count -eq 0) {
    Write-Host "WARNING: No CC-sourced IRM indicators found in the last 7 days." -ForegroundColor Yellow
    Write-Host "Verify: (1) IRM integration is enabled in CC Settings, (2) CC policy matches have occurred, (3) allow up to 24 hours for propagation."
} else {
    Write-Host "IRM integration confirmed: $($irmCcEvents.Count) CC-sourced IRM events in the last 7 days." -ForegroundColor Green
    $irmCcEvents | Select-Object CreationDate, UserIds, Operations |
        Export-Csv "IRM-CC-Indicators_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
}
```

### Script 5: Export Pending Review Items Summary

```powershell
# Identify the volume and age of pending review items
$pendingReviews = Search-UnifiedAuditLog `
    -StartDate (Get-Date).AddDays(-30) `
    -EndDate (Get-Date) `
    -Operations "SupervisionPolicyMatch" `
    -ResultSize 5000

$pendingByUser = $pendingReviews | Group-Object UserIds |
    Select-Object @{N='User'; E={$_.Name}}, @{N='PendingItems'; E={$_.Count}} |
    Sort-Object PendingItems -Descending

Write-Host "Pending Review Items by User (Last 30 Days):"
$pendingByUser | Format-Table -AutoSize

$pendingByUser | Export-Csv "PendingReviews_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Compliance review report | Weekly | Script 2 |
| Policy match volume monitoring | Daily | Script 3 |
| IRM integration health check | Weekly | Script 4 |
| Pending review items check | Daily | Script 5 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate communication compliance
- See [Troubleshooting](troubleshooting.md) for common policy issues
