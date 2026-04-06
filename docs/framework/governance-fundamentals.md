# Governance Fundamentals

Core concepts and principles for Microsoft 365 Copilot governance in financial services.

---

## Framework Overview

The FSI Copilot Governance Framework provides complete guidance for governing Microsoft 365 Copilot across all M365 applications in regulated US financial services environments.

**Version:** 1.2.1 (March 2026)
**Target Audience:** US Financial Services Organizations
**Regulatory Focus:** FINRA, SEC, SOX, GLBA, OCC, Federal Reserve, FDIC, NCUA, CFPB

!!! warning
    This framework is provided for informational purposes only and does not constitute legal,
    regulatory, or compliance advice. See [Disclaimer](../disclaimer.md) for full details.

---

## Scope and Assumptions

### What This Framework Covers

This framework provides governance guidance for:

- **Microsoft 365 Copilot** -- the AI assistant embedded across M365 applications
- **Microsoft 365 Copilot Chat** -- the cross-application Copilot experience
- **Copilot Pages** -- AI-generated collaborative content surfaces
- **Copilot in Teams** -- meeting transcription, recap, and chat assistance
- **Copilot extensibility** -- plugins, Graph connectors, declarative agents from SharePoint

### What This Framework Does NOT Cover

- **Copilot Studio** and custom AI agents -- see [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov)
- **Agent Builder** and enterprise agents -- see [FSI-AgentGov](https://github.com/judeper/FSI-AgentGov)
- **Non-US regulations** (EU AI Act, GDPR, DORA, MiFID II are out of scope)
- **Non-Microsoft AI platforms** (OpenAI direct, Google Gemini, etc.)
- Custom ML model development, training, or validation
- State privacy laws (CCPA/CPRA require separate analysis, though key intersections are noted)

See [Relationship to AgentGov](relationship-to-agentgov.md) for detailed scope boundaries.

### Key Assumptions

| Assumption | Rationale |
|------------|-----------|
| **Microsoft 365 E3/E5** | Required for Copilot licensing, Purview, Defender capabilities |
| **Microsoft 365 Copilot licenses** | Per-user licensing required for Copilot access |
| **Microsoft Entra ID** | Identity and access management foundation |
| **Microsoft Purview** | Compliance and data governance capabilities |
| **Foundational IT controls** | Network security, endpoint protection, backup/recovery assumed in place |

---

## Discovery Amplification

**Discovery amplification** is the central governance challenge for M365 Copilot in financial services.

### The Concept

Microsoft 365 Copilot does not bypass security permissions. It operates strictly within the user's existing access rights -- the "no elevated access" principle. However, Copilot fundamentally changes the *practical impact* of those access rights.

**Before Copilot:** A user with broad SharePoint permissions might never find a sensitive document buried in an old team site. The document was technically accessible but practically obscure.

**With Copilot:** That same user asks "What were the terms of the ABC Corp deal?" and Copilot instantly surfaces the document, quotes from it, and synthesizes it into a response. The content was always accessible; Copilot simply made discovery instantaneous.

### Why This Matters for FSI

```
+------------------------------------------------------------------+
|                    DISCOVERY AMPLIFICATION                         |
|                                                                    |
|   BEFORE COPILOT                    WITH COPILOT                  |
|   +-----------+                     +-----------+                 |
|   |           |                     |           |                 |
|   | Technical | <-- gap -->  Actual | Technical | == Actual       |
|   |  Access   |             Access  |  Access   |    Access       |
|   |           |                     |           |                 |
|   +-----------+                     +-----------+                 |
|                                                                    |
|   Users had access to far more      Copilot closes the gap        |
|   than they routinely discovered    between technical and          |
|   or consumed.                      practical access.              |
|                                                                    |
|   GOVERNANCE IMPLICATION: Fix permissions BEFORE enabling Copilot. |
+------------------------------------------------------------------+
```

In financial services, the gap between *technical access* and *intended access* frequently contains:

- **Deal documents** accessible to broader groups than the deal team
- **Compensation data** in SharePoint sites with inherited permissions
- **Client PII** in shared mailboxes or team sites with overly broad access
- **Board materials** in sites where former members retain access
- **Regulatory correspondence** accessible outside the compliance team

Copilot closes this gap instantly. Governance must address the permissions gap *before* enabling Copilot, not after.

### Governance Response

| Action | Control | Timing |
|--------|---------|--------|
| Oversharing assessment | 1.1 | Pre-deployment (required) |
| Permission remediation | 1.2, 1.3 | Pre-deployment |
| Sensitivity label deployment | 2.2, 2.3 | Pre-deployment |
| Restricted SharePoint Search | 1.4 | Pre-deployment (Regulated) |
| Ongoing access reviews | 1.6 | Post-deployment (continuous) |

---

## Three Governance Levels

### Overview

Each of the 56 controls in this framework provides implementation guidance at three governance levels. Organizations select their target level based on regulatory obligations, risk appetite, and institutional type.

| Level | Description | Typical Use | Control Coverage |
|-------|-------------|-------------|------------------|
| **Baseline** | Minimum viable governance | Initial Copilot deployment in low-risk environments | ~30 core controls |
| **Recommended** | Best-practice governance | Most production environments, standard FSI firms | ~45 controls |
| **Regulated** | Examination-ready, comprehensive governance | FINRA/SEC-regulated broker-dealers, banks with OCC oversight | All 56 controls |

### Baseline

**Target audience:** Organizations deploying M365 Copilot for the first time, or those in low-risk / non-customer-facing environments.

**Characteristics:**

- Core data hygiene controls (oversharing assessment, basic permissions review)
- Default M365 audit logging enabled
- Basic DLP policies for sensitive data types
- Standard M365 retention policies
- Copilot feature toggles configured per organizational policy
- User awareness training

**When Baseline applies:**

- Internal-only Copilot use with no customer-facing outputs
- Non-regulated business units within a regulated firm
- Pilot deployments during assessment phase
- Organizations not subject to FINRA, SEC, or banking regulators for AI use

**Limitations:** Baseline alone is unlikely to satisfy examination expectations for regulated firms. Organizations should plan to advance to Recommended or Regulated levels before production-scale deployment.

### Recommended

**Target audience:** Most production environments in financial services organizations.

**Characteristics:**

- Full oversharing remediation program
- Comprehensive sensitivity labeling with auto-labeling policies
- Extended audit logging with tailored retention periods
- Communication compliance monitoring
- DLP policies covering all sensitive information types
- Conditional access policies for Copilot access
- Regular access reviews and governance reporting
- Supervisory sampling for Copilot-assisted communications

**When Recommended applies:**

- Standard production deployments across the organization
- Environments where employees use Copilot for internal communications
- Organizations implementing Copilot with general customer data access
- Firms seeking strong governance without full examination-ready posture

### Regulated

**Target audience:** FINRA/SEC-registered broker-dealers, OCC/Fed-supervised banks, organizations expecting regulatory examination of their Copilot governance.

**Characteristics:**

- Comprehensive FINRA Rule 2210 communication compliance for Copilot-drafted content
- Full supervisory review program under FINRA Rule 3110
- WORM-compliant retention for applicable record types
- eDiscovery readiness for Copilot interactions
- Information barriers between business units
- Web search controls or restrictions
- Restricted SharePoint Search for high-sensitivity sites
- Model risk management documentation (where applicable under OCC 2011-12)
- Sentinel integration for advanced monitoring
- Documented examination response procedures

**When Regulated applies:**

- FINRA-registered broker-dealers using Copilot in customer-facing contexts
- SEC-registered investment advisers with Copilot access to client information
- OCC/Fed-supervised banks deploying Copilot broadly
- Any institution expecting regulatory examination of AI governance

---

## Shared Responsibility Model

M365 Copilot governance operates under a shared responsibility model between Microsoft and the deploying organization.

### Microsoft Responsibilities

| Area | Microsoft Provides |
|------|-------------------|
| **Platform security** | Azure infrastructure security, data center physical security, network isolation |
| **AI safety** | Responsible AI filters, content safety systems, prompt injection mitigations |
| **Data residency** | Data processing within specified geographic boundaries per service agreements |
| **No training on tenant data** | Microsoft does not use customer tenant data to train foundation models |
| **Permission enforcement** | Copilot respects Microsoft Graph permissions (no elevated access) |
| **Audit event generation** | Copilot activities generate audit events in the Unified Audit Log |
| **Encryption** | Data encrypted in transit and at rest |
| **Compliance certifications** | SOC 2, ISO 27001, FedRAMP (for applicable services) |

### Organization Responsibilities

| Area | Organization Must Provide |
|------|--------------------------|
| **Permission governance** | Correct SharePoint/OneDrive/Exchange permissions (Copilot does not fix oversharing) |
| **Sensitivity labeling** | Label deployment, auto-labeling policies, label-based DLP |
| **Audit configuration** | Retention policies, audit log access, search and export procedures |
| **Supervisory programs** | Communication compliance, supervisory review, FINRA 2210 compliance |
| **Access governance** | Regular access reviews, stale permission cleanup, access certification |
| **Feature management** | Per-app Copilot toggles, web search settings, plugin governance |
| **User training** | Copilot usage guidelines, FSI-specific prohibited uses, disclosure requirements |
| **Incident response** | Detection, investigation, and remediation of Copilot-related incidents |
| **Examination readiness** | Evidence compilation, examiner response procedures, artifact retention |

### The Boundary

```
+------------------------------------------------------------------+
|                    SHARED RESPONSIBILITY MODEL                     |
|                                                                    |
|  MICROSOFT                          ORGANIZATION                  |
|  +-----------------------------+   +-----------------------------+|
|  | Platform & AI safety        |   | Permission governance       ||
|  | Permission enforcement      |   | Sensitivity labeling        ||
|  | Audit event generation      |   | Audit retention & search    ||
|  | Encryption (transit & rest) |   | Supervisory programs        ||
|  | No training on tenant data  |   | Access reviews              ||
|  | Responsible AI filters      |   | Feature management          ||
|  | Data residency controls     |   | User training               ||
|  | Compliance certifications   |   | Incident response           ||
|  +-----------------------------+   +-----------------------------+|
|                                                                    |
|  KEY PRINCIPLE: Copilot inherits your permission problems.         |
|  Microsoft provides the guardrails; you provide the governance.    |
+------------------------------------------------------------------+
```

---

## Control Classification Methodology

### Classification Dimensions

Each control in this framework is classified along four dimensions:

**1. Pillar** -- Which lifecycle phase the control addresses:

| Pillar | Phase | Focus |
|--------|-------|-------|
| 1 | Readiness & Assessment | Pre-deployment preparation |
| 2 | Security & Protection | Runtime data and access protection |
| 3 | Compliance & Audit | Regulatory recordkeeping and supervision |
| 4 | Operations & Monitoring | Ongoing management and incident response |

**2. Governance Level** -- Minimum level at which the control is required:

| Level | Notation |
|-------|----------|
| Baseline | Required for all deployments |
| Recommended | Required for production environments |
| Regulated | Required for examination-ready environments |

**3. Regulatory Mapping** -- Which regulations the control supports:

Controls are mapped to specific regulatory requirements (e.g., FINRA 4511, SEC 17a-4). A single control may support multiple regulations. See [Regulatory Framework](regulatory-framework.md) for complete mappings.

**4. Admin Portal** -- Where the control is configured:

| Portal | Shorthand |
|--------|-----------|
| Microsoft Purview portal | Purview |
| Microsoft Entra admin center | Entra |
| Microsoft 365 admin center | M365 Admin |
| SharePoint admin center | SharePoint Admin |
| Microsoft Teams admin center | Teams Admin |
| Microsoft Defender portal | Defender |

---

## Mapping Your Organization to a Governance Level

### Assessment Process

1. **Identify your regulatory profile** -- Which regulators oversee your institution?
2. **Assess Copilot use cases** -- Will Copilot users access client data? Draft customer communications?
3. **Evaluate your permission posture** -- Has oversharing been assessed and remediated?
4. **Determine examination exposure** -- Are you likely to face regulatory examination of AI governance?

### Decision Matrix

| Factor | Baseline | Recommended | Regulated |
|--------|----------|-------------|-----------|
| **Regulator** | No primary financial regulator | General FSI firm | FINRA, SEC, OCC, Fed direct oversight |
| **Copilot use** | Internal productivity only | Internal + some customer data access | Customer-facing communications, financial data |
| **Data sensitivity** | Low-sensitivity internal content | Mixed sensitivity, some PII | High-sensitivity financial, client PII, deal data |
| **Examination likelihood** | Low | Moderate | High |
| **Institution type** | Fintech (pre-regulation), internal support | Mid-size FSI, investment firms | Broker-dealers, national banks, large RIAs |

### Governance Level by Institution Type

| Institution Type | Recommended Minimum Level |
|------------------|--------------------------|
| FINRA-registered broker-dealer | Regulated |
| SEC-registered investment adviser (large) | Regulated |
| SEC-registered investment adviser (small) | Recommended |
| National bank (OCC-supervised) | Regulated |
| State-chartered bank (Fed/FDIC) | Recommended to Regulated |
| Credit union (NCUA) | Recommended |
| Insurance company (state-regulated) | Recommended |
| Fintech (pre-regulation) | Baseline to Recommended |

---

## Control Applicability by Governance Level

### Pillar 1: Readiness & Assessment (15 controls)

| Control | Name | Baseline | Recommended | Regulated |
|---------|------|----------|-------------|-----------|
| 1.1 | Oversharing Assessment | Required | Required | Required |
| 1.2 | SharePoint Permissions Remediation | Required | Required | Required |
| 1.3 | Least-Privilege Access Review | -- | Required | Required |
| 1.4 | Restricted SharePoint Search | -- | -- | Required |
| 1.5 | Teams and Meeting Governance | Required | Required | Required |
| 1.6 | Access Certification Campaigns | -- | Required | Required |
| 1.7 | Data Classification Assessment | Required | Required | Required |
| 1.8 | Licensing and Assignment Governance | Required | Required | Required |
| 1.9 | Copilot Readiness Assessment | Required | Required | Required |
| 1.10 | Vendor Risk Assessment for Copilot | -- | Required | Required |
| 1.11 | External Sharing Audit | Required | Required | Required |
| 1.12 | OneDrive Governance | -- | Required | Required |
| 1.13 | Exchange/Mailbox Permissions Review | -- | Required | Required |
| 1.14 | Item-Level Permission Scanning | Required | Required | Required |
| 1.15 | SharePoint Permissions Drift Detection | Required | Required | Required |

### Pillar 2: Security & Protection (15 controls)

| Control | Name | Baseline | Recommended | Regulated |
|---------|------|----------|-------------|-----------|
| 2.1 | DLP Policy Configuration | Required | Required | Required |
| 2.2 | Sensitivity Label Deployment | Required | Required | Required |
| 2.3 | Conditional Access Policies | -- | Required | Required |
| 2.4 | Information Barriers (Chinese Wall) | -- | -- | Required |
| 2.5 | Data Minimization and Grounding Scope | -- | Required | Required |
| 2.6 | Web Search and Grounding Controls | Required | Required | Required |
| 2.7 | Data Residency and Cross-Border Data Flow | -- | Required | Required |
| 2.8 | Encryption (Transit and At Rest) | Required | Required | Required |
| 2.9 | Defender for Cloud Apps | -- | Required | Required |
| 2.10 | Insider Risk Detection | -- | -- | Required |
| 2.11 | Copilot Pages Security | Required | Required | Required |
| 2.12 | External Sharing and Guest Access Governance | -- | Required | Required |
| 2.13 | Plugin and Connector Security | -- | Required | Required |
| 2.14 | Declarative and SharePoint Agents Governance | -- | Required | Required |
| 2.15 | Network Security and Private Connectivity | Required | Required | Required |

### Pillar 3: Compliance & Audit (13 controls)

| Control | Name | Baseline | Recommended | Regulated |
|---------|------|----------|-------------|-----------|
| 3.1 | Copilot Audit Logging | Required | Required | Required |
| 3.2 | Retention Policies for Copilot | Required | Required | Required |
| 3.3 | eDiscovery for Copilot Content | -- | Required | Required |
| 3.4 | Communication Compliance Monitoring | -- | Required | Required |
| 3.5 | FINRA 2210 Communication Review | -- | -- | Required |
| 3.6 | Supervisory Review (FINRA 3110) | -- | Required | Required |
| 3.7 | CFPB UDAAP Monitoring | -- | -- | Required |
| 3.8 | Model Risk Documentation (OCC/SR 11-7) | -- | -- | Required |
| 3.9 | Regulatory Reporting | -- | Required | Required |
| 3.10 | Privacy Controls (Reg S-P) | Required | Required | Required |
| 3.11 | Recordkeeping (SEC 17a-3/4) | -- | Required | Required |
| 3.12 | SOX Internal Controls Integration | -- | -- | Required |
| 3.13 | FFIEC Examination Alignment | -- | -- | Required |

### Pillar 4: Operations & Monitoring (13 controls)

| Control | Name | Baseline | Recommended | Regulated |
|---------|------|----------|-------------|-----------|
| 4.1 | Copilot Feature Toggle Management | Required | Required | Required |
| 4.2 | Per-App Copilot Controls | Required | Required | Required |
| 4.3 | Copilot Usage Analytics | Required | Required | Required |
| 4.4 | Cost Tracking and Optimization | Required | Required | Required |
| 4.5 | Incident Response for Copilot | Required | Required | Required |
| 4.6 | Teams-Specific Copilot Controls | Required | Required | Required |
| 4.7 | Copilot Feedback and Quality Monitoring | -- | Required | Required |
| 4.8 | Copilot Pages Governance | -- | Required | Required |
| 4.9 | Business Continuity and DR | -- | Required | Required |
| 4.10 | Declarative Agent Governance | -- | Required | Required |
| 4.11 | Sentinel Integration for Copilot | -- | -- | Required |
| 4.12 | Change Management for Copilot Updates | Required | Required | Required |
| 4.13 | Governance Training and Awareness | Required | Required | Required |

---

## Integration with Existing Governance

This framework is designed to **complement, not replace** existing enterprise governance programs:

- Integrate controls with your existing IT risk management framework
- Align with enterprise information security policies
- Coordinate with records retention and eDiscovery requirements
- Map to your organization's internal audit program
- Extend existing supervisory procedures to cover Copilot-assisted activities

!!! note
    Organizations should validate all controls against their specific regulatory obligations and
    existing policy frameworks.

---

## Getting Started

### For Executives

1. Read [Executive Summary](executive-summary.md) (10 minutes)
2. Review the governance levels above to identify your target level (5 minutes)
3. Understand [Operating Model](operating-model.md) for accountability (10 minutes)

### For Compliance Officers

1. Review [Regulatory Framework](regulatory-framework.md) for applicable regulations
2. Map your institution to a governance level using the decision matrix above
3. Reference the control applicability tables to identify required controls

### For Implementation Teams

1. Follow the [Adoption Roadmap](adoption-roadmap.md) for phased approach
2. Reference the [Control Catalog](../controls/index.md) for control details
3. Follow [Playbooks](../playbooks/index.md) for step-by-step procedures

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
