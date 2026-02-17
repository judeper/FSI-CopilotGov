# Control 4.3: Copilot in Teams Phone and Queues Governance — Verification & Testing

Test cases and evidence collection procedures for Copilot governance in Teams Phone and call queues.

## Test Cases

### Test 1: Call Transcription and Summary Generation

- **Objective:** Verify that Copilot generates accurate call summaries with transcription
- **Steps:**
  1. Place a test call using Teams Phone with a Copilot-enabled user.
  2. Discuss predefined test content (e.g., account review, product inquiry).
  3. End the call and wait for Copilot to generate the call summary.
  4. Review the summary for accuracy, completeness, and appropriate detail level.
- **Expected Result:** Call summary accurately reflects the conversation content with key topics and action items.
- **Evidence:** Call summary output with comparison to the actual conversation content.

### Test 2: Call Summary Access Controls

- **Objective:** Confirm that call summaries are only accessible to authorized parties
- **Steps:**
  1. Generate a call summary from a test client call.
  2. Verify only the call participants can access the summary.
  3. Verify the supervisor has appropriate oversight access.
  4. Confirm external callers do not receive the AI-generated summary.
- **Expected Result:** Call summaries are restricted to authorized internal users only.
- **Evidence:** Access permissions documentation for call summary storage.

### Test 3: DLP Enforcement on Call Transcripts

- **Objective:** Validate that DLP policies scan call transcripts for sensitive information
- **Steps:**
  1. Place a test call and verbally mention test sensitive data (test SSN, account number).
  2. Wait for transcription to complete.
  3. Verify DLP policies detect the sensitive information in the transcript.
  4. Confirm the appropriate DLP action is taken (notification, blocking).
- **Expected Result:** DLP detects sensitive information in call transcripts and takes configured action.
- **Evidence:** DLP incident report showing detection from the call transcript.

### Test 4: Call Queue Copilot Integration

- **Objective:** Verify that Copilot functions correctly for agents handling queue calls
- **Steps:**
  1. Route a test call through a configured call queue.
  2. Have an agent answer the call with Copilot enabled.
  3. Verify Copilot provides real-time assistance during the call.
  4. After the call, verify the summary is generated and accessible to the supervisor.
- **Expected Result:** Copilot assists agents during queue calls and generates summaries for supervisory review.
- **Evidence:** Agent experience screenshots and supervisor access to call summary.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Calling policy configuration | Teams Admin Center | Screenshot | With control documentation |
| Call summary samples | Teams Phone | Redacted screenshots | Per retention policy |
| DLP detection results | Purview DLP | CSV | 7 years |
| Queue configuration | Teams Admin Center | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110 | Phone communication supervision | Supports compliance with supervisory review of phone-based interactions |
| SEC 17a-4 | Communication record retention | Helps meet record retention for AI-summarized phone communications |
| FINRA 4511 | Books-and-records for communications | Supports record-keeping of AI-generated call summaries |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Teams Phone issues
- Proceed to [Control 4.4](../4.4/portal-walkthrough.md) for Viva Suite governance
