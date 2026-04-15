# Control 2.3: Conditional Access Policies for Copilot Workloads — Verification & Testing

Test cases and evidence collection for validating Conditional Access policies for Copilot.

## Test Cases

### Test 1: App ID Accuracy Verification

- **Objective:** Confirm all CA policies targeting Copilot reference the correct Enterprise Copilot Platform App ID
- **Steps:**
  1. Run Script 1 (Copilot App ID Audit) from the PowerShell playbook
  2. Review output for any policy referencing an incorrect Copilot app ID
  3. Confirm no policies use the wrong app ID segment (`7ef4-4c2f` is incorrect; `7ef8-4ec0` is correct)
  4. Verify the correct ID `fb8d773d-7ef8-4ec0-a117-179f88add510` appears in all Copilot-targeting policies
- **Expected Result:** All Copilot CA policies reference only the correct app ID
- **Evidence:** PowerShell output showing correct app ID across all policies

### Test 2: May 2026 Enforcement Readiness Check

- **Objective:** Verify CA policies are compliant with the May 13, 2026 enforcement change
- **Steps:**
  1. Run Script 1 to identify "All resources" policies with exclusions
  2. For each identified policy, deploy in report-only mode to assess enforcement impact
  3. Review the report-only results for unexpected user impact
  4. Confirm remediation plan is documented
- **Expected Result:** No active "All resources + Copilot exclusion" policies at enforcement date
- **Evidence:** Report-only evaluation logs; remediation documentation with completion date

### Test 3: Compliant Device Access Verification

- **Objective:** Confirm Copilot is accessible from compliant managed devices
- **Steps:**
  1. Sign in from a compliant, Intune-managed device
  2. Access a Copilot-enabled Office application
  3. Verify Copilot is fully functional
  4. Check the sign-in log confirms device compliance was evaluated
- **Expected Result:** Full Copilot access from compliant device with compliance check logged
- **Evidence:** Sign-in log showing compliant device access

### Test 4: Non-Compliant Device Block Verification

- **Objective:** Confirm Copilot access is blocked from non-compliant or unmanaged devices
- **Steps:**
  1. Attempt to access a Copilot-enabled application from an unmanaged device
  2. Verify the Conditional Access policy blocks access or requires additional steps
  3. Confirm the appropriate error message is displayed
  4. Verify the blocked access attempt is logged
- **Expected Result:** Access blocked with appropriate error message displayed
- **Evidence:** Screenshot of access denial and sign-in log showing block reason

### Test 5: MFA Enforcement

- **Objective:** Verify MFA is required for all Copilot access
- **Steps:**
  1. Clear all MFA tokens for a test user
  2. Attempt to access Copilot from a compliant device
  3. Verify MFA prompt appears
  4. Complete MFA and verify Copilot access is granted
- **Expected Result:** MFA is required and enforced before Copilot access
- **Evidence:** Sign-in log showing MFA requirement and satisfaction

### Test 6: Session Control Enforcement

- **Objective:** Verify session timeout and re-authentication requirements
- **Steps:**
  1. Sign in and access Copilot
  2. Wait for the configured session timeout period (or simulate expiry)
  3. Verify re-authentication is prompted
  4. Confirm session controls are logged correctly
- **Expected Result:** Session timeout enforces re-authentication as configured
- **Evidence:** Sign-in logs showing session control enforcement

### Test 7: Adaptive Protection Integration

- **Objective:** Verify IRM Adaptive Protection triggers CA policy enforcement for at-risk users
- **Steps:**
  1. Confirm Adaptive Protection is enabled in Microsoft Purview IRM
  2. Elevate a test user's IRM risk level (or observe a genuine risk event in test environment)
  3. Attempt Copilot access as the test user
  4. Verify the CA policy responds to the elevated IRM risk level (block or step-up MFA)
  5. Lower the risk level and verify access is restored according to policy
- **Expected Result:** CA policy dynamically adjusts based on IRM risk signals
- **Evidence:** IRM risk level change log; CA sign-in log showing policy enforcement for at-risk user

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| App ID audit output | Text/CSV | Compliance evidence repository | 7 years |
| May 2026 remediation documentation | PDF | Compliance evidence repository | 7 years |
| Conditional Access policy export | CSV/JSON | Compliance evidence repository | 7 years |
| Sign-in log samples | CSV | Compliance evidence repository | 7 years |
| Access denial test results | PDF with screenshots | Compliance evidence repository | 7 years |
| MFA enforcement verification | PDF | Compliance evidence repository | 7 years |
| Adaptive Protection integration test | PDF with screenshots | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| NYDFS Part 500 §500.12 | MFA for external network access | MFA requirement ensures Copilot access from outside corporate network requires MFA; May 2026 enforcement closes the "All resources + exclusion" bypass path |
| FFIEC Authentication Guidance | Strong authentication | MFA requirement supports compliance with authentication guidance |
| NIST SP 800-63 | Authentication assurance levels | Conditional Access helps meet assurance level requirements |
| SEC Regulation S-P | Access controls | Device and authentication controls support compliance with access control obligations |
| PCI DSS Req 8 | Identify and authenticate access | MFA and device compliance help meet authentication requirements |
- Back to [Control 2.3](../../../controls/pillar-2-security/2.3-conditional-access-policies.md)
