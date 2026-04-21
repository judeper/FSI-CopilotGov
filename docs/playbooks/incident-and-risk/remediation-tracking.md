# Remediation Tracking

Procedures for tracking and resolving governance gaps, audit findings, and risk assessment items related to M365 Copilot.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## Remediation Sources

Governance gaps and remediation items originate from multiple sources:

| Source | Frequency | Typical Items |
|--------|-----------|---------------|
| Internal audit findings | Semi-annually | Control deficiencies, documentation gaps |
| Regulatory examination findings | As received | Matters Requiring Attention (MRA), Matters Requiring Immediate Attention (MRIA) |
| Risk assessment findings | Per assessment | Unmitigated risks, control gaps |
| Governance committee decisions | Monthly | Policy updates, control enhancements |
| Incident post-mortems | Per incident | Process improvements, control strengthening |
| Continuous monitoring | Ongoing | Configuration drift, new vulnerabilities |

## Remediation Tracking Template

### Remediation Item Record

| Field | Value |
|-------|-------|
| **Item ID** | [REM-YYYY-NNN] |
| **Source** | [Audit finding / Exam finding / Risk assessment / Incident / Monitoring] |
| **Date Identified** | [YYYY-MM-DD] |
| **Description** | [Clear description of the gap or finding] |
| **Severity** | [Critical / High / Medium / Low] |
| **Affected Controls** | [Control IDs from the governance framework] |
| **Owner** | [Name and role responsible for remediation] |
| **Target Date** | [YYYY-MM-DD] |
| **Status** | [Open / In Progress / Pending Validation / Closed] |
| **Remediation Plan** | [Description of the remediation actions] |
| **Evidence of Completion** | [What evidence will demonstrate the item is resolved] |
| **Validation Date** | [YYYY-MM-DD when remediation was validated] |
| **Validated By** | [Name and role of validator] |

## Remediation SLAs

| Severity | Remediation Target | Escalation Trigger |
|----------|--------------------|-------------------|
| **Critical** | 5 business days | After 3 days without progress |
| **High** | 30 business days | After 15 days without progress |
| **Medium** | 90 business days | After 60 days without progress |
| **Low** | 180 business days | After 120 days without progress |

Regulatory examination MRAs and MRIAs follow the regulator-specified timeline, which takes precedence over internal SLAs.

## Tracking Process

### Step 1: Log the Item

When a remediation item is identified:
1. Create a record using the template above
2. Assign a severity based on the risk scoring matrix
3. Assign an owner from the RACI matrix
4. Set a target date based on the SLA
5. Notify the owner and governance committee

### Step 2: Develop Remediation Plan

The remediation owner develops a plan including:
- Specific actions to resolve the gap
- Resources needed (budget, personnel, tools)
- Dependencies on other teams or vendors
- Milestones and checkpoint dates
- Evidence that will demonstrate completion

### Step 3: Execute and Report Progress

- Update item status at each governance committee meeting
- Provide progress notes with each status update
- Escalate blockers per the escalation matrix
- Request target date extensions with justification if needed

### Step 4: Validate Completion

When the owner marks an item as remediated:
1. An independent validator (not the owner) reviews the evidence
2. The validator runs applicable verification tests from the control playbook
3. If validation passes, the item is closed
4. If validation fails, the item returns to "In Progress" with notes

### Step 5: Close and Document

When validated:
1. Update the status to "Closed"
2. Record the validation date and validator
3. Store the evidence in the compliance evidence repository
4. Update the governance committee on closure
5. Retain the record per the evidence retention schedule

## Remediation Dashboard Metrics

Track these metrics for governance committee reporting:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Open items by severity | Zero critical; fewer than 5 high | Count at each meeting |
| Average time to remediation | Within SLA for severity level | Average days open by severity |
| Overdue items | Zero | Count of items past target date |
| Items closed this period | Positive trend | Count per reporting period |
| Validation failure rate | Below 10% | Failed validations / total validations |

## Regulatory Findings Special Handling

For regulatory examination findings (MRAs/MRIAs):
- Track separately from internal findings with examiner-specified deadlines
- Include legal counsel in remediation planning
- Provide progress reports to the regulator per the agreed schedule
- Obtain regulator sign-off on closure where required
- Maintain complete documentation for follow-up examination

---

*Review this process annually and after each examination cycle. Update SLAs and procedures based on organizational capacity and regulatory expectations.*

*FSI Copilot Governance Framework v1.4.0 - April 2026*
