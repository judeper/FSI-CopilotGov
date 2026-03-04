# Control 4.12: Change Management for Copilot Feature Rollouts — PowerShell Setup

Automation scripts for monitoring Microsoft 365 Message Center announcements, tracking service health incidents, and auditing configuration changes related to Copilot feature rollouts.

## Prerequisites

- **Modules:** `Microsoft.Graph`, `ExchangeOnlineManagement`
- **Permissions:** ServiceMessage.Read.All, ServiceHealth.Read.All, AuditLog.Read.All
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module Microsoft.Graph
Connect-MgGraph -Scopes "ServiceMessage.Read.All", "ServiceHealth.Read.All"
```

## Scripts

### Script 1: Monitor Message Center for Copilot Updates

```powershell
# Retrieve Copilot-related Message Center announcements
# Filters by the "Microsoft Copilot (Microsoft 365)" service and Copilot title matches
Connect-MgGraph -Scopes "ServiceMessage.Read.All"

$since = (Get-Date).AddDays(-90).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

$messages = Get-MgServiceAnnouncementMessage -All `
    -Filter "lastModifiedDateTime ge $since" |
    Where-Object {
        $_.Services -contains "Microsoft Copilot (Microsoft 365)" -or
        $_.Title -match "Copilot"
    } |
    Sort-Object LastModifiedDateTime -Descending

Write-Host "Copilot Message Center Entries (Last 90 Days): $($messages.Count)" -ForegroundColor Cyan

$export = $messages | Select-Object Id, Title, LastModifiedDateTime, MessageType,
    Severity,
    @{N="Services";E={$_.Services -join ", "}},
    @{N="ActionRequiredByDate";E={$_.ActionRequireByDate}}

$export | Format-Table Id, Title, Severity, ActionRequiredByDate -AutoSize

$export | Export-Csv "CopilotMessageCenter_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Message Center export complete" -ForegroundColor Green
```

### Script 2: Retrieve Specific Message Center Entry

```powershell
# Look up a specific MC message by ID for change assessment documentation
# Example: MC1139493 (Teams Copilot default change, September 2025)
Connect-MgGraph -Scopes "ServiceMessage.Read.All"

$messageId = "MC1139493"  # Replace with the MC ID to review

$message = Get-MgServiceAnnouncementMessage -ServiceUpdateMessageId $messageId

if ($message) {
    Write-Host "MC Entry: $($message.Title)" -ForegroundColor Cyan
    Write-Host "Last Modified: $($message.LastModifiedDateTime)"
    Write-Host "Severity: $($message.Severity)"
    Write-Host "Action Required By: $($message.ActionRequireByDate)"
    Write-Host "Services: $($message.Services -join ', ')"
    Write-Host ""
    Write-Host "Body (plain text excerpt):" -ForegroundColor Cyan
    # Strip HTML tags for readable output
    $plainText = $message.Body.Content -replace '<[^>]+>', ''
    $plainText.Substring(0, [Math]::Min($plainText.Length, 500))
} else {
    Write-Warning "Message $messageId not found — it may have expired or the ID may be incorrect"
}
```

### Script 3: Service Health Tracking for Copilot

```powershell
# Check active and recent service health issues affecting Copilot
Connect-MgGraph -Scopes "ServiceHealth.Read.All"

$issues = Get-MgServiceAnnouncementIssue -All |
    Where-Object { $_.Service -match "Copilot" }

$active = $issues | Where-Object { $_.Status -ne "Resolved" }
$recent = $issues | Where-Object {
    $_.Status -eq "Resolved" -and
    $_.LastModifiedDateTime -ge (Get-Date).AddDays(-30)
}

Write-Host "Copilot Service Health Issues:" -ForegroundColor Cyan
Write-Host "  Active: $($active.Count)"
Write-Host "  Resolved (last 30 days): $($recent.Count)"

if ($active.Count -gt 0) {
    Write-Host "`nActive Issues:" -ForegroundColor Yellow
    $active | Select-Object Id, Title, Service, Status, StartDateTime,
        LastModifiedDateTime | Format-Table -AutoSize
}

$issues | Select-Object Id, Title, Service, Status, StartDateTime,
    LastModifiedDateTime |
    Export-Csv "CopilotServiceHealth_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "Service health export complete" -ForegroundColor Green

# NOTE: For continuous monitoring, consider a Power Automate flow that triggers
# on new Message Center posts matching "Copilot" and routes them to your change
# management team via email or Teams channel.
```

### Script 4: Copilot Configuration Change Audit

```powershell
# Audit tenant-level Copilot configuration changes via UAL
Import-Module ExchangeOnlineManagement
Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

# Search for Copilot admin operations (policy changes, plugin management)
$adminOps = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -Operations "UpdateTenantSettings","CreatePlugin","DeletePlugin","EnablePromptBook" `
    -ResultSize 5000

Write-Host "Copilot Admin Configuration Changes (Last 30 Days): $($adminOps.Count)" -ForegroundColor Cyan

$adminOps | ForEach-Object {
    $data = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date      = $_.CreationDate
        User      = $_.UserIds
        Operation = $_.Operations
        Detail    = $data.Operation
    }
} | Format-Table -AutoSize

$adminOps | Select-Object CreationDate, UserIds, Operations |
    Export-Csv "CopilotConfigChanges_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

# LIMITATION: Release preference settings (Targeted vs. Standard release) must be
# verified manually in the M365 Admin Center:
#   Settings > Org settings > Organization profile > Release preferences
# There is no PowerShell cmdlet to read or set release preferences.
Write-Host "`nRelease preferences require manual verification in M365 Admin Center" -ForegroundColor Yellow
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Message Center monitoring | Weekly | Script 1 |
| Specific MC review | As needed | Script 2 |
| Service health check | Daily | Script 3 |
| Configuration change audit | Weekly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate change management
- See [Troubleshooting](troubleshooting.md) for change management issues
