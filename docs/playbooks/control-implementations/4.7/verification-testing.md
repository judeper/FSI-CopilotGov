# Control 4.7: Copilot Feedback and Telemetry Data Governance — Verification & Testing

Test cases and evidence collection procedures for Copilot feedback and telemetry data governance.

## Test Cases

### Test 1: Diagnostic Data Level Configuration

- **Objective:** Verify that diagnostic data is set to the minimum required level
- **Steps:**
  1. Check the M365 Admin Center diagnostic data settings.
  2. Verify the setting is "Required diagnostic data" (not "Optional").
  3. Confirm the setting is enforced via Cloud Policy or Group Policy.
  4. Test that a user cannot override the diagnostic data level locally.
- **Expected Result:** Diagnostic data is set to "Required" and enforced by policy.
- **Evidence:** Admin Center screenshot and Group Policy/Cloud Policy configuration.

### Test 2: Feedback Collection Controls

- **Objective:** Confirm that Copilot feedback collection is configured per organizational policy
- **Steps:**
  1. As a Copilot user, submit a thumbs-up or thumbs-down feedback on a Copilot response.
  2. Search the audit log for the feedback event.
  3. Verify the feedback event is captured with appropriate metadata (no sensitive content).
  4. Confirm the feedback data does not include the full prompt or response content.
- **Expected Result:** Feedback is collected per policy with appropriate metadata and without sensitive content.
- **Evidence:** Audit log entry showing feedback event metadata.

### Test 3: Connected Experiences Configuration

- **Objective:** Validate that optional connected experiences are disabled for the regulated environment
- **Steps:**
  1. Verify connected experiences settings in the Admin Center.
  2. On a test workstation, open an Office application and check Settings > Privacy.
  3. Confirm optional connected experiences are disabled and grayed out (enforced by policy).
  4. Test that services relying on required connected experiences still function.
- **Expected Result:** Optional connected experiences are disabled by policy; required ones function normally.
- **Evidence:** Screenshots of Admin Center settings and client-side privacy settings.

### Test 4: Data Processing Agreement Currency

- **Objective:** Verify that the Microsoft DPA is current and reviewed
- **Steps:**
  1. Locate the current Microsoft DPA on file.
  2. Verify the DPA version is the most recent available from Microsoft.
  3. Confirm a review has been completed within the last 12 months.
  4. Verify the review addressed Copilot-specific data processing provisions.
- **Expected Result:** Current DPA on file, reviewed within 12 months, with Copilot provisions documented.
- **Evidence:** DPA document with review attestation.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Diagnostic data settings | Admin Center | Screenshot | With control documentation |
| Feedback audit log | Unified Audit Log | CSV | Per retention policy |
| Connected experiences config | Admin Center + Client | Screenshots | With control documentation |
| DPA review attestation | Legal/Privacy team | PDF | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| GLBA | Data handling and privacy | Supports compliance with customer data governance requirements |
| CCPA/CPRA | Data minimization | Helps meet data collection minimization requirements |
| FFIEC IT Handbook | Vendor data management | Supports governance of vendor data processing activities |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for telemetry governance issues
- Proceed to [Control 4.8](../4.8/portal-walkthrough.md) for cost allocation and license optimization
- Back to [Control 4.7](../../../controls/pillar-4-operations/4.7-feedback-telemetry.md)
