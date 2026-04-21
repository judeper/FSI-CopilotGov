# Control 1.14: Item-Level Permission Scanning - Portal Walkthrough

Step-by-step portal workflow for selecting SharePoint sites, validating scope, and preparing governed item-level scanning for uniquely permissioned files and folders.

## Prerequisites

- Control [1.2 SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) has identified candidate sites.
- Control [1.7 SharePoint Advanced Management](../../../controls/pillar-1-readiness/1.7-sharepoint-advanced-management.md) is available if your organization uses Data Access Governance reports.
- SharePoint Admin or Purview Compliance Admin access.
- Reviewed companion solution [16-item-level-oversharing-scanner](https://github.com/judeper/FSI-CopilotGov-Solutions/tree/main/solutions/16-item-level-oversharing-scanner).
- Documented approval path for HIGH and CRITICAL remediation actions.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| Microsoft Purview | Data Security Posture Management > Assessments > Oversharing | Confirms which sites still warrant item-level analysis |
| SharePoint admin center | Reports > Data access governance | Helps identify high-risk sites, libraries, and owners |
| Microsoft Entra admin center | Groups and enterprise applications | Validates broad group access and ownership before remediation |

## Steps

### Step 1: Confirm the site-level baseline

Review DSPM and SharePoint Advanced Management findings for the sites you plan to scan. Record why each site is in scope and which owner or business unit approved the review.

### Step 2: Narrow the library and folder scope

In SharePoint, identify the libraries or folders most likely to contain uniquely permissioned content, such as deal rooms, legal workspaces, exception-based collaboration areas, and stale project folders.

### Step 3: Review inheritance cues before automation

Check whether the site or library already shows broken inheritance, broad sharing links, or large group-based access. This helps the automation team estimate scan size and likely remediation volume.

### Step 4: Prepare the remediation approval gate

Define who approves each remediation outcome:

- Site admin for operational cleanup
- Compliance lead for HIGH-risk items
- Business owner when remediation may affect active collaboration

### Step 5: Capture the scan manifest and handoff

Create a simple scan manifest containing site URL, targeted libraries, owner, approver, and expected cadence. This becomes the handoff input for the PowerShell workflow and the evidence package.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Scan only the highest-risk sites identified by Control 1.2 and require manual review of all HIGH findings. |
| **Recommended** | Use DSPM plus Data Access Governance to prioritize recurring scans for regulated business units and stale collaboration spaces. |
| **Regulated** | Maintain a documented scan manifest, named approvers, and evidence trail for every in-scope site and remediation decision. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to run the item-level scan and scoring workflow.
- Use [Verification & Testing](verification-testing.md) to validate that uniquely permissioned items are detected and triaged correctly.
- Keep [Troubleshooting](troubleshooting.md) available for scan coverage, throttling, and approval-path issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 1.14](../../../controls/pillar-1-readiness/1.14-item-level-permission-scanning.md)
