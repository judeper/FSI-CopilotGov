# Control 2.10: Insider Risk Detection for Copilot Usage — PowerShell Setup

Automation scripts for monitoring and reporting on insider risk detection for Copilot.

## Prerequisites

- Exchange Online Management / Security & Compliance PowerShell
- Audit access for CopilotInteraction records
- Supported Insider Risk Management subscription and assigned licenses

## Scripts

> Microsoft Learn pages in scope for this control document Risky AI usage, Risky Agents, Policy indicators, data risk graph, and the Triage Agent primarily through the Microsoft Purview portal. Use the scripts below for audit-backed Copilot usage analysis, and verify IRM policy/template configuration in the Purview portal.

### Script 1: Copilot Interaction Audit Summary

```powershell
# Summarize recent CopilotInteraction audit events for insider-risk review
# Requires: Security & Compliance PowerShell / Exchange Online Management

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$events = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -Operations CopilotInteraction -ResultSize 5000

$summary = $events | Group-Object UserIds | ForEach-Object {
    [PSCustomObject]@{
        User       = $_.Name
        EventCount = $_.Count
        FirstEvent = ($_.Group | Sort-Object CreationDate | Select-Object -First 1).CreationDate
        LastEvent  = ($_.Group | Sort-Object CreationDate -Descending | Select-Object -First 1).CreationDate
    }
} | Sort-Object EventCount -Descending

Write-Host "=== CopilotInteraction Audit Summary ==="
Write-Host "Users with CopilotInteraction events: $($summary.Count)"
$summary | Format-Table User, EventCount, FirstEvent, LastEvent -AutoSize
$summary | Export-Csv "CopilotInteractionSummary_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 2: Risk Signal Extraction from Copilot Audit Data

```powershell
# Extract audit properties that are useful during insider-risk review, such as
# AppHost, Bing web grounding, and jailbreak detection flags.
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-14)
$endDate = Get-Date

$copilotEvents = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -Operations CopilotInteraction -ResultSize 5000

$riskSignals = $copilotEvents | ForEach-Object {
    $audit = $_.AuditData | ConvertFrom-Json
    $usedWebSearch = @($audit.AISystemPlugin | Where-Object { $_.Id -eq "BingWebSearch" }).Count -gt 0
    $jailbreakDetected = @($audit.Messages | Where-Object { $_.JailbreakDetected -eq $true }).Count -gt 0
    [PSCustomObject]@{
        Date               = $_.CreationDate
        User               = $_.UserIds
        AppHost            = $audit.AppHost
        AppIdentity        = $audit.AppIdentity
        UsedWebSearch      = $usedWebSearch
        JailbreakDetected  = $jailbreakDetected
    }
}

Write-Host "=== Copilot Audit Risk Signals ==="
$riskSignals | Group-Object User | Sort-Object Count -Descending | Select-Object -First 20 |
    Format-Table Name, Count -AutoSize
$riskSignals | Export-Csv "CopilotAuditSignals_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 3: Off-Hours Copilot Activity Report

```powershell
# Detect Copilot usage outside business hours
# Requires: Security & Compliance PowerShell

Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-14)
$endDate = Get-Date

$events = Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate `
    -Operations CopilotInteraction -ResultSize 5000

$offHours = @()
foreach ($event in $events) {
    $eventTime = [DateTime]$event.CreationDate
    $hour = $eventTime.Hour
    if ($hour -lt 7 -or $hour -gt 20) {
        $offHours += [PSCustomObject]@{
            Date = $event.CreationDate
            User = $event.UserIds
            Hour = $hour
        }
    }
}

Write-Host "Off-hours Copilot activity (before 7am or after 8pm): $($offHours.Count)"
$offHours | Export-Csv "OffHoursCopilot_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Purpose |
|------|-----------|---------|
| CopilotInteraction Audit Summary | Weekly | Establish the Copilot interaction baseline used in investigations |
| Copilot Audit Risk Signals | Weekly | Review Bing web grounding and jailbreak-related audit indicators |
| Off-Hours Activity Report | Weekly | Flag off-hours access for review |

## Next Steps

- See [Verification & Testing](verification-testing.md) for insider risk validation
- See [Troubleshooting](troubleshooting.md) for insider risk issues
- Back to [Control 2.10](../../../controls/pillar-2-security/2.10-insider-risk-detection.md)
