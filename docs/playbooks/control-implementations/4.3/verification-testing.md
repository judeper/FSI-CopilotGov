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

### Test 3: Transcript/Artifact Compliance Coverage

- **Objective:** Validate whether tenant DLP, retention, eDiscovery, or Communication Compliance policies cover call transcripts and Copilot call artifacts
- **Steps:**
  1. Place a test call and verbally mention test sensitive data (test SSN, account number).
  2. Wait for transcription to complete.
  3. Verify which compliance policies detect the sensitive information in the transcript or artifact.
  4. Document unsupported artifact types as gaps rather than assuming DLP coverage.
- **Expected Result:** Tenant evidence shows which transcript/artifact types are covered and which require compensating controls.
- **Evidence:** Policy match, eDiscovery result, or documented unsupported-path finding.

### Test 4: Teams Phone Agent / Queue Scope Verification

- **Objective:** Verify ordinary queue-agent policy inheritance and, where preview is enabled, Teams Phone Agent behavior
- **Steps:**
  1. Route a test call through a configured call queue.
  2. Have an agent answer the call and verify the agent's calling policy controls Teams Phone Copilot availability.
  3. If using Teams Phone Agent, verify the voice-agent handoff, tags, escalation path, and artifact capture.
  4. After the call, verify which summaries/artifacts are generated and who can access them.
- **Expected Result:** Queue behavior, Teams Phone Copilot availability, and any Teams Phone Agent artifacts match the approved tenant design.
- **Evidence:** Agent experience screenshots, policy export, and artifact access evidence.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Calling policy configuration | Teams Admin Center | Screenshot | With control documentation |
| Call summary samples | Teams Phone | Redacted screenshots | Per retention policy |
| Compliance coverage results | Purview / Teams / eDiscovery | CSV or screenshot | Per firm-approved records schedule |
| Queue configuration | Teams Admin Center | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110 | Phone communication supervision | Supports compliance with supervisory review of phone-based interactions |
| SEC 17a-4 | Communication record retention | Can support firm-defined controls for record retention for AI-summarized phone communications |
| FINRA 4511 | Books-and-records for communications | Supports record-keeping of AI-generated call summaries |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for Teams Phone issues
- Proceed to [Control 4.4](../4.4/portal-walkthrough.md) for Viva Suite governance
- Back to [Control 4.3](../../../controls/pillar-4-operations/4.3-teams-phone-queues.md)
