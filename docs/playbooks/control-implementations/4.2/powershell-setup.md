# Control 4.2: Copilot in Teams Meetings Governance — PowerShell Setup

Automation scripts for configuring and managing Copilot governance in Microsoft Teams meetings, including enforcement of the `EnabledWithTranscript` setting for FSI recordkeeping requirements.

## Prerequisites

- **Modules:** `MicrosoftTeams`, `ExchangeOnlineManagement`
- **Permissions:** Teams Admin, Purview Compliance Admin
- **PowerShell:** Version 7.x recommended

## Connect to Required Services

```powershell
Import-Module MicrosoftTeams
Connect-MicrosoftTeams

Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
```

## Scripts

### Script 1: Enforce EnabledWithTranscript (FSI Recordkeeping Baseline)

Microsoft documents `EnabledWithTranscript` as the default value of the `-Copilot` parameter on `Set-CsTeamsMeetingPolicy`. With `EnabledWithTranscript`, organizers cannot change the per-meeting Copilot value — Copilot defaults to **During and after the meeting** and saved transcripts are required. This script enforces that setting on the FSI regulated meeting policy and confirms it across all meeting policies, which supports FINRA Rule 4511 books-and-records expectations and FINRA Rule 3110 supervisory review.

For the supported `-Copilot` values (`Enabled`, `EnabledWithTranscript`, `EnabledWithTranscriptDefaultOn`, `Disabled`) and the corresponding admin center labels, see [Manage Microsoft 365 Copilot in Teams meetings and events](https://learn.microsoft.com/en-us/microsoftteams/copilot-teams-transcription).

```powershell
# ============================================================
# Enforce EnabledWithTranscript on the FSI regulated meeting policy.
# EnabledWithTranscript is the documented default for the -Copilot
# parameter on Set-CsTeamsMeetingPolicy and is required for FSI
# recordkeeping (Copilot only runs when a transcript is captured).
# ============================================================

Import-Module MicrosoftTeams
Connect-MicrosoftTeams

# Step 1: Audit current state of all meeting policies
Write-Host "=== Current Meeting Policy Copilot Settings ===" -ForegroundColor Cyan
$allPolicies = Get-CsTeamsMeetingPolicy
foreach ($policy in $allPolicies) {
    $copilotStatus = $policy.Copilot
    $flagged = if ($copilotStatus -notin @("EnabledWithTranscript", "Disabled")) { " <-- ACTION REQUIRED" } else { "" }
    Write-Host "Policy: $($policy.Identity) | Copilot: $copilotStatus$flagged"
}

# Step 2: Create or update FSI-Regulated-Policy
$policyName = "FSI-Regulated-Policy"
$existingPolicy = Get-CsTeamsMeetingPolicy -Identity $policyName -ErrorAction SilentlyContinue

if (-not $existingPolicy) {
    Write-Host "`nCreating new policy: $policyName" -ForegroundColor Yellow
    New-CsTeamsMeetingPolicy -Identity $policyName
} else {
    Write-Host "`nUpdating existing policy: $policyName" -ForegroundColor Yellow
}

# Enforce EnabledWithTranscript: Copilot only runs when transcription is captured.
Set-CsTeamsMeetingPolicy -Identity $policyName `
    -AllowTranscription $true `
    -AllowCloudRecording $true `
    -RecordingStorageMode "OneDriveForBusiness" `
    -Copilot "EnabledWithTranscript"

# Step 3: Verify the setting
$verifyPolicy = Get-CsTeamsMeetingPolicy -Identity $policyName
Write-Host "`n=== Verification ===" -ForegroundColor Cyan
Write-Host "Policy: $policyName"
Write-Host "Copilot: $($verifyPolicy.Copilot)"
if ($verifyPolicy.Copilot -eq "EnabledWithTranscript") {
    Write-Host "PASS: EnabledWithTranscript enforced — Copilot requires a saved transcript." -ForegroundColor Green
} else {
    Write-Host "FAIL: Copilot is NOT EnabledWithTranscript. Review policy settings." -ForegroundColor Red
}
```

### Script 2: Assign FSI-Regulated Meeting Policy to User Group

```powershell
# Assign the FSI meeting policy to Copilot-licensed users
$policyName = "FSI-Regulated-Policy"
$copilotGroupId = "copilot-users-group-id"

$members = Get-MgGroupMember -GroupId $copilotGroupId -All
$assignedCount = 0

foreach ($member in $members) {
    $user = Get-MgUser -UserId $member.Id -Property UserPrincipalName
    Grant-CsTeamsMeetingPolicy -Identity $user.UserPrincipalName -PolicyName $policyName
    $assignedCount++
}

Write-Host "Meeting policy '$policyName' assigned to $assignedCount users" -ForegroundColor Green
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
    -AllowMeetingCoach $false

Write-Host "MNPI meeting policy created: $mnpiPolicyName (Copilot DISABLED)" -ForegroundColor Yellow
```

### Script 4: Verify EnabledWithTranscript Across All Policies (Compliance Audit)

```powershell
# Audit all Teams meeting policies for Copilot transcript enforcement.
# A policy is considered FSI-compliant only when its -Copilot value is
# EnabledWithTranscript (transcript required) or Disabled (Copilot off).
Write-Host "=== Teams Meeting Policy Copilot Audit ===" -ForegroundColor Cyan
Write-Host "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm')`n"

$allPolicies = Get-CsTeamsMeetingPolicy
$compliant = @()
$nonCompliant = @()

foreach ($policy in $allPolicies) {
    $status = [PSCustomObject]@{
        PolicyName         = $policy.Identity
        CopilotSetting     = $policy.Copilot
        AllowTranscription = $policy.AllowTranscription
        Compliant          = ($policy.Copilot -in @("EnabledWithTranscript", "Disabled"))
    }

    if ($status.Compliant) {
        $compliant += $status
    } else {
        $nonCompliant += $status
    }
}

if ($nonCompliant.Count -gt 0) {
    Write-Host "NON-COMPLIANT POLICIES (ACTION REQUIRED):" -ForegroundColor Red
    $nonCompliant | Format-Table -AutoSize
} else {
    Write-Host "All meeting policies comply with the EnabledWithTranscript requirement." -ForegroundColor Green
}

Write-Host "`nCompliant policies:" -ForegroundColor Green
$compliant | Format-Table -AutoSize

# Export audit results
$allPolicies | Select-Object Identity, Copilot, AllowTranscription |
    Export-Csv "TeamsMeetingPolicyAudit_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
Write-Host "`nAudit exported to TeamsMeetingPolicyAudit_$(Get-Date -Format 'yyyyMMdd').csv"
```

### Script 5: Meeting Copilot Usage Report

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
| EnabledWithTranscript baseline enforcement | Run once; re-run after meeting-policy changes | Script 1 |
| Policy assignment to user groups | As needed | Script 2 |
| Compliance audit of all policies | Monthly | Script 4 |
| Meeting Copilot usage report | Weekly | Script 5 |
| MNPI policy review | Quarterly | Script 3 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate meeting governance
- See [Troubleshooting](troubleshooting.md) for Teams meeting issues
- Back to [Control 4.2](../../../controls/pillar-4-operations/4.2-teams-meetings-governance.md)
