# AI Incident Response Playbook

Copilot-specific incident response procedures for financial services organizations. This playbook supplements your existing incident response plan with AI-specific procedures.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## AI Incident Categories

### Category 1: Data Exposure via Copilot

**Definition:** Copilot surfaces, generates, or distributes sensitive data to unauthorized users.

**Examples:**
- Copilot response contains customer PII accessible to unauthorized user
- Copilot grounding bypasses Information Barriers
- Copilot Pages shared broadly containing restricted data

**Severity:** P1 or P2 depending on data sensitivity and exposure scope

### Category 2: Copilot Governance Control Failure

**Definition:** A governance control stops functioning, allowing uncontrolled Copilot behavior.

**Examples:**
- DLP policies disabled or non-functional for Copilot
- Restricted SharePoint Search disabled without authorization
- Audit logging interrupted for Copilot interactions

**Severity:** P2 or P3 depending on duration and scope

### Category 3: Copilot Misuse

**Definition:** Users intentionally or unintentionally misuse Copilot in ways that violate policy.

**Examples:**
- Prompt injection attempts to access restricted content
- Systematic use of Copilot to extract or aggregate sensitive data
- Using Copilot to generate content that violates regulatory requirements

**Severity:** P2 or P3 depending on intent and impact

### Category 4: AI Output Accuracy Incident

**Definition:** Copilot generates inaccurate content that is used for business decisions or client communications.

**Examples:**
- Copilot generates incorrect financial figures used in a client report
- Copilot summarizes regulatory requirements inaccurately
- Copilot misattributes content to wrong sources

**Severity:** P2 or P3 depending on the use of the inaccurate content

## Response Procedures

### Phase 1: Detection and Triage (0-1 hour)

1. **Confirm the incident** — verify it is a real incident, not a false alarm
2. **Classify severity** using the categories and escalation matrix
3. **Notify** per the escalation path for the assigned severity
4. **Assign an incident lead** from the response team
5. **Begin incident log** documenting all actions with timestamps

### Phase 2: Containment (1-4 hours for P1/P2)

**Data Exposure containment:**
- Disable Copilot for affected users if needed (remove from license group)
- Restrict sharing on affected content
- Revoke sharing links on exposed content
- Preserve audit logs and evidence

**Control Failure containment:**
- Re-enable the failed control immediately
- Verify the control is functioning after re-enablement
- Determine the scope of the gap (what happened while the control was down)
- Enable compensating controls if the primary control cannot be restored

**Misuse containment:**
- Disable Copilot for the user under investigation
- Preserve all audit logs and interaction records
- Notify HR and Legal per your investigation procedures
- Do not alert the user until investigation guidance from Legal

### Phase 3: Investigation (4-48 hours)

1. **Collect evidence:**
   - Export Copilot audit logs for the incident timeframe
   - Capture DLP incident records
   - Export sign-in logs and Conditional Access evaluations
   - Preserve any Copilot-generated content involved

2. **Determine root cause:**
   - Was this a control gap, misconfiguration, or user action?
   - What was the scope of impact (users, data, timeframe)?
   - Was sensitive data actually exposed or only potentially exposed?

3. **Assess regulatory impact:**
   - Does this trigger breach notification obligations?
   - Are regulatory filings required (SAR, STR)?
   - Does this constitute a books and records violation?

### Phase 4: Remediation (24 hours - 2 weeks)

1. **Fix the root cause** — deploy permanent controls to prevent recurrence
2. **Remediate the impact** — notify affected parties if required
3. **Validate the fix** — run verification tests to confirm the issue is resolved
4. **Update controls** — strengthen governance controls based on findings

### Phase 5: Post-Incident (1-2 weeks after resolution)

1. **Conduct post-incident review** with the response team
2. **Document lessons learned** and update procedures
3. **Update the risk register** with the incident findings
4. **Brief governance committee** on the incident and remediation
5. **Update training** if user behavior contributed to the incident
6. **File regulatory notifications** if required

## Incident Communication Templates

### Internal Notification (P1)

Subject: [P1 INCIDENT] Copilot Data Security Event — [Brief Description]

A Copilot-related security event has been detected requiring immediate attention. The incident response team has been activated and containment actions are underway. Details will be shared as the investigation progresses. Please direct all inquiries to [Incident Lead].

### Regulatory Notification Assessment

When assessing whether regulatory notification is required, evaluate:
- Type and volume of data involved
- Number of individuals affected
- State breach notification requirements (varies by jurisdiction)
- GLBA Safeguards Rule notification obligations
- Time-sensitive notification deadlines

Engage Legal Counsel for all notification decisions.

---

*Test this playbook through tabletop exercises semi-annually. Update based on real incidents and evolving AI capabilities.*

*FSI Copilot Governance Framework v1.3 - April 2026*
