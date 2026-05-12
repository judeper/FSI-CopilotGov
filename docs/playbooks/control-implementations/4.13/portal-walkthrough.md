# Control 4.13: Copilot Extensibility and Agent Operations Governance — Portal Walkthrough

Step-by-step portal configuration for governing plugins, Graph connectors, and agent operations through Integrated apps and the Agent 365 control plane.

## Prerequisites

- **Role:** AI Administrator, Teams Admin, or another approved admin role for the surfaces being reviewed
- **License:** Microsoft 365 E5 with Copilot add-on
- **Access:** Microsoft 365 Admin Center, Teams admin center

## Steps

### Step 1: Review Agent Overview

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > Overview

1. Review hero metrics for active users, sessions, exception rate, and runtime.
2. Review governance action cards for pending requests or ownerless agents.
3. Record follow-up actions in the governance register.

### Step 2: Review Agent Registry and Ownership

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > All agents / Registry

1. Review published, shared, blocked, and ownerless agents.
2. Confirm each broadly available agent has an owner and approval record.
3. Block or remove agents that do not meet policy.

### Step 3: Configure Agent Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > Settings

1. Review allowed agent types.
2. Review sharing controls.
3. Review user access scope and any templates used in publication workflows.

### Step 4: Configure Integrated Apps Governance (Legacy App Inventory)

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Integrated apps

> **Note:** As of the current Microsoft 365 admin center experience, agent and plugin governance is centered on the **Agents** node and the Agent 365 control plane (Steps 1–3). Use **Settings > Integrated apps** for the legacy app inventory and to triage user requests for apps not yet surfaced through the Agents catalog — do not treat Integrated apps as the primary plugin governance flow.

1. Navigate to the Integrated apps settings.
2. Review the current list of deployed apps and plugins for legacy inventory completeness.
3. Configure the app governance settings:
    - **User consent settings** — Block user consent; require admin approval for all apps
    - **App catalog** — Curate the list of approved apps available to Copilot users
    - **Third-party app access** — Restrict to a pre-approved list for FSI environments
4. Reconcile the Integrated apps inventory against the Agent registry (Step 2) so that legacy plugin deployments are tracked alongside the current Agent 365 inventory.

### Step 5: Establish Plugin and Agent Approval Workflow

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > Tools > Requests (where licensed) and Settings > Integrated apps > User requests (legacy)

1. For agent tools and MCP servers (where the **Agents > Tools** surface is available — currently Frontier tenants), use the **Requests** tab to triage MCP server registration requests; **Approve** (which prompts for the Entra permission consent the server requires) or **Reject** with documented rationale.
2. For legacy plugin and integrated-app requests, enable the user request workflow in **Settings > Integrated apps > User requests**.
3. Configure the approval chain (applies to both surfaces):
    - First-level: IT team reviews technical requirements and security posture
    - Second-level: Compliance team reviews regulatory and data protection impact
    - Third-level: Business owner confirms business justification
4. Set SLA for approval decisions (5 business days recommended).
5. Create a standardized Plugin / Tool Risk Assessment template that covers requested Entra permission scopes, data flows, and vendor attestations.

### Step 6: Configure Copilot Plugin and Tool Access Controls

**Portal:** Microsoft 365 Admin Center
**Path:** Agents > Settings (primary) and Settings > Integrated apps (legacy inventory)

1. From **Agents > Settings**, scope plugin and tool availability via **Allowed agent types**, **Sharing**, and **User access** so that approved plugins and MCP-based tools reach only the intended user populations.
2. Configure plugin availability:
    - **First-party Microsoft plugins / agents** — Enable approved items; disable non-essential ones
    - **Third-party plugins / external publisher agents** — Block all or allow only from the approved list
    - **Custom plugins (line-of-business)** — Enable with governance controls
3. Set plugin and tool access by user group (not all users need all plugins or MCP servers).
4. Document which plugins, agents, and MCP-based tools are approved and for which user groups.

### Step 7: Configure Graph Connector Governance

**Portal:** Microsoft 365 Admin Center
**Path:** Settings > Search & intelligence > Data sources

1. Review existing Microsoft Graph connectors.
2. Evaluate each connector for data sensitivity:
   - What data does the connector expose to Copilot?
   - Are there access control restrictions on the connected data?
   - Does the connector data include regulated content?
3. Apply sensitivity labels to Graph connector content where applicable.
4. Document the connector inventory with data classification and access controls.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Agent Overview review | Monthly | Monthly with tracked follow-up | Weekly / monthly depending on risk |
| Agent ownership | Required for published agents | Required for all broad-scope agents | Required with escalation for ownerless agents |
| User consent for plugins | Allowed | Admin-only consent | Admin-only with compliance review |
| Third-party plugins / partner agents | Review | Pre-approved list | Pre-approved with security assessment |
| Graph connector review | Ad hoc | Annual | Semi-annual with data classification |

## Regulatory Alignment

- **FFIEC Development Booklet** — Supports compliance with third-party software governance requirements
- **OCC Third-Party Risk** — Helps meet vendor risk management for plugin providers
- **NYDFS 23 NYCRR 500** — Supports third-party service provider security assessment requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for plugin governance automation
- See [Verification & Testing](verification-testing.md) to validate extensibility controls
- Back to [Control 4.13](../../../controls/pillar-4-operations/4.13-extensibility-governance.md)
