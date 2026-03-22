# Control 2.6: Copilot Web Search and Web Grounding Controls — Portal Walkthrough

Step-by-step portal configuration for controlling Copilot's ability to search the web and use web content for response grounding.

## Prerequisites

- Global Administrator role
- Microsoft 365 Admin Center access
- Governance committee decision on web search policy for Copilot

## Steps

### Step 1: Review Web Search Settings

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings > Data access > Web search

Review the current web search configuration for Copilot. By default, Copilot may use Bing web search to supplement responses with public web content. For FSI environments, this behavior requires careful governance.

### Step 2: Disable or Restrict Web Search

**Portal:** Microsoft 365 Admin Center
**Path:** Admin Center > Copilot > Settings > Data access > Web search

For most FSI deployments, disable web search to prevent Copilot from:
- Grounding responses on unverified external content
- Potentially sending organizational context to web search services
- Generating responses that mix internal and external data without clear distinction

Toggle web search to "Off" for all users or specific groups based on governance policy.

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
