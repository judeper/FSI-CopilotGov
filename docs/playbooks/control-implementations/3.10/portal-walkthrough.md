<!-- Educational reference only — not legal advice. Verify all citations against current regulations. -->

# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Portal Walkthrough

Step-by-step portal configuration for implementing privacy controls that support compliance with SEC Regulation S-P, including the amendments proposed in 2023 and adopted in May 2024 ([SEC Release No. 34-100155](https://www.sec.gov/files/rules/final/2024/34-100155.pdf)), when using Microsoft 365 Copilot with consumer financial information.

## Prerequisites

- **Role:** Purview Compliance Admin or another role Microsoft documents for editing Copilot DLP policies; Privacy Officer for the institution's review
- **License:** Capability-specific. Prompt safeguards are available to all Microsoft Copilot and Copilot Chat users, subject to feature rollout. File/email processing restrictions require an eligible E5, Microsoft Purview Suite, Information Protection and Governance, or listed Office 365 E5 entitlement
- **Access:** Microsoft Purview portal

## Steps

### Step 1: Configure Sensitive Information Types for Consumer Financial Data

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information Protection > Classifiers > Sensitive info types

1. Review built-in sensitive information types relevant to Reg S-P:
   - U.S. Social Security Number (SSN)
   - Credit Card Number
   - U.S. Bank Account Number
   - U.S. Individual Taxpayer Identification Number (ITIN)
2. Create custom sensitive information types for firm-specific financial data:
   - Account numbers matching your firm's format
   - Client identifiers and portfolio numbers
3. Test each SIT against sample data to verify accuracy.

### Step 2: Create DLP Policies for Consumer Financial Information in Copilot

**Portal:** Microsoft Purview portal
**Path:** Solutions > Data loss prevention > Policies > Create policy

1. Select **Custom** > **Custom policy**, and name the policy "FSI-RegSP-Copilot-Privacy-Protection". The Copilot location isn't available in the regulatory templates.
2. On **Locations**, turn on **Microsoft 365 Copilot and Copilot Chat**. All other locations are disabled for this policy.
3. Configure the supported rule/action pairs as separate rules:
   - **Sensitivity labels** > **Prevent Copilot from processing content**. The labeled file or email content isn't used in the response, although the item can still appear as a citation. This applies to supported stored/open files and emails sent on or after January 1, 2025; calendar invites aren't supported.
   - **Sensitive information types** > **Prevent Copilot from processing content > Processing prompts**. This blocks a response when the text typed directly into the prompt contains a configured SIT. The capability is in preview and rolling out; confirm that it has reached the tenant.
   - **Sensitive information types** > **Prevent Copilot from processing content > Performing Web Searches**. This blocks external web search for a matching typed prompt while permitting a response from allowed internal Microsoft 365 sources.
   - **Email is received from > External users** > **Prevent Copilot from processing content**. This preview action evaluates sender-domain metadata, not the email body, and excludes matching external email from grounding, summarization, and citation. Confirm tenant availability before relying on it.
   - **Explicit coverage:** Microsoft lists Microsoft 365 Copilot, Copilot Chat, and Copilot in Word, Excel, and PowerPoint for the label/prompt features. Don't infer universal Copilot-in-Outlook or Copilot-in-Teams coverage from this location.
4. Don't combine sensitivity-label and SIT conditions in one rule. Use separate rules in the policy.
5. Configure alerts and notifications, which are supported for this location. Start in simulation mode, validate with synthetic data, and then use change control to move to enforcement. Policy updates can take up to four hours to appear in Copilot experiences.
6. Scope the policy to the approved user population. The location doesn't support administrative units.
7. Record the direct-upload limitation: DLP doesn't scan the contents of files uploaded directly into prompts; it evaluates the text typed into the prompt. Protect uploaded content at its source with permissions and labels.
8. In policy details or Security & Compliance PowerShell output, verify that the location contains GUID `470f2276-e011-4e9d-a6ec-20768be3a4b0` and that `EnforcementPlanes` includes `CopilotExperiences`.
9. Separately configure **Allow web search in Copilot** in the [Cloud Policy service for Microsoft 365](https://config.office.com) for the approved user/group scope.

### Step 3: Configure Information Barriers for Privacy Segregation

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information barriers > Segments and policies

1. Review existing information barrier segments.
2. Verify that segments prevent Copilot from surfacing consumer financial data across business unit boundaries where required by Reg S-P.
3. Create or update barrier policies to prevent cross-segment data access via Copilot grounding.
4. Document that Information Barriers don't support the SharePoint Embedded content used by Copilot Pages and Copilot Notebooks. Where that limitation conflicts with approved use, use the available admin policies to disable creation.

### Step 4: Enable Privacy Impact Assessment for Copilot Data Flows

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information Protection > Explorers > Data explorer; Solutions > DSPM > Discover > Activity explorer

1. Use Data explorer to review where consumer financial information is detected and how it is labeled.
2. Document the data flow from source systems through Copilot interactions.
3. In current DSPM, use **Discover > Activity explorer > AI activities** to review sensitive AI interactions and DLP rule matches. Viewing prompt and response bodies requires the additional Content Explorer Content Viewer and Microsoft Purview Data Security AI Content Viewer permissions.
4. Assess whether Copilot prompts and responses may expose nonpublic personal information (NPI).
5. Configure source access controls and the supported Copilot DLP actions to limit NPI processing.

### Step 5: Configure Response, Affected-Individual Notification, and Service-Provider Oversight

**Portal:** Microsoft Purview portal / Internal incident response documentation
**Path:** Microsoft Purview > Data Loss Prevention > Alerts; Microsoft Purview > Audit; Internal IRP documentation system

The [final rule text](https://www.ecfr.gov/current/title-17/chapter-II/part-248/section-248.30) assigns the response program to Rule 248.30(a)(3), affected-individual notification to (a)(4), and service-provider oversight and provider-to-institution notification to (a)(5). Configure and evidence those distinct responsibilities for Copilot NPI incidents:

1. **Document Copilot NPI scenarios in the written response program (Rule 248.30(a)(3)):**
   - Scenario: Copilot surfaces client NPI to unauthorized user (oversharing or permission misconfiguration)
   - Scenario: Copilot-drafted communication contains NPI that should not have been disclosed
   - Scenario: Copilot Chat response aggregates NPI from multiple sources into a single response accessible to an unauthorized party
   For each scenario, document: detection method, severity classification, scope assessment, escalation path, containment and recovery steps, and notification workflow.

2. **Configure and review Copilot DLP alerts:**
   - Navigate to **Microsoft Purview > Data Loss Prevention > Alerts**
   - Configure alerts on the applicable Copilot DLP rules and verify that synthetic rule matches create the expected alert
   - Set alert severity to High for SSN/account credential exposure; Medium for other NPI types
   - Configure alerts to route to the designated Privacy Officer and Compliance team
   - In **Microsoft Purview > Audit**, search **Copilot activities** / **Interacted with Copilot** for `CopilotInteraction` evidence

3. **Operate service-provider oversight and notification intake (Rule 248.30(a)(5)):**
   - Maintain written policies and procedures for due diligence and monitoring of applicable service providers.
   - When a provider reports a qualifying breach in a customer-information system it maintains, capture the provider's awareness time, the institution's receipt time, the provider-reported scope, and the provider-to-institution 72-hour timing evaluation. The 72-hour trigger is provider awareness, not the institution's detection time.
   - On receipt, initiate the institution's Rule 248.30(a)(3) response program. Keep designated tenant administrator contacts current and monitor Microsoft 365 Service health as part of the institution's tested intake process for Microsoft-determined incidents.
   - Do not state that Rule 248.30(a)(5) imposes a general written-contract requirement. The rule permits a written agreement for a provider to notify affected individuals on the institution's behalf, but the institution retains that notification obligation.

4. **Maintain the affected-individual notification process separately (Rule 248.30(a)(4)):**
   - Document the reasonable investigation and determination whether sensitive customer information was, or is reasonably likely to have been, used in a manner that would result in substantial harm or inconvenience.
   - If notification is required, track the institution's affected-individual notification clock separately: notice is due as soon as practicable and no later than 30 days after the institution becomes aware of qualifying unauthorized access or use.

### Step 6: Test the Incident Response Program Configuration

1. Conduct a tabletop exercise simulating a Copilot NPI incident.
2. Walk through each stage of the incident response procedures per the institution's written program.
3. Verify provider-to-institution notification intake, provider-awareness timing evidence, and service-provider oversight are documented and tested.
4. Verify the Rule 248.30(a)(4) affected-individual notification decision and clock are not conflated with the provider timing evaluation.
5. Document the exercise outcomes and any gaps identified.
6. Update the response program based on exercise findings.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| DLP for consumer financial data | Simulate supported rules | Exclude labeled sources and restrict sensitive web searches | Enforce validated supported rules; enable prompt blocking and external-email exclusion only where their previews have reached the tenant |
| Information barriers | Assess applicability | Business unit boundaries on supported sources | Full supported-source segregation; disable Pages/Notebooks where the SharePoint Embedded gap isn't acceptable |
| NPI detection in Copilot | Audit and DSPM review | DLP alerts and review cadence | Enforced supported actions and documented alert response |
| Privacy impact assessment | Annual | Semi-annual | Annual + event-driven |
| Written response program | Required (Rule 248.30(a)(3)) | With Copilot scenarios | With tabletop exercise documentation |
| Affected-individual notification | Document Rule 248.30(a)(4) determination | Test the institution's separate notification clock | Retain investigation and notice evidence |
| Service-provider oversight and notice | Written due diligence/monitoring procedures (Rule 248.30(a)(5)) | Test provider awareness, institution receipt, reported scope, and timing evidence | Quarterly drill without asserting a general written-contract requirement |

## Regulatory Alignment

- **[SEC Final Rule, Release No. 34-100155 (May 2024)](https://www.sec.gov/files/rules/final/2024/34-100155.pdf)** — Primary SEC source for the Reg S-P amendments proposed in 2023 and adopted in 2024
- **[Federal Register, 89 FR 47688 (June 3, 2024), document 2024-11116](https://www.federalregister.gov/documents/2024/06/03/2024-11116/regulation-s-p-privacy-of-consumer-financial-information-and-safeguarding-customer-information)** — Machine-checkable publication of the final rule
- **[SEC Reg S-P Rule 248.30(a)(3)](https://www.ecfr.gov/current/title-17/chapter-II/part-248/section-248.30)** — Response program for unauthorized access to or use of customer information
- **[SEC Reg S-P Rule 248.30(a)(4)](https://www.ecfr.gov/current/title-17/chapter-II/part-248/section-248.30)** — Affected-individual notification obligation, determination, timing, and contents
- **[SEC Reg S-P Rule 248.30(a)(5)](https://www.ecfr.gov/current/title-17/chapter-II/part-248/section-248.30)** — Service-provider oversight and provider-to-institution notification within 72 hours of provider awareness of a qualifying breach
- **SEC Reg S-P (Rule 30)** — Supports compliance with safeguarding requirements for customer records and information
- **GLBA Title V** — Helps meet financial privacy requirements for nonpublic personal information
- **GLBA §501(b)** — Helps meet safeguards provisions for nonpublic personal information at banks and broker-dealers (the statutory authority for SEC Reg S-P safeguards for SEC-regulated entities; the FTC Safeguards Rule is a separate implementing regulation that applies to FTC-jurisdiction institutions, not to SEC-regulated broker-dealers)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for privacy control automation
- See [Verification & Testing](verification-testing.md) to validate privacy protections
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
