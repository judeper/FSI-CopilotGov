# Control 3.2: Data Retention Policies for Copilot Interactions — Verification & Testing

Test cases and evidence collection procedures to confirm data retention policies are correctly applied to Copilot interaction data and generated content.

## Test Cases

### Test 1: Retention Policy Deployment Verification

- **Objective:** Confirm retention policies are deployed and active for Copilot locations
- **Steps:**
  1. Run `Get-RetentionCompliancePolicy | Where-Object { $_.Name -like "*Copilot*" }`.
  2. Verify each policy shows `Enabled: True` and `DistributionStatus: Success`.
  3. Confirm the `CopilotLocation` is set for policies targeting the Microsoft Copilot experiences location.
  4. Confirm `TeamsChannelLocation` and `TeamsChatLocation` are set for Teams retention policies.
- **Expected Result:** All FSI Copilot retention policies are deployed and distributed successfully, including the Microsoft Copilot experiences policy.
- **Evidence:** PowerShell output showing policy status and distribution.

### Test 2: Retention Rule Configuration Validation

- **Objective:** Verify retention duration and actions are correctly configured
- **Steps:**
  1. Run `Get-RetentionComplianceRule -Policy "FSI-Copilot-Experiences-Retention"`.
  2. Confirm `RetentionDuration` is 1095 days (3 years) for communications or 2190 days (6 years) for regulated tier.
  3. Confirm `RetentionComplianceAction` is `Keep`.
- **Expected Result:** Retention rules match the FSI-required retention period with retain-only action.
- **Evidence:** PowerShell output of retention rule configuration.

### Test 3: Microsoft Copilot Experiences Location Coverage

- **Objective:** Validate that Copilot Chat history and meeting recap content is retained by the Copilot experiences policy
- **Steps:**
  1. Have a test user perform a Copilot interaction in Microsoft 365 Copilot Chat.
  2. Wait for retention policy processing (up to 7 days for initial deployment).
  3. Use Content Search to locate the interaction data in the Copilot experiences location.
  4. Verify the content is marked as retained per the applied policy.
- **Expected Result:** Copilot interaction data in the Microsoft Copilot experiences location is discoverable and marked with retention metadata.
- **Evidence:** Content search results showing retained Copilot Chat interaction data.

### Test 4: Retention Label Application

- **Objective:** Confirm retention labels can be applied to Copilot-generated documents
- **Steps:**
  1. Create a document using Copilot assistance in Word or Excel.
  2. Apply the `FSI-Copilot-Regulatory-Record-6yr` label manually or via auto-labeling.
  3. Verify the label metadata appears in the document properties.
- **Expected Result:** Retention label is applied and the document shows the correct retention period.
- **Evidence:** Screenshot of document properties showing applied retention label.

### Test 5: Threaded Summary Retention Behavior

- **Objective:** Confirm that Copilot-generated meeting summaries are retained independently from source content deletion
- **Steps:**
  1. In a test Teams meeting, use Copilot to generate a meeting recap.
  2. Verify the meeting recap appears in the Teams channel or meeting chat.
  3. Delete the Teams meeting transcript (or a specific Teams message) and wait 24 hours.
  4. Confirm that the Copilot-generated meeting recap (threaded summary) remains accessible — it should be retained independently by the Microsoft Copilot experiences retention policy.
  5. Use Content Search in Purview to verify the summary is still discoverable after source content deletion.
- **Expected Result:** The Copilot-generated meeting recap remains retained and discoverable after the source Teams meeting content is deleted. FINRA Rule 4511(c) preservation requirements are met for both source and summary content.
- **Evidence:** Content search results showing the Copilot summary is retained independently of the deleted source content; screenshots comparing content before and after source deletion.

### Test 6: New Retention Location Categories Validation

- **Objective:** Verify that the Purview portal shows the restructured retention location categories and that the correct location is selected for M365 Copilot
- **Steps:**
  1. Navigate to Microsoft Purview portal > Data lifecycle management > Retention policies.
  2. Click **New retention policy** (or open an existing policy) and review the available location options.
  3. Confirm that **Microsoft Copilot experiences**, **Enterprise AI Apps**, and **Other AI Apps** are available as distinct location categories.
  4. Verify that the FSI retention policies use **Microsoft Copilot experiences** (not Enterprise AI Apps or Other AI Apps).
- **Expected Result:** The three Purview retention location categories are visible. All FSI M365 Copilot retention policies target the Microsoft Copilot experiences location.
- **Evidence:** Screenshot of retention policy location selector showing the three categories; screenshot of existing policies confirming Microsoft Copilot experiences is selected.

### Test 7: Priority Cleanup Scope Verification (Recommended Tier — if configured)

- **Objective:** Confirm that priority cleanup applies only to the intended narrow scope of unsent Copilot drafts
- **Steps:**
  1. Review the `FSI-Copilot-Draft-Priority-Cleanup` policy configuration.
  2. Verify the policy is scoped to personal OneDrive accounts only (not shared sites or SharePoint).
  3. Confirm that shared or sent documents in OneDrive are not subject to the cleanup policy (test by placing a shared document in the same OneDrive location and verifying it is not captured by the cleanup scope).
  4. Verify the retention period is documented in the firm's records management schedule with regulatory rationale.
- **Expected Result:** Priority cleanup policy is narrow in scope. No shared or sent documents are captured. Scope decision is documented.
- **Evidence:** PowerShell output of policy configuration; records management schedule entry showing regulatory rationale.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Retention policy configuration | PowerShell | Text export | With control documentation |
| Retention rule details | PowerShell | Text export | With control documentation |
| Microsoft Copilot experiences policy distribution | PowerShell/Portal | Screenshot | With control documentation |
| Threaded summary retention test | Purview Content Search | CSV/Screenshot | Per policy |
| Label application proof | SharePoint/OneDrive | Screenshot | With control documentation |
| Location category verification | Purview portal | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC Rule 17a-4(a) | 6-year retention for broker-dealer records | Microsoft Copilot experiences retention policy covers Copilot Chat history and meeting recaps for 6-year regulated tier |
| SEC Rule 17a-3(a)(17) | All communications relating to the member's business | Conservative Regulated-tier approach retains all Copilot-generated content regardless of draft status |
| FINRA Rule 4511 | Books-and-records retention | Helps meet retention obligations for AI interaction records across all Copilot surfaces |
| FINRA Rule 4511(c) | Preservation format and media requirements | Threaded summary retention test verifies both source and summary content are preserved in accessible format |
| GLBA | Financial record preservation | Supports privacy and record preservation requirements for AI-processed customer information |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for retention policy issues
- Proceed to [Control 3.3](../3.3/portal-walkthrough.md) for eDiscovery configuration
