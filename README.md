# FSI Copilot Governance Framework

**Comprehensive governance, compliance, and security framework for Microsoft 365 Copilot in US Financial Services.**

[![Publish Docs](https://github.com/judeper/FSI-CopilotGov/actions/workflows/publish_docs.yml/badge.svg)](https://github.com/judeper/FSI-CopilotGov/actions/workflows/publish_docs.yml)
[![Link Validation](https://github.com/judeper/FSI-CopilotGov/actions/workflows/link-check.yml/badge.svg)](https://github.com/judeper/FSI-CopilotGov/actions/workflows/link-check.yml)

---

## What This Is

A technical documentation framework providing **54 controls** and **216 playbooks** for governing Microsoft 365 Copilot across all M365 applications in regulated US financial services environments.

This covers M365 Copilot as it surfaces across **Word, Excel, PowerPoint, Outlook, Teams, OneNote, Loop, Whiteboard, Forms, Planner, Stream, Viva, Microsoft 365 Copilot Chat, Copilot Pages**, and **SharePoint declarative agents** — plus extensibility via **plugins, Graph connectors, and declarative agents**.

> **Companion Repository:** For governance of Copilot Studio, Agent Builder, and custom agents, see [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov).

---

## Framework Architecture

### Three-Layer Model

| Layer | Purpose | Content |
|-------|---------|---------|
| **Framework** (Strategic) | Board/executive governance context | Executive summary, regulatory landscape, architecture, operating model |
| **Controls** (Technical) | What to configure and why | 54 controls across 4 lifecycle pillars with FSI regulatory mappings |
| **Playbooks** (Implementation) | How to configure step-by-step | Portal walkthroughs, PowerShell automation, verification, troubleshooting |

### Four Lifecycle Pillars

| Pillar | Focus | Controls | Primary Admin Portals |
|--------|-------|----------|-----------------------|
| **1. Readiness & Assessment** | Pre-deployment data hygiene, oversharing, permissions, licensing | 13 | Purview, SharePoint Admin, M365 Admin |
| **2. Security & Protection** | DLP, sensitivity labels, conditional access, information barriers, Defender | 15 | Purview, Entra, Defender |
| **3. Compliance & Audit** | Audit logging, retention, eDiscovery, FINRA 2210, supervision, regulatory reporting | 13 | Purview, M365 Admin |
| **4. Operations & Monitoring** | Feature management, per-app toggles, analytics, cost tracking, incident response | 13 | M365 Admin, Viva Insights, Teams Admin |

### Three Governance Levels

Each control provides tiered implementation guidance:

- **Baseline** — Minimum viable governance for initial Copilot deployment
- **Recommended** — Best practices for most production environments
- **Regulated** — Comprehensive controls for high-risk, examination-ready deployments

---

## Regulatory Coverage

| Regulation | Issuer | Key Controls |
|------------|--------|--------------|
| **FINRA Rule 4511** | FINRA | Audit logging (3.1), Retention (3.2), Record keeping (3.11) |
| **FINRA Rule 3110** | FINRA | Supervision (3.6), Communication compliance (3.4) |
| **FINRA Rule 2210** | FINRA | Copilot-drafted communications compliance (3.5) |
| **SEC 17a-3/4** | SEC | Record keeping (3.11), eDiscovery (3.3) |
| **SEC Reg S-P** | SEC | Privacy of consumer information (3.10) |
| **SEC Reg BI** | SEC | Supervision and best interest (3.6) |
| **SOX 302/404** | Congress | Internal controls, audit trail |
| **GLBA 501(b)** | FTC | Data protection, safeguards |
| **OCC 2011-12 / SR 11-7** | OCC/Fed | Model risk management (3.8) |
| **CFPB UDAAP** | CFPB | Unfair/deceptive practices (3.7) |
| **FFIEC IT Handbook** | FFIEC | IT examination alignment (3.13) |
| **Interagency AI Guidance (2023)** | OCC/Fed/FDIC | Vendor risk management (1.10) |

---

## Quick Start

### Prerequisites

- Microsoft 365 E5 or E3 + Copilot licenses
- Administrative access to M365 Admin Center, Microsoft Purview, Microsoft Entra
- Familiarity with Microsoft 365 administration

### Browse the Documentation

**Online:** [https://judeper.github.io/FSI-CopilotGov/](https://judeper.github.io/FSI-CopilotGov/)

**Local:**

```bash
pip install mkdocs-material
mkdocs serve
```

### Implementation Path

1. **Start** with [Quick Start Guide](docs/getting-started/quick-start.md) and [Implementation Checklist](docs/getting-started/checklist.md)
2. **Understand** the [Executive Summary](docs/framework/executive-summary.md) and [Copilot Architecture](docs/framework/copilot-architecture.md)
3. **Implement** controls by pillar, starting with Pillar 1 (Readiness)
4. **Follow** the [Adoption Roadmap](docs/framework/adoption-roadmap.md) for phased rollout

---

## Repository Structure

```
FSI-CopilotGov/
├── docs/
│   ├── framework/          # Layer 1: Strategic governance documents
│   ├── controls/           # Layer 2: Technical control specifications
│   │   ├── pillar-1-readiness/    # 13 controls
│   │   ├── pillar-2-security/     # 15 controls
│   │   ├── pillar-3-compliance/   # 13 controls
│   │   └── pillar-4-operations/   # 13 controls
│   ├── playbooks/          # Layer 3: Implementation procedures
│   │   ├── control-implementations/  # 4 playbooks per control
│   │   ├── getting-started/          # Phased deployment guides
│   │   ├── governance-operations/    # Operating calendar, RACI
│   │   ├── compliance-and-audit/     # Evidence packs, audit readiness
│   │   ├── incident-and-risk/        # AI incident response
│   │   └── regulatory-modules/       # State-specific guides
│   └── reference/          # Quick-reference materials
├── scripts/                # CI validation scripts
├── templates/              # Downloadable governance templates
└── .github/                # CI/CD workflows
```

---

## Relationship to FSI-AgentGov

| Aspect | FSI-AgentGov | FSI-CopilotGov (this repo) |
|--------|-------------|----------------------------|
| **Subject** | Copilot Studio, Agent Builder, SharePoint Agents | Microsoft 365 Copilot (in-app AI) |
| **Pillars** | Security, Management, Reporting, SharePoint | Readiness, Security, Compliance, Operations |
| **Governance Model** | Zones 1-2-3 (Personal/Team/Enterprise agents) | Org-wide with Baseline/Recommended/Regulated levels |
| **Key Concepts** | Managed Environments, Connectors, DLP Connector Policies | Semantic Index, Graph grounding, Restricted SharePoint Search, DSPM for AI |
| **Controls** | 71 | 54 |
| **Playbooks** | 284 | 216 |

Both repositories are **standalone** — no cross-repo dependencies. Where governance topics overlap (e.g., sensitivity labels, audit logging), each repo provides self-contained guidance tailored to its scope.

---

## Contributing

Contributions are welcome. Please see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for community guidelines.

### Contribution Areas

- Control content improvements and corrections
- New regulatory mappings
- Portal path verification and updates
- PowerShell script improvements
- Additional FSI configuration examples

---

## Disclaimer

This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](docs/disclaimer.md).

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

*FSI Copilot Governance Framework v1.0 - February 2026*
