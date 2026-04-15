# Control 2.10: Insider Risk Detection for Copilot Usage — Verification & Testing

Test cases and evidence collection for validating insider risk detection for Copilot and agent activity.

## Test Cases

### Test 1: Insider Risk Policy Activation

- **Objective:** Confirm insider risk policies for Copilot are active and processing
- **Steps:**
  1. Navigate to Microsoft Purview > Insider Risk Management > Policies
  2. Verify Copilot-related policies show "Active" status
  3. Run Script 1 to confirm policy configuration
  4. Check that policy indicators include both Copilot-specific signals and AI usage indicators
- **Expected Result:** All configured insider risk policies are active with AI usage indicators enabled
- **Evidence:** Policy status screenshot and PowerShell output

### Test 2: Risky Agents Policy Verification

- **Objective:** Confirm the Risky Agents policy is active and covers all deployed agents
- **Steps:**
  1. Navigate to Microsoft Purview > Insider Risk Management > Policies
  2. Locate the auto-deployed Risky Agents policy
  3. Verify the policy scope includes all deployed Copilot Studio and Azure AI Foundry agents
  4. Confirm alert routing is configured to reach both compliance and agent deployment owners
  5. Review the policy thresholds for FSI appropriateness
- **Expected Result:** Risky Agents policy is active, scoped correctly, and alert routing is configured
- **Evidence:** Policy configuration screenshot; alert routing configuration

### Test 3: AI Usage Indicator Functionality

- **Objective:** Verify AI usage indicators are active and producing signals
- **Steps:**
  1. Navigate to Microsoft Purview > Insider Risk Management > Settings > Policy indicators
  2. Confirm AI usage indicator category is enabled
  3. Generate above-normal Copilot and agent activity volume with a test account
  4. Wait for the processing cycle (24-48 hours)
  5. Check the test user's risk timeline for AI usage indicator signals
- **Expected Result:** AI usage indicators appear in the risk timeline for elevated-activity accounts
- **Evidence:** IRM risk timeline showing AI usage indicator signals

### Test 4: Anomaly Detection Functionality

- **Objective:** Verify the system detects anomalous Copilot usage patterns
- **Steps:**
  1. Generate above-normal Copilot activity volume with a test account
  2. Wait for the insider risk processing cycle (24-48 hours)
  3. Check for risk alerts or elevated risk scores on the test account
  4. Verify the anomaly is captured in the insider risk dashboard
- **Expected Result:** Anomalous activity generates a risk signal
- **Evidence:** Insider risk alert or risk score increase for test account

### Test 5: Data Risk Graph Accessibility

- **Objective:** Confirm data risk graphs are available and integrated into investigation procedures
- **Steps:**
  1. Navigate to Microsoft Purview > Insider Risk Management > Investigations
  2. Access the Data risk graphs view
  3. Select a time window and verify graph data is loading
  4. Confirm the graph includes Copilot and agent interaction data
  5. Verify investigators know to include graph review in the standard investigation procedure
- **Expected Result:** Data risk graphs accessible and displaying Copilot/agent interaction data
- **Evidence:** Screenshot of data risk graph showing activity data

### Test 6: IRM Triage Agent Operation

- **Objective:** Verify the Triage Agent is functioning and producing useful context summaries
- **Steps:**
  1. Navigate to Microsoft Purview > Insider Risk Management > Alerts
  2. Select an active alert and review the Triage Agent context summary
  3. Verify the summary includes: activity type detected, data involved, user risk history context
  4. Confirm the alert severity categorization is reasonable
  5. For Regulated tier: verify that the human-in-the-loop workflow requires investigator confirmation before alert dismissal
- **Expected Result:** Triage Agent produces actionable context summaries; severity categorizations are appropriate
- **Evidence:** Screenshot of Triage Agent context summary for an active alert

### Test 7: Alert Triage Workflow

- **Objective:** Verify the alert triage process functions correctly
- **Steps:**
  1. Identify an active insider risk alert (or create one via testing)
  2. Verify the alert is routed to the assigned investigator
  3. Complete the triage workflow: review Triage Agent context, classify, and take action
  4. For agent risk alerts: verify routing reaches both compliance and agent deployment owners
  5. Verify the triage is documented in the case management system
- **Expected Result:** Alert is triaged per the documented workflow with Triage Agent context reviewed
- **Evidence:** Completed triage record with investigator actions

### Test 8: Privacy Controls Verification

- **Objective:** Confirm pseudonymization and privacy controls are active
- **Steps:**
  1. Navigate to Insider Risk Management as an investigator
  2. Verify user identities are pseudonymized in the initial alert view
  3. Verify de-pseudonymization requires appropriate authorization
  4. Confirm privacy settings match the documented configuration
- **Expected Result:** Privacy controls function as configured
- **Evidence:** Screenshot showing pseudonymized user identities

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Insider risk policy configuration | PDF | Compliance evidence repository | 7 years |
| Risky Agents policy configuration | PDF | Compliance evidence repository | 7 years |
| AI usage indicator configuration | Screenshot | Compliance evidence repository | 7 years |
| Triage Agent model inventory entry | PDF | Model risk management repository | 7 years |
| Alert and triage records | PDF | Compliance evidence repository | 7 years |
| Usage anomaly reports | CSV | Compliance evidence repository | 7 years |
| Privacy control verification | Screenshot | Compliance evidence repository | 7 years |
| Data risk graph samples | Screenshot | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory systems | Insider risk detection supports compliance with supervisory monitoring requirements; Risky Agents addresses the 2026 FINRA Oversight Report requirement for AI agent supervisory controls |
| FINRA Rule 3120 | Testing supervisory procedures | IRM alert generation and investigation workflow provide testable supervisory procedures for Copilot and agent oversight |
| FINRA 2026 Oversight Report (GenAI) | Agentic AI supervisory controls | Risky Agents policy and AI usage indicators directly address FINRA's 2026 requirement for supervisory systems covering AI workflow engines |
| OCC Bulletin 2025-26 | Model risk management | IRM Triage Agent documented as model per SR 11-7; proportionate AI-assisted governance |
| SEC Regulation S-P | Safeguards for customer data | Detecting data theft patterns helps meet customer data protection obligations |
| GLBA 501(b) | Monitoring and testing safeguards | IRM provides ongoing monitoring evidence and quarterly testing capability |
| Bank Secrecy Act | Suspicious activity monitoring | Copilot and agent usage monitoring supports compliance with suspicious activity reporting |
| NIST CSF | DE.AE-1 Anomaly detection | Insider risk supports compliance with anomaly detection requirements |
- Back to [Control 2.10](../../../controls/pillar-2-security/2.10-insider-risk-detection.md)
