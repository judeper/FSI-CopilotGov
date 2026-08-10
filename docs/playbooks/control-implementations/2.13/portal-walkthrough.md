# Control 2.13: Plugin and Graph Connector Security — Portal Walkthrough

Step-by-step portal configuration for securing Copilot plugins and Microsoft Graph connectors.

## Prerequisites

- Microsoft 365 Admin Center access with an appropriate agent-management role
- Global Administrator access for Microsoft Entra consent-workflow configuration
- Plugin security review process approved by governance committee

## Steps

### Step 1: Review the Agent Registry

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > All Agents > Registry

Review Microsoft agents, external partner-built agents, agents published by your organization, and agents shared by creators. Confirm that each broadly available agent has an owner and approval record, and block, uninstall, or delete agents that do not meet policy.

### Step 2: Configure Agent Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > Settings

Configure the settings required by the governance tier:
- **Allowed agent types** — disable external publishers until vendor review is complete
- **Sharing** — restrict broad sharing to the designated governance group
- **User access** — scope agent access to approved users and groups
- **Policy templates and agent management rules** — apply licensed lifecycle controls where available

### Step 3: Govern Plugins, Skills, and MCP Servers

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > Tools

Review the Registry, Plugins, and Requests views available for the tenant:
- Block non-Microsoft plugins for Baseline
- Scope approved plugins and skills to authorized users and groups
- Approve or reject bring-your-own MCP server requests with a recorded rationale
- Record the requested Microsoft Entra permissions before granting consent

Tenant-wide Agent Tools controls require Microsoft 365 E7 or Microsoft Agent 365. Where the Tools surface is unavailable, retain the approved inventory and enforce the applicable agent, integrated-app, and Entra controls separately.

### Step 4: Review Copilot Connector Security

**Portal:** Microsoft 365 Admin Center
**Path:** Copilot > Connectors > Your Connections

For each connection, review authentication, sync health, schema, and access permissions. Confirm that **Only people with access to this data source** is selected when source ACLs must be enforced. If permissions are incorrect, delete the connection and recreate it through **Custom setup**; Microsoft does not currently support changing access permissions in place.

### Step 5: Configure Consent and Approval Workflows

**Portal:** Microsoft Entra Admin Center
**Path:** Identity > Applications > Enterprise apps > Consent and permissions

Configure app consent policies to control how plugins request permissions:
- In **User consent settings**, select **Do not allow user consent**
- In **Admin consent settings**, enable requests and assign qualified reviewers
- Review and revoke existing grants separately; changing user consent settings affects only future consent operations

### Step 6: Document Plugin Security Standards

Create plugin security standards document covering:
- Required security certifications for approved plugins
- Data access review requirements before approval
- Plugin testing procedures (security scan, data flow analysis)
- Periodic review cadence for approved plugins

### Step 7: Separate Configuration and Usage Evidence

Use the Agent Registry and **Agents > Tools** inventory as the evidence of which tools are enabled, blocked, and scoped to users. Retain the associated approval record with that export.

For usage telemetry:

1. In Microsoft Purview **Audit**, search for the `CopilotInteraction` operation and record type.
2. Export the results and filter the audit data offline by exact `AppIdentity`.
3. Accept Microsoft 365 Copilot plugin evidence only when the `AppIdentity` is in the approved application inventory and `AISystemPlugin.ID` is in the approved plugin inventory.
4. Keep `Copilot.Security.SecurityCopilot` and all unknown application identities in a separate, non-Microsoft-365-Copilot evidence set.

Do not use `EnablePlugin` by itself as Microsoft 365 Copilot evidence. Microsoft lists that operation for both Microsoft 365 Copilot administration and Security Copilot platform management. See Script 4 in [PowerShell Setup](powershell-setup.md) for a fail-closed export.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Block external agents and non-Microsoft tools; disable user consent; do not deploy external Copilot connectors |
| **Recommended** | Security review for new agents and tools; connector ACL verification; quarterly inventory review |
| **Regulated** | Formal third-party assessment; documented tool and connector telemetry; monthly review with governance approval |

## Microsoft Guidance

- [Manage agent registry in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry)
- [Manage tools for agents in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-tools-for-agent)
- [Manage access permissions for connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/manage-access-permissions)
- [Configure how users consent to applications](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-user-consent)
- [Configure the admin consent workflow](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/configure-admin-consent-workflow)
- [Audit logs for Copilot and AI applications](https://learn.microsoft.com/en-us/purview/audit-copilot)
- [Microsoft 365 audit log activities](https://learn.microsoft.com/en-us/purview/audit-log-activities)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for plugin management automation
- See [Verification & Testing](verification-testing.md) to validate plugin security
- Review Control 1.13 for Extensibility Readiness
- Back to [Control 2.13](../../../controls/pillar-2-security/2.13-plugin-connector-security.md)
