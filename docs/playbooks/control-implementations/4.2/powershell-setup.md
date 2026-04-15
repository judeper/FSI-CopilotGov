# Control 4.2: Copilot in Teams Meetings Governance — PowerShell Setup

Automation scripts for configuring and managing Copilot governance in Microsoft Teams meetings, including the critical remediation for Microsoft's late April 2026 EnabledWithTranscript default change.

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

### Script 1: Enforce EnabledWithTranscript (Critical Remediation)

This script addresses the late April 2026 Microsoft default change from `EnabledWithTranscript` to `Enabled`. Run this script immediately for any Teams environment where recordkeeping obligations apply.

```powershell
# ============================================================
# CRITICAL REMEDIATION: Teams Copilot Default Change (Late April 2026)
# Microsoft changed default from EnabledWithTranscript to Enabled.
# This script enforces EnabledWithTranscript for FSI compliance.
# ============================================================

Import-Module MicrosoftTeams
Connect-MicrosoftTeams

# Step 1: Audit current state of all meeting policies
Write-Host "=== Current Meeting Policy Copilot Settings ===" -ForegroundColor Cyan
$allPolicies = Get-CsTeamsMeetingPolicy
foreach ($policy in $allPolicies) {
    $copilotStatus = $policy.CopilotWithoutTranscript
    $flagged = if ($copilotStatus -ne "Disabled") { " <-- ACTION REQUIRED" } else { "" }
    Write-Host "Policy: $($policy.Identity) | CopilotWithoutTranscript: $copilotStatus$flagged"
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

# Enforce EnabledWithTranscript: Copilot cannot run without transcription
Set-CsTeamsMeetingPolicy -Identity $policyName `
    -AllowTranscription $true `
    -AllowCloudRecording $true `
    -RecordingStorageMode "OneDriveForBusiness" `
    -Copilot "EnabledWithTranscript" `
    -CopilotWithoutTranscript "Disabled"

# Step 3: Verify the setting
$verifyPolicy = Get-CsTeamsMeetingPolicy -Identity $policyName
Write-Host "`n=== Verification ===" -ForegroundColor Cyan
Write-Host "Policy: $policyName"
Write-Host "CopilotWithoutTranscript: $($verifyPolicy.CopilotWithoutTranscript)"
if ($verifyPolicy.CopilotWithoutTranscript -eq "Disabled") {
    Write-Host "PASS: EnabledWithTranscript enforced — Copilot requires transcription." -ForegroundColor Green
} else {
    Write-Host "FAIL: CopilotWithoutTranscript is NOT Disabled. Review policy settings." -ForegroundColor Red
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
    -CopilotWithoutTranscript "Disabled" `
    -AllowMeetingCoach $false

Write-Host "MNPI meeting policy created: $mnpiPolicyName (Copilot DISABLED)" -ForegroundColor Yellow
```

### Script 4: Verify EnabledWithTranscript Across All Policies (Compliance Audit)

```powershell
# Audit all Teams meeting policies for Copilot transcript enforcement compliance
Write-Host "=== Teams Meeting Policy Copilot Audit ===" -ForegroundColor Cyan
Write-Host "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm')`n"

$allPolicies = Get-CsTeamsMeetingPolicy
$compliant = @()
$nonCompliant = @()

foreach ($policy in $allPolicies) {
    $status = [PSCustomObject]@{
        PolicyName              = $policy.Identity
        CopilotSetting          = $policy.Copilot
        CopilotWithoutTranscript = $policy.CopilotWithoutTranscript
        AllowTranscription      = $policy.AllowTranscription
        Compliant               = ($policy.CopilotWithoutTranscript -eq "Disabled" -or $policy.Copilot -eq "Disabled")
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
    Write-Host "All meeting policies comply with EnabledWithTranscript requirement." -ForegroundColor Green
}

Write-Host "`nCompliant policies:" -ForegroundColor Green
$compliant | Format-Table -AutoSize

# Export audit results
$allPolicies | Select-Object Identity, Copilot, CopilotWithoutTranscript, AllowTranscription |
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
| EnabledWithTranscript remediation | Immediate (run once; re-run after policy changes) | Script 1 |
| Policy assignment to user groups | As needed | Script 2 |
| Compliance audit of all policies | Monthly | Script 4 |
| Meeting Copilot usage report | Weekly | Script 5 |
| MNPI policy review | Quarterly | Script 3 (verify) |

## Next Steps

- See [Verification & Testing](verification-testing.md) to validate meeting governance
- See [Troubleshooting](troubleshooting.md) for Teams meeting issues
- Back to [Control 4.2](../../../controls/pillar-4-operations/4.2-teams-meetings-governance.md)
