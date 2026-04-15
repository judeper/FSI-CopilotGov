# Control 2.14: Declarative Agents from SharePoint Governance — Portal Walkthrough

Step-by-step portal configuration for governing declarative Copilot agents created from SharePoint content.

## Prerequisites

- SharePoint Admin role
- Microsoft 365 Copilot licenses deployed
- Understanding of declarative agent capabilities and data access
- Governance framework for agent creation and deployment

## Steps

### Step 1: Understand Declarative Agent Architecture

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Agents > Overview

Review how declarative agents work: users can create custom Copilot agents scoped to specific SharePoint sites or document libraries. These agents answer questions based on the defined content scope, making governance of the underlying content critical.

> **Agent 365 Centralized Governance:** Microsoft has introduced **Agent 365** as a centralized governance platform for managing all agent types across the Microsoft 365 ecosystem. Agent 365 consolidates agent inventory, policy management, and lifecycle governance into a single administrative surface. Organizations should review Agent 365 settings in the M365 Admin Center to establish centralized visibility over all deployed agents — including declarative agents, Copilot Studio agents, and third-party agents.

> **Entra Agent ID:** Agents can now be assigned an **Entra Agent ID** for identity management, enabling organizations to treat agents as managed identities within Entra ID. This supports conditional access policies, audit attribution, and permission management for agents. Organizations should evaluate whether agent identity management through Entra Agent ID is appropriate for their governance model.

### Step 2: Configure Agent Creation Policies

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Agents > Settings > User access

Configure who can create declarative agents:
- Restrict agent creation to specific groups (e.g., IT team, approved power users)
- Disable agent creation for general users until governance processes are established
- Require approval for agent publication to the organization

### Step 3: Review Agent Data Access Scope

**Portal:** SharePoint admin center
**Path:** SharePoint Admin > Active Sites > review sites used as agent data sources

For each declarative agent, the data access scope is defined by the SharePoint site or library it references. Verify:
- Sites used as data sources have appropriate sensitivity labels and permissions
- Content is appropriate for the agent's intended audience
- No oversharing exists on the source site (cross-reference with Control 1.2)

### Step 4: Configure Agent Sharing and Distribution

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Agents > Settings > Sharing

Control how declarative agents are shared:
- Limit sharing to "People with existing access" to the underlying content
- Disable organization-wide agent publishing for unapproved agents
- Require governance review before broad distribution

### Step 5: Document Agent Governance Framework

Create the agent governance document covering:
- Who can create agents and under what conditions
- Data access review requirements for agent source content
- Testing requirements before agent publication
- Ongoing monitoring and review of active agents
- Decommissioning process for obsolete agents
- **Third-party model provider policy** — document the organization's policy on third-party model providers (e.g., non-Microsoft AI models accessed through agents). By default, third-party model providers are disabled in the M365 Admin Center. Organizations should maintain this default unless a specific business case is approved, a vendor risk assessment is completed, and data residency implications are documented. If third-party model providers are enabled, define which providers are permitted and which data classifications may be processed.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Restrict agent creation to IT team; review data sources before agent deployment; verify third-party model providers are disabled (default) |
| **Recommended** | Formal agent approval process; source site security verification; agent inventory tracking via Agent 365; Entra Agent ID for agent identity management; documented third-party model provider policy |
| **Regulated** | Agent creation requires governance committee approval; data impact assessment for each agent; quarterly agent review; comprehensive audit logging; Entra Agent ID required for all deployed agents; third-party model providers disabled or restricted to approved providers with completed vendor risk assessment |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for agent management automation
- See [Verification & Testing](verification-testing.md) to validate agent governance
- Review Control 2.13 for broader plugin governance context
- Back to [Control 2.14](../../../controls/pillar-2-security/2.14-declarative-agents-governance.md)
