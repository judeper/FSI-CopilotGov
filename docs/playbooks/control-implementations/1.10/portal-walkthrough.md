# Control 1.10: Vendor Risk Management for Microsoft AI Services — Portal Walkthrough

Step-by-step procedures for conducting vendor risk assessment of Microsoft AI services used by Microsoft 365 Copilot.

## Prerequisites

- Vendor Risk Management team access and authority
- Microsoft Service Trust Portal access (servicetrust.microsoft.com)
- Third-party risk management framework or questionnaire (e.g., SIG, CAIQ)
- Governance committee sponsorship for vendor assessment

## Steps

### Step 1: Access Microsoft Service Trust Portal

**Portal:** Microsoft Service Trust Portal
**Path:** servicetrust.microsoft.com > Sign in with organizational credentials

Access the Service Trust Portal to review Microsoft's compliance documentation, audit reports, and data protection assessments relevant to AI services. Download the following key documents:
- SOC 2 Type II report for Microsoft 365
- ISO 27001 certificate for Azure and Microsoft 365
- Microsoft AI Transparency Notes, Data Protection Addendum (DPA), and Service Trust Portal documentation
- Data Processing Agreement (DPA) and product terms

### Step 2: Review Microsoft's AI Transparency Documentation

**Portal:** Microsoft Trust Center
**Path:** microsoft.com/trust-center > AI > Responsible AI

Review Microsoft's responsible AI commitments, transparency reports, and AI governance frameworks. Document:
- Microsoft's AI principles and how they apply to Copilot
- Data handling practices for Copilot prompts and responses
- Training data usage policies (tenant data is not used for model training)
- Sub-processor and third-party data processing disclosures

### Step 3: Complete Vendor Risk Questionnaire

Using your organization's vendor risk assessment framework, complete the assessment for Microsoft AI services. Key areas to evaluate:
- **Data security:** How is data protected during AI processing?
- **Data residency:** Where is data processed and stored?
- **Model governance:** How are AI models updated and tested?
- **Incident response:** What is Microsoft's AI incident response process?
- **Contractual protections:** What SLAs, indemnification, and liability terms apply?

### Step 4: Document Risk Findings and Mitigations

**Portal:** Internal GRC platform or risk register

Record all identified risks from the vendor assessment along with:
- Risk severity rating (Critical, High, Medium, Low)
- Existing mitigations provided by Microsoft
- Additional mitigations required by the organization
- Residual risk acceptance decisions with governance committee approval

### Step 5: Establish Ongoing Monitoring

Set up ongoing vendor monitoring processes:
- Subscribe to Microsoft 365 Message Center for service changes
- Monitor Microsoft Security Response Center for AI-related advisories
- Schedule annual vendor risk reassessment
- Track Microsoft compliance certification renewal dates

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Complete vendor risk assessment and document findings before Copilot deployment |
| **Recommended** | Integrate Microsoft AI services into ongoing vendor monitoring program with semi-annual reassessment |
| **Regulated** | Comprehensive third-party risk assessment per OCC/FFIEC guidelines; board-level reporting on AI vendor risk; contractual review by legal counsel |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated monitoring configuration
- See [Verification & Testing](verification-testing.md) to validate assessment completeness
- Review [Control 2.7: Data Residency](../../../controls/pillar-2-security/2.7-data-residency.md) for Data Residency considerations
- Back to [Control 1.10](../../../controls/pillar-1-readiness/1.10-vendor-risk-management.md)
