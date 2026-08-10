# Control 2.13: Plugin and Graph Connector Security — Troubleshooting

Common issues and resolution steps for plugin and connector security.

## Common Issues

### Issue 1: Approved Agent or Plugin Tool Not Available

- **Symptoms:** A previously approved agent or plugin tool is unavailable to users
- **Root Cause:** Agent type, user access, agent distribution, or tool scope no longer includes the affected user.
- **Resolution:**
  1. Review the agent under **Microsoft 365 Admin Center > Agents > All Agents > Registry**
  2. Check **Agents > Settings > Allowed agent types** and **User access**
  3. Where licensed, verify the plugin under **Agents > Tools > Plugins** and correct its user or group scope
  4. Allow 24 hours for policy propagation after changes

### Issue 2: Graph Connector Returning Unauthorized Content

- **Symptoms:** Users see content from Graph connectors that they should not have access to
- **Root Cause:** ACL mapping may be incorrect, or the connector may not be enforcing ACLs properly.
- **Resolution:**
  1. Review the connection under **Microsoft 365 Admin Center > Copilot > Connectors > Your Connections**
  2. Verify the ACL mapping correctly translates source system permissions to Entra ID
  3. If the access permission is wrong, delete the connection and recreate it through **Custom setup**; in-place permission changes are not supported
  4. Test with specific users to verify access restrictions

### Issue 3: Admin Consent Queue Growing Without Review

- **Symptoms:** Users submit admin consent requests that go unreviewed, blocking business app usage
- **Root Cause:** No dedicated approver or unclear ownership of the admin consent workflow.
- **Resolution:**
  1. Under **Microsoft Entra Admin Center > Enterprise apps > Consent and permissions > Admin consent settings**, assign dedicated reviewers
  2. Define SLAs for consent review (24 hours for standard, 4 hours for urgent)
  3. Configure email notifications for pending consent requests
  4. Confirm reviewers hold a role that can grant the requested permissions; reviewer assignment alone does not elevate privileges

### Issue 4: Plugin Security Assessment Blocking Business Adoption

- **Symptoms:** Business teams report that the plugin approval process takes too long
- **Root Cause:** Security assessment process may be too comprehensive for low-risk plugins.
- **Resolution:**
  1. Create tiered assessment levels based on plugin risk (data access scope, publisher reputation)
  2. Fast-track Microsoft first-party and Microsoft-certified plugins
  3. Use standardized assessment templates to streamline reviews
  4. Maintain a pre-approved plugin catalog that does not require individual review

## Diagnostic Steps

1. **Check agent status:** Review the agent in Agents > All Agents > Registry
2. **Review permissions:** Run Script 1 for plugin permission audit
3. **Test connector ACLs:** Verify access control on connector content
4. **Check consent policy:** Run Script 3 and review existing grants separately
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
