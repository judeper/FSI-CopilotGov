# Control 3.13: FFIEC IT Examination Handbook Alignment — Portal Walkthrough

Step-by-step portal configuration for aligning Microsoft 365 Copilot governance with the FFIEC IT Examination Handbook requirements across audit, management, development, and operations domains.

## Prerequisites

- **Role:** Compliance Administrator, IT Risk Manager
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal, Compliance Manager

## Steps

### Step 1: Map Copilot Controls to FFIEC Examination Booklets

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Assessments > Create assessment

1. Create a custom assessment titled "FFIEC IT Examination — Copilot AI Governance".
2. Map controls to relevant FFIEC booklets:
   - **Audit booklet** — Controls 3.1 (Audit Logging), 3.12 (Evidence Collection)
   - **Information Security booklet** — Controls 2.1-2.15 (Security and Protection)
   - **Management booklet** — Controls 3.6 (Supervision), 3.8 (Model Risk)
   - **Operations booklet** — Controls 4.1-4.13 (Operations and Monitoring)
3. For each mapping, document the control objective and evidence requirements.

### Step 2: Configure FFIEC-Aligned Audit Trail Requirements

**Portal:** Microsoft Purview portal
**Path:** Solutions > Audit > Audit retention policies

1. Review audit retention policies against FFIEC audit trail requirements.
2. Verify the following are logged and retained:
   - All administrative changes to Copilot configuration
   - User access to Copilot features and interactions
   - Security events related to Copilot data protection
   - Compliance policy violations in Copilot interactions
3. Confirm retention periods meet FFIEC expectations (minimum 5 years for examination-relevant records).

### Step 3: Document Risk Assessment Alignment

**Portal:** Microsoft Purview portal
**Path:** Solutions > Compliance Manager > Assessments > Improvement actions

1. For each FFIEC booklet mapping, create improvement actions documenting:
   - Risk assessment methodology for Copilot-related IT risks
   - Controls implemented to mitigate identified risks
   - Ongoing monitoring procedures
   - Testing frequency and evidence requirements
2. Assign improvement action owners and deadlines.
3. Upload supporting evidence for completed actions.

### Step 4: Prepare Examination Response Framework

**Portal:** Internal documentation / Compliance Manager
**Path:** Examination readiness documentation

1. Create an examination response playbook specific to FFIEC IT examinations of Copilot.
2. Document the points of contact for each examination area.
3. Pre-assemble evidence packages for common examiner requests:
   - AI tool inventory and risk assessment
   - Access controls and authentication evidence
   - Change management documentation
   - Incident response procedures
4. Schedule quarterly mock examination exercises.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| FFIEC assessment completion | Annual | Semi-annual | Continuous |
| Mock examination frequency | Annual | Semi-annual | Quarterly |
| Evidence pre-assembly | On-demand | Pre-assembled | Pre-assembled with index |
| Examiner response time target | 5 business days | 3 business days | 48 hours |

## Regulatory Alignment

- **FFIEC IT Examination Handbook** — Supports compliance across Audit, Information Security, Management, and Operations booklets
- **FFIEC Cybersecurity Assessment Tool** — Helps meet maturity levels for AI-related technology governance
- **OCC Heightened Standards** — Supports compliance with large institution IT governance requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for FFIEC evidence automation
- See [Verification & Testing](verification-testing.md) to validate FFIEC alignment
