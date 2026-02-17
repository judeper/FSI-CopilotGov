# Control 3.2: Data Retention Policies for Copilot Interactions — Portal Walkthrough

Step-by-step portal configuration for establishing data retention policies that govern the lifecycle of Copilot-generated content and interaction history in financial services environments.

## Prerequisites

- **Role:** Compliance Administrator or Records Management Administrator
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal

## Steps

### Step 1: Navigate to Data Lifecycle Management

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Data lifecycle management > Microsoft 365

1. Open the Data lifecycle management solution.
2. Select the **Retention policies** tab to view existing policies.
3. Identify any existing policies that may already cover Copilot content locations.

### Step 2: Create Copilot Interaction Retention Policy

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Data lifecycle management > Retention policies > New retention policy

1. Click **New retention policy** and name it "FSI-Copilot-Interaction-Retention".
2. Add a description: "Retains Copilot interaction data per FSI regulatory requirements."
3. Under **Choose the type of retention policy**, select **Static**.
4. Select the locations to include:
   - **Copilot for Microsoft 365 interactions** — toggle to On (covers all Copilot-generated prompts and responses)
5. Set retention period to **7 years** (aligns with SEC/FINRA record retention requirements).
6. Choose **Retain items for the specified period** and **Delete items automatically after the retention period**.

### Step 3: Create Retention Policy for Copilot-Generated Documents

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Data lifecycle management > Retention policies > New retention policy

1. Create a second policy named "FSI-Copilot-Generated-Content-Retention".
2. Select locations: **SharePoint sites**, **OneDrive accounts**, **Exchange email**.
3. Set retention to **7 years** with automatic deletion after expiry.
4. This policy covers documents, emails, and presentations created or modified with Copilot assistance.

### Step 4: Configure Retention Labels for Copilot Content

**Portal:** Microsoft Purview Compliance Portal
**Path:** Solutions > Records management > File plan > Create a label

1. Create a retention label named "Copilot-Generated — 7yr Retain".
2. Set the retention period to 7 years from creation date.
3. Mark as a regulatory record if required by your compliance framework.
4. Publish the label to relevant SharePoint sites and OneDrive locations.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Copilot interaction retention | 1 year | 3 years | 7 years |
| Copilot-generated content retention | 1 year | 3 years | 7 years |
| Regulatory record label | No | Recommended | Required |
| Auto-apply retention labels | Optional | Recommended | Required |

## Regulatory Alignment

- **SEC Rule 17a-4** — Supports compliance with electronic communication retention (3-6 year minimum)
- **FINRA Rule 4511** — Helps meet books-and-records retention obligations
- **SOX Section 802** — Supports audit record preservation requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated retention policy deployment
- See [Verification & Testing](verification-testing.md) to validate retention policies are applied correctly
