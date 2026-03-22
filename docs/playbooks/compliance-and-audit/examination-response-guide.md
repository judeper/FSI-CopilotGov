# Examination Response Guide

Guide for responding to FINRA, SEC, OCC, and other regulatory examination requests related to M365 Copilot governance.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## Examination Types and Scope

### FINRA Examination

**Focus areas for Copilot:**
- Supervisory procedures for AI-assisted communications (Rule 3110)
- Records retention for AI-generated content (Rule 4511)
- Communications with the public using AI (Rule 2210)
- Information barriers / Chinese Wall compliance

**Key evidence:** Supervisory procedures documentation, DLP policy configuration, audit logs showing Copilot interaction monitoring, Information Barrier policy evidence.

### SEC Examination

**Focus areas for Copilot:**
- Customer information protection (Regulation S-P)
- Electronic records retention (Rule 17a-4)
- Books and records obligations
- Cybersecurity risk management (proposed rules)

**Key evidence:** Data protection controls (DLP, encryption, access controls), records retention policies covering Copilot content, risk assessment documentation, cybersecurity control evidence.

### OCC Examination

**Focus areas for Copilot:**
- Third-party risk management (Bulletin 2013-29 / updated guidance)
- IT risk management and heightened standards
- Operational resilience
- Model risk management (SR 11-7 applicability to AI)

**Key evidence:** Vendor risk assessment for Microsoft AI, IT governance documentation, operational procedures, model risk assessment (if applicable).

## Response Protocols

### Request Handling

When an examiner submits a request:

1. **Log the request** with date, time, examiner name, and specific items requested
2. **Assign to the appropriate SME** based on the RACI matrix
3. **Set a response deadline** (standard: 24 business hours; complex: 48 hours)
4. **Review before submission** — have the response coordinator and legal review all responses
5. **Track delivery** — confirm the examiner received the materials

### Response Quality Standards

All examination responses must:
- Be accurate and complete — never provide partial or misleading information
- Reference specific controls and evidence where applicable
- Avoid speculation — if you do not know, say you will follow up
- Use precise language — avoid overclaiming (use "supports compliance with" phrasing)
- Include supporting evidence (screenshots, exports, policy documents)

### Language Guidelines for Examination Responses

| Avoid | Use Instead |
|-------|-------------|
| "This guarantees compliance with..." | "This control supports compliance with..." |
| "We [promise] that..." | "This control helps meet the requirement for..." |
| "This ensures compliance with..." | "This control helps prevent..." |
| "We have eliminated the risk of..." | "This control reduces the risk of..." |
| "Copilot cannot access..." | "Copilot access is restricted by [specific control]..." |

### Handling Adverse Findings

If an examiner identifies a finding or deficiency:

1. **Acknowledge the finding** without being defensive
2. **Understand the specific concern** — ask clarifying questions
3. **Provide context** if there are compensating controls or mitigating factors
4. **Commit to a remediation timeline** if the finding is valid
5. **Document the finding** and begin remediation planning immediately
6. **Follow up** with the examiner per the agreed timeline

## Examination Scenario Playbooks

### Scenario: "Show me how Copilot is prevented from accessing restricted data"

**Response approach:**
1. Demonstrate Restricted SharePoint Search configuration (Control 1.3)
2. Show the allowed sites list and governance approval documentation
3. Run a live test: Query Copilot for content outside the allowed scope
4. Show DLP policy configuration and a sample policy match
5. Present sensitivity label enforcement evidence

### Scenario: "How do you supervise Copilot-generated communications?"

**Response approach:**
1. Present the supervisory procedures documentation
2. Demonstrate audit logging of Copilot interactions
3. Show DLP monitoring and alert triage procedures
4. Present Defender for Cloud Apps session monitoring
5. Provide sample audit log exports showing interaction records

### Scenario: "What is your AI vendor risk assessment?"

**Response approach:**
1. Present the vendor risk assessment document for Microsoft AI services
2. Reference Microsoft compliance certifications (SOC 2, ISO 27001)
3. Show the Data Processing Agreement and product terms
4. Demonstrate ongoing monitoring (Message Center, service health)
5. Present the risk register with accepted residual risks and governance approval

### Scenario: "How do Information Barriers apply to Copilot?"

**Response approach:**
1. Present Information Barrier segment definitions and policies
2. Demonstrate barrier enforcement in Teams communication
3. Show Copilot grounding restriction across barrier boundaries
4. Present test evidence from Control 2.4 verification
5. Document any barrier exceptions with governance approval

## Post-Examination Activities

1. **Compile examination notes** within 24 hours of closing
2. **Brief leadership** on preliminary findings and themes
3. **Create remediation tracker** for any identified findings
4. **Assign remediation owners** with deadlines
5. **Track formal findings** when the examination report is received
6. **Submit remediation evidence** per examiner-specified timeline
7. **Update governance framework** based on lessons learned
8. **Conduct retrospective** with the response team

---

*Review this guide before each examination and update based on evolving regulatory expectations and examination trends.*

*FSI Copilot Governance Framework v1.2.1 - March 2026*
