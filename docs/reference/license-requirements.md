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
| **Microsoft 365 E5 Compliance** | Add-on for E3 providing E5-level compliance capabilities | Alternative to full E5 for compliance-focused deployments |
| **Microsoft 365 E5 Security** | Add-on for E3 providing E5-level security capabilities | Alternative to full E5 for security-focused deployments |
| **SharePoint Advanced Management (SAM)** | Add-on for advanced SharePoint governance | Required for oversharing reports and advanced site management |

---

## Pillar 1: Readiness and Assessment

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 1.1 | Oversharing Assessment (SAM reports) | -- | -- | -- | SharePoint Advanced Management | SAM is a separate add-on for both E3 and E5 |
| 1.1 | Basic SharePoint sharing audit | Included | Included | -- | -- | Basic sharing reports available in SharePoint Admin Center |
| 1.2 | SharePoint Permissions Review | Included | Included | -- | -- | Native SharePoint admin capabilities |
| 1.3 | Restricted SharePoint Search | Included | Included | -- | -- | Available in SharePoint Admin Center; limits Copilot Chat grounding |
| 1.4 | OneDrive Sharing Defaults | Included | Included | -- | -- | OneDrive admin settings |
| 1.5 | M365 Groups Membership Audit | Included | Included | -- | -- | Available via Entra admin center and PowerShell |
| 1.6 | Guest and External Access Review | Included | Included | -- | -- | Entra ID access reviews require Entra ID P2 (included in E5) |
| 1.6 | Entra ID Access Reviews | -- | Included | -- | Entra ID P2 | Automated access reviews for guest accounts |
| 1.7 | Inactive Site and Content Lifecycle | -- | -- | -- | SharePoint Advanced Management | SAM provides inactive site policies |
| 1.8 | Semantic Index Readiness | -- | -- | Included | -- | Semantic Index processing is part of Copilot license |
| 1.9 | License Assignment and Scoping | Included | Included | -- | -- | Group-based license assignment via Entra |
| 1.10 | Vendor Risk Assessment | Included | Included | -- | -- | Organizational process; no specific license needed |
| 1.11 | Data Classification Inventory | -- | Included | -- | E5 Compliance or Purview add-on | Content explorer and data classification dashboards |
| 1.12 | Governance Committee | Included | Included | -- | -- | Organizational process; no specific license needed |
| 1.13 | User Communication and Training | Included | Included | -- | -- | Organizational process; Viva Learning available for training delivery |

---

## Pillar 2: Security and Protection

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 2.1 | Sensitivity Labels (manual) | Included | Included | -- | -- | Manual label application available in E3 |
| 2.1 | Sensitivity Labels (auto-labeling) | -- | Included | -- | E5 Compliance or Information Protection P2 | Server-side auto-labeling requires E5 or add-on |
| 2.2 | Auto-labeling Policies | -- | Included | -- | E5 Compliance or Information Protection P2 | Service-side auto-labeling policies |
| 2.3 | Label Inheritance (Copilot) | -- | -- | Included | -- | Copilot label inheritance is part of Copilot functionality |
| 2.4 | DLP Policies (basic) | Included | Included | -- | -- | Basic DLP for Exchange, SharePoint, OneDrive |
| 2.4 | DLP for Copilot location | -- | Included | Included | E5 Compliance | Copilot as a DLP location requires E5 compliance capabilities |
| 2.5 | Custom Sensitive Information Types | Included | Included | -- | -- | Custom SITs available in E3; exact data match requires E5 |
| 2.5 | Exact Data Match (EDM) | -- | Included | -- | E5 Compliance | High-precision matching for structured data |
| 2.6 | DLP Policy Tips | Included | Included | -- | -- | User notifications for DLP policy matches |
| 2.7 | Conditional Access (basic) | Included | Included | -- | -- | Requires Entra ID P1 (included in E3) |
| 2.7 | Conditional Access (advanced) | -- | Included | -- | Entra ID P2 | Risk-based conditional access and sign-in risk policies |
| 2.8 | Information Barriers | -- | Included | -- | E5 Compliance | Required for MNPI walls in broker-dealer environments |
| 2.9 | Endpoint DLP | -- | Included | -- | E5 Compliance | DLP enforcement on Windows/macOS endpoints |
| 2.10 | Defender for Cloud Apps | -- | Included | -- | E5 Security or Defender for Cloud Apps | Session and access policies for cloud app governance |
| 2.11 | Insider Risk Management | -- | Included | -- | E5 Compliance or Insider Risk add-on | Anomalous Copilot usage detection |
| 2.12 | DSPM for AI | -- | Included | Included | E5 Compliance | Data Security Posture Management for AI; requires both E5 compliance and Copilot |
| 2.13 | Azure Information Protection encryption | Included | Included | -- | -- | Rights Management encryption included in E3 |
| 2.14 | Network Security | Included | Included | -- | -- | Network-level controls are infrastructure; not license-dependent |
| 2.15 | Zero Trust Alignment | Included | Included | -- | -- | Architectural approach; Entra ID P1 for Conditional Access is the key license |

---

## Pillar 3: Compliance and Audit

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 3.1 | Unified Audit Log (basic — 180 days) | Included | Included | -- | -- | 180-day retention in E3 |
| 3.1 | Audit (Premium — 1 year default, up to 10 years) | -- | Included | -- | E5 Compliance | Extended retention, high-fidelity events, Copilot-specific events |
| 3.1 | Copilot interaction audit events | -- | Included | Included | E5 Compliance | Detailed Copilot audit events require Audit (Premium) |
| 3.2 | Retention Policies (basic) | Included | Included | -- | -- | Basic retention policies for Exchange, SharePoint, OneDrive, Teams |
| 3.2 | Retention Policies (advanced — adaptive scopes) | -- | Included | -- | E5 Compliance | Adaptive retention scopes for dynamic policy targeting |
| 3.3 | eDiscovery (Standard) | Included | Included | -- | -- | Basic search and export |
| 3.3 | eDiscovery (Premium) | -- | Included | -- | E5 Compliance | Advanced workflows, review sets, custodian management, Copilot content search |
| 3.4 | Communication Compliance | -- | Included | -- | E5 Compliance or Communication Compliance add-on | Required for FINRA 3110 supervisory review |
| 3.5 | FINRA 2210 review process | -- | Included | -- | E5 Compliance (for Communication Compliance) | Uses Communication Compliance to flag Copilot-drafted content |
| 3.6 | Supervisory Review | -- | Included | -- | E5 Compliance (for Communication Compliance) | Uses Communication Compliance for supervision policies |
| 3.7 | UDAAP Compliance review | Included | Included | -- | -- | Process-based; Communication Compliance enhances detection |
| 3.8 | Model Risk Management | Included | Included | -- | -- | Primarily organizational process; no specific license for documentation |
| 3.9 | DSPM for AI (compliance monitoring) | -- | Included | Included | E5 Compliance | Ongoing monitoring dashboard for Copilot data risks |
| 3.10 | Privacy (Reg S-P) | Included | Included | -- | -- | Process-based with DLP/label enforcement; Priva add-on optional |
| 3.11 | Regulatory Record-keeping | -- | Included | -- | E5 Compliance | Requires Audit (Premium) and advanced retention for WORM-equivalent |
| 3.12 | Audit Evidence Packages | Included | Included | -- | -- | Process-based; Content Search available in E3 for evidence collection |
| 3.13 | FFIEC Alignment | Included | Included | -- | -- | Organizational mapping process; no specific license |

---

## Pillar 4: Operations and Monitoring

| Control | Feature | E3 | E5 | Copilot | Add-on Required (if E3) | Notes |
|---------|---------|----|----|---------|------------------------|-------|
| 4.1 | Feature Toggle Management | Included | Included | Included | -- | M365 Admin Center settings; requires Copilot license to be meaningful |
| 4.2 | Per-App Configuration | Included | Included | Included | -- | Per-app toggles in M365 Admin Center |
| 4.3 | Web Search Controls | Included | Included | Included | -- | Admin toggle in M365 Admin Center |
| 4.4 | Copilot Pages Governance | Included | Included | Included | -- | Admin settings for Copilot Pages |
| 4.5 | Plugin and Extensibility Governance | Included | Included | Included | -- | Integrated Apps settings in M365 Admin Center |
| 4.6 | Copilot Usage Analytics | Included | Included | Included | -- | Usage reports in M365 Admin Center; Viva Insights adds detail |
| 4.6 | Copilot Usage Analytics (advanced) | -- | -- | -- | Viva Insights | Advanced Copilot adoption analytics |
| 4.7 | Cost Management | Included | Included | Included | -- | License utilization tracking in M365 Admin Center |
| 4.8 | AI Incident Response | Included | Included | -- | -- | Process-based; Defender and Sentinel enhance automation |
| 4.9 | Business Continuity | Included | Included | -- | -- | Process-based planning |
| 4.10 | Change Management | Included | Included | -- | -- | Message Center monitoring; no additional license |
| 4.11 | Microsoft Sentinel Integration | -- | -- | -- | Microsoft Sentinel | Separate consumption-based (pay-per-GB) service |
| 4.12 | Governance Operating Calendar | Included | Included | -- | -- | Organizational process; no specific license |
| 4.13 | Stakeholder RACI Matrix | Included | Included | -- | -- | Organizational process; no specific license |

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
| Microsoft 365 Copilot | Copilot functionality per user |
| SharePoint Advanced Management | Oversharing assessment and site lifecycle management |

E5 is strongly recommended for FSI environments. The cost of individual add-ons to E3 typically exceeds the incremental cost of E5.

### Regulated Governance

| Required License | Purpose |
|-----------------|---------|
| Microsoft 365 E5 | Full compliance and security suite |
| Microsoft 365 Copilot | Copilot functionality per user |
| SharePoint Advanced Management | Oversharing reports, site lifecycle, access governance |
| Microsoft Sentinel | SIEM/SOAR for Copilot audit data |
| Viva Insights (optional) | Advanced Copilot adoption analytics |

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

*FSI Copilot Governance Framework v1.0 - February 2026*
