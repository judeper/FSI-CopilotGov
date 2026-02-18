# Control 4.2: Copilot in Teams Meetings Governance — Troubleshooting

Common issues and resolution steps for Copilot governance in Teams meetings, including issues related to Microsoft's March 2026 EnabledWithTranscript default change.

## Common Issues

### Issue 1: Copilot Available Without Transcription (Post-March 2026 Default Change)

- **Symptoms:** Users can access Copilot in meetings even when transcription is not enabled, bypassing the recordkeeping requirement. This issue is expected for any environment that has not yet applied the EnabledWithTranscript remediation after Microsoft's March 2026 default change.
- **Root Cause:** Microsoft changed the default Teams meeting Copilot policy from `EnabledWithTranscript` to `Enabled` in March 2026. Any meeting policy that was not explicitly overridden now defaults to allowing Copilot without transcription. Additionally, new policies created after March 2026 default to `Enabled` unless explicitly set to `EnabledWithTranscript`.
- **Resolution:**
  1. Run the immediate remediation:
     ```powershell
     Set-CsTeamsMeetingPolicy -Identity "FSI-Regulated-Policy" -CopilotWithoutTranscript Disabled
     ```
  2. Verify the policy change:
     ```powershell
     Get-CsTeamsMeetingPolicy -Identity "FSI-Regulated-Policy" | Select-Object CopilotWithoutTranscript
     # Expected: Disabled
     ```
  3. Run the full audit script (Script 4 in PowerShell Setup) to identify any other policies that still permit Copilot without transcript.
  4. Apply the fix to all non-compliant policies.
  5. Verify the correct policy is assigned to the affected user: `Get-CsOnlineUser -Identity user@contoso.com | Select TeamsMeetingPolicy`
  6. If the policy was recently changed, allow up to 24 hours for propagation.

### Issue 2: Policy Not Applying After Update (Assignment Delay)

- **Symptoms:** The meeting policy has been updated to enforce `CopilotWithoutTranscript = Disabled`, but users still see Copilot available without transcription in live meetings.
- **Root Cause:** Teams meeting policy changes typically propagate within 1-4 hours, but can take up to 24 hours in large tenants. Users already in active meetings may not receive the updated policy until they start a new meeting.
- **Resolution:**
  1. Verify the policy has been saved correctly: `Get-CsTeamsMeetingPolicy -Identity "FSI-Regulated-Policy" | Format-List`
  2. Confirm the policy is assigned to the affected user: `Get-CsOnlineUser -Identity "user@contoso.com" | Select TeamsMeetingPolicy`
  3. Ask the user to completely close and restart Teams to force policy refresh.
  4. Wait up to 24 hours and retest.
  5. For urgent compliance situations: temporarily suspend the user's Copilot license until the policy propagates fully.

### Issue 3: Copilot Priority — Per-User vs. Org-Wide Policy Inheritance

- **Symptoms:** Different users in the same meeting see different Copilot availability despite having the same meeting policy. Some users see Copilot available without transcription despite the org-wide policy restricting this.
- **Root Cause:** Teams Copilot availability in meetings is primarily determined by the meeting **organizer's** policy, not the attendee's policy. If the organizer has a different (or the old default) policy, Copilot behavior in the meeting reflects the organizer's policy settings.
- **Resolution:**
  1. Identify the meeting organizer and check their assigned policy: `Get-CsOnlineUser -Identity "organizer@contoso.com" | Select TeamsMeetingPolicy`
  2. Ensure the organizer also has the FSI-Regulated-Policy (or equivalent EnabledWithTranscript policy) assigned.
  3. For comprehensive coverage: apply the FSI-Regulated-Policy to all users, not just attendees — meeting behavior is organizer-controlled.
  4. Document in supervisory procedures that meeting organizer policy controls Copilot behavior.

### Issue 4: Copilot Not Working in Teams Meetings

- **Symptoms:** Copilot button is grayed out or not visible during meetings for licensed users.
- **Root Cause:** Transcription may not be enabled, the user may lack the Copilot license, or the Teams client is outdated.
- **Resolution:**
  1. Verify the user has an active Copilot license.
  2. Confirm transcription is enabled in the meeting (required under EnabledWithTranscript policy).
  3. Ensure the user is running the latest Teams client version.
  4. Check if the meeting organizer's policy allows Copilot (organizer policy may override attendee policy).
  5. Have the user restart the Teams client to refresh policy assignments.

### Issue 5: MNPI Meeting Policy Not Applied

- **Symptoms:** Users in MNPI-restricted roles still have Copilot and transcription available in meetings.
- **Root Cause:** The MNPI policy may not be assigned to the user, or the meeting organizer's policy is overriding the attendee's policy.
- **Resolution:**
  1. Verify the MNPI policy is assigned: `Get-CsOnlineUser -Identity user@contoso.com | Select TeamsMeetingPolicy`
  2. Remember that certain meeting features are controlled by the organizer's policy, not the attendee's.
  3. For MNPI meetings, ensure the meeting organizer also has the MNPI policy applied.
  4. Use sensitivity labels on meetings to enforce MNPI restrictions regardless of policy.

### Issue 6: Meeting Summaries Shared Too Broadly

- **Symptoms:** Meeting summaries generated by Copilot are accessible to people who did not attend the meeting.
- **Root Cause:** Meeting summaries may be stored in a location with broader access permissions, or Teams channel meeting summaries are visible to all channel members.
- **Resolution:**
  1. Review where meeting summaries are stored (organizer's OneDrive, SharePoint, or Teams channel).
  2. For sensitive meetings, ensure the meeting is not held in a public Teams channel.
  3. Apply sensitivity labels to restrict summary access.
  4. Configure meeting policies to limit who can access Intelligent Recap.

## Diagnostic Steps

1. **Check EnabledWithTranscript enforcement:** `Get-CsTeamsMeetingPolicy -Identity "FSI-Regulated-Policy" | Select-Object CopilotWithoutTranscript` — expect `Disabled`
2. **Check user policy:** `Get-CsOnlineUser -Identity "user@contoso.com" | Select TeamsMeetingPolicy`
3. **Review meeting policy settings:** `Get-CsTeamsMeetingPolicy -Identity "policy-name" | Format-List`
4. **Run full policy audit:** Execute Script 4 from PowerShell Setup to identify all non-compliant policies.
5. **Verify license:** Confirm Copilot and Teams Premium licenses in the M365 Admin Center.
6. **Check Teams client version:** Verify the user is on the latest Teams client.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Copilot active in meetings without transcription in any regulated environment | IT Admin — immediate policy remediation (`Set-CsTeamsMeetingPolicy -CopilotWithoutTranscript Disabled`); notify Compliance |
| Critical | Copilot active in MNPI meetings | IT Security + Compliance — immediate policy enforcement |
| High | Meeting summaries exposed to unauthorized users | IT Admin + Compliance — access review |
| High | EnabledWithTranscript remediation not propagated after 24 hours | IT Admin — verify policy assignment, escalate to Microsoft Support if needed |
| Medium | Copilot not working for licensed users | IT Support — troubleshoot licensing and policies |
| Low | Minor policy propagation delays | Monitor and verify after 24 hours |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.3: Copilot in Teams Phone](../4.3/portal-walkthrough.md)
