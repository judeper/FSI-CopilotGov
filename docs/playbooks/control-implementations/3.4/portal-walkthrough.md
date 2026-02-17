# Control 3.4: Communication Compliance Monitoring — Portal Walkthrough

Step-by-step portal configuration for implementing communication compliance policies that monitor Copilot-assisted communications for regulatory violations, inappropriate content, and policy breaches in financial services.

## Prerequisites

- **Role:** Compliance Administrator or Communication Compliance Admin
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview compliance portal

## Steps

### Step 1: Enable Communication Compliance

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Communication compliance

1. Navigate to the Communication compliance solution.
2. If first-time setup, follow the onboarding wizard to configure permissions and enable the solution.
3. Assign the **Communication Compliance Analyst** and **Communication Compliance Investigator** roles to appropriate team members.

### Step 2: Create Policy for Copilot-Assisted Communications

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Communication compliance > Policies > Create policy

1. Click **Create policy** and select **Custom policy**.
2. Name the policy "FSI-Copilot-Communication-Monitoring".
3. Under **Supervised users**, select the groups of users with Copilot licenses.
4. Under **Supervised locations**, enable:
   - Exchange email
   - Microsoft Teams (chat and channel messages)
   - Copilot interactions
5. Under **Direction**, select **Inbound, Outbound, and Internal**.

### Step 3: Configure Detection Conditions

**Portal:** Microsoft Purview Compliance Portal
**Path:** Policy wizard > Conditions

1. Under **Content contains**, add conditions for FSI-specific scenarios:
   - **Regulatory compliance** — detect potential FINRA/SEC violations in Copilot-drafted content
   - **Financial sensitive information** — detect account numbers, SSNs, or trade details
   - **Inappropriate promises** — detect promissory language, assured returns, or misleading language
2. Add trainable classifiers: **Regulatory collusion**, **Stock manipulation**, **Unauthorized disclosure**.
3. Set the **Review percentage** to 100% for regulated communications.

### Step 4: Configure Reviewers and Workflow

**Portal:** Microsoft Purview Compliance Portal
**Path:** Policy wizard > Reviewers

1. Assign primary reviewers from the compliance supervision team.
2. Configure escalation reviewers for items requiring senior review.
3. Set the review SLA to 48 hours for standard items and 4 hours for high-severity matches.
4. Enable email notifications for new items pending review.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Copilot communication monitoring | Optional | Enabled | Required |
| Review percentage | 10% | 25% | 100% |
| Trainable classifiers | Basic | Financial-specific | All financial classifiers |
| Review SLA | 7 days | 48 hours | 24 hours |

## Regulatory Alignment

- **FINRA Rule 3110** — Supports compliance with supervisory review requirements for communications
- **SEC Reg BI** — Helps meet best-interest documentation and communication standards
- **FINRA Rule 2210** — Supports review of AI-assisted client communications

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for policy automation
- See [Verification & Testing](verification-testing.md) to validate monitoring coverage
