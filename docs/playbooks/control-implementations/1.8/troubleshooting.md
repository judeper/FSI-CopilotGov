# Control 1.8: Information Architecture Review — Troubleshooting

Common issues and resolution steps for information architecture review.

## Common Issues

### Issue 1: Large Number of Orphaned Sites

- **Symptoms:** Inventory reveals many sites not associated with any hub site, making them difficult to govern and organize
- **Root Cause:** Sites created before hub site implementation or created by users without hub association requirements. Self-service site creation often produces orphaned sites.
- **Resolution:**
  1. Categorize orphaned sites by template and purpose
  2. Assign each site to an appropriate hub based on business function
  3. Use `Add-SPOHubSiteAssociation -Site <url> -HubSite <hub-url>` for bulk association
  4. Consider restricting self-service site creation to require hub association

### Issue 2: Inconsistent Content Types Across Sites

- **Symptoms:** Content type analysis reveals the same type of document is classified differently across sites, or standard content types are missing from key sites
- **Root Cause:** Content types may have been created locally on individual sites rather than published from the content type hub. Organic site growth leads to inconsistency.
- **Resolution:**
  1. Identify a canonical set of FSI content types for the organization
  2. Publish standard content types from the content type hub
  3. Map existing local content types to standard types and migrate
  4. Enforce content type publication policies for new site creation

### Issue 3: Hub Site Limit Constraints

- **Symptoms:** Organization needs more hub sites than the current limit allows, preventing proper architectural organization
- **Root Cause:** SharePoint Online has a limit of 2,000 hub sites per tenant, but practical governance limits may be lower. Complex organizations may need more granular hub structures.
- **Resolution:**
  1. Review existing hubs for consolidation opportunities
  2. Use hub-to-hub associations (hub hierarchy) for more granular organization
  3. Supplement hub structure with sensitivity labels and managed metadata for additional categorization
  4. Request limit increase through Microsoft support if needed

### Issue 4: Taxonomy Term Store Conflicts

- **Symptoms:** Multiple term groups with overlapping or conflicting terms, or term sets that are not used consistently across sites
- **Root Cause:** Decentralized taxonomy management allows different business units to create conflicting term structures without coordination.
- **Resolution:**
  1. Audit the term store for duplicate and conflicting term sets
  2. Designate a taxonomy steward responsible for term store governance
  3. Merge conflicting term groups and redirect deprecated terms
  4. Publish updated term sets and communicate changes to site owners

### Issue 5: Architecture Review Scope Too Large

- **Symptoms:** Architecture review is overwhelming due to thousands of sites, making it difficult to complete within project timelines
- **Root Cause:** Large tenants with years of accumulated sites require significant effort to review comprehensively.
- **Resolution:**
  1. Prioritize the review by focusing on sites that will be in the Copilot grounding scope first
  2. Use the data access governance reports to identify highest-risk sites
  3. Review sites in waves aligned with Copilot deployment phases
  4. Accept that a complete review may span multiple quarters and document the phased approach

## Diagnostic Steps

1. **Generate quick stats:** Run Script 1 for a high-level architecture overview
2. **Identify priorities:** Sort sites by sensitivity, size, and activity level
3. **Map relationships:** Generate the hub site map to visualize the architecture
4. **Spot anomalies:** Look for sites with unusual configurations or missing associations
5. **Validate with users:** Confirm architecture findings with content owners and business stakeholders

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Minor architecture inconsistencies | SharePoint team for remediation |
| **Medium** | Significant orphaned sites with sensitive content | Governance committee for prioritization |
| **High** | Architecture gaps causing Copilot to surface incorrect content | Copilot governance team and content owners |
| **Critical** | Architecture review blocked by technical limitations | Microsoft TAM and SharePoint team |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Architecture review steps
- [PowerShell Setup](powershell-setup.md) — Analysis scripts
- [Verification & Testing](verification-testing.md) — Validation procedures
