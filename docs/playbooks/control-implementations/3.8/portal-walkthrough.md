# Control 3.8: Model Risk Management Alignment (SR 26-2 / OCC Bulletin 2026-13, applying SR 11-7 / OCC 2011-12 principles to generative AI) — Portal Walkthrough

Step-by-step portal configuration for aligning Microsoft 365 Copilot governance with the firm's approved model-risk policy, the current SR 26-2 / OCC Bulletin 2026-13 model-risk context, and OCC Bulletin 2025-26 community-bank proportionality guidance where applicable.

!!! note "Regulatory applicability"
    Regulatory citations in this playbook identify commonly referenced requirements. Applicability, model classification, and supervisory-source mapping depend on the firm's regulatory status and approved MRM policy; confirm with counsel. See [judeper/OceanSquad#242](https://github.com/judeper/OceanSquad/issues/242).

## Prerequisites

- **Role:** Purview Compliance Admin, Model Risk Management Officer
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal, Microsoft Service Trust Portal

## Steps

### Step 1: Document Copilot as a Model in the Model Inventory

**Portal:** Internal Model Risk Management System / Microsoft Service Trust Portal
**Path:** Service Trust Portal > Compliance Reports > AI documentation

1. Access the Microsoft Service Trust Portal for Copilot AI documentation.
2. Download the Microsoft 365 Copilot AI Impact Assessment and Model Card documentation.
3. Determine the appropriate inventory path based on the institution's size and Copilot usage scope:

   **Path A — Community banks applying OCC Bulletin 2025-26 proportionality as firm policy (Tier 3 / Limited-scope):**
   - Create a model inventory entry with: model name, vendor (Microsoft Corporation), deployment date, usage scope (internal productivity only), risk tier (Tier 3 / Limited-scope), designated model owner, and the proportionality rationale citing OCC Bulletin 2025-26
   - Document that validation approach relies on vendor attestation and periodic output review rather than full MRM lifecycle
   - Do not infer additional validation infrastructure solely from the 2026 revised guidance; approve the validation scope through the firm's model-risk governance process

   **Path B — Institutions with broader Copilot use (Tier 2 / Medium):**
   - Create a complete model inventory entry covering all fields in the Model Inventory Entry template in Control 3.8
   - Assign risk tier and document rationale for tier selection
   - Include output monitoring schedule and vendor due diligence review cadence

   **Path C — Regulated institutions with client-facing or lending Copilot use (Tier 1 / High, if approved by legal/MRM owners):**
   - Create a full model inventory entry with the firm's approved MRM fields (historical OCC 2011-12 fields may be used as an internal-policy reference where approved)
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
| Model inventory entry | Required (all sizes; Tier 3 for community banks only if approved by firm policy and usage scope) | Required with tier classification and output monitoring schedule | Required with full firm-approved MRM fields and validation report |
| Model validation frequency | Annual (vendor attestation review) policy example | Semi-annual output quality assessment policy example | Quarterly output review + annual comprehensive assessment policy example |
| Performance monitoring | Manual supervisory review | Automated alerts | Continuous monitoring with defined thresholds |
| Vendor risk assessment | Annual | Semi-annual | Annual + event-driven |
| Proportionality documentation | Required for community banks (cite OCC Bulletin 2025-26) | Document tier rationale | N/A (full framework applies) |

## Regulatory Alignment

- **OCC Bulletin 2026-13 / Federal Reserve SR 26-2** — Current revised model-risk-management context; generative and agentic AI are outside the guidance's scope
- **OCC Bulletin 2025-26** — Community-bank proportionality clarification; use only as part of a documented firm-policy rationale
- **Historical SR 11-7 / OCC Bulletin 2011-12 principles** — Voluntary internal-policy reference only unless legal/MRM owners approve a current supervisory-source mapping for Copilot
- **OCC Third-Party Risk Management** — Provides a vendor-risk reference for AI services; applicability: confirm

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for monitoring automation
- See [Verification & Testing](verification-testing.md) to validate model risk controls
- Back to [Control 3.8](../../../controls/pillar-3-compliance/3.8-model-risk-management.md)
