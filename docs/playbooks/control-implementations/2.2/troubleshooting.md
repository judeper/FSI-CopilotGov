# Control 2.2: Sensitivity Labels and Copilot Content Classification — Troubleshooting

Common issues and resolution steps for sensitivity label enforcement with Copilot. This playbook covers label groups migration issues, agent label inheritance gaps, and nested auto-labeling condition troubleshooting.

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

### Issue 3: Copilot Studio Agent Inheriting Unexpected Label

- **Symptoms:** A Copilot Studio agent appears to trigger DLP policies or label enforcement at a higher sensitivity level than expected based on its described purpose
- **Root Cause:** The agent is inheriting the highest sensitivity label from all connected knowledge sources, including sources that may have been labeled at a higher tier than intended. One Highly Confidential document in a knowledge source elevates the entire agent's inherited label.
- **Resolution:**
  1. Review all knowledge sources connected to the agent in MAC > Agents > All agents / Registry > [Agent] > Details
  2. Identify the highest-labeled document or source in the knowledge base
  3. Determine whether that content should be in the agent's knowledge base:
     - If not needed: remove the high-sensitivity source from the agent's knowledge configuration
     - If needed: document the high inherited label and confirm compliance approval is in place
  4. After removing or adjusting knowledge sources, verify the effective inherited label updates as expected
  5. For regulated environments: treat any agent knowledge source change as requiring a new label inheritance assessment

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

### Issue 4: Auto-Labeling Overriding Manually Applied Labels on Files

- **Symptoms:** Files that users manually labeled at a lower sensitivity level are being upgraded by an auto-labeling policy, overriding the user's deliberate classification choice.
- **Root Cause:** Auto-labeling can now override manually applied labels for files (not just emails). If an auto-labeling policy is configured to apply a higher-priority label, it will override the existing manual label on files.
- **Resolution:**
  1. Review auto-labeling policy priority and override settings in Purview > Information Protection > Auto-labeling.
  2. If override behavior is undesired for specific content, add exclusion conditions (e.g., path-based NOT conditions) to the auto-labeling policy.
  3. Communicate the new override behavior to users and update training materials.
  4. For regulated content where manual classification decisions must be preserved, configure the auto-labeling policy to not override manually applied labels (if the option is available) or use monitoring mode.

### Issue 5: Users Bypassing Mandatory Labeling

- **Symptoms:** Documents found in SharePoint without sensitivity labels despite mandatory labeling policy being enabled
- **Root Cause:** Mandatory labeling is enforced client-side and may not apply to all document creation paths. Files uploaded via sync client, migrated from other systems, or created by automated processes may bypass labeling.
- **Resolution:**
  1. Enable auto-labeling policies as a safety net for unlabeled content
  2. Configure a default label at the site level for documents without labels
  3. Run the unlabeled content detection scripts (Script 3 or Script 4) weekly to catch gaps
  4. Review upload paths and ensure all channels enforce labeling

### Issue 6: Label Conflicts with Multiple Source Documents

- **Symptoms:** When Copilot references multiple source documents with different sensitivity labels, the resulting content label is inconsistent or unexpected
- **Root Cause:** When multiple sources with different labels are combined, the inheritance behavior may default to the highest label or may be unpredictable depending on the Copilot feature.
- **Resolution:**
  1. Document the expected behavior: most restrictive label should win
  2. Test multi-source scenarios with different label combinations
  3. If behavior is inconsistent, configure mandatory labeling as the backup
  4. Train users to verify the label on Copilot-generated content that references multiple sources

### Issue 7: Encrypted Label Blocking Copilot Access

- **Symptoms:** Copilot reports it cannot access content or returns incomplete responses when source documents have encryption-enabled labels
- **Root Cause:** Labels with encryption restrict access to authorized users only. Copilot accesses content as the current user, so if the user has decryption rights, Copilot should work. If not, Copilot is correctly blocked.
- **Resolution:**
  1. Verify the user has the required rights for the encrypted content
  2. If the user should have access, check the encryption configuration and add the user to the authorized list. Note: the permission level previously called "Reviewer" is now **Restricted Editor**, and "Co-author" is now **Editor** — use the updated names when configuring encryption permissions.
  3. If Copilot should not access the encrypted content, this is expected behavior — document it
  4. Consider using labels without encryption but with other protections (content marking, DLP) if Copilot access is required

### Issue 8: Label Analytics Showing Incomplete Data

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
| **Medium** | Agent inheriting unexpected label causing DLP disruption | Information protection team + agent owner |
| **High** | Mandatory labeling bypassed for sensitive content | Security Operations |
| **High** | DLP policies failing after label groups migration | Security Operations + Information protection team |
| **Critical** | Encrypted content accessible through Copilot without authorization | Security incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Label configuration for Copilot including label groups and agent inheritance
- [PowerShell Setup](powershell-setup.md) — Label management scripts with PnP custom app registration
- [Verification & Testing](verification-testing.md) — Label validation procedures
- Back to [Control 2.2](../../../controls/pillar-2-security/2.2-sensitivity-labels-classification.md)
