# Phase 0: Governance Setup (Days 0-30)

Establish governance foundations, assess data hygiene, and configure baseline controls before deploying M365 Copilot to any users.

!!! warning "Disclaimer"
    This playbook is provided for informational purposes only and does not constitute legal or regulatory advice. Consult legal counsel for specific compliance requirements.

---

## Objective

Complete all prerequisite governance, security, and compliance steps so that the organization is ready for a controlled Copilot pilot. No Copilot licenses are assigned to end users during Phase 0.

---

## Week-by-Week Timeline

### Week 1: Governance Foundation

| Day | Activity | Owner |
|-----|----------|-------|
| 1-2 | Establish AI Governance Committee (Step 1) | Executive Sponsor |
| 3-4 | Define committee charter, roles, and meeting cadence | AI Governance Lead |
| 5 | Conduct initial stakeholder briefing on Copilot governance requirements | AI Governance Lead |

### Week 2: Data Assessment

| Day | Activity | Owner |
|-----|----------|-------|
| 6-7 | Run DSPM for AI oversharing assessment (Step 2) | Purview Compliance Admin |
| 8-9 | Review oversharing findings and prioritize remediation | Security Lead |
| 10 | Begin SharePoint permission remediation for critical sites | SharePoint Admin |

### Week 3: Policy Configuration

| Day | Activity | Owner |
|-----|----------|-------|
| 11-12 | Implement baseline DLP policies for Copilot (Step 3) | Purview Compliance Admin |
| 13-14 | Enable Purview Unified Audit Log for Copilot events (Step 4) | M365 Global Admin |
| 15 | Review and update sensitivity label taxonomy (Step 5) | Information Protection Lead |

### Week 4: Technical Readiness

| Day | Activity | Owner |
|-----|----------|-------|
| 16-17 | Configure per-app Copilot toggles in M365 Admin Center (Step 6) | M365 Global Admin |
| 18-19 | Assign pilot group licenses and validate technical configuration (Step 7) | M365 Global Admin |
| 20 | Phase 0 governance review and sign-off | AI Governance Committee |

---

## Steps

### Step 1: Establish AI Governance Committee

**Why:** A governance committee provides oversight, accountability, and decision-making authority for Copilot deployment. Regulatory bodies (FINRA, OCC, FFIEC) expect documented governance structures for new technology adoption.

**Actions:**

1. **Identify committee members** -- include at minimum:
    - Executive sponsor (CTO, CIO, or COO)
    - CISO or Security Lead
    - Chief Compliance Officer or Compliance Lead
    - AI Governance Lead (may be a new role)
    - Legal representative
    - Business unit representatives from pilot departments
    - M365 Global Administrator

2. **Draft committee charter** documenting:
    - Purpose and scope (M365 Copilot governance decisions)
    - Meeting cadence (weekly during deployment phases, monthly at steady-state)
    - Decision authority (what requires committee approval vs. delegated authority)
    - Escalation procedures
    - Reporting obligations

3. **Schedule recurring meetings** -- weekly during Phase 0-2, transitioning to monthly after steady-state

4. **Create governance artifacts repository** -- designate a SharePoint site for committee meeting minutes, decision logs, and governance documentation

**Deliverable:** Signed committee charter with named members and defined responsibilities

---

### Step 2: Run DSPM for AI Oversharing Assessment

**Why:** Data Security Posture Management (DSPM) for AI identifies content that may be overshared relative to its sensitivity. Copilot respects existing permissions, so overshared content becomes accessible through Copilot interactions.

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > AI Security > Oversharing Assessment

**Actions:**

1. **Navigate to DSPM for AI** in the Purview portal and initiate an oversharing assessment
2. **Review assessment results** -- focus on:
    - SharePoint sites with "Everyone except external users" permissions containing sensitive data
    - Sites with broken inheritance where permissions are broader than intended
    - OneDrive locations shared broadly within the organization
    - Teams channels with overly permissive membership relative to content sensitivity
3. **Categorize findings** by risk level:
    - **Critical:** Regulated data (PII, financial records, NPI) accessible organization-wide
    - **High:** Confidential business data with excessive sharing
    - **Medium:** Internal data with sharing broader than necessary
    - **Low:** General content with minor permission anomalies
4. **Create remediation plan** for Critical and High findings -- these must be resolved before pilot
5. **Export assessment report** for governance committee review

**Deliverable:** DSPM assessment report with categorized findings and remediation plan

!!! tip "Remediation Priority"
    Focus remediation on sites and content that pilot users will have access to. Organization-wide remediation can continue in parallel during Phase 1, but pilot-scoped sites must be clean before license assignment.

See also: [Control 1.2 -- SharePoint Oversharing Detection](../control-implementations/1.2/portal-walkthrough.md)

---

### Step 3: Implement Baseline DLP Policies for Copilot

**Why:** Data Loss Prevention policies help prevent Copilot from surfacing or generating content that violates data handling rules. Baseline DLP policies should cover the most common FSI data types.

**Portal:** Microsoft Purview
**Path:** Purview > Data Loss Prevention > Policies

**Actions:**

1. **Review existing DLP policies** -- identify which policies already apply to Exchange, SharePoint, OneDrive, and Teams. Confirm that the "Microsoft 365 Copilot" location is available and enabled.

2. **Create or update DLP policies** covering at minimum:
    - **Financial data:** Account numbers, routing numbers, credit card numbers
    - **Personal data:** SSNs, driver's license numbers, passport numbers
    - **Regulatory data:** Non-public information (NPI) per Regulation S-P
    - **Custom sensitive information types** specific to your organization

3. **Configure policy actions for Copilot:**
    - Block Copilot from processing content matching high-confidence sensitive information types
    - Show policy tips to users when Copilot references content matching medium-confidence patterns
    - Log all DLP matches in Copilot interactions to the Unified Audit Log

4. **Set policies to test mode initially** -- run in simulation for at least 5 business days to evaluate false positive rates before enforcement

5. **Review simulation results** and tune sensitivity thresholds before enabling enforcement

**Deliverable:** DLP policies configured and tested for Copilot location with documented false positive analysis

See also: [Control 2.1 -- DLP Policies for M365 Copilot](../control-implementations/2.1/portal-walkthrough.md)

---

### Step 4: Enable Purview Unified Audit Log for Copilot Events

**Why:** Audit logging captures Copilot interaction events for compliance, investigation, and regulatory examination purposes. FINRA Rule 4511 and SEC Rule 17a-4 require record preservation, and Copilot interaction logs may constitute business records.

**Portal:** Microsoft Purview
**Path:** Purview > Audit > Audit Search

**Actions:**

1. **Verify Unified Audit Log is enabled** -- navigate to Purview Audit and confirm audit logging is active. If not, enable it (changes may take up to 24 hours to take effect).

2. **Confirm Copilot event types are captured:**
    - `CopilotInteraction` -- user interactions with Copilot across M365 apps
    - `MicrosoftCopilotForM365` -- Copilot-specific activity events
    - Search for these event types in the Audit Search to verify they appear

3. **Configure audit log retention:**
    - Default retention is 180 days (E5) or 90 days (E3)
    - For FSI organizations, configure extended retention of at least 3 years (aligning with SEC 17a-4(b)(4) for communications)
    - Consider 7-year retention if Copilot outputs may become part of financial records

4. **Set up audit log export** to a long-term storage solution if retention beyond the native limit is required

5. **Test audit log search** -- have a licensed admin interact with Copilot and verify the event appears in the audit log within the expected latency window

**Deliverable:** Audit logging confirmed active with Copilot events captured and retention period documented

See also: [Control 3.1 -- Copilot Audit Logging](../control-implementations/3.1/portal-walkthrough.md)

---

### Step 5: Review and Update Sensitivity Label Taxonomy

**Why:** Sensitivity labels govern how Copilot handles classified content. Copilot inherits the highest sensitivity label from source content when generating outputs. A well-structured label taxonomy supports appropriate content handling.

**Portal:** Microsoft Purview
**Path:** Purview > Information Protection > Labels

**Actions:**

1. **Review current label taxonomy** and evaluate adequacy for Copilot:
    - Do labels cover all FSI data classification tiers (Public, Internal, Confidential, Highly Confidential, Restricted)?
    - Are auto-labeling policies configured for common sensitive content?
    - Do label policies restrict sharing appropriately at each tier?

2. **Evaluate Copilot-specific label behaviors:**
    - Labels with encryption: Copilot can access encrypted content only if the user has decryption rights
    - Labels with "Do not forward" or "Encrypt-only": These restrictions carry forward to Copilot-generated content
    - Labels scoped to specific groups: Copilot respects group-scoped label access

3. **Update taxonomy if gaps are identified:**
    - Add labels for AI-specific scenarios if needed (e.g., "AI Training Data -- Restricted")
    - Configure auto-labeling policies for financial document types
    - Set default labels for SharePoint document libraries containing sensitive content

4. **Measure label coverage** -- target a minimum of 85% label coverage across SharePoint and OneDrive content before pilot deployment

**Deliverable:** Updated sensitivity label taxonomy documentation with coverage metrics

See also: [Control 1.5 -- Sensitivity Label Taxonomy Review](../control-implementations/1.5/portal-walkthrough.md)

---

### Step 6: Configure Per-App Copilot Toggles in M365 Admin Center

**Why:** M365 Admin Center provides granular toggles to enable or disable Copilot capabilities on a per-application basis. During Phase 0, configure toggles to match the approved pilot scope.

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings

**Actions:**

1. **Review available Copilot toggles** for each M365 application:
    - Word, Excel, PowerPoint, Outlook, Teams, OneNote, Loop, Whiteboard, Forms, Planner
    - Microsoft 365 Copilot Chat
    - Copilot Pages
    - Web search / web grounding

2. **Determine which applications to enable for pilot:**
    - Start with lower-risk applications (Word, Excel, PowerPoint) for initial pilot
    - Defer higher-risk applications (Microsoft 365 Copilot Chat, Copilot Pages) until DLP and information barrier controls are validated
    - Disable web search grounding if external data sourcing is a compliance concern

3. **Configure toggles according to governance committee decisions**

4. **Document the configuration** including rationale for each toggle setting

**Deliverable:** Per-app toggle configuration document with governance committee approval

See also: [Control 4.1 -- Admin Settings and Feature Management](../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md)

---

### Step 7: Assign Pilot Group Licenses

**Why:** License assignment controls who can use Copilot. Phase 0 assigns licenses only to the pilot group defined by the governance committee.

**Portal:** Microsoft 365 Admin Center / Microsoft Entra Admin Center
**Path:** Admin Center > Users > Active Users (or Entra ID group-based licensing)

**Actions:**

1. **Create a pilot group** in Entra ID:
    - Security group recommended (not Microsoft 365 group)
    - Name clearly: e.g., `SG-Copilot-Pilot-Phase1`
    - Size: 25-50 users from approved pilot departments
    - Include a mix of roles: analysts, advisors, managers, compliance staff

2. **Select pilot participants** based on:
    - Department readiness (data hygiene remediation complete for their content)
    - Willingness to provide feedback
    - Representation across business functions
    - Include at least 2-3 compliance or risk team members for monitoring validation

3. **Assign M365 Copilot licenses** via group-based licensing:
    - Navigate to Entra ID > Groups > `SG-Copilot-Pilot-Phase1` > Licenses
    - Assign the Microsoft 365 Copilot license
    - Verify license assignment status shows no errors

4. **Verify pilot readiness:**
    - Confirm all pilot users have completed Copilot training (see Control 1.12)
    - Validate that DLP policies are enforced for pilot user content
    - Confirm sensitivity labels are applied to pilot department content
    - Test Copilot access for 2-3 pilot users before full pilot launch

**Deliverable:** Licensed pilot group with verified access and documented participant list

---

## Phase 0 Deliverables Checklist

| # | Deliverable | Status |
|---|-------------|--------|
| 1 | Signed AI Governance Committee charter | [ ] |
| 2 | DSPM oversharing assessment report with remediation plan | [ ] |
| 3 | Critical and High oversharing findings remediated | [ ] |
| 4 | DLP policies configured and tested for Copilot | [ ] |
| 5 | Unified Audit Log enabled with Copilot events confirmed | [ ] |
| 6 | Audit log retention configured (minimum 3 years) | [ ] |
| 7 | Sensitivity label taxonomy reviewed and updated | [ ] |
| 8 | Label coverage at or above 85% for pilot scope | [ ] |
| 9 | Per-app Copilot toggles configured per governance decisions | [ ] |
| 10 | Pilot group created and licenses assigned | [ ] |
| 11 | Pilot users completed Copilot training | [ ] |
| 12 | Governance committee sign-off on Phase 0 completion | [ ] |

---

## Success Criteria

Phase 0 is complete when:

- [ ] AI Governance Committee is established with signed charter
- [ ] DSPM oversharing assessment completed with all Critical/High findings remediated
- [ ] Baseline DLP policies are enforced for Copilot interactions
- [ ] Unified Audit Log captures Copilot events with appropriate retention
- [ ] Sensitivity label coverage meets the 85% threshold for pilot scope
- [ ] Per-app toggles are configured and documented
- [ ] Pilot group is licensed with all participants trained
- [ ] Governance committee has formally approved Phase 1 launch

---

## Next Steps

- Proceed to [Phase 1 -- Pilot Deployment](phase-1-pilot-deployment.md) for controlled rollout
- Reference the [Governance Operating Calendar](../governance-operations/governance-operating-calendar.md) for ongoing governance activities
- Review the [RACI Template](../governance-operations/raci-governance-template.md) for responsibility assignments

---

*FSI Copilot Governance Framework v1.1 -- February 2026*
