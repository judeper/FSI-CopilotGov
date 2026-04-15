# Control 3.6: Supervision and Oversight (FINRA 3110 / SEC Reg BI) — Verification & Testing

Test cases and evidence collection procedures for validating supervisory controls over Copilot-assisted activities.

## Test Cases

### Test 1: Supervisory Review Workflow

- **Objective:** Confirm that Copilot-assisted communications flow through the supervisory review process
- **Steps:**
  1. Have a test registered representative draft an investment recommendation using Copilot.
  2. Send the recommendation to a test client account.
  3. Verify the communication appears in the assigned supervisor's review queue.
  4. Complete the review (approve, reject, or escalate) and confirm audit trail.
- **Expected Result:** Communication flows through supervisory review with complete audit trail of actions taken.
- **Evidence:** Review queue screenshot and audit log entry showing review completion.

### Test 2: Pre-Send Hold for Investment Recommendations

- **Objective:** Validate that Copilot-drafted investment recommendations are held pending supervisory approval
- **Steps:**
  1. Configure pre-send hold for investment recommendation communications.
  2. Have a test user draft a recommendation via Copilot and attempt to send.
  3. Verify the message is held and not delivered until supervisor approves.
  4. Have the supervisor approve the message and confirm delivery.
- **Expected Result:** Message is held, supervisor reviews and approves, and the message is then delivered with approval timestamp.
- **Evidence:** Message trace showing hold status, approval action, and delivery confirmation.

### Test 3: Supervisor Capacity Validation

- **Objective:** Verify that supervisory ratios are within acceptable limits for effective oversight
- **Steps:**
  1. Run the supervisor-to-representative ratio script.
  2. Verify no supervisor oversees more than 50 Copilot-enabled representatives.
  3. Review each supervisor's review queue backlog.
  4. Confirm all supervisors are completing reviews within the defined SLA.
- **Expected Result:** All supervisory ratios are within policy limits and review SLAs are being met.
- **Evidence:** Ratio report and SLA compliance metrics.

### Test 4: Reg BI Documentation Completeness

- **Objective:** Confirm that Copilot-assisted recommendations capture required Reg BI documentation elements
- **Steps:**
  1. Review a sample of 10 Copilot-drafted recommendations that were supervisory approved.
  2. Verify each recommendation includes: client suitability basis, cost disclosure, conflict of interest disclosure, and alternatives considered.
  3. Confirm the supervisory review log captures the reviewer's assessment of each element.
- **Expected Result:** All sampled recommendations contain required Reg BI elements and supervisory attestation.
- **Evidence:** Sampled review records showing Reg BI element completeness.

### Test 5: Agent Audit Trail Capture (FINRA 3110(a) Agent Supervision)

- **Objective:** Verify that the audit trail correctly captures agent-specific interactions for supervisory review when a Teams channel agent or declarative agent is used
- **Steps:**
  1. Deploy a test Teams channel agent or use an existing declarative agent in a non-production channel.
  2. Have a test registered representative interact with the agent (e.g., ask it to summarize account information or draft a communication).
  3. Wait 15–30 minutes for audit events to propagate to the Purview audit log.
  4. Run Script 5 (Agent Interaction Audit) from the PowerShell setup guide to retrieve agent-specific CopilotInteraction events.
  5. Verify the returned records contain: `AgentId`, `AgentName`, the interacting user's identity, and the interaction timestamp.
  6. Confirm the `XPIA` field is present and set to `false` for normal interactions (no cross-prompt injection attempt detected).
- **Expected Result:** Agent interactions appear in the audit log with correct AgentId, AgentName, user identity, and timestamp. XPIA flag is captured. The records are exportable for supervisory review evidence.
- **Evidence:** CSV export from Script 5 showing agent interaction records; Purview audit log screenshot showing CopilotInteraction records with AgentId populated.

### Test 6: WSP Coverage Verification for Deployed Agents

- **Objective:** Confirm that the firm's written supervisory procedures (WSPs) address every currently deployed Copilot agent
- **Steps:**
  1. Generate a list of deployed Teams channel agents and declarative agents from the Microsoft 365 Admin Center (Admin Center > Agents > All agents / Registry).
  2. Cross-reference each deployed agent against the agent inventory section of the firm's WSP Copilot addendum.
  3. For any agent not listed in the WSP, flag as a gap requiring immediate documentation.
  4. For listed agents, verify the WSP entry includes: agent scope, authorized actions, supervisory review cadence, and the person responsible for oversight.
- **Expected Result:** All deployed agents are listed in the WSP with complete supervisory documentation. Zero undocumented agents are found.
- **Evidence:** Agent inventory from Admin Center (screenshot or export) cross-referenced against WSP agent list; any gaps documented with remediation date.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Supervisory review logs | Purview audit log | CSV export | 7 years |
| Pre-send hold records | Message trace | CSV | 7 years |
| Supervisor ratio report | PowerShell | Text export | With control documentation |
| Reg BI documentation samples | Review records | Redacted copies | 7 years |
| Agent interaction audit records | Script 5 output | CSV export | 7 years |
| WSP agent coverage gap report | Test 6 results | Document | With control documentation |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110 | Supervisory system and WSP requirements | Supports compliance with supervisory review obligations for AI-assisted activities |
| FINRA 3110(a) | Supervisory system must cover all tools used by associated persons, including agents | Agent audit trail capture and WSP coverage verification confirm agent supervision |
| SEC Reg BI | Care, disclosure, and conflict obligations | Helps meet best-interest documentation requirements for recommendations |
| FINRA 3120 | Supervisory control system testing | Supports annual testing of supervisory effectiveness including agent supervision |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for supervisory workflow issues
- Proceed to [Control 3.7](../3.7/portal-walkthrough.md) for regulatory reporting
- Back to [Control 3.6](../../../controls/pillar-3-compliance/3.6-supervision-oversight.md)
