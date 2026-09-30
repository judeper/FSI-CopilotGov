# Control 1.4: Semantic Index Governance — Verification & Testing

Test cases and evidence collection for validating Semantic Index governance controls.

## Test Cases

### Test 1: Index Scope Configuration Verification

- **Objective:** Confirm the documented searchable/discoverable scope matches governance-approved configuration
- **Steps:**
  1. Review current SharePoint site searchability, RCD state, and any legacy RSS configuration
  2. Compare against the documented governance decision for site inclusion and exclusion
  3. Verify that sites marked for Copilot exclusion are using the intended control (RCD, RSS, or searchability off)
  4. Confirm settings have not been modified since the last governance review
- **Expected Result:** Searchability and discoverability controls exactly match governance-approved configuration
- **Evidence:** Admin center screenshots and configuration export

### Test 2: Sensitivity Label Enforcement in Index

- **Objective:** Verify that sensitivity labels and access controls affect Copilot retrieval behavior as configured
- **Steps:**
  1. Create a test document with a "Highly Confidential" sensitivity label
  2. Store the document in a SharePoint site included in the index scope
  3. As a user without access to Highly Confidential content, query Copilot for the test document content
  4. Verify Copilot does not surface the protected content to the unauthorized user because access enforcement and policy controls are working
  5. As an authorized user, verify Copilot can surface the content
- **Expected Result:** Copilot retrieval respects the sensitivity-label and access-control posture — authorized users see content, unauthorized users do not
- **Evidence:** Copilot interaction logs for both authorized and unauthorized test users

### Test 3: Discoverability Control Validation

- **Objective:** Confirm that sites marked for exclusion behave according to the selected control
- **Steps:**
  1. Identify a SharePoint site that was excluded from Copilot discovery per governance decision
  2. Create unique test content in that site
  3. Query Copilot using terms from the unique test content
  4. Verify the result matches the configured control: RCD/RSS suppresses Copilot discovery, while site searchability set to off removes the site from both Microsoft Search and semantic indexing
- **Expected Result:** Copilot discovery reflects the configured scope-control behavior for the test site
- **Evidence:** Copilot query results and site-configuration screenshots

### Test 4: Governance Documentation Completeness

- **Objective:** Verify that all semantic index governance decisions are properly documented
- **Steps:**
  1. Review the index governance policy document
  2. Confirm it includes: content source scope decisions, sensitivity label thresholds, user enablement criteria, review cadence
  3. Verify governance committee sign-off is current (within the last review period)
  4. Check that change history is maintained for all scope modifications
- **Expected Result:** Complete governance documentation with current approvals
- **Evidence:** Governance policy document with sign-off records

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Site searchability / RCD configuration screenshot | PNG/PDF | Compliance evidence repository | 7 years |
| Content source inventory | CSV | Compliance evidence repository | 7 years |
| Sensitivity label access test results | PDF | Compliance evidence repository | 7 years |
| Governance decision documentation | PDF | Governance document repository | 7 years |
| Index scope change history | CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory systems and WSPs | Index governance supports supervision of AI-assisted content access |
| SEC Regulation S-P | Customer information safeguards | Controlling index scope reduces risk of AI accessing protected NPI |
| 12 CFR part 30, appendix D (OCC Heightened Standards) | Risk management governance | Where applicable, governing AI content access supports heightened risk management requirements |
| NIST AI RMF | GOVERN 1.1 — AI governance policies | Formal index governance supports compliance with AI governance requirements |

## Next Steps

- Back to [Control 1.4: Semantic Index Governance](../../../controls/pillar-1-readiness/1.4-semantic-index-governance.md)
