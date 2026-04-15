# Control 4.2: Copilot in Teams Meetings Governance — Verification & Testing

Test cases and evidence collection procedures to validate Copilot governance in Teams meetings, including the critical test for EnabledWithTranscript enforcement following Microsoft's March 2026 default change.

## Test Cases

### Test 1: EnabledWithTranscript Enforcement (Critical)

- **Objective:** Verify that Copilot cannot activate in meetings without transcription — confirming the March 2026 default change has been remediated
- **Steps:**
  1. Run the PowerShell audit script: `Get-CsTeamsMeetingPolicy -Identity "FSI-Regulated-Policy" | Select-Object CopilotWithoutTranscript`
  2. Confirm the output shows `Disabled`.
  3. In a test meeting with the regulated policy applied, start the meeting without enabling transcription.
  4. Attempt to activate Copilot — Copilot should either be unavailable or prompt to enable transcription first.
  5. Enable transcription and verify Copilot becomes available.
  6. Check the Teams audit log to confirm that Copilot events are accompanied by corresponding transcription start events.
- **Expected Result:** Copilot requires transcription to be active; `CopilotWithoutTranscript` returns `Disabled`; Copilot-generated artifacts have accompanying verbatim transcripts in storage.
- **Evidence:** PowerShell output screenshot; meeting test screenshots showing Copilot availability states; audit log showing transcript and Copilot events paired.

### Test 2: Audit Log Verification — Transcript and Copilot Event Pairing

- **Objective:** Confirm that audit logs show transcript capture events alongside Copilot interaction events for every regulated meeting
- **Steps:**
  1. Conduct a test meeting with Copilot enabled and the FSI regulated policy in effect.
  2. After the meeting, search the Unified Audit Log for the meeting's date range:
     ```powershell
     Search-UnifiedAuditLog -StartDate [date] -EndDate [date] -RecordType CopilotInteraction
     Search-UnifiedAuditLog -StartDate [date] -EndDate [date] -Operations "MeetingTranscriptCreated", "TeamsTranscriptionStarted"
     ```
  3. Verify that Copilot interaction events for the meeting are accompanied by transcript creation events.
  4. Document the correlation for the evidence package.
- **Expected Result:** Transcript creation event in audit log accompanies every Copilot interaction event for regulated meetings.
- **Evidence:** Exported audit log records showing paired transcript and Copilot events.

### Test 3: Copilot Availability with Transcript

- **Objective:** Verify Copilot is available in meetings when transcription is active
- **Steps:**
  1. Schedule a Teams meeting with the FSI Copilot meeting policy applied.
  2. Start the meeting and enable transcription.
  3. Verify Copilot is available and functioning (recap, notes, action items accessible).
  4. Document the results for evidence.
- **Expected Result:** Copilot available when transcription is active, supporting the audit trail requirement.
- **Evidence:** Screenshots showing Copilot availability when transcription is enabled.

### Test 4: MNPI Meeting Policy Enforcement

- **Objective:** Confirm that Copilot is disabled for MNPI-designated meetings
- **Steps:**
  1. Assign the MNPI meeting policy to a test user.
  2. Have the test user schedule and join a meeting.
  3. Verify that Copilot, transcription, and recording are all disabled.
  4. Confirm no AI features are accessible during the meeting.
- **Expected Result:** All AI features are disabled in MNPI-policy meetings.
- **Evidence:** Screenshot showing disabled AI features in the meeting interface.

### Test 5: Meeting Summary Distribution Control

- **Objective:** Validate that meeting summaries are only distributed to authorized attendees
- **Steps:**
  1. Hold a meeting with Copilot enabled and transcript running.
  2. After the meeting, check where the meeting summary is stored and who has access.
  3. Verify that external participants do not receive meeting summaries if restricted by policy.
  4. Confirm the summary respects any sensitivity labels applied to the meeting.
- **Expected Result:** Meeting summaries are distributed only to authorized attendees per policy.
- **Evidence:** Summary distribution list and access permissions documentation.

### Test 6: Meeting Transcript Retention

- **Objective:** Verify that meeting transcripts are retained per the regulatory retention policy
- **Steps:**
  1. Locate a meeting transcript from at least 30 days ago.
  2. Verify the transcript is still available and accessible.
  3. Confirm the retention policy is applied to the transcript location.
  4. Verify the transcript cannot be deleted before the retention period expires.
- **Expected Result:** Meeting transcripts are retained and protected by the retention policy.
- **Evidence:** Transcript access confirmation and retention policy application proof.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| CopilotWithoutTranscript=Disabled verification | PowerShell | Screenshot/export | With control documentation |
| Audit log transcript + Copilot event pairing | Unified Audit Log | CSV export | Per retention policy |
| Meeting policy configuration | Teams Admin Center | Screenshot | With control documentation |
| Copilot availability test (with transcript) | Meeting interface | Screenshot | With control documentation |
| MNPI policy test | Meeting interface | Screenshot | With control documentation |
| Transcript retention proof | SharePoint/OneDrive | Screenshot | Per retention policy |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Rule 17a-4(b)(4) | 3-year preservation of business communications | EnabledWithTranscript supports verbatim transcript paired with AI summaries; both retained per policy |
| FINRA 3110(b)(4) | Supervisory review of communications | AI-generated meeting summaries reviewable through Communication Compliance |
| FINRA 4511 | Books and records preservation | Meeting transcripts and Copilot artifacts retained under Exchange and OneDrive retention policies |
| FFIEC | IT governance of AI features | Supports governance of AI-enabled collaboration tools |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Teams meeting Copilot issues
- Proceed to [Control 4.3](../4.3/portal-walkthrough.md) for Teams Phone governance
- Back to [Control 4.2](../../../controls/pillar-4-operations/4.2-teams-meetings-governance.md)
