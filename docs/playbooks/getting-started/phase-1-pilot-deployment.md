# Phase 1: Pilot Deployment (Days 30-60)

Controlled rollout of M365 Copilot to a pilot group of 25-50 users, with daily monitoring, policy validation, and structured feedback collection.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## Objective

Validate that governance controls, DLP policies, sensitivity labels, and audit logging function as expected in production use. Collect operational data and user feedback to inform broader deployment decisions.

---

## Prerequisites

- Phase 0 completed with governance committee sign-off
- All Phase 0 deliverables verified (see [Phase 0 checklist](phase-0-governance-setup.md#phase-0-deliverables-checklist))
- Pilot group licensed and trained

---

## Steps

### Step 1: Deploy Copilot to Pilot Group (25-50 Users)

**Actions:**

1. **Confirm license activation** -- verify all pilot group members show active Copilot licenses in the M365 Admin Center

2. **Send pilot launch communication** including:
    - Approved use cases and any usage restrictions
    - Feedback submission process
    - Support escalation contacts
    - Reminder of acceptable use policy for AI tools

3. **Enable Copilot access** by verifying the pilot security group is correctly assigned in the Copilot admin settings

4. **Validate initial access** -- have 2-3 pilot users confirm they can access Copilot in each enabled application (Word, Excel, PowerPoint, Outlook, Teams)

5. **Document launch date and time** for audit trail purposes

**Deliverable:** Confirmed Copilot access for all pilot group members with launch communication documented

---

### Step 2: Monitor Copilot Audit Logs Daily

**Portal:** Microsoft Purview
**Path:** Purview > Audit > Search

**Actions:**

1. **Establish daily monitoring routine** for the first 14 days of pilot:
    - Search Unified Audit Log for Copilot-related events (`CopilotInteraction`)
    - Filter by pilot group users
    - Review interaction volume, application usage patterns, and any unusual activity

2. **Create monitoring checklist** -- review daily:

    | Check | What to Look For |
    |-------|-----------------|
    | Interaction volume | Baseline usage patterns per user |
    | Application distribution | Which M365 apps are used most with Copilot |
    | DLP policy matches | Any DLP violations triggered by Copilot interactions |
    | Sensitivity label activity | Labels applied or inherited during Copilot use |
    | Error events | Copilot access failures or blocked interactions |
    | Unusual patterns | Unusually high volume or off-hours usage |

3. **Document findings** in a daily monitoring log for governance committee reporting

4. **Escalate anomalies** per the [Escalation Matrix](../governance-operations/escalation-matrix.md)

**Deliverable:** Daily monitoring logs for first 14 days, weekly thereafter

---

### Step 3: Validate DLP Policy Effectiveness

**Portal:** Microsoft Purview
**Path:** Purview > Data Loss Prevention > Activity Explorer

**Actions:**

1. **Review DLP Activity Explorer** for Copilot-related matches during the pilot period:
    - Filter by the "Microsoft 365 Copilot" location
    - Identify which sensitive information types are triggering
    - Review match accuracy (true positives vs. false positives)

2. **Conduct controlled tests** with pilot compliance team members:
    - Attempt to use Copilot to summarize documents containing test sensitive data
    - Verify that DLP policies block or warn as configured
    - Test across each enabled application
    - Document test results with screenshots

3. **Analyze false positive rate:**
    - Target less than 5% false positive rate for blocking actions
    - Target less than 15% false positive rate for warning actions
    - Tune sensitive information type confidence levels if thresholds are exceeded

4. **Document policy effectiveness** including gaps requiring adjustment

**Deliverable:** DLP effectiveness report with test results and tuning recommendations

---

### Step 4: Collect User Feedback

**Actions:**

1. **Deploy feedback collection mechanism:**
    - Microsoft Forms survey distributed at Day 7, Day 14, and Day 28
    - Optional: Viva Pulse surveys for quick sentiment checks
    - Designated Teams channel for real-time feedback and questions

2. **Feedback survey template:**

    | Question | Response Type |
    |----------|--------------|
    | Which M365 applications have you used Copilot with? | Multi-select |
    | How useful has Copilot been for your daily work? | 1-5 scale |
    | Have you encountered any data that Copilot surfaced that seemed inappropriate? | Yes/No + description |
    | Have you received any DLP policy tips or blocks while using Copilot? | Yes/No + description |
    | Has Copilot produced any output that was inaccurate or misleading? | Yes/No + description |
    | What concerns do you have about using Copilot with client or sensitive data? | Free text |
    | What additional training or guidance would be helpful? | Free text |
    | Would you recommend expanding Copilot to your broader team? | Yes/No + rationale |

3. **Compile feedback reports** for governance committee review at each collection point

4. **Track and categorize issues raised** -- separate into:
    - Security/compliance concerns (priority resolution)
    - Usability issues (inform training updates)
    - Feature requests (inform expansion planning)

**Deliverable:** Feedback survey results at Day 7, Day 14, and Day 28 with categorized issue tracker

---

### Step 5: Adjust Configurations Based on Findings

**Actions:**

1. **Review all monitoring data, DLP reports, and user feedback** at the Day 14 checkpoint

2. **Identify required adjustments:**

    | Finding Type | Potential Adjustment |
    |-------------|---------------------|
    | High false positive rate | Tune DLP sensitive information type confidence levels |
    | Oversharing detected via Copilot | Tighten SharePoint permissions, add sensitivity labels |
    | Users accessing unexpected content | Review and restrict site-level permissions |
    | Policy gaps identified | Create additional DLP rules or sensitivity labels |
    | Application-specific concerns | Adjust per-app Copilot toggles |
    | Audit log gaps | Verify logging configuration and retention |

3. **Implement adjustments** following change management procedures:
    - Document the change rationale
    - Obtain governance committee approval for significant policy changes
    - Test changes in simulation before enforcement where possible

4. **Communicate changes** to pilot group with updated guidance

**Deliverable:** Configuration change log with rationale and approval documentation

---

### Step 6: Document Lessons Learned

**Actions:**

1. **Compile lessons learned document** covering:
    - What worked well during the pilot
    - What required adjustment and why
    - Unexpected findings (both positive and negative)
    - DLP policy effectiveness metrics
    - User adoption patterns and barriers
    - Compliance monitoring effectiveness

2. **Categorize lessons** by area:
    - **Technical configuration** -- what settings needed tuning
    - **Governance process** -- what governance procedures were effective or insufficient
    - **User behavior** -- how users actually interacted with Copilot
    - **Compliance impact** -- any regulatory or compliance observations
    - **Training gaps** -- what users needed that training did not cover

3. **Present to governance committee** for review and input

**Deliverable:** Lessons learned document approved by governance committee

---

### Step 7: Prepare Expansion Plan

**Actions:**

1. **Develop Phase 2 expansion proposal** based on pilot results:
    - Recommended departments for next wave
    - Updated prerequisite checklist based on pilot lessons
    - Revised DLP policies and sensitivity label requirements
    - Additional controls to implement (conditional access, information barriers)
    - Updated training curriculum

2. **Define expansion criteria:**
    - Department has completed DSPM assessment with Critical/High findings remediated
    - Sensitivity label coverage meets threshold
    - Department leadership has approved participation
    - Users have completed updated training

3. **Create expansion timeline** with target dates and milestones

4. **Obtain governance committee approval** for Phase 2 launch

**Deliverable:** Phase 2 expansion plan approved by governance committee

---

## Pilot Monitoring Checklist

Use this checklist daily during the first two weeks, weekly thereafter.

| # | Check | Frequency | Status |
|---|-------|-----------|--------|
| 1 | Review Copilot audit log events for pilot users | Daily (Weeks 1-2), Weekly (Weeks 3-4) | [ ] |
| 2 | Check DLP Activity Explorer for Copilot matches | Daily (Weeks 1-2), Weekly (Weeks 3-4) | [ ] |
| 3 | Review sensitivity label activity for Copilot interactions | Weekly | [ ] |
| 4 | Check for DSPM alerts on new oversharing findings | Weekly | [ ] |
| 5 | Review user feedback submissions | As received | [ ] |
| 6 | Verify audit log retention is functioning | Weekly | [ ] |
| 7 | Check Copilot usage reports in M365 Admin Center | Weekly | [ ] |
| 8 | Review Insider Risk Management signals (if configured) | Weekly | [ ] |
| 9 | Validate Conditional Access policy enforcement | Weekly | [ ] |
| 10 | Report findings to governance committee | Weekly | [ ] |

---

## Success Criteria

Phase 1 is complete when:

- [ ] Copilot has been operational for pilot group for minimum 30 days
- [ ] Daily monitoring has been conducted for first 14 days with no unresolved Critical findings
- [ ] DLP policy effectiveness validated with false positive rate within acceptable thresholds
- [ ] User feedback collected at three intervals with all security/compliance concerns addressed
- [ ] Configuration adjustments documented and approved
- [ ] Lessons learned document completed and approved
- [ ] Phase 2 expansion plan approved by governance committee

---

## Next Steps

- Proceed to [Phase 2 -- Expansion](phase-2-expansion.md) for broader deployment
- Implement advanced controls identified during pilot (conditional access, information barriers)
- Update training materials based on pilot feedback

---

*FSI Copilot Governance Framework v1.1 -- February 2026*
