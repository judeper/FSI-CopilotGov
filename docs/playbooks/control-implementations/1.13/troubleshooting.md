# Control 1.13: Extensibility Readiness — Troubleshooting

Common issues and resolution steps for Copilot extensibility governance.

## Common Issues

### Issue 1: Third-Party Apps Installed Despite Block Policy

- **Symptoms:** Users have third-party Teams apps or Copilot extensions installed that should be blocked by the permission policy
- **Root Cause:** The app permission policy may not be assigned to all users, or the user may have been assigned a different policy that allows third-party apps. Admin-installed apps bypass user-level policies.
- **Resolution:**
  1. Verify the user's assigned app permission policy: `Get-CsOnlineUser -Identity <upn> | Select-Object TeamsAppPermissionPolicy`
  2. Check if the app was installed by an admin (admin installations are not blocked by user policies)
  3. Review the specific policy assigned to the user for third-party app settings
  4. Reassign the correct restrictive policy if the user has the wrong policy

### Issue 2: Graph Connector Ingesting Unintended Content

- **Symptoms:** Copilot responses reference content from external systems that should not be accessible, or connector is ingesting more data than expected
- **Root Cause:** Graph connector configuration may have an overly broad data scope, or the access control list (ACL) on ingested items may be too permissive.
- **Resolution:**
  1. Review the connector configuration for data scope settings
  2. Verify the ACL mapping is correctly restricting access to ingested items
  3. Adjust the connector's crawl scope to include only approved content
  4. If needed, pause the connector and re-crawl with corrected settings
  5. Test with a standard user to verify content access restrictions

### Issue 3: Custom Agent Fails Security Review

- **Symptoms:** A custom Copilot agent built in Copilot Studio fails the security review and cannot be deployed to production
- **Root Cause:** The agent may access data sources without proper authentication, expose sensitive data in responses, or lack proper error handling for edge cases.
- **Resolution:**
  1. Review the specific security findings and categorize by severity
  2. Address authentication issues by implementing proper credential management
  3. Add data masking or filtering for sensitive data in agent responses
  4. Implement input validation and error handling for edge cases
  5. Re-submit for security review after addressing all findings

### Issue 4: Extension Approval Process Causing Deployment Delays

- **Symptoms:** Business teams report long wait times for extension approvals, causing frustration and potential shadow IT risk
- **Root Cause:** The approval process may lack defined SLAs, have unclear ownership, or require too many approval steps for low-risk extensions.
- **Resolution:**
  1. Define SLAs for extension approval based on risk level (24h for low, 5 days for medium, 15 days for high)
  2. Create a pre-approved extensions list for common, low-risk Microsoft first-party extensions
  3. Implement a tiered review process — lightweight for low-risk, comprehensive for high-risk
  4. Assign a dedicated approver or approval team with backup coverage

### Issue 5: Extension Version Updates Bypass Governance

- **Symptoms:** Approved extensions receive automatic updates that change their data access scope or capabilities without re-review
- **Root Cause:** Teams app and Graph connector updates may be applied automatically, and the new version may have different permissions or capabilities.
- **Resolution:**
  1. Configure Teams admin policies to control automatic app updates where possible
  2. Implement monitoring using Script 4 to detect extension changes
  3. Establish a re-review trigger when an extension's permissions change
  4. Subscribe to Microsoft 365 Message Center for announcements about extension capability changes
  5. Maintain a version log for all approved extensions

## Diagnostic Steps

1. **Inventory current state:** Run all four scripts to get a complete picture
2. **Check policies:** Verify app permission policies are assigned to all Copilot users
3. **Review approvals:** Cross-reference active extensions against approval records
4. **Test restrictions:** Attempt to install a blocked extension to verify policies work
5. **Audit connectors:** Review each Graph connector's configuration and access scope

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Approval process delays | Governance team for process improvement |
| **Medium** | Unauthorized extensions detected on a few users | Security Operations for remediation |
| **High** | Graph connector exposing sensitive data | Security Operations and CISO |
| **Critical** | Widespread unauthorized extension deployment | CISO and governance committee immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Extension governance setup
- [PowerShell Setup](powershell-setup.md) — Extension management scripts
- [Verification & Testing](verification-testing.md) — Governance validation
- Back to [Control 1.13](../../../controls/pillar-1-readiness/1.13-extensibility-readiness.md)
