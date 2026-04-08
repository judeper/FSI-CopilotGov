# License Requirements

License requirements for each governance capability in the FSI Copilot Governance Framework. Use this reference to validate your organization's licensing posture before and during implementation.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. License requirements are subject to change by Microsoft. Verify current licensing at [Microsoft 365 licensing documentation](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-overview). See [full disclaimer](../disclaimer.md).

---

## License Tiers Overview

| License | Description | FSI Relevance |
|---------|-------------|---------------|
| **Microsoft 365 E3** | Productivity, security basics, compliance basics | Baseline governance — requires add-ons for most regulated controls |
| **Microsoft 365 E5** | Full productivity, advanced security, advanced compliance | Recommended for FSI — includes Purview, Defender, and advanced compliance |
| **Microsoft 365 Copilot** | Per-user add-on enabling AI assistance across M365 apps | Required for any Copilot functionality |
| **Microsoft Purview Suite (formerly E5 Compliance)** | Add-on for E3 providing E5-level compliance capabilities | Alternative to full E5 for compliance-focused deployments |
| **Microsoft 365 E5 Security** | Add-on for E3 providing E5-level security capabilities | Alternative to full E5 for security-focused deployments |
| **SharePoint Advanced Management (SAM)** | Advanced SharePoint governance (DAG reports, site lifecycle, RCD, RAC) | Included with Microsoft 365 Copilot licenses at no additional cost (Ignite 2024); also available as standalone add-on (~$3/user/month) for non-Copilot environments |
| **Microsoft 365 Copilot (PAYG)** | Pay-as-you-go billing for approved Copilot services | Usage-based Azure billing tied to a billing policy; commonly used for Copilot Chat without assigning full seats |
| **Microsoft 365 F1/F3** | Frontline worker licenses | Copilot availability extended to Frontline SKUs; check current Microsoft documentation for feature parity with E3/E5 |

---

## Pillar 1: Readiness and Assessment

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 1.1 | Readiness Assessment — basic sharing audit | Included | Included | -- | -- | Basic sharing reports available in SharePoint Admin Center |
| 1.2 | Oversharing Detection (DSPM for AI, SAM reports) | -- | Included | Included | Purview Suite | SAM is included with Copilot licenses (Ignite 2024); DSPM for AI requires E5 and Copilot |
| 1.3 | Restricted SharePoint Search Configuration | Included | Included | -- | -- | Available in SharePoint Admin Center; limits Microsoft 365 Copilot Chat grounding |
| 1.4 | Semantic Index Governance and Scope Control | -- | -- | Included | -- | Semantic Index processing is part of Copilot license |
| 1.5 | Sensitivity Label Taxonomy Review | -- | Included | -- | Purview Suite or Purview add-on | Content explorer and data classification dashboards |
| 1.6 | Permission Model Audit | Included | Included | -- | -- | Native SharePoint, OneDrive, Exchange, Teams admin capabilities |
| 1.6 | Permission Model Audit — Entra ID Access Reviews | -- | Included | -- | Entra ID P2 | Automated access reviews for guest and external accounts |
| 1.7 | SharePoint Advanced Management Readiness | -- | -- | Included | SharePoint Advanced Management (if no Copilot license) | SAM site lifecycle management included with Copilot licenses |
| 1.8 | Information Architecture Review | Included | Included | -- | -- | Organizational process; no specific license needed |
| 1.9 | License Planning and Assignment Strategy | Included | Included | -- | -- | Group-based license assignment via Entra |
| 1.10 | Vendor Risk Management | Included | Included | -- | -- | Organizational process; no specific license needed |
| 1.11 | Change Management and Adoption Planning | Included | Included | -- | -- | Organizational process; no specific license needed |
| 1.12 | Training and Awareness Program | Included | Included | -- | -- | Organizational process; Viva Learning available for training delivery |
| 1.13 | Extensibility Readiness (Connectors, Plugins, Agents) | Included | Included | Included | -- | Organizational process; M365 Admin Center for plugin governance |
| 1.14 | Item-Level Permission Scanning | Included | Included | -- | -- | SharePoint and OneDrive admin capabilities |
| 1.15 | Permissions Drift Detection (SAM) | -- | -- | Included | SharePoint Advanced Management (if no Copilot license) | SAM permissions change tracking; included with Copilot licenses |

---

## Pillar 2: Security and Protection

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 2.1 | DLP Policies (basic locations) | Included | Included | -- | -- | Basic DLP for Exchange, SharePoint, OneDrive |
| 2.1 | DLP for Copilot location | -- | Included | Included | Purview Suite | Copilot as a DLP location requires E5 compliance capabilities |
| 2.1 | Custom Sensitive Information Types | Included | Included | -- | -- | Custom SITs available in E3; exact data match requires E5 |
| 2.1 | Exact Data Match (EDM) | -- | Included | -- | Purview Suite | High-precision matching for structured data |
| 2.1 | DLP Policy Tips | Included | Included | -- | -- | User notifications for DLP policy matches |
| 2.2 | Sensitivity Labels (manual) | Included | Included | -- | -- | Manual label application available in E3 |
| 2.2 | Sensitivity Labels (auto-labeling) | -- | Included | -- | Purview Suite or Information Protection P2 | Server-side auto-labeling requires E5 or add-on |
| 2.2 | Auto-labeling Policies | -- | Included | -- | Purview Suite or Information Protection P2 | Service-side auto-labeling policies |
| 2.2 | Label Inheritance (Copilot) | -- | -- | Included | -- | Copilot label inheritance is part of Copilot functionality |
| 2.3 | Conditional Access (basic) | Included | Included | -- | -- | Requires Entra ID P1 (included in E3) |
| 2.3 | Conditional Access (advanced) | -- | Included | -- | Entra ID P2 | Risk-based conditional access and sign-in risk policies |
| 2.4 | Information Barriers | -- | Included | -- | Purview Suite | Required for MNPI walls in broker-dealer environments |
| 2.5 | Data Minimization and Grounding Scope | Included | Included | Included | -- | Configuration-based; limits Copilot grounding data sources |
| 2.6 | Web Search and Web Grounding Controls | Included | Included | Included | -- | Admin toggle in M365 Admin Center |
| 2.7 | Data Residency and Cross-Border Data Flow | Included | Included | -- | Microsoft 365 Multi-Geo (optional) | Multi-Geo requires add-on; Microsoft data boundary configuration |
| 2.8 | Encryption (Data in Transit and at Rest) | Included | Included | -- | -- | Rights Management encryption included in E3 |
| 2.9 | Defender for Cloud Apps — Session Controls | -- | Included | -- | E5 Security or Defender for Cloud Apps | Session and access policies for cloud app governance |
| 2.10 | Insider Risk Detection | -- | Included | -- | Purview Suite or Insider Risk add-on | Anomalous Copilot usage detection |
| 2.11 | Copilot Pages Security and Sharing Controls | Included | Included | Included | -- | Admin settings for Copilot Pages sharing |
| 2.12 | External Sharing and Guest Access Governance | Included | Included | -- | -- | Entra ID access reviews require P2 (included in E5) |
| 2.13 | Plugin and Graph Connector Security Governance | Included | Included | Included | -- | Integrated Apps settings in M365 Admin Center |
| 2.14 | Declarative and SharePoint Agents Governance | Included | Included | Included | -- | Admin settings for agent deployment and management |
| 2.15 | Network Security and Private Connectivity | Included | Included | -- | -- | Network-level controls are infrastructure; not license-dependent |

---

## Pillar 3: Compliance and Audit

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 3.1 | Audit Logging (basic — 180 days) | Included | Included | -- | -- | 180-day retention in E3 |
| 3.1 | Audit Logging (Premium — 1 year default, up to 10 years) | -- | Included | -- | Purview Suite | Extended retention, high-fidelity events, Copilot-specific events |
| 3.1 | Copilot interaction audit events | -- | Included | Included | Purview Suite | Detailed Copilot audit events require Audit (Premium) |
| 3.2 | Retention Policies (basic) | Included | Included | -- | -- | Basic retention policies for Exchange, SharePoint, OneDrive, Teams |
| 3.2 | Retention Policies (advanced — adaptive scopes) | -- | Included | -- | Purview Suite | Adaptive retention scopes for dynamic policy targeting |
| 3.3 | eDiscovery (Standard) | Included | Included | -- | -- | Basic search and export |
| 3.3 | eDiscovery (Premium) | -- | Included | -- | Purview Suite | Advanced workflows, review sets, custodian management, Copilot content search |
| 3.4 | Communication Compliance Monitoring | -- | Included | -- | Purview Suite or Communication Compliance add-on | Required for FINRA 3110 supervisory review |
| 3.5 | FINRA Rule 2210 Compliance | -- | Included | -- | Purview Suite (for Communication Compliance) | Uses Communication Compliance to flag Copilot-drafted content |
| 3.6 | Supervision and Oversight (FINRA 3110 / SEC Reg BI) | -- | Included | -- | Purview Suite (for Communication Compliance) | Uses Communication Compliance for supervision policies |
| 3.7 | Regulatory Reporting | Included | Included | -- | -- | Process-based; Communication Compliance enhances detection |
| 3.8 | Model Risk Management Alignment (OCC 2011-12 / SR 11-7) | Included | Included | -- | -- | Primarily organizational process; no specific license for documentation |
| 3.9 | AI Disclosure, Transparency, and SEC Marketing Rule | Included | Included | -- | -- | Organizational process; Purview labeling and DLP support disclosure workflows |
| 3.10 | SEC Reg S-P — Privacy of Consumer Financial Information | Included | Included | -- | -- | Process-based with DLP/label enforcement; Priva add-on optional |
| 3.11 | Record Keeping and Books-and-Records Compliance | -- | Included | -- | Purview Suite | Requires Audit (Premium) and advanced retention for WORM-equivalent |
| 3.12 | Evidence Collection and Audit Attestation | Included | Included | -- | -- | Process-based; Content Search available in E3 for evidence collection |
| 3.13 | FFIEC IT Examination Handbook Alignment | Included | Included | -- | -- | Organizational mapping process; no specific license |

---

## Pillar 4: Operations and Monitoring

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 4.1 | Copilot Admin Settings and Feature Management | Included | Included | Included | -- | M365 Admin Center settings; requires Copilot license to be meaningful |
| 4.2 | Copilot in Teams Meetings Governance | Included | Included | Included | -- | Teams meeting policy settings in Teams Admin Center |
| 4.3 | Copilot in Teams Phone and Queues Governance | Included | Included | Included | -- | Teams Phone settings in Teams Admin Center |
| 4.4 | Copilot in Viva Suite Governance | Included | Included | Included | -- | Viva app admin settings; Viva Insights requires add-on for advanced analytics |
| 4.5 | Copilot Usage Analytics and Adoption Reporting | Included | Included | Included | -- | Usage reports in M365 Admin Center |
| 4.6 | Viva Insights and Copilot Analytics | Included | Included | Included | -- | Basic usage reports in M365 Admin Center; Viva Insights adds detail |
| 4.6 | Viva Insights (advanced analytics) | -- | -- | -- | Viva Insights | Advanced Copilot adoption analytics |
| 4.7 | Copilot Feedback and Telemetry Data Governance | Included | Included | Included | -- | Admin controls for feedback and telemetry in M365 Admin Center |
| 4.8 | Cost Allocation and License Optimization | Included | Included | Included | -- | License utilization tracking in M365 Admin Center |
| 4.8 | Cost Allocation — PAYG Governance | -- | -- | -- | Azure-backed billing policy | PAYG billing requires billing policy governance, Cost Management review, and budget notifications |
| 4.9 | Incident Reporting and Root Cause Analysis | Included | Included | -- | -- | Process-based; Defender and Sentinel enhance automation |
| 4.10 | Business Continuity and Disaster Recovery | Included | Included | -- | -- | Process-based planning |
| 4.11 | Microsoft Sentinel Integration for Copilot Events | -- | -- | -- | Microsoft Sentinel | Separate consumption-based (pay-per-GB) service |
| 4.12 | Change Management for Copilot Feature Rollouts | Included | Included | -- | -- | Message Center monitoring; no additional license |
| 4.13 | Copilot Extensibility and Agent Operations Governance | Included | Included | Included | -- | Integrated Apps and agent settings in M365 Admin Center |

---

## License Summary by Governance Level

### Baseline Governance

| Required License | Purpose |
|-----------------|---------|
| Microsoft 365 E3 or E5 | Base productivity and admin capabilities |
| Microsoft 365 Copilot | Copilot functionality per user |

Baseline governance is achievable with E3 + Copilot, but with significant manual effort for monitoring and limited audit/retention capabilities.

### Recommended Governance

| Required License | Purpose |
|-----------------|---------|
| Microsoft 365 E5 (strongly recommended) | Advanced compliance, security, and audit capabilities |
| Microsoft 365 Copilot | Copilot functionality per user; includes SAM at no additional cost |

E5 is strongly recommended for FSI environments. The cost of individual add-ons to E3 typically exceeds the incremental cost of E5. Note: SharePoint Advanced Management (SAM) is included with Copilot licenses and no longer requires a separate add-on for Copilot-licensed users.

### Regulated Governance

| Required License | Purpose |
|-----------------|---------|
| Microsoft 365 E5 | Full compliance and security suite |
| Microsoft 365 Copilot | Copilot functionality per user; includes SAM at no additional cost |
| Microsoft Sentinel | SIEM/SOAR for Copilot audit data |
| Viva Insights (optional) | Advanced Copilot adoption analytics |
| Microsoft 365 Copilot PAYG (optional) | Pay-as-you-go for approved occasional Copilot Chat users through billing policy governance |

---

## E3 vs. E5 Comparison for FSI Governance

| Capability | E3 | E5 | FSI Impact |
|-----------|----|----|------------|
| Manual sensitivity labels | Yes | Yes | -- |
| Auto-labeling policies | No | Yes | Manual labeling only in E3 increases operational burden |
| DLP (basic locations) | Yes | Yes | -- |
| DLP for Copilot location | No | Yes | Cannot apply DLP to Copilot interactions in E3 |
| Information Barriers | No | Yes | Cannot enforce MNPI walls without E5 |
| Communication Compliance | No | Yes | Cannot perform FINRA 3110 supervisory review without E5 |
| Audit (Premium) | No | Yes | Limited to 180-day audit retention in E3 |
| eDiscovery (Premium) | No | Yes | Limited search and review capabilities in E3 |
| Insider Risk Management | No | Yes | No anomalous AI usage detection in E3 |
| DSPM for AI | No | Yes | No Copilot-specific data posture monitoring in E3 |
| Conditional Access (risk-based) | No | Yes | No risk-based policies in E3 (basic CA available) |
| Defender for Cloud Apps | No | Yes | No session policies for Copilot web sessions in E3 |

!!! tip "Recommendation"
    For any FSI organization subject to FINRA, SEC, or banking regulations, **Microsoft 365 E5 is the practical minimum** for achieving Recommended or Regulated governance levels. The regulatory requirements for audit retention, supervisory review, information barriers, and eDiscovery effectively require E5 capabilities.

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
