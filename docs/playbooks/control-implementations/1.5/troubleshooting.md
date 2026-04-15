# Control 1.5: Sensitivity Label Taxonomy Review — Troubleshooting

Common issues and resolution steps for sensitivity label taxonomy management.

## Common Issues

### Issue 1: Labels Not Appearing for Users

- **Symptoms:** Users report that sensitivity labels are not visible in Office applications or the label bar is missing entirely
- **Root Cause:** Label policies may not be scoped to the affected user groups, or the Office version does not support built-in sensitivity labeling.
- **Resolution:**
  1. Verify the user is included in an active label policy using `Get-LabelPolicy`
  2. Check that the label policy is enabled and in enforcement mode
  3. For desktop Office apps, verify the Office version supports built-in sensitivity labeling (Office 365 Apps, version 2111+ recommended)
  4. Force a policy refresh: In Office, go to Sensitivity button > Help and Feedback > Reset Settings
  5. Allow up to 24 hours for policy propagation to new user groups

### Issue 2: Auto-Labeling Not Applying Labels

- **Symptoms:** Auto-labeling policies are configured but documents are not being labeled automatically
- **Root Cause:** Policies may still be in simulation mode, the sensitive information type patterns may not match the content, or the policy scope may exclude the relevant locations.
- **Resolution:**
  1. Check policy mode: `Get-AutoSensitivityLabelPolicy -Identity <name>` — confirm Mode is "Enable"
  2. Review simulation results to verify the policy matches expected content
  3. Verify sensitive information type definitions match your data patterns
  4. Confirm the policy scope includes the SharePoint sites and OneDrive locations where content resides
  5. Check for conflicting policies that may override auto-labeling

### Issue 3: Label Priority Conflicts

- **Symptoms:** Higher-sensitivity labels are being overridden by lower-sensitivity auto-labeling, or users can apply lower labels without justification
- **Root Cause:** Label priority values may be incorrectly ordered, or the justification requirement for downgrades may not be enabled in the label policy.
- **Resolution:**
  1. Review label priority order: `Get-Label | Sort-Object Priority | Select-Object DisplayName, Priority`
  2. Verify higher-sensitivity labels have higher priority numbers
  3. Enable downgrade justification: In the label policy, set `RequireDowngradeJustification` to `$true`
  4. Test priority behavior by attempting to apply labels in different order

### Issue 4: Encryption Blocking Copilot Content Access

- **Symptoms:** Copilot cannot access content protected by encrypted sensitivity labels, resulting in incomplete responses or "I don't have access to that content" messages
- **Root Cause:** Sensitivity labels with encryption restrict access to specified users or groups. If the Copilot service principal does not have access rights, it cannot read encrypted content.
- **Resolution:**
  1. Review encryption settings on the label: `Get-Label -Identity <name> | Select-Object -ExpandProperty EncryptionRightsDefinitions`
  2. Verify that Copilot respects the user's access rights (Copilot accesses content as the user, not as a service)
  3. Confirm the user querying Copilot has the required rights to the encrypted content
  4. If Copilot should not access certain encrypted content, this is expected behavior — document it as intended

### Issue 5: Sub-Labels Not Displaying Correctly

- **Symptoms:** Sub-labels appear as standalone labels or do not show under the correct parent label
- **Root Cause:** Sub-label parent assignment may be incorrect, or the label policy may publish the sub-label but not the parent label.
- **Resolution:**
  1. Verify parent-child relationship: `Get-Label | Where-Object ParentId -ne $null`
  2. Confirm both parent and child labels are included in the same label policy
  3. Check that the parent label is not disabled while the child label is enabled
  4. Force a client-side policy refresh and restart the Office application

## Diagnostic Steps

1. **Export full taxonomy:** Run Script 1 and review the complete label hierarchy
2. **Verify policy assignment:** Check which policies apply to the affected user
3. **Test label application:** Manually apply and remove labels to verify behavior
4. **Review audit logs:** Search for label-related events using `Search-UnifiedAuditLog -RecordType SensitivityLabelAction`
5. **Check client version:** Verify Office client supports current label features (minimum version requirements)

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Individual user label display issues | IT Help Desk for client troubleshooting |
| **Medium** | Auto-labeling not functioning for a content type | Information Protection team |
| **High** | Label priority conflicts causing incorrect classification | Compliance team and governance committee |
| **Critical** | Encryption blocking legitimate Copilot access tenant-wide | Microsoft support and CISO |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Taxonomy review steps
- [PowerShell Setup](powershell-setup.md) — Label management scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
- Back to [Control 1.5: Sensitivity Label Taxonomy Review](../../../controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md)
