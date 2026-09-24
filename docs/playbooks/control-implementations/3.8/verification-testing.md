# Control 3.8: Model Risk Management Alignment (SR 26-2 / OCC Bulletin 2026-13, applying SR 11-7 / OCC 2011-12 principles to generative AI) — Verification & Testing

Test cases and evidence collection procedures to validate alignment with OCC and Federal Reserve model risk management requirements for Copilot.

!!! note "Regulatory applicability"
    Regulatory citations identify commonly referenced requirements. Applicability, record classification, and retention periods are a firm and counsel determination; this framework does not assert that any regulation applies or is satisfied. See the [Regulatory Applicability Questions](../../../reference/regulatory-applicability-questions.md) appendix.

## Test Cases

### Test 1: Model Inventory Completeness

- **Objective:** Verify that the Copilot model inventory entry contains all required fields appropriate to the institution's tier classification
- **Steps:**
  1. Review the model inventory entry for Microsoft 365 Copilot.
  2. Verify all required fields are populated: model name, version, purpose, inputs, outputs, risk tier, owner, validation date.
  3. Confirm the risk tier classification follows the firm's model tiering methodology and reflects actual Copilot usage scope (Tier 1/2/3 as appropriate).
  4. Verify the model card references Microsoft's published AI documentation.
  5. For community banks applying OCC Bulletin 2025-26 proportionality: verify the tier selection rationale documents usage scope, institution characteristics, and the OCC Bulletin 2025-26 citation.
- **Expected Result:** Model inventory entry is complete with all required fields populated; tier classification is documented with supporting rationale.
- **Evidence:** Model inventory entry export with all fields verified; proportionality rationale documentation if applicable.

### Test 2: Proportionality Classification Verification

- **Objective:** Verify that the Copilot model inventory entry includes a proportionality classification consistent with OCC Bulletin 2025-26 and that the tier reflects actual usage
- **Steps:**
  1. Review the model inventory entry for the risk tier and classification rationale.
  2. Confirm the inventory entry documents one of: Tier 3 (limited-scope / internal productivity), Tier 2 (business decision support), or Tier 1 (client-facing / lending workflows).
  3. Cross-reference the tier against the approved use-case register — if client-facing or lending uses are approved, Tier 3 should not be selected.
  4. For Tier 3 classifications at community banks: verify OCC Bulletin 2025-26 is cited and the proportionality rationale is documented in writing.
  5. Verify the tier classification has been reviewed and approved by the designated model owner or model risk committee.
- **Expected Result:** Model inventory entry includes a proportionality classification with documented rationale; tier is consistent with actual usage scope.
- **Evidence:** Model inventory entry with tier field and proportionality rationale; approved use-case register for cross-reference.

### Test 3: Performance Monitoring Effectiveness

- **Objective:** Confirm that model performance monitoring detects quality degradation
- **Steps:**
  1. Run the Copilot feedback metrics script for the current reporting period.
  2. Compare satisfaction rates against the baseline established during initial deployment.
  3. Verify that alert thresholds are configured for significant performance changes.
  4. Test that alerts trigger when metrics cross defined thresholds.
- **Expected Result:** Performance monitoring is operational, baseline comparison is available, and alerts function correctly.
- **Evidence:** Performance metrics report and alert policy configuration screenshots.

### Test 4: Vendor Risk Documentation Currency

- **Objective:** Validate that third-party risk documentation for Microsoft Copilot is current
- **Steps:**
  1. Verify the latest Microsoft SOC 2 Type II report is on file and within 12 months.
  2. Confirm the AI Impact Assessment from Microsoft Service Trust Portal is reviewed and current.
  3. Check that the vendor risk assessment is dated within the last 12 months.
  4. Verify that Microsoft's data processing terms are reviewed and documented.
- **Expected Result:** All vendor risk documentation is current and on file.
- **Evidence:** Document index showing file dates and review attestations.

### Test 5: Model Validation Documentation

- **Objective:** Confirm that the Copilot model validation process is documented and current
- **Steps:**
  1. Review the model validation documentation for the current assessment period.
  2. Verify that the validation includes: conceptual soundness, data quality assessment, outcome analysis, and limitations.
  3. Confirm an independent review was performed (separate from model users).
  4. Verify that identified limitations and recommendations are tracked for remediation.
- **Expected Result:** Model validation is documented, independently reviewed, and remediation items are tracked.
- **Evidence:** Validation report with independent reviewer sign-off and remediation tracking log.

## Evidence Collection

| Evidence Item | Source | Format | Retention |
|--------------|--------|--------|-----------|
| Model inventory entry | MRM system | PDF/Export | Life of model + 5 years; retention schedule: confirm |
| Proportionality rationale | MRM system | PDF/Document | Life of model + 5 years; retention schedule: confirm |
| Performance metrics | PowerShell | CSV | 7 years; retention schedule: confirm |
| Vendor risk documentation | Service Trust Portal | PDF | 7 years; retention schedule: confirm |
| Validation report | MRM system | PDF | Life of model + 5 years; retention schedule: confirm |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| OCC Bulletin 2026-13 / SR 26-2 | Current model-risk-management context; generative and agentic AI are outside the revised guidance's scope | Provides current context while legal/MRM owners decide the Copilot-specific framework |
| OCC Bulletin 2025-26 | Community-bank proportionality context | Provides a documented firm-policy rationale for simplified MRM where applicable; firms should confirm with legal/MRM owners |
| Historical SR 11-7 / OCC Bulletin 2011-12 principles | Voluntary internal-policy reference unless legal/MRM owners approve a current supervisory-source mapping | Can structure model inventory, validation, and monitoring artifacts without claiming current supervisory coverage for generative AI |
| OCC Third-Party Risk | Vendor risk assessment | Provides a third-party risk management reference for AI vendors; applicability: confirm |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for model risk management issues
- Proceed to [Control 3.9](../3.9/portal-walkthrough.md) for AI disclosure and transparency
- Back to [Control 3.8](../../../controls/pillar-3-compliance/3.8-model-risk-management.md)
