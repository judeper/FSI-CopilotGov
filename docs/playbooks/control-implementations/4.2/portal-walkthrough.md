# Control 4.2: Copilot in Teams Meetings Governance — Portal Walkthrough

Step-by-step portal configuration for governing Copilot capabilities in Microsoft Teams meetings, including transcription, summarization, and action item generation in financial services environments.

## Prerequisites

- **Role:** Teams Administrator, Compliance Administrator
- **License:** Microsoft 365 E5 with Copilot add-on, Teams Premium (for advanced meeting controls)
- **Access:** Microsoft Teams Admin Center, Microsoft 365 Admin Center

## Steps

### Step 1: Configure Meeting Transcription Policy

**Portal:** Microsoft Teams Admin Center
**Path:** Meetings > Meeting policies

1. Navigate to the Meeting policies section.
2. Edit or create a meeting policy for Copilot-enabled users.
3. Under **Recording and transcription**:
   - Set **Transcription** to On (required for Copilot meeting features)
   - Set **Meeting recording** to On or per your firm's recording policy
   - Set **Recording expiration** to align with retention requirements
4. Assign the policy to the appropriate user groups.

### Step 2: Configure Copilot Meeting Settings

**Portal:** Microsoft Teams Admin Center
**Path:** Meetings > Meeting policies > Copilot

1. Under the Copilot section of the meeting policy:
   - Set **Copilot** to "On with transcript" or "On without transcript" based on compliance requirements
   - For regulated meetings, recommend "On with transcript" to maintain full audit trail
2. Configure whether Copilot can be used during and/or after meetings.
3. Set the default Copilot access for different meeting types (scheduled, ad hoc, channel meetings).

### Step 3: Configure Sensitivity Labels for Meetings

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Information protection > Labels

1. Create or configure sensitivity labels for meeting types:
   - **Internal — Standard:** Copilot enabled with transcript
   - **Internal — Confidential:** Copilot enabled with transcript, recording restricted
   - **Client Meeting — Regulated:** Copilot enabled, transcript and recording mandatory
   - **Material Nonpublic Information:** Copilot disabled for MNPI meetings
2. Publish the meeting labels to Copilot-licensed users.

### Step 4: Configure Meeting Summary and Action Item Controls

**Portal:** Microsoft Teams Admin Center
**Path:** Meetings > Meeting policies > AI features

1. Configure AI-generated meeting notes and summary settings:
   - Enable or disable automatic meeting summaries
   - Control who receives AI-generated action items
   - Set summary distribution to meeting organizer and attendees only
2. Configure recap availability (Intelligent Recap for Teams Premium).
3. Set retention policies for meeting summaries and transcripts.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Meeting transcription | On | On (mandatory for compliance) | On (mandatory) |
| Copilot in meetings | On with transcript | On with transcript | On with transcript |
| MNPI meeting Copilot | Enabled | Disabled | Disabled |
| Meeting summary retention | Default | 1 year | 7 years |

## Regulatory Alignment

- **FINRA Rule 3110** — Supports compliance with supervisory requirements for meeting documentation
- **SEC Rule 17a-4** — Helps meet record retention for meeting records containing business communications
- **MiFID II** — Supports meeting documentation requirements for firms with EU operations

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Teams meeting policy automation
- See [Verification & Testing](verification-testing.md) to validate meeting governance
