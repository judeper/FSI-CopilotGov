# Control 1.2: SharePoint Oversharing Detection (DSPM) — Portal Walkthrough

Step-by-step portal configuration for deploying Microsoft Purview Data Security Posture Management (DSPM) to detect and remediate SharePoint oversharing before and during Copilot deployment.

## Prerequisites

- Purview Compliance Admin role, Data Security Management role group, or Data Security AI Admins role group (Purview Data Security AI Admin role) for DSPM setup and remediation configuration
- Purview Data Security AI Viewer, Data Security Viewers role group, or Data Security Viewer role for read-only DSPM reporting
- Microsoft 365 E5 or Purview Suite (formerly E5 Compliance) add-on license
- SharePoint Admin role for site-level remediation
- Current Data Security Posture Management enabled in the tenant

## Access Paths

DSPM is accessible from these current entry points:

| Path | Use Case |
|------|----------|
| **Microsoft Purview portal > Solutions > DSPM** (`https://purview.microsoft.com/datasecurityposturemanagement`) | Current full DSPM experience — AI hub, reports, oversharing assessments, recommendations, AI observability, Data Security Posture Agent, and item-level remediation |
| **Microsoft Purview portal > AI hub** (`https://purview.microsoft.com/aihub`) | Shortcut to AI-focused DSPM reporting, including **Reports > Oversharing assessments** and AI observability |
| **Microsoft 365 Admin Center > Copilot > Security** | Quick access to Copilot-specific security controls and links to Purview DSPM |

## Steps

### Step 1: Open Current DSPM

**Portal:** Microsoft Purview portal
**Path:** Solutions > DSPM (direct: `https://purview.microsoft.com/datasecurityposturemanagement`)

Navigate to the current Data Security Posture Management solution and complete any first-use setup tasks if they are not already enabled. The initial activation triggers a tenant-wide scan of SharePoint Online sites, OneDrive for Business locations, and Teams-connected file storage.

Accept the terms and initiate the first assessment. The initial scan typically takes 24-48 hours depending on tenant size.

### Step 2: Review Oversharing Assessment Results

**Portal:** Microsoft Purview portal
**Path:** AI hub > Reports > Oversharing assessments (or DSPM > Discover > Data risk assessments in unified navigation)

Once the scan completes, review the oversharing assessment dashboard. Current assessments surface per-site findings, including Everyone Except External Users (EEEU) access, broad sharing links, sensitivity-label context, and the remediation backlog. The report categorizes findings by risk level:

- **Critical:** Sites with sensitive content accessible to EEEU, "Everyone," anonymous links, or broader access
- **High:** Sites with sensitive labeled content shared with large security groups (100+ members)
- **Medium:** Sites with potential sensitive content and permissive sharing settings
- **Low:** Sites with minor sharing concerns requiring review

Filter by risk level and focus remediation on Critical and High findings first.

### Step 3: Use Item-Level Remediation for Critical Findings

**Portal:** Microsoft Purview portal
**Path:** AI hub > Reports > Oversharing assessments > [Select site or finding]

For high-priority findings, use item-level remediation to address individual files or items without requiring site-wide permission changes:

1. Select a Critical or High site or item finding from the oversharing assessment
2. Review the detailed finding showing which specific files contain sensitive content with overly broad access
3. Select individual items and apply remediation actions (restrict access, apply sensitivity label, remove sharing link)
4. Verify the remediation without disrupting access to the broader site

Item-level remediation is particularly valuable for sites where broad access is legitimate but specific sensitive files need to be protected.

### Step 4: Review AI Interaction Signals and Separately Govern Shadow AI

**Portal:** Microsoft Purview portal / Microsoft Defender portal
**Path:** Purview > Solutions > DSPM > AI observability; Discover > Activity explorer > AI activities; Defender > Cloud Apps > Cloud app catalog

Use DSPM for AI activity and interaction evidence, and use Microsoft Defender for Cloud Apps for Shadow AI app discovery:

1. Open **AI observability** and review AI apps and agents active in the last 30 days
2. Open **Discover > Activity explorer > AI activities** and review sensitive AI interactions
3. Do not treat DSPM AI observability or **Apps and agents** as Shadow AI discovery. For third-party AI app discovery, follow [Microsoft's Defender for Cloud Apps guidance](https://learn.microsoft.com/en-us/purview/deploymentmodels/depmod-data-leak-shadow-ai-step1): open **Cloud Apps** > **Cloud app catalog**, filter **App category** to **Generative AI**, review risk and usage details, and tag apps **Sanctioned** or **Unsanctioned**.
4. Record the prerequisite for every Purview signal used: auditing for Microsoft 365 Copilot interactions; device onboarding for sensitive-data visibility and endpoint DLP on third-party AI sites; an Edge configuration policy for Browser Data Security; and the Microsoft Purview browser extension on Windows users for Insider Risk Management site-visit detection. See [DSPM for AI prerequisites](https://learn.microsoft.com/en-us/purview/dspm-for-ai-considerations).
5. Document the review, classification, and escalation process, identifying whether each finding came from Defender discovery or Purview interaction evidence.

### Step 5: Use Recommendations for Remediation Actions

**Portal:** Microsoft Purview portal
**Path:** Data Security Posture Management > Recommendations (or Tasks and actions > Remediation actions)

Use Recommendations to create or update remediation actions for future oversharing. Prioritize actions that:
- Restrict Copilot access by sensitivity label for Confidential content or above
- Reduce site sharing capability from "Anyone" or organization-wide access to targeted groups
- Create DLP, auto-labeling, retention, or SharePoint Restricted Content Discovery actions for overshared sites
- Track remediation owners, status, and exceptions in the backlog

Set policy actions to alert compliance administrators and optionally restrict further sharing.

### Step 6: Use Data Security Posture Agent for Data Risk Investigation (Recommended and Regulated)

**Portal:** Microsoft Purview portal
**Path:** Data Security Posture Management > Asset explorer > Agent

The Data Security Posture Agent enables natural language investigation of data risks across Microsoft 365 and Copilot interactions without requiring pre-defined sensitive information types:

1. Access the Agent tab from Asset explorer in the DSPM navigation
2. Enter natural language queries to investigate specific data exposure risks
3. Review findings and export results for compliance documentation

### Step 7: Set Up Alerts and Monitoring

**Portal:** Microsoft Purview portal
**Path:** Data Security Posture Management > Reports and Recommendations

Configure monitoring and notification cadence for ongoing oversight. Set up email notifications to the governance team when new oversharing instances are detected. Recommended alert frequency is daily digest for medium-risk and immediate notification for critical findings. Route Microsoft Defender for Cloud Apps Generative AI discovery findings through a separate governance review queue; do not represent that queue as a DSPM Shadow AI feature.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable current DSPM and remediate all Critical findings before Copilot pilot. Use Microsoft Defender for Cloud Apps Cloud Discovery and the Generative AI cloud app catalog for Shadow AI discovery |
| **Recommended** | Remediate Critical and High findings; implement Recommendations-based remediation actions; configure AI observability and Data Security Posture Agent, documenting the prerequisites for selected third-party AI interaction signals |
| **Regulated** | Remediate all findings; use item-level remediation for surgical fixes; require governance approval for any exceptions; continuous monitoring with SLA-based remediation; full AI observability alerting |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated oversharing detection scripts
- See [Verification & Testing](verification-testing.md) to validate remediation completeness
- Review [Control 1.3: Restricted SharePoint Search](../../../controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md) for Restricted Content Discovery as a complementary control
- Back to [Control 1.2: SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md)
