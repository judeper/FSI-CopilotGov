# Control 2.17: Cross-Tenant Agent Federation - Portal Walkthrough

Step-by-step governance workflow for governing the three cross-tenant agent invocation patterns: Entra Agent ID trust, MCP federated server attestation, and Copilot Studio multi-tenant publishing.

## Prerequisites

- [Control 2.16 Federated Connector and MCP Governance](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md) is in place for single-tenant federated MCP usage.
- [Control 1.10 Vendor Risk Management](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) covers external tenants whose agents will be invoked.
- Cross-tenant access settings (CTAP) baselines are documented for the firm's Entra tenant.
- Named owners for each pattern: Entra cross-tenant trust, MCP attestation, and Copilot Studio publishing.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft Entra admin center | External Identities > Cross-tenant access settings | Governs Entra Agent ID trust and inbound/outbound configuration |
| Microsoft Entra admin center | Identity > Workload identities | Inventories Agent ID identities and their trust relationships |
| Microsoft 365 Admin Center | Copilot > Connectors / Integrations | Surfaces federated MCP server registrations |
| Copilot Studio | Solutions > Agents > Publish | Manages multi-tenant publishing and the receiving-tenant approval flow |
| Microsoft Purview portal | Audit | Cross-tenant invocation, attestation, and trust-grant events |

## Steps

### Step 1: Inventory the three cross-tenant patterns

Capture the present state for each of the three patterns: which external tenants have inbound Agent ID trust, which MCP federated servers are registered, and which Copilot Studio agents are published from or to the firm. Without this baseline, downstream attestation work has no anchor.

### Step 2: Apply cross-tenant access settings before granting trust

Configure Entra cross-tenant access settings to default-deny inbound Agent ID and require explicit per-tenant inclusion. Document the named external tenants approved under [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) and the Microsoft Cloud instances they operate in.

### Step 3: Require signed attestation for MCP federated servers

For each MCP federated server registered to the firm, require a signed attestation that names the operating tenant, model and prompt provenance, data residency, and incident notification path. Do not register an MCP server lacking this attestation.

### Step 4: Govern Copilot Studio multi-tenant publishing

For published agents authored in the firm, maintain a publishing-target list with the receiving tenants approved to install and use the agent. For published agents the firm consumes from external authors, require the receiving-tenant admin approval workflow and capture the approval record.

### Step 5: Establish supervisory observability

FINRA Rule 3110 (supervisory systems and WSPs) expects observable behavior. Configure unified audit logging for cross-tenant invocation events and route them to the supervisory review surface so cross-tenant activity is reconstructable.

### Step 6: Define termination procedures up front

When a cross-tenant relationship ends, residual grants persist by default. Document the termination playbook covering Entra trust removal, MCP de-registration, Copilot Studio uninstallation, and an evidence snapshot of the final state.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Inventory all three patterns and default-deny inbound Agent ID trust. |
| **Recommended** | Require signed MCP attestation, maintain a per-pattern third-party register, and review cross-tenant invocation audit logs monthly. |
| **Regulated** | All Recommended controls plus: data-residency attestation per external tenant, quarterly supervisory reconstruction drill, and tested termination playbook for each external tenant. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to inventory and audit cross-tenant patterns.
- Use [Verification & Testing](verification-testing.md) to validate trust scope and termination integrity.
- Keep [Troubleshooting](troubleshooting.md) available for trust, attestation, and publishing issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 2.17](../../../controls/pillar-2-security/2.17-cross-tenant-agent-federation.md)
