# Control 4.12: Change Management for Copilot Feature Rollouts — Troubleshooting

Common issues and resolution steps for Copilot change management processes.

## Common Issues

### Issue 1: Copilot Features Rolling Out Without CAB Approval

- **Symptoms:** New Copilot features appear for general users without going through the change advisory board process.
- **Root Cause:** Organization may be on standard release (not targeted), or Microsoft pushed a change that bypassed the targeted release delay.
- **Resolution:**
  1. Verify the organization's release preference is set to "Targeted release for selected users".
  2. If on standard release, switch to targeted release to enable validation time.
  3. Monitor the Message Center proactively for "Plan for Change" announcements.
  4. If a feature rolled out unexpectedly, conduct a retrospective impact assessment.

### Issue 2: Targeted Release Group Not Reflecting Correct Users

- **Symptoms:** New features appear for users who are not in the targeted release group, or targeted release users do not receive features early.
- **Root Cause:** The targeted release group membership may be outdated or the release preference may not be correctly configured.
- **Resolution:**
  1. Review the targeted release group membership in Admin Center > Settings > Org settings > Release preferences.
  2. Update the group to include current validation team members.
  3. Allow up to 72 hours after adding users to the targeted release group.
  4. Verify that per-user targeted release is assigned, not just organizational level.

### Issue 3: Change Impact Assessments Incomplete or Missing

- **Symptoms:** Audit reveals that Copilot configuration changes were made without completing the required impact assessment.
- **Root Cause:** Process is not enforced, change owners may not be trained on the requirement, or emergency changes bypassed the process.
- **Resolution:**
  1. Retroactively complete impact assessments for undocumented changes.
  2. Implement a technical control that requires assessment sign-off before configuration changes.
  3. Provide training to change owners on the impact assessment process.
  4. For emergency changes, require a post-implementation assessment within 48 hours.

### Issue 4: Rollback Procedures Not Working as Documented

- **Symptoms:** When attempting to roll back a Copilot change, the documented rollback procedure does not restore the previous state.
- **Root Cause:** The rollback procedure may be outdated, or the change created dependencies that prevent simple reversal.
- **Resolution:**
  1. Test rollback procedures before implementing changes (in a test environment if possible).
  2. Update the rollback procedure documentation after each change.
  3. For complex changes, create detailed pre-change configuration snapshots.
  4. If rollback fails, implement a forward-fix strategy and document the issue for future reference.

## Diagnostic Steps

1. **Check release preference:** Navigate to Admin Center > Settings > Org settings > Release preferences.
2. **Review Message Center:** Check for any recent Copilot change announcements.
3. **Audit configuration changes:** Run the configuration change audit script.
4. **Verify CAB records:** Cross-reference changes against the change management log.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unauthorized change affecting compliance controls | CISO + CCO — immediate assessment |
| High | Feature rollout without CAB approval affecting regulated users | IT Change Manager + Compliance |
| Medium | Missing impact assessments for recent changes | Change Manager — retroactive assessment |
| Low | Minor process deviations | Address in next CAB meeting |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.13: Copilot Extensibility Governance](../4.13/portal-walkthrough.md)
