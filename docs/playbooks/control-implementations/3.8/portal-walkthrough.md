# Control 3.8: Model Risk Management Alignment (OCC 2011-12 / SR 11-7) — Portal Walkthrough

Step-by-step portal configuration for aligning Microsoft 365 Copilot governance with OCC Bulletin 2011-12 and Federal Reserve SR 11-7 model risk management requirements.

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
3. Create a model inventory entry for M365 Copilot with:
   - Model name, version, and deployment date
   - Model purpose and use cases within the organization
   - Data inputs (organizational content, prompts, grounding data)
   - Model outputs (generated text, summaries, recommendations)
   - Risk tier classification (per OCC guidance)

### Step 2: Configure Compliance Manager for Model Risk Assessments

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Compliance Manager > Assessments > Create assessment

1. Create a custom assessment for "OCC 2011-12 Model Risk Management".
2. Map the following improvement actions to Copilot controls:
   - Model validation documentation
   - Ongoing monitoring procedures
   - Outcome analysis and back-testing
   - Change management processes
3. Assign owners from the model risk management team.

### Step 3: Establish Model Performance Monitoring

**Portal:** Microsoft Purview Compliance Portal
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
| Model inventory entry | Optional | Required | Required with tier classification |
| Model validation frequency | Annual | Semi-annual | Quarterly |
| Performance monitoring | Manual | Automated alerts | Continuous monitoring |
| Vendor risk assessment | Annual | Semi-annual | Annual + event-driven |

## Regulatory Alignment

- **OCC 2011-12** — Supports compliance with model risk management framework requirements
- **Federal Reserve SR 11-7** — Helps meet supervisory guidance on model risk management
- **OCC Third-Party Risk Management** — Supports vendor risk management for AI services

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for monitoring automation
- See [Verification & Testing](verification-testing.md) to validate model risk controls
