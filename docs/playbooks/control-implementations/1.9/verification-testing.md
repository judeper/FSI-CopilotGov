# Control 1.9: License Planning and Assignment Strategy — Verification & Testing

Test cases and evidence collection for validating Copilot license management.

## Test Cases

### Test 1: License Inventory Accuracy

- **Objective:** Confirm license counts match procurement records and assignment plan
- **Steps:**
  1. Run PowerShell Script 1 to generate license inventory
  2. Compare purchased counts against procurement records
  3. Verify assigned counts match the approved deployment plan
  4. Confirm available licenses are sufficient for the next deployment wave
- **Expected Result:** License counts are accurate and aligned with deployment plan
- **Evidence:** License inventory report with procurement comparison

### Test 2: Group-Based Assignment Verification

- **Objective:** Verify Copilot licenses are correctly assigned through deployment groups
- **Steps:**
  1. Check group membership for each deployment group in Entra ID
  2. Verify all group members have the Copilot license assigned
  3. Confirm no users outside deployment groups have Copilot licenses
  4. Test license propagation by adding a test user to the group and verifying assignment
- **Expected Result:** License assignments exactly match group memberships
- **Evidence:** Group membership and license assignment comparison

### Test 3: Prerequisite License Stack Completeness

- **Objective:** Confirm all Copilot users have required prerequisite licenses
- **Steps:**
  1. For a sample of 20 Copilot-licensed users, review their complete license stack
  2. Verify each user has the required base license (M365 E3/E5 for enterprise users; F1/F3 for Frontline users)
  3. Check for required add-on licenses based on governance controls (SAM, Compliance)
  4. Identify any users with incomplete license stacks
- **Expected Result:** All Copilot users have complete prerequisite license stacks
- **Evidence:** License stack audit for sample users

### Test 4: License Reclamation Process

- **Objective:** Verify the process for reclaiming licenses from inactive or departed users
- **Steps:**
  1. Identify users flagged as inactive in the utilization report
  2. Verify the reclamation workflow is documented and approved
  3. Test the reclamation process by removing a test user from the deployment group
  4. Confirm the Copilot license is removed within 24 hours
- **Expected Result:** License reclamation process works as documented
- **Evidence:** Reclamation workflow test results

### Test 5: Frontline User License Verification

- **Objective:** Confirm Frontline (F1/F3) users receiving the Copilot add-on have appropriate base licenses and governance coverage
- **Steps:**
  1. Run PowerShell Script 4 to generate the Frontline Copilot status report
  2. Verify all Frontline users with the Copilot add-on have a valid F1 or F3 base license
  3. Confirm that information barrier, DLP, and sensitivity label policies are applied to Frontline Copilot users
  4. Test Copilot access for a sample Frontline user to confirm the add-on is functional
  5. Document any feature limitations observed for F1/F3 users vs. E3/E5 users
- **Expected Result:** Frontline Copilot users have correct base licenses and governance coverage
- **Evidence:** Frontline license report; sample Copilot access confirmation; governance policy scope documentation

### Test 6: PAYG Copilot Chat Governance

- **Objective:** Verify PAYG Copilot Chat is governed and tracked appropriately
- **Steps:**
  1. Confirm Azure Cost Management shows PAYG Copilot Chat usage data
  2. Verify spend limits or budget alerts are configured in Azure Cost Management
  3. Confirm that governance policies (DLP, sensitivity labels, information barriers) apply to PAYG users
  4. Review PAYG user list against the governance policy scope to identify any coverage gaps
- **Expected Result:** PAYG Copilot Chat spending is tracked, limited, and governed
- **Evidence:** Azure Cost Management configuration; PAYG usage report; governance policy scope confirmation

## Evidence Collection

| Evidence Item | Format | Storage Location | Retention |
|--------------|--------|-----------------|-----------|
| License inventory report | CSV | Compliance evidence repository | 7 years |
| License assignment audit | CSV | Compliance evidence repository | 7 years |
| Deployment plan with wave definitions | PDF | Governance document repository | 7 years |
| Utilization and reclamation records | CSV | Compliance evidence repository | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Supports It |
|-----------|-------------|------------------------------|
| FINRA Rule 3110 | Supervisory system controls | Controlled license assignment supports compliance with supervisory access management |
| SOX Section 404 | Internal controls | License management as an internal control for AI access governance |
| OCC Heightened Standards | IT governance | Documented license strategy supports compliance with IT governance requirements |
| NIST AI RMF | GOVERN 1.2 — AI resource management | License planning supports compliance with AI resource governance |
