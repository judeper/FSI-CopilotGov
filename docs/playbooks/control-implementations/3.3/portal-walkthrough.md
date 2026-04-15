# Control 3.3: eDiscovery for Copilot-Generated Content — Portal Walkthrough

Step-by-step portal configuration for enabling eDiscovery capabilities that cover Copilot-generated content, interaction history, and AI-assisted communications in financial services environments.

The unified eDiscovery experience (generally available May 2025) consolidates all eDiscovery work into a single interface within the Microsoft Purview portal. All navigation in this walkthrough uses the unified experience.

> **Important — Classic Portal Retirement:** Classic Content Search and eDiscovery (Standard) experiences are being retired in favor of the unified Purview eDiscovery portal. Organizations still using classic workflows should plan to migrate. The unified experience uses a **case-centric access model** — all searches, holds, and review sets are scoped within a case, and access is controlled by case membership rather than standalone role assignments. Organizations should verify that case membership is configured correctly for all compliance personnel.

## Prerequisites

- **Role:** eDiscovery Manager or eDiscovery Administrator
- **License:** Microsoft 365 E5 or E5 eDiscovery add-on (Premium capabilities); E3 provides Standard capabilities within the unified experience
- **Access:** Microsoft Purview portal at [purview.microsoft.com](https://purview.microsoft.com)

## Steps

### Step 1: Verify eDiscovery Licensing and Access

**Portal:** Microsoft 365 Admin Center
**Path:** Billing > Licenses

1. Confirm that eDiscovery licenses are assigned to custodians who may be subject to discovery (E5 or E5 eDiscovery add-on for Premium capabilities).
2. Verify the compliance admin team has eDiscovery Manager or Administrator role assignments.
3. Navigate to **Microsoft Purview > eDiscovery > Cases** to confirm the unified experience is available in your tenant.

### Step 2: Create a Copilot-Specific eDiscovery Case

**Portal:** Microsoft Purview portal
**Path:** Microsoft Purview > eDiscovery > Cases > Create a case

1. Click **Create a case** and name it per your naming convention (e.g., "FSI-Copilot-Discovery-Template").
2. Add a description indicating this case covers Copilot-generated content searches.
3. Assign case members from the compliance and legal teams.
4. Click **Save** to create the case. The case opens in the unified eDiscovery interface.
5. All data access for this case is now governed by the **case-centric access model** — only assigned case members can view, search, or export content within the case.

> **Note:** If you have existing cases created before May 2025, open each case and verify the Copilot content location is included in data sources. Navigate to **Data sources** within the case and confirm "Microsoft Copilot experiences" appears as a data source option. Pre-migration cases may require manual addition of this location.

### Step 3: Add Custodial Data Sources Including Copilot

**Portal:** Microsoft Purview portal
**Path:** eDiscovery > Cases > [case name] > Data sources > Add custodians

1. Open the case and navigate to the **Data sources** tab.
2. Click **Add custodians** and select the relevant users.
3. For each custodian, confirm the following locations are included:
   - Exchange mailbox (contains Copilot interaction history)
   - OneDrive for Business (contains Copilot-generated documents)
   - SharePoint sites (contains collaborative Copilot content)
   - Microsoft Teams (contains Copilot-assisted Teams messages)
   - Microsoft Copilot experiences (the unified Copilot content location -- confirm this is present)
4. Enable **Hold** on custodial data sources to preserve Copilot content.

### Step 4: Create a Search for Copilot Content

**Portal:** Microsoft Purview portal
**Path:** eDiscovery > Cases > [case name] > Searches > New search

1. Click **New search** and name it "Copilot Interactions and Content".
2. Under **Custodian locations**, select the custodians added in Step 3.
3. Under search conditions, use KQL queries targeting Copilot-specific properties:
   - `kind:microsearch` for Copilot interaction records
   - `CopilotSurface:"Microsoft365Copilot"` to filter by surface (Premium tier)
4. Use the **Copilot surface filter** in the unified search builder to narrow results by surface type, agent name, or interaction type.
5. Set the date range appropriate to the discovery request.
6. Run the search estimate to preview results before committing to review.

### Step 5: Add Results to Review Set and Export

**Portal:** Microsoft Purview portal
**Path:** eDiscovery > Cases > [case name] > Review sets

1. After the search completes, click **Add results to review set**.
2. Use inline content rendering (available as of February 2026) to preview Copilot interaction content directly in the review set.
3. Apply tags to relevant items for production.
4. Export in the format required by the requesting party (PST, loose files, or PDF).

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| eDiscovery tier | Standard (within unified experience) | Premium | Premium |
| Custodian hold | Manual | Automatic | Automatic |
| Copilot content search scope | Mailbox only | All locations | All locations |
| Copilot surface filter | Not required | Recommended | Required |
| Review set AI-assisted review | Optional | Recommended | Recommended |
| Pre-migration case verification | Required | Required | Required |

## Regulatory Alignment

- **FRCP Rule 26(b)(1)** — Proportionality standard applies to scope of discoverable Copilot content; unified experience supports efficient, targeted search
- **SEC Rule 17a-4(j)** — Supports production of electronically stored records in response to SEC examination requests
- **FINRA Rule 8210** — Supports timely production of records in regulatory examinations

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for eDiscovery automation
- See [Verification & Testing](verification-testing.md) to validate eDiscovery readiness
- Back to [Control 3.3](../../../controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md)
