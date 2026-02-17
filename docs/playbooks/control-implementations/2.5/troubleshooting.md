# Control 2.5: Data Minimization and Grounding Scope — Troubleshooting

Common issues and resolution steps for data minimization and grounding scope controls.

## Common Issues

### Issue 1: Copilot Returning Content from Outside Grounding Scope

- **Symptoms:** Copilot responses reference content from sites not on the RSS allowed list
- **Root Cause:** RSS may not be fully propagated, content may be cached from before RSS was enabled, or the content may be in OneDrive or Exchange rather than SharePoint.
- **Resolution:**
  1. Verify RSS is enabled: `Get-SPOTenantRestrictedSearchMode`
  2. Check if content is in a workload not covered by RSS (Exchange, OneDrive personal)
  3. Allow 24-48 hours for RSS changes to fully propagate
  4. Verify the specific content source and determine if additional scoping controls are needed

### Issue 2: Grounding Scope Too Restrictive — Poor Copilot Quality

- **Symptoms:** Copilot responses are vague, incomplete, or frequently state it cannot find relevant information
- **Root Cause:** The grounding scope may be too narrow, excluding content sources needed for productive Copilot use.
- **Resolution:**
  1. Review user feedback to identify which content types are missing
  2. Evaluate whether additional sites should be added to the allowed list
  3. Submit a scope expansion request through the governance change process
  4. Balance data minimization with utility — the scope should include content needed for approved use cases

### Issue 3: Data Minimization Controls Conflicting with Business Needs

- **Symptoms:** Business teams request broader Copilot access than the current minimization controls allow
- **Root Cause:** Initial scope may have been set conservatively, and expanding use cases require broader access.
- **Resolution:**
  1. Document the specific business need and content sources required
  2. Assess the risk of expanding the grounding scope
  3. Submit the request through the governance committee for review
  4. Implement the expansion with appropriate additional controls (DLP, labels)

### Issue 4: Feature Disablement Not Taking Effect

- **Symptoms:** Copilot features disabled in Admin Center remain accessible to users
- **Root Cause:** Feature toggles may take time to propagate, or users may be using cached application states.
- **Resolution:**
  1. Verify the setting in Admin Center > Settings > Copilot
  2. Wait 24 hours for propagation
  3. Have users sign out and back in to refresh configuration
  4. Verify the user is in the correct policy group for feature restrictions

## Diagnostic Steps

1. **Check RSS status:** `Get-SPOTenantRestrictedSearchMode`
2. **Review allowed list:** `Get-SPOTenantRestrictedSearchAllowedList`
3. **Verify feature settings:** Check Admin Center Copilot configuration
4. **Test as user:** Query Copilot for known content and verify scope
5. **Review audit logs:** Check for configuration changes

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Scope expansion request | Governance committee |
| **Medium** | Controls not functioning correctly | IT Operations |
| **High** | Copilot accessing out-of-scope sensitive content | Security Operations |
| **Critical** | Data minimization controls bypassed | CISO and governance committee |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Scope configuration
- [PowerShell Setup](powershell-setup.md) — Scope management scripts
- [Verification & Testing](verification-testing.md) — Scope validation
