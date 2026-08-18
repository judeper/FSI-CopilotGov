# Control 2.5: Data Minimization and Grounding Scope — Verification & Testing

Test cases and evidence collection for validating data minimization and grounding scope controls.

## Test Cases

### Test 1: Grounding Scope Limitation Verification

- **Objective:** Confirm Copilot only accesses content within the approved grounding scope
- **Steps:**
  1. Create unique test content on a site outside the grounding scope
  2. Select a test user who does not own, has not recently accessed, and has not been directly or Teams/Outlook-shared that content — Microsoft documents these as cases where content still surfaces
  3. As that Copilot user, query Copilot for the unique test content
  4. Allow for index propagation before testing; propagation depends on site size
  5. Verify Copilot does not return results from the out-of-scope site
  6. Create similar test content on an in-scope site and verify Copilot finds it
- **Expected Result:** Copilot responses limited to in-scope content for users outside the documented exception cases; any exception observed is recorded with its cause
- **Evidence:** Copilot query results showing scope enforcement, plus the documented exception log

### Test 2: Feature Minimization Verification

- **Objective:** Confirm disabled Copilot features are not accessible to users
- **Steps:**
  1. Review the list of disabled Copilot features in Admin Center
  2. As a test user, attempt to access each disabled feature
  3. Verify disabled features are not available in the Office application UI
  4. Document any features that remain accessible despite being disabled
- **Expected Result:** All disabled features are inaccessible to users
- **Evidence:** Feature availability test results

### Test 3: Scope Growth Monitoring

- **Objective:** Verify the grounding scope has not expanded without governance approval
- **Steps:**
  1. Compare the current grounding scope (sites covered by RCD, plus any RSS allowed list) against the last governance-approved list
  2. Identify any additions or removals
  3. Verify all changes have documented approval
- **Expected Result:** Scope matches governance-approved list with no unauthorized changes
- **Evidence:** Scope comparison report with approval documentation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| Grounding scope inventory | CSV | Compliance evidence repository | 7 years |
| Feature minimization test results | PDF | Compliance evidence repository | 7 years |
| Scope change approval records | PDF | Governance document repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| GDPR Art. 5(1)(c) | Data minimization | Grounding scope limits support compliance with data minimization principles |
| GLBA §501(b) | Access controls | Limiting AI data scope supports compliance with access control requirements |
| NIST Privacy Framework | CT.DM-1 Data minimization | Grounding scope controls support compliance with data minimization practices |
- Back to [Control 2.5](../../../controls/pillar-2-security/2.5-data-minimization-grounding-scope.md)
