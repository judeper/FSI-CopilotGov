# Control 4.2: Copilot in Teams Meetings Governance — PowerShell Setup

Automation scripts for configuring and managing Copilot governance in Microsoft Teams meetings.

## Prerequisites

- **Modules:** `MicrosoftTeams`, `ExchangeOnlineManagement`
- **Permissions:** Teams Administrator, Compliance Administrator
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module MicrosoftTeams
Connect-MicrosoftTeams

Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Configure Teams Meeting Policy for Copilot

```powershell
# Create or update Teams meeting policy for Copilot-governed meetings
$policyName = "FSI-Copilot-Meeting-Policy"

# Check if policy exists
$existingPolicy = Get-CsTeamsMeetingPolicy -Identity $policyName -ErrorAction SilentlyContinue

if (-not $existingPolicy) {
    New-CsTeamsMeetingPolicy -Identity $policyName
}

Set-CsTeamsMeetingPolicy -Identity $policyName `
    -AllowTranscription $true `
    -AllowCloudRecording $true `
    -RecordingStorageMode "OneDriveForBusiness" `
    -AllowMeetingCoach $true `
    -Copilot "EnabledWithTranscript" `
    -CopilotWithoutTranscript "Disabled"

Write-Host "Meeting policy configured: $policyName" -ForegroundColor Green
```

### Script 2: Assign Meeting Policy to Copilot Users

```powershell
# Assign the Copilot meeting policy to licensed users
$policyName = "FSI-Copilot-Meeting-Policy"
$copilotGroupId = "copilot-users-group-id"

$members = Get-MgGroupMember -GroupId $copilotGroupId -All
$assignedCount = 0

foreach ($member in $members) {
    $user = Get-MgUser -UserId $member.Id -Property UserPrincipalName
    Grant-CsTeamsMeetingPolicy -Identity $user.UserPrincipalName -PolicyName $policyName
    $assignedCount++
}

Write-Host "Meeting policy assigned to $assignedCount users" -ForegroundColor Green
```

### Script 3: Create MNPI Meeting Policy (Copilot Disabled)

```powershell
# Create a restrictive meeting policy for MNPI discussions
$mnpiPolicyName = "FSI-MNPI-Meeting-NoAI"

$existingPolicy = Get-CsTeamsMeetingPolicy -Identity $mnpiPolicyName -ErrorAction SilentlyContinue
if (-not $existingPolicy) {
    New-CsTeamsMeetingPolicy -Identity $mnpiPolicyName
}

Set-CsTeamsMeetingPolicy -Identity $mnpiPolicyName `
    -AllowTranscription $false `
    -AllowCloudRecording $false `
    -Copilot "Disabled" `
    -CopilotWithoutTranscript "Disabled" `
    -AllowMeetingCoach $false

Write-Host "MNPI meeting policy created: $mnpiPolicyName (Copilot DISABLED)" -ForegroundColor Yellow
```

### Script 4: Meeting Copilot Usage Report

```powershell
# Report on Copilot usage in Teams meetings
$startDate = (Get-Date).AddDays(-30)
$endDate = Get-Date

$meetingCopilotEvents = Search-UnifiedAuditLog `
    -StartDate $startDate -EndDate $endDate `
    -RecordType CopilotInteraction `
    -ResultSize 5000

$meetingEvents = $meetingCopilotEvents | Where-Object {
    $_.AuditData -like "*Teams*Meeting*" -or $_.AuditData -like "*meeting*"
}

Write-Host "Copilot in Meetings Usage (Last 30 Days):"
Write-Host "Total meeting Copilot events: $($meetingEvents.Count)"
Write-Host "Unique users: $(($meetingEvents | Select-Object -Unique UserIds).Count)"

$meetingEvents | Select-Object CreationDate, UserIds, Operations |
    Export-Csv "CopilotMeetingUsage_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

## Scheduled Tasks

| Task | Frequency | Script |
|------|-----------|--------|
| Policy assignment verification | Monthly | Script 2 (verify) |
| Meeting Copilot usage report | Weekly | Script 4 |
| MNPI policy review | Quarterly | Script 3 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate meeting governance
- See [Troubleshooting](troubleshooting.md) for Teams meeting issues
