# Start Here

**This framework provides step-by-step controls for configuring Microsoft 365 Copilot in regulated financial services — helping your organization work toward meeting FINRA, SEC, and OCC requirements with clear, documented guidance.**

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](disclaimer.md).

---

## Is This For You?

### ✅ Use this framework if you are:

- An **M365 admin or cloud architect** deploying Microsoft 365 Copilot at a bank, insurer, broker-dealer, or credit union
- A **compliance or security engineer** who needs to prepare for a FINRA, SEC, OCC, SOX, or GLBA examination related to Copilot
- A **CSA or CSM** helping an FSI customer enable Copilot and needing a governance baseline to hand them
- An **engineer deploying Copilot for the first time** and wanting to know what you *must* configure vs. what is optional

### ❌ This is NOT the right place if you are:

- Deploying **custom AI agents** built in Copilot Studio or Agent Builder → see [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov)
- Looking for **prompt engineering guides** or how to *use* Copilot features as an end user → see [Microsoft Adoption Hub](https://adoption.microsoft.com/en-us/copilot/)
- Working in a **non-regulated industry** — this framework's controls are calibrated for financial services regulatory obligations and may be overly restrictive for other industries
- Trying to understand **what Microsoft 365 Copilot is** — start with [Microsoft's official docs](https://learn.microsoft.com/en-us/copilot/microsoft-365/)

---

## How This Differs from Microsoft's Copilot Docs

Microsoft's documentation explains how to deploy and use Copilot. This framework addresses the governance gap that Microsoft's docs do not cover:

- **FSI-specific regulatory mappings.** Each control maps to specific regulations — FINRA Rule 4511(a), FINRA Rule 3110, SEC Rule 17a-4, OCC Bulletin 2011-12, GLBA Section 501(b), and others. Microsoft's deployment guides do not provide these mappings.
- **Three governance tiers.** Instead of one-size-fits-all guidance, each control provides Baseline, Recommended, and Regulated implementation levels — so you can match your governance posture to your organization's risk profile.
- **Examination-ready artifacts.** The framework includes evidence collection procedures, audit readiness checklists, and examination response guides that help support your organization's ability to demonstrate a defensible governance posture to examiners.

Organizations should verify these configurations meet their specific regulatory obligations. No single framework addresses all requirements for every institution.

---

## Scenario Guide — Where Should I Go?

| Your Situation | Where to Start |
|---|---|
| "We just got Copilot licenses and need to know what to set up before we turn it on" | [Pillar 1 — Readiness & Assessment](controls/pillar-1-readiness/index.md) |
| "Compliance asked us to prove Copilot won't surface sensitive data to the wrong people" | [Control 1.2 — Oversharing Detection](controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) + [Control 2.4 — Information Barriers](controls/pillar-2-security/2.4-information-barriers.md) |
| "We have a FINRA exam coming up and need to show our Copilot audit posture" | [Pillar 3 — Compliance & Audit](controls/pillar-3-compliance/index.md) + [Audit Readiness Checklist](playbooks/compliance-and-audit/audit-readiness-checklist.md) |
| "Security team flagged Copilot as a DLP risk — how do we address it?" | [Control 2.1 — DLP Policies for Copilot](controls/pillar-2-security/2.1-dlp-policies-for-copilot.md) |
| "We need to show the board an executive-level governance summary" | [Executive Summary](framework/executive-summary.md) |
| "I'm an admin and just need to know which toggles to flip and where" | [Copilot Admin Toggles](reference/copilot-admin-toggles.md) |
| "We're doing a phased rollout — what's the recommended sequence?" | [Adoption Roadmap](framework/adoption-roadmap.md) + [Phase 0 Playbook](playbooks/getting-started/phase-0-governance-setup.md) |
| "We already deployed Copilot and now need to retroactively govern it" | [Implementation Checklist](getting-started/checklist.md) — start from Pillar 2 |
| "We need to map our controls to NIST AI RMF" | [NIST AI RMF Crosswalk](reference/nist-ai-rmf-crosswalk.md) |
| "Copilot surfaced sensitive data to the wrong person — what do we do?" | [AI Incident Response Playbook](playbooks/incident-and-risk/ai-incident-response-playbook.md) + [Control 2.1 — DLP](controls/pillar-2-security/2.1-dlp-policies-for-copilot.md) |
| "We want to benchmark our current Copilot governance posture and identify gaps" | [Governance Scorecard](assessment/index.md) |

---

## Orientation Path

This path helps you understand what the framework covers and how it applies to your organization. For hands-on implementation, see the [Quick Start Guide](getting-started/quick-start.md) (estimated 2–4 hours for baseline governance).

1. **Read the Executive Summary** — understand what this framework covers and who it's for → [Executive Summary](framework/executive-summary.md)
2. **Scan the Four Pillars** — understand the governance lifecycle at a glance → [Control Catalog](controls/index.md)
3. **Review the Readiness Assessment** — see what a pre-deployment assessment involves → [Control 1.1 — Copilot Readiness Assessment](controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md)
4. **Check your regulatory obligations** — identify which regulations apply to your organization → [Regulatory Framework](framework/regulatory-framework.md)
5. **Open the Implementation Checklist** — your actionable to-do list for getting started → [Implementation Checklist](getting-started/checklist.md)

!!! tip "Ready to assess your current posture?"
    Once you've reviewed the controls, use the [Governance Scorecard](assessment/index.md) to score your organization across all 54 controls, identify gaps, and generate a prioritized remediation roadmap.

---

## How This Framework Is Organized

| Layer | What It Answers | Who Uses It |
|---|---|---|
| **[Framework](framework/index.md)** | Why governance matters, what regulations apply, how Copilot works architecturally | CISOs, compliance leads, architects |
| **[Controls](controls/index.md)** | What specific configurations are required and why — 54 controls across 4 lifecycle pillars | Security engineers, M365 admins |
| **[Playbooks](playbooks/index.md)** | Step-by-step how to implement each control, with portal walkthroughs and PowerShell automation | Engineers doing the actual work |

Each control provides three governance tiers: **Baseline** (minimum viable), **Recommended** (production best practices), and **Regulated** (examination-ready).
