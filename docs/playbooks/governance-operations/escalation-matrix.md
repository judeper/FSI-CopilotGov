# Escalation Matrix

Escalation procedures by severity level for M365 Copilot governance events in financial services environments.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## Severity Level Definitions

| Level | Name | Definition | Resolution Target |
|-------|------|-----------|-------------------|
| **Level 4** | Critical | Regulatory impact -- active data exposure of regulated content, breach of information barriers, or confirmed regulatory violation | 4 hours |
| **Level 3** | High | Data exposure -- sensitive data surfaced by Copilot to unauthorized users, DLP bypass detected, or governance control failure | 24 hours |
| **Level 2** | Medium | Policy violation -- individual DLP policy match, non-critical control degradation, or procedural non-compliance | 2 business days |
| **Level 1** | Low | Standard issue -- minor configuration question, documentation gap, or isolated user issue | 5 business days |

---

## Level 4: Critical -- Regulatory Impact

**Trigger Criteria:**

- Regulated data (NPI, PII, material non-public information) exposed through Copilot to unauthorized users
- Information Barrier (Chinese Wall) breach via Copilot grounding
- Confirmed violation of FINRA, SEC, OCC, or other regulatory requirements
- All Copilot governance controls simultaneously disabled or non-functional
- Copilot used to generate content that causes material customer harm

**Notification Targets:**

| Recipient | Notification Window | Method |
|-----------|-------------------|--------|
| Security Operations | Immediate | Automated alert + phone |
| CISO / Security Lead | Within 15 minutes | Phone call |
| Compliance Officer | Within 30 minutes | Phone call |
| Legal Counsel | Within 30 minutes | Phone call |
| Executive Management (CRO, CEO) | Within 1 hour | Phone call + email |
| AI Governance Lead | Within 1 hour | Phone call + email |
| Regulatory notification assessment | Within 4 hours | Legal-led evaluation |

**Response Steps:**

1. **Contain immediately** -- disable Copilot for affected users or organization-wide if scope is unknown
2. **Activate incident response team** -- initiate war room (Teams channel or bridge call)
3. **Preserve all evidence** -- export audit logs, DLP reports, and interaction records
4. **Assess exposure scope** -- determine which data was exposed, to whom, and for how long
5. **Assess regulatory notification obligations** -- engage Legal to evaluate GLBA, state breach notification, and regulatory filing requirements
6. **Brief executive management** -- provide initial assessment within 1 hour
7. **Provide hourly status updates** until containment is confirmed
8. **File regulatory notifications** within required timeframes if applicable

**Documentation Requirements:**

- Incident timeline with all actions and timestamps
- Evidence preservation confirmation
- Exposure scope assessment
- Regulatory notification decision and rationale
- Remediation plan with assigned owners and target dates
- Executive briefing materials

---

## Level 3: High -- Data Exposure

**Trigger Criteria:**

- Sensitive (non-regulated) data surfaced by Copilot to users without appropriate access
- DLP policy bypass detected in Copilot interactions
- Copilot governance control failure lasting more than 1 hour
- Insider Risk Management alert triggered by Copilot-related activity
- Unauthorized Copilot access from unmanaged device or untrusted location

**Notification Targets:**

| Recipient | Notification Window | Method |
|-----------|-------------------|--------|
| Security Operations | Immediate | Automated alert |
| CISO / Security Lead | Within 2 hours | Email + Teams message |
| Compliance Officer | Within 4 hours | Email |
| AI Governance Lead | Within 4 hours | Email + Teams message |
| Governance Committee | Next business day | Email summary |

**Response Steps:**

1. **Investigate and confirm** the issue scope within 2 hours
2. **Implement compensating controls** if the primary control cannot be restored immediately
3. **Restrict Copilot access** for affected users or content if needed
4. **Develop remediation plan** with timeline (target resolution within 24 hours)
5. **Brief CISO and Compliance** with impact assessment
6. **Monitor for recurrence** after remediation
7. **Update governance committee** at next meeting or via ad-hoc briefing

**Documentation Requirements:**

- Issue description and scope
- Investigation findings and root cause
- Remediation plan and completion evidence
- Governance committee briefing notes

---

## Level 2: Medium -- Policy Violation

**Trigger Criteria:**

- Individual DLP policy match in Copilot interactions (not involving regulated data)
- Non-critical governance control operating in degraded state
- User-reported concern about Copilot data access
- Communication compliance policy match requiring review
- Copilot configuration drift detected

**Notification Targets:**

| Recipient | Notification Window | Method |
|-----------|-------------------|--------|
| Responsible team (per RACI) | Within 24 hours | Ticketing system |
| Team lead | Within 48 hours | Email |
| Governance Committee | Monthly meeting | Standing agenda item |

**Response Steps:**

1. **Investigate root cause** within 24 hours
2. **Assess whether the issue is isolated** or systemic
3. **Develop remediation plan** with target completion within 2 business days
4. **Implement fix** following standard change management
5. **Verify resolution** through testing
6. **Update governance records** and close the ticket

**Documentation Requirements:**

- Ticket in governance tracking system
- Root cause analysis
- Remediation completion evidence

---

## Level 1: Low -- Standard Issue

**Trigger Criteria:**

- Individual user configuration question or access issue
- Minor false positive pattern in DLP policies
- Documentation gap or update needed
- Non-urgent policy clarification request
- Minor Copilot feature behavior question

**Notification Targets:**

| Recipient | Notification Window | Method |
|-----------|-------------------|--------|
| Responsible team | Within 72 hours | Ticketing system |

**Response Steps:**

1. **Log the issue** in the governance tracking system
2. **Triage and assign** to the appropriate team
3. **Schedule remediation** within the standard work cycle (target 5 business days)
4. **Verify resolution** and close the ticket

**Documentation Requirements:**

- Ticket in governance tracking system
- Resolution notes

---

## Escalation Decision Tree

When an issue is detected, use this decision tree to assign severity:

```
1. Is regulated data (NPI, MNPI, PII) exposed or is there a confirmed
   regulatory violation?
   YES --> Level 4 (Critical)
   NO  --> Continue

2. Is sensitive data exposed to unauthorized users, or has a governance
   control failed?
   YES --> Level 3 (High)
   NO  --> Continue

3. Is there a policy violation or control degradation that needs
   prompt attention?
   YES --> Level 2 (Medium)
   NO  --> Level 1 (Low)
```

**When in doubt:** Escalate to the next higher severity level. It is safer to downgrade after investigation than to under-classify an incident.

---

## Escalation Contacts Template

| Role | Primary Contact | Backup Contact | Phone | Email |
|------|----------------|----------------|-------|-------|
| CISO / Security Lead | [Name] | [Name] | [Phone] | [Email] |
| Compliance Officer | [Name] | [Name] | [Phone] | [Email] |
| M365 Global Admin | [Name] | [Name] | [Phone] | [Email] |
| Security Operations Lead | [Name] | [Name] | [Phone] | [Email] |
| Legal Counsel | [Name] | [Name] | [Phone] | [Email] |
| AI Governance Lead | [Name] | [Name] | [Phone] | [Email] |
| CRO / Executive Sponsor | [Name] | [Name] | [Phone] | [Email] |
| Microsoft TAM | [Name] | [Name] | [Phone] | [Email] |

!!! tip "Contact List Maintenance"
    Update the contact list monthly or immediately when personnel changes occur. Test contact information quarterly as part of the escalation matrix review.

---

## External Escalation

### Microsoft Support

- **Standard issues:** Microsoft 365 service request via Admin Center
- **Security incidents:** Microsoft Security Response Center (MSRC)
- **TAM escalation:** For premier support customers with a Technical Account Manager
- **Severity A:** Available 24/7 for critical production-down scenarios

### Regulatory Notifications

If a Level 4 incident may require regulatory notification:

1. **Engage Legal Counsel** immediately
2. **Assess notification obligations** under applicable regulations:
    - GLBA Safeguards Rule (FTC/prudential regulators)
    - State data breach notification laws (varies by jurisdiction)
    - SAR filing requirements (if applicable to the activity)
    - FINRA regulatory event reporting
3. **Prepare notification materials** per Legal guidance
4. **File notifications** within required timeframes
5. **Document all notification actions** with timestamps and recipients

---

*Review and test this escalation matrix quarterly. Update contacts monthly or when personnel changes occur. Conduct a tabletop exercise using this matrix semi-annually.*

*FSI Copilot Governance Framework v1.2.1 - March 2026*
