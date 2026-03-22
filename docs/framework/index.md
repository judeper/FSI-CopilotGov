# Framework Overview

The FSI Copilot Governance Framework provides comprehensive governance guidance for Microsoft 365 Copilot in US financial services organizations.

---

## Purpose

This Framework layer establishes the foundational governance principles, organizational structure, and regulatory context for M365 Copilot deployment. Content here is designed for:

- **Executives and Board Members** -- Strategic oversight and risk appetite decisions
- **Compliance Officers** -- Regulatory alignment and examination readiness
- **AI Governance Committees** -- Policy decisions and governance operations
- **Auditors** -- Framework structure and control objectives

---

## Three-Layer Documentation Architecture

The FSI Copilot Governance Framework uses a three-layer documentation model to separate stable governance principles from frequently-updated implementation procedures:

```
+============================================================================+
|                                                                            |
|  LAYER 1: FRAMEWORK  (this layer)                                         |
|  Strategic governance context                                              |
|  Audience: Executives, compliance, board                                   |
|  Update frequency: 1-2x per year                                          |
|                                                                            |
+============================================================================+
        |                       |                       |
        v                       v                       v
+============================================================================+
|                                                                            |
|  LAYER 2: CONTROLS  (56 technical controls)                                |
|  What to configure and why                                                 |
|  Audience: Compliance officers, architects                                 |
|  Update frequency: Quarterly                                               |
|                                                                            |
|  +------------------+ +------------------+ +------------------+            |
|  | Pillar 1:        | | Pillar 2:        | | Pillar 3:        |            |
|  | Readiness &      | | Security &       | | Compliance &     |            |
|  | Assessment       | | Protection       | | Audit            |            |
|  | (15 controls)    | | (15 controls)    | | (13 controls)    |            |
|  +------------------+ +------------------+ +------------------+            |
|  +------------------+                                                      |
|  | Pillar 4:        |                                                      |
|  | Operations &     |                                                      |
|  | Monitoring       |                                                      |
|  | (13 controls)    |                                                      |
|  +------------------+                                                      |
|                                                                            |
+============================================================================+
        |                       |                       |
        v                       v                       v
+============================================================================+
|                                                                            |
|  LAYER 3: PLAYBOOKS  (224 implementation procedures)                       |
|  How to configure step-by-step                                             |
|  Audience: Platform teams, operations                                      |
|  Update frequency: Continuous (as Microsoft portals change)                |
|                                                                            |
|  Each control has 4 playbooks:                                             |
|  [Portal Walkthrough] [PowerShell Automation] [Verification] [Rollback]   |
|                                                                            |
+============================================================================+
```

This separation provides governance stability while allowing rapid updates to implementation guidance as Microsoft 365 evolves.

---

## Four Governance Pillars

```
+-------------------+-------------------+-------------------+-------------------+
|     PILLAR 1      |     PILLAR 2      |     PILLAR 3      |     PILLAR 4      |
|    Readiness &    |    Security &     |   Compliance &    |   Operations &    |
|    Assessment     |    Protection     |      Audit        |    Monitoring     |
|   (15 controls)   |   (15 controls)   |   (13 controls)   |   (13 controls)   |
+-------------------+-------------------+-------------------+-------------------+
| Data hygiene,     | DLP, labels,      | Audit logging,    | Feature toggles,  |
| oversharing,      | conditional       | retention,        | analytics, cost,  |
| permissions,      | access, barriers, | eDiscovery,       | incident response, |
| licensing         | Defender          | FINRA, SEC        | BC/DR, Sentinel   |
+-------------------+-------------------+-------------------+-------------------+
```

| Pillar | Focus | Controls | Primary Admin Portals |
|--------|-------|----------|-----------------------|
| **1. Readiness & Assessment** | Pre-deployment data hygiene, oversharing, permissions, licensing | 15 | Purview, SharePoint Admin, M365 Admin |
| **2. Security & Protection** | DLP, sensitivity labels, conditional access, information barriers, Defender | 15 | Purview, Entra, Defender |
| **3. Compliance & Audit** | Audit logging, retention, eDiscovery, FINRA 2210, supervision, regulatory reporting | 13 | Purview, M365 Admin |
| **4. Operations & Monitoring** | Feature management, per-app toggles, analytics, cost tracking, incident response | 13 | M365 Admin, Viva Insights, Teams Admin |

---

## Three Governance Levels

Each control provides tiered implementation guidance:

| Level | Description | Typical Use |
|-------|-------------|-------------|
| **Baseline** | Minimum viable governance for initial Copilot deployment | Organizations deploying Copilot for the first time |
| **Recommended** | Best practices for production environments | Most organizations in steady-state operations |
| **Regulated** | Comprehensive, examination-ready controls | High-risk, FINRA/SEC-regulated environments |

See [Governance Fundamentals](governance-fundamentals.md) for detailed level definitions and selection criteria.

---

## Framework Components

| Document | Purpose | Audience |
|----------|---------|----------|
| [Executive Summary](executive-summary.md) | Board-level overview of M365 Copilot risks and governance | C-suite, Board |
| [Governance Fundamentals](governance-fundamentals.md) | Core framework concepts, governance levels, shared responsibility | All stakeholders |
| [Copilot Architecture](copilot-architecture.md) | Technical deep-dive into M365 Copilot architecture and data flows | Architects, Security |
| [Copilot Surfaces](copilot-surfaces.md) | Where Copilot appears across M365 and governance implications per app | Compliance, Operations |
| [Regulatory Framework](regulatory-framework.md) | US regulatory requirements and control mappings | Compliance, Legal |
| [Operating Model](operating-model.md) | RACI, roles, committee structure, escalation procedures | All stakeholders |
| [Adoption Roadmap](adoption-roadmap.md) | 30/60/90-day phased implementation guidance | Implementation teams |
| [Relationship to AgentGov](relationship-to-agentgov.md) | Scope boundary with FSI-AgentGov companion repository | All stakeholders |

---

## Framework Principles

### 1. Risk-Based Governance

Controls scale with regulatory exposure. Baseline governance supports initial deployment while Regulated-level controls support examination readiness for FINRA/SEC-regulated firms.

### 2. Discovery Amplification Awareness

M365 Copilot does not bypass permissions, but it dramatically amplifies the speed and scale at which users discover content they already have access to. Governance must address the gap between *technical access* and *intended access*.

### 3. Regulatory Alignment

The framework maps controls to US financial regulations including FINRA 4511/3110/2210, SEC 17a-3/4, SOX 302/404, GLBA 501(b), OCC 2011-12, and Fed SR 11-7. Organizations should validate mappings against their specific regulatory obligations.

### 4. Microsoft Platform Foundation

All controls leverage native Microsoft 365 capabilities (Purview, Entra, Defender, SharePoint Admin, M365 Admin Center). This framework does not require third-party governance tools, though organizations may integrate additional solutions.

### 5. Separation of Concerns

The three-layer architecture separates:

- **Framework** (this layer) -- Stable governance principles updated 1-2x per year
- **Controls** -- Control objectives and requirements updated quarterly
- **Playbooks** -- Implementation procedures updated continuously as Microsoft portals change

---

## Quick Navigation

**For Executives:**

1. Start with [Executive Summary](executive-summary.md)
2. Review [Governance Fundamentals](governance-fundamentals.md) for governance levels
3. Understand [Operating Model](operating-model.md) for accountability

**For Compliance Officers:**

1. Review [Regulatory Framework](regulatory-framework.md)
2. Understand [Copilot Surfaces](copilot-surfaces.md) for app-specific considerations
3. Reference the [Control Catalog](../controls/index.md) for specific requirements

**For Implementation Teams:**

1. Follow [Adoption Roadmap](adoption-roadmap.md)
2. Understand [Copilot Architecture](copilot-architecture.md) for technical context
3. Reference [Playbooks](../playbooks/index.md) for step-by-step procedures

---

## Version Information

- **Framework Version:** 1.1 (February 2026)
- **Last Updated:** February 2026
- **Update Frequency:** 1-2 times per year (major regulatory or platform changes)

---

## Related Sections

- [Control Catalog](../controls/index.md) -- Detailed control requirements
- [Playbooks](../playbooks/index.md) -- Implementation procedures
- [Reference](../reference/index.md) -- Supporting materials
- [FSI-AgentGov](relationship-to-agentgov.md) -- Companion framework for Copilot Studio and AI agents

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
