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

Pre-deployment data hygiene, oversharing remediation, permissions review, and licensing validation.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 1.1 | Oversharing Assessment and Remediation | B | | | Run SAM oversharing report; remediate broad-access sites |
| [ ] | 1.2 | SharePoint Permissions Review | B | | | Audit site-level and item-level permissions for excessive access |
| [ ] | 1.3 | Restricted SharePoint Search Configuration | B | | | Enable RSS to limit BizChat grounding during remediation |
| [ ] | 1.4 | OneDrive Sharing Defaults | B | | | Set default sharing to "Specific people" |
| [ ] | 1.5 | Microsoft 365 Groups Membership Audit | R | | | Review open-membership groups granting site access |
| [ ] | 1.6 | Guest and External Access Review | R | | | Audit B2B guest access to SharePoint and Teams |
| [ ] | 1.7 | Inactive Site and Content Lifecycle | R | | | Identify stale sites with sensitive content |
| [ ] | 1.8 | Semantic Index Readiness Validation | B | | | Confirm Semantic Index processing status |
| [ ] | 1.9 | License Assignment and Scoping | B | | | Assign Copilot licenses to approved user groups |
| [ ] | 1.10 | Vendor and Third-Party Risk Assessment | Reg | | | Complete AI vendor risk assessment for Copilot |
| [ ] | 1.11 | Data Classification Inventory | R | | | Catalog sensitive data locations before Copilot enablement |
| [ ] | 1.12 | Governance Committee Establishment | R | | | Form cross-functional Copilot governance committee |
| [ ] | 1.13 | User Communication and Training Plan | B | | | Develop user awareness materials for Copilot governance policies |

---

## Pillar 2: Security and Protection (15 Controls)

DLP, sensitivity labels, conditional access, information barriers, and Microsoft Defender integration.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 2.1 | Sensitivity Label Taxonomy for Copilot | B | | | Define/validate label hierarchy: Public, Internal, Confidential, Highly Confidential |
| [ ] | 2.2 | Auto-labeling Policies | R | | | Configure auto-labeling for common FSI sensitive info types |
| [ ] | 2.3 | Label Inheritance and Copilot Behavior | B | | | Validate Copilot inherits highest label from source content |
| [ ] | 2.4 | DLP Policies for Copilot Interactions | B | | | Add Microsoft 365 Copilot location to DLP policies |
| [ ] | 2.5 | Sensitive Information Type Definitions | R | | | Define custom SITs for FSI data (account numbers, SWIFT codes) |
| [ ] | 2.6 | DLP Policy Tips and User Notification | B | | | Configure user-facing policy tips for Copilot DLP blocks |
| [ ] | 2.7 | Conditional Access for Copilot | R | | | Require compliant device and MFA for Copilot access |
| [ ] | 2.8 | Information Barriers for Copilot | Reg | | | Configure IB segments for MNPI walls (broker-dealer) |
| [ ] | 2.9 | Endpoint DLP and Copilot on Devices | R | | | Extend DLP to endpoint for Copilot on desktop apps |
| [ ] | 2.10 | Microsoft Defender for Cloud Apps Integration | R | | | Configure session policies for Copilot web sessions |
| [ ] | 2.11 | Insider Risk Management for Copilot | Reg | | | Configure insider risk indicators for anomalous Copilot usage |
| [ ] | 2.12 | Data Security Posture Management for AI (DSPM for AI) | R | | | Enable DSPM for AI to monitor Copilot data exposure |
| [ ] | 2.13 | Encryption and Rights Management | B | | | Validate Copilot respects Azure Information Protection encryption |
| [ ] | 2.14 | Network and Endpoint Security for Copilot Traffic | R | | | Review network controls for Copilot API traffic |
| [ ] | 2.15 | Zero Trust Alignment for Copilot | Reg | | | Map Copilot governance to Zero Trust architecture principles |

---

## Pillar 3: Compliance and Audit (13 Controls)

Audit logging, retention, eDiscovery, FINRA/SEC record-keeping, supervisory review, and regulatory reporting.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 3.1 | Copilot Audit Logging | B | | | Enable Unified Audit Log; verify CopilotInteraction events |
| [ ] | 3.2 | Retention Policies for Copilot Data | B | | | Set retention to meet FINRA 4511 / SEC 17a-4 requirements |
| [ ] | 3.3 | eDiscovery for Copilot Interactions | R | | | Configure eDiscovery (Premium) to search Copilot content |
| [ ] | 3.4 | Communication Compliance for Copilot | Reg | | | Enable supervisory review of Copilot-assisted communications |
| [ ] | 3.5 | FINRA 2210 Compliance for Copilot-Drafted Content | Reg | | | Review process for Copilot-drafted retail communications |
| [ ] | 3.6 | Supervisory Review Procedures (FINRA 3110) | Reg | | | Integrate Copilot interactions into supervision workflows |
| [ ] | 3.7 | CFPB UDAAP Compliance for Copilot Outputs | Reg | | | Review process for Copilot outputs used in consumer-facing contexts |
| [ ] | 3.8 | Model Risk Management (OCC 2011-12 / SR 11-7) | Reg | | | Document Copilot in model inventory with risk assessment |
| [ ] | 3.9 | DSPM for AI Compliance Monitoring | R | | | Use DSPM for AI dashboard for ongoing compliance monitoring |
| [ ] | 3.10 | Privacy and Reg S-P Compliance | R | | | Validate Copilot handling of consumer financial information |
| [ ] | 3.11 | Regulatory Record-keeping (SEC 17a-3/4) | Reg | | | Map Copilot data to SEC record-keeping categories |
| [ ] | 3.12 | Audit Evidence Packages | R | | | Prepare pre-built evidence packages for regulatory examinations |
| [ ] | 3.13 | FFIEC IT Examination Alignment | Reg | | | Map Copilot governance to FFIEC IT Handbook domains |

---

## Pillar 4: Operations and Monitoring (13 Controls)

Feature management, per-app toggles, analytics, cost tracking, incident response, and business continuity.

| | # | Control | Level | Status | Owner | Notes |
|---|---|---------|-------|--------|-------|-------|
| [ ] | 4.1 | Copilot Feature Toggle Management | B | | | Configure global Copilot on/off and feature-level toggles |
| [ ] | 4.2 | Per-App Copilot Configuration | B | | | Enable/disable Copilot per M365 application |
| [ ] | 4.3 | Web Search and External Data Controls | B | | | Disable Bing web search in Copilot for regulated environments |
| [ ] | 4.4 | Copilot Pages Governance | R | | | Configure Copilot Pages creation, sharing, and retention |
| [ ] | 4.5 | Plugin and Extensibility Governance | R | | | Control third-party plugin and Graph connector availability |
| [ ] | 4.6 | Copilot Usage Analytics and Reporting | B | | | Enable Copilot usage reports in M365 Admin Center |
| [ ] | 4.7 | Copilot Cost Management and License Optimization | R | | | Track Copilot license utilization and ROI |
| [ ] | 4.8 | AI Incident Response Procedures | R | | | Define incident response for AI-specific scenarios |
| [ ] | 4.9 | Business Continuity for Copilot Services | R | | | Plan for Copilot service disruption scenarios |
| [ ] | 4.10 | Change Management for Copilot Updates | R | | | Track Microsoft Copilot feature changes via Message Center |
| [ ] | 4.11 | Microsoft Sentinel Integration for Copilot | Reg | | | Stream Copilot audit data to Sentinel for SIEM/SOAR |
| [ ] | 4.12 | Governance Operating Calendar | R | | | Define recurring governance review cadence |
| [ ] | 4.13 | Stakeholder RACI Matrix | R | | | Document roles and responsibilities for Copilot governance |

---

## Summary by Governance Level

| Level | Pillar 1 | Pillar 2 | Pillar 3 | Pillar 4 | Total |
|-------|----------|----------|----------|----------|-------|
| **Baseline (B)** | 6 | 4 | 2 | 4 | **16** |
| **Recommended (R)** | 4 | 6 | 4 | 6 | **20** |
| **Regulated (Reg)** | 1 | 3 | 6 | 1 | **11** |
| **All controls that contribute to each pillar** | 2 | 2 | 1 | 2 | **7** |
| **Pillar Total** | **13** | **15** | **13** | **13** | **54** |

!!! tip "Implementation Priority"
    - **Phase 1 (Pre-deployment):** All Baseline controls (16 controls)
    - **Phase 2 (Early production):** All Recommended controls (20 controls)
    - **Phase 3 (Maturity):** All Regulated controls (11 controls) plus remaining items
    - Controls marked as both B and R in different sub-areas should be started at Baseline and matured to Recommended.

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
