# Control 2.16: Federated Copilot Connector and MCP Governance - Portal Walkthrough

Step-by-step governance workflow for inventorying federated connectors, scoping admin enablement, capturing user authentications, and aligning MCP-based connector usage to the firm's third-party risk model.

## Prerequisites

- [Control 1.10 Vendor Risk Management](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) assessment is in place for each federated connector vendor in scope.
- [Control 2.13 Plugin and Connector Security](../../../controls/pillar-2-security/2.13-plugin-connector-security.md) is implemented to control admin-managed plugins and Graph connectors.
- DLP policies for sensitive data (Control 2.1) are evaluated for whether they apply to federated connector responses.
- A governance owner is named for federated connector posture review.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft 365 Admin Center | Agents > Settings > Allowed agent types | Tenant-wide publisher-category policy for Microsoft-published and external-publisher agents, apps, and connectors |
| Microsoft 365 Admin Center | Copilot connectors > Your connections | Connector-specific enabled state, allowed-user scope, and staged rollout |
| Microsoft Entra admin center | Enterprise applications | Captures user-credential authentications to third-party services |
| Microsoft Purview portal | Audit | Federated connector invocation events and sign-in records |

## Steps

### Step 1: Inventory the federated connector catalog

Open **Copilot connectors > Your connections** and capture the current list of federated connectors available to administrators. Record each connector's publisher, enabled state, allowed-user scope, and any **Staged rollout** group assignment. Administrative catalog visibility is inventory evidence; it does not by itself prove that end users can access a connector.

### Step 2: Set the tenant-wide publisher-category posture

Review **Agents > Settings > Allowed agent types**. Microsoft documents using the Microsoft-published and external-publisher category settings to govern whether federated connectors in those categories are enabled by default, including future connectors. These settings also affect agents and apps in the same publisher categories, so document the broader tenant impact before changing them.

Tenants that previously used `Set-FederatedConnectorToggle` may receive a Message Center post with a tenant-specific window to reapply the choice in this UX. The command-line toggle retired on **August 25, 2026**; do not use its output as evidence of current effective access or assume a universal reapplication deadline.

### Step 3: Decide connector-specific access

For each connector, decide whether to permit, restrict to a named group, or set the allowed-user scope to **No users**. Use **Staged rollout** where available for approved pilots. For FSI tenants, connectors that route to consumer-grade or unvetted services should remain unavailable to users until vendor risk has cleared them under [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md).

### Step 4: Address the user-credential authentication pattern

Document that federated connectors authenticate with end-user credentials (delegated) rather than admin-managed service principals. Update the Acceptable Use guidance to clarify whether users may authenticate personal accounts (e.g., personal Google or Notion) to a federated connector, and reflect that decision in conditional-access scope.

### Step 5: Wire DLP and audit-log review into the operating model

Federated connector responses are evaluated by DLP at the response layer, not at ingestion. Confirm that current DLP policies cover Copilot interactions and that audit-log review includes federated connector invocation events on the governance cadence.

### Step 6: Establish ongoing third-party monitoring

Federated connector vendors are third parties under OCC Bulletin 2023-17. Re-assess each enabled connector vendor on the firm's third-party monitoring cadence and capture whether the vendor's authentication, data handling, or pricing model has changed.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Disable all federated connector access: review the tenant-wide publisher-category policy, inventory all federated connectors, and set every connector's allowed-user scope to **No users**. |
| **Recommended** | Restrict federated connectors to named Entra groups, prohibit personal-account authentication on regulated workstreams, and review invocation audit logs monthly. |
| **Regulated** | All Recommended controls plus: prohibit federated connectors that route customer NPI outside approved data residency boundaries, and require quarterly third-party attestation per enabled vendor. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to automate inventory and audit collection.
- Use [Verification & Testing](verification-testing.md) to validate scoping and DLP coverage.
- Keep [Troubleshooting](troubleshooting.md) available for enablement, authentication, and audit issues.

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 2.16](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md)
