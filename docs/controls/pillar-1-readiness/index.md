# Pillar 1: Readiness & Assessment

**Pre-deployment governance controls for Microsoft 365 Copilot in financial services environments.**

---

## Overview

Pillar 1 establishes the foundational readiness posture required before deploying Microsoft 365 Copilot into a regulated financial services environment. These 16 controls address the critical pre-deployment activities that help reduce risk from data oversharing, permission sprawl, inadequate classification, and insufficient organizational preparedness.

Financial regulators increasingly expect that institutions demonstrate due diligence *before* deploying AI capabilities -- not after. The controls in this pillar provide a structured approach to assessing data hygiene, remediating access risks, planning license strategy, and preparing the organization for responsible Copilot adoption.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../../disclaimer.md).

---

## Why Readiness Matters for FSI

Microsoft 365 Copilot inherits the permissions of the user who invokes it. This means every existing oversharing issue, stale permission, and miscategorized document becomes a potential compliance exposure when Copilot surfaces content through natural language queries. Readiness controls help prevent these latent risks from becoming regulatory findings.

Key regulatory drivers for pre-deployment readiness:

- **GLBA §501(b):** Requires financial institutions to protect customer information through administrative, technical, and physical safeguards -- which begins with knowing where that information resides and who can access it.
- **FFIEC IT Handbook:** Expects institutions to conduct risk assessments before deploying new technology, including AI-powered tools.
- **Interagency AI Guidance (2023):** Calls for appropriate due diligence and risk management before adopting AI services from third-party providers.
- **Sarbanes-Oxley §§302/404 (where applicable to ICFR):** Internal control requirements that extend to AI-assisted financial reporting and document generation workflows.
- **FINRA 3110:** Supervisory obligations that must account for how Copilot may draft or modify regulated communications.

---

## Controls Summary

| Control ID | Control Name | Description | Governance Level |
|------------|-------------|-------------|------------------|
| [1.1](1.1-copilot-readiness-assessment.md) | Copilot Readiness Assessment and Data Hygiene | Pre-deployment assessment covering data classification maturity, permission sprawl analysis, stale content identification, and sensitive data inventory | Baseline |
| [1.2](1.2-sharepoint-oversharing-detection.md) | SharePoint Oversharing Detection and Remediation (DSPM for AI) | Microsoft Purview DSPM for AI oversharing assessments, weekly risk assessment cadence, Activity Explorer for Copilot interactions, and oversharing remediation workflows | Baseline |
| [1.3](1.3-restricted-sharepoint-search.md) | Restricted SharePoint Search Configuration | Restricted SharePoint Search (RSS) configuration to limit Copilot grounding scope to curated site lists with a 100-site governance limit | Recommended |
| [1.4](1.4-semantic-index-governance.md) | Semantic Index Governance and Scope Control | Governance of the Semantic Index scope, understanding what gets indexed, and controlling Copilot grounding behavior across workloads | Recommended |
| [1.5](1.5-sensitivity-label-taxonomy-review.md) | Sensitivity Label Taxonomy Review for Copilot | Review and update of sensitivity label taxonomy to address Copilot-specific scenarios including auto-labeling and DLP integration | Baseline |
| [1.6](1.6-permission-model-audit.md) | Permission Model Audit (SharePoint, OneDrive, Exchange, Teams, Graph) | Comprehensive permission audit across all workloads Copilot accesses via Microsoft Graph, with EEEU remediation priority | Baseline |
| [1.7](1.7-sharepoint-advanced-management.md) | SharePoint Advanced Management Readiness for Copilot | SharePoint Advanced Management (SAM) features for Copilot governance including Data Access Governance reports, site access reviews, and Restricted Content Discovery | Recommended |
| [1.8](1.8-information-architecture-review.md) | Information Architecture Review | Review of SharePoint site structure, Teams channel organization, and OneDrive folder structure for Copilot grounding quality | Recommended |
| [1.9](1.9-license-planning.md) | License Planning and Copilot Assignment Strategy | Copilot license types, assignment strategies, prerequisite licenses, and add-on requirements for governance tooling | Baseline |
| [1.10](1.10-vendor-risk-management.md) | Vendor Risk Management for Microsoft AI Services | Third-party risk management for Microsoft as AI vendor, including subprocessor review, data processing agreements, and responsible AI commitments | Regulated |
| [1.11](1.11-change-management-adoption.md) | Organizational Change Management and Adoption Planning | Change management framework for Copilot rollout including stakeholder communication, user readiness assessment, and adoption metrics | Recommended |
| [1.12](1.12-training-awareness.md) | Training and Awareness Program | Role-based training program covering responsible AI use, data sensitivity, prompt hygiene, and regulatory boundaries for Copilot users | Baseline |
| [1.13](1.13-extensibility-readiness.md) | Extensibility Readiness (Graph Connectors, Plugins, Declarative Agents) | Pre-deployment assessment for Copilot extensibility features including Graph connectors, plugins, and declarative agents | Regulated |
| [1.14](1.14-item-level-permission-scanning.md) | Item-Level Permission Scanning | Extend oversharing detection to individual files and folders with unique permissions that site-level tools miss, addressing the gap between site-level DAG and Copilot's file-level content surfacing | Recommended |
| [1.15](1.15-sharepoint-permissions-drift.md) | SharePoint Permissions Drift Detection | Establish permissions baselines and continuous drift detection to identify unauthorized or unintended permission changes that expand Copilot's data surface | Recommended |

---

## Implementation Sequence

The recommended implementation order for Pillar 1 controls:

```
Phase 1: Assessment (Week 1-2)
├── Control 1.1  Copilot Readiness Assessment
├── Control 1.6  Permission Model Audit
└── Control 1.8  Information Architecture Review

Phase 2: Remediation (Week 3-4)
├── Control 1.2  SharePoint Oversharing Detection and Remediation
├── Control 1.5  Sensitivity Label Taxonomy Review
├── Control 1.7  SharePoint Advanced Management Readiness
├── Control 1.14 Item-Level Permission Scanning
└── Control 1.15 SharePoint Permissions Drift Detection

Phase 3: Configuration (Week 5-6)
├── Control 1.3  Restricted SharePoint Search
├── Control 1.4  Semantic Index Governance
└── Control 1.9  License Planning and Assignment Strategy

Phase 4: Organizational Readiness (Week 7-8)
├── Control 1.10 Vendor Risk Management
├── Control 1.11 Change Management and Adoption
├── Control 1.12 Training and Awareness
└── Control 1.13 Extensibility Readiness
```

---

## Dependencies

Pillar 1 controls are primarily foundational and have few intra-pillar dependencies. However, several controls feed directly into Pillar 2 (Security & Protection) and Pillar 3 (Compliance & Audit):

| This Control | Feeds Into | Relationship |
|-------------|-----------|--------------|
| 1.2 Oversharing Detection | 2.x DLP Policies | Oversharing findings inform DLP rule creation |
| 1.14 Item-Level Scanning | 1.2 Oversharing Detection, 2.x DLP Policies | Item-level findings extend site-level oversharing remediation |
| 1.15 Permissions Drift | 1.2 Oversharing Detection, 2.x Conditional Access | Drift findings feed ongoing access control governance |
| 1.5 Sensitivity Labels | 2.x Label Enforcement | Label taxonomy must be defined before enforcement |
| 1.6 Permission Audit | 2.x Conditional Access | Permission findings inform access policies |
| 1.9 License Planning | All Pillars | Licensing determines which governance tools are available |
| 1.10 Vendor Risk | 3.x Audit Controls | Vendor assessments feed compliance evidence packages |

---

## Related Resources

- [Framework Executive Summary](../../framework/executive-summary.md)
- [Quick Start Guide](../../getting-started/quick-start.md)
- [Pillar 2: Security & Protection](../pillar-2-security/index.md)
- [Regulatory Mappings Reference](../../reference/regulatory-mappings.md)

---

*FSI Copilot Governance Framework v1.3 - April 2026*
