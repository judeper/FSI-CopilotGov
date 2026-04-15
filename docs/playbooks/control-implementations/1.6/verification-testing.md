# Control 1.6: Permission Model Audit — Verification & Testing

Test cases and evidence collection for validating the permission model audit and remediation.

## Test Cases

### Test 1: Zero "Everyone" Access on Sensitive Sites

- **Objective:** Verify no sites containing sensitive data grant "Everyone" or "Everyone except external users" access
- **Steps:**
  1. Run PowerShell Script 1 (Site Permission Audit)
  2. Filter results for sites with `HasEveryoneAccess = True`
  3. Cross-reference flagged sites against the sensitive content inventory
  4. Verify zero overlap between "Everyone" access sites and sensitive content sites
- **Expected Result:** No sites containing Confidential or Highly Confidential content have "Everyone" access
- **Evidence:** Filtered audit report showing zero sensitive sites with broad access

### Test 2: Access Review Completion Rate

- **Objective:** Verify that access reviews are being completed on schedule
- **Steps:**
  1. Navigate to Microsoft Entra admin center > Identity Governance > Access Reviews
  2. Review the status of all active and recent access reviews
  3. Verify completion rate exceeds 95% within the review period
  4. Check that denied access has been properly revoked
- **Expected Result:** Access reviews completed on time with denied access removed
- **Evidence:** Access review status report from Entra ID

### Test 3: Group Membership Accuracy

- **Objective:** Verify that group memberships accurately reflect business need for access
- **Steps:**
  1. Select 5 groups that provide access to sensitive SharePoint content
  2. For each group, compare membership against the expected business user list
  3. Identify any members who should not have access (departed employees, role changes)
  4. Verify dynamic group membership rules produce correct results
- **Expected Result:** Group memberships match business requirements with no unauthorized members
- **Evidence:** Group membership comparison report

### Test 4: Sharing Link Remediation

- **Objective:** Confirm that flagged sharing links have been removed or restricted
- **Steps:**
  1. Reference the initial sharing links inventory
  2. Re-run the sharing links scan on previously flagged sites
  3. Verify anonymous and organization-wide links to sensitive content have been removed
  4. Confirm remaining links have appropriate expiration dates
- **Expected Result:** All flagged sharing links on sensitive sites have been remediated
- **Evidence:** Before and after sharing link inventory comparison

### Test 5: DSPM for AI Role Assignments

- **Objective:** Verify that DSPM for AI RBAC roles are assigned to appropriate personnel only
- **Steps:**
  1. Navigate to Microsoft Purview portal > Settings > Roles and scopes > Role groups
  2. Open the "Purview Data Security AI Viewer" role group and verify member list matches the compliance team roster
  3. Open the "Purview Data Security AI Content Viewer" role group and verify members have documented authorization to view prompt/response content
  4. Navigate to Microsoft Entra admin center > Roles and administrators > AI Administrator
  5. Verify only the designated Copilot governance lead is assigned
  6. Cross-reference all three role memberships against the approved list in the governance documentation
- **Expected Result:** All AI-prefixed roles assigned only to authorized personnel; no unauthorized assignments
- **Evidence:** Role membership screenshots from Purview portal and Entra admin center

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Permission audit report | CSV | Compliance evidence repository | 7 years |
| Access review completion records | PDF | Compliance evidence repository | 7 years |
| Group membership analysis | CSV | Compliance evidence repository | 7 years |
| Sharing link remediation log | CSV | Compliance evidence repository | 7 years |
| DSPM role assignment records | Screenshot/PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory access controls | Permission audit supports compliance with access control requirements |
| SEC Regulation S-P | Access to customer information | Auditing permissions helps meet NPI access control obligations |
| SOX Section 404 | Internal controls over access | Periodic permission reviews support compliance with internal control requirements |
| NIST CSF | PR.AC-1 Identity and access management | Permission audits validate access control effectiveness |
| FFIEC IT Handbook | Least privilege and separation of duties | DSPM role assignments enforce least-privilege access to AI governance data, with AI Content Viewer separated from AI Administrator |
- Back to [Control 1.6: Permission Model Audit](../../../controls/pillar-1-readiness/1.6-permission-model-audit.md)
