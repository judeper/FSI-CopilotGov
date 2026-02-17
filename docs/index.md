# FSI Copilot Governance Framework

**Comprehensive governance, compliance, and security framework for Microsoft 365 Copilot in US Financial Services.**

---

## Welcome

This framework provides **54 technical controls** and **216 implementation playbooks** for governing Microsoft 365 Copilot across all M365 applications in regulated US financial services environments.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](disclaimer.md).

---

## Framework Architecture

```
+-------------------+-------------------+-------------------+-------------------+
|     PILLAR 1      |     PILLAR 2      |     PILLAR 3      |     PILLAR 4      |
|    Readiness &    |    Security &     |   Compliance &    |   Operations &    |
|    Assessment     |    Protection     |      Audit        |    Monitoring     |
|   (13 controls)   |   (15 controls)   |   (13 controls)   |   (13 controls)   |
+-------------------+-------------------+-------------------+-------------------+
| Data hygiene,     | DLP, labels,      | Audit logging,    | Feature toggles,  |
| oversharing,      | conditional       | retention,        | analytics, cost,  |
| permissions,      | access, barriers, | eDiscovery,       | incident response, |
| licensing         | Defender          | FINRA, SEC        | BC/DR, Sentinel   |
+-------------------+-------------------+-------------------+-------------------+
```

### Three Layers

| Layer | Purpose | Start Here |
|-------|---------|------------|
| [Framework](framework/index.md) | Strategic governance context | [Executive Summary](framework/executive-summary.md) |
| [Controls](controls/index.md) | Technical specifications (what & why) | [Control Index](controls/index.md) |
| [Playbooks](playbooks/index.md) | Implementation procedures (how) | [Quick Start](getting-started/quick-start.md) |

### Three Governance Levels

| Level | Description | Typical Use |
|-------|-------------|-------------|
| **Baseline** | Minimum viable governance | Initial Copilot deployment |
| **Recommended** | Best practices for production | Most organizations |
| **Regulated** | Comprehensive, examination-ready | High-risk, FINRA/SEC-regulated |

---

## Copilot Surfaces Covered

Microsoft 365 Copilot as it appears in:

- **Productivity:** Word, Excel, PowerPoint, OneNote, Loop, Whiteboard, Forms
- **Communication:** Outlook, Teams (chat, meetings, phone, queues)
- **Collaboration:** SharePoint, OneDrive, Planner, Stream
- **Intelligence:** Viva (Insights, Engage, Learning, Pulse, Goals)
- **AI-Native:** Microsoft 365 Copilot Chat, Copilot Pages
- **Extensibility:** Plugins, Graph connectors, declarative agents

---

## Quick Navigation

| I want to... | Go to... |
|--------------|----------|
| Get started quickly | [Quick Start Guide](getting-started/quick-start.md) |
| See all controls | [Control Index](controls/index.md) |
| Understand Copilot architecture | [Copilot Architecture](framework/copilot-architecture.md) |
| Find regulatory mappings | [Regulatory Mappings](reference/regulatory-mappings.md) |
| See admin portal toggles | [Copilot Admin Toggles](reference/copilot-admin-toggles.md) |
| Understand this vs. FSI-AgentGov | [Relationship to AgentGov](framework/relationship-to-agentgov.md) |

---

## Companion Repository

For governance of **Copilot Studio**, **Agent Builder**, and **custom AI agents**, see the companion framework:

**[FSI-AgentGov](https://github.com/judeper/FSI-AgentGov)** — 71 controls, 284 playbooks for Microsoft 365 AI agent governance.

---

*FSI Copilot Governance Framework v1.0 - February 2026*
