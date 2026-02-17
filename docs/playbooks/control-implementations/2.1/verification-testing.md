# Control 2.1: DLP Policies for M365 Copilot Interactions — Verification & Testing

Test cases and evidence collection for validating DLP policy effectiveness for Copilot.

## Test Cases

### Test 1: DLP Policy Activation Verification

- **Objective:** Confirm all Copilot DLP policies are active and properly configured
- **Steps:**
  1. Run PowerShell Script 2 to list all Copilot DLP policies
  2. Verify each policy is in the expected mode (Test or Enforce)
  3. Confirm policy locations include Copilot-relevant workloads
  4. Verify rule conditions match the approved DLP strategy
- **Expected Result:** All planned DLP policies are active with correct configurations
- **Evidence:** DLP policy configuration export

### Test 2: Sensitive Data Detection in Copilot

- **Objective:** Verify DLP detects sensitive data when referenced in Copilot interactions
- **Steps:**
  1. Create a test document containing sample sensitive data (test SSN format: 000-00-0000)
  2. Store the test document in a SharePoint site accessible to a test user
  3. As the test user, ask Copilot to summarize or reference the test document
  4. Verify the DLP policy tip is displayed and the interaction is logged
  5. Clean up test data after verification
- **Expected Result:** DLP detects sensitive data and displays policy tip
- **Evidence:** Screenshot of DLP policy tip and audit log entry

### Test 3: Block Action Enforcement

- **Objective:** Confirm DLP blocking actions prevent sensitive data from being exposed through Copilot
- **Steps:**
  1. With the DLP policy in enforcement mode, repeat the sensitive data test
  2. Verify Copilot does not include the sensitive data in its response
  3. Verify the user receives a notification about the blocked content
  4. Confirm the block event is recorded in DLP incident reports
- **Expected Result:** Sensitive data is blocked from Copilot responses
- **Evidence:** Copilot response showing blocked content and DLP incident record

### Test 4: Override and Justification Flow

- **Objective:** Verify override mechanisms work correctly for permitted override scenarios
- **Steps:**
  1. Configure a test DLP rule with override allowed (business justification required)
  2. Trigger the DLP policy with medium-sensitivity test content
  3. Attempt to override with a business justification
  4. Verify the justification is recorded in the audit log
  5. Verify the override is granted and content is accessible
- **Expected Result:** Override flow works correctly with justification recorded
- **Evidence:** Override audit log entry with justification text

### Test 5: False Positive Rate Assessment

- **Objective:** Evaluate the DLP policy false positive rate to validate confidence level settings
- **Steps:**
  1. Run Script 3 to export DLP incidents from the past 30 days
  2. Review a sample of 50 incidents and classify as true positive or false positive
  3. Calculate the false positive rate
  4. If rate exceeds 20%, adjust confidence levels or sensitive info type patterns
- **Expected Result:** False positive rate below 20%
- **Evidence:** Incident classification analysis with false positive calculation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| DLP policy configuration export | CSV/JSON | Compliance evidence repository | 7 years |
| DLP test results | PDF with screenshots | Compliance evidence repository | 7 years |
| DLP incident reports | CSV | Compliance evidence repository | 7 years |
| False positive analysis | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory data controls | DLP policies support compliance with supervisory requirements for data protection in AI interactions |
| SEC Regulation S-P | Customer NPI protection | DLP helps prevent AI from exposing non-public personal information |
| GLBA Safeguards Rule | Technical safeguards | DLP provides technical controls for data protection in AI workloads |
| PCI DSS | Cardholder data protection | DLP helps prevent credit card data exposure through Copilot |
