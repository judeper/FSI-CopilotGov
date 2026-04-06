# Control 1.10: Vendor Risk Management for Microsoft AI Services — Troubleshooting

Common issues and resolution steps for vendor risk management of Microsoft AI services.

## Common Issues

### Issue 1: Service Trust Portal Access Denied

- **Symptoms:** Unable to sign in to servicetrust.microsoft.com or receiving "Access Denied" when attempting to download compliance documents
- **Root Cause:** The Service Trust Portal requires authentication with a valid organizational account. Some compliance documents may require specific licensing or acceptance of NDA terms.
- **Resolution:**
  1. Sign in with an Entra Global Admin or Purview Compliance Admin account
  2. Accept the Service Trust Portal terms of service if prompted
  3. Verify the account has the required license for accessing restricted documents
  4. For partner or consultant access, request a guest account with appropriate permissions

### Issue 2: Vendor Risk Questionnaire Does Not Cover AI-Specific Risks

- **Symptoms:** Standard vendor risk questionnaire templates do not include questions specific to AI data processing, model governance, or AI incident response
- **Root Cause:** Traditional vendor risk questionnaires were designed before AI services became prevalent and may not address AI-specific risk domains.
- **Resolution:**
  1. Supplement the standard questionnaire with AI-specific sections covering: model governance, training data practices, prompt/response data handling, AI incident response, bias and fairness testing
  2. Reference the NIST AI RMF for AI-specific risk categories
  3. Use Microsoft's AI Impact Assessment documentation to pre-populate answers
  4. Consult with your GRC team to update the standard questionnaire template for future AI vendor assessments

### Issue 3: Microsoft Documentation Changes Between Assessments

- **Symptoms:** Previously documented compliance certifications or AI commitments are updated by Microsoft between assessment cycles, potentially invalidating findings
- **Root Cause:** Microsoft regularly updates compliance documentation, product terms, and AI transparency materials. Annual or semi-annual assessments may not capture interim changes.
- **Resolution:**
  1. Subscribe to Microsoft 365 Message Center notifications for product term changes
  2. Set up automated monitoring using PowerShell Script 2
  3. Assign a team member to review Microsoft AI transparency updates quarterly
  4. Maintain a change log for Microsoft AI-related documentation updates

### Issue 4: Governance Committee Unfamiliar with AI Risk Concepts

- **Symptoms:** Governance committee cannot effectively evaluate AI-specific vendor risks, delaying assessment approval
- **Root Cause:** AI risk concepts (model drift, hallucination, grounding, prompt injection) may be unfamiliar to committee members with traditional financial risk backgrounds.
- **Resolution:**
  1. Provide an AI risk primer to governance committee members before the review session
  2. Translate AI risks into familiar financial risk categories (operational, reputational, compliance)
  3. Use concrete FSI examples to illustrate AI-specific risks
  4. Invite an AI subject matter expert to present findings and answer committee questions

### Issue 5: Residual Risk Acceptance Disagreements

- **Symptoms:** Stakeholders disagree on acceptable residual risk levels for Microsoft AI services, blocking deployment approval
- **Root Cause:** Different risk tolerances between business units, compliance, and security teams. AI risk quantification is still an emerging discipline.
- **Resolution:**
  1. Document each stakeholder's specific concerns with supporting evidence
  2. Propose compensating controls that address the specific concerns
  3. Reference industry benchmarks for AI risk acceptance in financial services
  4. Escalate to the appropriate executive (CRO, CISO) for final risk acceptance decision
  5. Document the risk acceptance decision with clear conditions and review triggers

## Diagnostic Steps

1. **Review assessment status:** Check the vendor risk register for current assessment status
2. **Verify documentation:** Confirm all Microsoft compliance documents are current
3. **Check monitoring:** Review recent Message Center posts and service health alerts
4. **Assess team readiness:** Verify the assessment team has AI risk evaluation capabilities
5. **Review timeline:** Confirm the reassessment schedule is on track

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor documentation gaps in assessment | Vendor risk management team |
| **Medium** | Microsoft compliance certification lapse | Compliance officer and vendor risk team |
| **High** | New AI risk discovered not covered in assessment | CISO and governance committee |
| **Critical** | Microsoft AI service data handling practices change materially | CRO, CISO, Legal, and executive management |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Assessment procedure steps
- [PowerShell Setup](powershell-setup.md) — Monitoring automation
- [Verification & Testing](verification-testing.md) — Assessment validation
