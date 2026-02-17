# Control 2.13: Plugin and Graph Connector Security — Verification & Testing

Test cases and evidence collection for validating plugin and connector security.

## Test Cases

### Test 1: Third-Party Plugin Block Verification

- **Objective:** Confirm third-party plugins are blocked by default
- **Steps:**
  1. As a standard Copilot user, attempt to install a third-party Teams app
  2. Verify the installation is blocked by the permission policy
  3. Verify the block event is logged
- **Expected Result:** Third-party plugin installation blocked
- **Evidence:** Block notification screenshot and audit log

### Test 2: Admin Consent Enforcement

- **Objective:** Verify user consent is disabled and admin consent is required
- **Steps:**
  1. Run Script 3 to verify consent policy settings
  2. As a standard user, access an app requiring consent — verify admin consent is required
  3. Submit an admin consent request and verify it routes correctly
- **Expected Result:** Admin consent required for all app permission grants
- **Evidence:** Consent policy configuration and test results

### Test 3: Graph Connector ACL Verification

- **Objective:** Confirm Graph connector ACLs correctly restrict content access
- **Steps:**
  1. For each active connector, verify the ACL mapping configuration
  2. Test with a user who should not have access — verify content is not returned by Copilot
  3. Test with an authorized user — verify content is returned
- **Expected Result:** Connector ACLs enforce access restrictions correctly
- **Evidence:** Access test results for authorized and unauthorized users

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Plugin permission audit | CSV | Compliance evidence repository | 7 years |
| Connector security audit | CSV | Compliance evidence repository | 7 years |
| Consent policy verification | Screenshot | Compliance evidence repository | 7 years |
| ACL test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| OCC Heightened Standards | Third-party risk management | Plugin security supports compliance with third-party technology risk requirements |
| FINRA Rule 3110 | Technology oversight | Plugin governance supports compliance with supervisory technology controls |
| NIST CSF | PR.IP-1 Baseline configuration | Plugin restrictions establish and maintain secure baseline configurations |
