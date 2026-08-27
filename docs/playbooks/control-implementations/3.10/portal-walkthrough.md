<!-- Educational reference only — not legal advice. Verify all citations against current regulations. -->

# Control 3.10: SEC Reg S-P — Privacy of Consumer Financial Information — Portal Walkthrough

Step-by-step portal configuration for implementing privacy controls that support compliance with SEC Regulation S-P, including the amendments proposed in 2023 and adopted in May 2024 (SEC Release No. 34-100155), when using Microsoft 365 Copilot with consumer financial information.

## Prerequisites

- **Role:** Purview Compliance Admin, Privacy Officer
- **License:** Required Microsoft 365 and Purview licensing for the features used; verify current eligibility in the applicable Microsoft service descriptions
- **Access:** Microsoft Purview portal

## Steps

### Step 1: Configure Sensitive Information Types for Consumer Financial Data

**Portal:** Microsoft Purview portal
**Path:** Information Protection > Classifiers > Sensitive info types

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

1. Create a DLP policy named "FSI-RegSP-Copilot-Privacy-Protection".
2. Select the **Microsoft 365 Copilot and Copilot Chat** location under the Custom policy template and leave non-Copilot workloads disabled in this policy.
3. Configure rules:
   - **Low volume (1-9 instances):** Notify the user with a policy tip; take no restrictive action.
   - **High volume (10+ instances):** **Prevent Copilot from processing content > Processing prompts** and, where approved, **> Performing Web Searches**.
4. Configure alerting **on each rule**, in the rule's **Incident reports** section — this is what actually produces the notification, and it is required for the high-volume rule to deliver on the "notify the compliance team" commitment:
   - Set **Use this severity level in admin alerts and reports** to `Medium` for the low-volume rule and `High` for the high-volume rule.
   - Turn **Send an alert to admins when a rule match occurs** to **On**.
   - Under **Send email alerts to these people (optional)**, select **+ Add or remove users** and add the Privacy Officer and the compliance team distribution list.
   - Choose the alert frequency (for example, **Send alert every time an activity matches the rule**) that matches the institution's triage capacity.
   - Leave the report content at detection metadata; do not add original content, so detected NPI isn't copied into notification email.
5. Scope the policy to **all users who can reach Microsoft Copilot or Copilot Chat — not only users with a paid Microsoft 365 Copilot add-on.** Copilot Chat is available at no extra cost to users holding common Microsoft 365, Office 365, and Teams licenses, and organizational content can enter Copilot Chat through uploaded and pasted content, `/` file references, and agents. Microsoft's own default Copilot DLP policy ships scoped to all tenant users and groups, and the PowerShell equivalent in [PowerShell Setup](powershell-setup.md) uses `"Inclusions":[{"Type":"Tenant","Identity":"All"}]`. If the institution deliberately narrows the scope, document which Copilot and Copilot Chat users are left uncovered and why.
6. Set the policy to **Turn the policy on immediately** when you are ready to enforce. A policy left in simulation mode logs events but takes no action on prompts.
7. In policy details (or Security & Compliance PowerShell output), verify this policy resolves to `Mode=Enable`, `EnforcementPlanes` includes `CopilotExperiences`, and `Locations` contains the documented Copilot location GUID `470f2276-e011-4e9d-a6ec-20768be3a4b0`, and that both rules show their intended actions and alert configuration. Script 1b in [PowerShell Setup](powershell-setup.md) performs these checks and fails closed.

> **Documented Copilot DLP limitations (read before relying on this control):** In the **Microsoft 365 Copilot and Copilot Chat** location, sensitive information type (SIT) enforcement evaluates **the text a user types into the prompt**. The two documented SIT actions are **Prevent Copilot from processing content > Processing prompts** and **> Performing Web Searches**. Microsoft does not document a DLP action that inspects or blocks the text of a **generated Copilot response**; sensitive data in responses can be *observed* after the fact (DSPM / Activity explorer **AI activities**, Audit, eDiscovery) but is not blocked by this control. DLP also can't scan the contents of files uploaded directly into a prompt — only typed prompt text is checked. SIT-based prompt blocking is in preview and rolling out. The sensitivity label condition covers emails sent on or after January 1, 2025; calendar invites and Admin units are not supported. Policy updates can take up to four hours to take effect in the Copilot experience.

### Step 3: Configure Information Barriers for Privacy Segregation

**Portal:** Microsoft Purview portal
**Path:** Solutions > Information barriers > Segments and policies

1. Review existing information barrier segments.
2. Verify that segments prevent Copilot from surfacing consumer financial data across business unit boundaries where required by Reg S-P.
3. Create or update barrier policies to prevent cross-segment data access via Copilot grounding.

### Step 4: Enable Privacy Impact Assessment for Copilot Data Flows

**Portal:** Microsoft Purview portal
**Path:** Solutions > Data classification > Content Explorer (classic)

1. Use Content Explorer (classic) to identify where consumer financial information resides.
2. Document the data flow from source systems through Copilot interactions.
3. Assess whether Copilot prompts and responses may expose nonpublic personal information (NPI). For the response side this is an **observation** exercise — use DSPM / Activity explorer **AI activities** to see SIT detections in prompts and responses. The Copilot DLP location does not block response text.
4. Configure access controls, sensitivity labels, and information barriers to limit which NPI Copilot can ground on in the first place; permission and label scoping — not response inspection — is what constrains NPI in Copilot responses.

### Step 5: Configure the Incident Response Program for Copilot NPI Events (Reg S-P Rule 248.30(a)(4))

**Portal:** Microsoft Purview portal / Internal incident response documentation
**Path:** Microsoft Purview > Data loss prevention > Policies (rule **Incident reports** settings); Microsoft Purview > Data loss prevention > Alerts; Internal IRP documentation system

The amended Reg S-P requires a written incident response program addressing unauthorized access to or use of customer information. Configure the following for Copilot NPI incident coverage:

1. **Document Copilot NPI scenarios in the written IRP:**
   - Scenario: Copilot surfaces client NPI to unauthorized user (oversharing or permission misconfiguration)
   - Scenario: Copilot-drafted communication contains NPI that should not have been disclosed
   - Scenario: Copilot Chat response aggregates NPI from multiple sources into a single response accessible to an unauthorized party
   For each scenario, document: detection method, severity classification, escalation path, containment steps, and notification workflow.

2. **Define the alerts on the Copilot DLP rules themselves:**
   - Alert generation, recipients, and severity for Copilot NPI events are configured in each rule's **Incident reports** section, as described in Step 2.4 — that is the alert definition surface for this control.
   - Set severity to **High** for the SSN / account credential rule and **Medium** for other NPI rules, and add the Privacy Officer and compliance team as email alert recipients.
   - Re-open each rule after saving and confirm the **Incident reports** section still shows the alert toggle on, the severity, and the recipients. An unsaved or empty recipient list means no notification is produced.
   - Microsoft Defender XDR and the Purview **Data loss prevention > Alerts** dashboard are where these alerts are **investigated and triaged**. They are not a substitute for defining the alert on the rule — if the rule has no alert configured, nothing arrives in either surface.

3. **Verify service provider notification arrangements (Reg S-P Rule 248.30(a)(3)):**
   - Verify that service provider agreements require Microsoft to notify the institution within 72 hours of becoming aware of unauthorized access to customer information
   - Document the institution's process for receiving and acting on service provider notifications

4. **Set up the incident response notification timeline:**
   - Internal escalation: Per the institution's incident response procedures
   - Customer notification: Per amended Reg S-P requirements

### Step 6: Test the Incident Response Program Configuration

1. Conduct a tabletop exercise simulating a Copilot NPI incident.
2. Walk through each stage of the incident response procedures per the institution's written program.
3. Verify that service provider notification arrangements are documented and tested.
4. Document the exercise outcomes and any gaps identified.
5. Update the IRP based on exercise findings.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| DLP for consumer financial data | Notify | Block external | Block all unauthorized |
| Information barriers | Optional | Business unit boundaries | Full segregation |
| NPI detection in Copilot | Audit only | Warn users | Block and log |
| Privacy impact assessment | Annual | Semi-annual | Annual + event-driven |
| Written incident response program | Required (Rule 248.30(a)(4)) | With Copilot scenarios | With tabletop exercise documentation |
| Service provider notification requirement | Verify agreements | Test in tabletop | Quarterly drill |

## Regulatory Alignment

- **SEC Final Rule, Release No. 34-100155 (May 2024)** — Primary SEC source for the Reg S-P amendments proposed in 2023 and adopted in 2024
- **SEC Reg S-P Rule 248.30(a)(3)** — Requires institutions to adopt policies requiring service providers to notify the institution within 72 hours of unauthorized access to customer information
- **SEC Reg S-P Rule 248.30(a)(4)** — Mandatory written incident response program; Copilot-specific scenarios must be included
- **SEC Reg S-P (Rule 30)** — Supports compliance with safeguarding requirements for customer records and information
- **GLBA Title V** — Helps meet financial privacy requirements for nonpublic personal information
- **GLBA §501(b)** — Helps meet safeguards provisions for nonpublic personal information at banks and broker-dealers (the statutory authority for SEC Reg S-P safeguards for SEC-regulated entities; the FTC Safeguards Rule is a separate implementing regulation that applies to FTC-jurisdiction institutions, not to SEC-regulated broker-dealers)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for privacy control automation
- See [Verification & Testing](verification-testing.md) to validate privacy protections
- Back to [Control 3.10](../../../controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md)
