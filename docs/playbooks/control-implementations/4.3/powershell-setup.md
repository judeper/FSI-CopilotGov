# Control 4.3: Copilot in Teams Phone and Queues Governance — PowerShell Setup

Automation scripts for configuring and managing Copilot governance in Teams Phone and call queue environments.

## Prerequisites

- **Modules:** `MicrosoftTeams`, `ExchangeOnlineManagement`
- **Permissions:** Teams Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module MicrosoftTeams
Connect-MicrosoftTeams
```

## Scripts

### Script 1: Configure Calling Policy with Copilot Controls

```powershell
# Create calling policy with Copilot governance settings
$policyName = "FSI-Copilot-Calling-Policy"

$existingPolicy = Get-CsTeamsCallingPolicy -Identity $policyName -ErrorAction SilentlyContinue
if (-not $existingPolicy) {
    New-CsTeamsCallingPolicy -Identity $policyName
}

Set-CsTeamsCallingPolicy -Identity $policyName `
    -AllowVoicemail "AlwaysEnabled" `
    -AllowCallForwardingToPhone $true `
    -AllowCallForwardingToUser $true `
    -BusyOnBusyEnabledType "Enabled" `
    -AllowWebPSTNCalling $true

Write-Host "Calling policy created: $policyName" -ForegroundColor Green
Write-Host "Note: Copilot-specific calling settings are configured in Teams Admin Center" -ForegroundColor Yellow
```

### Script 2: Assign Calling Policies to Phone Users

```powershell
# Assign the FSI calling policy to Teams Phone users
$policyName = "FSI-Copilot-Calling-Policy"
$phoneUsers = Get-CsOnlineUser -Filter { EnterpriseVoiceEnabled -eq $true }

$assignedCount = 0
foreach ($user in $phoneUsers) {
    Grant-CsTeamsCallingPolicy -Identity $user.UserPrincipalName -PolicyName $policyName
    $assignedCount++
}

Write-Host "Calling policy assigned to $assignedCount Teams Phone users" -ForegroundColor Green
```

### Script 3: Report on Call Queue Configuration

```powershell
# Report on call queue configurations and Copilot settings
$callQueues = Get-CsCallQueue

$report = $callQueues | ForEach-Object {
    [PSCustomObject]@{
        Name              = $_.Name
        Agents            = $_.Agents.Count
        RoutingMethod     = $_.RoutingMethod
        OverflowAction    = $_.OverflowAction
        TimeoutAction     = $_.TimeoutAction
        LanguageId        = $_.LanguageId
    }
}

Write-Host "Call Queue Configuration Report:" -ForegroundColor Cyan
$report | Format-Table -AutoSize
$report | Export-Csv "CallQueueConfig_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Phone Call Copilot Usage Audit

```powershell
# Audit Copilot usage in Teams Phone interactions
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$phoneEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$callEvents = $phoneEvents | Where-Object {
    $_.AuditData -like "*Phone*" -or $_.AuditData -like "*PSTN*" -or $_.AuditData -like "*Call*"
}

Write-Host "Copilot in Teams Phone Usage (Last 30 Days):"
Write-Host "Total call-related Copilot events: $($callEvents.Count)"

$callEvents | Select-Object CreationDate, UserIds, Operations |
    Export-Csv "CopilotPhoneUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Policy assignment verification | Monthly | Script 2 (verify) |
| Call queue configuration audit | Quarterly | Script 3 |
| Phone Copilot usage report | Weekly | Script 4 |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate phone governance
- See [Troubleshooting](troubleshooting.md) for Teams Phone Copilot issues
