# Control 2.5: Data Minimization and Grounding Scope — Troubleshooting

Common issues and resolution steps for data minimization and grounding scope controls.

## Common Issues

### Issue 1: Copilot Returning Content from Outside Grounding Scope

- **Symptoms:** Copilot responses reference content from sites that are restricted or not on the RSS allowed list
- **Root Cause:** Neither Restricted Content Discovery (RCD) nor Restricted SharePoint Search (RSS) is a security boundary. Microsoft documents that users continue to see content they own, recently accessed, or that was shared with them directly or via Teams/Outlook. Index propagation can also lag, and the content may be in OneDrive or Exchange rather than SharePoint.
- **Resolution:**
  1. Confirm the content is not owned by, recently accessed by, or directly shared with the test user — these are documented exceptions, not failures
  2. Verify RCD on the site: `Get-SPOSite -Identity <site-url> | Select RestrictContentOrgWideSearch`
  3. Verify RSS mode where still in use: `Get-SPOTenantRestrictedSearchMode`
  4. Allow time for index propagation. Microsoft states RSS takes effect within about an hour; RCD propagation depends on site size and can take more than a week for sites with over 500,000 items
  5. Check if content is in a workload not covered by these controls (Exchange, OneDrive personal)
  6. Verify the specific content source and determine if permissions, sensitivity labels, or DLP are the appropriate control

### Issue 2: Grounding Scope Too Restrictive — Poor Copilot Quality

- **Symptoms:** Copilot responses are vague, incomplete, or frequently state it cannot find relevant information
- **Root Cause:** The grounding scope may be too narrow, excluding content sources needed for productive Copilot use.
- **Resolution:**
  1. Review user feedback to identify which content types are missing
  2. Evaluate whether Restricted Content Discovery should be removed from specific sites, or whether additional sites should be added to a remaining RSS allowed list
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

1. **Check RCD status for a site:** `Get-SPOSite -Identity <site-url> | Select RestrictContentOrgWideSearch`
2. **Report RCD coverage across the tenant:** `Start-SPORestrictedContentDiscoverabilityReport` then `Get-SPORestrictedContentDiscoverabilityReport`
3. **Check RSS status (where still in use):** `Get-SPOTenantRestrictedSearchMode`
4. **Review allowed list:** `Get-SPOTenantRestrictedSearchAllowedList`
5. **Verify feature settings:** Check Admin Center Copilot configuration
6. **Test as user:** Query Copilot for known content and verify scope
7. **Review audit logs:** Check for configuration changes, including RCD enable/disable and justification events in Microsoft Purview audit log activities

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
- Back to [Control 2.5](../../../controls/pillar-2-security/2.5-data-minimization-grounding-scope.md)
