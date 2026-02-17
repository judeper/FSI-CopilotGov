# Control 2.1: DLP Policies for M365 Copilot Interactions — Portal Walkthrough

Step-by-step portal configuration for deploying Data Loss Prevention policies that govern M365 Copilot interactions and protect sensitive data.

## Prerequisites

- Microsoft Purview Compliance Administrator role
- Microsoft 365 E5 or E5 Compliance license
- Sensitivity information types defined for FSI data (account numbers, SSNs, financial data)
- DLP policy strategy approved by governance committee

## Steps

### Step 1: Navigate to DLP Policy Management

**Portal:** Microsoft Purview
**Path:** Purview > Data Loss Prevention > Policies > Create Policy

Access the DLP policy creation wizard. For Copilot-specific policies, select the "Microsoft 365 Copilot (preview)" location when configuring policy scope. This location covers Copilot interactions across Word, Excel, PowerPoint, Teams, and Outlook.

### Step 2: Create Copilot-Specific DLP Policy

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > Create > Custom Policy

Configure a DLP policy targeting Copilot interactions:
- **Name:** "FSI Copilot DLP — Sensitive Financial Data Protection"
- **Locations:** Microsoft 365 Copilot interactions
- **Conditions:** Content contains sensitive information types (SSN, account numbers, credit card numbers, financial data patterns)
- **Actions:** Block Copilot from processing content matching conditions; show policy tip to user
- **User notifications:** Enable with custom message explaining why content was restricted

### Step 3: Configure Sensitive Information Types

**Portal:** Microsoft Purview
**Path:** Purview > Data Classification > Sensitive Info Types

Review and configure sensitive information types used in DLP conditions:
- Built-in types: U.S. Social Security Number, Credit Card Number, ABA Routing Number
- Custom types: Internal account number patterns, proprietary financial identifiers
- Exact Data Match types: Client lists, employee records

Set confidence levels appropriate for FSI (recommended: high confidence to reduce false positives).

### Step 4: Set Policy Priority and Override Rules

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > [Policy] > Priority

Configure policy priority to handle conflicts between multiple DLP policies. Set override options:
- Allow business justification overrides for medium-sensitivity content
- Block overrides for highly confidential content (no user bypass)
- Require manager approval for override requests on regulated data

### Step 5: Enable Policy in Test Mode

**Portal:** Microsoft Purview
**Path:** Purview > DLP > Policies > [Policy] > Status > Test with policy tips

Deploy the policy in test mode first to evaluate effectiveness:
- Monitor policy matches without blocking content
- Review false positive rates across departments
- Adjust sensitive information type confidence levels as needed
- After validation period (2-4 weeks), switch to enforcement mode

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | DLP policy blocking Copilot from processing SSN, account numbers, and credit card data |
| **Recommended** | Multiple DLP policies by data type with tuned confidence levels; user notification with governance guidance |
| **Regulated** | Comprehensive DLP coverage for all FSI sensitive info types; no-override policies for regulated data; real-time alerting for policy matches |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for DLP automation
- See [Verification & Testing](verification-testing.md) to validate DLP effectiveness
- Review Control 2.2 for Sensitivity Label integration with DLP
