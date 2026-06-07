# Control 2.6: Copilot Web Search and Web Grounding Controls — Portal Walkthrough

Step-by-step portal configuration for controlling Copilot's ability to search the web and use web content for response grounding.

## Prerequisites

- Entra Global Admin or AI Administrator role
- Microsoft 365 Admin Center access
- Governance committee decision on web search policy for Copilot

## Steps

### Step 1: Review Web Search Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings > Data access > Web search for Microsoft 365 Copilot and Microsoft 365 Copilot Chat

Review the current web search configuration for Copilot. The admin control is the **Allow web search in Copilot** policy in the Cloud Policy service for Microsoft 365 Apps; the Microsoft 365 admin center Data access page provides a shortcut that creates this policy. In commercial tenants, if the policy is not configured, web search is on by default and may use Bing web search to supplement responses with public web content; in GCC and DoD tenants it is off by default. For FSI environments, this behavior requires careful governance.

### Step 2: Disable or Restrict Web Search

**Portal:** Microsoft 365 Cloud Policy service (Microsoft 365 Apps)
**Path:** `https://config.office.com` > Customization > Policy Management > Allow web search in Copilot (reachable via the web search shortcut on Admin Center > Copilot > Settings > Data access)

For most FSI deployments, configure the **Allow web search in Copilot** policy and set it off to prevent Copilot from:
- Grounding responses on unverified external content
- Potentially sending organizational context to web search services
- Generating responses that mix internal and external data without clear distinction

Set the policy to off for all users, or scope it to specific user groups based on governance policy. In commercial tenants, web search stays on until this policy is configured to off, so create the policy explicitly rather than relying on defaults.

### Step 3: Configure Web Content Plugin Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Agents > Settings and Settings > Integrated apps

If web search is selectively enabled, configure the web content plugin:
- Restrict to specific user groups with business justification
- Enable content attribution so users can distinguish web-sourced content
- Configure data handling policies for web-retrieved content

### Step 4: Set Up Third-Party Plugin Web Access Controls

**Portal:** Microsoft Teams Admin Center
**Path:** Teams Admin > Teams Apps > Permission Policies

Review third-party plugins that may access web content or external data sources. Block plugins that:
- Send organizational data to external services without governance approval
- Retrieve web content that could introduce unvetted information into Copilot responses

### Step 5: Document Web Grounding Policy

Document the organization's web grounding policy including:
- Whether web search is enabled, disabled, or selectively enabled
- Which user groups have web search access and business justification
- Data handling requirements for web-sourced content
- Review cadence for web grounding policy

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Disable web search for all Copilot users |
| **Recommended** | Disable web search by default; enable for specific approved use cases with user training |
| **Regulated** | Web search disabled organization-wide; any exceptions require formal risk assessment and governance approval |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for web control automation
- See [Verification & Testing](verification-testing.md) to validate web controls
- Review Control 2.5 for overall grounding scope management
- Back to [Control 2.6](../../../controls/pillar-2-security/2.6-web-search-controls.md)
