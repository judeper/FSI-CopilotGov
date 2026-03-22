# Control 2.11: Copilot Pages Security and Sharing Controls — Portal Walkthrough

Step-by-step portal configuration for governing Copilot Pages and Copilot Notebooks using Cloud Policy, SharePoint Embedded administration, and Microsoft Purview.

## Prerequisites

- Office Apps admin role, SharePoint Admin role, or M365 Global Admin for the required portals
- Microsoft 365 Copilot deployment planned or active
- Governance decision on which users can create Copilot Pages and Copilot Notebooks
- Records management and eDiscovery contacts identified

## Steps

### Step 1: Configure Copilot Pages Creation Policy

**Portal:** Microsoft 365 Cloud Policy service  
**Path:** `https://config.office.com` > **Customization** > **Policy Management**

1. Create a new policy or open the existing Copilot collaboration policy.
2. Scope the policy to the approved users or groups.
3. Set **Create and view Copilot Pages and Copilot Notebooks** to the approved state.
4. Record the target group, owner, and approval reference.

### Step 2: Review Code Preview Policy

**Portal:** Microsoft 365 Cloud Policy service  
**Path:** `https://config.office.com` > **Customization** > **Policy Management**

1. Review **Enable code previews for AI-generated content in Microsoft 365 Copilot Chat and Copilot Pages**.
2. Disable it unless the business case is documented and approved.
3. If enabled, document which teams are allowed to use the feature.

### Step 3: Review SharePoint Embedded Storage

**Portal:** SharePoint Admin Center / SharePoint PowerShell

1. Review the user-owned SharePoint Embedded containers used for Copilot Pages, Copilot Notebooks, and Loop My workspace.
2. Confirm administrators understand the user departure lifecycle and cleanup timing.
3. Document how ownerless or preservation-sensitive containers are escalated.

### Step 4: Validate Sharing and Collaboration Posture

**Portal:** Microsoft 365 Copilot app, Loop app, SharePoint Admin Center

1. Create a test Page with an approved pilot account.
2. Confirm the default sharing behavior aligns with the firm's approved model.
3. Test whether Loop component sharing is enabled in the broader Microsoft 365 ecosystem and document the effect on Pages sharing.
4. Validate that external or cross-tenant scenarios are blocked unless expressly approved and tested.

### Step 5: Apply Purview Controls

**Portal:** Microsoft Purview

1. Verify sensitivity labels are available for Pages content.
2. Run a DLP test with representative FSI-sensitive data.
3. Confirm retention coverage by reviewing policies that include **All SharePoint Sites**.
4. Run a test eDiscovery search for `.page` content and document the results.

### Step 6: Document Legal Hold and Offboarding Procedures

1. Record the manual legal hold step required to add the user's container when preservation is needed.
2. Update the offboarding procedure to preserve Pages/Notebooks content before cleanup windows expire.
3. Identify populations that require Information Barriers and document whether Pages/Notebooks remain disabled for them.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Scope creation to approved users; test SharePoint retention and eDiscovery coverage; prefer named-user sharing only |
| **Recommended** | Add code preview decision, quarterly sharing reviews, and documented offboarding preservation workflow |
| **Regulated** | Disable Pages/Notebooks where Information Barriers are required; include manual hold workflow in examination and litigation procedures |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Pages management automation
- See [Verification & Testing](verification-testing.md) to validate Pages security
- Review Control 2.12 for External Sharing governance
