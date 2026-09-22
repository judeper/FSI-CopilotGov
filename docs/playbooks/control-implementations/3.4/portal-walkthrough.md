# Control 3.4: Communication Compliance Monitoring — Portal Walkthrough

Step-by-step portal configuration for implementing communication compliance policies that monitor Copilot-assisted communications for regulatory violations, inappropriate content, and policy breaches in financial services. This walkthrough includes enabling Insider Risk Management (IRM) integration so CC policy violations contribute to user risk scores.

## Prerequisites

- **Role:** Purview Compliance Admin or Communication Compliance Admin
- **License:** Eligible Communication Compliance licensing, such as Microsoft Purview Suite (formerly Microsoft 365 E5 Compliance), Office 365 E5, or Office 365 E3 with the Advanced Compliance add-on
- **Access:** Microsoft Purview portal at [purview.microsoft.com](https://purview.microsoft.com)

## Steps

### Step 1: Enable Communication Compliance

**Portal:** Microsoft Purview portal
**Path:** Microsoft Purview > Communication compliance

1. Navigate to the Communication compliance solution.
2. If first-time setup, follow the onboarding wizard to configure permissions and enable the solution.
3. Assign the **Communication Compliance Analyst** and **Communication Compliance Investigator** roles to appropriate team members.

### Step 2: Create Policy for Copilot-Assisted Communications

**Portal:** Microsoft Purview portal
**Path:** Microsoft Purview > Communication compliance > Policies > Create policy

1. Click **Create policy** and select **Detect Microsoft Copilot interactions** for a baseline Copilot policy, or select **Custom policy** if the firm needs custom conditions from the start.
2. Name the policy "FSI-Copilot-Communication-Monitoring".
3. Under **Supervised users**, select the groups of users with Copilot licenses.
4. Under **Locations**, enable:
   - Exchange email
   - Microsoft Teams (chat and channel messages)
   - Microsoft Copilot experiences
   - Enterprise AI apps or Other AI apps only if those categories are in scope and billing prerequisites are approved
5. Under **Direction**, select **Inbound, Outbound, and Internal**.

### Step 3: Configure Detection Conditions

**Portal:** Microsoft Purview portal
**Path:** Policy wizard > Conditions

1. Under **Content contains**, add conditions for FSI-specific scenarios:
   - **Regulatory compliance** — detect potential FINRA/SEC violations in Copilot-drafted content
   - **Financial sensitive information** — detect account numbers, SSNs, or trade details
   - **Inappropriate promises** — detect promissory language, assured returns, or misleading language
2. Add trainable classifiers: **Regulatory collusion**, **Stock manipulation**, **Unauthorized disclosure**.
3. Set the **Review percentage** to 100% for regulated communications.

### Step 4: Configure Reviewers and Workflow

**Portal:** Microsoft Purview portal
**Path:** Policy wizard > Reviewers

1. Assign primary reviewers from the compliance supervision team.
2. Configure escalation reviewers for items requiring senior review.
3. Set the review SLA to 48 hours for standard items and 4 hours for high-severity matches.
4. Enable email notifications for new items pending review.

### Step 5: Configure Communication Compliance Indicators in IRM

**Portal:** Microsoft Purview portal
**Path:** Microsoft Purview > Insider Risk Management > Settings > Policy indicators

This step connects Communication Compliance violations to Insider Risk Management, creating a cross-pillar governance loop where CC policy matches contribute to user risk scores in IRM (Control 2.10).

1. Navigate to **Insider Risk Management** > **Settings** > **Policy indicators**.
2. Enable the Communication Compliance indicators that should contribute to IRM policies.
3. Select the relevant Communication Compliance policies if using custom CC policy alerts as IRM indicators.
4. Select which violation types should generate IRM risk indicators:
   - **Regulatory compliance violations** (required for Recommended tier)
   - **MNPI-related violations** (required for Recommended tier)
   - **All violation types** (required for Regulated tier)
5. Click **Save**.
6. Navigate to the IRM dashboard to confirm CC indicators are flowing after policy matches occur. Expect propagation delay after the first CC policy match before IRM indicators appear.

> **Cross-pillar dependency:** IRM integration requires Insider Risk Management to be configured (Control 2.10). Ensure IRM is enabled and at least one IRM policy is active before enabling CC-to-IRM indicator flow.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Copilot communication monitoring | Optional | Enabled | Required |
| Review percentage | 10% | 25% | 100% |
| Trainable classifiers | Basic | Financial-specific | All financial classifiers |
| Review SLA | 7 days | 48 hours | 24 hours |
| IRM integration | Not required | High-risk policies | All policies |

## Regulatory Alignment

- **FINRA Rule 3110(a)** — Supports compliance with the "reasonably designed" supervisory system requirement; IRM integration creates automated escalation strengthening the supervisory system
- **SEC Reg BI** — Helps meet best-interest documentation and communication standards
- **FINRA Rule 2210** — Supports review of AI-assisted client communications

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for policy automation
- See [Verification & Testing](verification-testing.md) to validate monitoring coverage
- Back to [Control 3.4](../../../controls/pillar-3-compliance/3.4-communication-compliance.md)
