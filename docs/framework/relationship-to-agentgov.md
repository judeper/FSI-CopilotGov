# Relationship to FSI-AgentGov

Scope boundary between FSI-CopilotGov and FSI-AgentGov, and guidance on when to use each framework.

---

## Overview

Microsoft's AI ecosystem in Microsoft 365 spans two distinct categories:

1. **Microsoft 365 Copilot** -- the AI assistant embedded in M365 applications (Word, Excel, Outlook, Teams, Microsoft 365 Copilot Chat, etc.)
2. **Copilot Studio / Agent Builder** -- the platform for building custom AI agents, declarative agents, and automated workflows

Each category presents different governance challenges. The FSI governance framework is split across two companion repositories to provide focused, actionable guidance for each:

- **FSI-CopilotGov** (this repository) -- governs M365 Copilot
- **[FSI-AgentGov](https://github.com/judeper/FSI-AgentGov)** -- governs Copilot Studio, Agent Builder, and custom AI agents

Both repositories are **standalone** -- no cross-repo dependencies. Where governance topics overlap, each repo provides self-contained guidance tailored to its scope.

---

## Comparison Table

| Aspect | FSI-CopilotGov (this repo) | FSI-AgentGov |
|--------|---------------------------|--------------|
| **Subject** | Microsoft 365 Copilot (in-app AI assistant) | Copilot Studio, Agent Builder, SharePoint Agents |
| **What it governs** | AI capabilities embedded in M365 apps | Custom AI agents and automated workflows |
| **Governance model** | Three governance levels: Baseline, Recommended, Regulated | Three governance zones: Zone 1 (Personal), Zone 2 (Team), Zone 3 (Enterprise) |
| **Pillars** | 1. Readiness & Assessment, 2. Security & Protection, 3. Compliance & Audit, 4. Operations & Monitoring | 1. Security, 2. Management, 3. Reporting, 4. SharePoint |
| **Controls** | 56 | 71 |
| **Playbooks** | 224 (4 per control) | 284 (4 per control) |
| **Key concepts** | Semantic Index, Graph grounding, discovery amplification, Restricted SharePoint Search, DSPM for AI | Managed Environments, Connectors, DLP Connector Policies, Agent Lifecycle, Multi-Agent Orchestration |
| **Primary risk** | Oversharing amplification -- Copilot surfaces content users already have access to, but at unprecedented speed and scale | Unauthorized agent creation -- custom agents that access regulated data without governance |
| **Deployment model** | Org-wide (Copilot is tenant-level, per-user licensed) | Per-agent (each agent is individually built, tested, deployed) |
| **Admin portals** | M365 Admin Center, Purview, Entra, SharePoint Admin, Teams Admin, Defender | Power Platform Admin Center (PPAC), M365 Admin Center, Purview |
| **Regulatory focus** | FINRA 2210 (Copilot-drafted communications), recordkeeping, supervision | Model risk management (OCC 2011-12), agent lifecycle, testing |
| **Framework version** | v1.2.1 | v1.2.42 |

---

## Scope Boundary

### What FSI-CopilotGov Covers

| In Scope | Description |
|----------|-------------|
| M365 Copilot in Word, Excel, PowerPoint, OneNote | Document-level AI assistance |
| M365 Copilot in Outlook | Email drafting, summarization, coaching |
| M365 Copilot in Teams | Chat summaries, meeting recaps, transcription |
| Microsoft 365 Copilot Chat | Cross-application Copilot |
| Copilot Pages | AI-generated collaborative content |
| Copilot in Viva suite | Viva Insights, Engage, Learning, Pulse, Goals |
| Copilot in Loop, Whiteboard, Forms, Planner, Stream | App-specific AI features |
| Web search / web grounding | Bing integration in Copilot |
| Plugins and Graph connectors | Extending Copilot's data reach |
| Declarative agents from SharePoint | Custom Copilot experiences built from SharePoint (not Copilot Studio) |

### What FSI-AgentGov Covers

| In Scope | Description |
|----------|-------------|
| Copilot Studio custom agents | Agents built in the Copilot Studio designer |
| Agent Builder agents | Agents built via M365 Agent Builder |
| Power Platform environments | Managed Environments, environment groups |
| DLP connector policies | Data boundary enforcement for agents |
| Agent lifecycle management | Creation, testing, deployment, monitoring, retirement |
| Model risk management | OCC 2011-12 / SR 11-7 alignment for AI agents |
| Multi-agent orchestration | Governance of agent-to-agent interactions |
| SharePoint as agent knowledge source | Pillar 4 (SharePoint-specific agent controls) |
| Microsoft-built Copilot chat experiences (Researcher, Analyst, Facilitator) | Usage oversight and access decisions for first-party experiences surfaced in Copilot Chat |
| Agent 365 / Agent Registry / agent settings | Centralized control plane for agent governance at scale |

### Scope Boundary Diagram

```
+------------------------------------------------------------------+
|               MICROSOFT 365 AI GOVERNANCE SCOPE                    |
|                                                                    |
|  +-----------------------------+  +-----------------------------+  |
|  |     FSI-CopilotGov          |  |     FSI-AgentGov            |  |
|  |     (this repository)       |  |                             |  |
|  |                             |  |                             |  |
|  |  M365 Copilot in:          |  |  Custom agents:             |  |
|  |  - Word, Excel, PPT        |  |  - Copilot Studio           |  |
|  |  - Outlook, Teams          |  |  - Agent Builder            |  |
|  |  - Copilot Chat, Copilot Pages  |  |  - Power Platform           |  |
|  |  - Viva, Loop, etc.        |  |  - Agent 365 / Entra Agent  |  |
|  |                             |  |                             |  |
|  |  Extensibility:            |  |  Microsoft agents:          |  |
|  |  - Plugins                 |  |  - Agent 365 / Registry     |  |
|  |  - Graph connectors        |  |  - Facilitator              |  |
|  |  - Declarative agents      |  |                             |  |
|  |    from SharePoint         |  |  Agent lifecycle:           |  |
|  |                             |  |  - Managed Environments     |  |
|  |  Governance model:         |  |  - DLP Connector Policies   |  |
|  |  Baseline / Recommended    |  |  - ALM Pipelines            |  |
|  |  / Regulated               |  |                             |  |
|  |                             |  |  Governance model:          |  |
|  |  56 controls, 224 books    |  |  Zone 1 / 2 / 3            |  |
|  |                             |  |  71 controls, 284 books    |  |
|  +-----------------------------+  +-----------------------------+  |
|                                                                    |
|  SHARED TOPICS (each repo provides self-contained guidance):       |
|  - Sensitivity labels  - DLP policies  - Audit logging             |
|  - Retention policies  - SharePoint governance  - eDiscovery       |
+------------------------------------------------------------------+
```

---

## When to Use Which Repository

### Use FSI-CopilotGov When

| Scenario | Why |
|----------|-----|
| Deploying M365 Copilot to your organization | Primary governance framework for Copilot rollout |
| Assessing oversharing before Copilot enablement | Copilot-specific oversharing assessment and remediation |
| Configuring Copilot feature toggles (web search, per-app controls) | Copilot operational controls |
| Implementing supervisory review for Copilot-drafted communications | FINRA 2210 / 3110 for Copilot |
| Setting up communication compliance for Copilot-assisted emails | Copilot-specific compliance monitoring |
| Governing Copilot Pages, Microsoft 365 Copilot Chat, or Teams Copilot features | AI-native surface governance |
| Managing plugins and Graph connectors for Copilot | Copilot extensibility governance |
| Building declarative agents from SharePoint (not Copilot Studio) | SharePoint-based custom Copilot experiences |

### Use FSI-AgentGov When

| Scenario | Why |
|----------|-----|
| Building custom agents in Copilot Studio | Agent-specific governance (lifecycle, testing, deployment) |
| Deploying Agent Builder agents | M365 agent governance |
| Configuring Managed Environments for agent hosting | Power Platform environment governance |
| Implementing DLP connector policies for agent data boundaries | Agent-specific DLP controls |
| Conducting model risk management for AI agents | OCC 2011-12 / SR 11-7 agent alignment |
| Governing multi-agent orchestration | Agent-to-agent interaction governance |
| Governing Researcher and Analyst usage within Copilot Chat | Core Copilot chat experience governance |
| Implementing Agent 365, Registry, templates, or large-scale agent lifecycle controls | Agent governance control plane and lifecycle |

### Use Both Repositories When

| Scenario | CopilotGov Focus | AgentGov Focus |
|----------|-----------------|----------------|
| Organization deploys both M365 Copilot and custom agents | Copilot in-app governance | Agent lifecycle governance |
| SharePoint governance for AI | Copilot access to SharePoint content | Agents grounded in SharePoint data |
| Sensitivity labels | Labels applied to content Copilot accesses | Labels applied to content agents access |
| Audit logging | Copilot interaction audit events | Agent interaction audit events |
| DLP policies | DLP for Copilot data flow | DLP connector policies for agent data flow |
| Board-level AI governance reporting | Copilot risk metrics | Agent risk metrics |

---

## Overlapping Governance Topics

Several governance topics appear in both repositories. Each provides self-contained guidance tailored to its scope:

| Topic | FSI-CopilotGov Treatment | FSI-AgentGov Treatment |
|-------|--------------------------|------------------------|
| **Sensitivity labels** | Labels on documents, emails, sites that Copilot accesses; auto-labeling policies; label-based DLP for Copilot | Labels on SharePoint sites used for agent grounding; label-based data protection |
| **DLP policies** | M365 DLP policies (Exchange, SharePoint, OneDrive, Teams) that apply to Copilot-surfaced content | DLP connector policies in Power Platform that control agent data boundaries |
| **Audit logging** | CopilotInteraction events in Unified Audit Log; Copilot-specific retention | Power Platform audit events; agent interaction logging; agent-specific retention |
| **SharePoint governance** | Oversharing assessment, permissions remediation, Restricted SharePoint Search for Copilot grounding | SharePoint as agent knowledge source; Pillar 4 controls for agent-specific SharePoint governance |
| **eDiscovery** | eDiscovery for Copilot-generated content and interaction logs | eDiscovery for agent interactions and outputs |
| **Retention policies** | Retention for Copilot interactions, Copilot Pages, Copilot-generated content | Retention for agent conversation logs, agent outputs |
| **Conditional access** | CA policies for Copilot user access | CA policies for agent creator and admin access |
| **Supervision (FINRA 3110)** | Supervision of Copilot-assisted activities by associated persons | Supervision of agent-generated outputs and decisions |
| **Incident response** | Copilot-related incidents (data exposure via Copilot, hallucination in customer communication) | Agent-related incidents (unauthorized agent, agent malfunction, data leakage) |

**Key principle:** If a control topic appears in both repositories, you should implement the guidance from the repository relevant to your deployment. If you deploy both Copilot and custom agents, implement the guidance from both.

---

## Migration Path from FSI-AgentGov

If your organization already uses FSI-AgentGov and is now deploying M365 Copilot:

### What Carries Over

| From FSI-AgentGov | Applies to CopilotGov |
|--------------------|-----------------------|
| Sensitivity label taxonomy | Same labels protect content from both Copilot and agents |
| DLP policies (M365 scope) | Same M365 DLP policies apply to Copilot |
| Audit logging configuration | Unified Audit Log serves both Copilot and agent events |
| SharePoint site governance | Same site permissions affect both Copilot and agent grounding |
| Governance committee | Expand scope to include M365 Copilot governance |
| Compliance reporting framework | Extend to include Copilot metrics |

### What Is New for CopilotGov

| New Requirement | Why |
|----------------|-----|
| Oversharing assessment and remediation | Copilot amplifies oversharing; agents have scoped data access |
| Copilot feature toggle management | Per-app controls, web search settings unique to Copilot |
| Communication compliance for Copilot | Copilot-drafted emails require FINRA 2210 review |
| Restricted SharePoint Search | Controls Copilot Chat grounding scope; not applicable to agents |
| Copilot Pages governance | New content surface unique to Copilot |
| Teams meeting/transcription governance | Copilot indexes meeting transcripts; agents do not |

### Recommended Approach

1. **Extend your governance committee** scope to include M365 Copilot (do not create a separate committee)
2. **Validate existing controls** -- confirm that sensitivity labels, DLP policies, and audit logging from AgentGov also cover Copilot scenarios
3. **Add Copilot-specific controls** -- implement the controls unique to Copilot (oversharing, communication compliance, feature toggles)
4. **Follow the CopilotGov adoption roadmap** -- use Phase 0/1/2 even if AgentGov is mature; oversharing assessment is mandatory
5. **Unify reporting** -- combine Copilot and agent governance metrics into a single governance dashboard for the committee

---

## Link to FSI-AgentGov

**Repository:** [https://github.com/judeper/FSI-AgentGov](https://github.com/judeper/FSI-AgentGov)

**Documentation site:** [https://judeper.github.io/FSI-AgentGov/](https://judeper.github.io/FSI-AgentGov/)

**Key documents to review:**

- [Executive Summary](https://judeper.github.io/FSI-AgentGov/framework/executive-summary/) -- Board-level overview of agent governance
- [Zones and Tiers](https://judeper.github.io/FSI-AgentGov/framework/zones-and-tiers/) -- Three-zone agent classification model
- [Governance Fundamentals](https://judeper.github.io/FSI-AgentGov/framework/governance-fundamentals/) -- Core agent governance concepts
- [Control Catalog](https://judeper.github.io/FSI-AgentGov/controls/) -- 71 agent governance controls

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
