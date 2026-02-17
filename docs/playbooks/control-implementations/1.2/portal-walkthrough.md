# Control 1.2: SharePoint Oversharing Detection (DSPM for AI) — Portal Walkthrough

Step-by-step portal configuration for deploying Data Security Posture Management for AI to detect and remediate SharePoint oversharing before Copilot deployment.

## Prerequisites

- Microsoft Purview administrator or Compliance Administrator role
- Microsoft 365 E5 or E5 Compliance add-on license
- SharePoint Administrator role for site-level remediation
- DSPM for AI feature enabled in the tenant

## Steps

### Step 1: Enable DSPM for AI

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Overview > Get Started

Navigate to the DSPM for AI module and activate the service if not already enabled. The initial activation triggers a tenant-wide scan of SharePoint Online sites, OneDrive for Business locations, and Teams-connected file storage.

Accept the terms and initiate the first assessment. The initial scan typically takes 24-48 hours depending on tenant size.

### Step 2: Review Oversharing Assessment Results

**Portal:** Microsoft Purview
**Path:** Purview > DSPM for AI > Assessments > Oversharing

Once the scan completes, review the oversharing assessment dashboard. The report categorizes findings by risk level:

- **Critical:** Sites with sensitive content accessible to "Everyone except external users" or broader
- **High:** Sites with sensitive labeled content shared with large security groups (100+ members)
- **Medium:** Sites with potential sensitive content and permissive sharing settings
- **Low:** Sites with minor sharing concerns requiring review

Filter by risk level and focus remediation on Critical and High findings first.

### Step 3: Investigate Individual Site Findings

**Portal:** Microsoft Purview
**Path:** Purview > DSPM for AI > Assessments > Oversharing > [Select finding]

For each flagged site, review the detailed finding that includes:
- Which sensitive content was detected and its classification
- Current permission model and sharing configuration
- Which users or groups have access beyond their need-to-know
- Recommended remediation actions

Document each finding with business justification for current access or mark for remediation.

### Step 4: Configure Oversharing Policies

**Portal:** Microsoft Purview
**Path:** Purview > DSPM for AI > Policies > Create Policy

Create automated policies to detect future oversharing. Configure policy conditions:
- Content contains sensitivity labels at Confidential level or above
- Site sharing capability set to "Anyone" or "Organization-wide"
- Files shared with more than 50 unique users

Set policy actions to alert compliance administrators and optionally restrict further sharing.

### Step 5: Set Up Alerts and Monitoring

**Portal:** Microsoft Purview
**Path:** Purview > DSPM for AI > Alerts

Configure alert thresholds for ongoing monitoring. Set up email notifications to the governance team when new oversharing instances are detected. Recommended alert frequency is daily digest for medium-risk and immediate notification for critical findings.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable DSPM for AI and remediate all Critical findings before Copilot pilot |
| **Recommended** | Remediate Critical and High findings; implement automated oversharing policies |
| **Regulated** | Remediate all findings; require governance approval for any exceptions; continuous monitoring with SLA-based remediation |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated oversharing detection scripts
- See [Verification & Testing](verification-testing.md) to validate remediation completeness
- Review Control 1.3 for Restricted SharePoint Search as a complementary control
