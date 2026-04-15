# Control 1.7: SharePoint Advanced Management Readiness — Verification & Testing

Test cases and evidence collection for validating SharePoint Advanced Management configuration.

## Test Cases

### Test 1: SAM License and Feature Activation

- **Objective:** Confirm SAM is available and all required features are accessible
- **Steps:**
  1. For organizations with Microsoft 365 Copilot licenses: verify Copilot license count in Admin Center > Billing > Licenses (SAM is included)
  2. For organizations using the standalone add-on: verify SharePoint Advanced Management license in Admin Center > Billing > Licenses
  3. Navigate to SharePoint admin center and confirm SAM-specific features are visible (Data access governance, Site lifecycle management, Restricted Content Discovery in site settings)
  4. Run PowerShell Script 1 to enumerate available features
  5. Confirm Data Access Governance reports, RCD, RAC, and lifecycle management are accessible
- **Expected Result:** SAM features are available and accessible without requiring a separate purchase (for Copilot-licensed organizations)
- **Evidence:** License confirmation screenshot and PowerShell feature status output

### Test 2: Data Access Governance Reports Functioning

- **Objective:** Verify data access governance reports generate accurate data including the site permissions snapshot
- **Steps:**
  1. Navigate to SharePoint admin center > Reports > Data access governance
  2. Verify each report type loads and contains data (sharing links, sensitivity labels, EEEU, oversharing baseline)
  3. Run the site permissions snapshot report and verify it captures a complete point-in-time view of site permissions
  4. Cross-reference the sharing links report with a manual check of known shared sites
  5. Confirm report data freshness (within 7 days)
- **Expected Result:** All data access governance reports are populated with current, accurate data; site permissions snapshot is available as a baseline record
- **Evidence:** Screenshots of each governance report with data; site permissions snapshot export

### Test 3: Site Lifecycle Policy Enforcement

- **Objective:** Verify inactive site detection and notification is functioning
- **Steps:**
  1. Confirm the inactivity threshold is set to 180 days via PowerShell
  2. Identify at least one site that exceeds the inactivity threshold
  3. Verify the site owner received an inactivity notification
  4. Confirm the site appears in the "Inactive sites" filter in the Admin Center
- **Expected Result:** Inactive sites are detected and owners are notified
- **Evidence:** Inactivity notification email and admin center inactive sites list

### Test 4: Restricted Content Discovery Enforcement

- **Objective:** Confirm RCD-enabled sites are excluded from Copilot content discovery
- **Steps:**
  1. Identify a site with Restricted Content Discovery enabled
  2. As a licensed Copilot user, submit a query that would naturally reference content from the RCD-enabled site
  3. Verify that Copilot's response does not include content from the RCD-enabled site
  4. Confirm the user can still navigate directly to the site and access content
  5. Run PowerShell Script 3 and verify `RestrictContentOrg = True` for the site
- **Expected Result:** Copilot does not surface content from RCD-enabled sites; direct access is unaffected
- **Evidence:** Copilot query results (no RCD site content), direct site access confirmation, PowerShell report

### Test 5: Restricted Access Control Enforcement

- **Objective:** Confirm RAC-enabled sites restrict access to designated security group members only
- **Steps:**
  1. Identify a site with Restricted Access Control enabled and a designated security group
  2. As a user who has a sharing link to the site but is NOT in the designated security group, attempt to access the site
  3. Verify access is denied despite holding a sharing link
  4. As a user who IS in the designated security group, verify access is granted
  5. Confirm Copilot does not surface content from the RAC-enabled site to the user outside the security group
- **Expected Result:** RAC enforces the security group boundary; sharing links do not bypass RAC; Copilot cannot expose content to users without group membership
- **Evidence:** Access denial screenshot for non-group user, access confirmation for group member, Copilot query results

### Test 6: Site-Level Access Review Functionality

- **Objective:** Confirm site access reviews can be initiated and completed
- **Steps:**
  1. Select a test site and initiate an access review
  2. As the designated reviewer, complete the review by approving or denying access
  3. Verify the review results are recorded
  4. If auto-apply is configured, confirm denied access is revoked
- **Expected Result:** Access reviews complete successfully with results applied
- **Evidence:** Access review completion record and results

### Test 7: Conditional Access Integration

- **Objective:** Verify SAM conditional access policies enforce access restrictions
- **Steps:**
  1. Configure a test site with "AllowLimitedAccess" conditional access policy
  2. Access the site from a managed device — verify full access
  3. Access the site from an unmanaged device — verify restricted access (web preview only)
  4. Confirm access restrictions are logged in audit trail
- **Expected Result:** Conditional access policies enforce device-based access restrictions
- **Evidence:** Access attempt logs from both managed and unmanaged devices

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| SAM license confirmation | Screenshot | Compliance evidence repository | 7 years |
| Site permissions snapshot report | CSV | Compliance evidence repository | 7 years |
| Data access governance reports | PDF/CSV | Compliance evidence repository | 7 years |
| RCD site configuration list | PowerShell output/CSV | Compliance evidence repository | 7 years |
| RAC site configuration and group membership | PowerShell output/CSV | Compliance evidence repository | 7 years |
| Lifecycle policy configuration | PowerShell output | Compliance evidence repository | 7 years |
| Access review records | PDF | Compliance evidence repository | 7 years |
| Conditional access test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| GLBA 501(b) | Safeguards for customer information | DAG reports identify oversharing risks; RAC enforces least-privilege access boundaries for customer data sites |
| FINRA Rule 3110 | Supervisory systems and WSPs | SAM provides the tooling to implement and monitor supervisory access controls |
| SEC Regulation S-P | Administrative safeguards | RCD prevents Copilot from surfacing consumer financial data; RAC enforces access boundaries per Regulation S-P |
| OCC Heightened Standards | IT risk management | SAM lifecycle and governance features support compliance with IT risk management standards |
| FFIEC IT Handbook | Information security controls | DAG reports and access reviews support periodic access certification; RAC enforces least privilege |
| SOX 302/404 | Internal controls over financial data access | Site access reviews and RAC support access certification for sites containing financial reporting data |
- Back to [Control 1.7: SharePoint Advanced Management](../../../controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md)
