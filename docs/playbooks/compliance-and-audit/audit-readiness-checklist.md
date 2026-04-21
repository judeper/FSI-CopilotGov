# Audit Readiness Checklist

Pre-examination preparation checklist for regulatory examinations and internal audits of M365 Copilot governance controls.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## 30 Days Before Examination

### Governance Documentation

- [ ] Governance committee charter is current and signed
- [ ] Meeting minutes for the examination period are compiled
- [ ] Governance decisions are documented with rationale
- [ ] RACI matrix is current with named individuals
- [ ] Acceptable use policy for Copilot is published and acknowledged by users
- [ ] Escalation matrix is current with valid contact information

### Policy Documentation

- [ ] DLP policy documentation is current with configuration details
- [ ] Sensitivity label taxonomy is documented with change history
- [ ] Conditional Access policy documentation is current
- [ ] Information Barrier policy documentation is current
- [ ] Data residency documentation is current
- [ ] Vendor risk assessment is current (within the last 12 months)

### Technical Evidence

- [ ] Run all evidence collection scripts (see Evidence Pack Assembly)
- [ ] Export DLP incident reports for the examination period
- [ ] Export audit logs for the examination period
- [ ] Capture current configuration screenshots for all controls
- [ ] Generate Copilot usage analytics for the examination period
- [ ] Export insider risk alert summary

## 14 Days Before Examination

### Evidence Organization

- [ ] Evidence pack assembled and organized by category
- [ ] Evidence index document created with file listing
- [ ] All evidence items verified for completeness and accuracy
- [ ] Date ranges on all reports match the examination period
- [ ] Sensitive data unrelated to the examination is redacted
- [ ] Quality review completed by a second reviewer

### Personnel Preparation

- [ ] Examination response team identified and notified
- [ ] Subject matter experts briefed on their areas of responsibility
- [ ] Response coordinator designated to manage examiner interactions
- [ ] Meeting rooms and technical access arranged for examiners
- [ ] Backup personnel identified for key roles

### Process Readiness

- [ ] Walk-through of evidence pack with the response team
- [ ] Practice Q&A session for common examiner questions
- [ ] Review of previous examination findings and remediation status
- [ ] Identification of any known gaps with documented remediation plans
- [ ] Communication plan for internal stakeholders during examination

## 7 Days Before Examination

### Final Verification

- [ ] Re-run critical verification tests to confirm current control status
- [ ] Verify all controls are in enforcement mode (not test mode)
- [ ] Confirm audit logging is active and capturing Copilot events
- [ ] Verify the evidence pack is accessible to the response team
- [ ] Conduct a final review of any recent governance changes

### Logistics

- [ ] Examiner access credentials prepared (if on-site examination)
- [ ] Conference rooms booked for the examination period
- [ ] Technical demonstration environment prepared
- [ ] Backup copies of evidence pack stored securely
- [ ] Emergency contact list distributed to the response team

## Day of Examination

### Opening

- [ ] Greet examiners and complete introductions
- [ ] Provide overview of Copilot governance framework
- [ ] Distribute evidence pack or provide access to shared repository
- [ ] Assign a single point of contact for all examiner requests
- [ ] Establish daily check-in schedule with examiners

### During Examination

- [ ] Log all examiner requests with date, time, and assigned responder
- [ ] Provide requested materials within the agreed SLA (typically 24 hours)
- [ ] Brief response team daily on examination progress and emerging themes
- [ ] Escalate any unexpected findings immediately per escalation matrix
- [ ] Document any verbal commitments made to examiners

### Closing

- [ ] Attend closing meeting and take detailed notes
- [ ] Request a summary of preliminary findings
- [ ] Agree on timeline for formal findings delivery
- [ ] Thank examiners and confirm follow-up process
- [ ] Debrief response team and document lessons learned

## Common Examiner Questions

Prepare responses for these frequently asked examination questions:

1. How does your organization govern AI/Copilot data access?
2. What controls prevent Copilot from accessing data users should not see?
3. How do you monitor Copilot interactions for compliance?
4. What happens when Copilot generates content containing sensitive data?
5. How are Copilot-generated records retained and supervised?
6. What training do employees receive on Copilot governance?
7. How do you manage the risk of AI-generated inaccuracies?
8. What vendor risk assessment has been conducted for Microsoft AI services?
9. How do Information Barriers apply to Copilot in your organization?
10. What incident response procedures exist for Copilot-related events?

---

*Review and update this checklist annually and after each examination to incorporate lessons learned.*

*FSI Copilot Governance Framework v1.4.0 - April 2026*
