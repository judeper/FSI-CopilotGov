# Control 4.1: Copilot Admin Settings and Feature Management — Portal Walkthrough

Step-by-step portal review for the current Microsoft 365 Copilot administration model across Copilot settings, Agents, billing, and Cloud Policy.

## Prerequisites

- **Role:** AI Administrator (recommended), Global Reader for read-only review, or M365 Global Admin where broader tenant changes are required
- **Access:** Microsoft 365 Admin Center and Cloud Policy service
- **Governance prerequisite:** Approved rollout groups and change approval process

## Steps

### Step 1: Review Copilot Overview

**Portal:** Microsoft 365 Admin Center  
**Path:** Copilot > Overview

1. Open **Copilot > Overview**.
2. Review readiness, adoption, and recommended actions.
3. Capture evidence of who reviewed the dashboard and when.

### Step 2: Review Copilot Settings Tabs

**Portal:** Microsoft 365 Admin Center  
**Path:** Copilot > Settings

1. Open **User access** and confirm which users or groups can use Copilot.
2. Open **Data access** and review web search and related data-source decisions.
3. Open **Copilot actions** and review actions that affect feature behavior or connected experiences.
4. Open **Other settings** and review tenant-level settings that affect the Copilot experience.
5. Record any deviations from the approved baseline.

### Step 3: Review Agents Governance

**Portal:** Microsoft 365 Admin Center  
**Path:** Agents > Overview / All agents / Settings

1. Open **Agents > Overview** and review governance signals.
2. Open **All agents** to review inventory, requests, blocked agents, and ownerless agents.
3. Open **Settings** and verify:
   - allowed agent types
   - sharing settings
   - user access scope

### Step 4: Review Copilot Pages / Notebooks Policy

**Portal:** Microsoft 365 Cloud Policy service  
**Path:** `https://config.office.com` > Customization > Policy Management

1. Review **Create and view Copilot Pages and Copilot Notebooks**.
2. Review the code preview policy for Copilot Chat and Pages.
3. Confirm the policy is scoped only to the intended user population.

### Step 5: Review Billing Controls

**Portal:** Microsoft 365 Admin Center

1. Open **Settings > Org settings > Self-service trials and purchases** and confirm Microsoft 365 Copilot self-service purchasing is configured as approved.
2. Open **Billing > Pay-as-you-go services** and confirm whether any billing policies are active.
3. Open **Cost Management** and review cost visibility if PAYG is enabled.

### Step 6: Review Baseline Security Mode

**Portal:** Microsoft 365 Admin Center  
**Path:** Settings > Org settings > Security & privacy

1. Review the organization's Baseline Security Mode posture.
2. Confirm any relevant findings are reflected in Copilot governance decisions.
3. Document Baseline Security Mode as a complementary Microsoft 365 baseline rather than a Copilot-specific tab.

## FSI Recommendations

| Area | Baseline | Recommended | Regulated |
|------|----------|-------------|-----------|
| Admin role | AI Administrator | AI Administrator + documented reviewer roles | AI Administrator with PIM / time-bound activation |
| Web search | Disabled | Disabled by default | Disabled |
| Agents | Approved types only | Approved types + scoped user access | Restricted to approved groups with compliance review |
| Pages / Notebooks | Scoped by Cloud Policy | Scoped by Cloud Policy + quarterly review | Disabled for IB-sensitive populations unless exception approved |
| PAYG | Review before enablement | Approved groups only | Approved groups only with documented spend governance |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for administrative automation
- See [Verification & Testing](verification-testing.md) to validate configuration
- Back to [Control 4.1](../../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md)
