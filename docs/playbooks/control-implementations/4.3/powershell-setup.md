# Control 4.3: Copilot in Teams Phone and Queues Governance — PowerShell Setup

Automation scripts for configuring and auditing Copilot-relevant settings in Teams Phone and call queue environments. Copilot in Teams Phone relies on call transcription and recording infrastructure — these scripts configure the underlying policies that support Copilot functionality and compliance record-keeping.

## Prerequisites

- **Modules:** `MicrosoftTeams`, `ExchangeOnlineManagement`
- **Permissions:** Teams Admin, Purview Compliance Admin (for audit log search)
- **Licenses:** Microsoft 365 Copilot, Teams Phone
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module MicrosoftTeams
Connect-MicrosoftTeams

# For audit log search (Script 4)
Import-Module ExchangeOnlineManagement
Connect-IPPSSession
```

## Scripts

### Script 1: Configure Calling Policy with Copilot-Relevant Controls

Copilot in Teams Phone requires call transcription to generate real-time assistance and post-call summaries. This script configures the calling policy parameters that support Copilot functionality.

```powershell
# Configure calling policy with transcription and recording for Copilot support
# Copilot in calls depends on AllowTranscriptionForCalling and AllowCloudRecordingForCalls
# Requires: MicrosoftTeams module

$policyName = "FSI-Copilot-Calling-Policy"

$existingPolicy = Get-CsTeamsCallingPolicy -Identity $policyName -ErrorAction SilentlyContinue
if (-not $existingPolicy) {
    New-CsTeamsCallingPolicy -Identity $policyName
}

Set-CsTeamsCallingPolicy -Identity $policyName `
    -AllowCloudRecordingForCalls $true `
    -AllowTranscriptionForCalling $true `
    -LiveCaptionsEnabledType "DisabledUserOverride" `
    -AllowPrivateCalling $true `
    -AllowVoicemail "UserOverride" `
    -AllowCallGroups $true `
    -AllowDelegation $true `
    -AllowCallForwardingToUser $true `
    -AllowCallForwardingToPhone $true

Write-Host "Calling policy configured: $policyName" -ForegroundColor Green

# Verify Copilot-relevant parameters
Write-Host "`nVerification — Copilot-relevant calling policy settings:" -ForegroundColor Cyan
Get-CsTeamsCallingPolicy -Identity $policyName |
    Select-Object Identity, AllowCloudRecordingForCalls, AllowTranscriptionForCalling,
        LiveCaptionsEnabledType, AllowPrivateCalling, AllowVoicemail |
    Format-List
```

### Script 2: Configure Meeting Policy for Copilot with Transcript Enforcement

Teams meetings involving phone dial-in participants also require meeting policy configuration. Effective March 2026, the Global policy default changed to allow Copilot without transcription — FSI organizations should explicitly set `EnabledWithTranscript` to support compliance record-keeping.

```powershell
# Configure meeting policy to require Copilot WITH transcript
# Critical: Default changed March 2026 — without explicit setting, post-meeting
# Copilot summaries and "after the meeting" access are unavailable
# Requires: MicrosoftTeams module

$meetingPolicyName = "FSI-Regulated"

Set-CsTeamsMeetingPolicy -Identity $meetingPolicyName `
    -Copilot "EnabledWithTranscript" `
    -AllowTranscription $true `
    -AllowCloudRecording $true `
    -LiveCaptionsEnabledType "DisabledUserOverride" `
    -AllowMeetingCoach $true `
    -AllowCarbonSummary $true

Write-Host "Meeting policy configured: $meetingPolicyName" -ForegroundColor Green

# Verify Global policy Copilot default (check for post-March 2026 drift)
Write-Host "`nGlobal policy Copilot settings (verify post-March 2026 default):" -ForegroundColor Cyan
Get-CsTeamsMeetingPolicy -Identity Global |
    Select-Object Identity, Copilot, AllowTranscription, AllowCloudRecording |
    Format-List

# Assign calling and meeting policies to Teams Phone users
$callingPolicyName = "FSI-Copilot-Calling-Policy"
$phoneUsers = Get-CsOnlineUser -Filter { EnterpriseVoiceEnabled -eq $true }

$assignedCount = 0
foreach ($user in $phoneUsers) {
    Grant-CsTeamsCallingPolicy -Identity $user.UserPrincipalName -PolicyName $callingPolicyName
    Grant-CsTeamsMeetingPolicy -Identity $user.UserPrincipalName -PolicyName $meetingPolicyName
    $assignedCount++
}

Write-Host "`nCalling + meeting policies assigned to $assignedCount Teams Phone users" -ForegroundColor Green
```

### Script 3: Call Queue and Compliance Recording Audit

Call queue Copilot access is governed by each agent's calling policy and license assignment — `Set-CsCallQueue` does not have direct Copilot-specific parameters. This script audits call queue configuration and verifies compliance recording policies.

```powershell
# Audit call queue configurations
# Note: Set-CsCallQueue has no direct Copilot parameters as of March 2026
# Copilot availability for queue agents depends on agent-level calling policy + license
# Requires: MicrosoftTeams module

$callQueues = Get-CsCallQueue

$queueReport = $callQueues | ForEach-Object {
    [PSCustomObject]@{
        Name              = $_.Name
        Agents            = $_.Agents.Count
        RoutingMethod     = $_.RoutingMethod
        OverflowAction    = $_.OverflowAction
        TimeoutAction     = $_.TimeoutAction
        LanguageId        = $_.LanguageId
    }
}

Write-Host "=== Call Queue Configuration Report ===" -ForegroundColor Cyan
$queueReport | Format-Table -AutoSize

# Verify compliance recording policies
# Certified providers (NICE, Verint, etc.) capture Copilot-generated call summaries
# if the provider supports transcript ingestion
Write-Host "`n=== Compliance Recording Policies ===" -ForegroundColor Cyan
$recordingPolicies = Get-CsTeamsComplianceRecordingPolicy
if ($recordingPolicies) {
    $recordingPolicies | Select-Object Identity, Enabled,
        ComplianceRecordingApplications | Format-Table -AutoSize
} else {
    Write-Warning "No compliance recording policies found."
    Write-Host "Configure via: Teams Admin Center > Voice > Compliance recording policies" -ForegroundColor Yellow
}

# Export combined report
$queueReport | Export-Csv "CallQueueConfig_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

### Script 4: Copilot Usage Audit for Teams Phone Context

Copilot interactions in Teams calls log under `RecordType = CopilotInteraction` with `AppHost` values that include `Teams`. This script searches the Unified Audit Log and filters for call-context Copilot events.

```powershell
# Search Copilot audit events and filter for Teams call context
# Requires: ExchangeOnlineManagement module, Connect-IPPSSession

$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$copilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

# Parse AuditData and filter for call-related Copilot interactions
$callCopilotEvents = $copilotEvents | ForEach-Object {
    $auditData = $_.AuditData | ConvertFrom-Json
    [PSCustomObject]@{
        Date        = $_.CreationDate
        User        = $_.UserIds
        Operation   = $_.Operations
        AppHost     = $auditData.AppHost
        Resources   = ($auditData.AccessedResources.Name -join "; ")
    }
} | Where-Object {
    $_.AppHost -match "Teams" -or
    $_.Operation -match "Call|Phone|PSTN"
}

Write-Host "=== Copilot in Teams Phone Usage (Last 30 Days) ===" -ForegroundColor Cyan
Write-Host "Total Copilot events found: $($copilotEvents.Count)"
Write-Host "Teams/call-context events: $($callCopilotEvents.Count)"

if ($callCopilotEvents.Count -gt 0) {
    $callCopilotEvents | Group-Object AppHost |
        Select-Object @{N='AppHost';E={$_.Name}}, @{N='Count';E={$_.Count}} |
        Format-Table -AutoSize
}

$callCopilotEvents | Export-Csv "CopilotPhoneUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Calling policy verification | Monthly | Script 1 (verify section) |
| Policy assignment for new phone users | Monthly | Script 2 |
| Call queue + compliance recording audit | Quarterly | Script 3 |
| Copilot phone usage report | Weekly | Script 4 |

## Limitations

| Area | Detail |
|------|--------|
| Call queue Copilot params | `Set-CsCallQueue` has no direct Copilot parameters; agent Copilot access is governed by per-user calling policy and license |
| Compliance recording | Copilot-generated call summaries are captured only if the certified recording provider supports transcript ingestion |
| Audit log filtering | No dedicated `AppHost` value for "phone call Copilot" — filter on `Teams` and verify call context in audit data |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate phone governance
- See [Troubleshooting](troubleshooting.md) for Teams Phone Copilot issues
