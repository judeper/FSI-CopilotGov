# Control 3.2: Data Retention Policies for Copilot Interactions — Verification & Testing

Test cases and evidence collection procedures to confirm data retention policies are correctly applied to Copilot interaction data and generated content.

## Test Cases

### Test 1: Retention Policy Deployment Verification

- **Objective:** Confirm retention policies are deployed and active for Copilot locations
- **Steps:**
  1. Run `Get-RetentionCompliancePolicy | Where-Object { $_.Name -like "*Copilot*" }`.
  2. Verify each policy shows `Enabled: True` and `DistributionStatus: Success`.
  3. Confirm the `CopilotInteractionLocation` is set to "All" or specific scoped groups.
- **Expected Result:** All FSI Copilot retention policies are deployed and distributed successfully.
- **Evidence:** PowerShell output showing policy status and distribution.

### Test 2: Retention Rule Configuration Validation

- **Objective:** Verify retention duration and actions are correctly configured
- **Steps:**
  1. Run `Get-RetentionComplianceRule -Policy "FSI-Copilot-Interaction-Retention"`.
  2. Confirm `RetentionDuration` is 2555 days (7 years).
  3. Confirm `RetentionComplianceAction` is `KeepAndDelete`.
- **Expected Result:** Retention rules match the FSI-required 7-year retention period with automatic deletion.
- **Evidence:** PowerShell output of retention rule configuration.

### Test 3: Copilot Interaction Preservation Hold

- **Objective:** Validate that Copilot interactions are held by retention policies
- **Steps:**
  1. Have a test user perform a Copilot interaction.
  2. Wait for retention policy processing (up to 7 days for initial deployment).
  3. Use Content Search to locate the interaction data.
  4. Verify the content is marked as retained per the applied policy.
- **Expected Result:** Copilot interaction data is discoverable and marked with retention metadata.
- **Evidence:** Content search results showing retained Copilot interaction data.

### Test 4: Retention Label Application

- **Objective:** Confirm retention labels can be applied to Copilot-generated documents
- **Steps:**
  1. Create a document using Copilot assistance in Word or Excel.
  2. Apply the "Copilot-Generated-7yr-Retain" label manually or via auto-labeling.
  3. Verify the label metadata appears in the document properties.
- **Expected Result:** Retention label is applied and the document shows the correct retention period.
- **Evidence:** Screenshot of document properties showing applied retention label.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Retention policy configuration | PowerShell | Text export | With control documentation |
| Retention rule details | PowerShell | Text export | With control documentation |
| Content search results | Purview portal | CSV/Screenshot | Per policy |
| Label application proof | SharePoint/OneDrive | Screenshot | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| SEC 17a-4 | 3-6 year retention for electronic records | Supports compliance with 7-year retention policy |
| FINRA 4511 | Books-and-records retention | Helps meet retention obligations for AI interaction records |
| GLBA | Financial record preservation | Supports privacy and record preservation requirements |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for retention policy issues
- Proceed to [Control 3.3](../3.3/portal-walkthrough.md) for eDiscovery configuration
