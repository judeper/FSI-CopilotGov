# Control 2.11: Copilot Pages Security and Sharing Controls — Troubleshooting

Common issues and resolution steps for Copilot Pages security.

## Common Issues

### Issue 1: Pages Sharing Settings Not Restrictive Enough

- **Symptoms:** Users can share Copilot Pages more broadly than governance policy allows
- **Root Cause:** Pages sharing may inherit tenant-level sharing defaults if specific Pages controls are not configured.
- **Resolution:**
  1. Review and adjust tenant-level sharing settings if they affect Pages
  2. Configure Pages-specific sharing controls in Admin Center > Copilot > Pages
  3. Apply DLP policies to Pages content as an additional safeguard
  4. Communicate sharing expectations to Copilot users through training

### Issue 2: Sensitivity Labels Not Applied to Pages

- **Symptoms:** Copilot Pages are created without sensitivity labels despite mandatory labeling policies
- **Root Cause:** SharePoint and OneDrive may not be enabled for sensitivity labels, or the label publishing policy scope may not include the Pages storage location. Automatic and recommended labeling aren't supported for Pages, so unlabeled content is never auto-labeled. Copilot Notebooks don't have Notebook-level sensitivity labels at all — they share the user-owned container with Pages and Loop My workspace.
- **Resolution:**
  1. Confirm sensitivity labels are enabled for SharePoint and OneDrive, and that the label publishing policy scope includes the relevant locations
  2. If Pages should never be left unlabeled, configure mandatory labeling or a default document label in the label publishing policy — automatic and recommended labeling can't be used as a substitute
  3. Train users to manually apply published labels to Pages as the primary compensating control
  4. For Notebooks, document that sensitivity labels aren't available as a Notebook-level control and rely on DLP policies as the compensating control instead

### Issue 3: Pages Content Not Under Retention

- **Symptoms:** Copilot Pages content is deleted without being subject to retention holds
- **Root Cause:** Retention policies may not include the Copilot Pages storage location by default.
- **Resolution:**
  1. Review retention policy scope and verify it includes Copilot Pages locations
  2. Extend existing retention policies or create new ones targeting Pages
  3. Test retention by attempting to delete a Page under policy coverage
  4. Monitor retention compliance using the Purview retention reporting

### Issue 4: Users Creating Pages with Sensitive Content Inadvertently

- **Symptoms:** Copilot Pages contain sensitive information that users did not intend to persist or share
- **Root Cause:** Users may not understand that Pages persist content and can be shared. Copilot may include sensitive data from source interactions in the Page.
- **Resolution:**
  1. Update training to explain Pages persistence and sharing behavior
  2. Implement DLP policies to detect sensitive content in Pages
  3. Configure alerts for Pages containing sensitive information types
  4. Consider disabling Pages creation if the risk is too high for your environment

### Issue 5: Departed User Content Access and Recycle Bin

- **Symptoms:** After a user's account is deleted, their Copilot Pages and Notebooks content becomes inaccessible, or content that should have been preserved for regulatory or legal purposes has been permanently deleted.
- **Root Cause:** When a user account is deleted, their SharePoint Embedded container follows the OneDrive deletion lifecycle: it stays active for the tenant's configurable deleted-user retention period (30 days by default), then moves to a separate, fixed 93-day recycle-bin period before permanent deletion. Because the access handoff for these containers isn't automatic (unlike OneDrive's automatic manager delegation), it's easy to miss the active retention window and let content reach — or expire out of — the recycle bin before anyone is notified.
- **Resolution:**
  1. Before deleting a departing user's account, check whether their Pages/Notebooks content is subject to legal hold, regulatory retention, or active eDiscovery cases.
  2. If preservation is required, place a hold on the user's SharePoint Embedded container before account deletion.
  3. Update the offboarding checklist to include a "Copilot Pages/Notebooks preservation check" step: add a custodian as a container owner to copy content, or use SharePoint PowerShell `Set-SPOContainer -CurrentPrincipalOwner <upn> -NewPrincipalOwner <upn>` to permanently reassign the container, as soon as the user departs rather than waiting for the active retention window to run out.
  4. If content has already entered the recycle bin, an administrator can restore the container during the fixed 93-day recycle-bin period; unlike the active retention period, this window is fixed and can't be extended.
  5. To lengthen the window before content reaches the recycle bin, configure the tenant's deleted-user retention period with `Set-SPOTenant -OrphanedPersonalSitesRetentionPeriod <days>` — the 93-day recycle-bin period itself is fixed and not configurable.

### Issue 6: Information Barriers Not Enforced on Pages

- **Symptoms:** Users subject to Information Barriers can share or access Copilot Pages content that should be segmented by IB policy.
- **Root Cause:** Information Barriers are not supported for SharePoint Embedded content, including Copilot Pages and Notebooks. IB policies do not apply to this storage type.
- **Resolution:**
  1. Disable Copilot Pages and Notebooks creation for all user populations subject to Information Barriers.
  2. Communicate this limitation to compliance and legal teams.
  3. Monitor for any attempts by IB-segmented users to create or access Pages content.
  4. Document this limitation in the firm's IB policy implementation records.

## Diagnostic Steps

1. **Check sharing settings:** Verify Pages sharing configuration in Admin Center
2. **Review activity logs:** Run Script 2 to track Pages creation and sharing
3. **Check labels:** Verify sensitivity labels on recently created Pages
4. **Verify retention:** Check retention policy scope for Pages coverage
5. **Test controls:** Create a test Page and verify all security controls apply

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor sharing configuration adjustments needed | SharePoint team |
| **Medium** | Pages not covered by retention policies | Compliance team |
| **High** | Sensitive data found in broadly shared Pages | Security Operations |
| **Critical** | Regulated content exposed through Pages sharing | CISO and Compliance Officer |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Pages security configuration
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Security validation
- Back to [Control 2.11](../../../controls/pillar-2-security/2.11-copilot-pages-security.md)
