# Control 2.1: DLP Policies for M365 Copilot Interactions — Portal Walkthrough

Step-by-step portal configuration for deploying Data Loss Prevention policies that govern M365 Copilot interactions and protect sensitive data. Control 2.1 requires configuring three architecturally distinct Copilot DLP rule types — label-based response blocking, SIT-based prompt blocking, and SIT-based web-search restriction. They address different enforcement points and must be configured as separate DLP rules; separate policies may be used when operationally needed.

## Prerequisites

- Purview Compliance Admin role
- Microsoft 365 E5 or E5 Compliance license
- Sensitivity information types defined for FSI data (account numbers, SSNs, financial data)
- Sensitivity label taxonomy deployed (see Control 2.2 — label-based DLP depends on labels)
- DLP policy strategy approved by governance committee

## Policy Type Reference

| Policy Type | What It Protects | Enforcement Point |
|-------------|-----------------|-------------------|
| **Type 1: Label-Based Response Blocking** | Prevents Copilot from surfacing labeled files/emails in responses | Copilot's grounding phase (response side) |
| **Type 2: SIT-Based Prompt Blocking** | Prevents users from submitting sensitive data in prompts | User's prompt (before Copilot processes it) |
| **Type 3: SIT-Based Web Search Restriction** | Prevents sensitive prompt data from being sent to external web search providers | User prompt, external web-search grounding path |

These rule types must be configured as separate DLP rules. Sensitivity-label and SIT conditions cannot be combined within a single DLP rule, but separate rules can exist within the same policy.

## Steps

### Step 1: Navigate to DLP Policy Management

**Portal:** Microsoft Purview
**Path:** Purview > Data Loss Prevention > Policies > Create Policy

Access the DLP policy creation wizard. The procedures below use the **Microsoft 365 Copilot and Copilot Chat** location. Selecting this location disables all other locations in that policy, so create separate policies for Exchange, SharePoint, OneDrive, Teams, or Devices.

**Alternative access for default Copilot DLP policy:**
**Path:** Microsoft 365 Admin Center > Copilot > Security

The MAC Security tab provides quick access to the Microsoft-deployed default Copilot DLP policy (in simulation mode, GA January 2026) and links to Purview DLP for full policy management.

### Step 2: Create the Label-Based Response Blocking Policy (Type 1)

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Configure the label-based response blocking policy:
- **Name:** "FSI Copilot DLP — Label-Based Response Blocking"
- **Locations:** Microsoft 365 Copilot and Copilot Chat
- **Conditions:** "Content contains sensitivity label" — select Highly Confidential (all sub-labels)
- **Actions:** Prevent Copilot from processing the labeled content
- **User notifications:** Configure the available notification and validate its presentation in each supported surface. The labeled item can still appear as a citation even though Copilot does not use its content in the response.

For the Recommended tier, extend conditions to include the Confidential — MNPI sub-label for information wall enforcement.

### Step 3: Create the SIT-Based Prompt Blocking Policy (Type 2)

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Confirm the preview rollout has reached the tenant, then configure a separate SIT-based prompt blocking rule. This rule scans text users type directly into Copilot, not the contents of files uploaded with a prompt:
- **Name:** "FSI Copilot DLP — SIT-Based Prompt Blocking"
- **Locations:** Microsoft 365 Copilot and Copilot Chat
- **Conditions:** Content contains sensitive information types (SSN, account numbers, credit card numbers, ABA routing numbers)
- **Actions:** Prevent Copilot from processing content > Processing prompts
- **User notifications:** Configure the available message and validate actual behavior. During preview, Word, Excel, and PowerPoint might block the interaction without clearly identifying organizational policy as the cause.

Test only documented supported surfaces: Microsoft 365 Copilot, Copilot Chat, Word, Excel, and PowerPoint. Do not assume equivalent prompt-blocking behavior in Outlook, Teams, OneNote, or Loop.

### Step 3a: Create the SIT-Based Web Search Restriction Rule (Type 3)

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Configure a separate SIT-based web-search restriction rule for prompts that can use external web grounding:
- **Name:** "FSI Copilot DLP — SIT-Based Web Search Restriction"
- **Locations:** Microsoft 365 Copilot and Copilot Chat
- **Conditions:** Content contains sensitive information types (SSN, account numbers, credit card numbers, ABA routing numbers)
- **Actions:** Prevent Copilot from processing content > Performing Web Searches
- **User notifications:** Validate the message shown in supported clients and confirm DLP match logging.

Verify tenant availability and preview behavior before relying on this control. This rule blocks external web search as a grounding source when prompt text contains configured SITs; it may still allow responses grounded in permitted internal Microsoft 365 data sources.

### Step 4: Review and Configure the Default DLP Policy

**Portal:** Microsoft 365 Admin Center
**Path:** MAC > Copilot > Security (or Purview > DLP > Policies)

Microsoft auto-deploys a default DLP policy for Copilot in simulation mode. This is the SIT-based prompt blocking type:

1. Locate the Microsoft-deployed default policy in the policy list
2. Review the simulation mode match data (no blocking occurs in simulation mode — matches are logged only)
3. Examine false positive rates across your user population
4. After a minimum 2-week review period: if false positive rate is acceptable (<10%), transition from simulation to enforcement
5. Tune SIT confidence levels before enabling enforcement if needed

### Step 5: Configure Sensitive Information Types

**Portal:** Microsoft Purview
**Path:** Purview > Data Classification > Sensitive Info Types

Review and configure sensitive information types used in SIT-based Copilot DLP rules:
- Built-in types: U.S. Social Security Number, Credit Card Number, ABA Routing Number
- Custom types: Internal account number patterns, proprietary financial identifiers, CUSIP, ISIN
- Exact Data Match types: Client lists, employee records

Set confidence levels appropriate for FSI (recommended: high confidence for enforcement policies to reduce false positives; medium confidence acceptable for audit-only/simulation policies).

### Step 6: Configure Edge Browser DLP

**Portal:** Microsoft Purview
**Path:** Purview > Data loss prevention > Endpoint DLP settings

Extend DLP coverage to Copilot interactions accessed through Microsoft Edge browser:

1. Navigate to Endpoint DLP settings
2. Enable Microsoft Edge as a monitored browser
3. Confirm Endpoint DLP and Copilot-location DLP responsibilities are documented separately for browser-based Copilot surfaces
4. Verify Edge browser version meets minimum requirements for Endpoint DLP enforcement

Edge DLP (GA September 2025) catches browser-based Copilot interactions not covered by the native M365 app DLP location.

### Step 6a: Review Platform-Specific DLP Capabilities

**Portal:** Microsoft Purview
**Path:** Purview > Data loss prevention > Endpoint DLP settings

Review expanded platform-specific DLP capabilities that affect Copilot-adjacent data handling:

1. **Mac endpoint DLP:** File type coverage has expanded from approximately 40 to over 100 file types. If your organization has Mac users with Copilot access, verify Endpoint DLP policies include the expanded file types.
2. **Adaptive scoping for SharePoint DLP:** DLP policies can now use adaptive scopes to dynamically target SharePoint sites based on site properties (e.g., sensitivity label, department). Use adaptive scoping to apply DLP policies selectively to SharePoint sites that serve as Copilot grounding sources without requiring manual site enumeration.
3. **AI-powered policy explanations:** Security Copilot can generate natural-language explanations of DLP policy configurations. Use this capability (available in the Purview DLP console) to review complex DLP rule logic and verify all Copilot DLP rule types are configured as intended.

### Step 7: Set Policy Priority and Override Rules

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > [Policy] > Priority

Configure policy priority to handle conflicts between multiple DLP policies. Set override options:
- Allow business justification overrides for medium-sensitivity content
- Block overrides for Highly Confidential content (no user bypass)
- Require manager approval for override requests on regulated data

### Step 8: Enable Policies in Test Mode First

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > [Policy] > Status > Test with policy tips

For any new policy not yet in simulation mode, deploy in test mode first:
- Monitor policy matches without blocking content
- Review false positive rates across departments
- Adjust sensitive information type confidence levels as needed
- After validation period (2-4 weeks), switch to enforcement mode

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Review the default policy in simulation mode; create a Type 1 label-based rule for Highly Confidential content in audit mode; evaluate Type 2 SIT prompt blocking and Type 3 web-search restriction only after confirming tenant availability |
| **Recommended** | Enforce validated Type 1 and available Type 2 rules; enable validated Type 3 rules where external web-search grounding is enabled for sensitive prompt scenarios; enable Edge/Endpoint DLP where required; add MNPI label conditions and custom FSI SITs; document the direct-upload inspection gap |
| **Regulated** | Enforce validated controls with no override for Highly Confidential/MNPI; use custom SITs for FSI identifiers; require Type 3 web-search restriction for sensitive prompt scenarios where web grounding is allowed; maintain complementary endpoint and storage controls for direct uploads; configure real-time alerts and a 4-hour review SLA for high-severity incidents |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for DLP automation
- See [Verification & Testing](verification-testing.md) to validate all Copilot DLP rule types
- Review Control 2.2 for Sensitivity Label integration with Type 1 label-based DLP
- Back to [Control 2.1](../../../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md)
