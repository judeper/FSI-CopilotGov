# Control 3.2: Data Retention Policies for Copilot Interactions — Portal Walkthrough

Step-by-step portal configuration for establishing data retention policies that govern the lifecycle of Copilot-generated content and interaction history in financial services environments.

## Prerequisites

- **Role:** Purview Compliance Admin or Records Management Administrator
- **License:** Microsoft 365 E5 or E5 Compliance add-on
- **Access:** Microsoft Purview portal

## Steps

### Step 1: Navigate to Data Lifecycle Management

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Data lifecycle management > Microsoft 365

1. Open the Data lifecycle management solution.
2. Select the **Retention policies** tab to view existing policies.
3. Identify any existing policies that may already cover Copilot content locations.

### Step 2: Create Retention Policy for Microsoft Copilot Experiences

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Data lifecycle management > Retention policies > New retention policy

The **Microsoft Copilot experiences** location is the primary retention target for M365 Copilot deployments. It covers Microsoft 365 Copilot Chat history, Copilot interactions in Word/Excel/PowerPoint/Outlook/Teams, and Copilot Pages.

1. Click **New retention policy** and name it `FSI-Copilot-Experiences-Retention`.
2. Add a description: "Retains Microsoft Copilot experiences content per FSI regulatory requirements — covers Copilot Chat history, meeting recaps, and in-app Copilot interactions."
3. Under **Choose the type of retention policy**, select **Static**.
4. Select the locations to include:
   - **Microsoft Copilot experiences** — toggle to On
5. Set retention period to **3 years** for communications baseline (SEC/FINRA minimum).
6. For regulated deployments, create a separate 6-year policy for this location.
7. Choose **Retain items for the specified period** with **Do nothing** at the end (retain only).
8. Click **Submit**.

**Note on related location categories:** You will also see **Enterprise AI Apps** and **Other AI Apps** in the location selector. Current Microsoft Learn documentation lists Copilot Studio under **Microsoft Copilot experiences**. **Enterprise AI Apps** covers Entra-registered AI apps, ChatGPT Enterprise, and Microsoft Foundry; **Other AI Apps** covers third-party AI tools detected through browser or network activity. For M365 Copilot and Copilot Studio deployments covered by this framework, configure retention policies targeting the **Microsoft Copilot experiences** location. Assess the other AI app categories separately for broader AI governance programs.

### Step 3: Create Retention Policy for Copilot-Generated Documents

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Data lifecycle management > Retention policies > New retention policy

1. Create a policy named `FSI-Copilot-Generated-Content-Retention`.
2. Select locations: **SharePoint sites**, **OneDrive accounts**, **Exchange email**.
3. Set retention to **6 years** for financial records coverage per SEC Rule 17a-4(a).
4. This policy covers documents, emails, and presentations created or modified with Copilot assistance.

### Step 4: Verify Microsoft Copilot Experiences Policy Distribution

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Data lifecycle management > Retention policies > [select policy] > Policy status

After creating the Microsoft Copilot experiences retention policy:

1. Select the policy from the Retention policies list.
2. Under **Status**, verify the **Distribution status** shows **Success** (may take up to 24 hours after creation).
3. If status shows **Pending** after 24 hours, review the error details and re-submit if needed.
4. Verify the policy scope includes all users or the targeted user groups.

### Step 5: Configure Retention Labels for Copilot Content

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Records management > File plan > Create a label

1. Create a retention label named `FSI-Copilot-Regulatory-Record-6yr`.
2. Set the retention period to 6 years from creation date.
3. Mark as a regulatory record if required by your compliance framework.
4. Publish the label to relevant SharePoint sites, OneDrive locations, and the Microsoft Copilot experiences location.

### Step 6: Evaluate Priority Cleanup for Documented Storage Remediation (Recommended Tier)

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Data lifecycle management > Priority cleanup

Priority cleanup is a separate Data Lifecycle Management feature that can override existing retention settings or eDiscovery holds for selected SharePoint and OneDrive content after simulation and approval. Microsoft documents Copilot-related use cases such as stale Teams meeting recordings/transcripts and departed-user Preservation Hold Library cleanup. It is not documented as a detector for unsent Copilot drafts or generic Copilot-generated content signatures. Baseline-tier deployments should use standard retention.

1. Confirm the operator has the **Priority Cleanup Admin** role.
2. Define the narrow business scenario, such as stale Teams meeting recordings/transcripts or departed-user Preservation Hold Library cleanup.
3. Run the required simulation and review the item sample, affected holds, and any eDiscovery-hold dependencies.
4. Confirm that no items marked as records or regulatory records are in scope; Priority cleanup cannot target them.
5. Route the request through the required approval workflow, including eDiscovery Administrator approval when an eDiscovery hold applies.
6. Document the scope decision, simulation results, approvals, and regulatory rationale in the firm's records management schedule.

**Important:** Do not apply Priority cleanup to documents that have been shared, sent, saved to shared drives, declared as records, or otherwise treated as business records unless compliance/legal has approved the exception. If the firm needs shorter retention for unsent Copilot drafts, implement and document a standard retention/deletion policy rather than labeling it as a Microsoft-documented Priority cleanup scenario.

### Step 7: Verify Threaded Summary Retention Coverage

**Portal:** Microsoft Purview portal
**Path:** purview.microsoft.com > Data lifecycle management > Retention policies

Threaded Copilot summaries (meeting recaps, conversation summaries) are retained independently from their source content. Verify complete coverage:

1. Confirm the **Microsoft Copilot experiences** retention policy is active — this location covers Copilot-generated meeting recaps and summaries.
2. Confirm the **Teams** retention policy is active — this location covers native Teams channel and chat messages. Copilot prompts, responses, recaps, and threaded summaries require the Microsoft Copilot experiences policy.
3. Run a test: delete a Teams meeting transcript and verify that the Copilot-generated meeting recap is still present and covered by the Microsoft Copilot experiences retention policy.
4. Document the verification outcome in the firm's retention coverage log.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Microsoft Copilot experiences retention | Required | Required | Required (6 years) |
| Exchange retention (email + legacy Copilot Chat) | Required | Required | Required |
| SharePoint/OneDrive retention | Required | Required | Required |
| Teams retention | Required | Required | Required |
| Priority cleanup for AI drafts | Not recommended | Optional (scoped) | Optional (conservative) |
| Regulatory record label | No | Recommended | Required |
| Threaded summary coverage verification | Optional | Recommended | Required |

## Regulatory Alignment

- **SEC Rule 17a-4(a)** — Six-year retention for broker-dealer records; Microsoft Copilot experiences location must be included
- **SEC Rule 17a-3(a)(17)** — All communications relating to the member's business; conservative interpretation supports retaining all Copilot-generated content
- **FINRA Rule 4511** — Books-and-records retention obligations; Copilot Chat history and meeting recaps are covered records
- **FINRA Rule 4511(c)** — Preservation format requirements; threaded summaries must be retained in accessible, regulation-compliant format
- **SOX Section 802** — Criminal penalties for record destruction; retention policies must prevent inadvertent deletion of Copilot-generated financial content

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for automated retention policy deployment
- See [Verification & Testing](verification-testing.md) to validate retention policies are applied correctly
- Back to [Control 3.2](../../../controls/pillar-3-compliance/3.2-data-retention-policies.md)
