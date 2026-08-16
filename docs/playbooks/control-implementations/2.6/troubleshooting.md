# Control 2.6: Copilot Web Search and Web Grounding Controls — Troubleshooting

Common issues and resolution steps for web search and grounding controls.

## Common Issues

### Issue 1: Web Search Toggle Not Found in the Microsoft 365 Admin Center

- **Symptoms:** Administrators look for a web search on/off toggle under Copilot settings in the Microsoft 365 admin center and cannot find one
- **Root Cause:** Microsoft states the scenario is not configured in the Microsoft 365 admin center. The admin center page provides a shortcut to the **Allow web search in Copilot** policy in the Cloud Policy service for Microsoft 365 Apps, which is where the setting actually lives.
- **Resolution:**
  1. Go to Admin Center > Copilot > Settings > Data Access > **Web search for Microsoft 365 Copilot and Microsoft 365 Copilot Chat** and follow the shortcut
  2. Alternatively, go directly to `https://config.office.com` > Customization > Policy Management and configure **Allow web search in Copilot**
  3. Verify the signed-in account holds Office Apps Administrator (Microsoft's recommended role), Security Administrator, or Entra Global Admin
  4. If the Cloud Policy setting itself is unavailable, contact Microsoft support to verify feature availability for the tenant

### Issue 2: Web Content Still Appearing in Copilot Responses After Disabling

- **Symptoms:** After configuring the Cloud Policy to off, Copilot responses still appear to reference web-sourced information
- **Root Cause:** Cloud Policy is applied on Office app check-in and restart, not instantly. Microsoft documents a check-in of roughly every 90 minutes for users covered by a policy configuration, and about every 24 hours otherwise, with the policy taking effect the next time the Office app is restarted. The user may also be referencing organizational content that happens to also exist on the web.
- **Resolution:**
  1. Confirm the user is a member of a group assigned to the policy configuration
  2. Have the user close and restart the Office app (or sign out and back in) and retest
  3. Allow up to 24 hours for users not covered by an assigned policy configuration, then retest
  4. Verify the content is actually web-sourced (check for web citations in the response — Microsoft states these appear in Microsoft 365 Copilot Chat and remain in the thread for 24 hours)
  5. If content appears to be from organizational sources that match web content, this is expected

### Issue 3: Users Requesting Web Search Access

- **Symptoms:** Users request web search be enabled for specific use cases (market research, competitive analysis)
- **Root Cause:** Legitimate business needs for web-sourced information in Copilot responses.
- **Resolution:**
  1. Document the specific business use case and justification
  2. Assess the risk: what data might be sent to web search in the process
  3. If approved, enable web search for a limited group via selective policy
  4. Provide training on distinguishing web-sourced vs. organizational content
  5. Monitor web search usage for the enabled group

### Issue 4: Web Search Found Enabled Unexpectedly

- **Symptoms:** Web search is found enabled for users despite an earlier governance decision to disable it
- **Root Cause:** In commercial tenants, web search is available by default when the **Allow web search in Copilot** policy has not been configured. A policy configuration that is deleted, unassigned, or scoped to a group that no longer contains the affected users returns those users to the default behavior.
- **Resolution:**
  1. Configure or reinstate the **Allow web search in Copilot** Cloud Policy to off in the Microsoft 365 Apps admin center
  2. Verify the policy configuration's assigned Microsoft Entra security groups still cover all in-scope users
  3. Verify the change took effect after an Office app restart
  4. Set up monitoring (Script 1) to detect configuration changes weekly
  5. Report the issue to Microsoft support if the configured policy does not apply

## Diagnostic Steps

1. **Check Cloud Policy:** Verify the **Allow web search in Copilot** policy state and its assigned groups
2. **Test with user:** Ask Copilot a web-specific question and check for citations
3. **Review audit logs:** Run Script 3 for web search usage, and corroborate with Purview DSPM for AI activity explorer
4. **Check plugins:** Run Script 2 for web-accessing plugin inventory
5. **Verify propagation:** Restart the Office app; allow up to 24 hours for users not covered by an assigned policy configuration

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | User requests for web search access | Governance committee |
| **Medium** | Web search Cloud Policy unavailable or not applying | Microsoft support |
| **High** | Web search re-enabled without authorization | Security Operations |
| **Critical** | Sensitive data sent to web search service | CISO and incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Web search configuration
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Web control validation
- Back to [Control 2.6](../../../controls/pillar-2-security/2.6-web-search-controls.md)
