# Control 1.1: Copilot Readiness Assessment and Data Hygiene — Portal Walkthrough

Step-by-step portal configuration for evaluating organizational readiness and establishing data hygiene baselines before M365 Copilot deployment.

## Prerequisites

- Global Administrator or Security Administrator role
- Microsoft 365 E5 or E3 + Security add-on license
- Access to Microsoft 365 Admin Center and Microsoft Purview portal
- SharePoint Administrator role for site-level assessment

## Steps

### Step 1: Access the Microsoft 365 Copilot Readiness Dashboard

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Microsoft 365 Copilot > Readiness

Navigate to the Copilot readiness page to review the automated assessment results. This dashboard surfaces data hygiene concerns including overshared content, unlabeled sensitive documents, and permission anomalies across your tenant.

Review each category and note any items flagged as high-risk. These must be remediated before Copilot license assignment.

### Step 2: Review Data Oversharing Report

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Reports > Oversharing Assessment

Open the DSPM for AI oversharing assessment. This report identifies SharePoint sites, OneDrive locations, and Teams channels where sensitive content may be accessible to users who should not have access.

Filter results by sensitivity level and focus on sites containing financial data, PII, or regulated content. Export the report for governance committee review.

### Step 3: Evaluate Sensitivity Label Coverage

**Portal:** Microsoft Purview
**Path:** Purview > Information Protection > Label Analytics

Review label adoption metrics across the organization. For FSI environments, target a minimum of 85% label coverage on documents stored in SharePoint and OneDrive before enabling Copilot.

Document current coverage percentages by department and content type. Identify gaps where auto-labeling policies may be needed.

### Step 4: Assess Permission Model Health

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin > Sites > Active Sites > Sharing column

Review sharing settings across all active SharePoint sites. Identify sites configured with "Anyone" or "Organization-wide" sharing that contain sensitive financial data.

Flag sites where sharing settings are more permissive than the content sensitivity warrants.

### Step 5: Document Readiness Findings

Compile findings from Steps 1-4 into a readiness assessment report. Include:
- Overall readiness score from the Copilot dashboard
- Count of overshared sites requiring remediation
- Sensitivity label coverage percentage
- Permission model exceptions requiring attention

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Complete readiness assessment and remediate all critical oversharing findings before pilot |
| **Recommended** | Achieve 85% sensitivity label coverage and resolve all high-risk permission anomalies |
| **Regulated** | Require governance committee sign-off on readiness report with documented remediation plan for all findings |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated assessment scripts
- See [Verification & Testing](verification-testing.md) to validate readiness criteria
- Review Control 1.2 for detailed oversharing detection procedures
