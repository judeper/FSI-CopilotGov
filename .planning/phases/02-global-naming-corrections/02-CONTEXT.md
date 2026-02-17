# Phase 2: Global Naming Corrections - Context

**Gathered:** 2026-02-17
**Status:** Ready for planning

<domain>
## Phase Boundary

Replace all deprecated Microsoft product names across the entire 314-file documentation site with current, correct terminology. The primary targets are "BizChat", "M365 Chat", and "Microsoft 365 Chat", but the scope extends to a full terminology audit of all outdated Microsoft product names. This phase produces a clean naming baseline that all subsequent phases build upon.

</domain>

<decisions>
## Implementation Decisions

### Dual-name mapping (CRITICAL)
- **"Microsoft 365 Copilot Chat"** = the free/seeded version (included with any M365 subscription, web-grounded only, no Copilot license required). This is what "BizChat" most commonly referred to.
- **"Microsoft 365 Copilot"** = the licensed version (requires per-user Copilot license, grounded in web + work data via Microsoft Graph).
- Every "BizChat" instance must be categorized by which product it actually describes before replacement. This is NOT a simple find-replace.
- The researcher must audit all ~119 BizChat instances and categorize each one before any replacement begins.

### Shortened form policy
- First mention in each document: Use full name ("Microsoft 365 Copilot Chat" or "Microsoft 365 Copilot")
- Subsequent mentions in same document: "Copilot Chat" for the free/seeded product
- Headings (all levels): Always use full product name, never shortened form
- Compound phrases (e.g., "BizChat-specific", "BizChat/Teams"): Claude uses judgment to pick the most natural phrasing per occurrence

### Historical context and exceptions
- **No exceptions.** Replace old names everywhere — zero preservation of "BizChat", "M365 Chat", or "Microsoft 365 Chat" in any context.
- MC post references: Update the name in reference text; keep the MC post number/link intact for traceability.
- Frontmatter, YAML metadata, structured data tables: Same replacement policy as body text — no content type gets special treatment.

### Terminology scope
- Full terminology audit, not limited to BizChat family.
- **Microsoft Learn is the canonical authority** for all product names. Whatever Learn calls it, we call it.
- Researcher should identify ALL outdated Microsoft product/feature names across the docs (admin portals, feature names, service names, deprecated terms).
- Correct everything discovered in Phase 2 regardless of volume — no deferral of terminology fixes.

### Transition approach
- **Silent replacement** — no "formerly known as" notes, no inline parentheticals, no changelog entries about the rename. Docs should read as if current names were always used.
- Update nav entries, page titles, mkdocs.yml, breadcrumbs — everything that contains old names.

### Verification
- MkDocs build must pass without new broken reference warnings
- Grep verification confirms zero remaining instances of old terms
- No separate change report needed — git history provides the audit trail

### Git commit style
- Commit messages SHOULD reference old names being replaced (e.g., "fix(naming): replace BizChat with Microsoft 365 Copilot Chat across pillar 1") for traceability in git history

### Success criteria update needed
- Current ROADMAP.md success criteria assume a single canonical replacement ("Microsoft 365 Copilot Chat"). Criteria must be revised to reflect the dual-name mapping: some instances become "Microsoft 365 Copilot Chat" (free) and others become "Microsoft 365 Copilot" (licensed).

</decisions>

<specifics>
## Specific Ideas

- Microsoft's own naming distinction (confirmed via Microsoft Learn, Feb 2026): "Microsoft 365 Copilot Chat" is the free/seeded experience, "Microsoft 365 Copilot" is the licensed experience. Source: https://learn.microsoft.com/en-us/copilot/overview
- The 4 research reports provided for Review 01 document many of the renames but Microsoft Learn should be treated as the primary authority for current names.
- ~119 instances of "BizChat" across ~61 files, plus ~55 instances of partial new names already in use — the researcher needs to reconcile both old and inconsistent new references.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 02-global-naming-corrections*
*Context gathered: 2026-02-17*
