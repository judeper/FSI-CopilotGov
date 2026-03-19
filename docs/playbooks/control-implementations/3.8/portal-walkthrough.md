# Control 3.8: Model Risk Management Alignment (OCC 2011-12 / SR 11-7) — Portal Walkthrough

Step-by-step portal configuration for aligning Microsoft 365 Copilot governance with OCC Bulletin 2011-12, OCC Bulletin 2025-26 (proportionality), and Federal Reserve SR 11-7 model risk management requirements.

<!-- NEEDS_HUMAN_REVIEW: OCC Bulletin 2025-26 is cited throughout this file and related 3.8 files
     as proportionality guidance for community bank model risk management. Verify this bulletin
     number and URL are correct before publishing. If misnumbered, update all 15 references
     across portal-walkthrough.md, troubleshooting.md, and verification-testing.md. -->

## Prerequisites

- **Role:** Compliance Administrator, Model Risk Management Officer
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal, Microsoft Service Trust Portal

## Steps

### Step 1: Document Copilot as a Model in the Model Inventory

**Portal:** Internal Model Risk Management System / Microsoft Service Trust Portal
**Path:** Service Trust Portal > Compliance Reports > AI documentation

1. Access the Microsoft Service Trust Portal for Copilot AI documentation.
2. Download the Microsoft 365 Copilot AI Impact Assessment and Model Card documentation.
3. Determine the appropriate inventory path based on the institution's size and Copilot usage scope:

   **Path A — Community banks applying OCC Bulletin 2025-26 proportionality (Tier 3 / Limited-scope):**
   - Create a model inventory entry with: model name, vendor (Microsoft Corporation), deployment date, usage scope (internal productivity only), risk tier (Tier 3 / Limited-scope), designated model owner, and the proportionality rationale citing OCC Bulletin 2025-26
   - Document that validation approach relies on vendor attestation and periodic output review rather than full MRM lifecycle
   - No additional validation infrastructure required at this tier

   **Path B — Institutions with broader Copilot use (Tier 2 / Medium):**
   - Create a complete model inventory entry covering all fields in the Model Inventory Entry template in Control 3.8
   - Assign risk tier and document rationale for tier selection
   - Include output monitoring schedule and vendor due diligence review cadence

   **Path C — Regulated institutions with client-facing or lending Copilot use (Tier 1 / High):**
   - Create a full model inventory entry with all required OCC 2011-12 fields
   - Include validation plan, output monitoring metrics, fair lending testing protocol, and governance chain
   - Schedule quarterly output review and annual comprehensive MRM assessment

4. For all paths: assign an internal model owner and document their responsibilities

### Step 2: Configure Compliance Manager for Model Risk Assessments

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Assessments > Create assessment

1. Create a custom assessment for "OCC 2011-12 Model Risk Management".
2. Map the following improvement actions to Copilot controls:
   - Model validation documentation
   - Ongoing monitoring procedures
   - Outcome analysis and back-testing
   - Change management processes
3. Assign owners from the model risk management team.

### Step 3: Establish Model Performance Monitoring

**Portal:** Microsoft Purview portal
**Path:** Solutions > Audit > Copilot activity searches

1. Configure monitoring for Copilot output quality indicators:
   - User feedback signals (thumbs up/down on Copilot responses)
   - Error rates and retry patterns
   - Content correction frequency after Copilot generation
2. Create alert policies for significant changes in quality metrics.
3. Set thresholds for model performance degradation alerts.

### Step 4: Configure Third-Party Risk Documentation

**Portal:** Microsoft Service Trust Portal
**Path:** Compliance Reports > SOC reports, AI documentation

1. Download and archive the latest Microsoft SOC 2 Type II report covering Copilot services.
2. Review the AI-specific controls documentation from Microsoft.
3. Document the vendor risk assessment for Copilot AI services per OCC third-party risk guidance.
4. Schedule annual re-assessment aligned with Microsoft's reporting cycle.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Model inventory entry | Required (all sizes; Tier 3 for community banks per OCC Bulletin 2025-26) | Required with tier classification and output monitoring schedule | Required with full OCC 2011-12 fields and annual validation report |
| Model validation frequency | Annual (vendor attestation review) | Semi-annual output quality assessment | Quarterly output review + annual comprehensive assessment |
| Performance monitoring | Manual supervisory review | Automated alerts | Continuous monitoring with defined thresholds |
| Vendor risk assessment | Annual | Semi-annual | Annual + event-driven |
| Proportionality documentation | Required for community banks (cite OCC Bulletin 2025-26) | Document tier rationale | N/A (full framework applies) |

## Regulatory Alignment

- **OCC Bulletin 2011-12** — Supports compliance with model risk management framework requirements
- **OCC Bulletin 2025-26** — Proportionality guidance for community banks; justification path for simplified MRM approach
- **Federal Reserve SR 11-7** — Helps meet supervisory guidance on model risk management
- **OCC Third-Party Risk Management** — Supports vendor risk management for AI services

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for monitoring automation
- See [Verification & Testing](verification-testing.md) to validate model risk controls
