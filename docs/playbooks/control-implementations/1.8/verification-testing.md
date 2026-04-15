# Control 1.8: Information Architecture Review — Verification & Testing

Test cases and evidence collection for validating information architecture readiness for Copilot.

## Test Cases

### Test 1: Site Inventory Completeness

- **Objective:** Verify the site architecture inventory accounts for all active SharePoint sites
- **Steps:**
  1. Run PowerShell Script 1 to generate the site inventory
  2. Compare the total count with the Active Sites count in SharePoint Admin Center
  3. Verify all site templates are represented
  4. Confirm no active sites are missing from the inventory
- **Expected Result:** Inventory count matches admin center count with all site types represented
- **Evidence:** Inventory CSV with admin center comparison

### Test 2: Hub Site Alignment

- **Objective:** Confirm hub site structure aligns with business unit and governance boundaries
- **Steps:**
  1. Run Script 2 to generate the hub site relationship map
  2. Review hub-to-business unit alignment with governance committee
  3. Identify orphaned sites that should be hub-associated
  4. Verify no sites are associated with incorrect hubs
- **Expected Result:** Hub site structure reflects approved organizational structure
- **Evidence:** Hub site map with governance committee approval

### Test 3: Content Type Standardization

- **Objective:** Verify consistent content type usage across the tenant
- **Steps:**
  1. Run Script 3 on a sample of 20+ sites
  2. Identify content types that are used inconsistently
  3. Verify FSI-required content types are deployed to relevant sites
  4. Check for duplicate or conflicting content type definitions
- **Expected Result:** Core FSI content types are consistently deployed
- **Evidence:** Content type usage report with standardization analysis

### Test 4: Copilot Content Discovery Quality

- **Objective:** Validate that the information architecture supports accurate Copilot responses
- **Steps:**
  1. Identify 5 common Copilot use cases for the organization
  2. For each use case, query Copilot and evaluate response quality
  3. Assess whether responses reference appropriate content sources
  4. Note any cases where architecture gaps result in poor responses
- **Expected Result:** Copilot responses are grounded on relevant, well-organized content
- **Evidence:** Copilot response quality assessment with source references

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Site architecture inventory | CSV | Compliance evidence repository | 7 years |
| Hub site relationship map | CSV/PDF | Compliance evidence repository | 7 years |
| Content type analysis | CSV | Compliance evidence repository | 7 years |
| Architecture review findings | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory systems and WSPs | Proper information architecture supports supervisory oversight of AI-accessible content |
| SEC Rule 17a-4 | Records accessibility | Structured content architecture helps meet records accessibility requirements |
| NIST CSF 2.0 | ID.AM-5 — Data asset inventory | Information architecture inventory supports identification and management of data assets |
| NIST AI RMF | MAP 3.1 — AI system context | Architecture review documents the AI content access context |
- Back to [Control 1.8: Information Architecture Review](../../../controls/pillar-1-readiness/1.8-information-architecture-review.md)
