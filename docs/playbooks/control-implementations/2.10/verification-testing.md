# Control 2.10: Insider Risk Detection for Copilot Usage — Verification & Testing

Test cases and evidence collection for validating insider risk detection for Copilot.

## Test Cases

### Test 1: Insider Risk Policy Activation

- **Objective:** Confirm insider risk policies for Copilot are active and processing
- **Steps:**
  1. Navigate to Purview > Insider Risk Management > Policies
  2. Verify Copilot-related policies show "Active" status
  3. Run Script 1 to confirm policy configuration
  4. Check that policy indicators include Copilot-specific signals
- **Expected Result:** All configured insider risk policies are active
- **Evidence:** Policy status screenshot and PowerShell output

### Test 2: Anomaly Detection Functionality

- **Objective:** Verify the system detects anomalous Copilot usage patterns
- **Steps:**
  1. Generate above-normal Copilot activity volume with a test account
  2. Wait for the insider risk processing cycle (24-48 hours)
  3. Check for risk alerts or elevated risk scores on the test account
  4. Verify the anomaly is captured in the insider risk dashboard
- **Expected Result:** Anomalous activity generates a risk signal
- **Evidence:** Insider risk alert or risk score increase for test account

### Test 3: Alert Triage Workflow

- **Objective:** Verify the alert triage process functions correctly
- **Steps:**
  1. Identify an active insider risk alert (or create one via testing)
  2. Verify the alert is routed to the assigned investigator
  3. Complete the triage workflow: review, classify, and take action
  4. Verify the triage is documented in the case management system
- **Expected Result:** Alert is triaged per the documented workflow
- **Evidence:** Completed triage record with investigator actions

### Test 4: Privacy Controls Verification

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
| Alert and triage records | PDF | Compliance evidence repository | 7 years |
| Usage anomaly reports | CSV | Compliance evidence repository | 7 years |
| Privacy control verification | Screenshot | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory systems | Insider risk detection supports compliance with supervisory monitoring requirements |
| SEC Regulation S-P | Safeguards for customer data | Detecting data theft patterns helps meet customer data protection obligations |
| Bank Secrecy Act | Suspicious activity monitoring | Copilot usage monitoring supports compliance with suspicious activity reporting |
| NIST CSF | DE.AE-1 Anomaly detection | Insider risk supports compliance with anomaly detection requirements |
