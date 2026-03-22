# Control 4.13: Copilot Extensibility and Agent Operations Governance — Troubleshooting

Common issues and resolution steps for Copilot extensibility governance and agent operations.

## Common Issues

### Issue 1: Unauthorized Plugins Accessible to Users

- **Symptoms:** Users can access and use Copilot plugins that are not on the approved list.
- **Root Cause:** User consent settings may allow self-service consent, or the admin-approved plugin list is not enforced.
- **Resolution:**
  1. Navigate to Microsoft Entra admin center > Enterprise applications > Consent and permissions.
  2. Set "Users can consent to apps" to **No** to require admin approval.
  3. Review the Integrated Apps settings in the Microsoft 365 admin center for any overrides.
  4. Audit the current plugin list and remove any unauthorized apps.
  5. Communicate the approved plugin catalog to all Copilot users.

### Issue 2: Plugin Approval Workflow Bottleneck

- **Symptoms:** Plugin requests are stuck in the approval queue for extended periods, frustrating users.
- **Root Cause:** Approval chain is too long, approvers are unavailable, or the volume of requests exceeds capacity.
- **Resolution:**
  1. Add backup approvers at each level of the approval chain.
  2. Set auto-escalation rules for requests pending more than the SLA period (5 business days).
  3. Create a fast-track process for plugins from Microsoft's verified catalog.
  4. Pre-approve categories of low-risk plugins to reduce the review burden.

### Issue 3: Ownerless or Unmanaged Agents in the Registry

- **Symptoms:** Agents appear in the Registry without an assigned owner or approval evidence.
- **Root Cause:** Publishing or sharing occurred without the governance workflow being completed.
- **Resolution:**
  1. Review **Agents > All agents / Registry**.
  2. Assign an owner where appropriate or block the agent.
  3. Record remediation in the governance register.

### Issue 4: Graph Connector Exposing Sensitive Data to Copilot

- **Symptoms:** Copilot surfaces sensitive information from a Graph connector that should not be accessible.
- **Root Cause:** The Graph connector's access controls are insufficient, or the data was not properly classified before connection.
- **Resolution:**
  1. Immediately disable the Graph connector if sensitive data exposure is confirmed.
  2. Conduct a data sensitivity assessment for the connector's content.
  3. Apply access controls that restrict which users can access connector data through Copilot.
  4. Apply sensitivity labels to connector content if supported.
  5. Re-enable the connector only after appropriate controls are in place.

### Issue 5: Plugin Permissions Exceeding Least Privilege

- **Symptoms:** Permission audit reveals plugins with broader access than necessary (e.g., read-write access when read-only is sufficient).
- **Root Cause:** Initial consent granted excessive permissions, or permissions were not reviewed during the approval process.
- **Resolution:**
  1. Review the permission audit report and identify over-privileged apps.
  2. Revoke excessive permissions where possible without breaking functionality.
  3. Work with plugin vendors to understand minimum required permissions.
  4. Update the Plugin Risk Assessment template to include a permissions review step.
  5. Implement a quarterly permissions review cycle.

## Diagnostic Steps

1. **Check user consent settings:** Microsoft Entra admin center > Enterprise applications > Consent and permissions.
2. **Review plugin catalog:** Microsoft 365 admin center > Settings > Integrated apps.
3. **Review agent inventory:** Microsoft 365 admin center > Agents > All agents / Registry.
4. **Audit app permissions:** Run the permission audit script (Script 3 from PowerShell Setup).
5. **Test user experience:** Log in as a standard user and verify plugin and agent access restrictions.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unauthorized plugin exposing sensitive data | IT Security + Compliance — immediate remediation |
| High | Graph connector data exposure | IT Admin — disable connector + data classification |
| Medium | Plugin approval workflow delays | IT Management — process optimization |
| Low | Minor permission excess | Schedule for next quarterly review |

## Related Resources

- [Control 4.1: Copilot Admin Settings](../4.1/portal-walkthrough.md)
- [Control 4.12: Change Management](../4.12/portal-walkthrough.md)
- [Control 2.13: Plugin and Graph Connector Security](../2.13/portal-walkthrough.md)
