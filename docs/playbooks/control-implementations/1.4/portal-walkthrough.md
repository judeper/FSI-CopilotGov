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

### Step 2: Configure Content Source Scope

**Portal:** Microsoft 365 Admin Center
**Path:** SharePoint Admin > Settings > Search > Restricted SharePoint Search and related content-source governance

Review which content sources are included in the Semantic Index. By default, the index covers SharePoint Online, OneDrive for Business, Exchange Online, and Teams messages.

For FSI environments, evaluate whether all content sources should be indexed. Consider excluding content sources that contain highly sensitive data until proper controls are in place.

### Step 3: Review Item-Level Processing

**Portal:** Microsoft Purview
**Path:** Purview > Data Security Posture Management for AI > Activity Explorer

Review Copilot activity and content interaction patterns. DSPM for AI Activity Explorer shows how Copilot interacts with organizational content, including which sensitivity labels are present on accessed items.

Verify that items with "Highly Confidential" labels are handled according to your organization's policy (indexed with access enforcement vs. excluded entirely via Restricted Content Discovery).

### Step 4: Set Tenant-Level Index Controls

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings

Configure tenant-level controls that affect Copilot content access:
- Restricted SharePoint Search (RSS) configuration (see Control 1.3) to scope which sites Copilot can discover
- DLP policies for Copilot interaction channels
- User-level Copilot license assignment that controls who can query content via Copilot

### Step 5: Document Index Governance Decisions

Record all governance decisions about semantic index scope, including:
- Which content sources are indexed and which are excluded
- How sensitivity labels affect indexing behavior
- User populations enabled for Copilot querying
- Review cadence for index governance decisions

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Review default semantic index scope and document governance decisions |
| **Recommended** | Configure content source restrictions via RSS (Control 1.3) and DLP policies for Copilot channels |
| **Regulated** | Implement formal index governance policy with change control and quarterly governance committee review |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for index management automation
- See [Verification & Testing](verification-testing.md) to validate index governance
- Review Control 1.3 for Restricted SharePoint Search as a complementary scoping control
