# Control 1.3: Restricted SharePoint Search Configuration — Portal Walkthrough

Step-by-step portal configuration for implementing Restricted SharePoint Search (RSS) to limit Copilot's grounding scope to approved sites.

## Prerequisites

- SharePoint Administrator role
- SharePoint Advanced Management (SAM) license
- List of approved SharePoint sites for Copilot grounding
- Governance committee approval on the allowed sites list

## Steps

### Step 1: Enable Restricted SharePoint Search

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search

Navigate to search settings and locate the Restricted SharePoint Search toggle. Enable RSS to switch from the default "search everywhere" model to an allowlist-based model.

When enabled, SharePoint search and M365 Copilot will only surface content from sites explicitly added to the allowed list. All other sites are excluded from search results and Copilot grounding.

### Step 2: Build the Allowed Sites List

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search > Manage allowed sites

Add sites to the allowed list based on governance committee approval. Consider including:
- Departmental collaboration sites with proper access controls
- Policy and procedure document libraries
- Approved knowledge bases and reference materials

Exclude sites containing sensitive data that has not been properly classified or where permissions have not been validated.

### Step 3: Verify Site Inclusion

**Portal:** SharePoint Admin Center
**Path:** SharePoint Admin Center > Settings > Search > Restricted SharePoint Search > View allowed sites

Review the complete allowed sites list. Verify each site has been reviewed for appropriate permissions and sensitivity labels. Document the list with business justification for each included site.

The allowed list supports up to 100 sites initially. Plan site inclusion carefully for organizations with more sites than the limit.

### Step 4: Configure Search Scope for Copilot

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Settings > Microsoft 365 Copilot > Data Access

Verify that the Copilot data access settings reflect the RSS configuration. Copilot should only ground responses on content from allowed sites when RSS is enabled.

### Step 5: Communicate Changes to Users

Document the RSS configuration and communicate to Copilot users that search results and Copilot responses will be limited to approved content sources. Set expectations that some previously searchable content may no longer appear in results.

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Enable RSS with a conservative initial allowed list of fully vetted sites |
| **Recommended** | Implement RSS with quarterly review of the allowed sites list by governance committee |
| **Regulated** | Enable RSS with formal change control process for any additions to the allowed list; maintain audit trail of all changes |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for scripted RSS management
- See [Verification & Testing](verification-testing.md) to validate search restrictions
- Review Control 1.4 for Semantic Index Governance as a complementary control
