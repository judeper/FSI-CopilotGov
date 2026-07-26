# Control 1.1: Copilot Readiness Assessment and Data Hygiene — Portal Walkthrough

Step-by-step portal configuration for evaluating organizational readiness and establishing data hygiene baselines before M365 Copilot deployment.

## Prerequisites

- Entra Global Admin or Security Administrator role
- Microsoft 365 E5 or E3 + Security add-on license
- Access to Microsoft 365 Admin Center and Microsoft Purview portal
- SharePoint Admin role for site-level assessment

## Steps

### Step 1: Run the Microsoft 365 Copilot Readiness Report

**Portal:** Microsoft 365 admin center
**Path:** Reports > Usage > Microsoft 365 Copilot > Readiness

Open the **Readiness** tab of the Microsoft 365 Copilot report. It shows:

- **Total prerequisite licenses:** Users who hold, or can be assigned, a Copilot-eligible base license
- **Users on an eligible update channel:** Users enrolled in Current Channel or Monthly Enterprise Channel for Microsoft 365 Apps updates
- **Assigned and available Copilot licenses**, with recommended action cards such as moving users to a monthly update channel

Network readiness is assessed separately with the **Microsoft 365 network connectivity test tool** (`connectivity.m365.cloud.microsoft`), which measures average latency to Microsoft 365 Copilot endpoints (latency above 250 ms may degrade the Copilot experience) and confirms WebSocket (WSS) connectivity to `*.cloud.microsoft` and `*.office.com`. Aggregated network insights are also available in the Microsoft 365 admin center under **Health > Connectivity**.

Review each category and address any findings flagged as blocking before assigning Copilot licenses. Document the assessment results for your regulatory examination file.

### Step 2: Review Data Oversharing Report

**Portal:** Microsoft Purview
**Path:** Purview portal > Solutions > DSPM > Discover > Data risk assessments

Open the default data risk assessment, which runs weekly against the top 100 SharePoint sites by usage. This assessment identifies SharePoint and OneDrive locations where sensitive content may be accessible to users who should not have access. Create a custom assessment to target specific users or sites.

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
- Readiness report results (license eligibility, update channel eligibility) and network connectivity test results
- Overall readiness score from the Copilot dashboard
- Count of overshared sites requiring remediation
- Sensitivity label coverage percentage
- Permission model exceptions requiring attention

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Review the Copilot readiness report and network connectivity test results, and address infrastructure findings. Run readiness assessment and remediate all critical oversharing findings before pilot |
| **Recommended** | Achieve >75% sensitivity label coverage (per Control 1.1 scoring model), resolve all high-risk permission anomalies, and achieve >95% update channel eligibility |
| **Regulated** | Require governance committee sign-off on readiness report with documented remediation plan for all findings, including update channel policy enforcement |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated assessment scripts
- See [Verification & Testing](verification-testing.md) to validate readiness criteria
- Review [Control 1.2: SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) for detailed oversharing detection procedures
- Back to [Control 1.1: Copilot Readiness Assessment](../../../controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md)
