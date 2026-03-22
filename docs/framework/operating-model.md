# Operating Model

Roles, responsibilities, governance structure, and operational cadence for M365 Copilot oversight.

---

## Overview

This document defines the organizational structure, committee charter, roles, and accountability for M365 Copilot governance. It establishes who is Responsible, Accountable, Consulted, and Informed (RACI) for governance activities and defines the decision-making and escalation framework.

---

## RACI Definitions

- **R (Responsible):** Does the work
- **A (Accountable):** Final approval authority (one per activity)
- **C (Consulted):** Provides input and expertise before decisions
- **I (Informed):** Kept updated on status after decisions

!!! note "Note for Smaller Institutions"
    Roles may be combined based on organizational size and structure. For example, the M365 Admin may also serve as the Purview Admin, or the Compliance Officer may double as the AI Governance Lead. The RACI assignments remain the same; the individual simply holds multiple roles. Maintain adequate segregation of duties for critical controls.

---

## Copilot Governance Committee

### Purpose

The Copilot Governance Committee provides strategic oversight for M365 Copilot deployment, monitors governance effectiveness, and makes policy decisions affecting Copilot configuration and scope.

### Charter

**Mission:** Govern the deployment, operation, and ongoing risk management of Microsoft 365 Copilot to support compliance with applicable regulations while enabling organizational productivity.

**Scope:**

- Copilot deployment decisions (expansion, restriction, feature enablement)
- Governance policy decisions (web search, plugins, Copilot Pages, declarative agents)
- Incident review and remediation approval
- Regulatory alignment validation
- Governance effectiveness monitoring

**Authority:**

- Approve or restrict Copilot features and scope
- Direct remediation activities for identified governance gaps
- Escalate material issues to executive leadership or the board
- Commission special reviews or assessments

### Composition

| Role | Committee Function | Required/Optional |
|------|-------------------|-------------------|
| **AI Governance Lead / Copilot Program Manager** | Chair; agenda setting, meeting facilitation | Required |
| **Chief Compliance Officer / Compliance Officer** | Regulatory alignment, examination readiness | Required |
| **CISO / Security Lead** | Security controls, incident response | Required |
| **M365 / SharePoint Admin** | Technical implementation status, platform updates | Required |
| **Legal / General Counsel** | Legal risk assessment, regulatory interpretation | Required (Regulated) |
| **Business Unit Representative** | User experience, business requirements | Recommended |
| **Internal Audit** | Independent oversight (observer) | Recommended |
| **HR / Training Lead** | Training compliance, user adoption | Optional |

### Meeting Cadence

| Meeting | Frequency | Duration | Focus | Attendees |
|---------|-----------|----------|-------|-----------|
| **Governance Committee** | Monthly | 60 minutes | Operational governance, policy decisions, incident review | Full committee |
| **Quarterly Compliance Review** | Quarterly | 90 minutes | Regulatory alignment, control effectiveness, metrics review | Committee + executive sponsor |
| **Annual Board Review** | Annual | 30-45 minutes | Strategic governance posture, annual risk assessment, investment needs | Committee + board/executive leadership |
| **Incident Review** | As needed | 30 minutes | Material incidents requiring committee attention | Chair + relevant members |

### Standing Agenda (Monthly Governance Committee)

1. **Approval of prior meeting minutes** (5 min)
2. **Copilot governance dashboard review** -- metrics, control status, open items (10 min)
3. **Incident report** -- any Copilot-related incidents since last meeting (10 min)
4. **Microsoft platform updates** -- Copilot feature changes, new capabilities, deprecations (10 min)
5. **Policy decisions** -- pending feature approvals, scope changes, configuration decisions (15 min)
6. **Regulatory update** -- any regulatory changes affecting Copilot governance (5 min)
7. **Action items and next meeting planning** (5 min)

---

## RACI Matrices

### Copilot Deployment Governance

| Activity | AI Gov Lead | Compliance | CISO | M365 Admin | Legal | Board |
|----------|-------------|------------|------|------------|-------|-------|
| Copilot deployment decision | R | **A** | C | C | C | I |
| Oversharing assessment | R | C | C | **A** | I | I |
| Permission remediation | C | I | C | **A** | I | I |
| Pilot group selection | **A** | C | C | R | I | I |
| Feature toggle configuration | C | C | C | **A** | I | I |
| Web search policy | R | **A** | C | C | C | I |
| Plugin/connector approval | R | C | **A** | C | C | I |
| Copilot expansion decision | R | **A** | C | C | C | I |
| User training program | R | C | I | I | I | I |

### Security and Data Protection

| Activity | AI Gov Lead | Compliance | CISO | Purview Admin | Entra Admin | Legal |
|----------|-------------|------------|------|---------------|-------------|-------|
| DLP policy design | C | C | **A** | R | I | I |
| DLP policy implementation | I | I | C | **A** | I | I |
| Sensitivity label taxonomy | C | **A** | C | R | I | C |
| Auto-labeling policies | C | C | **A** | R | I | I |
| Conditional access policies | I | I | **A** | I | R | I |
| Information barriers | C | **A** | C | R | C | C |
| Insider risk configuration | C | **A** | C | R | I | I |

### Compliance and Audit

| Activity | AI Gov Lead | Compliance | CISO | Purview Admin | Legal | Internal Audit |
|----------|-------------|------------|------|---------------|-------|----------------|
| Audit log retention | C | **A** | C | R | I | C |
| Communication compliance | I | **A** | I | R | C | I |
| eDiscovery configuration | I | C | I | R | **A** | I |
| Supervisory review program | C | **A** | I | R | C | I |
| Regulatory reporting | C | **A** | C | I | C | C |
| FINRA 2210 compliance | C | **A** | I | R | C | I |
| Examination preparation | R | **A** | C | C | C | C |
| Annual control testing | C | C | C | I | I | **A** |

### Operations and Monitoring

| Activity | AI Gov Lead | Compliance | CISO | M365 Admin | Teams Admin | SharePoint Admin |
|----------|-------------|------------|------|------------|-------------|------------------|
| Copilot feature management | **A** | C | C | R | R | I |
| Per-app Copilot toggles | **A** | C | C | R | R | I |
| Usage analytics monitoring | R | I | I | **A** | I | I |
| Cost tracking | **A** | I | I | R | I | I |
| Incident response | R | C | **A** | R | C | C |
| Copilot Pages governance | **A** | C | C | R | I | C |
| Declarative agent governance | **A** | C | C | R | I | R |
| Teams Copilot settings | **A** | C | C | I | R | I |
| Sentinel integration | C | C | **A** | C | I | I |
| Change management | **A** | C | C | R | R | R |

---

## Core Governance Roles

### 1. AI Governance Lead / Copilot Program Manager

**Accountability:** Copilot governance framework and deployment program

**Responsibilities:**

- Governance committee chair
- Framework administration and updates
- Copilot deployment strategy and scope decisions
- Feature toggle policy recommendations
- Governance dashboard and reporting
- Coordination across security, compliance, and operations teams
- Vendor relationship management (Microsoft Copilot program)
- User adoption and change management oversight

**Reports to:** CIO, CTO, or CISO (varies by organization)

---

### 2. Chief Compliance Officer / Compliance Officer

**Accountability:** Regulatory alignment and compliance effectiveness

**Responsibilities:**

- Regulatory mapping and interpretation for Copilot
- Communication compliance program oversight
- Supervisory review procedures (FINRA 3110, 2210)
- Examination preparation and response coordination
- Compliance monitoring and reporting
- Policy violation investigation
- Training requirements definition

---

### 3. Chief Information Security Officer (CISO)

**Accountability:** Information security program, including Copilot security controls

**Responsibilities:**

- DLP policy strategy and approval
- Conditional access and identity governance
- Incident response for Copilot-related security events
- Insider risk management
- Security monitoring (Sentinel, Defender)
- Plugin and connector security assessment
- Board-level security reporting

---

### 4. M365 / Purview Administrator

**Accountability:** Technical implementation and operation of Copilot governance controls

**Responsibilities:**

- Copilot feature toggle configuration
- DLP policy implementation and tuning
- Sensitivity label deployment
- Audit log configuration and retention
- Communication compliance policy setup
- eDiscovery configuration
- Purview dashboard monitoring
- Platform update assessment and testing

---

### 5. SharePoint Administrator

**Accountability:** SharePoint governance for Copilot data access

**Responsibilities:**

- Oversharing assessment and remediation
- Site permissions and access governance
- Restricted SharePoint Search configuration
- External sharing controls
- Declarative agent site governance
- Access review coordination for SharePoint
- Site lifecycle management

---

### 6. Entra / Identity Administrator

**Accountability:** Identity and access security for Copilot users

**Responsibilities:**

- Conditional access policy implementation
- Access review campaigns
- User provisioning and Copilot license assignment
- MFA enforcement
- Privileged access management
- Identity governance reporting

---

### 7. Teams Administrator

**Accountability:** Teams-specific Copilot controls

**Responsibilities:**

- Meeting transcription policies
- Teams Copilot feature management
- Meeting policy configuration
- Teams communication compliance
- Teams channel governance

---

### 8. Legal / General Counsel

**Accountability:** Legal risk and regulatory obligations

**Responsibilities:**

- Regulatory interpretation for Copilot use cases
- eDiscovery legal hold management
- Privacy impact assessment
- Customer disclosure requirements
- Vendor agreement review (Microsoft DPA)
- Fair lending compliance oversight (if applicable)
- Examination response legal review

---

### 9. Internal Audit

**Accountability:** Independent control testing and assessment

**Responsibilities:**

- Annual control effectiveness testing
- Governance procedure testing (FINRA 3120 alignment)
- Compliance monitoring validation
- SOX 404 assessment (if applicable)
- Audit reporting to board/audit committee
- Finding follow-up and remediation tracking

---

## Escalation Procedures

### Escalation Levels

```
+------------------------------------------------------------------+
|                    ESCALATION FRAMEWORK                            |
|                                                                    |
|  LEVEL 1 (Operational)         LEVEL 2 (Management)               |
|  +------------------------+   +------------------------+          |
|  | M365 Admin / Purview   |   | AI Governance Lead     |          |
|  | Admin                  |   | + Compliance Officer   |          |
|  |                        |   | + CISO                 |          |
|  | - Policy violations    |-->| - Repeated violations  |          |
|  | - Configuration issues |   | - Potential regulatory  |          |
|  | - User reports         |   |   exposure              |          |
|  | - Minor incidents      |   | - Security incidents    |          |
|  +------------------------+   +----------+-------------+          |
|                                          |                         |
|                                          v                         |
|  LEVEL 3 (Executive)          LEVEL 4 (Board)                     |
|  +------------------------+   +------------------------+          |
|  | CIO/CTO + CCO + CISO   |   | Board / Audit          |          |
|  | + General Counsel       |   | Committee              |          |
|  |                        |   |                        |          |
|  | - Material incidents   |-->| - Regulatory violations |          |
|  | - Regulatory inquiries |   | - Material breaches     |          |
|  | - Significant exposure |   | - Examination findings  |          |
|  | - Legal matters        |   | - Strategic decisions   |          |
|  +------------------------+   +------------------------+          |
|                                                                    |
+------------------------------------------------------------------+
```

### Escalation Triggers

| Level | Trigger | Response Time | Examples |
|-------|---------|---------------|---------|
| **Level 1** | Operational issue, policy violation | < 24 hours | DLP alert, user complaint, configuration drift |
| **Level 2** | Management attention required | < 8 hours | Repeated violations, potential data exposure, security alert |
| **Level 3** | Executive attention required | < 4 hours | Regulatory inquiry, material incident, significant compliance gap |
| **Level 4** | Board notification required | < 24 hours | Regulatory violation, customer data breach, examination finding |

### Escalation Procedures by Type

**Data Exposure Incident:**

1. M365 Admin contains the exposure (disable Copilot for affected user/scope if needed)
2. CISO assesses scope and impact
3. Compliance Officer evaluates regulatory reporting obligations
4. Legal assesses notification requirements
5. AI Governance Lead coordinates remediation
6. Governance committee reviews at next meeting (or special session if material)

**Regulatory Inquiry:**

1. Compliance Officer receives and logs the inquiry
2. AI Governance Lead provides technical documentation
3. Legal reviews all responses before submission
4. CISO provides security-related evidence
5. Governance committee briefed within 24 hours
6. Board notified if examination or enforcement action

---

## Decision Authority Matrix

| Decision | Authority | Consultation Required | Board Notification |
|----------|-----------|----------------------|-------------------|
| Enable Copilot for new department | AI Governance Lead | Compliance, CISO | No |
| Disable Copilot feature (web search, plugin) | AI Governance Lead | Compliance | No |
| Approve new plugin or connector | CISO | Compliance, Legal | No |
| Change DLP policy | CISO | Compliance | No |
| Change retention policy | Compliance Officer | Legal | No |
| Disable Copilot tenant-wide (emergency) | CISO | AI Governance Lead | Yes (post-action) |
| Expand Copilot beyond pilot | Governance Committee | All members | Yes |
| Respond to regulatory examination | Compliance Officer | Legal, AI Governance Lead | Yes |
| Approve Copilot for customer-facing use | Governance Committee | Legal, CISO | Yes |
| Change supervisory review procedures | Compliance Officer | Legal | No |

---

## Integration with Existing IT Governance

M365 Copilot governance should integrate with, not replace, existing IT governance structures:

### IT Governance Alignment

| Existing Structure | Copilot Integration Point |
|-------------------|--------------------------|
| **IT Risk Committee** | Copilot risk assessment results reported quarterly |
| **Change Advisory Board (CAB)** | Copilot configuration changes follow existing change management |
| **Information Security Committee** | Copilot security controls reviewed as part of security program |
| **Data Governance Committee** | Oversharing remediation, data classification for Copilot |
| **Vendor Management Program** | Microsoft Copilot included in vendor risk assessments |
| **Incident Response Team** | Copilot-related incidents follow existing IR procedures |
| **Internal Audit Program** | Copilot controls included in annual audit plan |
| **Records Management Program** | Copilot interaction retention aligned with records schedule |

### Governance Integration Approach

1. **Do not create a standalone Copilot governance silo** -- integrate into existing structures
2. **The Copilot Governance Committee is a working group**, not a replacement for existing committees
3. **Copilot controls map to existing control frameworks** (NIST CSF, ISO 27001, COBIT)
4. **Reporting flows through existing channels** -- the Copilot Governance Committee provides input to existing risk and compliance reporting

---

## Training Requirements

| Role | Training Topic | Frequency | Delivery |
|------|----------------|-----------|----------|
| **All Copilot users** | Copilot usage guidelines, FSI-specific restrictions, data handling | Annual + at Copilot enablement | LMS / in-person |
| **Supervisors/Managers** | Supervisory obligations for Copilot-assisted work | Annual | LMS / in-person |
| **M365 Admins** | Copilot governance controls, Purview configuration, audit procedures | Annual + as-needed | Technical training |
| **Compliance team** | Copilot regulatory alignment, communication compliance, examination readiness | Annual + as-needed | Specialized training |
| **Governance committee** | Framework updates, regulatory changes, governance effectiveness | Annual (at annual review) | Committee session |
| **Board/Executive** | Copilot governance overview, key metrics, risk posture | Annual (at board review) | Briefing |

---

## Governance Artifacts

### Required Documentation

| Artifact | Owner | Review Frequency | Retention |
|----------|-------|------------------|-----------|
| Copilot Governance Policy | AI Governance Lead | Annual | Current + 7 years |
| Written Supervisory Procedures (Copilot) | Compliance Officer | Annual | Current + 7 years |
| Copilot Deployment Documentation | M365 Admin | Continuous | Current + 3 years |
| DLP Policy Documentation | CISO | Quarterly | Current + 3 years |
| Governance Committee Minutes | AI Governance Lead | Per meeting | 7 years |
| Quarterly Compliance Reports | Compliance Officer | Quarterly | 7 years |
| Annual Governance Assessment | AI Governance Lead | Annual | 7 years |
| Incident Reports (Copilot-related) | CISO | Per incident | 7 years |
| Training Completion Records | HR | Continuous | 7 years |

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
