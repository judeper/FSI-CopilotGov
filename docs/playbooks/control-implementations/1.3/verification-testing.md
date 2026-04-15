# Control 1.3: Restricted SharePoint Search and Restricted Content Discovery — Verification & Testing

Test cases and evidence collection for validating Restricted SharePoint Search (RSS) and Restricted Content Discovery (RCD) configuration.

## Test Cases

### Test 1: RSS Mode Activation Verification

- **Objective:** Confirm that Restricted SharePoint Search is enabled at the tenant level
- **Steps:**
  1. Run `Get-SPOTenantRestrictedSearchMode` in PowerShell
  2. Verify the output shows `Mode: Enabled`
  3. Cross-reference in SharePoint Admin Center > Settings > Search
  4. Confirm the setting matches expected configuration
- **Expected Result:** RSS mode returns "Enabled" via both PowerShell and Admin Center
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

### Test 5: Restricted Content Discovery (RCD) Functional Test

- **Objective:** Verify that RCD-enabled sites are excluded from Copilot discovery while remaining accessible to users
- **Steps:**
  1. Identify a SharePoint site where RCD has been enabled
  2. As a standard user with Copilot license and read access to the site, ask Copilot a question about specific content from that site
  3. Verify Copilot does not return content from the RCD-excluded site
  4. Navigate directly to the site and confirm the user can still access it
  5. Verify the content is accessible directly but not through Copilot
- **Expected Result:** Copilot does not surface content from RCD-excluded sites, but users can still access the sites directly via SharePoint
- **Evidence:** Copilot interaction log showing no results from RCD-excluded site; direct SharePoint access screenshot confirming user can still reach the site

### Test 6: Change Control Verification

- **Objective:** Verify that changes to the RSS allowed list and RCD configuration follow the documented change control process
- **Steps:**
  1. Review audit logs for RSS configuration changes in the past 30 days
  2. Run Script 7 (RCD Audit) to get current list of RCD-enabled sites
  3. Cross-reference each RSS and RCD change with approved change requests
  4. Verify each addition, removal, or RCD configuration change has governance committee approval documentation
  5. Confirm no unauthorized changes have been made
- **Expected Result:** All RSS allowed list changes and RCD configuration changes have corresponding approved change requests
- **Evidence:** Audit log export with change request cross-reference; RCD audit CSV

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| RSS mode verification | Screenshot/PowerShell output | Compliance evidence repository | 7 years |
| RSS allowed list export with audit details | CSV | Compliance evidence repository | 7 years |
| RCD site configuration audit | CSV | Compliance evidence repository | 7 years |
| Search restriction test results | PDF with screenshots | Compliance evidence repository | 7 years |
| RCD functional test results | PDF with screenshots | Compliance evidence repository | 7 years |
| Copilot grounding validation | PDF with interaction logs | Compliance evidence repository | 7 years |
| Change control documentation (RSS and RCD) | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory controls over information access | RSS limits Copilot data scope to approved content sources |
| SEC Regulation S-P | Safeguarding customer information | Restricting search scope reduces risk of AI surfacing protected data |
| GLBA §501(b) | Information security program / access controls | RSS acts as a preventive control limiting AI content access |
| SOX Section 404 | Internal controls | Change-controlled allowed list supports compliance with internal control requirements |

## Next Steps

- See [Troubleshooting](troubleshooting.md) for resolving failed test cases
- Back to [Control 1.3: Restricted SharePoint Search](../../../controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md)
