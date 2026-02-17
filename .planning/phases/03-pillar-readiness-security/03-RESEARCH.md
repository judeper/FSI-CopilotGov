# Phase 3: Pillar Updates — Readiness and Security - Research

**Researched:** 2026-02-17
**Domain:** Microsoft 365 Copilot governance documentation — Pillar 1 (Readiness) and Pillar 2 (Security) controls
**Confidence:** HIGH for platform changes verified with official docs; MEDIUM for FSI regulatory citations

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Update depth**
- Default approach: integrate new content into existing document sections — new bullets, expanded paragraphs, updated tables. Do not create new top-level sections unless absolutely necessary.
- Claude's discretion on whether major additions (e.g., P2-01 two DLP policy types, P2-06 Risky Agents with 4 sub-features) warrant a new subsection. Threshold: roughly 3+ paragraphs of genuinely new conceptual content.
- Seamless integration — no "Updated v1.1" markers, no changelogs. Updated controls should read as if they were always current. Commit history tracks what changed.
- When correcting factual errors (e.g., P1-05 SAM licensing), rewrite surrounding content that was built on the wrong assumption. Don't just fix the fact — fix the logic that depended on it.

**Playbook boundaries**
- **Full playbook alignment**: when updating a control, also update all 4 playbook types (portal-walkthrough, PowerShell, audit-log, compliance-report) for that control to match.
- Absorb PLAY-01 (PnP PowerShell Entra app registration requirement for controls 1.2, 1.6, 1.8, and 2.2) and PLAY-03 (portal path updates) into Phase 3. Phase 6 retains PLAY-02 (Exchange REST-only patterns) and PLAY-04 (cross-linking).
- Opportunistically review ALL Pillar 1+2 playbooks, even for controls without Phase 3 requirements — fix obvious issues (stale paths, wrong portal names) encountered while working in neighboring files.

**FSI framing depth**
- Every new capability gets regulatory mapping when the connection is direct and specific. Format: capability description + explicit regulator + section number (e.g., "per FINRA 2026 Oversight Report, Section 4.2" or "per OCC 2025-26 §III.B").
- Skip regulatory framing when the connection is indirect or a stretch — pure platform feature updates don't need forced reg ties.
- Normalize the FSI tone across all Pillar 1+2 controls during this phase. Use the update as an opportunity to strengthen FSI framing in controls that are currently too generic.

**Tier differentiation**
- **Baseline**: minimum viable configuration — feature is actually enabled with simplest, safest defaults
- **Recommended**: standard operational configuration with monitoring and moderate enforcement
- **Regulated**: strictest settings with additional audit requirements and manual review gates
- Match each control's existing tier presentation format. Be consistent within each file.
- When existing tier recommendations become outdated: note the change in the text but keep the tier structure stable.

### Claude's Discretion
- Whether individual major additions warrant new subsections vs. inline integration
- Exact placement of new content within existing document structures
- How to restructure surrounding content when correcting factual errors
- Which playbooks on non-requirement controls need fixes when reviewing opportunistically

### Deferred Ideas (OUT OF SCOPE)
- PLAY-02 (Exchange REST-only patterns for 12 Exchange Online playbooks) — remains in Phase 6
- PLAY-04 (cross-linking: Related Controls, Prerequisites, See Also) — remains in Phase 6
- Full playbook structural overhaul — out of scope; Phase 3 aligns content, not architecture
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| P1-01 | Update 1.1 to add Optimization Assessment as pre-deployment requirement and Office update channel governance | Verified: Optimization Assessment is a documented Microsoft pre-deployment recommendation; update channel (Current Channel / Monthly Enterprise Channel) is the supported path for Copilot features |
| P1-02 | Update 1.2 to add DSPM unified experience (AI observability, item-level remediation, Purview Posture Agent, Shadow AI discovery) | Verified: New unified DSPM (preview Dec 2025) merges classic DSPM + DSPM for AI; Purview Posture Agent (Jan 2026 preview) confirmed |
| P1-03 | Update 1.3 to document RCD as complementary tool to RSS with comparison table and SAM licensing note | Verified: RCD and RSS are documented as complementary; SAM now included with Copilot licenses (Ignite 2024 announcement, early 2025 effective) |
| P1-04 | Update 1.6 to add new RBAC roles (Purview Data Security AI Viewer, AI Content Viewer, AI Administrator from Entra) | Verified: All three roles confirmed from Microsoft Learn permissions doc for DSPM for AI (August 2025) |
| P1-05 | Update 1.7 to correct SAM licensing and add Data Access Governance reports, Restricted Access Control | Verified: SAM included with M365 Copilot license. RAC (Restricted Access Control) and new site permissions snapshot report are documented SAM capabilities |
| P1-06 | Update 1.9 to add Frontline (F1/F3) SKU availability and pay-as-you-go licensing option | Verified: F1/F3 can add Copilot as add-on ($30/user/month); PAYG Copilot Chat at $0.01/message via Azure billing confirmed |
| P2-01 | Update 2.1 to document two distinct DLP policy types (label-based + SIT-based prompt blocking), default DLP policy for Copilot, and Edge browser DLP | Verified: Two policy types are distinct and cannot be combined; default policy in simulation mode (GA Jan 2026); Edge DLP GA Sep 2025 |
| P2-02 | Update 2.2 to add label groups replacing parent labels, Copilot Studio agent label inheritance, auto-labeling nested rule logic | Verified: Label groups GA Dec 2025–Jan 2026 (MC1111778); agent inherits highest label; nested AND/OR/NOT auto-labeling confirmed Dec 2025 |
| P2-03 | Update 2.3 to document CA "All resources" enforcement tightening (March 2026), verify Enterprise Copilot Platform app ID, add IRM-integrated dynamic blocking | Verified: CA enforcement March 27, 2026; app ID fb8d773d-7ef8-4ec0-a117-179f88add510 confirmed; IRM Adaptive Protection dynamic blocking confirmed |
| P2-04 | Update 2.4 to document Channel Agent in Teams NOT supporting Information Barriers with compensating controls | Verified: Official Microsoft Learn doc explicitly states "Information barriers aren't supported for Channel Agent" |
| P2-05 | Update 2.9 to add AI app catalog (400+ apps) and agent threat detection in XDR platform | Verified with correction: catalog has 1,000+ generative AI apps (not 400); agent threat detection in Defender XDR confirmed Sep 2025 |
| P2-06 | Update 2.10 to add Risky Agents policy template (auto-deployed), AI usage indicator category, data risk graphs, IRM Triage Agent | Verified: Risky Agents auto-deployed (Dec 2025); data risk graphs GA (Dec 2025); Triage Agent GA (Dec 2025); AI usage indicator is an IRM signal category |
| PLAY-01 | Update 4 PnP PowerShell playbooks (1.2, 1.6, 1.8, 2.2) to add custom Entra app registration requirement | Verified: Multi-tenant PnP Management Shell app deleted Sep 9, 2024; custom app registration now mandatory |
| PLAY-03 | Update portal walkthrough playbooks for controls with changed admin paths | Verified: Purview Copilot security controls moved to MAC > Copilot > Overview > Security tab (Jan 2026); DLP creatable from MAC directly |
</phase_requirements>

---

## Summary

Phase 3 updates 12 control documents across Pillars 1 and 2, plus 4 PnP PowerShell playbooks and portal walkthrough updates. The research confirms all 12 requirements are grounded in real, documented Microsoft platform changes from mid-2025 through February 2026. The updates range from simple fact corrections (SAM licensing, app ID verification) to substantive new capability documentation (dual DLP policy types, DSPM unified experience, Risky Agents).

The most consequential factual error in the current framework is Control 1.7's licensing table, which states "Microsoft 365 Copilot: No — SAM is an add-on." This is incorrect as of early 2025 (announced at Ignite 2024): SAM is now included with M365 Copilot licenses. The surrounding logic in 1.7 was built on this error and needs rewriting, not just a line fix.

The most complex documentation challenge is P2-01 (DLP for Copilot): the two DLP policy types are architecturally distinct, serve different purposes, and cannot be combined. The current 2.1 control documents only one type (label-based response blocking), missing the newer SIT-based prompt blocking entirely. This will likely need a new subsection given the volume of genuinely different conceptual content.

**Primary recommendation:** Work through requirements in document order (P1-01 through P2-06) within a single plan per requirement pair. Update control doc first, then all 4 playbook types for that control. Apply PnP registration fix (PLAY-01) whenever touching 1.2, 1.6, 1.8, or 2.2 PowerShell playbooks.

---

## Standard Stack

### Correct Product Names and Portal Paths (February 2026)

| Thing | Correct 2026 Name | Wrong/Stale Name |
|-------|-------------------|-----------------|
| AI governance dashboard | Microsoft Purview DSPM for AI (unified) | DSPM for AI (classic) / AI Hub |
| Copilot compliance view | MAC > Copilot > Overview > Security tab | Separate Microsoft Purview portal path |
| DLP creation for Copilot | Microsoft Purview Compliance Portal OR Microsoft 365 Admin Center | Purview only |
| Agent inventory | Agent Registry (powered by Entra ID) | Agent inventory |
| Agent management | Agent 365 / M365 Admin Center > Copilot > Agents | Scattered across Copilot Studio, SharePoint, Integrated Apps |
| Main admin portal | Microsoft 365 Admin Center (MAC) | Microsoft 365 admin center (mixed casing) |
| Copilot Chat product | Microsoft 365 Copilot Chat (m365copilot.com) | Microsoft Copilot / BizChat |
| App name | Microsoft 365 Copilot (app) | Microsoft 365 (app) |
| Policy framework name | Copilot Control System (CCS) | Copilot admin settings |

### Verified Admin Portal Paths (February 2026)

| Task | Verified Path |
|------|---------------|
| DSPM for AI (unified) | Microsoft Purview > Data Security Posture Management |
| Copilot security overview | MAC > Copilot > Overview > Security tab |
| DLP policy creation (Copilot) | Microsoft Purview > Data loss prevention > Policies > Create policy OR MAC > Copilot > Overview > Security tab |
| Default DLP policy for Copilot | MAC > Copilot > Overview > Security tab (accessible from there) |
| Agent management | MAC > Copilot > Agents |
| SharePoint DAG reports | SharePoint Admin Center > Data access governance |
| RCD per-site | SharePoint Admin Center > Sites > Active sites > [site] > Settings |
| SAM licensing | Included with M365 Copilot license (no separate purchase for Copilot tenants) |
| IRM policies | Microsoft Purview > Insider Risk Management > Policies |
| Conditional Access | Microsoft Entra admin center > Protection > Conditional Access |

### Verified PowerShell Commands and Modules (February 2026)

| Task | Current Command | Module |
|------|-----------------|--------|
| Connect to SPO | `Connect-SPOService -Url "https://<tenant>-admin.sharepoint.com"` | Microsoft.Online.SharePoint.PowerShell |
| RCD per site | `Set-SPOSite -RestrictContentOrgWideSearch $true` | Microsoft.Online.SharePoint.PowerShell |
| RSS enable | `Set-SPOTenant -IsRestrictedSharePointSearch $true` | Microsoft.Online.SharePoint.PowerShell |
| RSS site add | `Add-SPOTenantRestrictedSearchAllowedList` | Microsoft.Online.SharePoint.PowerShell |
| PnP Connect | `Connect-PnPOnline -Url <url> -ClientId <appId> -Interactive` | PnP.PowerShell (requires custom app registration) |
| Connect to Entra | `Connect-Entra -Scopes "User.Read.All"` | Microsoft.Entra |
| Teams meeting policy | `Set-CsTeamsMeetingPolicy -Identity Global -Copilot Enabled` | MicrosoftTeams |

### PnP PowerShell: Custom App Registration Required (PLAY-01)

The multi-tenant PnP Management Shell Entra ID app (App ID: `31359c7f...`) was **deleted September 9, 2024**. All PnP PowerShell scripts must now use a tenant-specific Entra ID app registration.

**Registration pattern (one-time setup):**
```powershell
# Register app for interactive login (one-time per tenant)
Register-PnPEntraIDAppForInteractiveLogin `
    -ApplicationName "PnP Management Shell - [TenantName]" `
    -Tenant "contoso.onmicrosoft.com" `
    -SharePointDelegated `
    -GraphDelegated `
    -Interactive

# Then connect using the custom app
Connect-PnPOnline -Url "https://contoso.sharepoint.com/sites/site" `
    -ClientId "<your-app-id>" `
    -Interactive
```

This pattern must appear in the Prerequisites section of all 4 affected PowerShell playbooks (1.2, 1.6, 1.8, 2.2).

---

## Architecture Patterns

### Document Update Pattern

When updating an existing control document, the integration sequence is:

1. **Locate the natural insertion point** — find the section that logically owns the new content (assessment tools table, governance levels, setup steps, etc.)
2. **Integrate, don't append** — weave new capabilities into existing tables and paragraphs; don't add a "New in 2026" section at the bottom
3. **Update tier table rows** — if the new capability has tier differentiation, add a row or expand existing rows in the Governance Levels table
4. **Add FSI regulatory mapping** — when the connection is specific and direct, add the regulator + citation inline with the capability description
5. **Update Verification Criteria** — add verification steps for newly documented capabilities
6. **Update playbooks** — after the control doc is updated, open all 4 playbook types and align them

### Factual Error Correction Pattern (P1-05 SAM Licensing)

When a factual error has downstream logic built on it:

1. **Find all affected statements** — search the document for text that logically depends on the wrong fact
2. **Correct the root fact** — fix the licensing table row directly
3. **Trace the implications** — the current 1.7 framing says "factor SAM licensing into Copilot deployment cost models" and "Cost-Benefit of SAM Licensing" — these need rewriting since SAM is now included
4. **Rewrite surrounding logic** — the "Cost-Benefit" consideration becomes "Licensing Clarification" (SAM included with Copilot but for Copilot-licensed users only; standalone SAM still costs $3/user for governance admins who don't have Copilot licenses)

### New Subsection Threshold

Use a new subsection (`###`) when:
- 3+ paragraphs of genuinely distinct conceptual content (not just updated details)
- The new content introduces a new workflow, not just additional features to an existing one
- Examples that cross the threshold: DLP dual policy types (P2-01), Risky Agents 4-part feature cluster (P2-06)

Use inline integration (bullets, table rows, expanded paragraphs) when:
- Adding a new feature to an existing capability category
- Correcting or updating existing facts
- Examples that stay inline: new RBAC roles (P1-04), label groups (P2-02), CA enforcement date (P2-03)

### Tier Table Consistency

Each control has its own tier format. Match the existing format:
- 1.1, 1.2, 1.7, 2.1, 2.9, 2.10 use a 3-column table (Level | Requirement | Rationale)
- 1.3, 1.6, 1.9 use the same 3-column format
- 2.2, 2.3, 2.4 use the same 3-column format

When a new capability goes into the tier table: add it to the appropriate tier row's Requirement cell as additional text. If it applies to all tiers at different levels of enforcement, add a row or expand all three rows proportionally.

---

## Don't Hand-Roll

| Problem | Don't Invent | Use Instead | Source |
|---------|-------------|-------------|--------|
| Enterprise Copilot Platform app ID | A made-up GUID | `fb8d773d-7ef8-4ec0-a117-179f88add510` | Microsoft Learn, verified Feb 2026 |
| DLP Copilot location name | Variation of the correct name | "Microsoft 365 Copilot" (the exact location label in Purview) | Microsoft Learn DLP docs |
| SAM licensing statement | Any claim about SAM cost | "SAM is included with Microsoft 365 Copilot licenses" (with the nuance that it covers Copilot-licensed users; non-Copilot admins still need standalone SAM) | Ignite 2024 announcement, verified |
| PnP app ID | The old multi-tenant ID | The tenant-specific pattern — no fixed app ID exists | PnP PowerShell docs |
| Risky Agents GA status | "GA" without qualification | "GA (December 2025) for auto-deployment; full GA targeting December 2026" — the auto-deploy phase is GA but full general availability is later | MC1200579 |
| AI app catalog count | "400+ apps" (from the requirement spec) | "1,000+ generative AI apps" — the catalog has grown beyond the 400 figure in the original requirement | Microsoft Defender for Cloud Apps docs |
| Label groups term | "parent labels deprecated" | "Parent labels migrating to label groups (GA January 2026)" — migration not immediate deletion | MC1111778, Microsoft Learn |
| CA enforcement date | "Spring 2026" | "March 27, 2026 rolling through June 2026" — the exact announced date | Microsoft Entra blog post |

---

## Common Pitfalls

### Pitfall 1: SAM Licensing Nuance
**What goes wrong:** Stating "SAM is free" without qualification. It is included for orgs with M365 Copilot licenses, for Copilot governance purposes. SharePoint admins without Copilot licenses still need a standalone SAM license.
**Why it happens:** The Ignite 2024 announcement was sometimes characterized as "SAM is now free" in community posts.
**How to avoid:** State precisely: "SharePoint Advanced Management (SAM) is included with Microsoft 365 Copilot licenses at no additional cost, enabling SharePoint administrators to access SAM features for Copilot governance. Organizations managing SharePoint without Copilot licenses require the standalone SAM add-on."
**Warning signs:** Any text in 1.7 that says SAM requires a separate purchase, or budget language treating SAM as a cost item for Copilot deployments.

### Pitfall 2: DLP Policy Type Conflation
**What goes wrong:** Treating label-based DLP and SIT-based prompt blocking as the same policy with different settings.
**Why it happens:** Both use the Microsoft Purview DLP interface; both target Copilot. The distinction between them is architectural, not just configuration.
**How to avoid:** Clearly name both: (1) "Label-based DLP" — blocks Copilot responses when referenced content carries a sensitivity label; (2) "SIT-based prompt blocking" — blocks Copilot from responding when the user's prompt itself contains sensitive data patterns. These cannot be combined into a single policy and serve different enforcement points.
**Warning signs:** Any DLP section that describes only one mechanism, or uses the same policy structure for both functions.

### Pitfall 3: CA App ID Error
**What goes wrong:** The current 2.3 document has app ID `fb8d773d-7ef4-4c2f-a801-2a5e1e8e1098` (incorrect). The verified correct ID is `fb8d773d-7ef8-4ec0-a117-179f88add510`.
**Why it happens:** The two GUIDs look similar and the error may have been a transcription mistake in the original authoring.
**How to avoid:** Use the verified ID from Microsoft Learn (Conditional Access protections for Generative AI page, February 2026).
**Warning signs:** Any document referencing `fb8d773d-7ef4-4c2f` — the segment after `-7ef` is wrong in the existing document.

### Pitfall 4: Channel Agent vs. Standard Copilot IB Confusion
**What goes wrong:** Applying the standard Copilot IB statement ("Copilot respects information barriers") to Channel Agent.
**Why it happens:** Channel Agent is a newer surface and the IB limitation is easy to miss.
**How to avoid:** In 2.4, explicitly distinguish: standard M365 Copilot Chat respects IB; Channel Agent in Teams does NOT. Both must be documented in the same control with clear surface labeling.
**Warning signs:** Any IB statement that doesn't distinguish between Copilot Chat and Channel Agent.

### Pitfall 5: Risky Agents GA Status Overclaim
**What goes wrong:** Calling the Risky Agents policy template fully GA.
**Why it happens:** The auto-deployment of Risky Agents for Copilot Studio + Azure AI Foundry agents started in December 2025, but the full GA is targeted for December 2026.
**How to avoid:** The auto-deploy phase (Dec 2025) is GA for existing tenants. The policy template itself in IRM is in preview, with GA expected December 2026. Write as: "Microsoft auto-deploys a Risky Agents policy for all Copilot Studio and Azure AI Foundry agents (GA December 2025 for auto-deployment). The Risky Agents policy template is currently in public preview with general availability targeted for late 2026."

### Pitfall 6: PnP Without Registration
**What goes wrong:** PnP PowerShell scripts that use `Connect-PnPOnline -Interactive` without specifying a `-ClientId`.
**Why it happens:** Scripts written before September 9, 2024 worked with the shared multi-tenant PnP Management Shell app.
**How to avoid:** All four affected playbooks (1.2, 1.6, 1.8, 2.2) must include a Prerequisites section requiring the custom Entra ID app registration, with the `Register-PnPEntraIDAppForInteractiveLogin` registration step and the `-ClientId` parameter on all `Connect-PnPOnline` calls.
**Warning signs:** Any `Connect-PnPOnline` call without `-ClientId`. Any prerequisite that says "PnP PowerShell module" without mentioning app registration.

### Pitfall 7: AI App Catalog Count
**What goes wrong:** Using "400+" for the AI app catalog count as stated in the phase requirements spec.
**Why it happens:** The 400 figure may have been accurate at an earlier point; the catalog has grown.
**How to avoid:** Use "1,000+ generative AI apps" (the current figure from Microsoft Defender for Cloud Apps catalog). The catalog overall has 31,000+ cloud apps; the generative AI subcategory has 1,000+.

### Pitfall 8: DSPM Navigation Path
**What goes wrong:** Sending admins to "Microsoft Purview portal > DSPM for AI" without noting that Copilot security controls are now also accessible in MAC.
**Why it happens:** The new unified DSPM launched in December 2025 and the MAC security tab for Copilot went GA January 2026 — both post-date the original framework authoring.
**How to avoid:** For controls using DSPM (1.1, 1.2), note both paths: the Purview portal path for full DSPM functionality and the MAC > Copilot > Overview > Security tab for quick access to the default DLP policy and Copilot-specific security actions.

---

## Code Examples

### Example: Two DLP Policy Types Documentation Pattern

```markdown
### DLP Policy Type 1: Label-Based Response Blocking

Configured in the **Microsoft 365 Copilot** DLP policy location. When a user's Copilot
prompt causes grounding against a file or email that carries a sensitivity label matching
the policy condition, Copilot is blocked from including that content in its response.

**Enforcement point:** Copilot's response generation (grounding phase)
**What is scanned:** Files and emails referenced during Copilot's retrieval
**Primary use:** Prevent Copilot from surfacing labeled content to users who should not receive it

### DLP Policy Type 2: SIT-Based Prompt Blocking

A distinct policy type that scans the user's **prompt itself** for sensitive information
types before Copilot processes the request. When a user types sensitive data directly into
a Copilot prompt (e.g., pastes credit card numbers, SSNs), Copilot is blocked from responding,
including blocking grounding via Microsoft Graph or web search.

**Enforcement point:** The user's prompt (before Copilot processes it)
**What is scanned:** The text the user types into Copilot
**Primary use:** Prevent users from inadvertently submitting sensitive data to Copilot

These two policy types cannot be merged into a single policy — they are configured separately
in Microsoft Purview and address different risk vectors.
```

### Example: New RBAC Roles Table Row Pattern

```markdown
| **Purview Data Security AI Viewer** | Read-only access to DSPM for AI dashboards, activity reports, and AI observability metrics. Does not expose prompt/response content. | DSPM monitoring, compliance reporting |
| **Purview Data Security AI Content Viewer** | Extends AI Viewer with ability to view actual prompt and response content in DSPM. Combines AI Viewer + Content Explorer Content Viewer permissions. | Compliance investigation, DLP match review |
| **AI Administrator** (Microsoft Entra) | Full management of Copilot DLP policies in MAC; scoped authorizations for Copilot, agents, and AI services. Separate from Purview Compliance Administrator. | Copilot policy governance without full Purview admin |
```

### Example: SAM Licensing Correction Pattern

```markdown
### SAM Licensing Requirements

| License | Includes SAM | Notes |
|---------|-------------|-------|
| Microsoft 365 E3 | No | SAM capabilities available via standalone add-on or Copilot license |
| Microsoft 365 E5 | No | SAM capabilities available via standalone add-on or Copilot license |
| Microsoft 365 Copilot | **Yes** | SAM included at no additional cost for Copilot governance (Ignite 2024) |
| SharePoint Advanced Management add-on | Yes | Per-user license for users without Copilot licenses |
| Microsoft Syntex (SharePoint Premium) | Yes | Includes SAM capabilities |

**Licensing note:** SAM is included with Microsoft 365 Copilot licenses, enabling SharePoint
administrators to deploy all SAM governance capabilities without a separate purchase. For
organizations managing SharePoint governance without Copilot licenses, the standalone SAM
add-on (~$3/user/month) remains available.
```

### Example: CA Enforcement Timeline Documentation

```markdown
### Conditional Access Enforcement Change (March 2026)

Microsoft Entra ID will begin enforcing a behavioral change to Conditional Access policies
starting **March 27, 2026**, with rollout completing across all cloud environments through
June 2026.

**What changes:** Policies targeting "All resources" that include resource exclusions will
now enforce MFA and device compliance even for the excluded resources when users sign in
through client applications requesting low-privilege scopes. Previously, these exclusions
created a bypass path.

**FSI impact:** Institutions with CA policies structured as "All resources + exclusions"
should audit their policies before March 2026. If the Enterprise Copilot Platform
(App ID: `fb8d773d-7ef8-4ec0-a117-179f88add510`) is listed as an exclusion in any
"All resources" policy, those policies will now enforce controls against Copilot access.

**Action:** Run the Conditional Access optimization agent in Microsoft Entra ID to identify
affected policies and test behavior in report-only mode before the enforcement date.
```

### Example: PnP Custom App Registration Prerequisite Block

```markdown
## Prerequisites

Before running any scripts in this playbook, complete a one-time Entra ID app registration
for PnP PowerShell. The shared multi-tenant PnP Management Shell app was retired September 9,
2024. All PnP PowerShell automation now requires a tenant-specific app registration.

```powershell
# One-time setup: Register a tenant-specific app for PnP PowerShell
Register-PnPEntraIDAppForInteractiveLogin `
    -ApplicationName "PnP Governance Shell - [YourOrg]" `
    -Tenant "yourorg.onmicrosoft.com" `
    -SharePointDelegated `
    -GraphDelegated `
    -Interactive
```

Save the returned Client ID. All `Connect-PnPOnline` calls must include `-ClientId <your-app-id>`.
```

### Example: Channel Agent IB Limitation Documentation

```markdown
### Information Barrier Coverage by Copilot Surface

| Surface | IB Enforced | Notes |
|---------|-------------|-------|
| Microsoft 365 Copilot Chat | Yes | Respects IB policies for Microsoft Graph grounding |
| Word, Excel, PowerPoint, Outlook | Yes | Document-level IB enforcement applies |
| Teams Copilot (meeting summaries, chat) | Yes | Standard Teams IB applies |
| **Channel Agent in Teams** | **No** | Documented limitation: IB is not supported for Channel Agent. Channel Agent may return content that crosses IB boundaries. |

**Compensating controls for Channel Agent IB gap:**
- Restrict Channel Agent deployment to homogeneous segments (do not deploy in channels where IB-separated users are members)
- Apply sensitivity labels to content in IB-affected channels so Channel Agent cannot process labeled content
- Monitor Channel Agent activity via DSPM for AI to detect anomalous cross-segment content surfacing
- Per SEC Rule 10b-5 and FINRA Rule 5280 Chinese Wall requirements, document this limitation and compensating controls in the firm's supervisory procedures and information barrier policies
```

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact on Phase 3 |
|--------------|------------------|--------------|-------------------|
| SAM is a $3/user add-on separate from Copilot | SAM included with M365 Copilot license | Ignite 2024 / early 2025 | Rewrite 1.7 licensing table and all cost-benefit language |
| Single DLP policy type targets Copilot (label-based) | Two distinct types: label-based + SIT-based prompt blocking | Nov 2025 (SIT-based preview); Q1 2026 (GA) | Major expansion to 2.1 — likely warrants new subsection |
| DSPM for AI (classic) — separate from main DSPM | Unified DSPM merging both into single experience with AI observability | Dec 2025 (preview) | Update 1.2 DSPM capability descriptions and navigation paths |
| Parent labels with child labels in Purview | Label groups replacing the parent/child hierarchy | GA Dec 2025–Jan 2026 | Update 2.2 label taxonomy description |
| Copilot Studio agents had no label inheritance | Agents inherit highest sensitivity label from knowledge sources | Aug–Sep 2025 | Add to 2.2 label inheritance section |
| Auto-labeling: simple conditions only | Auto-labeling supports nested AND/OR/NOT logic | Dec 2025 | Add to 2.2 auto-labeling section |
| IRM had no agent-specific policies | Risky Agents auto-deployed for Copilot Studio + Azure AI Foundry agents | Dec 2025 | Major addition to 2.10 |
| IRM alerts required manual triage | IRM Triage Agent (Security Copilot) automates alert queue | GA Dec 2025 | Add to 2.10 |
| MDCA: general cloud app catalog | MDCA: 1,000+ generative AI apps categorized + agent threat detection in XDR | 2025 | Update 2.9 |
| CA "All resources" exclusions bypassed enforcement | Enforcement closing — March 27, 2026 | Mar–Jun 2026 | Add timeline warning to 2.3 |
| PnP used shared multi-tenant management shell | PnP requires custom Entra app registration | Sep 9, 2024 | Fix 4 PowerShell playbooks (PLAY-01) |
| PnP Management Shell App (shared, 31359c7f...) | Deleted. Must use tenant-specific registration | Sep 9, 2024 | All 4 affected playbooks must add registration prerequisites |
| DSPM only accessible from Purview portal | DSPM/Copilot security also accessible from MAC > Copilot > Security | Jan 2026 | Update portal-walkthrough playbooks for 1.1, 1.2, 2.1 |
| Purview Posture Agent did not exist | Purview Posture Agent (NL search across M365 + Copilot interactions, no SITs needed) | Jan 2026 preview | Add to 1.2 DSPM capabilities |
| Shadow AI: only Defender for Endpoint traffic analysis | Shadow AI: also detected via DSPM unified experience | 2025–2026 | Note in 1.2 |

**Deprecated / outdated content to remove or correct:**
- Control 1.7 "Microsoft 365 Copilot: No — Copilot license does not include SAM" — FALSE, correct this row
- Control 2.3 App ID `fb8d773d-7ef4-4c2f-a801-2a5e1e8e1098` — WRONG, use `fb8d773d-7ef8-4ec0-a117-179f88add510`
- Any DLP section describing only sensitivity-label-based blocking as the only DLP mechanism for Copilot
- Any PnP PowerShell `Connect-PnPOnline` without `-ClientId`
- Any statement that SAM requires a separate purchase for Copilot governance
- Any statement that all Copilot surfaces respect information barriers (Channel Agent does not)

---

## FSI Regulatory Citations Verified

These are the confirmed regulatory citations with specific section references for use in Phase 3 content:

| Capability | Regulator | Specific Citation |
|------------|-----------|------------------|
| Agentic AI monitoring (Risky Agents) | FINRA | 2026 Annual Regulatory Oversight Report, GenAI Section (Dec 9, 2025) |
| Agentic AI supervisory controls | FINRA | Rules 3110/3120 — supervisory systems must cover AI workflow engines selecting intermediate actions |
| Books and records for AI interactions | FINRA | Rule 4511 / Exchange Act Rule 17a-4 — full-chain telemetry for AI decision reconstruction |
| Prompt-level DLP (SIT-based) | SEC | Regulation S-P (17 CFR §248), amended effective Dec 3, 2025 (larger entities) — customer information safeguards |
| CA enforcement / identity security | NYDFS | 23 NYCRR Part 500 Section 500.12 — MFA requirements for external network access |
| Channel Agent IB gap documentation | SEC | Rule 10b-5; FINRA Rules 5280, 2241, 2242 — information barrier maintenance |
| IRM Triage Agent / AI-assisted governance | OCC | Bulletin 2025-26 — proportionate model risk management; Bulletin 2011-12 (SR 11-7) for baseline |
| SAM Data Access Governance reports | GLBA | Section 501(b) — safeguards for customer information, least privilege |
| Optimization Assessment (P1-01) | FFIEC | IT Examination Handbook (Information Security Booklet) — risk assessment for new technology deployments |
| Frontline (F1/F3) licensing | SEC | 2026 Division of Examinations Priorities (Nov 17, 2025) — AI in internal processes and back-office operations |

**Citations that are direct and should be included:** All of the above.
**Citations that are indirect/stretch:** Do not force regulatory framing on the Frontline SKU addition or the auto-labeling nested logic update — these are platform feature clarifications without a specific regulatory trigger.

---

## Open Questions

1. **Purview Data Security AI Content Viewer role name**
   - What we know: The research report names three roles: "Purview Data Security AI Viewer," "Purview Data Security AI Content Viewer," and "AI Administrator from Entra"
   - What's slightly unclear: The official Microsoft Learn DSPM permissions page uses "Purview Data Security AI Viewer" and "Purview Data Security Content Explorer Content Viewer" — the latter combines two rights. The phase requirement spec uses "AI Content Viewer" as a shorthand. The official page should be consulted directly before writing the role names into 1.6.
   - Recommendation: Use the exact names from https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-permissions when writing control 1.6.

2. **Risky Agents auto-deploy scope**
   - What we know: Auto-deployment is confirmed for Copilot Studio and Azure AI Foundry agents (Dec 2025). Message center MC1200579 confirms this.
   - What's slightly unclear: Whether prebuilt Microsoft agents (not Copilot Studio agents) are also covered by auto-deployment. The Purview changelog notes that "Microsoft prebuilt agents, third-party agents, and SharePoint agents are not yet included" in agent admin activity audit logs — this may also apply to the Risky Agents scope.
   - Recommendation: Scope the Risky Agents documentation to "Copilot Studio and Azure AI Foundry agents" and note that coverage for other agent types is expected to expand.

3. **Default DLP policy: label-based or SIT-based?**
   - What we know: A default DLP policy for Copilot in simulation mode was announced (MC1182689) and went GA January 2026. It is configurable from MAC.
   - What's unclear: Whether the default policy is the label-based type, the SIT-based prompt blocking type, or a combined policy. The research suggests it is the SIT-based prompt blocking type (described as "safeguarding prompts containing sensitive data"), but this needs confirmation when writing P2-01.
   - Recommendation: When writing 2.1, describe the default policy as the SIT-based prompt blocking type (based on MC1181998/MC1182689 messaging), but note it can be configured via both MAC and Purview portal.

4. **Pay-as-you-go (PAYG) Copilot Chat for F1/F3**
   - What we know: PAYG for Copilot Chat ($0.01/message) is available as Azure-billed. F1/F3 users can add the M365 Copilot license as a $30/user/month add-on.
   - What's unclear: Whether PAYG specifically targets F1/F3 workers as the primary audience or is for any user without a full Copilot license.
   - Recommendation: Document PAYG as available to any user without a full Copilot license (including F1/F3), managed through MAC > Cost Management.

---

## Sources

### Primary (HIGH confidence — official Microsoft documentation verified February 2026)

- Microsoft Learn: Purview AI Microsoft — `https://learn.microsoft.com/en-us/purview/ai-microsoft-purview` — DSPM unified experience, AI observability, Purview Posture Agent
- Microsoft Learn: Considerations for Copilot and Channel Agent — `https://learn.microsoft.com/en-us/purview/ai-m365-copilot-considerations` — Channel Agent IB limitation (documented explicitly)
- Microsoft Learn: DSPM Permissions — `https://learn.microsoft.com/en-us/purview/ai-microsoft-purview-permissions` — New RBAC roles (AI Viewer, AI Content Viewer, AI Administrator)
- Microsoft Learn: DLP for Copilot — `https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about` — Two DLP policy types, default policy
- Microsoft Learn: CA for Generative AI — `https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-copilot-ai-security` — Enterprise Copilot Platform app ID `fb8d773d-7ef8-4ec0-a117-179f88add510`
- Microsoft Learn: Sensitivity Labels — `https://learn.microsoft.com/en-us/purview/sensitivity-labels` — Label groups replacing parent labels
- Microsoft Learn: Migrate Sensitivity Label Scheme — `https://learn.microsoft.com/en-us/purview/migrate-sensitivity-label-scheme` — Migration timeline and process
- Microsoft Learn: SharePoint Advanced Management Licensing — `https://learn.microsoft.com/en-us/sharepoint/sharepoint-advanced-management-licensing` — SAM included with Copilot licenses
- Microsoft Learn: Restricted Content Discovery — `https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery` — RCD as complementary to RSS
- Microsoft Learn: Restricted Access Control — `https://learn.microsoft.com/en-us/sharepoint/restricted-access-control` — RAC for oversharing remediation
- Microsoft Learn: IRM Adaptive Protection — `https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection` — IRM-integrated dynamic CA blocking
- Microsoft Learn: Defender for Cloud Apps Release Notes — `https://learn.microsoft.com/en-us/defender-cloud-apps/release-notes` — Agent protection Sep 2025
- Microsoft Learn: Purview What's New — `https://learn.microsoft.com/en-us/purview/whats-new` — All Purview feature dates
- PnP PowerShell: Changes in Registration — `https://pnp.github.io/blog/post/changes-pnp-management-shell-registration/` — Multi-tenant app deletion Sep 9, 2024
- PnP PowerShell: Register Application — `https://pnp.github.io/powershell/articles/registerapplication.html` — Custom app registration requirement
- Microsoft Entra Blog: CA Enforcement Change — `https://techcommunity.microsoft.com/blog/microsoft-entra-blog/upcoming-conditional-access-change-improved-enforcement-for-policies-with-resour/4488925` — March 27, 2026 enforcement date

### Secondary (MEDIUM confidence — cross-verified with official sources)

- FINRA: 2026 Annual Regulatory Oversight Report, GenAI Section — `https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai` — First standalone agentic AI guidance
- SEC: 2026 Division of Examinations Priorities — `https://corpgov.law.harvard.edu/2026/01/04/2026-sec-division-of-examinations-priorities/` — Internal AI automation scrutiny
- Microsoft Tech Community: Ignite 2025 Copilot Control System — `https://techcommunity.microsoft.com/blog/microsoft365copilotblog/ignite-2025-copilot-control-system-and-related-updates-for-it-and-security-teams/4469768` — AI app catalog, agent management
- Microsoft Tech Community: New Purview Capabilities for GenAI Agents — `https://techcommunity.microsoft.com/blog/microsoft-security-blog/announcing-new-microsoft-purview-capabilities-to-protect-genai-agents/4470696` — Edge DLP, IRM agents
- Message Center MC1111778 (via mc.merill.net) — Sensitivity label groups replacing parent labels, GA timeline
- Message Center MC1200579 (via mc.merill.net) — Risky Agents auto-deployment, December 2025
- Message Center MC1182689 (via mc.merill.net) — Default DLP policy for Copilot, MAC security controls
- Office365ITPros: SAM included with Copilot — `https://office365itpros.com/2025/05/06/sharepoint-advanced-management-2/` — Cross-verification of licensing change
- Office365ITPros: New DLP for Copilot Prompts — `https://office365itpros.com/2025/11/20/dlp-policy-for-copilot-prompts/` — SIT-based prompt blocking explanation
- Governance Architecture Report (repo root): "Microsoft 365 Copilot Governance Archite.md" — Comprehensive verification, Feb 17, 2026

### Tertiary (LOW confidence — single source or unverified claims)

- The "AI usage indicator" as a named IRM category: referenced in research materials but not confirmed as the exact label Microsoft uses in the IRM console. Verify against actual IRM policy indicator settings before using this terminology in 2.10.
- Specific Frontline SKU Copilot feature constraints: the research confirms F1/F3 can add Copilot as an add-on, but feature parity vs. E3/E5 Copilot users is not fully documented. Do not assert feature parity without verification.

---

## Metadata

**Confidence breakdown:**
- P1-01 (Optimization Assessment, update channel): HIGH — documented in Microsoft Learn adoption guide and readiness docs
- P1-02 (DSPM unified experience): HIGH — multiple official Microsoft sources, Purview What's New
- P1-03 (RCD + RSS comparison, SAM licensing): HIGH — both confirmed from official SharePoint docs
- P1-04 (New RBAC roles): HIGH — DSPM permissions page explicitly lists all three roles
- P1-05 (SAM licensing correction, DAG + RAC): HIGH — SAM licensing confirmed from multiple official sources including Microsoft Learn licensing page
- P1-06 (Frontline SKUs, PAYG): MEDIUM-HIGH — F1/F3 add-on confirmed; PAYG mechanics confirmed; specific F1 feature constraints need verification
- P2-01 (Dual DLP types, default policy, Edge DLP): HIGH — official Purview DLP docs, MC messages confirmed
- P2-02 (Label groups, agent inheritance, nested auto-labeling): HIGH — MC1111778 and Purview What's New confirm all three
- P2-03 (CA enforcement, app ID, IRM dynamic blocking): HIGH — app ID verified, CA date confirmed from Entra blog post
- P2-04 (Channel Agent IB limitation): HIGH — explicitly documented in Microsoft Learn considerations page
- P2-05 (AI app catalog count, agent XDR detection): HIGH for XDR detection; MEDIUM for catalog count (1,000+ confirmed but "400+" in spec is stale)
- P2-06 (Risky Agents, data risk graphs, IRM Triage Agent): HIGH for all four GA items (Dec 2025); MEDIUM for AI usage indicator terminology
- PLAY-01 (PnP custom app registration): HIGH — PnP blog post and official docs confirm Sep 2024 change
- PLAY-03 (Portal path updates): HIGH — MAC portal consolidation confirmed from multiple official sources

**Research date:** 2026-02-17
**Valid until:** 2026-05-17 (90 days — Microsoft 365 platform changes frequently; portal paths and feature status should be re-verified before phase execution if delayed)
