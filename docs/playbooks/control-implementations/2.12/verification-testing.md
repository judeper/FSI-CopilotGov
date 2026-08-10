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
  4. Verify denied access has been removed from the reviewed resource
  5. Verify alternate access paths through Microsoft 365 groups, security groups, Teams, applications, direct permissions, and sharing links are separately reconciled
- **Expected Result:** Reviews complete on schedule, changes are applied to the reviewed resource, and surviving access paths are explicitly resolved or approved
- **Evidence:** Access review completion records and access-path reconciliation record

### Test 3: SharePoint/OneDrive Guest-Access Expiration

- **Objective:** Verify the limited scope of SharePoint/OneDrive guest expiration without misrepresenting it as complete access removal or Entra guest-account deletion
- **Steps:**
  1. Review `ExternalUserExpirationRequired` and `ExternalUserExpireInDays`
  2. Confirm site-level overrides are documented
  3. Confirm the test uses direct site permission or sharing-link access granted after the policy was enabled
  4. Inventory pre-existing direct or sharing-link access separately
  5. Inventory Microsoft 365 group, security group, and Teams membership that can preserve access to a group-connected site or related content
  6. Verify the renewal or removal process for each access path
  7. Confirm the evidence states that SharePoint guest-access expiration does not alter or delete the Entra B2B account
- **Expected Result:** Eligible direct or sharing-link access expires according to policy; surviving pre-existing, Microsoft 365 group, security group, and Teams access is separately identified and reconciled; the Entra account lifecycle remains governed independently
- **Evidence:** Tenant setting export, policy enablement date, site override record, expiration notification or test record, and group/Teams membership reconciliation

### Test 4: Guest Account Deletion Review Configuration

- **Objective:** Verify automatic B2B guest-account deletion, if required, uses a supported access-review configuration
- **Steps:**
  1. Confirm the review is scoped to **Select Teams + groups**, not **All Microsoft 365 groups with guest users**
  2. Confirm **Auto apply results to resource** is enabled
  3. Confirm **If reviewers don't respond** is set to **Remove access**
  4. Confirm **Action to apply on denied guest users** is set to **Block user from signing-in for 30 days, then remove user from the tenant**
- **Expected Result:** Account deletion is configured only through the supported selected-groups review mode
- **Evidence:** Access-review scope and post-review action screenshots or exported configuration

### Test 5: Anonymous Link Prevention

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
| Guest-access expiration configuration | PDF/CSV | Compliance evidence repository | 7 years |
| Guest group, security-group, and Teams access reconciliation | CSV/PDF | Compliance evidence repository | 7 years |
| Sharing block test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| SEC Regulation S-P | Third-party information sharing | External sharing controls support compliance with NPI sharing restrictions |
| GLBA §501(b) | Access controls for NPI | Guest access governance helps meet safeguards requirements |
| FINRA Rule 3110 | Supervisory systems and WSPs | External sharing restrictions support compliance with supervisory controls |
- Back to [Control 2.12](../../../controls/pillar-2-security/2.12-external-sharing-governance.md)
