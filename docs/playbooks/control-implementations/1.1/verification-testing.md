# Control 1.1: Copilot Readiness Assessment and Data Hygiene — Verification & Testing

Test cases and evidence collection procedures for validating Copilot readiness and data hygiene controls.

## Test Cases

### Test 1: Optimization Assessment Completeness

- **Objective:** Verify that the Copilot Optimization Assessment has run and all infrastructure findings have been reviewed
- **Steps:**
  1. Sign in to Microsoft 365 Admin Center as Entra Global Admin
  2. Navigate to Admin Center > Copilot > Settings > Readiness
  3. Confirm the Optimization Assessment has completed and shows current results
  4. Verify network readiness, Office update channel compliance, and app compatibility sections are all reviewed
  5. Confirm that any "blocking" findings have been addressed or have documented remediation plans
- **Expected Result:** Optimization Assessment shows no blocking infrastructure issues, or all blocking issues have documented remediation timelines
- **Evidence:** Screenshot of Optimization Assessment results with timestamp; remediation plan document if findings exist

### Test 1b: Readiness Dashboard Accessibility

- **Objective:** Verify that the Copilot readiness dashboard is accessible and returning data
- **Steps:**
  1. Sign in to Microsoft 365 Admin Center as Entra Global Admin
  2. Navigate to Copilot > Settings > Readiness
  3. Confirm the dashboard loads and displays assessment categories
  4. Verify data freshness (last updated within 48 hours)
- **Expected Result:** Dashboard displays current readiness scores across all assessment categories
- **Evidence:** Screenshot of readiness dashboard with timestamp

### Test 2: Oversharing Assessment Completeness

- **Objective:** Verify the oversharing assessment has scanned all relevant SharePoint sites
- **Steps:**
  1. Run PowerShell Script 2 (Data Hygiene Scan) to get total site count
  2. Compare against the DSPM oversharing report site count in Purview
  3. Verify coverage exceeds 95% of active sites
  4. Confirm high-sensitivity sites are all included in the scan
- **Expected Result:** DSPM report covers at least 95% of active SharePoint sites
- **Evidence:** Export of scan coverage comparison showing site counts

### Test 3: Sensitivity Label Coverage Threshold

- **Objective:** Verify sensitivity label adoption meets the target for the organization's governance tier (>50% Baseline / >75% Recommended / >90% Regulated)
- **Steps:**
  1. Open Microsoft Purview > Information Protection > Label Analytics
  2. Review the overall labeling rate for documents in SharePoint and OneDrive
  3. Check department-level breakdown for any groups below threshold
  4. Verify auto-labeling policies are active for common FSI content types
- **Expected Result:** Organization-wide label coverage meets or exceeds the target for the selected governance tier
- **Evidence:** Label analytics report export showing coverage percentages

### Test 4: Permission Model Remediation Verification

- **Objective:** Confirm that identified permission anomalies have been remediated
- **Steps:**
  1. Reference the initial readiness assessment report findings
  2. Re-run PowerShell Script 1 against previously flagged sites
  3. Verify that "Anyone" links have been removed from sensitive sites
  4. Confirm sharing capabilities are set to appropriate levels
- **Expected Result:** Zero critical permission anomalies on sites containing regulated data
- **Evidence:** Before and after comparison of permission scan results

### Test 5: Governance Committee Sign-off

- **Objective:** Verify that the readiness assessment has been formally reviewed and approved
- **Steps:**
  1. Locate the readiness assessment report in the governance document repository
  2. Verify it includes all required sections (oversharing, labels, permissions, recommendations)
  3. Confirm governance committee has reviewed and signed off
  4. Verify remediation plan is documented for any outstanding items
- **Expected Result:** Signed readiness assessment report with documented approval
- **Evidence:** Signed report copy with committee meeting minutes

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Readiness dashboard screenshot | PNG/PDF | Compliance evidence repository | 7 years |
| Oversharing assessment export | CSV/JSON | Compliance evidence repository | 7 years |
| Label coverage analytics | PDF | Compliance evidence repository | 7 years |
| Permission scan results | CSV | Compliance evidence repository | 7 years |
| Governance committee sign-off | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory system review | Readiness assessment documents supervisory review of AI data access |
| SEC Rule 17a-4 | Records preservation | If the firm treats readiness assessments as required books and records, preserve them in accordance with Rule 17a-4; otherwise retain per internal record-retention policy |
| 12 CFR part 30, appendix D (OCC Heightened Standards) | Risk management governance | Where applicable to covered institutions, formal governance review supports compliance with heightened risk management requirements |
| NIST AI RMF | MAP 1.1 — Context established | Readiness assessment maps the AI deployment context |

## Next Steps

- See [Troubleshooting](troubleshooting.md) for resolving failed test cases
- Proceed to [Control 1.2: SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) verification after all readiness tests pass
- Back to [Control 1.1: Copilot Readiness Assessment](../../../controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md)
