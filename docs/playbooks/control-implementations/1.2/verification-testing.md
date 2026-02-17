# Control 1.2: SharePoint Oversharing Detection (DSPM for AI) — Verification & Testing

Test cases and evidence collection for validating SharePoint oversharing detection and remediation.

## Test Cases

### Test 1: DSPM for AI Activation Verification

- **Objective:** Confirm DSPM for AI is enabled and scanning the tenant
- **Steps:**
  1. Navigate to Microsoft Purview > DSPM for AI > Overview
  2. Verify the service status shows "Active"
  3. Confirm the last scan date is within the past 7 days
  4. Check that the scan scope includes all SharePoint Online sites
- **Expected Result:** DSPM for AI is active with a current scan covering all in-scope sites
- **Evidence:** Screenshot of DSPM overview page showing active status and scan date

### Test 2: Oversharing Detection Accuracy

- **Objective:** Verify that DSPM correctly identifies overshared sites
- **Steps:**
  1. Create a test SharePoint site with "Everyone except external users" access
  2. Upload a document with a Confidential sensitivity label to the test site
  3. Wait for the next DSPM scan cycle (or trigger a manual assessment)
  4. Check that the test site appears in the oversharing report
  5. Clean up the test site after verification
- **Expected Result:** The test site with sensitive labeled content and broad access appears as a Critical or High finding
- **Evidence:** DSPM finding showing the test site with correct risk classification

### Test 3: Remediation Effectiveness

- **Objective:** Confirm that remediated sites no longer appear as overshared
- **Steps:**
  1. Select a site that was previously flagged and remediated
  2. Verify the sharing capability has been restricted via `Get-SPOSite -Identity <url>`
  3. Wait for the next DSPM scan to process the change
  4. Confirm the site no longer appears in the oversharing findings or shows as remediated
- **Expected Result:** Remediated sites are marked as resolved in subsequent scans
- **Evidence:** Before and after DSPM reports showing finding resolution

### Test 4: Oversharing Policy Alert Functionality

- **Objective:** Verify that oversharing policies generate alerts when triggered
- **Steps:**
  1. Create or identify an active oversharing detection policy
  2. Simulate the policy condition (e.g., share a sensitive document broadly)
  3. Wait for the alert generation cycle (up to 24 hours)
  4. Verify the alert appears in Purview > Alerts and email notification is received
  5. Reverse the simulated oversharing action
- **Expected Result:** Alert is generated and delivered to configured recipients within the expected timeframe
- **Evidence:** Alert record from Purview and email notification screenshot

### Test 5: Copilot Access Validation Post-Remediation

- **Objective:** Confirm Copilot respects remediated permissions and does not surface overshared content
- **Steps:**
  1. Identify a user who previously had unintended access to sensitive content via oversharing
  2. After remediation, have the user query Copilot for content from the restricted site
  3. Verify Copilot does not return results from the restricted site
  4. Document the Copilot response
- **Expected Result:** Copilot only returns content the user has legitimate access to post-remediation
- **Evidence:** Copilot interaction log showing no results from restricted content

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| DSPM activation screenshot | PNG/PDF | Compliance evidence repository | 7 years |
| Oversharing assessment export | CSV | Compliance evidence repository | 7 years |
| Remediation log | CSV | Compliance evidence repository | 7 years |
| Alert notification records | PDF | Compliance evidence repository | 7 years |
| Copilot access validation results | PDF | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory procedures for information access | Oversharing detection supports compliance with information barrier requirements |
| SEC Regulation S-P | Protection of customer information | Detecting and remediating oversharing helps meet customer data protection obligations |
| GLBA Safeguards Rule | Access controls for NPI | Reduces risk of unauthorized access to non-public personal information |
| SOX Section 404 | Internal controls over financial reporting | Helps prevent unauthorized access to financial data through Copilot |
