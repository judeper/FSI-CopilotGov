# Phase 2: Expansion and Steady-State (Days 60-90)

Broader deployment of M365 Copilot across additional departments with advanced controls, compliance validation, and establishment of ongoing governance operations.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## Objective

Scale Copilot from pilot to broader organizational deployment while implementing advanced security controls, validating compliance posture, and establishing the steady-state operational governance cadence.

---

## Prerequisites

- Phase 1 completed with governance committee sign-off
- Lessons learned document reviewed and incorporated
- Phase 2 expansion plan approved
- Advanced control prerequisites in place (E5 licenses, SharePoint Advanced Management)

---

## Steps

### Step 1: Expand to Additional Departments

**Actions:**

1. **Validate department readiness** for each expansion wave:
    - DSPM oversharing assessment completed for department content
    - Critical and High oversharing findings remediated
    - Sensitivity label coverage at or above 85% for department content
    - Department leadership approval obtained
    - Users have completed Copilot training

2. **Create expansion wave groups** in Entra ID:
    - Wave 1 (Days 60-70): Next priority departments (e.g., operations, marketing)
    - Wave 2 (Days 70-80): Additional departments (e.g., HR, finance support)
    - Wave 3 (Days 80-90): Remaining approved departments

3. **Assign licenses** via group-based licensing for each wave

4. **Monitor each wave** for the first 5 business days using the same daily monitoring routine established during pilot

5. **Apply tuned policies** -- use the DLP and sensitivity label configurations refined during Phase 1

**Deliverable:** Documented deployment for each wave with readiness verification and monitoring results

---

### Step 2: Implement Advanced Controls (Conditional Access, Information Barriers)

Deploy security controls that require broader deployment context or were deferred from Phase 0/1.

#### 2a: Conditional Access Policies for Copilot

**Portal:** Microsoft Entra Admin Center
**Path:** Entra ID > Protection > Conditional Access > Policies

**Actions:**

1. **Create Copilot-specific Conditional Access policies:**
    - Require compliant or Entra-joined devices for Copilot access
    - Block Copilot access from unmanaged devices
    - Require multi-factor authentication for Copilot sessions
    - Restrict Copilot access to approved locations (if applicable)

2. **Target the Microsoft 365 Copilot cloud app** in the policy assignment

3. **Test in report-only mode** for 5 business days before enforcement

See also: [Control 2.3 -- Conditional Access Policies](../control-implementations/2.3/portal-walkthrough.md)

#### 2b: Information Barriers for Copilot (Chinese Wall)

**Portal:** Microsoft Purview
**Path:** Purview > Information Barriers > Policies

**Actions:**

1. **Define information barrier segments** based on business functions that must be separated:
    - Investment banking vs. research
    - Trading vs. compliance
    - Advisory vs. proprietary operations

2. **Create barrier policies** that help prevent Copilot from surfacing content across barrier boundaries

3. **Apply barriers** and verify enforcement through controlled testing

4. **Document barrier configurations** for regulatory examination readiness

See also: [Control 2.4 -- Information Barriers](../control-implementations/2.4/portal-walkthrough.md)

**Deliverable:** Conditional Access and Information Barrier policies deployed and verified

---

### Step 3: Enable Communication Compliance Monitoring

**Portal:** Microsoft Purview
**Path:** Purview > Communication Compliance > Policies

**Actions:**

1. **Create communication compliance policies** for Copilot interactions:
    - Monitor for regulatory language violations (investment recommendations, forward-looking statements)
    - Monitor for inappropriate content generation
    - Monitor for potential customer communication compliance issues

2. **Configure review workflows:**
    - Assign compliance reviewers
    - Set review cadence (daily for high-risk policies, weekly for standard)
    - Configure escalation for confirmed violations

3. **Integrate with existing supervision programs** -- Copilot-assisted communications should be subject to the same supervision requirements as other business communications per FINRA Rules 3110 and 3120

4. **Test policies** with controlled scenarios before enabling for all users

**Deliverable:** Communication compliance policies active for Copilot interactions with documented review workflow

See also: [Control 3.4 -- Communication Compliance](../control-implementations/3.4/portal-walkthrough.md)

---

### Step 4: Set Up Sentinel Integration for Monitoring

**Portal:** Microsoft Sentinel
**Path:** Sentinel > Data Connectors > Microsoft 365

**Actions:**

1. **Enable the Microsoft 365 data connector** in Sentinel if not already active

2. **Create Copilot-specific analytics rules:**

    | Rule | Detection | Severity |
    |------|-----------|----------|
    | High-volume Copilot usage | User exceeds 3x average daily interactions | Medium |
    | After-hours Copilot access | Copilot usage outside business hours from non-exempt users | Low |
    | DLP violation spike | More than 5 DLP matches in Copilot within 1 hour | High |
    | Sensitive content access pattern | Copilot used to access content across multiple sensitivity labels in rapid succession | Medium |
    | Failed access attempts | Multiple Copilot access failures suggesting permission issues | Medium |

3. **Configure automated response playbooks** for high-severity alerts:
    - Disable Copilot license for the affected user
    - Notify the security operations team
    - Create an incident ticket

4. **Create Copilot governance workbook** in Sentinel for executive dashboards

**Deliverable:** Sentinel analytics rules and response playbooks deployed for Copilot monitoring

---

### Step 5: Establish Operational Governance Cadence

**Actions:**

1. **Transition governance committee to steady-state cadence:**
    - Monthly governance committee meetings (down from weekly during deployment)
    - Quarterly compliance review meetings
    - Annual comprehensive governance review

2. **Implement the Governance Operating Calendar:**
    - Monthly activities: usage report review, DLP violation review, license optimization
    - Quarterly activities: compliance assessment, policy updates, training refresher
    - Annual activities: board review, comprehensive audit, framework update
    - See [Governance Operating Calendar](../governance-operations/governance-operating-calendar.md) for full schedule

3. **Assign ongoing operational responsibilities** using the [RACI Template](../governance-operations/raci-governance-template.md)

4. **Establish reporting cadence:**
    - Monthly Copilot governance report to CISO
    - Quarterly compliance status report to governance committee
    - Annual governance program report to board or executive leadership

5. **Document operational procedures** for:
    - New user onboarding (Copilot license assignment, training requirement)
    - User offboarding (license revocation, access review)
    - Policy change management
    - Incident response (see [AI Incident Response Playbook](../incident-and-risk/ai-incident-response-playbook.md))

**Deliverable:** Operational governance procedures document with assigned responsibilities and reporting cadence

---

### Step 6: Conduct Compliance Validation

**Actions:**

1. **Perform a compliance gap assessment** against applicable regulations:

    | Regulation | Key Validation Points |
    |-----------|----------------------|
    | FINRA Rule 4511 | Copilot records retained per required periods |
    | SEC Rule 17a-4 | Retention policies cover Copilot interaction logs |
    | FINRA Rules 3110/3120 | Copilot communications included in supervision program |
    | FINRA Rule 2210 | Copilot-generated customer communications reviewed |
    | Regulation S-P | NPI protected from unauthorized Copilot access |
    | GLBA | Customer financial information safeguards applied |
    | SOX (if applicable) | Copilot controls documented in ITGC framework |

2. **Collect evidence** demonstrating control effectiveness:
    - Export audit log samples showing Copilot event capture
    - Document DLP policy configurations and violation reports
    - Export sensitivity label deployment reports
    - Capture Conditional Access policy configurations
    - Document Information Barrier configurations

3. **Identify gaps** and create remediation plans with target dates

4. **Present validation results** to governance committee

**Deliverable:** Compliance validation report with evidence inventory and gap remediation plan

See also: [Evidence Pack Assembly](../compliance-and-audit/evidence-pack-assembly.md)

---

### Step 7: Achieve Steady-State Operations

**Actions:**

1. **Confirm all deployment waves are complete** and stable

2. **Verify steady-state monitoring is operational:**
    - Sentinel analytics rules active and generating alerts appropriately
    - Communication compliance policies reviewed regularly
    - DLP policies enforced with acceptable false positive rates
    - Audit log retention confirmed and verified

3. **Formalize the governance program:**
    - All operational procedures documented
    - RACI matrix finalized and communicated
    - Escalation matrix published and tested
    - Training program established for new employees

4. **Conduct Phase 2 retrospective** with governance committee:
    - Review overall deployment success
    - Document remaining items for continuous improvement
    - Identify controls requiring further maturation
    - Set goals for the next governance review cycle

5. **Archive deployment documentation** for regulatory examination readiness

**Deliverable:** Steady-state declaration signed by governance committee with ongoing governance program documented

---

## Success Criteria

Phase 2 is complete when:

- [ ] Copilot deployed to all approved departments across expansion waves
- [ ] Conditional Access policies enforced for Copilot access
- [ ] Information Barriers configured and verified for required business function separations
- [ ] Communication compliance monitoring active for Copilot interactions
- [ ] Sentinel integration operational with analytics rules and response playbooks
- [ ] Governance operating cadence established and documented
- [ ] Compliance validation completed with no unresolved Critical gaps
- [ ] Steady-state operations confirmed by governance committee

---

## Ongoing Monitoring Plan

After achieving steady-state, maintain the following monitoring activities:

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| Copilot audit log review | Weekly | Compliance Analyst |
| DLP violation report review | Weekly | Purview Compliance Admin |
| Sentinel alert triage | Daily | Security Operations |
| Communication compliance review | Per policy cadence | Compliance Reviewer |
| DSPM oversharing assessment | Monthly | Information Protection Lead |
| Usage analytics review | Monthly | AI Governance Lead |
| License utilization review | Monthly | M365 Admin |
| Governance committee meeting | Monthly | AI Governance Lead |
| Comprehensive compliance review | Quarterly | Compliance Officer |
| Board governance report | Annually | CISO |

---

## Next Steps

- Maintain governance operations per the [Governance Operating Calendar](../governance-operations/governance-operating-calendar.md)
- Prepare for regulatory examinations using the [Audit Readiness Checklist](../compliance-and-audit/audit-readiness-checklist.md)
- Conduct ongoing risk assessments using the [AI Risk Assessment Template](../incident-and-risk/ai-risk-assessment-template.md)
- Monitor for regulatory changes, including the [Colorado AI Act](../regulatory-modules/colorado-ai-act-readiness.md)

---

*FSI Copilot Governance Framework v1.1 -- February 2026*
