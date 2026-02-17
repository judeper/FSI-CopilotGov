# Control 3.3: eDiscovery for Copilot-Generated Content — Portal Walkthrough

Step-by-step portal configuration for enabling eDiscovery capabilities that cover Copilot-generated content, interaction history, and AI-assisted communications in financial services environments.

## Prerequisites

- **Role:** eDiscovery Manager or eDiscovery Administrator
- **License:** Microsoft 365 E5 or E5 eDiscovery add-on
- **Access:** Microsoft Purview compliance portal

## Steps

### Step 1: Verify eDiscovery (Premium) Licensing

**Portal:** Microsoft 365 Admin Center
**Path:** Billing > Licenses

1. Confirm that eDiscovery (Premium) licenses are assigned to custodians who may be subject to discovery.
2. Verify the compliance admin team has eDiscovery Manager or Administrator role assignments.

### Step 2: Create a Copilot-Specific eDiscovery Case

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > eDiscovery > Premium > Cases > Create a case

1. Click **Create a case** and name it per your naming convention (e.g., "FSI-Copilot-Discovery-Template").
2. Add a description indicating this case covers Copilot-generated content searches.
3. Assign case members from the compliance and legal teams.
4. Click **Save** to create the case.

### Step 3: Add Custodial Data Sources Including Copilot

**Portal:** Microsoft Purview Compliance Portal
**Path:** eDiscovery case > Data sources > Add custodians

1. Open the case and navigate to the **Data sources** tab.
2. Click **Add custodians** and select the relevant users.
3. For each custodian, confirm the following locations are included:
   - Exchange mailbox (contains Copilot interaction history)
   - OneDrive for Business (contains Copilot-generated documents)
   - SharePoint sites (contains collaborative Copilot content)
   - Microsoft Teams (contains Copilot-assisted Teams messages)
4. Enable **Hold** on custodial data sources to preserve Copilot content.

### Step 4: Create a Collection for Copilot Content

**Portal:** Microsoft Purview Compliance Portal
**Path:** eDiscovery case > Collections > New collection

1. Create a new collection named "Copilot Interactions and Content".
2. Under search conditions, use KQL queries targeting Copilot-specific properties:
   - `kind:microsoftcopilot` for Copilot interaction records
   - `appname:Copilot` for Copilot-generated artifacts
3. Set the date range appropriate to the discovery request.
4. Run the collection estimate to preview results before committing to review.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| eDiscovery tier | Standard | Premium | Premium |
| Custodian hold | Manual | Automatic | Automatic |
| Copilot content search scope | Mailbox only | All locations | All locations |
| Review set AI-assisted review | Optional | Recommended | Recommended |

## Regulatory Alignment

- **FRCP Rule 26** — Supports compliance with federal discovery obligations for electronically stored information
- **SEC Rule 17a-4** — Helps meet electronic record preservation and production requirements
- **FINRA Rule 8210** — Supports timely production of records in regulatory examinations

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for eDiscovery automation
- See [Verification & Testing](verification-testing.md) to validate eDiscovery readiness
