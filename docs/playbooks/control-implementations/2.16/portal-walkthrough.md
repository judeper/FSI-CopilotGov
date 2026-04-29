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
| Microsoft 365 Admin Center | Copilot > Settings > Connectors / Integrations | Tenant-level enablement and per-connector scoping for federated connectors |
| Microsoft 365 Admin Center | Copilot > Agents and connectors inventory | Discovery of which federated connectors are available and which are user-authenticated |
| Microsoft Entra admin center | Enterprise applications | Captures user-credential authentications to third-party services |
| Microsoft Purview portal | Audit | Federated connector invocation events and sign-in records |

## Steps

### Step 1: Inventory the federated connector catalog

Open the M365 Admin Center connector / integrations surface and capture the current list of federated (MCP) connectors available to the tenant. Connectors are commonly enabled by default — record the default state and the per-connector posture.

### Step 2: Decide enablement posture per connector

For each connector, decide whether to permit, restrict to a named group, or disable. For FSI tenants, default-enabled connectors that route to consumer-grade or unvetted services should be restricted until vendor risk has cleared them under [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md).

### Step 3: Address the user-credential authentication pattern

Document that federated connectors authenticate with end-user credentials (delegated) rather than admin-managed service principals. Update the Acceptable Use guidance to clarify whether users may authenticate personal accounts (e.g., personal Google or Notion) to a federated connector, and reflect that decision in conditional-access scope.

### Step 4: Wire DLP and audit-log review into the operating model

Federated connector responses are evaluated by DLP at the response layer, not at ingestion. Confirm that current DLP policies cover Copilot interactions and that audit-log review includes federated connector invocation events on the governance cadence.

### Step 5: Establish ongoing third-party monitoring

Federated connector vendors are third parties under OCC Bulletin 2023-17. Re-assess each enabled connector vendor on the firm's third-party monitoring cadence and capture whether the vendor's authentication, data handling, or pricing model has changed.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Inventory all federated connectors and disable any whose vendor has not cleared third-party risk review. |
| **Recommended** | Restrict federated connectors to named Entra groups, prohibit personal-account authentication on regulated workstreams, and review invocation audit logs monthly. |
| **Regulated** | All Recommended controls plus: prohibit federated connectors that route customer NPI outside approved data residency boundaries, and require quarterly third-party attestation per enabled vendor. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to automate inventory and audit collection.
- Use [Verification & Testing](verification-testing.md) to validate scoping and DLP coverage.
- Keep [Troubleshooting](troubleshooting.md) available for enablement, authentication, and audit issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.16](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md)
