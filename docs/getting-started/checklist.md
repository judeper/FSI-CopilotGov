# Implementation Checklist

Use this checklist to track implementation of all 54 controls across the four governance pillars. Each item includes its governance level and space for status tracking.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## How to Use This Checklist

**Governance Levels:**

| Code | Level | Description |
|------|-------|-------------|
| **B** | Baseline | Minimum viable governance for initial Copilot deployment |
| **R** | Recommended | Best practices for most production environments |
| **Reg** | Regulated | Comprehensive controls for high-risk, examination-ready deployments |

**Status Values:** Not Started, In Progress, Complete, N/A

**Implementation Order:** Start with Pillar 1 (Readiness) before enabling Copilot, then implement Pillar 2 (Security) and Pillar 3 (Compliance) in parallel, and Pillar 4 (Operations) alongside rollout.

---

## Pillar 1: Readiness and Assessment (13 Controls)

Pre-deployment data hygiene, oversharing remediation, permissions audit, sensitivity label review, licensing, vendor risk, change management, and extensibility readiness.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 1.1 | Copilot Readiness Assessment | B | | | Pre-deployment assessment of data environment, classification maturity, and permission sprawl |
| [ ] | 1.2 | Oversharing Detection (DSPM for AI) | B | | | Purview DSPM oversharing assessments, Activity Explorer, and remediation workflows |
| [ ] | 1.3 | Restricted SharePoint Search | R | | | Configure RSS to limit Copilot grounding scope to curated allow-list of SharePoint sites |
| [ ] | 1.4 | Semantic Index Governance | R | | | Govern Semantic Index scope and understand Copilot grounding behavior across workloads |
| [ ] | 1.5 | Sensitivity Label Taxonomy Review | B | | | Review and update label taxonomy for Copilot-specific scenarios (auto-labeling, DLP integration) |
| [ ] | 1.6 | Permission Model Audit | B | | | Comprehensive permission audit across SharePoint, OneDrive, Exchange, Teams, and Graph |
| [ ] | 1.7 | SharePoint Advanced Management | R | | | Deploy SAM features: Data Access Governance reports, site access reviews, Restricted Content Discovery |
| [ ] | 1.8 | Information Architecture Review | R | | | Review SharePoint site structure, Teams channels, and OneDrive folders for grounding quality |
| [ ] | 1.9 | License Planning | B | | | Copilot license types, assignment strategies, prerequisite licenses, and governance add-ons |
| [ ] | 1.10 | Vendor Risk Management | Reg | | | Third-party risk management for Microsoft as AI vendor, including subprocessor review |
| [ ] | 1.11 | Change Management and Adoption | R | | | Organizational change management framework for Copilot rollout and adoption |
| [ ] | 1.12 | Training and Awareness | B | | | Role-based training on responsible AI use, data sensitivity, prompt hygiene, and regulatory boundaries |
| [ ] | 1.13 | Extensibility Readiness | Reg | | | Pre-deployment assessment for Graph connectors, plugins, and declarative agents |

---

## Pillar 2: Security and Protection (15 Controls)

DLP, sensitivity labels, conditional access, information barriers, data minimization, encryption, Defender integration, and extensibility security.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 2.1 | DLP Policies for Copilot | B | | | Deploy DLP policies targeting the M365 Copilot location for sensitive data in prompts and responses |
| [ ] | 2.2 | Sensitivity Labels and Classification | B | | | Label taxonomy and auto-labeling strategy governing Copilot content classification |
| [ ] | 2.3 | Conditional Access Policies | B | | | Entra CA policies for device compliance, location restrictions, and risk-based authentication |
| [ ] | 2.4 | Information Barriers (Chinese Wall) | Reg | | | Purview Information Barriers to enforce MNPI separation across Copilot interactions |
| [ ] | 2.5 | Data Minimization and Grounding Scope | R | | | Limit data scope Copilot can access via RSS, site exclusions, and data access governance |
| [ ] | 2.6 | Web Search Controls | B | | | Govern web search and web grounding capabilities; disable for regulated user populations |
| [ ] | 2.7 | Data Residency | R | | | Governance over data residency and cross-border data flows for Copilot processing |
| [ ] | 2.8 | Encryption | B | | | Verify encryption for data in transit, at rest, and during AI processing (CMK/DKE implications) |
| [ ] | 2.9 | Defender for Cloud Apps | R | | | MDCA session policies for real-time monitoring and anomaly detection of Copilot usage |
| [ ] | 2.10 | Insider Risk Detection | R | | | Purview IRM policies to detect anomalous Copilot usage indicating data exfiltration or misuse |
| [ ] | 2.11 | Copilot Pages Security | R | | | Security and sharing controls for Copilot Pages (creation, sharing scope, label inheritance) |
| [ ] | 2.12 | External Sharing Governance | R | | | Govern guest access and external sharing settings impacting Copilot content surfacing |
| [ ] | 2.13 | Plugin and Connector Security | R | | | Security governance for Copilot plugins and Graph connectors (approval, OAuth, monitoring) |
| [ ] | 2.14 | Declarative Agents Governance | R | | | Govern creation, sharing, and data boundaries for SharePoint declarative agents |
| [ ] | 2.15 | Network Security | Reg | | | Network-level security controls, private connectivity options, and traffic inspection for Copilot |

---

## Pillar 3: Compliance and Audit (13 Controls)

Audit logging, retention, eDiscovery, communication compliance, FINRA/SEC record-keeping, supervisory review, model risk management, and regulatory reporting.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 3.1 | Copilot Audit Logging | B | | | Copilot-specific audit events in Purview Unified Audit Log (CopilotInteraction events) |
| [ ] | 3.2 | Data Retention Policies | B | | | Retention policies for Copilot chat history, Pages, Teams transcripts, and Exchange interactions |
| [ ] | 3.3 | eDiscovery for Copilot Content | R | | | eDiscovery (Premium) search, hold, review, and export for Copilot-generated content |
| [ ] | 3.4 | Communication Compliance | R | | | Purview Communication Compliance policies monitoring Copilot-assisted communications |
| [ ] | 3.5 | FINRA 2210 Compliance | Reg | | | Content standards and pre-review requirements for Copilot-drafted customer communications |
| [ ] | 3.6 | Supervision and Oversight | Reg | | | Written supervisory procedures and qualified supervisor assignment for Copilot usage (FINRA 3110) |
| [ ] | 3.7 | Regulatory Reporting | R | | | Compliance reporting obligations, automated report generation, and CFPB UDAAP considerations |
| [ ] | 3.8 | Model Risk Management | Reg | | | MRM framework alignment (OCC 2011-12 / SR 11-7) for Copilot as vendor-provided AI model |
| [ ] | 3.9 | AI Disclosure and Transparency | Reg | | | AI disclosure requirements, SEC Marketing Rule compliance, and anti-AI-washing controls |
| [ ] | 3.10 | SEC Reg S-P Privacy | Reg | | | Copilot access to consumer financial information and NPI safeguard requirements |
| [ ] | 3.11 | Record Keeping | B | | | SEC 17a-3/4 and FINRA 4511 record-keeping for Copilot interactions (WORM, metadata, chain of custody) |
| [ ] | 3.12 | Evidence Collection | R | | | Standardized evidence collection workflows and attestation procedures for examinations |
| [ ] | 3.13 | FFIEC Alignment | R | | | Mapping to FFIEC IT Examination Handbook booklets and Cybersecurity Assessment Tool |

---

## Pillar 4: Operations and Monitoring (13 Controls)

Admin settings, per-app configuration, analytics, Viva governance, cost tracking, incident response, Sentinel SIEM, and change management.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 4.1 | Admin Settings and Feature Management | B | | | Centralized governance over Copilot admin settings, feature toggles, and Baseline Security Mode |
| [ ] | 4.2 | Teams Meetings Governance | B | | | Governance for Copilot in Teams meetings (transcription, recap, notes, and follow-up actions) |
| [ ] | 4.3 | Teams Phone and Queues | R | | | Governance for Copilot in Teams Phone (call summarization) and Queues (agent assist) |
| [ ] | 4.4 | Viva Suite Governance | R | | | Governance across Viva Insights, Engage, Learning, Pulse, and Goals (employee privacy, data aggregation) |
| [ ] | 4.5 | Usage Analytics | B | | | Structured monitoring and reporting of Copilot usage to measure control effectiveness and adoption |
| [ ] | 4.6 | Viva Insights Measurement | R | | | Copilot Impact Dashboard governance (productivity metrics, time savings, ROI) with privacy safeguards |
| [ ] | 4.7 | Feedback and Telemetry | R | | | Governance for Copilot user feedback data and telemetry (privacy, data collection scope, residency) |
| [ ] | 4.8 | Cost Allocation | R | | | License cost tracking, per-department allocation, usage-based optimization, and budget forecasting |
| [ ] | 4.9 | Incident Reporting | R | | | AI-specific incident classification, reporting, root cause analysis, and remediation tracking |
| [ ] | 4.10 | Business Continuity | R | | | BC/DR planning for Copilot dependency (service degradation, fallback procedures, SLA monitoring) |
| [ ] | 4.11 | Sentinel Integration | Reg | | | Sentinel data connectors, KQL detection queries, alert rules, workbooks, and SOAR playbooks |
| [ ] | 4.12 | Change Management for Rollouts | R | | | Message Center monitoring, feature update impact assessment, and targeted release ring management |
| [ ] | 4.13 | Extensibility Governance | R | | | Ongoing lifecycle governance for deployed plugins, Graph connectors, and declarative agents |

---

## Summary by Governance Level

| Level | Pillar 1 | Pillar 2 | Pillar 3 | Pillar 4 | Total |
|-------|----------|----------|----------|----------|-------|
| **Baseline (B)** | 6 | 5 | 3 | 3 | **17** |
| **Recommended (R)** | 5 | 8 | 5 | 9 | **27** |
| **Regulated (Reg)** | 2 | 2 | 5 | 1 | **10** |
| **Pillar Total** | **13** | **15** | **13** | **13** | **54** |

!!! tip "Implementation Priority"
    - **Phase 1 (Pre-deployment):** All Baseline controls (17 controls)
    - **Phase 2 (Early production):** All Recommended controls (27 controls)
    - **Phase 3 (Maturity):** All Regulated controls (10 controls)

---

## Tracking Template

Download or copy this checklist into your governance tracking system. Recommended fields for your internal tracker:

| Field | Description |
|-------|-------------|
| **Control #** | Reference number (e.g., 1.1) |
| **Control Name** | Full control name |
| **Governance Level** | B / R / Reg |
| **Status** | Not Started / In Progress / Complete / N/A |
| **Owner** | Assigned individual or team |
| **Target Date** | Planned completion date |
| **Completion Date** | Actual completion date |
| **Evidence** | Link to configuration screenshot or audit evidence |
| **Notes** | Implementation notes, exceptions, or deviations |

---

*FSI Copilot Governance Framework v1.0 - February 2026*
