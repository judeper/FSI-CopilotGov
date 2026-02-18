# Control 2.1: DLP Policies for M365 Copilot Interactions — Verification & Testing

Test cases and evidence collection for validating DLP policy effectiveness for Copilot. This playbook covers verification for both DLP policy types (label-based response blocking and SIT-based prompt blocking) and the default Microsoft-deployed policy.

## Test Cases

### Test 1: DLP Policy Activation Verification (Both Policy Types)

- **Objective:** Confirm both Copilot DLP policy types are active and properly configured
- **Steps:**
  1. Run Script 3 to list all Copilot DLP policies
  2. Verify at least one label-based response blocking policy exists and is in the expected mode (Test or Enforce)
  3. Verify at least one SIT-based prompt blocking policy exists and is in the expected mode
  4. Locate the Microsoft-deployed default Copilot DLP policy (simulation mode) and confirm it is present
  5. Confirm policy locations include Microsoft 365 Copilot as the monitored location
  6. Verify rule conditions match the approved DLP strategy for each policy type
- **Expected Result:** Both policy types and the default policy are present; each is in the expected mode
- **Evidence:** DLP policy configuration export showing all three policies

### Test 2: Label-Based Response Blocking (Type 1 Verification)

- **Objective:** Verify the label-based policy blocks Copilot from surfacing Highly Confidential content
- **Steps:**
  1. Upload a test document labeled "Highly Confidential" to a SharePoint site accessible to a test user
  2. As the test user, ask Copilot to summarize or reference the test document
  3. Verify Copilot does not include the document content in its response
  4. Confirm a DLP policy tip is displayed (or block action fires in enforcement mode)
  5. Confirm the match event is logged in the DLP incident report
  6. Clean up test data after verification
- **Expected Result:** Copilot is blocked from surfacing the Highly Confidential document; event is logged
- **Evidence:** Screenshot of Copilot response showing block/tip, and DLP incident record

### Test 3: SIT-Based Prompt Blocking (Type 2 Verification)

- **Objective:** Verify the SIT-based policy blocks Copilot when the user types sensitive data in a prompt
- **Steps:**
  1. With the SIT-based prompt blocking policy active, type a prompt containing a test SSN pattern (000-00-0000) directly into Copilot
  2. Verify Copilot does not process the request — Copilot should be blocked from responding
  3. Verify the user sees a policy tip explaining the prompt was blocked
  4. Confirm the block event is recorded in DLP incident reports
  5. Verify the enforcement happens on the prompt side (before Copilot retrieves any content)
- **Expected Result:** Copilot is blocked from responding to a prompt containing a sensitive data pattern
- **Evidence:** Copilot response showing blocked prompt and DLP incident record

### Test 4: Default Policy Simulation Mode Review

- **Objective:** Validate that the Microsoft-deployed default Copilot DLP policy is capturing expected matches
- **Steps:**
  1. Access the default policy via MAC > Copilot > Overview > Security tab or Purview > DLP > Policies
  2. Review simulation mode match data for the past 14+ days
  3. Classify a sample of 20 matches as true positive or false positive
  4. Calculate the false positive rate
  5. If false positive rate is below 10%, document readiness to transition from simulation to enforcement
- **Expected Result:** Simulation data captured; false positive rate documented; enforcement readiness assessed
- **Evidence:** Simulation match data export and false positive analysis

### Test 5: Block Action Enforcement

- **Objective:** Confirm DLP blocking actions prevent sensitive data from being exposed through Copilot (both policy types)
- **Steps:**
  1. With both DLP policies in enforcement mode, repeat the label-based test and the SIT-based test
  2. Verify Copilot does not include the sensitive data in responses (Type 1) and does not process sensitive prompts (Type 2)
  3. Verify users receive notifications about the blocked content or prompt
  4. Confirm block events are recorded separately by policy type in DLP incident reports
- **Expected Result:** Both policy types block as designed; events recorded
- **Evidence:** Copilot responses showing blocked content and DLP incident records for each policy type

### Test 6: Edge Browser DLP Coverage

- **Objective:** Verify DLP policies apply to Copilot interactions accessed through Microsoft Edge browser
- **Steps:**
  1. Access Copilot via Microsoft Edge (browser-based access, e.g., m365copilot.com)
  2. Type a prompt containing a test SSN pattern (000-00-0000)
  3. Verify the Edge browser DLP policy triggers (audit or block)
  4. Confirm the event appears in DLP incident reports attributed to the Endpoint DLP / Edge channel
- **Expected Result:** Edge browser DLP applies to browser-based Copilot interactions
- **Evidence:** DLP match event attributed to Edge/Endpoint DLP channel

### Test 7: Override and Justification Flow

- **Objective:** Verify override mechanisms work correctly for permitted override scenarios
- **Steps:**
  1. Configure a test DLP rule with override allowed (business justification required)
  2. Trigger the DLP policy with medium-sensitivity test content
  3. Attempt to override with a business justification
  4. Verify the justification is recorded in the audit log
  5. Verify the override is granted and content is accessible
- **Expected Result:** Override flow works correctly with justification recorded
- **Evidence:** Override audit log entry with justification text

### Test 8: False Positive Rate Assessment

- **Objective:** Evaluate the DLP policy false positive rate to validate confidence level settings
- **Steps:**
  1. Run Script 4 to export DLP incidents from the past 30 days
  2. Review a sample of 50 incidents and classify as true positive or false positive (assess each policy type separately)
  3. Calculate the false positive rate per policy type
  4. If rate exceeds 20% for either type, adjust confidence levels or SIT patterns
- **Expected Result:** False positive rate below 20% for each policy type
- **Evidence:** Incident classification analysis with false positive calculation per policy type

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| DLP policy configuration export (both types + default) | CSV/JSON | Compliance evidence repository | 7 years |
| Label-based response blocking test results | PDF with screenshots | Compliance evidence repository | 7 years |
| SIT-based prompt blocking test results | PDF with screenshots | Compliance evidence repository | 7 years |
| Default policy simulation review | PDF with match data | Compliance evidence repository | 7 years |
| Edge browser DLP test results | PDF with screenshots | Compliance evidence repository | 7 years |
| DLP incident reports | CSV | Compliance evidence repository | 7 years |
| False positive analysis (per policy type) | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| SEC Regulation S-P (17 CFR §248, amended Dec 3, 2025) | Customer NPI safeguards covering AI interaction surfaces | SIT-based prompt blocking (Type 2) addresses the requirement that customer information safeguards extend to AI interaction surfaces |
| FINRA Rule 3110 | Supervisory data controls | Both DLP policy types support compliance with supervisory requirements for data protection in AI interactions |
| GLBA Safeguards Rule | Technical safeguards | Both DLP types provide technical controls — Type 1 at the response layer, Type 2 at the prompt layer |
| PCI DSS | Cardholder data protection | SIT-based prompt blocking prevents credit card data from entering Copilot prompts; label-based blocking prevents labeled cardholder data from being surfaced in responses |
