# Control 2.17: Cross-Tenant Agent Federation - Portal Walkthrough

Step-by-step governance workflow for governing cross-tenant agent invocation patterns: Entra Agent ID-backed access, MCP / BYO MCP server attestation, Copilot Studio A2A endpoints, and externally published agents.

## Prerequisites

- [Control 2.16 Federated Connector and MCP Governance](../../../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md) is in place for single-tenant federated MCP usage.
- [Control 1.10 Vendor Risk Management](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md) covers external tenants whose agents will be invoked.
- Cross-tenant access settings (CTAP) baselines are documented for the firm's Entra tenant.
- Named owners for each pattern: Entra cross-tenant trust, MCP attestation, and Copilot Studio publishing.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft Entra admin center | External Identities > Cross-tenant access settings | Governs configured inbound/outbound cross-tenant access; verify whether the selected agent pattern is actually controlled by CTAP in the tenant |
| Microsoft Entra admin center | Identity > Workload identities | Inventories Agent ID identities and their trust relationships |
| Microsoft 365 Admin Center | Agents > Tools; Copilot connectors > Your connections | Surfaces MCP servers, BYO MCP requests, and federated connector access decisions |
| Copilot Studio | Agents > Add agent > A2A agent; Solutions > Agents > Publish | Manages A2A endpoint connections, multi-tenant publishing, and the receiving-tenant approval flow |
| Microsoft Purview portal | Audit | Cross-tenant invocation, attestation, and trust-grant events |

## Steps

### Step 1: Inventory the cross-tenant patterns

Capture the present state for each pattern: which external tenants have configured trust or partner access, which MCP/BYO MCP servers are registered or requested, which A2A endpoints are connected, and which Copilot Studio agents are published from or to the firm. Without this baseline, downstream attestation work has no anchor.

### Step 2: Apply cross-tenant access settings before granting trust

Configure Entra cross-tenant access settings to the firm's approved default posture and require explicit per-tenant inclusion where CTAP governs the pattern. Document the named external tenants approved under [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md), the Microsoft Cloud instances they operate in, and the evidence proving whether CTAP applies to the specific agent path. Do not assume CTAP blocks every A2A, MCP, or published-agent path without tenant evidence.

### Step 3: Require signed attestation for MCP federated servers

For each MCP federated server registered to the firm, require a signed attestation that names the operating tenant, model and prompt provenance, data residency, and incident notification path. Do not register an MCP server lacking this attestation.

### Step 4: Govern Copilot Studio multi-tenant publishing

For published agents authored in the firm, maintain a publishing-target list with the receiving tenants approved to install and use the agent. For published agents the firm consumes from external authors, require the receiving-tenant admin approval workflow and capture the approval record. For A2A endpoint connections, Microsoft Learn states supported authentication options are **None**, **API key**, and **OAuth 2.0**, and typical A2A metadata includes full chat history, not just the latest user utterance; capture endpoint authentication, hosting jurisdiction, full-chat-history handling, and data-residency approval before enabling an external A2A endpoint.

### Step 5: Establish supervisory observability

FINRA Rule 3110 (supervisory systems and WSPs) expects observable behavior. Configure unified audit logging for cross-tenant invocation events and route them to the supervisory review surface so cross-tenant activity is reconstructable.

### Step 6: Define termination procedures up front

When a cross-tenant relationship ends, residual grants persist by default. Document the termination playbook covering Entra trust removal, MCP de-registration, Copilot Studio uninstallation, and an evidence snapshot of the final state.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Inventory each cross-tenant pattern and configure CTAP / Copilot / tool controls to deny or withhold unapproved external access where the tenant exposes an applicable control. |
| **Recommended** | Require signed MCP / A2A attestation, maintain a per-pattern third-party register, and review cross-tenant invocation audit logs monthly. |
| **Regulated** | All Recommended controls plus: data-residency attestation per external tenant or endpoint, quarterly supervisory reconstruction drill, and tested termination playbook for each external tenant or endpoint. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to inventory and audit cross-tenant patterns.
- Use [Verification & Testing](verification-testing.md) to validate trust scope and termination integrity.
- Keep [Troubleshooting](troubleshooting.md) available for trust, attestation, and publishing issues.

*FSI Copilot Governance Framework v1.8.0 - July 2026*
- Back to [Control 2.17](../../../controls/pillar-2-security/2.17-cross-tenant-agent-federation.md)
