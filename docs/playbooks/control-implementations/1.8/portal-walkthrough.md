# Control 1.8: Information Architecture Review — Portal Walkthrough

Step-by-step portal procedures for reviewing and optimizing the Microsoft 365 information architecture for Copilot readiness.

## Prerequisites

- SharePoint Admin and Global Reader roles
- Access to SharePoint admin center and Microsoft Purview
- Content inventory documentation or content management system records
- Information architecture governance committee or content owners

## Steps

### Step 1: Inventory Site Architecture

**Portal:** SharePoint admin center
**Path:** SharePoint Admin > Active Sites

Review the complete site inventory to understand the current information architecture. Categorize sites by:
- **Type:** Team sites, communication sites, hub sites, OneDrive
- **Purpose:** Departmental, project, cross-functional, knowledge base
- **Hub associations:** Which sites are connected to hub sites
- **Content volume:** Storage usage and item counts

Export the site list for documentation and analysis.

### Step 2: Evaluate Hub Site Structure

**Portal:** SharePoint admin center
**Path:** SharePoint Admin > Active Sites > Hub sites filter

Review the hub site hierarchy. Hub sites define content relationships that affect how Copilot discovers and associates content. Verify:
- Hub sites align with business unit or function boundaries
- Associated sites are correctly linked to their parent hub
- No orphaned sites that should be hub-associated

Identify opportunities to improve hub structure for better Copilot content grounding.

### Step 3: Review Content Type and Metadata Standards

**Portal:** SharePoint admin center
**Path:** SharePoint admin center > Content services > Content type gallery

Review the content type hierarchy published from the content type hub. Consistent content types and metadata improve Copilot's ability to understand and classify content accurately.

Verify that FSI-relevant content types are defined (e.g., client agreements, regulatory filings, research reports, policies and procedures).

### Step 4: Assess Taxonomy and Term Store

**Portal:** SharePoint admin center
**Path:** SharePoint admin center > Content services > Term store

Review the managed metadata term store for FSI-relevant term groups:
- Business unit taxonomy
- Document type classification
- Regulatory domain categorization
- Geographic region tagging

Verify term sets are current and actively used for content tagging.

### Step 5: Map Content to Copilot Use Cases

Document how the current information architecture supports intended Copilot use cases. For each planned Copilot use case, identify:
- Which content sources will be accessed
- Whether content is properly organized and labeled
- Any architectural gaps that could result in poor Copilot responses
- Recommended architecture improvements

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Complete information architecture inventory and document current state |
| **Recommended** | Optimize hub site structure and implement consistent content types for FSI data |
| **Regulated** | Formal information architecture governance with annual review; content types and metadata standards enforced via policy |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for architecture analysis scripts
- See [Verification & Testing](verification-testing.md) to validate architecture readiness
- Review Control 1.4 for Semantic Index Governance considerations
