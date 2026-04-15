# Control 4.7: Copilot Feedback and Telemetry Data Governance — Troubleshooting

Common issues and resolution steps for Copilot feedback and telemetry data governance.

## Common Issues

### Issue 1: Diagnostic Data Level Not Enforced by Policy

- **Symptoms:** Users can change diagnostic data settings locally, overriding the organizational policy.
- **Root Cause:** Cloud Policy or Group Policy is not deployed to all devices, or the policy has not propagated.
- **Resolution:**
  1. Verify Cloud Policy assignment in the M365 Apps Admin Center.
  2. Check Group Policy deployment status via GPMC or Intune.
  3. Confirm the policy applies to the correct device/user groups.
  4. Allow up to 24 hours for Cloud Policy propagation.
  5. Force a policy refresh on a test device: `gpupdate /force` (for Group Policy) or restart Office apps (for Cloud Policy).

### Issue 2: Feedback Events Not Appearing in Audit Log

- **Symptoms:** Users submit feedback on Copilot responses, but no corresponding audit log entries are found.
- **Root Cause:** Copilot feedback events may have a different record type, or the audit log search is using incorrect parameters.
- **Resolution:**
  1. Search with broader parameters: try `RecordType: CopilotInteraction` instead of filtering by specific operations.
  2. Allow up to 24 hours for feedback events to appear in the audit log.
  3. Verify that audit logging is enabled for the tenant.
  4. Check Microsoft documentation for the current feedback event record type and operation name.

### Issue 3: Optional Connected Experiences Still Active

- **Symptoms:** Users report that optional connected experiences (e.g., third-party content suggestions) are still functioning despite being disabled.
- **Root Cause:** Policy may only apply to new sessions, or specific connected experiences are classified as "required" rather than "optional".
- **Resolution:**
  1. Have users restart all Office applications to apply the updated policy.
  2. Review which specific connected experiences are classified as "required" vs. "optional".
  3. Verify the Cloud Policy setting targets the correct user/device scope.
  4. Test on a clean device to rule out cached settings.

### Issue 4: DPA Version Mismatch or Missing Provisions

- **Symptoms:** During audit, the Microsoft DPA on file is outdated or does not address Copilot-specific data processing.
- **Root Cause:** Microsoft periodically updates the DPA, and the organization may not have reviewed or accepted the latest version.
- **Resolution:**
  1. Access the latest DPA from the Microsoft Service Trust Portal or licensing portal.
  2. Compare the current version on file with the latest available.
  3. Conduct a legal review of any changes, particularly those related to AI and Copilot data processing.
  4. Update the internal DPA review record and schedule the next review.

## Diagnostic Steps

1. **Check policy deployment:** Verify Cloud Policy/Group Policy is deployed to all Copilot user devices.
2. **Test client settings:** Open an Office app and navigate to File > Account > Privacy Settings.
3. **Verify audit logging:** Run a broad audit log search for the test period.
4. **Review DPA status:** Check the Service Trust Portal for the latest DPA version.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Sensitive data being shared via telemetry in violation of policy | Privacy Officer + IT Security |
| High | Policy enforcement failure across the organization | IT Admin — policy deployment review |
| Medium | DPA review overdue | Legal/Privacy team |
| Low | Minor feedback collection configuration issues | IT support |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.8: Cost Allocation and License Optimization](../4.8/portal-walkthrough.md)
- Back to [Control 4.7](../../../controls/pillar-4-operations/4.7-feedback-telemetry.md)
