# Control 3.4: Communication Compliance Monitoring — PowerShell Setup

Automation scripts for deploying and managing communication compliance policies that monitor Copilot-assisted communications.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph.Compliance`
- **Permissions:** Compliance Administrator or Communication Compliance Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module ExchangeOnlineManagement
Connect-IPPSSession -UserPrincipalName admin@contoso.com
Connect-MgGraph -Scopes "CommunicationsCompliance.ReadWrite.All"
```

## Scripts

### Script 1: Create Communication Compliance Policy via Graph API

```powershell
# Create a communication compliance policy targeting Copilot-assisted communications
# Note: Communication compliance policies are primarily managed via portal
# The Graph API supports reporting and review operations

$policyParams = @{
    displayName = "FSI-Copilot-Communication-Monitoring"
    description = "Monitors Copilot-assisted communications for FSI regulatory compliance"
}

# Retrieve existing policies for inventory
$existingPolicies = Invoke-MgGraphRequest -Method GET `
    -Uri "https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases" `
    -OutputType PSObject

Write-Host "Current compliance policies retrieved for review" -ForegroundColor Green
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

### Script 4: Export Pending Review Items Summary

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
| Pending review items check | Daily | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate communication compliance
- See [Troubleshooting](troubleshooting.md) for common policy issues
