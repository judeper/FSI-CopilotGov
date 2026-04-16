# Control 3.1: Copilot Interaction Audit Logging — PowerShell Setup

Automation scripts for configuring, monitoring, and reporting on Copilot interaction audit logs in Microsoft 365.

## Prerequisites

- **Modules:** `ExchangeOnlineManagement`, `Microsoft.Graph.Security`
- **Permissions:** Purview Compliance Admin or Entra Global Admin
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

### Script 3: Search Agent Administrative Activity

```powershell
# Search for agent configuration changes (AgentAdminActivity)
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$agentAdminLogs = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -RecordType AgentAdminActivity `
    -ResultSize 5000

Write-Host "Found $($agentAdminLogs.Count) agent admin activity records"
$agentAdminLogs | Select-Object CreationDate, UserIds, Operations, AuditData |
    Export-Csv -Path "AgentAdminActivity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

# Search for agent settings changes (AgentSettingsAdminActivity)
$agentSettingsLogs = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -RecordType AgentSettingsAdminActivity `
    -ResultSize 5000

Write-Host "Found $($agentSettingsLogs.Count) agent settings admin activity records"
$agentSettingsLogs | Select-Object CreationDate, UserIds, Operations, AuditData |
    Export-Csv -Path "AgentSettingsActivity_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Filter Audit Data by AgentId or AgentName

```powershell
# Retrieve CopilotInteraction logs and filter for a specific agent
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date
$targetAgentId = "your-agent-id-here"

$allCopilotLogs = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$agentInteractions = $allCopilotLogs | Where-Object {
    $auditData = $_.AuditData | ConvertFrom-Json
    $auditData.AgentId -eq $targetAgentId
}

Write-Host "Found $($agentInteractions.Count) interactions with agent $targetAgentId"
$agentInteractions | Export-Csv -Path "AgentInteractions_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 5: Detect JailbreakDetected Events

```powershell
# Search for and report on JailbreakDetected events — requires immediate review
$startDate = (Get-Date).AddDays(-7)
$endDate = Get-Date

$allCopilotLogs = Search-UnifiedAuditLog `
    -StartDate $startDate `
    -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$jailbreakEvents = $allCopilotLogs | Where-Object {
    $auditData = $_.AuditData | ConvertFrom-Json
    $auditData.JailbreakDetected -eq $true
}

if ($jailbreakEvents.Count -gt 0) {
    Write-Warning "SECURITY ALERT: $($jailbreakEvents.Count) JailbreakDetected events found — escalate per incident response procedures"
    $jailbreakEvents | Select-Object CreationDate, UserIds, AuditData |
        Export-Csv -Path "JailbreakDetected_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
} else {
    Write-Host "No JailbreakDetected events found in search window" -ForegroundColor Green
}
```

### Script 6: Create Audit Retention Policies

```powershell
# Create 6-year retention policy for Copilot interactions (FSI regulated — SEC Rule 17a-4(a))
New-UnifiedAuditLogRetentionPolicy `
    -Name "FSI-Copilot-6Year-Retention" `
    -Description "6-year retention for Copilot interactions per SEC Rule 17a-4(a) and FINRA 4511" `
    -RecordTypes CopilotInteraction `
    -RetentionDuration SixYears `
    -Priority 100

# Create 6-year retention policy for agent administrative record types
New-UnifiedAuditLogRetentionPolicy `
    -Name "FSI-AgentAdmin-6Year-Retention" `
    -Description "6-year retention for agent admin events per Sarbanes-Oxley §404 IT general controls" `
    -RecordTypes @("AgentAdminActivity", "AgentSettingsAdminActivity") `
    -RetentionDuration SixYears `
    -Priority 100

Write-Host "Audit retention policies created" -ForegroundColor Green
```

### Script 7: Daily Copilot Activity Summary Report

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

### Script 8: PAYG Billing Monitoring

```powershell
# Monitor PAYG audit event volume (helps track spend at $0.01 per event)
# Run this monthly to project PAYG billing costs before invoice
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$copilotVolume = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction -ResultSize 1 -SessionCommand ReturnNextPreviewPage
# Note: For volume estimation, use the Management Activity API for accurate counts at scale

$agentAdminVolume = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType AgentAdminActivity -ResultSize 1 -SessionCommand ReturnNextPreviewPage

Write-Host "PAYG Cost Estimate (30-day period at `$0.01/event):"
Write-Host "  Review Azure Cost Management for actual charges — filter by 'Microsoft.Purview' resource provider"
Write-Host "  Ensure budget alerts are configured in Azure Cost Management for your Purview audit spend threshold"
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Audit log status check | Daily | Script 1 |
| Copilot log export | Weekly | Script 2 |
| Agent admin activity review | Weekly | Script 3 |
| JailbreakDetected scan | Daily | Script 5 |
| Daily activity summary | Daily | Script 7 |
| PAYG billing review | Monthly | Script 8 |
| Retention policy review | Quarterly | Script 6 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate audit log coverage
- See [Troubleshooting](troubleshooting.md) for common audit logging issues
- Back to [Control 3.1](../../../controls/pillar-3-compliance/3.1-copilot-audit-logging.md)
