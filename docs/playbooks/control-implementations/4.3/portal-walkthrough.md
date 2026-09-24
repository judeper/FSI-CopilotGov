# Control 4.3: Copilot in Teams Phone and Queues Governance — Portal Walkthrough

Step-by-step portal configuration for governing Copilot capabilities in Teams Phone, call queues, and auto-attendants within financial services environments.

## Prerequisites

- **Role:** Teams Admin, Purview Compliance Admin
- **License:** Microsoft 365 E5 with Copilot add-on, Teams Phone license
- **Access:** Teams admin center

## Steps

### Step 1: Configure Copilot for Teams Phone

**Portal:** Teams admin center
**Path:** Voice > Calling policies

1. Navigate to Voice > Calling policies.
2. Edit or create a calling policy for Copilot-enabled phone users.
3. Configure Copilot settings for phone calls:
   - Enable or disable Copilot call summarization
   - Configure real-time transcription for phone calls
   - Set call summary distribution rules
4. Assign the policy to the appropriate user groups (e.g., contact center agents, advisors).

### Step 2: Verify Call Queue and Teams Phone Agent Scope

**Portal:** Teams admin center
**Path:** Voice > Call queues; Voice > Templates & Resources > Agents and Queues (Teams Phone Agent preview/gated tenants only)

1. Open each call queue that handles client interactions and document queue routing, authorized users, supervisor permissions, and reporting access.
2. Confirm ordinary queue agents inherit Teams Phone Copilot availability through their assigned `CsTeamsCallingPolicy`; current Learn syntax does not document a direct `Set-CsCallQueue -Copilot` parameter.
3. If the tenant participates in Teams Phone Agent / Copilot Studio voice-agent preview, verify:
   - Microsoft has enabled the tenant/environment for the Teams Phone channel.
   - Required Teams Phone, Copilot Studio tenant, and Copilot Studio user licenses are assigned.
   - Transfer targets, tags, authentication mode, supported region, and escalation paths are approved.
4. Apply additional controls for queues handling sensitive financial information:
   - Require approved recording/transcription controls where appropriate.
   - Apply retention policies to recordings, transcripts, recaps, and AI-agent artifacts per firm-approved schedule.

### Step 3: Configure Recording and Transcription Compliance

**Portal:** Teams admin center
**Path:** Voice > Calling policies > Recording and transcription

1. Enable compliance recording if required by your firm's communication recording obligations.
2. Verify the tenant storage location and data residency behavior for each call artifact type.
3. Set transcript retention per firm-approved records schedule.
4. Verify whether DLP or communication compliance policies can inspect each transcript/artifact type in the tenant; document unsupported paths.

### Step 4: Configure Auto Attendants and Teams Phone Agent Separately

**Portal:** Teams admin center
**Path:** Voice > Auto attendants; Voice > Templates & Resources > Agents and Queues (preview/gated tenants only)

1. Review standard auto attendants for configured menus, voice commands, greetings, business hours, and transfer destinations.
2. If using Teams Phone Agent, document that it is the AI-driven conversational option and verify tenant preview eligibility.
3. Ensure caller-facing disclosure language and escalation paths are approved for any AI-assisted voice-agent workflow.
4. Configure logging/evidence capture for standard auto-attendant changes and Teams Phone Agent / Copilot Studio voice-agent interactions where available.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Call transcription | Optional | Enabled | Required for client calls |
| Copilot call summary | Enabled where approved | Enabled with controls | Enabled with tenant-verified DLP/compliance coverage where supported |
| Compliance recording | Optional | Recommended | Required |
| Summary retention | Per firm schedule | Per firm schedule | Per firm-approved records schedule |

## Regulatory Alignment

- **FINRA Rule 3110** — May be relevant to firm-defined supervision of phone-based client communications
- **SEC 17a-4** — May be relevant to firm-defined record retention for phone-based business communications
- **MiFID II Article 16** — May be relevant to firm-defined recording controls for investment service communications

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for phone policy automation
- See [Verification & Testing](verification-testing.md) to validate phone governance
- Back to [Control 4.3](../../../controls/pillar-4-operations/4.3-teams-phone-queues.md)
