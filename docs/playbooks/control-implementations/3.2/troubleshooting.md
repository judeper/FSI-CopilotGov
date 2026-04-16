# Control 3.2: Data Retention Policies for Copilot Interactions — Troubleshooting

Common issues and resolution steps for Copilot data retention policy configuration and operation.

## Common Issues

### Issue 1: Retention Policy Distribution Fails

- **Symptoms:** Policy status shows `DistributionPending` or `DistributionFailed` in Purview portal or PowerShell output.
- **Root Cause:** Location scoping conflicts with existing policies, or service provisioning delays.
- **Resolution:**
  1. Check policy status: `Get-RetentionCompliancePolicy -Identity "FSI-Copilot-Experiences-Retention" | Select DistributionStatus`
  2. If `DistributionFailed`, review error details in the Purview portal under the policy's status page.
  3. Remove and re-add any conflicting locations.
  4. Allow up to 24 hours for distribution to complete after changes.

### Issue 2: Microsoft Copilot Experiences Location Not Available

- **Symptoms:** The "Microsoft Copilot experiences" location does not appear when creating a retention policy, or only the legacy "Copilot for Microsoft 365 interactions" label is shown.
- **Root Cause:** The Purview portal UI is undergoing a gradual rollout of the restructured retention location categories. Tenants that have not yet received the update may see the legacy location name. Some tenants may still display "Copilot for Microsoft 365 interactions" as the location name — this is the same underlying location and is functionally equivalent until the rename is fully rolled out.
- **Resolution:**
  1. If the Microsoft Copilot experiences location is not visible, check whether "Copilot for Microsoft 365 interactions" appears — use this location as an interim measure if the renamed location has not yet rolled out to your tenant.
  2. Verify at least one Copilot license is assigned in the tenant (required for the location to appear).
  3. Check the Microsoft 365 Message Center for announcements about retention location UI updates in your tenant ring.
  4. If neither location is available, configure retention on Exchange, SharePoint, OneDrive, and Teams locations to provide comprehensive interim coverage while awaiting the Copilot experiences location availability.

### Issue 3: Policies Not Applying to New Location Categories After Restructuring

- **Symptoms:** Existing retention policies that targeted the legacy Copilot interaction location do not appear to cover content in the restructured Microsoft Copilot experiences category.
- **Root Cause:** When Microsoft restructured the retention location categories (consolidating various Copilot locations into Microsoft Copilot experiences, Enterprise AI Apps, and Other AI Apps), existing policies targeting legacy location names may have required updating.
- **Resolution:**
  1. Review existing Copilot-related retention policies: `Get-RetentionCompliancePolicy | Where-Object { $_.Name -like "*Copilot*" } | Select Name, CopilotLocation, DistributionStatus`
  2. If `CopilotLocation` shows a legacy value or is null for policies that should cover Copilot experiences, update the policy to target the current Microsoft Copilot experiences location.
  3. Create a new policy with the current location name if updating the existing policy causes distribution errors.
  4. Verify coverage by running a Content Search targeting the Microsoft Copilot experiences location and confirming Copilot Chat history is returned.

### Issue 4: Threaded Summaries Retained Beyond Source Content Deletion

- **Symptoms:** After deleting a Teams meeting transcript or Teams message, the Copilot-generated summary remains visible and searchable — which may appear to be an error but is actually expected behavior.
- **Root Cause:** This is by design. Copilot-generated meeting summaries and conversation summaries are retained as threaded objects in the Microsoft Copilot experiences location, independent of the source content's retention policy. Deleting a source Teams message does not delete the Copilot summary.
- **Resolution:**
  1. Confirm this is expected behavior, not a data governance gap. FINRA Rule 4511(c) requires records to be preserved in accessible format — the independent retention of summaries supports this requirement.
  2. If the intent is to delete both source and summary simultaneously (e.g., for a user under active disposal), use eDiscovery purge operations targeting both the Teams location and the Microsoft Copilot experiences location.
  3. Document this behavior in the firm's records management procedures: "Copilot-generated summaries are retained independently of their source content — disposal procedures must explicitly target both the source content location and the Microsoft Copilot experiences location."
  4. Update eDiscovery hold configurations to include the Microsoft Copilot experiences location whenever Teams content is placed on hold — this ensures threaded summaries are captured in hold operations.

### Issue 5: Retention Labels Not Applying to Copilot Content

- **Symptoms:** Auto-apply retention labels are not being applied to documents created with Copilot assistance.
- **Root Cause:** Auto-apply label policies may not detect Copilot-generated content characteristics, or the policy indexing is incomplete.
- **Resolution:**
  1. Verify the label policy is published to the correct locations, including the Microsoft Copilot experiences location for Copilot Chat content.
  2. Confirm the auto-apply condition matches the content correctly (keyword, trainable classifier, or sensitive info type).
  3. Allow up to 7 days for auto-apply policies to fully index and apply.
  4. Consider using manual labeling or default labels as an interim approach.

### Issue 6: Conflict Between Retention and Deletion Policies

- **Symptoms:** Content is being deleted before the expected retention period ends, or content is not being deleted after the retention period.
- **Root Cause:** Multiple retention policies with conflicting actions may be applied to the same content. Retention always wins over deletion per Microsoft's conflict resolution.
- **Resolution:**
  1. Review all policies affecting the same locations: `Get-RetentionCompliancePolicy | Format-List Name, *Location*`
  2. Identify overlapping policies and review their retention rules.
  3. Follow the principle that the longest retention period and "retain" action take precedence.
  4. Consolidate overlapping policies where possible to reduce complexity.

## Diagnostic Steps

1. **Check policy sync status:** `Get-RetentionCompliancePolicy | Select Name, Enabled, DistributionStatus`
2. **Review rule configuration:** `Get-RetentionComplianceRule | Select PolicyName, RetentionDuration, RetentionComplianceAction`
3. **Verify Copilot licensing:** Confirm M365 Copilot licenses in the Microsoft 365 Admin Center.
4. **Test content search:** Use Purview Content Search targeting the Microsoft Copilot experiences location to verify Copilot content is indexed and discoverable.
5. **Check threaded summary independence:** Verify that Copilot-generated summaries are searchable after source content deletion — this confirms proper independent retention behavior.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Retention policies failing to retain required records | Compliance team + Microsoft Premier Support |
| High | Policy distribution failures across tenant | Internal IT + Microsoft Support |
| High | Microsoft Copilot experiences location unavailable after 48 hours | Microsoft Support — verify tenant ring and provisioning |
| Medium | Threaded summary retention questions | Internal compliance team — review records management procedures |
| Medium | Label application delays | Monitor and re-evaluate after 7 days |
| Low | Minor policy configuration adjustments | Internal compliance team |

## Related Resources

- [Control 3.1: Copilot Interaction Audit Logging](../3.1/portal-walkthrough.md)
- [Control 3.3: eDiscovery for Copilot Content](../3.3/portal-walkthrough.md)
- Back to [Control 3.2](../../../controls/pillar-3-compliance/3.2-data-retention-policies.md)
