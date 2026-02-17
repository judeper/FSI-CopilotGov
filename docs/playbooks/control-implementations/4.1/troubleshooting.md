# Control 4.1: Copilot Admin Settings and Feature Management — Troubleshooting

Common issues and resolution steps for Copilot administrative settings and feature management.

## Common Issues

### Issue 1: Copilot Features Available to Unauthorized Users

- **Symptoms:** Users outside the approved deployment group can access Copilot features.
- **Root Cause:** License may have been assigned directly (not via group), or the user was added to the Copilot-licensed group inadvertently.
- **Resolution:**
  1. Run the license assignment report to identify all licensed users.
  2. Compare against the approved deployment list.
  3. Remove licenses from unauthorized users via the Admin Center or PowerShell.
  4. Implement group-based licensing to prevent manual assignment errors.

### Issue 2: Copilot Not Appearing for Licensed Users

- **Symptoms:** Users with valid Copilot licenses cannot see or access Copilot features in Office applications.
- **Root Cause:** License provisioning delay, outdated Office client, or the feature is disabled for the user's group.
- **Resolution:**
  1. Verify the user has an active Copilot license: check in Admin Center > Users > Active users.
  2. Confirm the user is running a supported Office version (Microsoft 365 Apps, current channel).
  3. Have the user sign out and back into Office to refresh license tokens.
  4. Check for any Copilot feature policies that may be blocking the user's group.
  5. Allow up to 72 hours for license provisioning to complete.

### Issue 3: Web Grounding Re-Enabled After Policy Change

- **Symptoms:** Web grounding is active despite being disabled, users see web-sourced content in Copilot responses.
- **Root Cause:** A recent admin center change may have re-enabled web grounding, or a global policy update from Microsoft changed the default.
- **Resolution:**
  1. Navigate to Admin Center > Settings > Copilot and verify web grounding status.
  2. Disable web grounding if re-enabled.
  3. Check the audit log for recent changes: `Search-UnifiedAuditLog -Operations "Set-CopilotPolicy"`
  4. Set up an alert policy for Copilot configuration changes.

### Issue 4: Plugin Access Not Restricted as Expected

- **Symptoms:** Users can access non-approved plugins through Copilot, despite administrative restrictions being configured.
- **Root Cause:** Plugin access controls may not apply to all plugin types, or the restriction policy has not fully propagated.
- **Resolution:**
  1. Review the plugin access settings in the M365 Admin Center.
  2. Verify that both first-party and third-party plugin categories are restricted.
  3. Allow up to 24 hours for policy propagation.
  4. Check the Teams Admin Center for additional plugin control settings.
  5. Use Integrated Apps settings in the Admin Center for more granular control.

## Diagnostic Steps

1. **Check license status:** Verify Copilot license assignment for the affected user.
2. **Verify Office version:** Confirm the user is running a Copilot-compatible Office version.
3. **Review admin settings:** Check M365 Admin Center > Settings > Copilot for current configuration.
4. **Audit recent changes:** Search for Copilot-related administrative changes in the audit log.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unauthorized users accessing Copilot with sensitive data | IT Security + Compliance — immediate license removal |
| High | Web grounding enabled in regulated environment | IT Admin — immediate reconfiguration |
| Medium | Licensed users unable to access Copilot | IT Support — troubleshoot licensing and client |
| Low | Plugin access inconsistencies | IT Admin — policy review |

## Related Resources

- [Control 4.2: Copilot in Teams Meetings Governance](../4.2/portal-walkthrough.md)
- [Control 4.12: Change Management for Copilot Rollouts](../4.12/portal-walkthrough.md)
