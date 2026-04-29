# FSI Copilot Governance Framework

**Comprehensive governance, compliance, and security framework for Microsoft 365 Copilot in US Financial Services.**

[![Publish Docs](https://github.com/judeper/FSI-CopilotGov/actions/workflows/publish_docs.yml/badge.svg)](https://github.com/judeper/FSI-CopilotGov/actions/workflows/publish_docs.yml)
[![Link Validation](https://github.com/judeper/FSI-CopilotGov/actions/workflows/link-check.yml/badge.svg)](https://github.com/judeper/FSI-CopilotGov/actions/workflows/link-check.yml)
[![SPA Tests](https://github.com/judeper/FSI-CopilotGov/actions/workflows/spa-tests.yml/badge.svg)](https://github.com/judeper/FSI-CopilotGov/actions/workflows/spa-tests.yml)
[![Engine Tests](https://github.com/judeper/FSI-CopilotGov/actions/workflows/engine-tests.yml/badge.svg)](https://github.com/judeper/FSI-CopilotGov/actions/workflows/engine-tests.yml)
[![Solutions Drift](https://github.com/judeper/FSI-CopilotGov/actions/workflows/solutions-drift.yml/badge.svg)](https://github.com/judeper/FSI-CopilotGov/actions/workflows/solutions-drift.yml)

> **New to this framework? [→ Start Here](docs/start-here.md)** — understand what this is and where to begin.

---

## What This Is

A technical documentation framework providing **62 controls** and **263 playbooks** for governing Microsoft 365 Copilot across all M365 applications in regulated US financial services environments. (Counts in published documentation are rendered from the canonical `assessment/manifest/content-graph.json`; this README is plain GitHub Markdown and quotes the same numbers verbatim.)

This covers M365 Copilot as it surfaces across **Word, Excel, PowerPoint, Outlook, Teams, OneNote, Loop, Whiteboard, Forms, Planner, Stream, Viva, Microsoft 365 Copilot Chat (Basic & Premium tiers), Copilot Pages**, and **SharePoint agents** — plus extensibility via **plugins, Graph connectors, declarative agents, and Agents 365**.

> **Companion Repository:** For governance of Copilot Studio, Agent Builder, and custom agents, see [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov).

---

## Who Is This For?

**You should use this framework if you are:**

- An M365 admin or architect deploying Microsoft 365 Copilot at a bank, insurer, or broker-dealer
- A compliance or security engineer preparing for FINRA, SEC, or OCC examination
- A Microsoft CSA helping an FSI customer establish a defensible Copilot governance posture

**This is NOT the right repo if you are:**

- Deploying custom agents built in Copilot Studio → see [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov)
- Looking for end-user Copilot usage guides or prompt tips
- Working outside regulated financial services

---

## Framework Architecture

### Three-Layer Model

| Layer | Purpose | Content |
|-------|---------|---------|
| **Framework** (Strategic) | Board/executive governance context | Executive summary, regulatory landscape, architecture, operating model |
| **Controls** (Technical) | What to configure and why | 62 controls across 4 lifecycle pillars with FSI regulatory mappings |
| **Playbooks** (Implementation) | How to configure step-by-step | Portal walkthroughs, PowerShell automation, verification, troubleshooting |

### Four Lifecycle Pillars

| Pillar | Focus | Controls | Primary Admin Portals |
|--------|-------|----------|-----------------------|
| **1. Readiness & Assessment** | Pre-deployment data hygiene, oversharing, permissions, licensing | 16 | Purview, SharePoint Admin, M365 Admin |
| **2. Security & Protection** | DLP, sensitivity labels, conditional access, information barriers, Defender | 16 | Purview, Entra, Defender |
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
| **Sarbanes-Oxley §§302/404** | Congress | Internal controls, audit trail |
| **GLBA §501(b)** | FTC | Data protection, safeguards |
| **OCC 2011-12 / SR 11-7** | OCC/Fed | Model risk management (3.8) |
| **CFPB UDAAP** | CFPB | Unfair/deceptive practices (3.7) |
| **FFIEC IT Handbook** | FFIEC | IT examination alignment (3.13) |
| **Interagency AI Guidance (2023)** | OCC/Fed/FDIC | Vendor risk management (1.10) |

---

## What's New in v1.4

Released April 2026. Full notes: [Release Notes v1.4](docs/reference/release-notes-v1.4.md).

- **Python assessment engine** (`assessment/engine/`) scores collector evidence against the 62-control manifest.
- **Evidence collectors** (`assessment/collectors/`) for Microsoft Graph, Purview, SharePoint, and Sentinel.
- **Schema-validated control manifest** (`assessment/manifest/controls.json`) drives both the engine and the SPA.
- **Governance Scorecard SPA** upgrades: role filter, quick-start mode (5 foundation controls), sector calibration (8 FSI types), "how to verify" drawer, facilitator mode, zone auto-exclusion, collector evidence import, versioned portal export envelope, inline solutions catalog.
- **Role checklist templates** (`assessment/templates/*.xlsx`) generated from the manifest.
- **Solutions integration** — pinned reference to [FSI-CopilotGov-Solutions](https://github.com/judeper/FSI-CopilotGov-Solutions) via `assessment/data/solutions-lock.json`; drift-guarded in CI.
- **Test suites** — 25+ pytest cases (engine, collectors, drift) and 77+ vitest cases (SPA behaviour).
- **Monitoring workflows** — scheduled daily CI (10:00 UTC) watches Microsoft Learn URLs and regulatory sources, opening a PR when content drift is detected.
- **Pre-session homework pages** — per-role preparation guides under `docs/getting-started/`.

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

### Orientation Path (New to the Framework?)

If you're not yet sure where to begin, this path helps you understand what the framework covers:

1. **Read the Executive Summary** — understand scope and audience → [Executive Summary](docs/framework/executive-summary.md)
2. **Scan the Four Pillars** — see the governance lifecycle at a glance → [Control Catalog](docs/controls/index.md)
3. **Review the Readiness Assessment** — see what a pre-deployment assessment involves → [Control 1.1](docs/controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md)
4. **Check your regulatory obligations** — identify which regulations apply → [Regulatory Framework](docs/framework/regulatory-framework.md)
5. **Open the Implementation Checklist** — your actionable to-do list → [Implementation Checklist](docs/getting-started/checklist.md)

---

## Repository Structure

```
FSI-CopilotGov/
├── docs/
│   ├── framework/          # Layer 1: Strategic governance documents
│   ├── controls/           # Layer 2: Technical control specifications
│   │   ├── pillar-1-readiness/    # 16 controls
│   │   ├── pillar-2-security/     # 16 controls
│   │   ├── pillar-3-compliance/   # 15 controls
│   │   └── pillar-4-operations/   # 14 controls
│   ├── playbooks/          # Layer 3: Implementation procedures
│   │   ├── control-implementations/  # 4 playbooks per control
│   │   ├── getting-started/          # Phased deployment guides
│   │   ├── governance-operations/    # Operating calendar, RACI
│   │   ├── compliance-and-audit/     # Evidence packs, audit readiness
│   │   ├── incident-and-risk/        # AI incident response
│   │   └── regulatory-modules/       # State-specific guides
│   ├── getting-started/    # Quick start, checklist, homework pages per role
│   ├── assessment/         # Governance Scorecard SPA entry point
│   ├── javascripts/        # SPA (assessment-app.js, loader, Chart.js)
│   ├── stylesheets/        # Site + assessment styles
│   └── reference/          # Regulatory mappings, release notes, glossary
├── assessment/
│   ├── engine/             # Python scoring + reporting (score.py, report.py)
│   ├── collectors/         # PowerShell evidence collectors (Graph, Purview, SharePoint, Sentinel)
│   ├── manifest/           # controls.json + generate_manifest.py + authored_content.py
│   ├── templates/          # XLSX role checklists + governance-maturity dashboard
│   ├── data/               # solutions-lock.json (pinned to sister repo)
│   └── tests/              # pytest engine + lock schema suites
├── tests/spa/              # vitest SPA behaviour suite
├── scripts/                # Manifest pipeline, solutions integration, monitoring, templates
├── package.json            # vitest + jsdom (dev-only)
├── vitest.config.mjs       # SPA test runner config
├── mkdocs.yml              # Material theme + nav + plugin hooks
└── .github/workflows/      # publish_docs, link-check, spa-tests, engine-tests,
                            # manifest-fence, solutions-drift, learn-url-monitor,
                            # regulatory-monitoring
```

---

## Relationship to FSI-AgentGov

| Aspect | FSI-AgentGov | FSI-CopilotGov (this repo) |
|--------|-------------|----------------------------|
| **Subject** | Copilot Studio, Agent Builder, SharePoint Agents | Microsoft 365 Copilot (in-app AI) |
| **Pillars** | Security, Management, Reporting, SharePoint | Readiness, Security, Compliance, Operations |
| **Governance Model** | Zones 1-2-3 (Personal/Team/Enterprise agents) | Org-wide with Baseline/Recommended/Regulated levels |
| **Key Concepts** | Managed Environments, Connectors, DLP Connector Policies | Semantic Index, Graph grounding, Restricted SharePoint Search, DSPM for AI |
| **Controls** | 71 | 58 |
| **Playbooks** | 284 | 243 |

Both repositories are **standalone** — no cross-repo dependencies. Where governance topics overlap (e.g., sensitivity labels, audit logging), each repo provides self-contained guidance tailored to its scope.

> **Governance Boundary Note:** Agent governance surfaces (Agent 365, agent pinning, agent registry, multi-agent orchestration) now appear in the M365 Admin Center alongside Copilot controls as GA features. FSI-CopilotGov covers agent governance as it intersects with M365 Copilot admin controls, security, and compliance — including Agent 365 operational governance, Entra Agent ID, and agent-to-agent orchestration security. FSI-AgentGov covers custom agent development, deployment, and lifecycle management in Copilot Studio and Agent Builder.

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

*FSI Copilot Governance Framework v1.4.0 - April 2026*
