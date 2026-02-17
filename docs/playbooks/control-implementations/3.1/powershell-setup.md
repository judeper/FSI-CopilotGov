# Control 3.1: Copilot Interaction Audit Logging — PowerShell Setup

Automation scripts for configuring, monitoring, and reporting on Copilot interaction audit logs in Microsoft 365.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph.Security`
- **Permissions:** Compliance Administrator or Global Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
# Connect to Exchange Online for audit management
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

# Connect to Microsoft Graph for advanced queries
Import-Module Microsoft.Graph.Security
Connect-MgGraph -Scopes "AuditLog.Read.All"
```

## Scripts

### Script 1: Verify Audit Log Status

```powershell
# Check if unified audit logging is enabled
$auditStatus = Get-AdminAuditLogConfig | Select-Object UnifiedAuditLogIngestionEnabled
if ($auditStatus.UnifiedAuditLogIngestionEnabled -eq $true) {
    Write-Host "Audit logging is ENABLED" -ForegroundColor Green
} else {
    Write-Warning "Audit logging is DISABLED — enabling now"
    Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true
}
```

### Script 2: Search Copilot Interaction Audit Logs

```powershell
# Search for all Copilot interactions in the last 7 days
$startDate = (Get-Date).AddDays(-7)
$endDate = Get-Date

$copilotLogs = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

Write-Host "Found $($copilotLogs.Count) Copilot interaction records"

# Export to CSV for compliance review
$copilotLogs | Select-Object CreationDate, UserIds, Operations, AuditData |
    Export-Csv -Path "CopilotAuditLog_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Create Audit Retention Policy

```powershell
# Create 10-year retention policy for Copilot interactions (FSI regulated)
New-UnifiedAuditLogRetentionPolicy `
    -Name "FSI-Copilot-10Year-Retention" `
    -Description "10-year retention for Copilot interactions per FSI regulatory requirements" `
    -RecordTypes CopilotInteraction `
    -RetentionDuration TenYears `
    -Priority 100
```

### Script 4: Daily Copilot Activity Summary Report

```powershell
# Generate daily summary of Copilot usage across the organization
$yesterday = (Get-Date).AddDays(-1).Date
$today = (Get-Date).Date

$dailyLogs = Search-UnifiedAuditLog `
    -StartDate $yesterday -EndDate $today `
    -RecordType CopilotInteraction -ResultSize 5000

$summary = $dailyLogs | Group-Object UserIds | Select-Object @{
    N='User'; E={$_.Name}}, @{N='InteractionCount'; E={$_.Count}
} | Sort-Object InteractionCount -Descending

$summary | Export-Csv "DailyCopilotSummary_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Daily summary exported: $($summary.Count) users, $($dailyLogs.Count) total interactions"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Audit log status check | Daily | Script 1 |
| Copilot log export | Weekly | Script 2 |
| Daily activity summary | Daily | Script 4 |
| Retention policy review | Quarterly | Script 3 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate audit log coverage
- See [Troubleshooting](troubleshooting.md) for common audit logging issues
