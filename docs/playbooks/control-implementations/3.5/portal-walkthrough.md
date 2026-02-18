# Control 3.5: FINRA Rule 2210 Compliance for Copilot-Drafted Communications — Portal Walkthrough

Step-by-step portal configuration for implementing controls that help Copilot-drafted communications comply with FINRA Rule 2210 (Communications with the Public) requirements for fair, balanced, and non-misleading content.

## Prerequisites

- **Role:** Compliance Administrator or Communication Compliance Admin
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal

## Steps

### Step 1: Create FINRA 2210 Communication Compliance Policy

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Communication compliance > Policies > Create policy

1. Click **Create policy** and select **Custom policy**.
2. Name the policy "FSI-FINRA-2210-Copilot-Review".
3. Under **Supervised users**, select registered representatives and associated persons with Copilot licenses.
4. Under **Supervised locations**, enable Exchange email, Microsoft Teams, and Copilot interactions.
5. Set **Direction** to **Outbound** (client-facing communications).

### Step 2: Configure FINRA 2210-Specific Detection Rules

**Portal:** Microsoft Purview Compliance Portal
**Path:** Policy wizard > Conditions

1. Add keyword conditions for prohibited language patterns:
   - Guaranteed returns, risk-free investments, assured performance
   - Promissory language: "will achieve", "certain to", "no possibility of loss"
   - Misleading comparisons or omissions of material facts
2. Add keyword conditions for AI washing — unsubstantiated AI capability claims that may violate FINRA Rule 2210(d)(1)(A) and the Investment Advisers Act Section 206 antifraud provisions (per SEC v. Delphia Inc. and Global Predictions Inc., March 2024):
   - "our AI guarantees", "AI-powered returns", "AI eliminates risk"
   - "our algorithms always", "AI ensures superior", "proven AI superiority"
3. Add sensitive information types for financial data (account numbers, trade confirmations).
4. Enable the **Financial regulatory collusion** trainable classifier.
5. Add custom keyword dictionaries for firm-specific prohibited terms.

### Step 3: Configure Pre-Send Review Workflow

**Portal:** Microsoft Purview Compliance Portal
**Path:** Policy wizard > Review settings

1. Set the review percentage to **100%** for outbound client communications.
2. Assign primary reviewers from the compliance supervision team.
3. Configure the review SLA to 24 hours for standard communications and 4 hours for time-sensitive items.
4. Enable the **Supervisory review** workflow requiring approval before release for high-risk matches.

### Step 4: Set Up FINRA Correspondence Categories

**Portal:** Microsoft Purview Compliance Portal
**Path:** Policy wizard > Categories

1. Create classification tags aligned with FINRA 2210 categories:
   - **Retail Communication** — any communication distributed to more than 25 retail investors
   - **Correspondence** — communication to 25 or fewer retail investors
   - **Institutional Communication** — communication exclusively to institutional investors
2. Assign default review requirements per category (retail requires pre-use approval).

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Outbound review percentage | 10% | 50% | 100% |
| Pre-send review for retail | Optional | Recommended | Required |
| Prohibited language detection | Basic keywords | Custom dictionaries | Custom + classifiers |
| AI washing detection | Awareness only | Keyword detection | Keyword + classifier |
| Review SLA | 72 hours | 24 hours | 4 hours |

## Regulatory Alignment

- **FINRA Rule 2210** — Supports compliance with fair and balanced communication requirements
- **FINRA Rule 2210(b)** — Helps meet content standards for accuracy and balance
- **FINRA Rule 2210(c)** — Supports filing requirements for retail communications
- **FINRA Rule 2210(d)(1)(A)** — Supports detection of misleading statements about AI capabilities in client-facing communications
- **Investment Advisers Act Section 206** — Antifraud provisions apply to AI capability claims in communications (see SEC v. Delphia enforcement precedent)

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automation of FINRA 2210 monitoring
- See [Verification & Testing](verification-testing.md) to validate detection accuracy
