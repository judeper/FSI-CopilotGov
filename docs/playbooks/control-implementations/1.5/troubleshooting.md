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
- **Root Cause:** Policies may still be in simulation mode, simulation might have completed for a single policy while overlapping active policies change the enforced result, the sensitive information type patterns may not match the content, the files may predate the relevant SIT definitions, or the policy scope may exclude the relevant locations.
- **Resolution:**
  1. Check policy mode: `Get-AutoSensitivityLabelPolicy -Identity <name>` — confirm Mode is "Enable"
  2. Review the completed simulation and then, after enforcement, inspect **Coverage by simulation context** to compare what simulation found versus what enforcement labeled
  3. Open the policy's **Labeled items** tab and switch to the **Failed** view to identify files the service could not label
  4. Verify sensitive information type definitions match your data patterns and confirm the files were created or modified after the SIT definitions were created or changed
  5. Confirm the policy scope includes the SharePoint sites and OneDrive locations where content resides
  6. Check for conflicting policies that may override auto-labeling

### Issue 3: Label Priority Conflicts

- **Symptoms:** Higher-sensitivity labels are being overridden by lower-sensitivity auto-labeling, or users can apply lower labels without justification
- **Root Cause:** Label priority values may be incorrectly ordered, or the justification requirement for downgrades may not be enabled in the label policy.
- **Resolution:**
  1. Review label priority order: `Get-Label | Sort-Object Priority | Select-Object DisplayName, Priority`
  2. Verify higher-sensitivity labels have higher priority numbers
  3. Enable downgrade justification: In the label policy, set `RequireDowngradeJustification` to `$true`
  4. Test priority behavior by attempting to apply labels in different order

### Issue 4: Encrypted-content behavior differs by user or surface

- **Symptoms:** Copilot returns a link, an incomplete response, or an unavailable-item message for encrypted sensitivity-label content.
- **Root Cause:** Copilot evaluates the requesting user’s effective EXTRACT (Copy) right; it does not make a generic service-principal access decision. VIEW without EXTRACT normally prevents summarization but can return a link. OWNER includes EXTRACT, and data-in-use, user-defined permissions, Edge, and external-source behavior have documented exceptions or limitations.
- **Resolution:**
  1. Review encryption settings on the label: `Get-Label -Identity <name> | Select-Object -ExpandProperty EncryptionRightsDefinitions`
  2. Verify the requesting user’s effective EXTRACT right and whether that user is the Rights Management owner.
  3. Test the item unopened, directly referenced where supported, and open in an Office app; record the source and surface.
  4. If Edge DLP is not deployed, test active encrypted browser-tab behavior; test external plugin/Graph connector sources separately.
  5. If the organization intends a Copilot exclusion, validate the appropriate DLP, DKE, or connected-experience control rather than relying on an untested label outcome.

### Issue 5: Label Groups or Legacy Sublabels Not Displaying Correctly

- **Symptoms:** Labels appear as standalone labels unexpectedly, or legacy sublabels do not show under the expected parent/grouping
- **Root Cause:** The tenant may still be on the legacy parent/child model, the parent label or label group transition may not be complete, or the label policy may publish the child label without the required parent container.
- **Resolution:**
  1. Verify whether the tenant is using legacy parent labels or the modern label-group scheme: `Get-Label | Select-Object DisplayName, ParentId, IsParent`
  2. If still on the legacy model, confirm both parent and child labels are included in the same label policy
  3. If the tenant is migrating, verify the **Migrate to the modern label scheme** workflow has completed and that any replacement sublabel created during migration is published as intended
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
