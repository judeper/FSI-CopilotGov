# Control 1.3: Restricted SharePoint Search Configuration — Verification & Testing

Test cases and evidence collection for validating Restricted SharePoint Search configuration.

## Test Cases

### Test 1: RSS Mode Activation Verification

- **Objective:** Confirm that Restricted SharePoint Search is enabled at the tenant level
- **Steps:**
  1. Run `Get-SPOTenantRestrictedSearchMode` in PowerShell
  2. Verify the output shows `Mode: Restricted`
  3. Cross-reference in SharePoint Admin Center > Settings > Search
  4. Confirm the setting matches expected configuration
- **Expected Result:** RSS mode returns "Restricted" via both PowerShell and Admin Center
- **Evidence:** PowerShell output and admin center screenshot

### Test 2: Allowed List Completeness

- **Objective:** Verify all governance-approved sites are on the allowed list and no unauthorized sites are included
- **Steps:**
  1. Export the current allowed list using Script 3 (Audit and Export)
  2. Compare against the governance committee's approved sites list
  3. Identify any discrepancies (missing approved sites or unauthorized additions)
  4. Verify count matches expected number
- **Expected Result:** Allowed list exactly matches governance-approved sites list with zero discrepancies
- **Evidence:** Comparison report showing approved list vs. actual allowed list

### Test 3: Search Restriction Functional Test

- **Objective:** Verify that search results only return content from allowed sites
- **Steps:**
  1. As a standard user with Copilot license, search for a term that exists on both allowed and non-allowed sites
  2. Verify search results only include content from allowed sites
  3. Confirm no results appear from sites not on the allowed list
  4. Repeat the test with 3-5 different search terms across different content types
- **Expected Result:** Search results are limited exclusively to content from allowed sites
- **Evidence:** Search result screenshots showing results only from allowed sites

### Test 4: Copilot Grounding Scope Validation

- **Objective:** Confirm Copilot only uses content from allowed sites when generating responses
- **Steps:**
  1. Create unique test content on a non-allowed site (distinct phrase not found elsewhere)
  2. Create similar test content on an allowed site
  3. Ask Copilot a question that would require the test content
  4. Verify Copilot references only the allowed site content
  5. Verify Copilot does not reference the non-allowed site content
- **Expected Result:** Copilot responses are grounded exclusively on allowed site content
- **Evidence:** Copilot interaction logs showing referenced sources

### Test 5: Change Control Verification

- **Objective:** Verify that changes to the allowed list follow the documented change control process
- **Steps:**
  1. Review audit logs for RSS configuration changes in the past 30 days
  2. Cross-reference each change with approved change requests
  3. Verify each addition or removal has governance committee approval documentation
  4. Confirm no unauthorized changes have been made
- **Expected Result:** All allowed list changes have corresponding approved change requests
- **Evidence:** Audit log export with change request cross-reference

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| RSS mode verification | Screenshot/PowerShell output | Compliance evidence repository | 7 years |
| Allowed list export with audit details | CSV | Compliance evidence repository | 7 years |
| Search restriction test results | PDF with screenshots | Compliance evidence repository | 7 years |
| Copilot grounding validation | PDF with interaction logs | Compliance evidence repository | 7 years |
| Change control documentation | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory controls over information access | RSS limits Copilot data scope to approved content sources |
| SEC Regulation S-P | Safeguarding customer information | Restricting search scope reduces risk of AI surfacing protected data |
| GLBA Safeguards Rule | Access controls | RSS acts as a preventive control limiting AI content access |
| SOX Section 404 | Internal controls | Change-controlled allowed list supports compliance with internal control requirements |
