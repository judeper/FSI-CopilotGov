# Control 4.1: Copilot Admin Settings and Feature Management — Troubleshooting

Common issues and resolution steps for Copilot Control System administrative settings and feature management.

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

### Issue 3: Overview Dashboard Not Showing All Data

- **Symptoms:** The MAC > Copilot > Overview dashboard shows incomplete data — license utilization or security posture sections appear blank or show "Data not available."
- **Root Cause:** Licensing data and usage telemetry in the Copilot overview dashboard may require up to 48 hours to populate after initial configuration or after license changes. Dashboard requires appropriate reporting permissions.
- **Resolution:**
  1. Verify the administrator has the Copilot Administrator, Global Administrator, or Global Reader role.
  2. Allow 24-48 hours after initial setup or major license changes for dashboard data to populate.
  3. Check that usage analytics are not blocked by any privacy-restricting admin policies (Admin Center > Settings > Org settings > Reports).
  4. Verify the tenant has Microsoft 365 Copilot licenses assigned — the dashboard only populates for tenants with active Copilot deployments.

### Issue 4: Baseline Security Mode Conflicts with Existing Policies

- **Symptoms:** After enabling Baseline Security Mode, existing DLP policies, Conditional Access policies, or sensitivity label configurations generate conflicts or unexpected behavior.
- **Root Cause:** Baseline Security Mode applies a set of recommended security defaults that may overlap with or conflict with pre-existing custom policies configured before Baseline Security Mode was available.
- **Resolution:**
  1. Navigate to M365 Admin Center > Copilot > Settings > Security and review the specific settings applied by Baseline Security Mode.
  2. Identify which existing policies conflict with the baseline defaults.
  3. For each conflict: determine whether the existing policy or the baseline default is more restrictive. Prefer the more restrictive setting.
  4. Document the conflict and resolution in the configuration register with compliance officer review.
  5. If the baseline default is less restrictive than an existing policy: disable that specific Baseline Security Mode default and retain the custom policy.

### Issue 5: Copilot for Admins Not Available

- **Symptoms:** The Copilot for Admins interface is not visible or accessible in the M365 Admin Center for administrators who should have access.
- **Root Cause:** Copilot for Admins requires the administrator account to have a Microsoft 365 Copilot license assigned, in addition to an admin role. Without the license, the AI assistant feature is not available even for Global Administrators.
- **Resolution:**
  1. Verify that the administrator account has a Microsoft 365 Copilot license assigned in Admin Center > Users > Active users > Licenses.
  2. Confirm the account holds a qualifying admin role (Global Administrator, Copilot Administrator, or equivalent).
  3. Allow up to 24 hours after license assignment for Copilot for Admins to become available.
  4. If available after licensing, confirm the feature is not blocked by any admin tenant-level setting.

### Issue 6: Web Grounding Re-Enabled After Policy Change

- **Symptoms:** Web grounding is active despite being disabled; users see web-sourced content in Copilot responses.
- **Root Cause:** A recent admin center change may have re-enabled web grounding, or a global policy update from Microsoft changed the default.
- **Resolution:**
  1. Navigate to Admin Center > Copilot > Settings > Data and privacy and verify web grounding status.
  2. Disable web grounding if re-enabled.
  3. Check the audit log for recent changes: `Search-UnifiedAuditLog -Operations "Set-CopilotPolicy"`
  4. Set up an alert policy for Copilot configuration changes.

### Issue 7: Plugin Access Not Restricted as Expected

- **Symptoms:** Users can access non-approved plugins through Copilot, despite administrative restrictions being configured.
- **Root Cause:** Plugin access controls may not apply to all plugin types, or the restriction policy has not fully propagated.
- **Resolution:**
  1. Review the plugin access settings in M365 Admin Center > Copilot > Settings.
  2. Verify that both first-party and third-party plugin categories are restricted.
  3. Allow up to 24 hours for policy propagation.
  4. Check the Teams Admin Center for additional plugin control settings.
  5. Use Integrated Apps settings in the Admin Center for more granular control.

## Diagnostic Steps

1. **Check license status:** Verify Copilot license assignment for the affected user.
2. **Verify Office version:** Confirm the user is running a Copilot-compatible Office version.
3. **Review admin settings:** Check M365 Admin Center > Copilot > Settings for current configuration.
4. **Check Baseline Security Mode:** Verify Baseline Security Mode status in Copilot > Settings > Security.
5. **Audit recent changes:** Search for Copilot-related administrative changes in the audit log.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unauthorized users accessing Copilot with sensitive data | IT Security + Compliance — immediate license removal |
| High | Web grounding enabled in regulated environment | IT Admin — immediate reconfiguration |
| High | Baseline Security Mode disabled without documented justification | IT Admin + Compliance — re-enable or document |
| Medium | Licensed users unable to access Copilot | IT Support — troubleshoot licensing and client |
| Medium | Overview dashboard not populating | IT Admin — verify licensing and permissions |
| Low | Plugin access inconsistencies | IT Admin — policy review |

## Related Resources

- [Control 4.2: Copilot in Teams Meetings Governance](../4.2/portal-walkthrough.md)
- [Control 4.12: Change Management for Copilot Rollouts](../4.12/portal-walkthrough.md)
