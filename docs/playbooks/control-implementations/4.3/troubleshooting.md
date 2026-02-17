# Control 4.3: Copilot in Teams Phone and Queues Governance — Troubleshooting

Common issues and resolution steps for Copilot governance in Teams Phone and call queue environments.

## Common Issues

### Issue 1: Copilot Call Summaries Not Generating

- **Symptoms:** After completing phone calls, no Copilot-generated call summary is available.
- **Root Cause:** The calling policy may not have Copilot features enabled, the user may lack the required license, or transcription is not active.
- **Resolution:**
  1. Verify the user has both a Copilot and Teams Phone license.
  2. Check the calling policy includes Copilot summarization settings.
  3. Confirm transcription is enabled in the calling policy.
  4. Verify the call duration exceeded the minimum threshold for summary generation.
  5. Update the Teams client to the latest version.

### Issue 2: Call Transcription Quality Issues

- **Symptoms:** Call transcripts contain frequent errors, misidentify speakers, or miss content.
- **Root Cause:** Audio quality issues, multiple speakers overlapping, or language/accent recognition limitations.
- **Resolution:**
  1. Ensure call participants have adequate audio quality (headsets recommended over speakerphone).
  2. Verify the transcription language setting matches the primary language of the call.
  3. Report systematic transcription quality issues to Microsoft support for model improvement.
  4. Train users to speak clearly and avoid overlapping speech for better transcription accuracy.

### Issue 3: Compliance Recording Conflict with Copilot

- **Symptoms:** Third-party compliance recording solution interferes with Copilot transcription or summarization.
- **Root Cause:** Both the compliance recorder and Copilot may be attempting to process the audio stream simultaneously.
- **Resolution:**
  1. Verify compatibility between the compliance recording solution and Copilot.
  2. Check with the compliance recording vendor for known Copilot integration guidance.
  3. If conflicts persist, configure Copilot to generate summaries from the compliance recorder's output rather than the live stream.
  4. Contact Microsoft support for guidance on dual-processing scenarios.

### Issue 4: Call Queue Agent Copilot Access Inconsistent

- **Symptoms:** Some call queue agents have Copilot during queue calls while others do not, despite identical configurations.
- **Root Cause:** Individual agent policies may differ, or license assignment is inconsistent across the agent pool.
- **Resolution:**
  1. Verify all agents in the queue have identical calling policies: review with `Get-CsOnlineUser`.
  2. Confirm all agents have Copilot licenses assigned.
  3. Check for any conflicting policies at the user, group, or organization level.
  4. Re-assign policies uniformly using the batch assignment script.

## Diagnostic Steps

1. **Check user policy:** `Get-CsOnlineUser -Identity "user@contoso.com" | Select TeamsCallingPolicy`
2. **Verify license:** Confirm Copilot and Teams Phone licenses in the Admin Center.
3. **Test call transcription:** Place a test call and verify transcription generates.
4. **Review call queue config:** `Get-CsCallQueue -Identity "queue-name" | Format-List`

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Compliance recording failure affecting regulatory obligations | Compliance team + IT + Recording vendor |
| High | Copilot exposing call content to unauthorized users | IT Security + Teams Admin |
| Medium | Call summary generation failures | IT Support — license and policy verification |
| Low | Transcription quality issues | Document and monitor improvements |

## Related Resources

- [Control 4.2: Copilot in Teams Meetings Governance](../4.2/portal-walkthrough.md)
- [Control 4.4: Copilot in Viva Suite Governance](../4.4/portal-walkthrough.md)
