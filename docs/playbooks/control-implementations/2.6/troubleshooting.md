# Control 2.6: Copilot Web Search and Web Grounding Controls — Troubleshooting

Common issues and resolution steps for web search and grounding controls.

## Common Issues

### Issue 1: Web Search Toggle Not Available in Admin Center

- **Symptoms:** The web search control does not appear under Copilot settings in the Admin Center
- **Root Cause:** The web search toggle may be in a staged rollout or may require specific license configurations to appear.
- **Resolution:**
  1. Verify the Admin Center is accessed with Global Administrator role
  2. Check the Microsoft 365 roadmap for web search control availability
  3. Try accessing via direct URL: admin.microsoft.com > Settings > Copilot
  4. If unavailable, contact Microsoft support to verify feature availability for your tenant

### Issue 2: Web Content Still Appearing in Copilot Responses After Disabling

- **Symptoms:** After disabling web search, Copilot responses still appear to reference web-sourced information
- **Root Cause:** Changes may take up to 24 hours to propagate. Additionally, some Copilot features may use cached web data or the user may be referencing content that happens to also exist on the web.
- **Resolution:**
  1. Wait 24 hours after disabling and retest
  2. Have the user sign out and back in to refresh settings
  3. Verify the content is actually web-sourced (check for web citations in the response)
  4. If content appears to be from organizational sources that match web content, this is expected

### Issue 3: Users Requesting Web Search Access

- **Symptoms:** Users request web search be enabled for specific use cases (market research, competitive analysis)
- **Root Cause:** Legitimate business needs for web-sourced information in Copilot responses.
- **Resolution:**
  1. Document the specific business use case and justification
  2. Assess the risk: what data might be sent to web search in the process
  3. If approved, enable web search for a limited group via selective policy
  4. Provide training on distinguishing web-sourced vs. organizational content
  5. Monitor web search usage for the enabled group

### Issue 4: Web Search Enabled by Service Update

- **Symptoms:** Web search is found enabled after a Microsoft 365 service update, despite being previously disabled
- **Root Cause:** Service updates may occasionally reset tenant-level settings to defaults.
- **Resolution:**
  1. Immediately disable web search in Admin Center
  2. Verify the change took effect
  3. Set up monitoring (Script 1) to detect configuration changes weekly
  4. Report the issue to Microsoft support if it recurs

## Diagnostic Steps

1. **Check Admin Center:** Verify web search toggle state
2. **Test with user:** Ask Copilot a web-specific question and check for citations
3. **Review audit logs:** Run Script 3 for web search usage
4. **Check plugins:** Run Script 2 for web-accessing plugin inventory
5. **Verify propagation:** Allow 24 hours after configuration changes

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | User requests for web search access | Governance committee |
| **Medium** | Web search toggle unavailable | Microsoft support |
| **High** | Web search re-enabled without authorization | Security Operations |
| **Critical** | Sensitive data sent to web search service | CISO and incident response |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Web search configuration
- [PowerShell Setup](powershell-setup.md) — Monitoring scripts
- [Verification & Testing](verification-testing.md) — Web control validation
