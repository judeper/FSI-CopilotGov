---
phase: 02-global-naming-corrections
plan: 04
subsystem: documentation
tags: [naming, terminology, purview, entra-id, microsoft-365, azure-ad, compliance-portal]

# Dependency graph
requires: []
provides:
  - Zero "Azure Active Directory" or "Azure AD" references in docs (replaced with Microsoft Entra ID)
  - Zero generic "Office 365" or "O365" references in docs (SKU names preserved)
  - Zero "compliance.microsoft.com" URLs in docs (replaced with purview.microsoft.com)
  - Zero "Microsoft Purview compliance portal" portal name references (replaced with "Microsoft Purview portal")
  - Zero "Microsoft 365 Defender" references (replaced with "Microsoft Defender XDR")
  - portal-paths-quick-reference.md fully migrated to purview.microsoft.com with ~30 purview URLs
affects: [all phases, phase-3-pillar-content, phase-4-pillar-content]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Microsoft Entra ID is the canonical name for the identity platform (not Azure AD)"
    - "Microsoft Purview portal at purview.microsoft.com is the current portal (not compliance.microsoft.com)"
    - "Microsoft Defender XDR is the current name (not Microsoft 365 Defender)"
    - "Office 365 E3/E5/E1 SKU names are preserved; generic Office 365 platform references replaced with Microsoft 365"

key-files:
  created: []
  modified:
    - docs/reference/portal-paths-quick-reference.md
    - docs/reference/glossary.md
    - docs/framework/governance-fundamentals.md
    - docs/getting-started/quick-start.md
    - docs/controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md
    - docs/controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md
    - docs/controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md
    - docs/controls/pillar-2-security/2.3-conditional-access-policies.md
    - docs/controls/pillar-3-compliance/3.1-copilot-audit-logging.md
    - docs/controls/pillar-3-compliance/3.2-data-retention-policies.md
    - docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md
    - docs/controls/pillar-3-compliance/3.4-communication-compliance.md
    - docs/controls/pillar-3-compliance/3.5-finra-2210-compliance.md
    - docs/controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md
    - docs/controls/pillar-4-operations/4.11-sentinel-integration.md
    - docs/playbooks/control-implementations/2.3/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.9/portal-walkthrough.md
    - docs/playbooks/control-implementations/2.9/troubleshooting.md
    - docs/playbooks/control-implementations/3.6/troubleshooting.md
    - docs/playbooks/control-implementations/4.5/powershell-setup.md
    - docs/playbooks/control-implementations/4.5/verification-testing.md
    - docs/playbooks/control-implementations/4.8/troubleshooting.md
    - docs/reference/microsoft-learn-urls.md
    - "13 x docs/playbooks/control-implementations/3.*/portal-walkthrough.md"

key-decisions:
  - "Office 365 SKU names (E1/E3/E5) preserved as valid Microsoft product names; generic platform references replaced"
  - "PowerShell code literals (appDisplayName eq 'Office 365' filter value, regex pattern) preserved as technical API values"
  - "Glossary removed '(formerly Azure Active Directory / Azure AD)' parenthetical to meet must-have zero-instance requirement"
  - "Office 365 Management Activity API name preserved (still valid product name with canonical MS Learn URL)"
  - "Microsoft Entra ID replaces Azure AD in all prose; Entra ID used as shortened form in subsequent mentions"

patterns-established:
  - "Entra ID: use 'Microsoft Entra ID' on first mention, 'Entra ID' thereafter"
  - "Purview portal: always 'Microsoft Purview portal' at purview.microsoft.com"
  - "Defender: use 'Microsoft Defender XDR' (not Microsoft 365 Defender)"

requirements-completed: [GLOB-01, GLOB-02]

# Metrics
duration: 12min
completed: 2026-02-17
---

# Phase 2 Plan 4: Full Terminology Audit (Azure AD, Office 365, Purview Portal) Summary

**Replaced all remaining outdated Microsoft product terminology: Azure AD to Entra ID, Office 365 to Microsoft 365 (preserving SKUs), compliance.microsoft.com to purview.microsoft.com, and Microsoft Purview compliance portal to Microsoft Purview portal across 40+ docs files**

## Performance

- **Duration:** 12 min
- **Started:** 2026-02-17T21:41:10Z
- **Completed:** 2026-02-17T21:53:36Z
- **Tasks:** 2
- **Files modified:** 40

## Accomplishments

- All Azure AD/Azure Active Directory references replaced with Microsoft Entra ID (6 instances across 5 files, including one extra file found via grep outside plan's list)
- All Office 365/O365 generic platform references replaced with Microsoft 365 (10+ instances), Office 365 E3/E5 SKU names preserved
- Microsoft 365 Defender renamed to Microsoft Defender XDR (1 instance in 4.11)
- portal-paths-quick-reference.md fully migrated: section renamed to "Microsoft Purview Portal", all 28 compliance.microsoft.com URLs replaced with purview.microsoft.com
- All "Microsoft Purview compliance portal" portal name references updated to "Microsoft Purview portal" (across 13 playbook files, 6 control files, quick-start, and governance-fundamentals)

## Task Commits

Each task was committed atomically:

1. **Task 1: Replace Azure AD with Microsoft Entra ID and Office 365 with Microsoft 365** - `b4588d0` (fix) - Note: Task 1 changes were committed by the previous plan execution agent in its metadata commit. All changes verified at HEAD.
2. **Task 2: Update Purview portal name and compliance.microsoft.com URLs** - `2b74e1d` (fix)

## Files Created/Modified

**Task 1 (Azure AD / Office 365 / Defender XDR corrections):**
- `docs/reference/glossary.md` - Removed "formerly Azure Active Directory / Azure AD" parenthetical
- `docs/playbooks/control-implementations/4.5/verification-testing.md` - "Azure AD department attributes" -> "Entra ID"
- `docs/playbooks/control-implementations/4.5/powershell-setup.md` - "Azure AD" comment -> "Entra ID" (auto-fix: file not in plan list but had Azure AD reference)
- `docs/playbooks/control-implementations/4.8/troubleshooting.md` - 2x "Azure AD" -> "Entra ID"
- `docs/playbooks/control-implementations/3.6/troubleshooting.md` - "Azure AD dynamic groups" -> "Entra ID"
- `docs/controls/pillar-4-operations/4.11-sentinel-integration.md` - "Microsoft 365 (Office 365)" -> "Microsoft 365", "Microsoft 365 Defender" -> "Microsoft Defender XDR", 3 instances updated
- `docs/controls/pillar-2-security/2.3-conditional-access-policies.md` - 6x "Via Office 365 app targeting" -> "Via Microsoft 365", "Microsoft 365 Copilot, Office 365" -> "Microsoft 365"
- `docs/playbooks/control-implementations/2.3/portal-walkthrough.md` - "Office 365" target resources -> "Microsoft 365"
- `docs/playbooks/control-implementations/2.9/portal-walkthrough.md` - 3x "Office 365" -> "Microsoft 365"
- `docs/playbooks/control-implementations/2.9/troubleshooting.md` - 2x "Office 365" -> "Microsoft 365"
- `docs/reference/microsoft-learn-urls.md` - "Connect Office 365 data" -> "Connect Microsoft 365 data"
- `docs/reference/portal-paths-quick-reference.md` - "Office 365 connector" -> "Microsoft 365 connector"
- `docs/framework/governance-fundamentals.md` - "Microsoft Purview compliance portal" -> "Microsoft Purview portal" (in portal table)

**Task 2 (Purview portal name and URL migration):**
- `docs/reference/portal-paths-quick-reference.md` - Section renamed, base URL removed, 28 compliance.microsoft.com -> purview.microsoft.com
- `docs/getting-started/quick-start.md` - Portal link updated
- `docs/controls/pillar-1-readiness/1.1-copilot-readiness-assessment.md` - 2 portal name instances
- `docs/controls/pillar-1-readiness/1.2-sharepoint-oversharing-detection.md` - 2 portal name instances
- `docs/controls/pillar-1-readiness/1.5-sensitivity-label-taxonomy-review.md` - 1 portal name instance
- `docs/controls/pillar-3-compliance/3.1-copilot-audit-logging.md` - Portal name + URL
- `docs/controls/pillar-3-compliance/3.2-data-retention-policies.md` - Portal name + URL
- `docs/controls/pillar-3-compliance/3.3-ediscovery-copilot-content.md` - Portal name + URL
- `docs/controls/pillar-3-compliance/3.4-communication-compliance.md` - Portal name + URL
- `docs/controls/pillar-3-compliance/3.5-finra-2210-compliance.md` - Portal name + URL
- `docs/controls/pillar-3-compliance/3.10-sec-reg-sp-privacy.md` - Portal name + URL
- `docs/playbooks/control-implementations/3.1-3.13/portal-walkthrough.md` (13 files) - Access field portal name

## Decisions Made

- Office 365 E3/E5 SKU names preserved as valid Microsoft product names (still actively sold and distinct from Microsoft 365 E3/E5)
- PowerShell code literals referencing "Office 365" as an API filter/regex value preserved (these are technical values that must match actual API responses)
- Glossary parenthetical "(formerly Azure Active Directory / Azure AD)" removed to meet zero-instance must-have; the glossary entry heading "Microsoft Entra ID" is self-explanatory
- "Office 365 Management Activity API" preserved as the actual Microsoft product/API name
- "Microsoft 365 (Office 365)" in the Conditional Access app target table preserved as it is the actual app name shown in the Entra portal UI

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing Coverage] Fixed Azure AD reference in 4.5/powershell-setup.md**
- **Found during:** Task 1 (grep verification)
- **Issue:** File `docs/playbooks/control-implementations/4.5/powershell-setup.md` had "Azure AD" comment but was not in the plan's file list for Task 1
- **Fix:** Updated comment "Enrich with department data from Azure AD" to "Enrich with department data from Entra ID"
- **Files modified:** docs/playbooks/control-implementations/4.5/powershell-setup.md
- **Verification:** grep for Azure AD returned zero results
- **Committed in:** b4588d0 (Task 1 commit)

---

**Total deviations:** 1 auto-fixed (Rule 2 - missing coverage in plan's file list)
**Impact on plan:** Auto-fix required to meet must-have "zero instances" criterion. No scope creep.

## Issues Encountered

- Task 1 changes were already committed to HEAD (in commit b4588d0) by the previous plan's (02-01) metadata commit, which erroneously included Plan 04 file changes. All Task 1 changes are confirmed at HEAD and verified against must-have criteria. A formal Task 1 commit was not created separately since the changes were already committed.

## Next Phase Readiness

- Full terminology baseline is clean: zero Azure AD, zero Office 365 (platform), zero compliance.microsoft.com, zero "Microsoft Purview compliance portal" across all docs
- Plans 02-01 through 02-04 complete — Phase 2 global naming corrections done
- Phase 3 (Pillar content updates) can proceed with confidence in clean naming foundation

---
*Phase: 02-global-naming-corrections*
*Completed: 2026-02-17*
