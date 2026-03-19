# Control Catalog

The FSI Copilot Governance Framework contains **56 controls** organized across four lifecycle-based pillars, providing comprehensive governance coverage for Microsoft 365 Copilot in US financial services.

---

## Control Index

### Pillar 1: Readiness & Assessment (15 Controls)

Pre-deployment data hygiene, oversharing detection, permission audits, and license planning.

| ID | Control | Governance Level |
|----|---------|-----------------|
| 1.1 | [Copilot Readiness Assessment and Data Hygiene](pillar-1-readiness/1.1-copilot-readiness-assessment.md) | Baseline |
| 1.2 | [SharePoint Oversharing Detection and Remediation (DSPM for AI)](pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) | Baseline |
| 1.3 | [Restricted SharePoint Search Configuration](pillar-1-readiness/1.3-restricted-sharepoint-search.md) | Recommended |
| 1.4 | [Semantic Index Governance and Scope Control](pillar-1-readiness/1.4-semantic-index-governance.md) | Recommended |
| 1.5 | [Sensitivity Label Taxonomy Review for Copilot](pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md) | Baseline |
| 1.6 | [Permission Model Audit](pillar-1-readiness/1.6-permission-model-audit.md) | Baseline |
| 1.7 | [SharePoint Advanced Management Readiness for Copilot](pillar-1-readiness/1.7-sharepoint-advanced-management.md) | Recommended |
| 1.8 | [Information Architecture Review](pillar-1-readiness/1.8-information-architecture-review.md) | Recommended |
| 1.9 | [License Planning and Copilot Assignment Strategy](pillar-1-readiness/1.9-license-planning.md) | Baseline |
| 1.10 | [Vendor Risk Management for Microsoft AI Services](pillar-1-readiness/1.10-vendor-risk-management.md) | Regulated |
| 1.11 | [Organizational Change Management and Adoption Planning](pillar-1-readiness/1.11-change-management-adoption.md) | Baseline |
| 1.12 | [Training and Awareness Program](pillar-1-readiness/1.12-training-awareness.md) | Baseline |
| 1.13 | [Extensibility Readiness](pillar-1-readiness/1.13-extensibility-readiness.md) | Recommended |
| 1.14 | [Item-Level Permission Scanning](pillar-1-readiness/1.14-item-level-permission-scanning.md) | Recommended |
| 1.15 | [SharePoint Permissions Drift Detection](pillar-1-readiness/1.15-sharepoint-permissions-drift.md) | Recommended |

---

### Pillar 2: Security & Protection (15 Controls)

DLP, sensitivity labels, conditional access, encryption, information barriers, and Defender integration.

| ID | Control | Governance Level |
|----|---------|-----------------|
| 2.1 | [DLP Policies for M365 Copilot Interactions](pillar-2-security/2.1-dlp-policies-for-copilot.md) | Baseline |
| 2.2 | [Sensitivity Labels and Copilot Content Classification](pillar-2-security/2.2-sensitivity-labels-classification.md) | Baseline |
| 2.3 | [Conditional Access Policies for Copilot Workloads](pillar-2-security/2.3-conditional-access-policies.md) | Recommended |
| 2.4 | [Information Barriers for Copilot (Chinese Wall)](pillar-2-security/2.4-information-barriers.md) | Regulated |
| 2.5 | [Data Minimization and Grounding Scope](pillar-2-security/2.5-data-minimization-grounding-scope.md) | Recommended |
| 2.6 | [Copilot Web Search and Web Grounding Controls](pillar-2-security/2.6-web-search-controls.md) | Baseline |
| 2.7 | [Data Residency and Cross-Border Data Flow Governance](pillar-2-security/2.7-data-residency.md) | Regulated |
| 2.8 | [Encryption (Data in Transit and at Rest)](pillar-2-security/2.8-encryption.md) | Baseline |
| 2.9 | [Defender for Cloud Apps — Copilot Session Controls](pillar-2-security/2.9-defender-cloud-apps.md) | Recommended |
| 2.10 | [Insider Risk Detection for Copilot Usage Patterns](pillar-2-security/2.10-insider-risk-detection.md) | Recommended |
| 2.11 | [Copilot Pages Security and Sharing Controls](pillar-2-security/2.11-copilot-pages-security.md) | Baseline |
| 2.12 | [External Sharing and Guest Access Governance](pillar-2-security/2.12-external-sharing-governance.md) | Baseline |
| 2.13 | [Plugin and Graph Connector Security Governance](pillar-2-security/2.13-plugin-connector-security.md) | Recommended |
| 2.14 | [Declarative Agents from SharePoint — Creation and Sharing Governance](pillar-2-security/2.14-declarative-agents-governance.md) | Recommended |
| 2.15 | [Network Security and Private Connectivity](pillar-2-security/2.15-network-security.md) | Regulated |

---

### Pillar 3: Compliance & Audit (13 Controls)

Audit logging, retention, eDiscovery, communication compliance, and regulatory reporting.

| ID | Control | Governance Level |
|----|---------|-----------------|
| 3.1 | [Copilot Interaction Audit Logging](pillar-3-compliance/3.1-copilot-audit-logging.md) | Baseline |
| 3.2 | [Data Retention Policies for Copilot Interactions](pillar-3-compliance/3.2-data-retention-policies.md) | Baseline |
| 3.3 | [eDiscovery for Copilot-Generated Content](pillar-3-compliance/3.3-ediscovery-copilot-content.md) | Recommended |
| 3.4 | [Communication Compliance Monitoring](pillar-3-compliance/3.4-communication-compliance.md) | Recommended |
| 3.5 | [FINRA Rule 2210 Compliance for Copilot-Drafted Communications](pillar-3-compliance/3.5-finra-2210-compliance.md) | Regulated |
| 3.6 | [Supervision and Oversight (FINRA Rule 3110 / SEC Reg BI)](pillar-3-compliance/3.6-supervision-oversight.md) | Regulated |
| 3.7 | [Regulatory Reporting](pillar-3-compliance/3.7-regulatory-reporting.md) | Recommended |
| 3.8 | [Model Risk Management Alignment (OCC 2011-12 / SR 11-7)](pillar-3-compliance/3.8-model-risk-management.md) | Regulated |
| 3.9 | [AI Disclosure, Transparency, and SEC Marketing Rule](pillar-3-compliance/3.9-ai-disclosure-transparency.md) | Recommended |
| 3.10 | [SEC Reg S-P — Privacy of Consumer Financial Information](pillar-3-compliance/3.10-sec-reg-sp-privacy.md) | Regulated |
| 3.11 | [Record Keeping and Books-and-Records Compliance](pillar-3-compliance/3.11-record-keeping.md) | Baseline |
| 3.12 | [Evidence Collection and Audit Attestation](pillar-3-compliance/3.12-evidence-collection.md) | Recommended |
| 3.13 | [FFIEC IT Examination Handbook Alignment](pillar-3-compliance/3.13-ffiec-alignment.md) | Regulated |

---

### Pillar 4: Operations & Monitoring (13 Controls)

Feature management, per-app toggles, usage analytics, cost tracking, and incident response.

| ID | Control | Governance Level |
|----|---------|-----------------|
| 4.1 | [Copilot Admin Settings and Feature Management](pillar-4-operations/4.1-admin-settings-feature-management.md) | Baseline |
| 4.2 | [Copilot in Teams Meetings Governance](pillar-4-operations/4.2-teams-meetings-governance.md) | Recommended |
| 4.3 | [Copilot in Teams Phone and Queues Governance](pillar-4-operations/4.3-teams-phone-queues.md) | Recommended |
| 4.4 | [Copilot in Viva Suite Governance](pillar-4-operations/4.4-viva-suite-governance.md) | Recommended |
| 4.5 | [Copilot Usage Analytics and Adoption Reporting](pillar-4-operations/4.5-usage-analytics.md) | Baseline |
| 4.6 | [Microsoft Viva Insights — Copilot Impact Measurement](pillar-4-operations/4.6-viva-insights-measurement.md) | Recommended |
| 4.7 | [Copilot Feedback and Telemetry Data Governance](pillar-4-operations/4.7-feedback-telemetry.md) | Recommended |
| 4.8 | [Cost Allocation and License Optimization](pillar-4-operations/4.8-cost-allocation.md) | Baseline |
| 4.9 | [Incident Reporting and Root Cause Analysis](pillar-4-operations/4.9-incident-reporting.md) | Baseline |
| 4.10 | [Business Continuity and Disaster Recovery for Copilot Dependency](pillar-4-operations/4.10-business-continuity.md) | Recommended |
| 4.11 | [Microsoft Sentinel Integration for Copilot Events](pillar-4-operations/4.11-sentinel-integration.md) | Regulated |
| 4.12 | [Change Management for Copilot Feature Rollouts](pillar-4-operations/4.12-change-management-rollouts.md) | Baseline |
| 4.13 | [Copilot Extensibility Governance](pillar-4-operations/4.13-extensibility-governance.md) | Recommended |

---

## Control Statistics

| Pillar | Controls | Baseline | Recommended | Regulated |
|--------|----------|----------|-------------|-----------|
| 1. Readiness & Assessment | 15 | 7 | 7 | 1 |
| 2. Security & Protection | 15 | 6 | 6 | 3 |
| 3. Compliance & Audit | 13 | 3 | 5 | 5 |
| 4. Operations & Monitoring | 13 | 5 | 7 | 1 |
| **Total** | **56** | **21** | **25** | **10** |

---

## How to Use This Catalog

1. **Identify your governance level** — See [Governance Fundamentals](../framework/governance-fundamentals.md) to determine if your organization needs Baseline, Recommended, or Regulated controls
2. **Start with Pillar 1** — Complete readiness assessments before enabling Copilot
3. **Implement by priority** — Within each pillar, Baseline controls should be implemented first
4. **Use playbooks** — Each control has 4 implementation playbooks (portal walkthrough, PowerShell, verification, troubleshooting)

---

*FSI Copilot Governance Framework v1.2.1 — March 2026*
