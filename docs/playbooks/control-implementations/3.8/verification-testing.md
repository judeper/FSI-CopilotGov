# Control 3.8: Model Risk Management Alignment (OCC 2011-12 / SR 11-7) — Verification & Testing

Test cases and evidence collection procedures to validate alignment with OCC and Federal Reserve model risk management requirements for Copilot.

## Test Cases

### Test 1: Model Inventory Completeness

- **Objective:** Verify that the Copilot model inventory entry contains all OCC 2011-12 required fields
- **Steps:**
  1. Review the model inventory entry for Microsoft 365 Copilot.
  2. Verify all required fields are populated: model name, version, purpose, inputs, outputs, risk tier, owner, validation date.
  3. Confirm the risk tier classification follows the firm's model tiering methodology.
  4. Verify the model card references Microsoft's published AI documentation.
- **Expected Result:** Model inventory entry is complete with all required OCC 2011-12 fields populated.
- **Evidence:** Model inventory entry export with all fields verified.

### Test 2: Performance Monitoring Effectiveness

- **Objective:** Confirm that model performance monitoring detects quality degradation
- **Steps:**
  1. Run the Copilot feedback metrics script for the current reporting period.
  2. Compare satisfaction rates against the baseline established during initial deployment.
  3. Verify that alert thresholds are configured for significant performance changes.
  4. Test that alerts trigger when metrics cross defined thresholds.
- **Expected Result:** Performance monitoring is operational, baseline comparison is available, and alerts function correctly.
- **Evidence:** Performance metrics report and alert policy configuration screenshots.

### Test 3: Vendor Risk Documentation Currency

- **Objective:** Validate that third-party risk documentation for Microsoft Copilot is current
- **Steps:**
  1. Verify the latest Microsoft SOC 2 Type II report is on file and within 12 months.
  2. Confirm the AI Impact Assessment from Microsoft Service Trust Portal is reviewed and current.
  3. Check that the vendor risk assessment is dated within the last 12 months.
  4. Verify that Microsoft's data processing terms are reviewed and documented.
- **Expected Result:** All vendor risk documentation is current and on file.
- **Evidence:** Document index showing file dates and review attestations.

### Test 4: Model Validation Documentation

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
| Model inventory entry | MRM system | PDF/Export | Life of model + 5 years |
| Performance metrics | PowerShell | CSV | 7 years |
| Vendor risk documentation | Service Trust Portal | PDF | 7 years |
| Validation report | MRM system | PDF | Life of model + 5 years |

## Compliance Mapping

| Regulation | Requirement | How This Control Helps |
|-----------|-------------|----------------------|
| OCC 2011-12 | Model inventory and validation | Supports compliance with model risk management framework |
| SR 11-7 | Ongoing monitoring and outcome analysis | Helps meet supervisory expectations for model performance tracking |
| OCC Third-Party Risk | Vendor risk assessment | Supports third-party risk management requirements for AI vendors |

## Next Steps

- Review [Troubleshooting](troubleshooting.md) for model risk management issues
- Proceed to [Control 3.9](../3.9/portal-walkthrough.md) for AI disclosure and transparency
