# Control 2.3: Conditional Access Policies for Copilot Workloads — Verification & Testing

Test cases and evidence collection for validating Conditional Access policies for Copilot.

## Test Cases

### Test 1: Compliant Device Access Verification

- **Objective:** Confirm Copilot is accessible from compliant managed devices
- **Steps:**
  1. Sign in from a compliant, Intune-managed device
  2. Access a Copilot-enabled Office application
  3. Verify Copilot is fully functional
  4. Check the sign-in log confirms device compliance was evaluated
- **Expected Result:** Full Copilot access from compliant device with compliance check logged
- **Evidence:** Sign-in log showing compliant device access

### Test 2: Non-Compliant Device Block Verification

- **Objective:** Confirm Copilot access is blocked from non-compliant or unmanaged devices
- **Steps:**
  1. Attempt to access a Copilot-enabled application from an unmanaged device
  2. Verify the Conditional Access policy blocks access or requires additional steps
  3. Confirm the appropriate error message is displayed
  4. Verify the blocked access attempt is logged
- **Expected Result:** Access blocked with appropriate error message displayed
- **Evidence:** Screenshot of access denial and sign-in log showing block reason

### Test 3: MFA Enforcement

- **Objective:** Verify MFA is required for all Copilot access
- **Steps:**
  1. Clear all MFA tokens for a test user
  2. Attempt to access Copilot from a compliant device
  3. Verify MFA prompt appears
  4. Complete MFA and verify Copilot access is granted
- **Expected Result:** MFA is required and enforced before Copilot access
- **Evidence:** Sign-in log showing MFA requirement and satisfaction

### Test 4: Session Control Enforcement

- **Objective:** Verify session timeout and re-authentication requirements
- **Steps:**
  1. Sign in and access Copilot
  2. Wait for the configured session timeout period (or simulate expiry)
  3. Verify re-authentication is prompted
  4. Confirm session controls are logged correctly
- **Expected Result:** Session timeout enforces re-authentication as configured
- **Evidence:** Sign-in logs showing session control enforcement

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Conditional Access policy export | CSV/JSON | Compliance evidence repository | 7 years |
| Sign-in log samples | CSV | Compliance evidence repository | 7 years |
| Access denial test results | PDF with screenshots | Compliance evidence repository | 7 years |
| MFA enforcement verification | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FFIEC Authentication Guidance | Strong authentication | MFA requirement supports compliance with authentication guidance |
| NIST SP 800-63 | Authentication assurance levels | Conditional Access helps meet assurance level requirements |
| SEC Regulation S-P | Access controls | Device and authentication controls support compliance with access control obligations |
| PCI DSS Req 8 | Identify and authenticate access | MFA and device compliance help meet authentication requirements |
