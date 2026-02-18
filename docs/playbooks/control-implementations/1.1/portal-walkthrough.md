# Control 1.1: Copilot Readiness Assessment and Data Hygiene — Portal Walkthrough

Step-by-step portal configuration for evaluating organizational readiness and establishing data hygiene baselines before M365 Copilot deployment.

## Prerequisites

- Global Administrator or Security Administrator role
- Microsoft 365 E5 or E3 + Security add-on license
- Access to Microsoft 365 Admin Center and Microsoft Purview portal
- SharePoint Administrator role for site-level assessment

## Steps

### Step 1: Run the Microsoft 365 Copilot Optimization Assessment

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Health > Copilot readiness

Navigate to the Copilot readiness page to access the Optimization Assessment. This Microsoft-provided tool evaluates infrastructure readiness across three dimensions:

- **Network readiness:** Bandwidth, latency, and proxy/firewall compatibility with Copilot service endpoints
- **Office update channel compliance:** Percentage of endpoints on Current Channel or Monthly Enterprise Channel (required for Copilot features; Semi-Annual Enterprise Channel is not supported)
- **App compatibility:** Office add-ins and applications with known Copilot compatibility issues

Review each category and address any findings flagged as blocking before assigning Copilot licenses. Document the assessment results for your regulatory examination file.

### Step 2: Review Data Oversharing Report

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Reports > Oversharing Assessment

Open the DSPM oversharing assessment. This report identifies SharePoint sites, OneDrive locations, and Teams channels where sensitive content may be accessible to users who should not have access.

Filter results by sensitivity level and focus on sites containing financial data, PII, or regulated content. Export the report for governance committee review.

**Quick access alternative:** Microsoft 365 Admin Center > Copilot > Overview > Security tab provides access to key Copilot security controls and the default DLP policy status without navigating to the full Purview portal.

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
- Optimization Assessment results (network, update channel, app compatibility)
- Overall readiness score from the Copilot dashboard
- Count of overshared sites requiring remediation
- Sensitivity label coverage percentage
- Permission model exceptions requiring attention

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Complete Optimization Assessment and address infrastructure findings. Run readiness assessment and remediate all critical oversharing findings before pilot |
| **Recommended** | Achieve 85% sensitivity label coverage, resolve all high-risk permission anomalies, and achieve >95% update channel compliance |
| **Regulated** | Require governance committee sign-off on readiness report with documented remediation plan for all findings, including update channel policy enforcement |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated assessment scripts
- See [Verification & Testing](verification-testing.md) to validate readiness criteria
- Review Control 1.2 for detailed oversharing detection procedures
