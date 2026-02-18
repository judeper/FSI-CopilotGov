# Control 1.2: SharePoint Oversharing Detection (DSPM) — Portal Walkthrough

Step-by-step portal configuration for deploying Microsoft Purview Data Security Posture Management (DSPM) to detect and remediate SharePoint oversharing before and during Copilot deployment.

## Prerequisites

- Microsoft Purview administrator or Compliance Administrator role
- Microsoft 365 E5 or E5 Compliance add-on license
- SharePoint Administrator role for site-level remediation
- DSPM feature enabled in the tenant

## Access Paths

DSPM is accessible from two locations:

| Path | Use Case |
|------|----------|
| **Microsoft Purview > Data Security Posture Management** | Full DSPM experience — oversharing assessments, AI observability, Purview Posture Agent, Shadow AI discovery, item-level remediation |
| **Microsoft 365 Admin Center > Copilot > Overview > Security tab** | Quick access to Copilot-specific security controls: default DLP policy status, Shadow AI findings summary, and links to Purview DSPM |

## Steps

### Step 1: Enable DSPM

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Overview > Get Started

Navigate to the DSPM module and activate the service if not already enabled. The initial activation triggers a tenant-wide scan of SharePoint Online sites, OneDrive for Business locations, and Teams-connected file storage.

Accept the terms and initiate the first assessment. The initial scan typically takes 24-48 hours depending on tenant size.

### Step 2: Review Oversharing Assessment Results

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Assessments > Oversharing

Once the scan completes, review the oversharing assessment dashboard. The report categorizes findings by risk level:

- **Critical:** Sites with sensitive content accessible to "Everyone except external users" or broader
- **High:** Sites with sensitive labeled content shared with large security groups (100+ members)
- **Medium:** Sites with potential sensitive content and permissive sharing settings
- **Low:** Sites with minor sharing concerns requiring review

Filter by risk level and focus remediation on Critical and High findings first.

### Step 3: Use Item-Level Remediation for Critical Findings

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Assessments > Oversharing > [Select finding]

For high-priority findings, use item-level remediation to address individual files or items without requiring site-wide permission changes:

1. Select a Critical or High finding from the oversharing assessment
2. Review the detailed finding showing which specific files contain sensitive content with overly broad access
3. Select individual items and apply remediation actions (restrict access, apply sensitivity label, remove sharing link)
4. Verify the remediation without disrupting access to the broader site

Item-level remediation is particularly valuable for sites where broad access is legitimate but specific sensitive files need to be protected.

### Step 4: Enable AI Observability and Shadow AI Discovery

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > AI Observability

Configure the unified AI observability view to monitor AI activity across Microsoft 365 Copilot and any third-party AI apps in use:

1. Navigate to the AI observability section
2. Review the unified view of AI activity across all monitored AI surfaces
3. Check **Shadow AI discovery** findings for unsanctioned AI tools detected in the organization
4. Configure alerts for new Shadow AI tool detections

**Quick access:** Microsoft 365 Admin Center > Copilot > Overview > Security tab shows a summary of Shadow AI findings and provides a link to the full Purview DSPM experience.

### Step 5: Configure Oversharing Policies

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Policies > Create Policy

Create automated policies to detect future oversharing. Configure policy conditions:
- Content contains sensitivity labels at Confidential level or above
- Site sharing capability set to "Anyone" or "Organization-wide"
- Files shared with more than 50 unique users

Set policy actions to alert compliance administrators and optionally restrict further sharing.

### Step 6: Use Purview Posture Agent for Data Risk Investigation (Recommended and Regulated)

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Posture Agent

The Purview Posture Agent (January 2026 preview) enables natural language investigation of data risks across M365 and Copilot interactions without requiring pre-defined sensitive information types:

1. Access the Posture Agent from the DSPM navigation
2. Enter natural language queries to investigate specific data exposure risks
3. Review findings and export results for compliance documentation

### Step 7: Set Up Alerts and Monitoring

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management > Alerts

Configure alert thresholds for ongoing monitoring. Set up email notifications to the governance team when new oversharing instances are detected. Recommended alert frequency is daily digest for medium-risk and immediate notification for critical findings. Configure separate alerts for Shadow AI tool detections.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable DSPM and remediate all Critical findings before Copilot pilot. Enable Shadow AI discovery |
| **Recommended** | Remediate Critical and High findings; implement automated oversharing policies; configure AI observability and Purview Posture Agent |
| **Regulated** | Remediate all findings; use item-level remediation for surgical fixes; require governance approval for any exceptions; continuous monitoring with SLA-based remediation; full AI observability alerting |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated oversharing detection scripts
- See [Verification & Testing](verification-testing.md) to validate remediation completeness
- Review Control 1.3 for Restricted SharePoint Search and Restricted Content Discovery as complementary controls
