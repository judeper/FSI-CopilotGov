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
- **Root Cause:** Label inheritance for Pages may not be fully supported, or the label policy scope may not include the Pages storage location.
- **Resolution:**
  1. Verify label policy scope includes all relevant locations
  2. Check if Pages support sensitivity label application in your tenant version
  3. Configure auto-labeling as a fallback for unlabeled Pages
  4. Train users to manually apply labels to Pages as a compensating control

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
