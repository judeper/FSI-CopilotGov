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

### Step 2: Configure Call Queue Copilot Settings

**Portal:** Teams admin center
**Path:** Voice > Call queues

1. Open each call queue that handles client interactions.
2. Configure Copilot features for the queue:
   - Enable call summarization for agent calls
   - Configure supervisor access to Copilot-generated summaries
   - Set language and transcription preferences
3. For queues handling sensitive financial information, apply additional controls:
   - Require DLP scanning on call transcripts
   - Apply retention policies to call summaries

### Step 3: Configure Recording and Transcription Compliance

**Portal:** Teams admin center
**Path:** Voice > Calling policies > Recording and transcription

1. Enable compliance recording if required by your firm's communication recording obligations.
2. Configure transcription storage location (aligned with data residency requirements).
3. Set transcript retention per regulatory requirements (minimum 3 years, recommended 7 years for FSI).
4. Enable real-time DLP scanning on phone transcripts where available.

### Step 4: Configure Auto-Attendant AI Responses

**Portal:** Teams admin center
**Path:** Voice > Auto attendants

1. Review auto-attendant configurations that use AI-powered responses.
2. Verify that auto-attendant scripts align with compliance requirements.
3. Ensure AI-generated responses include required disclaimers for financial services.
4. Configure logging of all auto-attendant AI interactions for audit purposes.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Call transcription | Optional | Enabled | Required for client calls |
| Copilot call summary | Enabled | Enabled with controls | Enabled with DLP |
| Compliance recording | Optional | Recommended | Required |
| Summary retention | 90 days | 1 year | 7 years |

## Regulatory Alignment

- **FINRA Rule 3110** — Supports compliance with supervision of phone-based client communications
- **SEC 17a-4** — Helps meet record retention for phone-based business communications
- **MiFID II Article 16** — Supports recording requirements for investment service communications

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for phone policy automation
- See [Verification & Testing](verification-testing.md) to validate phone governance
