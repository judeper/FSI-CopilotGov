# Control 1.3: Restricted SharePoint Search and Restricted Content Discovery — Verification & Testing

Test cases and evidence collection for validating Microsoft 365 Copilot discoverability governance. Restricted Content Discovery (RCD) is the current per-site discoverability control for new and ongoing deployments; Restricted SharePoint Search (RSS) checks apply only to existing configurations enabled before RSS retirement.

!!! warning "RSS is retiring — verify RCD first"
    Microsoft has blocked new enablement of Restricted SharePoint Search (RSS) from July 31, 2026. For new and current Copilot deployments, verify **Restricted Content Discovery (RCD)** as the primary discoverability control (Tests 1–5). The RSS test cases (Tests 6–8) apply **only** to organizations validating an existing RSS configuration enabled before the cutoff and planning migration to RCD.

## Test Cases (Current — RCD)

### Test 1: RCD Configuration State Verification (Current)

- **Objective:** Confirm Restricted Content Discovery is enabled on the intended sites and the configuration matches the RCD governance log
- **Steps:**
  1. Run Script 7 (Audit RCD Configuration Across All Sites) from the [PowerShell Setup](powershell-setup.md) playbook to export all sites with `RestrictContentOrgWideSearch = $true`
  2. For a targeted site, confirm the setting directly: `(Get-SPOSite -Identity <url>).RestrictContentOrgWideSearch` returns `True`
  3. Compare the exported RCD site list against the governance committee's approved RCD exclusion list and the RCD governance log
  4. Identify any discrepancies (sites missing RCD, or RCD applied without a governance-log entry)
- **Expected Result:** RCD-enabled sites exactly match the approved exclusion list, with a governance-log entry (URL, justification, review date, owner) for each
- **Evidence:** RCD audit CSV and governance-log comparison report

### Test 2: RCD Functional Test — Copilot Discovery Exclusion (Current)

- **Objective:** Verify that RCD-enabled sites are excluded from Copilot discovery and organization-wide search while remaining accessible to users
- **Steps:**
  1. Identify a SharePoint site where RCD has been enabled
  2. Using an account with read access but **no prior interaction history** with the site (has not recently accessed it, does not own content on it, and has not had content directly shared), ask Copilot a question about specific content from that site
  3. Verify Copilot does not return content from the RCD-excluded site
  4. Confirm the site does not appear in organization-wide search experiences (SharePoint home, Office.com)
  5. Verify AI entry points (Copilot button, AI action menus, **Create pages with AI**) are not shown on the site
  6. Navigate directly to the site and confirm the user can still access it
- **Expected Result:** Copilot and organization-wide search do not surface content from RCD-excluded sites for users without prior interaction history; AI entry points are hidden on the site; users retain direct SharePoint access
- **Evidence:** Copilot interaction log showing no results from the RCD-excluded site; organization-wide search screenshot; screenshot of the site with AI entry points absent; direct SharePoint access screenshot confirming the user can still reach the site

### Test 3: Copilot Grounding Scope Validation (Current)

- **Objective:** Confirm Copilot grounds responses only on content outside RCD-excluded sites
- **Steps:**
  1. Create unique test content (a distinct phrase not found elsewhere) on an RCD-excluded site
  2. Create similar test content on a non-excluded site
  3. Using an account with **no prior interaction history** with the RCD-excluded site, ask Copilot a question that would require the test content
  4. Verify Copilot references only the non-excluded site content
  5. Verify Copilot does not reference the RCD-excluded site content
- **Expected Result:** Copilot responses are grounded exclusively on non-excluded content; RCD-excluded content is not referenced for users without documented interaction exceptions
- **Evidence:** Copilot interaction logs showing referenced sources

### Test 4: RCD Monitoring Report Verification (Current)

- **Objective:** Confirm the tenant-wide RCD monitoring report runs successfully and reflects the governance log
- **Steps:**
  1. Run `Start-SPORestrictedContentDiscoverabilityReport` (Script 1c in the [PowerShell Setup](powershell-setup.md) playbook)
  2. Retrieve the completed report with `Get-SPORestrictedContentDiscoverabilityReport`
  3. Cross-reference the reported RCD sites against the RCD governance log
  4. Confirm the report is generated on the documented cadence (monthly per governance level)
- **Expected Result:** The RCD report generates successfully and its site list matches the governance log with zero discrepancies
- **Evidence:** RCD monitoring report export with governance-log cross-reference

### Test 5: Change Control Verification (Current — RCD; Legacy — RSS)

- **Objective:** Verify that changes to RCD configuration (and, for existing deployments, the RSS allowed list) follow the documented change control process
- **Steps:**
  1. Run Script 7 (RCD Audit) to get the current list of RCD-enabled sites
  2. Review Microsoft Purview audit logs for RCD enablement, disablement, and justification changes in the past 30 days
  3. Cross-reference each RCD change with an approved change request and its RCD governance-log entry
  4. *(Existing RSS configurations only)* Review audit logs for RSS configuration changes in the past 30 days and cross-reference each with an approved change request
  5. Confirm no unauthorized changes have been made
- **Expected Result:** All RCD configuration changes (and any legacy RSS allowed-list changes for existing deployments) have corresponding approved change requests and governance documentation
- **Evidence:** Purview audit log export with change-request cross-reference; RCD audit CSV; (legacy) RSS change log

## Legacy Test Cases — Existing RSS Configurations Only

!!! warning "Applies only to existing RSS configurations"
    Tests 6–8 validate an existing Restricted SharePoint Search configuration enabled before the July 31, 2026 new-enablement cutoff. Do **not** use these tests to validate new deployments — RSS cannot be newly enabled after that date. For new or current deployments, use Tests 1–5 (RCD).

### Test 6: RSS Mode Verification (Legacy — Existing Configurations Only)

- **Objective:** Confirm that an existing Restricted SharePoint Search configuration is in the expected state at the tenant level
- **Steps:**
  1. Run `Get-SPOTenantRestrictedSearchMode` in PowerShell
  2. Verify the output shows the expected mode (`Enabled` while the configuration remains in use during migration to RCD)
  3. Cross-reference in SharePoint Admin Center > Settings > Search
  4. Confirm the setting matches the documented migration state
- **Expected Result:** RSS mode matches the documented state via both PowerShell and Admin Center
- **Evidence:** PowerShell output and admin center screenshot

### Test 7: RSS Allowed List Completeness (Legacy — Existing Configurations Only)

- **Objective:** Verify all governance-approved sites are on the existing RSS allowed list and no unauthorized sites are included
- **Steps:**
  1. Export the current allowed list using Script 3 (Audit and Export) from the [PowerShell Setup](powershell-setup.md) playbook
  2. Compare against the governance committee's approved sites list
  3. Identify any discrepancies (missing approved sites or unauthorized additions)
  4. Verify the count matches the expected number and remains within the 100-site cap
- **Expected Result:** Allowed list exactly matches the governance-approved sites list with zero discrepancies
- **Evidence:** Comparison report showing approved list vs. actual allowed list

### Test 8: RSS Search Restriction Functional Test (Legacy — Existing Configurations Only)

- **Objective:** Verify that, for an existing RSS configuration, search results only return content from allowed sites
- **Steps:**
  1. Using an account with **no prior interaction history**, search for a term that exists on both allowed and non-allowed sites
  2. Verify search results only include content from allowed sites
  3. Confirm no results appear from sites not on the allowed list
  4. Repeat the test with 3–5 different search terms across different content types
  5. Note that recently accessed, Teams/Outlook-shared, or owned/frequently-visited content may still appear due to documented RSS exceptions (limited to the last 2,000 entities)
- **Expected Result:** Search results are limited to content from allowed sites, except for documented RSS recent-activity exceptions
- **Evidence:** Search result screenshots showing results only from allowed sites

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| RCD configuration audit (per-site state) | CSV | Compliance evidence repository | 7 years |
| RCD governance log (site, justification, review date, owner) | CSV/PDF | Governance document repository | 7 years |
| RCD functional test results | PDF with screenshots | Compliance evidence repository | 7 years |
| RCD monitoring report | CSV | Compliance evidence repository | 7 years |
| Copilot grounding validation | PDF with interaction logs | Compliance evidence repository | 7 years |
| Change control documentation (RCD and legacy RSS) | PDF | Governance document repository | 7 years |
| RSS mode verification *(legacy — existing configurations only)* | Screenshot/PowerShell output | Compliance evidence repository | 7 years |
| RSS allowed list export with audit details *(legacy — existing configurations only)* | CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory controls over information access | RCD limits Copilot discovery scope per site as the current control; the legacy RSS allow-list served this role in existing configurations |
| SEC Regulation S-P | Safeguarding customer information | Restricting Copilot discovery scope reduces risk of AI surfacing protected data — RCD per-site exclusion is the current mechanism, with RSS as a legacy posture |
| GLBA §501(b) | Information security program / access controls | RCD acts as a preventive control limiting AI content discovery (current); RSS is a legacy transitional allow-list posture |
| SOX Section 404 | Internal controls | A change-controlled RCD governance log supports internal control requirements; legacy RSS allowed-list change control applies to existing configurations |

## Next Steps

- See [Troubleshooting](troubleshooting.md) for resolving failed test cases
- See [PowerShell Setup](powershell-setup.md) for the RCD and legacy RSS scripts referenced above
- Back to [Control 1.3: Restricted SharePoint Search](../../../controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md)
