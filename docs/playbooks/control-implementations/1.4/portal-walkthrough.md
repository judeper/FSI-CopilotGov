# Control 1.4: Semantic Index Governance — Portal Walkthrough

Step-by-step portal configuration for governing the Microsoft 365 Semantic Index that powers Copilot content discovery and grounding.

## Prerequisites

- Entra Global Admin or SharePoint Admin role
- Microsoft 365 Copilot licenses provisioned in the tenant
- Understanding of current content landscape across SharePoint, OneDrive, and Exchange
- Governance committee approval on semantic index scope decisions

## Steps

### Step 1: Review Semantic Index Status

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Overview

Review the current status of the Semantic Index for your tenant. The Semantic Index processes content across Microsoft 365 to create embeddings that Copilot uses for content discovery and response grounding.

Review the Copilot license assignment status and readiness checks. Confirm which users are licensed for Copilot and whether tenant readiness prerequisites are met.

### Step 2: Review Searchability and Discoverability Controls

**Portal:** SharePoint admin center
**Path:** SharePoint admin center > Sites > Active sites > [site] > Settings tab for **Restrict content from Microsoft Copilot** (RCD); site > Settings > Site settings > Search and offline availability for **Allow this site to appear in Search results**; SharePoint admin center > Settings > Search > Restricted SharePoint Search (legacy, where already enabled; see [Microsoft Learn: Restricted SharePoint Search](https://learn.microsoft.com/en-us/sharepoint/restricted-sharepoint-search))

Review which SharePoint sites remain searchable and which sites are excluded from organization-wide discovery. Microsoft documents tenant-level semantic indexing primarily through searchable SharePoint Online content, while paid-license user experiences also combine Microsoft Graph and mailbox context at query time.

For FSI environments, evaluate whether any searchable SharePoint sites containing highly sensitive data should remain discoverable to Copilot. Prefer Restricted Content Discovery (RCD) for current per-site exclusion decisions; use Restricted SharePoint Search (RSS) only where it is already enabled and a retirement plan is documented.

### Step 3: Review Item-Level Processing

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management for AI > Activity Explorer

Review Copilot activity and content interaction patterns. DSPM for AI Activity Explorer shows how Copilot interacts with organizational content, including which sensitivity labels are present on accessed items.

Verify that items with "Highly Confidential" labels are handled according to your organization's policy. Labels and DLP govern access and policy outcomes, while RCD, RSS, and site searchability govern whether SharePoint content is discoverable to Copilot.

### Step 4: Set Discovery and Retrieval Controls

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings

Configure the controls that affect Copilot content discovery and retrieval:
- Restricted Content Discovery (RCD) for current per-site exclusions from organization-wide search and Copilot
- Restricted SharePoint Search (RSS) only where it is already enabled and its retirement timeline is being managed
- DLP, information barriers, and workload-specific controls for content that remains discoverable
- User-level Copilot licensing and any PAYG agent/service decisions that determine which users can access broader work-grounded experiences

### Step 5: Document Index Governance Decisions

Record all governance decisions about semantic index scope, including:
- Which SharePoint sites remain searchable, use RCD, or remain under legacy RSS scoping
- How labels, DLP, and information barriers affect retrieved content
- User populations enabled for Copilot querying
- Review cadence for index governance decisions

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Review searchable SharePoint scope, current Copilot licensing posture, and document governance decisions |
| **Recommended** | Prefer RCD for per-site exclusions, use RSS only where already enabled, and pair discoverability controls with DLP policies for Copilot channels |
| **Regulated** | Implement formal index governance policy with change control and quarterly governance committee review |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for index management automation
- See [Verification & Testing](verification-testing.md) to validate index governance
- Review Control 1.3 for Restricted SharePoint Search retirement planning and RCD migration detail
