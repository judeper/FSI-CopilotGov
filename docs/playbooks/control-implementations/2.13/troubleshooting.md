# Control 2.13: Plugin and Graph Connector Security — Troubleshooting

Common issues and resolution steps for plugin and connector security.

## Common Issues

### Issue 1: Approved Plugin Not Working After Policy Update

- **Symptoms:** A previously approved plugin stops functioning after a Teams app permission policy update
- **Root Cause:** Policy changes may inadvertently remove the plugin from the allowlist or change the policy assignment.
- **Resolution:**
  1. Verify the plugin is on the current allowlist in Teams admin center
  2. Check the user's assigned app permission policy
  3. Re-add the plugin to the allowlist if it was inadvertently removed
  4. Allow 24 hours for policy propagation after changes

### Issue 2: Graph Connector Returning Unauthorized Content

- **Symptoms:** Users see content from Graph connectors that they should not have access to
- **Root Cause:** ACL mapping may be incorrect, or the connector may not be enforcing ACLs properly.
- **Resolution:**
  1. Review the connector's ACL configuration
  2. Verify the ACL mapping correctly translates source system permissions to Entra ID
  3. Pause the connector, correct the ACL mapping, and re-crawl
  4. Test with specific users to verify access restrictions

### Issue 3: Admin Consent Queue Growing Without Review

- **Symptoms:** Users submit admin consent requests that go unreviewed, blocking business app usage
- **Root Cause:** No dedicated approver or unclear ownership of the admin consent workflow.
- **Resolution:**
  1. Assign dedicated admin consent reviewers
  2. Define SLAs for consent review (24 hours for standard, 4 hours for urgent)
  3. Configure email notifications for pending consent requests
  4. Pre-approve common low-risk Microsoft first-party apps

### Issue 4: Plugin Security Assessment Blocking Business Adoption

- **Symptoms:** Business teams report that the plugin approval process takes too long
- **Root Cause:** Security assessment process may be too comprehensive for low-risk plugins.
- **Resolution:**
  1. Create tiered assessment levels based on plugin risk (data access scope, publisher reputation)
  2. Fast-track Microsoft first-party and Microsoft-certified plugins
  3. Use standardized assessment templates to streamline reviews
  4. Maintain a pre-approved plugin catalog that does not require individual review

## Diagnostic Steps

1. **Check plugin status:** Verify plugin is on the Teams allowlist
2. **Review permissions:** Run Script 1 for plugin permission audit
3. **Test connector ACLs:** Verify access control on connector content
4. **Check consent policy:** Run Script 3 to verify settings
5. **Review audit logs:** Search for plugin-related events

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Plugin approval delays | Governance team process improvement |
| **Medium** | Connector ACL misconfiguration | Security Operations and connector admin |
| **High** | Unauthorized content exposed through connector | Security Operations and CISO |
| **Critical** | Plugin data breach or unauthorized data exfiltration | Incident response team immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Plugin security configuration
- [PowerShell Setup](powershell-setup.md) — Security audit scripts
- [Verification & Testing](verification-testing.md) — Security validation
- Back to [Control 2.13](../../../controls/pillar-2-security/2.13-plugin-connector-security.md)
