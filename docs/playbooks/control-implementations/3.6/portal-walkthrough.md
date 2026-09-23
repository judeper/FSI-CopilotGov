# Control 3.6: Supervision and Oversight (FINRA 3110 / SEC Reg BI) — Portal Walkthrough

Step-by-step portal configuration for establishing supervisory controls over Copilot-assisted activities that provide evidence for FINRA Rule 3110 (Supervision) and SEC Regulation Best Interest review; firms should confirm applicability with counsel.

## Prerequisites

- **Role:** Purview Compliance Admin, Supervisory Principal
- **License:** Eligible Communication Compliance licensing, such as Microsoft Purview Suite (formerly Microsoft 365 E5 Compliance), Office 365 E5, or Office 365 E3 with the Advanced Compliance add-on
- **Access:** Microsoft Purview portal, Microsoft 365 Admin Center

## Steps

### Step 1: Define Supervisory Hierarchy in Purview

**Portal:** Microsoft Purview portal
**Path:** Solutions > Communication compliance > Policies (verify tenant navigation; if a separate supervisory-review settings page exists in your tenant, capture the exact label)

1. Map the supervisory hierarchy through each Communication Compliance policy's scoped users and reviewers. Verify in your tenant whether a separate supervisory-review settings page exists before documenting a standalone hierarchy path.
2. Create supervisor groups aligned with business units (wealth management, trading, advisory).
3. Use the firm's approved supervisor-capacity threshold to assign supervised users; 50 supervised users is a firm policy example that should be confirmed with compliance/legal.

### Step 2: Create Supervisory Review Policies

**Portal:** Microsoft Purview portal
**Path:** Solutions > Communication compliance > Policies > Create policy

1. Create a policy named "FSI-FINRA-3110-Supervision-Copilot".
2. Set supervised users to registered representatives using Copilot.
3. Set supervised locations to include all Copilot-enabled communication channels.
4. Under conditions, configure:
   - **All outbound communications** — 25% sampling for routine supervision as a firm policy example
   - **Client-facing communications with financial recommendations** — 100% review as a firm policy example
   - **Copilot-drafted investment advice** — 100% review with pre-send hold as a firm policy example

### Step 3: Configure Reg BI Documentation Review

**Portal:** Microsoft Purview portal
**Path:** Solutions > Communication compliance > Policies

1. Create a second policy named "FSI-RegBI-Copilot-BestInterest-Review".
2. Target communications where Copilot assists in creating investment recommendations.
3. Add conditions to detect:
   - Recommendation language (buy, sell, hold, allocate)
   - Product-specific terms (mutual fund, ETF, annuity, structured product)
   - Cost and fee disclosures
4. Apply the firm's approved supervisory review percentage for matches; 100% review is a regulated-tier firm policy example.

### Step 4: Set Up Supervision Dashboards

**Portal:** Microsoft Purview portal
**Path:** Solutions > Communication compliance > Dashboard

1. Configure the dashboard to display key supervision metrics:
   - Outstanding review items by supervisor
   - Average review completion time
   - Policy match trend over 30/60/90 days
   - Escalation rate by policy
2. Set up weekly email digests for supervisory principals.

### Step 5: View Agent-Specific Audit Events for Supervisory Review

**Portal:** Microsoft Purview portal
**Path:** Solutions > Audit > New search

Supervisory review of M365 Copilot agent interactions (Teams channel agents, declarative agents) requires searching for agent-specific audit events in the Purview audit log. These events are captured as `CopilotInteraction` records with agent-identifying fields.

1. Navigate to **Microsoft Purview** > **Solutions** > **Audit** > **New search**.
2. Set the date range to cover the supervisory review period.
3. Under **Activities – friendly names**, search for **"Interacted with Copilot"** to capture `CopilotInteraction` records.
4. Under **Users**, enter the registered representative whose agent interactions you are reviewing.
5. Run the search and open individual records to inspect:
   - **AgentId** — identifies the specific agent (Teams channel agent or declarative agent) that participated in the interaction
   - **AgentName** — the display name of the agent, useful for correlating to the firm's agent inventory in the WSP
   - **AccessedResources.XPIADetected** — nested cross-prompt injection attempt flag on an accessed resource; a value of `true` indicates the agent may have processed untrusted external content
   - **CopilotEventData** — contains the prompt context and any grounding sources the agent accessed
6. Export results using the **Export** button for retention as supervisory review evidence.

**Note:** Agent interactions where the output was forwarded to a client (via email or document share) should be correlated with Communication Compliance records to confirm the output was reviewed before or after delivery per the firm's supervisory procedures.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Routine communication sampling | 10% policy example | 25% policy example | 25% policy example |
| Investment recommendation review | 25% policy example | 100% policy example | 100% policy example |
| Pre-send hold for Copilot advice | Off | Recommended policy example | Required if approved by firm policy |
| Supervisor-to-rep ratio | 1:100 policy example | 1:50 policy example | 1:25 policy example |
| Agent audit event review | Agent inventory only | Periodic sampling of agent interactions | Correlated agent-to-communication review |

## Regulatory Alignment

- **FINRA Rule 3110** — Provides evidence for supervisory system and written supervisory procedure review; firms should confirm applicability with counsel
- **FINRA Rule 3110(a)** — Agent supervision: firms should confirm with counsel when supervisory systems should extend to Teams channel agents and declarative agents used by associated persons
- **FINRA Rule 3120** — Supports supervisory control system testing requirements
- **SEC Reg BI** — Provides evidence for best-interest documentation, disclosure, and care review; firms should confirm applicability with counsel

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automation
- See [Verification & Testing](verification-testing.md) to validate supervisory controls
- Back to [Control 3.6](../../../controls/pillar-3-compliance/3.6-supervision-oversight.md)
