# Control 2.12: External Sharing and Guest Access Governance — Verification & Testing

Test cases and evidence collection for validating external sharing controls.

## Test Cases

### Test 1: External Sharing Block Verification

- **Objective:** Confirm external sharing is blocked on Copilot-scoped sites
- **Steps:**
  1. Select a site on the Copilot RSS allowed list
  2. Attempt to share a document with an external user
  3. Verify the sharing is blocked by policy
  4. Verify the block is logged in audit trail
- **Expected Result:** External sharing blocked on Copilot-scoped sites
- **Evidence:** Sharing block screenshot and audit log

### Test 2: Guest Access Review Completion

- **Objective:** Verify guest access reviews are completing on schedule
- **Steps:**
  1. Navigate to Entra ID > Identity Governance > Access Reviews
  2. Verify active reviews are on schedule
  3. Confirm completion rate exceeds 95%
  4. Verify denied access has been removed
- **Expected Result:** Reviews completing on schedule with access changes applied
- **Evidence:** Access review completion records

### Test 3: Anonymous Link Prevention

- **Objective:** Confirm anonymous sharing links cannot be created
- **Steps:**
  1. As a standard user, attempt to create an "Anyone with the link" sharing link
  2. Verify the option is not available
  3. Repeat on multiple site types
- **Expected Result:** Anonymous link creation is blocked organization-wide
- **Evidence:** Screenshot showing unavailable sharing option

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| External sharing configuration | CSV | Compliance evidence repository | 7 years |
| Guest user inventory | CSV | Compliance evidence repository | 7 years |
| Access review records | PDF | Compliance evidence repository | 7 years |
| Sharing block test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| SEC Regulation S-P | Third-party information sharing | External sharing controls support compliance with NPI sharing restrictions |
| GLBA §501(b) | Access controls for NPI | Guest access governance helps meet safeguards requirements |
| FINRA Rule 3110 | Supervisory systems and WSPs | External sharing restrictions support compliance with supervisory controls |
- Back to [Control 2.12](../../../controls/pillar-2-security/2.12-external-sharing-governance.md)
