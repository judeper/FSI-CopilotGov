# Adoption Roadmap

30/60/90-day phased implementation guidance for deploying M365 Copilot governance in financial services.

---

## Overview

This roadmap provides a structured approach to implementing M365 Copilot governance controls in a regulated financial services environment. The three-phase model (Foundation, Pilot, Expansion) balances rapid value delivery with regulatory obligations.

Organizations should adapt timelines and priorities based on their specific regulatory obligations, existing infrastructure, tenant size, and Copilot deployment plans.

!!! warning "Oversharing First"
    **Do not deploy M365 Copilot broadly before completing oversharing assessment and remediation.** Copilot amplifies existing permission problems at scale. Phase 0 (Foundation) must be completed before enabling Copilot for any production users.

---

## Implementation Phases

| Phase | Timeline | Focus | Key Outcomes |
|-------|----------|-------|--------------|
| **Phase 0** | Days 0-30 | Foundation | Oversharing remediated, governance structure established, core controls active |
| **Phase 1** | Days 30-60 | Pilot | Controlled Copilot rollout, monitoring active, supervisory review operational |
| **Phase 2** | Days 60-90 | Expansion | Broader deployment, advanced controls, compliance validated |

---

## Phase 0: Foundation (Days 0-30)

### Objectives

- Assess and remediate oversharing before Copilot enablement
- Establish governance committee and assign accountabilities
- Implement core security and compliance controls
- Configure Copilot feature toggles for pilot scope
- Complete baseline governance training

### Week-by-Week Activities

**Week 1: Governance Structure and Assessment**

- [ ] Appoint AI Governance Lead / Copilot Program Manager
- [ ] Draft Copilot Governance Committee charter
- [ ] Identify governance committee members (see [Operating Model](operating-model.md))
- [ ] Conduct initial oversharing assessment using SharePoint Advanced Management reports
- [ ] Review existing sensitivity label taxonomy for Copilot readiness
- [ ] Audit current M365 audit logging configuration

**Week 2: Oversharing Remediation**

- [ ] Identify high-risk SharePoint sites (broad access, sensitive content) -- Control 1.1
- [ ] Remediate permissions on priority sites (remove "Everyone" and "Everyone except external users" permissions) -- Control 1.2
- [ ] Review and update external sharing settings -- Control 1.11
- [ ] Assess Teams meeting transcription settings and impact -- Control 1.5
- [ ] Review OneDrive sharing defaults -- Control 1.12

**Week 3: Core Security Controls**

- [ ] Configure DLP policies for sensitive information types (SSN, account numbers, financial data) -- Control 2.1
- [ ] Deploy sensitivity labels to priority content (or validate existing labels) -- Control 2.2
- [ ] Configure web search policy (enable/disable per governance level decision) -- Control 2.7
- [ ] Review and configure plugin/connector policies (default deny recommended) -- Control 2.8
- [ ] Enable Copilot audit logging (verify CopilotInteraction events flow to Unified Audit Log) -- Control 3.1

**Week 4: Operational Readiness**

- [ ] Configure Copilot feature toggles in M365 Admin Center -- Control 4.1
- [ ] Set per-app Copilot controls (enable/disable by application) -- Control 4.2
- [ ] Configure retention policies for Copilot interactions -- Control 3.2
- [ ] Establish incident response procedures for Copilot -- Control 4.5
- [ ] Conduct first governance committee meeting
- [ ] Complete baseline training for pilot users and administrators -- Control 4.13
- [ ] Select pilot group (50-200 users recommended)

### Core Controls to Implement in Phase 0

| Control | Name | Priority | Owner |
|---------|------|----------|-------|
| 1.1 | Oversharing Assessment | **Critical** | SharePoint Admin |
| 1.2 | SharePoint Permissions Remediation | **Critical** | SharePoint Admin |
| 2.1 | DLP Policy Configuration | **Critical** | Purview Admin |
| 2.2 | Sensitivity Label Deployment | **Critical** | Purview Admin |
| 2.7 | Web Search Controls | High | M365 Admin |
| 3.1 | Copilot Audit Logging | **Critical** | Purview Admin |
| 3.2 | Retention Policies | **Critical** | Purview Admin |
| 4.1 | Feature Toggle Management | High | M365 Admin |
| 4.5 | Incident Response | High | CISO |
| 4.13 | Governance Training | High | AI Governance Lead |

### Phase 0 Success Criteria

- [ ] AI Governance Lead appointed with clear accountability
- [ ] Governance committee chartered and held first meeting
- [ ] Oversharing assessment completed; high-risk sites remediated
- [ ] DLP policies active for sensitive information types
- [ ] Sensitivity labels deployed (or existing labels validated for Copilot)
- [ ] Copilot audit logging verified (CopilotInteraction events confirmed)
- [ ] Retention policies configured for Copilot interactions
- [ ] Web search and plugin policies configured
- [ ] Pilot group identified and trained
- [ ] Incident response procedures documented

### Phase 0 Deliverables

| Deliverable | Owner | Due |
|-------------|-------|-----|
| Governance committee charter | AI Governance Lead | Week 1 |
| Oversharing assessment report | SharePoint Admin | Week 2 |
| DLP policy documentation | Purview Admin | Week 3 |
| Copilot configuration documentation | M365 Admin | Week 4 |
| Pilot group training completion | AI Governance Lead | Week 4 |
| Phase 0 readiness report | AI Governance Lead | Week 4 |

---

## Phase 1: Pilot (Days 30-60)

### Objectives

- Deploy Copilot to a controlled pilot group
- Enable communication compliance monitoring
- Implement supervisory review workflows
- Monitor Copilot usage patterns and governance effectiveness
- Identify and address governance gaps before expansion

### Week-by-Week Activities

**Week 5: Pilot Launch**

- [ ] Enable Copilot licenses for pilot group
- [ ] Verify audit logging captures pilot user Copilot interactions -- Control 3.1
- [ ] Enable Copilot usage analytics monitoring -- Control 4.3
- [ ] Activate communication compliance policies for Copilot-assisted emails -- Control 3.4
- [ ] Distribute pilot user guidelines (approved uses, prohibited uses, disclosure requirements)

**Week 6: Supervisory Controls**

- [ ] Implement supervisory review workflow for Copilot-assisted customer communications -- Control 3.6
- [ ] Configure communication compliance keyword policies (promissory language, performance claims) -- Control 3.4
- [ ] For Regulated: Configure FINRA 2210 communication review for pilot users -- Control 3.5
- [ ] Establish supervisory sampling rates for Copilot-assisted correspondence
- [ ] Document written supervisory procedures (WSPs) for Copilot use

**Week 7: Advanced Security**

- [ ] Enable conditional access policies for Copilot users (if not already active) -- Control 2.4
- [ ] Configure auto-labeling policies for common sensitive content -- Control 2.3
- [ ] Review and address DLP policy alerts from pilot usage -- Control 2.1
- [ ] For Regulated: Configure Restricted SharePoint Search for Microsoft 365 Copilot Chat -- Control 1.4
- [ ] Assess Copilot Pages usage and governance needs -- Control 4.8

**Week 8: Monitoring and Assessment**

- [ ] Review Copilot usage analytics from pilot -- Control 4.3
- [ ] Assess communication compliance review results -- Control 3.4
- [ ] Evaluate DLP policy effectiveness (false positive rate, coverage gaps)
- [ ] Review supervisory sampling results -- Control 3.6
- [ ] Conduct pilot user feedback sessions
- [ ] Conduct second governance committee meeting with pilot results
- [ ] Document lessons learned and governance gaps
- [ ] Prepare expansion recommendation

### Controls to Implement in Phase 1

| Control | Name | Priority | Owner |
|---------|------|----------|-------|
| 3.4 | Communication Compliance Monitoring | **Critical** | Compliance Officer |
| 3.5 | FINRA 2210 Communication Review | Critical (Regulated) | Compliance Officer |
| 3.6 | Supervisory Review (FINRA 3110) | **Critical** | Compliance Officer |
| 2.3 | Auto-Labeling Policies | High | Purview Admin |
| 2.4 | Conditional Access for Copilot | High | Entra Admin |
| 4.3 | Usage Analytics | High | M365 Admin |
| 4.8 | Copilot Pages Governance | Medium | M365 Admin |
| 1.4 | Restricted SharePoint Search | Critical (Regulated) | SharePoint Admin |

### Phase 1 Success Criteria

- [ ] Copilot active for pilot group with no critical incidents
- [ ] Communication compliance monitoring active and reviewed
- [ ] Supervisory review procedures operational with documented results
- [ ] DLP policies tuned based on pilot observations (false positive rate acceptable)
- [ ] Audit logs verified for completeness and accessibility
- [ ] Usage analytics dashboard operational
- [ ] Governance committee reviewed pilot results and approved expansion (or identified blockers)
- [ ] Written supervisory procedures documented and approved

### Phase 1 Deliverables

| Deliverable | Owner | Due |
|-------------|-------|-----|
| Pilot usage analytics report | M365 Admin | Week 8 |
| Communication compliance review summary | Compliance Officer | Week 8 |
| Supervisory sampling results | Compliance Officer | Week 8 |
| Written supervisory procedures (Copilot) | Compliance Officer | Week 6 |
| DLP policy tuning report | Purview Admin | Week 7 |
| Expansion recommendation | AI Governance Lead | Week 8 |

---

## Phase 2: Expansion (Days 60-90)

### Objectives

- Deploy Copilot to broader user population based on pilot learnings
- Implement advanced controls for Regulated environments
- Validate examination readiness
- Establish steady-state governance operations

### Week-by-Week Activities

**Week 9: Broader Deployment**

- [ ] Enable Copilot licenses for approved expansion groups
- [ ] Apply pilot-tuned DLP policies, communication compliance, and supervisory procedures to expanded scope
- [ ] Scale training program for new Copilot users -- Control 4.13
- [ ] Configure per-app Copilot controls for expanded scope -- Control 4.2
- [ ] Expand Copilot Pages governance to all users -- Control 4.8

**Week 10: Advanced Controls**

- [ ] Enable eDiscovery for Copilot content -- Control 3.3
- [ ] For Regulated: Configure information barriers between business units -- Control 2.6
- [ ] Enable Defender for Cloud Apps integration -- Control 2.9
- [ ] Configure cost tracking and license optimization -- Control 4.4
- [ ] For Regulated: Implement DSPM for AI -- Control 2.12

**Week 11: Compliance Validation**

- [ ] Conduct examination readiness review (see [Regulatory Framework](regulatory-framework.md) checklist) -- Control 3.13
- [ ] Validate audit log completeness and retention compliance -- Controls 3.1, 3.2
- [ ] Test eDiscovery search and export for Copilot content -- Control 3.3
- [ ] Review and document governance committee effectiveness
- [ ] For Regulated: Document model risk management alignment -- Control 3.8
- [ ] For Regulated: Validate FINRA 2210 compliance program effectiveness -- Control 3.5

**Week 12: Steady-State Operations**

- [ ] Establish ongoing governance operating cadence (monthly committee, quarterly review)
- [ ] For Regulated: Configure Sentinel integration for advanced monitoring -- Control 4.11
- [ ] Document steady-state governance procedures
- [ ] Conduct third governance committee meeting with expansion results
- [ ] Prepare annual governance review framework
- [ ] Complete business continuity assessment for Copilot -- Control 4.9
- [ ] Implement change management procedures for Copilot updates -- Control 4.12

### Controls to Implement in Phase 2

| Control | Name | Priority | Owner |
|---------|------|----------|-------|
| 3.3 | eDiscovery for Copilot Content | **Critical** | Purview Admin |
| 2.6 | Information Barriers | Critical (Regulated) | Compliance Officer |
| 2.9 | Defender for Cloud Apps | High | CISO |
| 2.12 | DSPM for AI | High (Regulated) | Purview Admin |
| 3.8 | Model Risk Documentation | Critical (Regulated) | AI Governance Lead |
| 3.13 | FFIEC Examination Alignment | High (Regulated) | Compliance Officer |
| 4.4 | Cost Tracking | High | M365 Admin |
| 4.9 | Business Continuity | High | M365 Admin |
| 4.11 | Sentinel Integration | High (Regulated) | CISO |
| 4.12 | Change Management | High | AI Governance Lead |

### Phase 2 Success Criteria

- [ ] Copilot deployed to approved broader user population
- [ ] eDiscovery operational for Copilot content
- [ ] All governance level-appropriate controls implemented
- [ ] Examination readiness validated (for Regulated environments)
- [ ] Steady-state governance operating cadence established
- [ ] Governance committee operational with documented procedures
- [ ] Annual governance review framework in place
- [ ] All Copilot-related incidents handled through established procedures

### Phase 2 Deliverables

| Deliverable | Owner | Due |
|-------------|-------|-----|
| eDiscovery readiness validation | Purview Admin | Week 11 |
| Examination readiness report | Compliance Officer | Week 11 |
| Steady-state operations guide | AI Governance Lead | Week 12 |
| Governance effectiveness assessment | AI Governance Lead | Week 12 |
| Annual governance review plan | AI Governance Lead | Week 12 |

---

## Control Implementation Priority Order

### Critical Path Controls

These controls must be implemented first as they enable other governance capabilities:

| Priority | Control | Dependency | Enables |
|----------|---------|------------|---------|
| 1 | 1.1 Oversharing Assessment | None | All Copilot deployment |
| 2 | 1.2 Permissions Remediation | 1.1 | Safe Copilot enablement |
| 3 | 3.1 Copilot Audit Logging | None | Compliance, eDiscovery, supervision |
| 4 | 2.1 DLP Policies | None | Data protection across all surfaces |
| 5 | 2.2 Sensitivity Labels | None | DLP effectiveness, auto-labeling |
| 6 | 3.2 Retention Policies | 3.1 | Regulatory record preservation |
| 7 | 3.4 Communication Compliance | 3.1 | FINRA 2210, supervisory review |
| 8 | 3.6 Supervisory Review | 3.4 | FINRA 3110 compliance |

### Implementation Dependencies

```
+------------------------------------------------------------------+
|                CONTROL IMPLEMENTATION DEPENDENCIES                  |
|                                                                    |
|  1.1 Oversharing -----> 1.2 Permissions -----> Copilot Enabled   |
|  Assessment              Remediation                               |
|                                                                    |
|  2.2 Sensitivity -----> 2.3 Auto-Labeling                        |
|  Labels                                                            |
|                                                                    |
|  3.1 Audit Logging --+--> 3.2 Retention                          |
|                       +--> 3.3 eDiscovery                         |
|                       +--> 3.4 Communication Compliance           |
|                       +--> 3.6 Supervisory Review                 |
|                                                                    |
|  2.1 DLP Policies -----> 2.10 Endpoint DLP                       |
|                                                                    |
|  4.1 Feature Toggles --> 4.2 Per-App Controls                    |
|                                                                    |
+------------------------------------------------------------------+
```

---

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Deploying Copilot Before Fixing Oversharing

**Risk:** Copilot amplifies oversharing at scale. Users discover sensitive content they were never intended to see.

**How to avoid:** Complete oversharing assessment (Control 1.1) and remediation (Control 1.2) as non-negotiable prerequisites. Do not skip Phase 0.

### Pitfall 2: No Communication Compliance Monitoring

**Risk:** Copilot-drafted customer emails are sent without review, potentially violating FINRA Rule 2210.

**How to avoid:** Implement communication compliance monitoring (Control 3.4) and supervisory review (Control 3.6) before pilot users begin using Copilot in Outlook.

### Pitfall 3: Enabling Web Search Without Assessment

**Risk:** Copilot sends search queries containing sensitive context (client names, deal terms) to Bing.

**How to avoid:** Make an explicit, documented decision about web search (Control 2.7) based on your governance level. Default to disabled for Regulated environments.

### Pitfall 4: Ignoring Teams Meeting Transcription

**Risk:** Meeting transcriptions are indexed by the Semantic Index, making all spoken content searchable by Copilot.

**How to avoid:** Assess meeting transcription policies (Control 1.5) in Phase 0. Consider disabling transcription for sensitive meetings or restricting transcript access.

### Pitfall 5: No Retention Policy for Copilot Interactions

**Risk:** Copilot interaction logs are deleted by default retention settings, failing to meet SEC 17a-4 or FINRA 4511 obligations.

**How to avoid:** Configure Copilot-specific retention policies (Control 3.2) in Phase 0 before enabling Copilot.

### Pitfall 6: Treating Copilot Governance as a One-Time Project

**Risk:** Controls degrade over time as Microsoft updates Copilot, new features are released, and permission sprawl resumes.

**How to avoid:** Establish steady-state governance operations (monthly committee, quarterly review, change management) in Phase 2.

### Pitfall 7: Not Training Users on FSI-Specific Restrictions

**Risk:** Users use Copilot for prohibited activities (generating customer recommendations without review, sharing Copilot outputs with clients directly).

**How to avoid:** Develop FSI-specific Copilot usage guidelines and train all users before enablement (Control 4.13).

### Pitfall 8: Skipping the Pilot

**Risk:** Deploying Copilot broadly without understanding organizational-specific governance gaps, DLP false positive rates, or communication compliance volume.

**How to avoid:** Always run a 30-day pilot (Phase 1) with a controlled group before expansion.

---

## Resource Planning

### Estimated Effort by Phase

| Phase | M365 Admin | Compliance | Security | AI Gov Lead | SharePoint Admin |
|-------|------------|------------|----------|-------------|------------------|
| Phase 0 | 30-40 hours | 15-20 hours | 10-15 hours | 40-50 hours | 30-40 hours |
| Phase 1 | 20-30 hours | 30-40 hours | 15-20 hours | 30-40 hours | 10-15 hours |
| Phase 2 | 30-40 hours | 25-35 hours | 25-35 hours | 30-40 hours | 15-20 hours |

### Ongoing Operations (Post-Phase 2)

| Activity | Frequency | Estimated Effort |
|----------|-----------|------------------|
| Governance committee meeting | Monthly | 4-6 hours preparation + meeting |
| Communication compliance review | Weekly | 2-4 hours |
| DLP alert review | Weekly | 2-4 hours |
| Usage analytics review | Weekly | 1-2 hours |
| Access review campaigns | Quarterly | 8-16 hours |
| Quarterly compliance review | Quarterly | 8-12 hours |
| Annual governance assessment | Annual | 40-60 hours |

---

## Governance Review Checkpoints

| Checkpoint | Timing | Focus | Participants |
|------------|--------|-------|--------------|
| Phase 0 Review | Day 30 | Foundation readiness, pilot go/no-go | AI Gov Lead, SharePoint Admin, Compliance, CISO |
| Phase 1 Midpoint | Day 45 | Pilot health check, early findings | AI Gov Lead, Compliance, M365 Admin |
| Phase 1 Review | Day 60 | Pilot results, expansion go/no-go | Governance Committee |
| Phase 2 Midpoint | Day 75 | Expansion health, advanced controls progress | AI Gov Lead, Compliance |
| Phase 2 Review | Day 90 | Steady-state readiness, examination readiness | Governance Committee + Executive Sponsor |
| First Annual Review | Day 365 | Full governance assessment, program effectiveness | Governance Committee + Board/Audit Committee |

---

## Next Steps

1. **Assess current state** -- Review existing M365 governance maturity (permissions, labels, DLP, audit)
2. **Assign accountability** -- Identify the AI Governance Lead and secure executive sponsorship
3. **Secure budget** -- Obtain licensing (Copilot, SharePoint Advanced Management) and staffing commitments
4. **Customize timeline** -- Adapt phases based on organizational priorities and regulatory obligations
5. **Begin Phase 0** -- Start with oversharing assessment and governance committee formation

---

*FSI Copilot Governance Framework v1.2.1 - March 2026*
