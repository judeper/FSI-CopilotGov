# Control 3.6: Supervision and Oversight (FINRA 3110 / SEC Reg BI) — Troubleshooting

Common issues and resolution steps for supervisory controls over Copilot-assisted activities.

## Common Issues

### Issue 1: Supervisory Review Backlog Exceeding SLA

- **Symptoms:** Review items are aging beyond the 24/48 hour SLA, supervisors report insufficient time for reviews.
- **Root Cause:** Supervisor-to-representative ratio too high, policy scope too broad, or supervisors lack training on review tools.
- **Resolution:**
  1. Check current supervisor ratios and redistribute if any supervisor exceeds 1:50.
  2. Implement automated resolution for low-risk, low-confidence policy matches.
  3. Provide refresher training on the Communication compliance review interface.
  4. Consider adding a deputy supervisor role for backup coverage.

### Issue 2: Pre-Send Hold Causing Business Disruption

- **Symptoms:** Time-sensitive client communications are delayed by pre-send supervisory holds, leading to complaints.
- **Root Cause:** Pre-send hold scope may be too broad, or supervisor response time is too slow for urgent communications.
- **Resolution:**
  1. Narrow pre-send hold to only high-risk communication types (investment recommendations, new account openings).
  2. Implement an expedited review path for time-sensitive items (4-hour SLA).
  3. Designate on-call supervisors for real-time review during business hours.
  4. Move lower-risk communications to post-send review with escalation triggers.

### Issue 3: Supervisory Hierarchy Not Reflecting Organizational Changes

- **Symptoms:** New representatives are not assigned to supervisors, or departed supervisors still have assigned users.
- **Root Cause:** Supervisory hierarchy is not synchronized with HR or registration systems.
- **Resolution:**
  1. Audit the current supervisory hierarchy against the firm's registration database.
  2. Update group memberships for any misaligned users.
  3. Implement a monthly reconciliation process between HR systems and supervisory groups.
  4. Configure Entra ID dynamic groups to auto-assign based on department and registration attributes.

### Issue 4: Reg BI Documentation Gaps in Copilot-Drafted Recommendations

- **Symptoms:** Supervisory reviewers find that Copilot-drafted recommendations lack required Reg BI elements.
- **Root Cause:** Copilot may not automatically include all required disclosure and documentation elements in its generated content.
- **Resolution:**
  1. Create Copilot prompt templates that include Reg BI required elements as placeholders.
  2. Train representatives to verify Reg BI completeness before submitting for review.
  3. Add a Reg BI checklist to the supervisory review workflow.
  4. Consider configuring Copilot declarative agents with instructions to include required disclosures.

### Issue 5: Agent Actions Not Appearing in Supervisory Review Queue

- **Symptoms:** A Teams channel agent or declarative agent has produced client-facing outputs, but these do not appear in the Communication Compliance review queue for supervisory review.
- **Root Cause:** Communication Compliance policies are scoped to human-initiated outbound communications and may not capture content generated or forwarded by agents unless the agent's output passes through a supervised location (Exchange Online, Teams external). Agent-to-agent interactions or internal-only agent outputs will not appear in the review queue unless the output is ultimately sent or shared externally by the associated person.
- **Resolution:**
  1. Review the agent's configuration to understand where its outputs are delivered — if outputs are written to SharePoint or shared internally only, they are not captured by Communication Compliance. These require a separate review process defined in the WSP.
  2. For agents whose outputs are forwarded externally by associated persons, verify the supervisor's outbound email or Teams policies include the associated person's account in the supervised scope.
  3. Use Script 5 (Agent Interaction Audit) from the PowerShell setup to retrieve CopilotInteraction records for the agent and correlate them with Communication Compliance review records to identify any gap.
  4. Update the WSP agent inventory to document each agent's output delivery mechanism and the corresponding supervisory review method.

### Issue 6: Agent Audit Events Delayed or Missing

- **Symptoms:** CopilotInteraction audit events for agent interactions are not appearing in the Purview audit log within the expected 15–30 minute window, or some interactions appear to be missing entirely.
- **Root Cause:** Audit log ingestion latency can be up to 24 hours in some environments. Short-lived or lightweight agent interactions (e.g., single-turn queries with no external grounding) may produce reduced audit footprints. Agent interactions within Copilot Chat sessions may be batched differently from direct agent invocations.
- **Resolution:**
  1. Wait up to 24 hours before concluding that audit events are missing — check again with a wider search window.
  2. Verify the tenant has audit logging enabled: navigate to **Microsoft Purview** > **Audit** > confirm audit retention is active and search returns results for other event types.
  3. Confirm the agent is a supported M365 Copilot agent type (Teams channel agent, declarative agent). Custom Copilot Studio agents may produce different audit record structures.
  4. Run Script 6 (Search Agent Events by Specific Agent ID) with a broader date range to confirm whether events exist at all for the agent.
  5. If events are consistently missing for a specific agent over multiple days, open a support case with Microsoft referencing the AgentId and interaction timestamps.

### Issue 7: WSP Gap for Newly Deployed Agents

- **Symptoms:** During Test 6 (WSP coverage verification), a deployed agent is found that is not documented in the firm's written supervisory procedures.
- **Root Cause:** A Teams channel agent or declarative agent was deployed by a business unit or IT team without notifying compliance, resulting in an undocumented agent operating outside the supervisory framework.
- **Resolution:**
  1. Immediately suspend or restrict the undocumented agent's access to external data or client-facing outputs pending WSP documentation.
  2. Conduct a brief supervisory review of the agent's historical interactions using Script 5 (Agent Interaction Audit) to assess whether any client-facing outputs were produced without supervisory coverage.
  3. Draft and approve a WSP addendum entry for the agent, documenting: agent scope, authorized actions, data sources accessed, and supervisory review cadence.
  4. Implement a governance gate for new agent deployments: require compliance review and WSP documentation before any agent is activated for use by associated persons.
  5. Add the agent to the firm's agent inventory and include it in the next annual FINRA 3120(b) supervisory testing cycle.

## Diagnostic Steps

1. **Review supervisor assignments:** Verify all Copilot-enabled reps have an assigned supervisor.
2. **Check SLA metrics:** Run the SLA compliance script to identify systemic delays.
3. **Audit policy scope:** Confirm policies target the correct user groups and communication channels.
4. **Test the review workflow:** Process a test item through the complete supervisory review cycle.
5. **Check agent inventory:** Verify the WSP agent inventory matches deployed agents in Microsoft 365 Admin Center.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Supervisory review system non-functional | Chief Compliance Officer + Microsoft Support |
| Critical | Undocumented agent producing client-facing outputs without supervisory coverage | Chief Compliance Officer + immediate agent suspension |
| High | Systematic SLA breaches across multiple supervisors | Compliance leadership — capacity review |
| High | Agent audit events missing for multiple agents across multiple days | IT + Microsoft Support |
| Medium | Individual supervisor backlog issues | Reassign representatives or add backup |
| Medium | WSP gap for newly deployed agent (contained, no client-facing outputs) | Compliance team — 5-business-day remediation |
| Low | Minor workflow inefficiencies | Address in next quarterly process review |

## Related Resources

- [Control 3.4: Communication Compliance Monitoring](../3.4/portal-walkthrough.md)
- [Control 3.5: FINRA Rule 2210 Compliance](../3.5/portal-walkthrough.md)
- [Control 3.7: Regulatory Reporting](../3.7/portal-walkthrough.md)
- Back to [Control 3.6](../../../controls/pillar-3-compliance/3.6-supervision-oversight.md)
