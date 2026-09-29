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
| **Microsoft Purview portal > Solutions > DSPM** (`https://purview.microsoft.com/datasecurityposturemanagement`) | Current full DSPM experience — data risk assessments, recommendations, AI observability, Data Security Posture Agent, and item-level remediation |
| **Microsoft Purview portal > AI hub** (`https://purview.microsoft.com/aihub`) | AI-focused shortcut that can surface related DSPM insights, but current oversharing workflows are documented under **DSPM > Discover > Data risk assessments** |
| **Microsoft 365 Admin Center > Copilot > Security** | Quick access to Copilot-specific security controls and links to Purview DSPM |

## Steps

### Step 1: Open Current DSPM

**Portal:** Microsoft Purview portal
**Path:** Solutions > DSPM (direct: `https://purview.microsoft.com/datasecurityposturemanagement`)

Navigate to the current Data Security Posture Management solution and complete any first-use setup tasks if they are not already enabled. The initial activation triggers a tenant-wide scan of SharePoint Online sites, OneDrive for Business locations, and Teams-connected file storage.

Accept the terms and initiate the first assessment. Microsoft documents two separate timing expectations: allow roughly a day before tenant data is available to act on, and expect the **first default assessment** to have a **four-day delay** before results display. For **custom assessments**, wait at least **48 hours** after the assessment completes before reviewing results.

### Step 2: Review Oversharing Assessment Results

**Portal:** Microsoft Purview portal
**Path:** DSPM > Discover > Data risk assessments

Once the scan completes, review the oversharing assessment dashboard. Current assessments surface per-site findings, including Everyone Except External Users (EEEU) access, broad sharing links, sensitivity-label context, and the remediation backlog. The report categorizes findings by risk level:

- **Critical:** Sites with sensitive content accessible to EEEU, "Everyone," anonymous links, or broader access
- **High:** Sites with sensitive labeled content shared with large security groups (100+ members)
- **Medium:** Sites with potential sensitive content and permissive sharing settings
- **Low:** Sites with minor sharing concerns requiring review

Filter by risk level and focus remediation on Critical and High findings first.

### Step 3: Use Item-Level Remediation for Critical Findings

**Portal:** Microsoft Purview portal
**Path:** DSPM > Discover > Data risk assessments > [Select assessment] > [Select site or finding]

For high-priority findings, use item-level remediation to address individual files or items without requiring site-wide permission changes:

1. Select a Critical or High site or item finding from the oversharing assessment
2. Review the detailed finding showing which specific files contain sensitive content with overly broad access
3. Select individual items and apply remediation actions (restrict access, apply sensitivity label, remove sharing link)
4. Verify the remediation without disrupting access to the broader site

Item-level remediation is particularly valuable for sites where broad access is legitimate but specific sensitive files need to be protected.

### Step 4: Review AI Observability and Evaluate the Shadow AI Preview Separately

**Portal:** Microsoft Purview portal
**Path:** Solutions > DSPM > AI observability

Configure **AI observability** in DSPM to monitor AI activity across Microsoft 365 Copilot and any third-party AI apps and agents in use:

1. Navigate to the AI observability section
2. Review the unified view of AI activity across all monitored AI surfaces
3. Review high-risk apps, sensitive interactions, and the per-agent policy coverage shown on the page
4. Route findings on unsanctioned or high-risk AI usage to the governance team for follow-up and remediation

If the organization separately opts into the **Frontier preview** and meets its prerequisites, review the distinct **Microsoft 365 admin center > Agents > Shadow AI** page for unmanaged standalone AI agents. Treat that Shadow AI experience as a separate preview workflow rather than as part of DSPM AI observability.

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

Microsoft Learn still documents the agent as preview. The Microsoft 365 roadmap entry now lists general availability from June 2026 and a launched status as of its August 10, 2026 update, so verify tenant availability before depending on the agent for operational controls.

### Step 7: Set Up Alerts and Monitoring

**Portal:** Microsoft Purview portal
**Path:** Data Security Posture Management > Reports and Recommendations

Configure monitoring and notification cadence for ongoing oversight. Set up email notifications to the governance team when new oversharing instances are detected. Recommended alert frequency is daily digest for medium-risk and immediate notification for critical findings. For AI observability, document how the team reviews high-risk apps, sensitive interactions, and agent findings. If the tenant also uses the separate Shadow AI preview, maintain a distinct review queue and prerequisite checklist for that preview surface.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable current DSPM and remediate all Critical findings before Copilot pilot. Review AI observability so the governance team can see current AI-app and agent activity. |
| **Recommended** | Remediate Critical and High findings; implement Recommendations-based remediation actions; configure AI observability review procedures and the Data Security Posture Agent. If the tenant uses the separate Shadow AI preview, document its prerequisites and governance owner separately. |
| **Regulated** | Remediate all findings; use item-level remediation for surgical fixes; require governance approval for any exceptions; continuous monitoring with SLA-based remediation; formal AI observability review with documented escalation criteria. Evaluate the Shadow AI preview only through a separate approved pilot with its own controls and evidence. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated oversharing detection scripts
- See [Verification & Testing](verification-testing.md) to validate remediation completeness
- Review [Control 1.3: Restricted SharePoint Search](../../../controls/pillar-1-readiness/1.3-restricted-sharepoint-search.md) for Restricted Content Discovery as a complementary control
- Back to [Control 1.2: SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md)
