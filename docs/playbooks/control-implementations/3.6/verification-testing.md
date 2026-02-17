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

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Supervisory review logs | Purview audit log | CSV export | 7 years |
| Pre-send hold records | Message trace | CSV | 7 years |
| Supervisor ratio report | PowerShell | Text export | With control documentation |
| Reg BI documentation samples | Review records | Redacted copies | 7 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| FINRA 3110 | Supervisory system and WSP requirements | Supports compliance with supervisory review obligations for AI-assisted activities |
| SEC Reg BI | Care, disclosure, and conflict obligations | Helps meet best-interest documentation requirements for recommendations |
| FINRA 3120 | Supervisory control system testing | Supports annual testing of supervisory effectiveness |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for supervisory workflow issues
- Proceed to [Control 3.7](../3.7/portal-walkthrough.md) for regulatory reporting
