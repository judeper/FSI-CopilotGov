# Control 4.2: Copilot in Teams Meetings Governance — Verification & Testing

Test cases and evidence collection procedures to validate Copilot governance in Teams meetings.

## Test Cases

### Test 1: Copilot Availability with Transcript

- **Objective:** Verify Copilot is available in meetings only when transcription is active
- **Steps:**
  1. Schedule a Teams meeting with the FSI Copilot meeting policy applied.
  2. Start the meeting without enabling transcription.
  3. Verify Copilot is not available or prompts to enable transcription.
  4. Enable transcription and verify Copilot becomes available.
- **Expected Result:** Copilot requires transcription to be active, supporting the audit trail requirement.
- **Evidence:** Screenshots showing Copilot availability state with and without transcription.

### Test 2: MNPI Meeting Policy Enforcement

- **Objective:** Confirm that Copilot is disabled for MNPI-designated meetings
- **Steps:**
  1. Assign the MNPI meeting policy to a test user.
  2. Have the test user schedule and join a meeting.
  3. Verify that Copilot, transcription, and recording are all disabled.
  4. Confirm no AI features are accessible during the meeting.
- **Expected Result:** All AI features are disabled in MNPI-policy meetings.
- **Evidence:** Screenshot showing disabled AI features in the meeting interface.

### Test 3: Meeting Summary Distribution Control

- **Objective:** Validate that meeting summaries are only distributed to authorized attendees
- **Steps:**
  1. Hold a meeting with Copilot enabled and transcript running.
  2. After the meeting, check where the meeting summary is stored and who has access.
  3. Verify that external participants do not receive meeting summaries if restricted by policy.
  4. Confirm the summary respects any sensitivity labels applied to the meeting.
- **Expected Result:** Meeting summaries are distributed only to authorized attendees per policy.
- **Evidence:** Summary distribution list and access permissions documentation.

### Test 4: Meeting Transcript Retention

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
| Meeting policy configuration | Teams Admin Center | Screenshot | With control documentation |
| Copilot availability test | Meeting interface | Screenshot | With control documentation |
| MNPI policy test | Meeting interface | Screenshot | With control documentation |
| Transcript retention proof | SharePoint/OneDrive | Screenshot | Per retention policy |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110 | Meeting supervision and documentation | Supports compliance with supervisory review of meeting content |
| SEC 17a-4 | Meeting record retention | Helps meet record retention for AI-generated meeting records |
| FFIEC | IT governance of AI features | Supports governance of AI-enabled collaboration tools |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Teams meeting Copilot issues
- Proceed to [Control 4.3](../4.3/portal-walkthrough.md) for Teams Phone governance
