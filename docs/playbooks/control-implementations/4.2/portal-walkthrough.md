# Control 4.2: Copilot in Teams Meetings Governance — Portal Walkthrough

Step-by-step portal configuration for governing Copilot capabilities in Microsoft Teams meetings, including transcription enforcement, summarization governance, and action item management in financial services environments.

## Prerequisites

- **Role:** Teams Administrator, Compliance Administrator
- **License:** Microsoft 365 E5 with Copilot add-on, Teams Premium (for advanced meeting controls)
- **Access:** Microsoft Teams Admin Center, Microsoft 365 Admin Center

## Steps

### Step 1: Override the Teams Copilot Default Change (Critical)

**Portal:** Microsoft Teams Admin Center
**Path:** Meetings > Meeting Policies

!!! danger "Effective March 2026, Microsoft changed the default Copilot Teams meeting policy from EnabledWithTranscript to Enabled. This step overrides that change for FSI compliance."

1. Navigate to **Teams Admin Center > Meetings > Meeting Policies**.
2. Select the meeting policy assigned to regulated users (e.g., "FSI-Regulated-Policy" or "Global").
3. Locate the **Copilot** section within the policy settings.
4. Verify the **Copilot** setting — if it shows "Enabled" (without transcript requirement), this must be changed.
5. Set **Copilot** to **"On with transcript"** (corresponds to `EnabledWithTranscript` in PowerShell).
6. Save the policy.
7. Verify the change has propagated by checking the policy summary — the Copilot row should show "On with transcript."

### Step 2: Configure Meeting Transcription Policy

**Portal:** Microsoft Teams Admin Center
**Path:** Meetings > Meeting Policies > Recording and transcription

1. Navigate to the Meeting policies section.
2. Edit or create a meeting policy for Copilot-enabled users.
3. Under **Recording and transcription**:
   - Set **Transcription** to On (required for Copilot meeting features under EnabledWithTranscript)
   - Set **Meeting recording** to On or per your firm's recording policy
   - Set **Recording expiration** to align with retention requirements
4. Assign the policy to the appropriate user groups.

### Step 3: Configure Copilot Meeting Settings

**Portal:** Microsoft Teams Admin Center
**Path:** Meetings > Meeting Policies > Copilot

1. Under the Copilot section of the meeting policy:
   - Set **Copilot** to "On with transcript" — this is the FSI-compliant configuration (EnabledWithTranscript)
   - Do not use "On without transcript" for any user group with recordkeeping obligations
   - For regulated meetings, "On with transcript" ensures that all Copilot-generated artifacts have a corresponding verbatim record
2. Configure whether Copilot can be used during and/or after meetings.
3. Set the default Copilot access for different meeting types (scheduled, ad hoc, channel meetings).

### Step 4: Configure Sensitivity Labels for Meetings

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Information protection > Labels

1. Create or configure sensitivity labels for meeting types:
   - **Internal — Standard:** Copilot enabled with transcript
   - **Internal — Confidential:** Copilot enabled with transcript, recording restricted
   - **Client Meeting — Regulated:** Copilot enabled, transcript and recording mandatory
   - **Material Nonpublic Information:** Copilot disabled for MNPI meetings
2. Publish the meeting labels to Copilot-licensed users.

### Step 5: Configure Meeting Summary and Action Item Controls

**Portal:** Microsoft Teams Admin Center
**Path:** Meetings > Meeting Policies > AI features

1. Configure AI-generated meeting notes and summary settings:
   - Enable or disable automatic meeting summaries
   - Control who receives AI-generated action items
   - Set summary distribution to meeting organizer and attendees only
2. Configure recap availability (Intelligent Recap for Teams Premium).
3. Set retention policies for meeting summaries and transcripts.

### Step 6: Verify Policy Assignment

**Portal:** Microsoft Teams Admin Center
**Path:** Users > Manage users

1. Select a sample of users from regulated business units.
2. For each user, verify the assigned Teams meeting policy shows "FSI-Regulated-Policy" (or the firm's named policy).
3. Confirm the policy enforces "On with transcript" for Copilot.
4. For users who should not have Copilot: confirm they have a restrictive meeting policy or no Copilot license.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Copilot in meetings | EnabledWithTranscript | EnabledWithTranscript | EnabledWithTranscript |
| Auto-transcription | On | On (mandatory for compliance) | On (mandatory) |
| Auto-recording | Optional | On for scheduled meetings with clients | On for all regulated activities |
| MNPI meeting Copilot | Disabled | Disabled | Disabled |
| Meeting summary retention | Default | 3 years (FINRA/SEC) | 7 years (FINRA/SEC extended) |

## Regulatory Alignment

- **SEC Rule 17a-4(b)(4)** — EnabledWithTranscript ensures verbatim transcript preservation alongside AI-generated summaries, meeting the 3-year readily accessible retention requirement
- **FINRA Rule 3110** — Supports compliance with supervisory requirements for meeting documentation
- **FINRA Rule 4511** — Preserves the underlying record (transcript) that validates the AI-generated meeting artifacts
- **MiFID II** — Supports meeting documentation requirements for firms with EU operations

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Teams meeting policy automation and EnabledWithTranscript enforcement scripts
- See [Verification & Testing](verification-testing.md) to validate meeting governance
