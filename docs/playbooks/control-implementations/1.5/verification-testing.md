# Control 1.5: Sensitivity Label Taxonomy Review — Verification & Testing

Test cases and evidence collection for validating the sensitivity label taxonomy readiness for Copilot.

## Test Cases

### Test 1: Taxonomy Completeness

- **Objective:** Verify the label taxonomy covers all required classification levels for FSI
- **Steps:**
  1. Export the current taxonomy using PowerShell Script 1
  2. Verify the hierarchy includes at minimum: Public, General, Confidential, Highly Confidential
  3. Confirm sub-labels exist for FSI-specific data types (client data, financial reports, trading data)
  4. Verify each label has a clear description and user tooltip
- **Expected Result:** Taxonomy covers all FSI data classification requirements with clear descriptions
- **Evidence:** Taxonomy export CSV with governance committee review notes

### Test 2: Label Policy Coverage

- **Objective:** Confirm all Copilot-licensed users have access to the full label taxonomy
- **Steps:**
  1. Run PowerShell Script 2 to export label policies
  2. Cross-reference policy scope with the list of Copilot-licensed users
  3. Verify no Copilot users are excluded from label policies
  4. Confirm default label is configured for each applicable policy
- **Expected Result:** 100% of Copilot-licensed users are covered by label policies
- **Evidence:** Policy coverage cross-reference report

### Test 3: Auto-Labeling Effectiveness

- **Objective:** Verify auto-labeling policies correctly identify and label FSI sensitive content
- **Steps:**
  1. Create test documents containing known sensitive data patterns (sample account numbers, SSN patterns)
  2. Store test documents in a monitored SharePoint location
  3. Wait for auto-labeling processing (24-48 hours)
  4. Verify the correct sensitivity label was applied to each test document
  5. Clean up test documents after verification
- **Expected Result:** Auto-labeling correctly identifies and labels test documents with appropriate sensitivity levels
- **Evidence:** Before and after screenshots of test documents showing label application

### Test 4: Mandatory Labeling Enforcement

- **Objective:** Verify that mandatory labeling is enforced for Copilot users
- **Steps:**
  1. Sign in as a Copilot-licensed user subject to mandatory labeling
  2. Create a new Word document and attempt to save without applying a label
  3. Verify the system prompts for label selection before saving
  4. Confirm the user cannot bypass the labeling requirement
- **Expected Result:** Users cannot save documents without selecting a sensitivity label
- **Evidence:** Screenshot of mandatory labeling prompt

### Test 5: Label Priority and Override Behavior

- **Objective:** Verify label priority order and downgrade justification requirements
- **Steps:**
  1. Apply a "Confidential" label to a test document
  2. Attempt to downgrade the label to "General"
  3. Verify the system requires a justification for the downgrade
  4. Confirm the justification is logged in the audit trail
- **Expected Result:** Label downgrades require justification and are audited
- **Evidence:** Justification prompt screenshot and audit log entry

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Label taxonomy export | CSV | Compliance evidence repository | 7 years |
| Label policy coverage report | CSV | Compliance evidence repository | 7 years |
| Auto-labeling test results | PDF | Compliance evidence repository | 7 years |
| Mandatory labeling verification | Screenshots | Compliance evidence repository | 7 years |
| Governance committee review minutes | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Information classification | Label taxonomy supports compliance with supervisory information classification |
| SEC Regulation S-P | Customer information categories | Sensitivity labels help classify customer NPI appropriately |
| GLBA Safeguards Rule | Data classification | Taxonomy provides the classification foundation for safeguards implementation |
| NIST CSF | PR.DS-1 Data classification | Sensitivity labels support data-at-rest and data-in-use classification |
