# Control 2.2: Sensitivity Labels and Copilot Content Classification — Troubleshooting

Common issues and resolution steps for sensitivity label enforcement with Copilot. This playbook covers label groups migration issues, agent knowledge source label gaps, and nested auto-labeling condition troubleshooting.

## Common Issues

### Issue 1: DLP Policies Stop Working After Label Groups Migration

- **Symptoms:** After migrating from parent/child label hierarchy to label groups, label-based DLP policies (Control 2.1, Type 1) no longer block Copilot from processing labeled content as expected
- **Root Cause:** DLP policies may reference the old parent label name in their conditions. After migration to label groups, the label container name changes — DLP policy conditions that used the parent label name to match all sub-labels may not automatically update to reference the new label group structure.
- **Resolution:**
  1. After completing the label groups migration, audit all DLP policies that reference sensitivity labels:
     - `Get-DlpComplianceRule | Where-Object { $_.ContentContainsSensitivityLabel -ne $null }`
  2. Verify that each policy condition correctly matches the new label or label group names
  3. Test each DLP policy with a document carrying a migrated label to confirm blocking behavior
  4. Update any DLP conditions that reference old parent label names
  5. Allow 24 hours for DLP policy changes to propagate after updates

### Issue 2: Copilot Content Not Inheriting Source Labels

- **Symptoms:** Documents created by Copilot from labeled source documents do not inherit the source label, instead receiving the default label or no label
- **Root Cause:** Label inheritance for Copilot-generated content may depend on the specific Copilot feature and Office application version. Some features may not support automatic inheritance.
- **Resolution:**
  1. Verify the label policy has inheritance settings configured correctly
  2. Update Office applications to the latest version (label inheritance requires recent builds)
  3. If automatic inheritance is not supported, configure mandatory labeling so users must select a label
  4. Document the expected behavior for each Copilot feature and communicate to users

### Issue 3: Copilot Studio Agent Response Shows an Unexpected Label

- **Symptoms:** A Copilot Studio agent surfaces a higher sensitivity label on its responses, or triggers DLP policies at a higher tier than expected based on its described purpose
- **Root Cause:** The response label is the highest-priority label across the content the agent used to generate that response. One Highly Confidential document reachable through a knowledge source can raise the label shown on responses that cite it.
- **Resolution:**
  1. Review all knowledge sources connected to the agent in Microsoft 365 admin center > Agents > All agents > [Agent]
  2. Identify the highest-labeled document or source in the knowledge base
  3. Determine whether that content should be in the agent's knowledge base:
     - If not needed: remove the high-sensitivity source from the agent's knowledge configuration
     - If needed: document the high label and confirm compliance approval is in place
  4. After removing or adjusting knowledge sources, verify the label shown on responses updates as expected
  5. For regulated environments: treat any agent knowledge source change as requiring a new knowledge source label assessment

### Issue 4: Nested Auto-Labeling Conditions Not Applying Labels Correctly

- **Symptoms:** Auto-labeling policies with nested AND/OR/NOT conditions are either over-labeling (applying labels when they shouldn't) or under-labeling (not applying when conditions are met)
- **Root Cause:** Complex nested conditions can have logic errors in how AND/OR/NOT operators are grouped. The condition builder requires careful ordering — the sequence of condition groups and the selected operator between groups determines final logic.
- **Resolution:**
  1. Run the auto-labeling policy in simulation mode and review match results
  2. For over-labeling (false positives): check NOT conditions — verify exclusion groups are correctly excluding intended paths/content types
  3. For under-labeling (false negatives): check AND conditions — verify all required conditions are actually being met by test documents; lower confidence levels if SITs are not matching
  4. Test each condition group individually before combining them:
     - Create a test policy with only one condition group, verify it matches as expected
     - Add the second condition group and verify the combined logic
  5. Review the simulation mode results for sample documents to understand which conditions are and are not matching

### Issue 5: Auto-Labeling Overriding Manually Applied Labels on Files

- **Symptoms:** Files that users manually labeled at a lower sensitivity level are being replaced by an auto-labeling policy, overriding the user's deliberate classification choice.
- **Root Cause:** Auto-labeling policies can override manually applied labels for files in SharePoint and OneDrive (Microsoft 365 Roadmap ID 558342, general availability April 2026) when the policy's **Additional label settings** page is set to **All locations**. The override applies only where the policy's label has a higher priority than the existing label — a manually applied higher-priority label is never replaced.
- **Resolution:**
  1. Review the policy's **Additional label settings** page in Microsoft Purview portal > Solutions > Information Protection > Policies > Auto-labeling policies. Select **Emails only** to limit the override to email, or clear the setting to stop overriding manually applied labels.
  2. If override behavior is undesired for specific content, add exclusion conditions (e.g., path-based NOT conditions) to the auto-labeling policy.
  3. Communicate the override behavior to users and update training materials.
  4. For regulated content where manual classification decisions must be preserved, leave the override setting off and use simulation mode to report on the mismatches instead.

### Issue 6: Users Bypassing Mandatory Labeling

- **Symptoms:** Documents found in SharePoint without sensitivity labels despite mandatory labeling policy being enabled
- **Root Cause:** Mandatory labeling is enforced client-side and may not apply to all document creation paths. Files uploaded via sync client, migrated from other systems, or created by automated processes may bypass labeling.
- **Resolution:**
  1. Enable auto-labeling policies as a safety net for unlabeled content
  2. Configure a default sensitivity label on the SharePoint document libraries that hold Copilot-accessible content — this is location-based labeling and raises files that carry a lower-priority label
  3. Run the unlabeled content detection scripts (Script 3 or Script 4) weekly to catch gaps
  4. Review upload paths and confirm all channels enforce labeling

### Issue 7: Label Conflicts with Multiple Source Documents

- **Symptoms:** When Copilot references multiple source documents with different sensitivity labels, the resulting content label is inconsistent or unexpected
- **Root Cause:** Where more than one labeled source is referenced, sensitivity label inheritance selects the highest-priority label. Support varies by surface — Copilot in Word, Copilot in PowerPoint, and Copilot in Outlook support inheritance for newly created content, and a user can replace an inherited label unless mandatory labeling and downgrade justification are configured.
- **Resolution:**
  1. Document the expected behavior: the highest-priority label wins
  2. Test multi-source scenarios with different label combinations
  3. If behavior is inconsistent, configure mandatory labeling as the backup
  4. Train users to verify the label on Copilot-generated content that references multiple sources

### Issue 8: Encrypted Label Blocking Copilot Access

- **Symptoms:** Copilot reports it cannot access content or returns incomplete responses when source documents have encryption-enabled labels
- **Root Cause:** EXTRACT (shown as **Copy**) controls whether Copilot and agents display encrypted-item text for the requesting user. With VIEW but not EXTRACT, Copilot normally does not summarize the item but can return a link. This is not a categorical access rule: OWNER includes EXTRACT, the person applying encryption is the Rights Management owner, and data-in-use, Edge, user-defined-permissions, and external-source cases have documented distinctions.
- **Resolution:**
  1. Verify the requesting user’s effective EXTRACT right and whether that user is the Rights Management owner.
  2. Test the item unopened, directly referenced where supported, and open in an Office app. For Edge, determine whether Edge DLP is deployed before treating EXTRACT as determinative.
  3. Identify external plugin/Graph connector sources; do not assume their label/encryption metadata is recognized by Microsoft 365 Copilot Chat.
  4. If the user should have access, check the encryption configuration and add the user to the authorized list. Note: in the Microsoft Purview portal and the custom permissions dialog in Word, Excel, and PowerPoint for Windows (version 2411 and later), the permission level previously called "Reviewer" is now **Restricted Editor**, "Co-Author" is now **Editor**, and "Co-Owner" is now **Owner** — use the updated names when configuring encryption permissions. Restricted Editor does not include EXTRACT (Copy); Editor and Owner do.
  5. If Copilot should not use the content, document the observed supported-surface behavior and apply a DLP, DKE, or connected-experience control appropriate to the approved design.
  6. Check whether the label carries the `BlockContentAnalysisServices` PowerShell advanced setting, which stops Office apps from sending the labeled content to connected experiences that analyze content, including Copilot.

### Issue 9: Label Analytics Showing Incomplete Data

- **Symptoms:** Label analytics reports in Purview show lower label counts than expected or data appears to be delayed
- **Root Cause:** Label analytics data has a reporting lag of up to 7 days. Additionally, label events from all workloads may not be aggregated in real-time.
- **Resolution:**
  1. Allow 7 days for data to fully populate in label analytics
  2. Cross-reference with audit log data for more current information
  3. Use PowerShell Script 2 for near-real-time label event monitoring
  4. Check service health for any Purview reporting delays

## Diagnostic Steps

1. **Check label taxonomy status:** Run Script 5 to inventory label structure and migration status
2. **Check label policies:** Run Script 1 to verify policy configuration
3. **Review label events:** Run Script 2 for recent labeling activity
4. **Scan for unlabeled content:** Run Script 3 or 4 on key sites
5. **Test inheritance:** Create test scenarios with known source labels
6. **Audit agent knowledge sources:** Review knowledge source labels for each deployed Copilot Studio agent
7. **Verify client version:** Check Office client version supports label inheritance

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Label analytics reporting delays | Monitor and recheck after 7 days |
| **Low** | Auto-labeling false positive pattern in nested conditions | DLP/label policy tuning team |
| **Medium** | Inconsistent label inheritance behavior post-migration | Information protection team |
| **Medium** | Agent response label higher than expected, causing DLP disruption | Information protection team + agent owner |
| **High** | Mandatory labeling bypassed for sensitive content | Security Operations |
| **High** | DLP policies failing after label groups migration | Security Operations + Information protection team |
| **Critical** | Encrypted content accessible through Copilot without authorization | Security incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Label configuration for Copilot including label groups and agent knowledge source label review
- [PowerShell Setup](powershell-setup.md) — Label management scripts with PnP custom app registration
- [Verification & Testing](verification-testing.md) — Label validation procedures
- Back to [Control 2.2](../../../controls/pillar-2-security/2.2-sensitivity-labels-classification.md)
