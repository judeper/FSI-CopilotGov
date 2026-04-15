# Control 4.9: Incident Reporting and Root Cause Analysis — Verification & Testing

Test cases and evidence collection procedures for Copilot incident reporting and root cause analysis.

## Test Cases

### Test 1: Alert Policy Trigger Verification

- **Objective:** Confirm that Copilot incident alert policies trigger correctly
- **Steps:**
  1. Review the configured alert policies for Copilot incidents.
  2. Simulate a condition that should trigger an alert (e.g., DLP violation in a Copilot interaction).
  3. Verify the alert is generated within the expected timeframe.
  4. Confirm the alert notification reaches the designated recipients.
- **Expected Result:** Alert triggers within the configured timeframe and notifications are delivered.
- **Evidence:** Alert notification email and alert entry in the Purview alerts dashboard.

### Test 2: Incident Response Workflow Execution

- **Objective:** Validate the end-to-end incident response workflow for a Copilot incident
- **Steps:**
  1. Simulate a Copilot-related incident scenario (e.g., Copilot surfacing restricted content).
  2. Follow the incident response workflow from detection through containment and resolution.
  3. Complete the incident report template with all required sections.
  4. Verify the RCA is completed within the defined timeline.
- **Expected Result:** Incident response workflow executes smoothly with all steps documented.
- **Evidence:** Completed incident report with timeline and RCA documentation.

### Test 3: Regulatory Notification Decision Process

- **Objective:** Verify that the regulatory notification assessment process functions correctly
- **Steps:**
  1. Create a hypothetical scenario involving customer NPI exposure via Copilot.
  2. Walk through the regulatory notification assessment criteria.
  3. Verify the decision matrix correctly identifies applicable notification requirements.
  4. Confirm the CCO approval workflow for notification decisions is functional.
- **Expected Result:** Notification assessment correctly identifies regulatory obligations and approval workflow functions.
- **Evidence:** Documented assessment walkthrough with decision rationale.

### Test 4: Anomaly Detection Effectiveness

- **Objective:** Confirm that anomaly detection scripts correctly identify unusual patterns
- **Steps:**
  1. Run the anomaly detection script against the current audit log data.
  2. Review flagged users to determine if the anomalies are genuine.
  3. Verify the threshold settings are appropriate for the organization's usage patterns.
  4. Adjust thresholds if false positive rate is too high or false negatives are observed.
- **Expected Result:** Anomaly detection identifies genuine unusual patterns with acceptable false positive rates.
- **Evidence:** Anomaly detection report with validation notes.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Alert policy configuration | Purview portal | Screenshot | With control documentation |
| Incident response test report | Simulation exercise | Document | 7 years |
| RCA template and completed examples | Incident management | PDF | 7 years |
| Anomaly detection reports | PowerShell | CSV | 1 year |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 4530 | Incident reporting to FINRA | Supports compliance with event reporting obligations |
| SEC Reg S-P | Breach notification | Helps meet breach notification requirements for NPI exposure |
| FFIEC IT Handbook | Incident response and RCA | Supports IT incident management and root cause analysis requirements |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for incident management issues
- Proceed to [Control 4.10](../4.10/portal-walkthrough.md) for business continuity
- Back to [Control 4.9](../../../controls/pillar-4-operations/4.9-incident-reporting.md)
