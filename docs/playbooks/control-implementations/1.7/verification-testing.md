# Control 1.7: SharePoint Advanced Management Readiness — Verification & Testing

Test cases and evidence collection for validating SharePoint Advanced Management configuration.

## Test Cases

### Test 1: SAM License and Feature Activation

- **Objective:** Confirm SAM is licensed and all required features are accessible
- **Steps:**
  1. Verify SAM license in Admin Center > Billing > Licenses
  2. Navigate to SharePoint Admin Center and confirm SAM-specific features are visible
  3. Run PowerShell Script 1 to enumerate available features
  4. Confirm Restricted SharePoint Search, data access governance, and lifecycle management are accessible
- **Expected Result:** SAM license is active and all governance features are available
- **Evidence:** License confirmation screenshot and PowerShell feature status output

### Test 2: Data Access Governance Reports Functioning

- **Objective:** Verify data access governance reports generate accurate data
- **Steps:**
  1. Navigate to SharePoint Admin > Reports > Data access governance
  2. Verify each report type loads and contains data
  3. Cross-reference the sharing links report with a manual check of known shared sites
  4. Confirm report data freshness (within 7 days)
- **Expected Result:** All data access governance reports are populated with current, accurate data
- **Evidence:** Screenshots of each governance report with data

### Test 3: Site Lifecycle Policy Enforcement

- **Objective:** Verify inactive site detection and notification is functioning
- **Steps:**
  1. Confirm the inactivity threshold is set to 180 days via PowerShell
  2. Identify at least one site that exceeds the inactivity threshold
  3. Verify the site owner received an inactivity notification
  4. Confirm the site appears in the "Inactive sites" filter in the Admin Center
- **Expected Result:** Inactive sites are detected and owners are notified
- **Evidence:** Inactivity notification email and admin center inactive sites list

### Test 4: Site-Level Access Review Functionality

- **Objective:** Confirm site access reviews can be initiated and completed
- **Steps:**
  1. Select a test site and initiate an access review
  2. As the designated reviewer, complete the review by approving or denying access
  3. Verify the review results are recorded
  4. If auto-apply is configured, confirm denied access is revoked
- **Expected Result:** Access reviews complete successfully with results applied
- **Evidence:** Access review completion record and results

### Test 5: Conditional Access Integration

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
| Data access governance reports | PDF/CSV | Compliance evidence repository | 7 years |
| Lifecycle policy configuration | PowerShell output | Compliance evidence repository | 7 years |
| Access review records | PDF | Compliance evidence repository | 7 years |
| Conditional access test results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory system effectiveness | SAM provides the tooling to implement and monitor supervisory access controls |
| SEC Regulation S-P | Administrative safeguards | Advanced management features support compliance with administrative safeguard requirements |
| OCC Heightened Standards | IT risk management | SAM lifecycle and governance features support compliance with IT risk management standards |
| FFIEC Guidelines | Information security controls | SAM provides enhanced security controls for SharePoint content |
