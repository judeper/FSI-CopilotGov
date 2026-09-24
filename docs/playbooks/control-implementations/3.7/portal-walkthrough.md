# Control 3.7: Regulatory Reporting — Portal Walkthrough

Step-by-step portal configuration for establishing regulatory reporting capabilities that incorporate Copilot-generated data and AI governance metrics for financial regulatory submissions.

!!! note "Regulatory applicability"
    Regulatory citations identify commonly referenced requirements. Applicability, record classification, and retention periods are a firm and counsel determination; this framework does not assert that any regulation applies or is satisfied. See the [Regulatory Applicability Questions](../../../reference/regulatory-applicability-questions.md) appendix.

## Prerequisites

- **Role:** Purview Compliance Admin or Regulatory Reporting Officer
- **License:** Eligible Microsoft Purview/Communication Compliance licensing, such as Microsoft Purview Suite (formerly Microsoft 365 E5 Compliance), Office 365 E5, or Office 365 E3 with the Advanced Compliance add-on
- **Access:** Microsoft Purview portal, Microsoft 365 Admin Center

## Steps

### Step 1: Configure Compliance Manager Assessments for AI Governance

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Assessments

1. Navigate to Compliance Manager and review existing assessments.
2. Create or update assessments for regulatory frameworks that require AI disclosure:
   - FINRA AI usage reporting
   - SEC AI disclosure requirements
   - OCC supervisory reporting for model risk
3. Map Copilot governance controls to relevant assessment items.
4. Assign improvement actions to responsible teams.

### Step 2: Set Up Regulatory Report Data Sources

**Portal:** Microsoft Purview portal
**Path:** Solutions > Audit > Saved searches

1. Create saved audit log searches for data that feeds into regulatory reports:
   - Copilot interaction volume by business unit
   - Communication compliance review outcomes
   - Supervisory review statistics
   - DLP policy match counts related to Copilot content
2. Schedule these searches to run at the frequency matching your reporting cycle.

### Step 3: Configure Report Export Templates

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Reports

1. Create report templates for each regulatory submission that includes AI governance data.
2. Map data fields from Copilot audit logs and compliance metrics to report templates.
3. Include the following standard sections in each report:
   - AI tool inventory (Copilot features in use)
   - Governance control status (pass/fail per control)
   - Incident and exception summary
   - Supervisory review metrics

### Step 4: Establish Reporting Calendar

**Portal:** Microsoft 365 Admin Center
**Path:** Verify the current reporting-calendar location in the Microsoft 365 admin center or the firm's GRC tool; public Microsoft docs do not confirm a stable **Settings > Org settings > Compliance reporting** breadcrumb

1. Document the regulatory reporting calendar with deadlines:
   - FINRA internal supervisory-control report (FINRA Rule 3120; not a regulator filing) — annual
   - SEC Form ADV amendments (if applicable and confirmed with counsel) — annual/material changes
   - OCC supervisory reports — as required by examination
2. Set calendar reminders and assign report owners.
3. Create a pre-submission review workflow for each report.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Compliance Manager assessments | Annual review | Quarterly review | Continuous monitoring |
| AI governance reporting | Manual | Semi-automated | Automated data feeds |
| Report pre-submission review | Single reviewer | Dual review | Committee review |
| Reporting calendar automation | Manual tracking | Automated reminders | Integrated workflow |

## Regulatory Alignment

- **FINRA Rule 3120** — Provides evidence for internal annual supervisory-control report review to senior management; it is not itself a regulator filing
- **SEC Form ADV** — Potential advisory-disclosure review item for AI tool usage; applicability: confirm
- **OCC Bulletin 2026-13 / Federal Reserve SR 26-2 revised model-risk-management guidance** — Current model-risk governance reference; note that the 2026 guidance rescinds OCC Bulletin 2011-12 / supersedes SR 11-7 and states generative AI and agentic AI models are outside its scope

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated reporting scripts
- See [Verification & Testing](verification-testing.md) to validate reporting accuracy
- Back to [Control 3.7](../../../controls/pillar-3-compliance/3.7-regulatory-reporting.md)
