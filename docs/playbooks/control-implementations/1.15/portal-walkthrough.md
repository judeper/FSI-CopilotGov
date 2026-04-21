# Control 1.15: SharePoint Permissions Drift Detection - Portal Walkthrough

Step-by-step governance workflow for establishing approved permission baselines, defining drift thresholds, and preparing escalation paths for SharePoint permissions drift detection.

## Prerequisites

- Control [1.2 SharePoint Oversharing Detection](../../../controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md) has identified sites that require ongoing monitoring.
- Reviewed companion solution [17-sharepoint-permissions-drift](https://github.com/judeper/FSI-CopilotGov-Solutions/tree/main/solutions/17-sharepoint-permissions-drift).
- If access recertification is part of the operating model, review companion solution [18-entra-access-reviews](https://github.com/judeper/FSI-CopilotGov-Solutions/tree/main/solutions/18-entra-access-reviews).
- Named site owners, compliance approvers, and change-management contacts are documented.

## Access Paths

| Portal | Path | Why it matters |
|--------|------|----------------|
| SharePoint admin center | Reports > Data access governance | Establishes the approved access baseline for each monitored site |
| Microsoft Entra admin center | Groups / Access reviews | Supports group membership validation and downstream recertification |
| Governance reporting surface | Evidence repository / review workspace | Stores drift findings, approvals, and exception records |

## Steps

### Step 1: Identify the baseline population

Determine which sites, libraries, or permission scopes will be monitored for drift. Start with the same high-risk sites surfaced by Control 1.2 and any locations that routinely handle regulated or privileged content.

### Step 2: Capture the approval model

Define who can approve or reject permission changes by severity tier so the drift workflow has a named operational path before the first scan runs.

### Step 3: Align thresholds to change windows

Review how the organization distinguishes expected change from unauthorized drift. Record approved change windows, emergency paths, and exception handling.

### Step 4: Define alert and review channels

Decide where drift findings are reviewed and how notifications are routed, such as a governance mailbox, collaboration channel, or ticketing system.

### Step 5: Connect drift detection to periodic recertification

If the organization uses access reviews, define when repeated HIGH-risk drift should trigger or inform a downstream review cycle.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Monitor only the highest-risk SharePoint sites and require documented review of every HIGH finding. |
| **Recommended** | Align drift thresholds to formal change windows and record approval paths for each in-scope site. |
| **Regulated** | Maintain baseline evidence, approval history, and escalation records for every monitored site and periodic review cycle. |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) to capture baselines and run drift scans.
- Use [Verification & Testing](verification-testing.md) to validate baseline integrity and drift classification.
- Keep [Troubleshooting](troubleshooting.md) available for baseline, alerting, and reversion issues.

*FSI Copilot Governance Framework v1.4.0 - April 2026*
- Back to [Control 1.15](../../../controls/pillar-1-readiness/1.15-sharepoint-permissions-drift.md)
