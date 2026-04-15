# Control 2.1: DLP Policies for M365 Copilot Interactions — Portal Walkthrough

Step-by-step portal configuration for deploying Data Loss Prevention policies that govern M365 Copilot interactions and protect sensitive data. Control 2.1 requires configuring two architecturally distinct DLP policy types — they address different enforcement points and must be configured as separate policies.

## Prerequisites

- Microsoft Purview Purview Compliance Admin role
- Microsoft 365 E5 or E5 Compliance license
- Sensitivity information types defined for FSI data (account numbers, SSNs, financial data)
- Sensitivity label taxonomy deployed (see Control 2.2 — label-based DLP depends on labels)
- DLP policy strategy approved by governance committee

## Policy Type Reference

| Policy Type | What It Protects | Enforcement Point |
|-------------|-----------------|-------------------|
| **Type 1: Label-Based Response Blocking** | Prevents Copilot from surfacing labeled files/emails in responses | Copilot's grounding phase (response side) |
| **Type 2: SIT-Based Prompt Blocking** | Prevents users from submitting sensitive data in prompts | User's prompt (before Copilot processes it) |

These two types must be configured as separate DLP rules — they cannot be combined within a single DLP rule, but may exist as separate rules within the same policy.

## Steps

### Step 1: Navigate to DLP Policy Management

**Portal:** Microsoft Purview
**Path:** Purview > Data Loss Prevention > Policies > Create Policy

Access the DLP policy creation wizard. Two separate policies will be created for the two DLP policy types. Both use the "Microsoft 365 Copilot" location.

**Alternative access for default Copilot DLP policy:**
**Path:** Microsoft 365 Admin Center > Copilot > Security

The MAC Security tab provides quick access to the Microsoft-deployed default Copilot DLP policy (in simulation mode, GA January 2026) and links to Purview DLP for full policy management.

### Step 2: Create the Label-Based Response Blocking Policy (Type 1)

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Configure the label-based response blocking policy:
- **Name:** "FSI Copilot DLP — Label-Based Response Blocking"
- **Locations:** Microsoft 365 Copilot (enable this location; optionally include Exchange, SharePoint, OneDrive for broader coverage)
- **Conditions:** "Content contains sensitivity label" — select Highly Confidential (all sub-labels)
- **Actions:** Block Copilot from processing/returning the labeled content
- **User notifications:** Enable with custom message: "This content is classified as Highly Confidential and cannot be accessed through Copilot"

For the Recommended tier, extend conditions to include the Confidential — MNPI sub-label for information wall enforcement.

### Step 3: Create the SIT-Based Prompt Blocking Policy (Type 2)

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Configure a separate SIT-based prompt blocking policy. This policy scans what users type into Copilot, not what Copilot retrieves:
- **Name:** "FSI Copilot DLP — SIT-Based Prompt Blocking"
- **Locations:** Microsoft 365 Copilot interactions
- **Conditions:** Content contains sensitive information types (SSN, account numbers, credit card numbers, ABA routing numbers)
- **Actions:** Block Copilot from responding to prompts matching conditions; show policy tip to user
- **User notifications:** Enable with custom message explaining why the prompt was blocked

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

Review and configure sensitive information types used in both DLP policy types:
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
3. Confirm the DLP policy includes browser-based Copilot surfaces
4. Verify Edge browser version meets minimum requirements for Endpoint DLP enforcement

Edge DLP (GA September 2025) catches browser-based Copilot interactions not covered by the native M365 app DLP location.

### Step 6a: Review Platform-Specific DLP Capabilities

**Portal:** Microsoft Purview
**Path:** Purview > Data loss prevention > Endpoint DLP settings

Review expanded platform-specific DLP capabilities that affect Copilot-adjacent data handling:

1. **Mac endpoint DLP:** File type coverage has expanded from approximately 40 to over 100 file types. If your organization has Mac users with Copilot access, verify Endpoint DLP policies include the expanded file types.
2. **Adaptive scoping for SharePoint DLP:** DLP policies can now use adaptive scopes to dynamically target SharePoint sites based on site properties (e.g., sensitivity label, department). Use adaptive scoping to apply DLP policies selectively to SharePoint sites that serve as Copilot grounding sources without requiring manual site enumeration.
3. **AI-powered policy explanations:** Security Copilot can generate natural-language explanations of DLP policy configurations. Use this capability (available in the Purview DLP console) to review complex DLP rule logic and verify both policy types are configured as intended.

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
| **Baseline** | Enable the default DLP policy (simulation mode review); create Type 1 label-based policy for Highly Confidential content (audit mode); create Type 2 SIT-based policy for SSN and account numbers (audit mode) |
| **Recommended** | Both policy types in enforcement; Edge DLP enabled; MNPI label conditions added to Type 1; custom FSI SITs (ABA routing, CUSIP) in Type 2; default policy transitioned from simulation to enforcement |
| **Regulated** | Both types enforced with no override allowed for Highly Confidential/MNPI; custom SITs for all FSI-specific identifiers (CUSIP, ISIN, SWIFT, CRD); Edge DLP with Endpoint DLP for complete coverage; adaptive scoping for SharePoint DLP targeting Copilot grounding sources; Mac endpoint DLP verified for expanded file types; real-time alerting for policy matches; 4-hour review SLA for high-severity incidents |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for DLP automation
- See [Verification & Testing](verification-testing.md) to validate both DLP policy types
- Review Control 2.2 for Sensitivity Label integration with Type 1 label-based DLP
- Back to [Control 2.1](../../../controls/pillar-2-security/2.1-dlp-policies-for-copilot.md)
