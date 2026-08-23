# Control 2.1: DLP Policies for M365 Copilot Interactions — Portal Walkthrough

Step-by-step portal configuration for deploying Data Loss Prevention policies that govern Microsoft 365 Copilot and Copilot Chat interactions. Supported condition/action pairs use separate rules; sensitivity-label and sensitive-information-type conditions can't be combined within one rule.

## Prerequisites

- Purview Compliance Admin role
- Appropriate Microsoft 365 and Microsoft Purview licensing. Prompt safeguards are available to Copilot and Copilot Chat users, subject to rollout; file/email exclusion requires an eligible Purview Information Protection and Governance entitlement.
- Sensitive information types defined for FSI data (account numbers, SSNs, financial data)
- Sensitivity label taxonomy deployed (see Control 2.2 — label-based DLP depends on labels)
- DLP policy strategy approved by governance committee

## Policy Type Reference

| Policy Type | What It Protects | Enforcement Point |
|-------------|-----------------|-------------------|
| **Type 1: Label-Based Source Exclusion** | Prevents Copilot from processing the content of labeled files/emails; citations may remain | Source processing during grounding |
| **Type 2: SIT-Based Prompt Blocking** | Prevents users from submitting sensitive data in prompts | User's prompt (before Copilot processes it) |
| **Type 3: SIT-Based Web-Search Restriction** | Prevents external web search for matching prompts while allowing permitted internal grounding | User's prompt (web-search path) |
| **Type 4: External-Email Exclusion** | Excludes email from senders outside accepted domains without inspecting the body | Email sender-domain metadata |

Prompt blocking is in preview and rolling out. External-email exclusion is also in preview. Web-search restriction is generally available. Confirm tenant availability before treating a preview rule as enforced.

## Steps

### Step 1: Navigate to DLP Policy Management

**Portal:** Microsoft Purview
**Path:** Purview > Data Loss Prevention > Policies > Create Policy

Access the DLP policy creation wizard. Create a **Custom** policy for the **Microsoft 365 Copilot and Copilot Chat** location. Supported condition/action pairs require separate rules; they can be in one policy.

**Alternative access for default Copilot DLP policy:**
**Path:** Microsoft 365 Admin Center > Copilot > Security

The MAC Security tab provides quick access to the Microsoft-deployed default Copilot DLP policy (in simulation mode, GA January 2026) and links to Purview DLP for full policy management.

### Step 2: Create the Label-Based Source-Exclusion Rule (Type 1)

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Configure the label-based source-exclusion rule:
- **Name:** "FSI Copilot DLP — Label-Based Source Exclusion"
- **Locations:** Microsoft 365 Copilot and Copilot Chat. Confirm all other locations are disabled; the Copilot location can't be combined with other policy locations.
- **Conditions:** "Content contains sensitivity label" — select Highly Confidential (all sub-labels)
- **Actions:** Prevent Copilot from processing content. The item can remain visible as a citation.
- **User notifications:** Enable with custom message: "This content is classified as Highly Confidential and cannot be accessed through Copilot"

For the Recommended tier, extend conditions to include the Confidential — MNPI sub-label for information wall enforcement.

This action covers supported stored/open files and emails sent on or after January 1, 2025; calendar invites aren't supported. Microsoft explicitly lists Microsoft 365 Copilot, Copilot Chat, and Copilot in Word, Excel, and PowerPoint for the label and prompt features.

### Step 3: Create the SIT-Based Prompt Blocking Rule (Type 2)

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Configure a separate SIT-based prompt rule in the same Custom policy or another Copilot-only Custom policy. This rule evaluates what users type into Copilot, not what Copilot retrieves:
- **Name:** "FSI Copilot DLP — SIT-Based Prompt Blocking"
- **Locations:** Microsoft 365 Copilot and Copilot Chat
- **Conditions:** Content contains sensitive information types (SSN, account numbers, credit card numbers, ABA routing numbers)
- **Actions:** Prevent Copilot from processing content > Processing prompts; show policy tip to user
- **User notifications:** Enable with custom message explaining why the prompt was blocked

This action is in preview and rolling out. Verify that it has reached the tenant before treating it as enforced.

### Step 3a: Create the SIT-Based Web-Search Restriction Rule (Type 3)

Add another SIT-based rule:

- **Locations:** Microsoft 365 Copilot and Copilot Chat
- **Conditions:** Content contains the approved sensitive information types
- **Actions:** Prevent Copilot from processing content > Performing Web Searches
- **Expected result:** Matching prompts don't use external web search but can still use permitted internal Microsoft 365 sources

!!! warning "Direct-upload limitation"
    Copilot DLP doesn't scan the contents of files uploaded directly into prompts. It evaluates the text typed into the prompt. Validate source access controls and sensitivity labels as compensating controls.

### Step 3b: Assess the External-Email Exclusion Rule (Type 4)

If the preview is available, add a separate rule:

- **Conditions:** Email is received from > External users
- **Actions:** Prevent Copilot from processing content
- **Expected result:** Email from a domain outside the tenant's accepted domains is excluded from grounding, summarization, and citation
- **Limitation:** The rule compares sender-domain metadata and doesn't inspect the email body

### Step 4: Review and Configure the Default DLP Policy

**Portal:** Microsoft 365 Admin Center
**Path:** MAC > Copilot > Security (or Purview > DLP > Policies)

Microsoft auto-deploys a default DLP policy for Copilot in simulation mode. This is the SIT-based prompt blocking type:

1. Locate the Microsoft-deployed default policy in the policy list
2. Review the simulation mode match data (no blocking occurs in simulation mode — matches are logged only)
3. Examine false positive rates across your user population
4. After the institution-approved observation period, transition to enforcement only if test results meet the approved acceptance criteria
5. Tune SIT confidence levels before enabling enforcement if needed

### Step 5: Configure Sensitive Information Types

**Portal:** Microsoft Purview
**Path:** Solutions > Information Protection > Classifiers > Sensitive info types

Review and configure sensitive information types used in the prompt and web-search rules:
- Built-in types: U.S. Social Security Number, Credit Card Number, ABA Routing Number
- Custom types: Internal account number patterns, proprietary financial identifiers, CUSIP, ISIN
- Exact Data Match types: Client lists, employee records

Set confidence levels appropriate for FSI (recommended: high confidence for enforcement policies to reduce false positives; medium confidence acceptable for audit-only/simulation policies).

### Step 6: Configure Edge Browser DLP

**Portal:** Microsoft Purview
**Path:** Purview > Data loss prevention > Endpoint DLP settings

Evaluate a separately documented Endpoint/browser DLP path for an approved browser activity:

1. Navigate to Endpoint DLP settings
2. Enable Microsoft Edge as a monitored browser
3. Configure the applicable browser/Endpoint DLP controls independently; don't infer coverage from the Copilot policy location
4. Verify Edge browser version meets minimum requirements for Endpoint DLP enforcement

Endpoint/browser DLP is a separate enforcement path from the Copilot policy location. Verify its current supported browsers, activities, and licensing before relying on it for a Copilot upload path.

### Step 6a: Review Platform-Specific DLP Capabilities

**Portal:** Microsoft Purview
**Path:** Purview > Data loss prevention > Endpoint DLP settings

Review expanded platform-specific DLP capabilities that affect Copilot-adjacent data handling:

1. **Mac endpoint DLP:** File type coverage has expanded from approximately 40 to over 100 file types. If your organization has Mac users with Copilot access, verify Endpoint DLP policies include the expanded file types.
2. **Adaptive scoping for SharePoint DLP:** DLP policies can now use adaptive scopes to dynamically target SharePoint sites based on site properties (e.g., sensitivity label, department). Use adaptive scoping to apply DLP policies selectively to SharePoint sites that serve as Copilot grounding sources without requiring manual site enumeration.
3. **AI-powered policy explanations:** If licensed and available in the tenant, use Security Copilot explanations to review complex DLP rule logic; validate the actual policy configuration rather than relying on generated text.

### Step 7: Set Policy Priority and Notifications

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > [Policy] > Priority

Configure policy priority to handle conflicts between multiple policies. Configure only the notifications, alerts, and actions supported by the selected Copilot rule. Don't assume workload-specific override or manager-approval behavior unless the portal exposes and testing confirms it.

### Step 8: Enable Policies in Test Mode First

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > [Policy] > Edit policy > Policy mode

For any new policy not yet in simulation mode, deploy in test mode first:
- Monitor policy matches without blocking content
- Review false positive rates across departments
- Adjust sensitive information type confidence levels as needed
- After the institution-approved validation period and acceptance review, switch to enforcement mode

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Review the default simulation policy; create a Custom Copilot-location policy with label-exclusion and web-search rules in simulation mode |
| **Recommended** | Enforce validated label-exclusion and web-search rules; add prompt blocking only after confirming preview availability; assess preview external-email exclusion; document the direct-upload limitation; evaluate Endpoint/browser DLP separately |
| **Regulated** | Enforce all applicable, tenant-available rules with institution-approved FSI SITs; assess external-email exclusion; retain source permissions/labels for upload gaps; configure supported alerts and review evidence on the approved schedule |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for DLP automation
- See [Verification & Testing](verification-testing.md) to validate the supported DLP actions
- Review Control 2.2 for Sensitivity Label integration with Type 1 label-based DLP
- Back to [Control 2.1](../../../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md)
