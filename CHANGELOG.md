# Changelog

All notable changes to the FSI Copilot Governance Framework are documented in this file.

---

## [1.7.1] - 2026-04-30

Post-release CI hardening and dependency refresh. No content or framework changes.

### Fixed

- **Bandit B701 (Jinja `autoescape=False`)** on `assessment/engine/report.py`:
  the two `Environment(...)` instances now set `autoescape=False` explicitly with
  a `# nosec B701` justification — the templates render Markdown (not HTML) and
  consume only repo-owned manifest data, so HTML escaping is intentionally off.
  Resolves the only finding from the new `Security Scan` workflow shipped in
  1.7.0.
- **Manifest Fence on Dependabot PRs**: the `Check solutions-lock is up to date`
  step in `.github/workflows/manifest-fence.yml` now skips when the actor is
  `dependabot[bot]`. The step calls `generate_solutions_lock.py --check`, which
  needs read access to the sister repo; Dependabot's token does not have that
  scope. Solutions-lock drift continues to be enforced on every other PR and on
  the daily schedule by the dedicated `Solutions Drift` workflow.

### Dependencies

- **GitHub Actions** (gha group, major bumps): `actions/checkout` v4 → v6,
  `github/codeql-action` v3 → v4, `actions/upload-artifact` v4 → v7,
  `peter-evans/create-pull-request` v6 → v8, `actions/setup-node` v4 → v6,
  `actions/setup-python` v5 → v6, `actions/cache` v4 → v5,
  `peter-evans/create-issue-from-file` v5 → v6. Smoke-tested via manual
  `workflow_dispatch` of `learn-url-monitor`, `regulatory-monitoring`, and
  `solutions-drift` after merge — all green.
- **Python tooling** (7 bumps) and **python-scripts** runtime deps (4 bumps).
- **JS dev tooling** (3 bumps): vitest + jsdom group.
- **Monitor baselines refreshed** for 2026-04-29 and 2026-04-30 (Federal
  Register + FINRA + Microsoft Learn URL hashes). All findings classified as
  NOISE — no governance-impacting changes detected.

---

## [1.7.0] - 2026-04-29

Response to the external repository critique. This release lands credibility
fixes (count drift, AgentGov heritage cleanup, scope-boundary visibility),
enterprise-grade repo hardening (CodeQL, Dependabot, security scan,
PSScriptAnalyzer, SBOM, expanded SECURITY.md), and a deeper engine/SPA test
suite.

### Phase A — Credibility fixes

- **Authored 5 missing playbook sets** (controls **1.16, 2.16, 2.17, 3.14,
  4.14**) — 4 files each (`portal-walkthrough`, `powershell-setup`,
  `verification-testing`, `troubleshooting`) plus nav wiring in
  `mkdocs.yml`. Playbook total moves from 243 → **263** (245 control
  implementations + 18 cross-cutting).
- **New count drift detector** (`scripts/verify_count_consistency.py`) +
  smoke test (`scripts/test_verify_count_consistency.py`). Wired into
  `publish_docs.yml`. Catches hand-typed control / playbook / solution /
  pillar numbers that disagree with `content-graph.json`.
- **Macro adoption** — replaced ~55 hard-coded count occurrences across
  `README.md`, `docs/index.md`, `docs/controls/index.md`,
  `docs/assessment/index.md`, `docs/getting-started/checklist.md`,
  `docs/getting-started/quick-start.md`, every `docs/framework/*.md` page,
  `docs/playbooks/index.md`, `docs/playbooks/control-implementations/index.md`,
  and `docs/reference/faq.md` with `{{ counts.controls }}`,
  `{{ counts.playbooks_total }}`, etc. Per-pillar literal counts updated
  to **16 / 17 / 15 / 14 = 62**.
- **SPA + extractor de-numerified** — `docs/javascripts/assessment-app.js`
  and `scripts/extract_assessment_data.py` no longer carry hand-typed
  control counts.
- **`.github/copilot-instructions.md`** brought into alignment with
  `AGENTS.md` (62 controls, 263 playbooks).

### Phase B — AgentGov heritage cleanup

- **Engine self-identification** renamed in `assessment/engine/score.py`,
  `assessment/engine/report.py`, the `PREFILLED_TEMPLATE` /
  `QUESTIONNAIRE_TEMPLATE` titles, all argparse descriptions, and the
  Python loggers (`fsi-copilotgov-score`, `fsi-copilotgov-report`).
- **Quarantined `COPILOT_STUDIO_APP_ID`** behind
  `LEGACY_AGENTGOV_COPILOT_STUDIO_APP_ID` with an explanatory comment
  block; back-compat alias retained so external callers don't break.
- **Collector PowerShell headers** — all four `Collect-*.ps1` `.SYNOPSIS` /
  `.NOTES` blocks rewritten to "FSI-CopilotGov" with a single-line lineage
  parenthetical.
- **`assessment/README.md` heritage callout** explaining the v1.4 port
  lineage so the rename is auditable rather than silent.

### Phase C — Scope-boundary visibility

- **Reusable `{{ agentgov_boundary() }}` macro** registered via
  `scripts/macros_module.py`. Renders an inline "Scope boundary:
  FSI-CopilotGov vs FSI-AgentGov" callout pointing readers to the
  companion framework for agent-level governance.
- **Boundary callout injected** at the top of every control that brushes
  against Copilot Studio / declarative agents / Agent 365 surfaces:
  **1.13, 2.13, 2.14, 2.16, 2.17, 4.1, 4.13**.
- **"What This Framework Does *Not* Cover"** section added to both
  `docs/framework/governance-fundamentals.md` and the homepage
  (`docs/index.md`), enumerating Copilot Studio, Power Platform ALM,
  Power Platform DLP, identity/CA design, RIM/supervisory authoring, and
  production runtime as out-of-scope domains.

### Phase D — Repo hardening

- **`.github/CODEOWNERS`** mapping controls, playbooks, framework prose,
  assessment code, scripts, workflows, and security-sensitive paths to the
  repository owner.
- **`.github/dependabot.yml`** — weekly Monday updates for `pip` (root +
  `scripts/`), `npm`, and `github-actions`. Grouped to bound PR noise.
- **`.github/workflows/codeql.yml`** — Python + JavaScript SAST on every
  push/PR and weekly Tuesday at 09:00 UTC, with the
  `security-and-quality` query suite.
- **`.github/workflows/security-scan.yml`** running `pip-audit`, `bandit`
  (medium severity gate), `npm audit` (high severity gate), and
  `Invoke-ScriptAnalyzer` against `assessment/collectors/`. Weekly Monday
  at 10:00 UTC + on push/PR.
- **SBOM generation** added to `publish_docs.yml` via
  `anchore/sbom-action@v0` (SPDX-JSON), attached to the GitHub Pages
  deploy artifact at `site/fsi-copilotgov-sbom.spdx.json`.
- **`SECURITY.md` expanded** with a Supported Versions table, GitHub
  Private Vulnerability Reporting workflow, response targets
  (acknowledge / triage / fix / disclosure), explicit scope and
  out-of-scope sections, and a hardening-posture summary.

### Phase E — Test depth

- **`assessment/tests/test_engine_fixtures.py`** — deterministic scoring
  fixtures (passing / failing / mixed synthetic tenants) pinning
  evaluator semantics for `audit_log_enabled`,
  `copilot_retention_policy_exists`, `grounding_sources_approved`,
  and `no_external_sharing_on_grounding`. Plus manifest-vs-docs
  invariants (every control has a doc page and a playbook directory; no
  orphaned playbook directories) — handles the `3.8a` sub-control
  parent-directory fallback.
- **`tests/spa/count-snapshot.test.mjs`** — pins the manifest /
  content-graph / SPA-data triple in lockstep so any single regeneration
  drift fails CI.
- **`scripts/test_content_graph_smoke.py`** expected counts updated
  (`playbooks_total` 243 → 263, `playbooks_control` 225 → 245).

### Validation

Full local gate sweep passes:

| Check | Result |
|---|---|
| `verify_controls.py` | 62 controls, 0 errors |
| `verify_language_rules.py` | 360 files, 0 violations |
| `validate_manifest.py --strict --allow-todo` | green |
| `verify_count_consistency.py` | 414 files scanned, no drift |
| `mkdocs build --strict` | green |
| `pytest assessment/tests scripts -q` | **47 passed** |
| `vitest run` | **84 passed** (12 test files) |

### Out of scope (handled in `FSI-CopilotGov-Solutions`)

Power Platform ALM templates, `deploymentSettings.template.json`,
environment-variable schemas, connection-reference templates, agent
registry / model-card / Responsible AI / model-risk evidence schemas,
per-solution managed-deployment runbooks, `pac cli` guidance, and the
DORA ICT third-party register template. These are tracked separately in
the companion repo.

---

## [1.6.2] - 2026-04-28

### Changed

- **Monitoring cadence: weekly → daily.** `.github/workflows/learn-url-monitor.yml` and `.github/workflows/regulatory-monitoring.yml` now run daily at 10:00 UTC (previously Tue / Wed weekly). Daily detection of upstream Microsoft Learn or regulatory drift, with PR creation rate-limited by the underlying scripts' no-op-on-no-change behaviour.
- **`AGENTS.md`** and **`.github/copilot-instructions.md`** workflow inventory updated to reflect the daily cadence.
- **`README.md`** monitoring-workflows bullet specifies "scheduled daily CI (10:00 UTC)".

### Fixed

- **PR creation by GitHub Actions was blocked by repo policy** (`Settings → Actions → General → Workflow permissions → "Allow GitHub Actions to create and approve pull requests"` was OFF). Both monitor workflows had been detecting changes and pushing branches but failing at the PR-create step (`##[error]GitHub Actions is not permitted to create or approve pull requests`) for several runs (Learn ~7h before fix, Regulatory ~6 days before fix). Setting flipped via `gh api PUT /repos/.../actions/permissions/workflow`. End-to-end verified by manual `workflow_dispatch` of both monitors immediately after the fix.

### Operational

- Cleared two stale `monitoring/*` branches that had accumulated while PR-create was blocked. Preserved the genuine `reports/monitoring/regulatory-changes-2026-04-22.md` findings report from the older stale branch (cherry-picked into the same commit as the cadence change).
- Merged the first successful daily PRs as baseline updates: **PR #5** (Learn — 1012-line baseline initialization of Microsoft Learn URL content hashes) and **PR #6** (Regulatory — 101 items: 0 CRITICAL, 0 HIGH, 3 MEDIUM, 98 NOISE; no controls action required, the SEC Consolidated Audit Trail concept release is at the earliest stage of rulemaking).
- Ran `git fetch --prune` and `git gc --prune=now --aggressive` to clear stale remote-tracking refs and 39 dangling objects.

---

## [1.6.1] - 2026-04-22

### Fixed

Post-tag follow-ups required for v1.6.0 to be functionally complete in the engine and SPA layers (initial v1.6.0 tag at `6a18fbe` only covered the docs/manifest layer; engine + SPA wiring landed afterward on `main`).

- **Engine manifest** (`assessment/manifest/generate_manifest.py`) — added 4 new control entries (3.8a, 2.17, 3.14, 4.14) to the engine-facing CONTROLS list. Without this, the assessment engine and SPA manifest-loader stayed at 58 controls.
- **Solutions drift coverage** (`assessment/manifest/authored_content.py`) — added `_SOLUTIONS_BY_CONTROL` entries mapping 2.17→Sol21, 3.8a→Sol20, 3.14→Sol22, 4.14→Sol23. Without this, `check_solutions_drift` reported 4 COVERAGE_ORPHANs.
- **Assessment SPA control parsing** (`scripts/extract_assessment_data.py`) — refactored to discover control files from disk (instead of integer ranges) and loosened H1 regex to `\d+\.\d+[a-z]?` so `3.8a` is parsed correctly.
- **SPA literal counts** (`docs/javascripts/assessment-app.js`) — two `"of 58"` strings updated to `"of 62"` in the solutions catalog badge.
- **Validation tooling** — `scripts/validate_manifest.py`, `scripts/validate_content_graph.py`, `scripts/test_content_graph_smoke.py`, `assessment/tests/test_engine_smoke.py`, `assessment/tests/test_solutions_lock.py`, and 7 SPA tests bumped hardcoded counts (58→62, 19→23) and per-pillar distribution (16/16/13/13 → 16/17/15/14); regex `^[1-4]\.\d+$` → `^[1-4]\.\d+[a-z]?$` to accept alpha-suffixed IDs.
- **XLSX templates** (`assessment/templates/*.xlsx`) — regenerated for 62 controls; `verify_excel_templates.py` patched to recognize `3.8a`-style IDs.
- **Link checker** (`mlc-config.json`) — extended ignore list for `learn.microsoft.com` paths used in the new control files plus `sr1107.htm` (case-sensitive 404 from CI runners).
- **Cross-reference link fixes** — Control 2.17 now points to `pillar-1-readiness/1.10-vendor-risk-management.md` (was non-existent `pillar-1-foundation/1.10-agent-authoring-governance.md`); Control 3.14 now points to actual filenames for 3.2 and 3.11 cross-refs.

---

## [1.6.0] - 2026-04-22

### Added
- **Control 3.8a: Generative AI Model Governance** — extends Control 3.8 (Model Risk Management) with explicit generative AI governance addressing the SR 26-2 / OCC Bulletin 2026-13 generative AI exclusion. Synthesizes SR 11-7, NIST AI RMF 1.0, and ISO/IEC 42001.
- **Control 2.17: Cross-Tenant Agent Federation** — governs cross-tenant Entra Agent ID trust, MCP federated server attestation, and Copilot Studio multi-tenant publishing. Extends Control 2.16 to multi-tenant scenarios.
- **Control 3.14: Copilot Pages and Notebooks Retention and Provenance** — governs branch-aware Pages retention, Notebook section-level coverage, and Loop component provenance. Extends Control 3.2 (data retention) for these mutable artifact types.
- **Control 4.14: Copilot Studio Agent Lifecycle** — governs authoring → testing → publishing → versioning → deprecation evidence for Copilot Studio agents. Distinguished from Control 1.10 (initial approval gate), 1.16 (tuning), and 4.13 (extensibility).
- Cross-reference notes added to Controls 3.8, 3.2, 2.16, 4.13 pointing readers to the new controls.

### Changed
- Framework grew from 58 to **62 controls**. README.md, AGENTS.md, and content-graph regenerated to reflect new counts.
- `assessment/manifest/content-graph.schema.json` — `controls[].id` regex extended to allow lowercase suffix (e.g., `3.8a`).
- Sister Solutions repo repinned from v0.6.0 → **v0.7.0** (adds Solutions 20-23 covering the new controls).

---

## v1.5.2 — 2026-04-22

### Added — Phase X (CG side) + Phase Y + Phase U.C.2

- **Phase X — Sister-graph repin.** `scripts/generate_solutions_lock.py` now pins to `FSI-CopilotGov-Solutions@v0.6.0` (was v0.5.1). The sister release introduces a canonical `solutions-graph.json` with per-solution `controlCoverage`, framework-control union, tier counts, and doc-file counts — laying the groundwork for cross-repo content-graph coupling.
- **Phase Y — Playbook classifier macros.** `scripts/macros_module.py` now exposes two derived Jinja variables:
    - `playbooks_by_category` — counts per content category (`control-implementations`, `compliance-and-audit`, `governance-operations`, `incident-and-risk`, `regulatory-modules`, `getting-started`, `overview`).
    - `playbooks_by_pillar` — counts of control-implementation playbooks per pillar (`pillar-1`..`pillar-4`).

  Templates can render category/pillar breakdowns without re-deriving classification. Backed by a new smoke test in `scripts/test_macros_smoke.py`.

### Changed — Phase U.C.2 MRM citation sweep

- Heading-only sweep across files that referenced **SR 11-7 / OCC Bulletin 2011-12** as the primary MRM authority. They now lead with **SR 26-2 / OCC Bulletin 2026-13** (April 2026) as the current interagency framework, with a one-line clarifier noting the genAI exclusion and that Copilot governance continues applying SR 11-7 / OCC Bulletin 2011-12 principles per Control 3.8. Body prose untouched (the SR 11-7 principles remain the operative framework for Copilot pending genAI-specific guidance):
    - `docs/reference/regulatory-mappings.md` — section heading.
    - `docs/reference/fsi-use-case-risk-scenarios.md` — three Regulatory references lines and the Investment Research model-risk row.
    - `docs/playbooks/regulatory-modules/state-ai-laws-compliance-matrix.md` — 3.8 link annotation.
    - `docs/playbooks/control-implementations/3.8/{portal-walkthrough,powershell-setup,verification-testing,troubleshooting}.md` — page titles.
    - `docs/controls/pillar-4-operations/4.13-extensibility-governance.md` — auditability/lineage callout MRM reference.

### Notes

- Doc + infrastructure release. No new controls or playbooks; framework counts unchanged at **58 controls / 243 playbooks / 4 pillars / 19 sister solutions**.
- `assessment/data/solutions-lock.json` regenerated against sister `v0.6.0` (commit `446d5d9`).

---

## v1.5.1 — 2026-04-22

### Added — Policy resolutions (Phase W; closes Issue #3 + U.C.1 DORA)
- **Control 3.8 — "Future direction" callout** — commits to a forward-looking control **3.8a (Generative AI Model Governance)** to be authored when **either** the Federal Reserve, OCC, or FDIC issues genAI-specific MRM guidance (filling the SR 26-2 / OCC 2026-13 exclusion), **or by 2027-Q1**, whichever comes first. Resolves Issue [#3](https://github.com/judeper/FSI-CopilotGov/issues/3) with the **hybrid roadmap** posture (Option C). Documents the watch list for SR letters and OCC bulletins (publication channels outside the Federal Register).
- **`docs/framework/regulatory-framework.md` — "Cross-jurisdictional solutions (DORA)" callout** — clarifies that the framework is scoped to **US financial services regulation** and that Solution 13 (DORA Operational Resilience Monitor) in the companion sister repository is provided as a courtesy for US-headquartered organizations with EU operations or for organizations operating directly in the EU. Resolves U.C.1 DORA scoping decision: status-quo + scope clarifier (rather than drop or expand framework scope to EU).

### Changed
- `assessment/data/solutions-lock.json` — repinned to sister `v0.5.1` (commit `3b528ea`) which carries the matching DORA scope clarifier in `solutions/13-dora-resilience-monitor/README.md`.
- `scripts/generate_solutions_lock.py` — `PINNED_REF` bumped to `v0.5.1`.

### Notes
- Both decisions are defensible to a regulatory examiner: the hybrid 3.8a roadmap demonstrates the framework is tracking the SR 26-2 / OCC 2026-13 supersession; the DORA clarifier confirms scope discipline.
- No new controls, playbooks, or solutions. Headline counts unchanged (58 controls, 243 playbooks, 19 solutions, 4 pillars).
- Issue [#3](https://github.com/judeper/FSI-CopilotGov/issues/3) closed with this release.

---

## v1.5.0 — 2026-04-22

### Added — Canonical Content Graph (Phase V; eliminates the headline-counts drift class)
- **`scripts/build_content_graph.py`** — walks `docs/controls/`, `docs/playbooks/`, and `assessment/data/solutions-lock.json` and emits `assessment/manifest/content-graph.json` as the single source of truth for framework metadata (control IDs, pillars, playbook paths and types, solution coverage, headline counts).
- **`assessment/manifest/content-graph.schema.json`** — JSON Schema (draft 2020-12) defining the canonical shape.
- **`scripts/validate_content_graph.py`** — schema + business-rules validator (control-id uniqueness, orphan-ref detection, count integrity, pillar bounds).
- **`scripts/verify_readme_counts.py`** — anchors hand-typed counts in `README.md` and `AGENTS.md` (which GitHub renders directly and cannot use mkdocs macros) to the content graph; CI fails on drift.
- **`scripts/test_content_graph_smoke.py`** and **`scripts/test_macros_smoke.py`** — pytest smoke coverage for the new infrastructure.
- **`mkdocs-macros-plugin`** dependency (root `requirements.txt`); configured in `mkdocs.yml`.
- **`scripts/macros_module.py`** — mkdocs-macros entry point; exposes `counts.controls`, `counts.playbooks_total`, `counts.playbooks_control`, `counts.playbooks_cross_cutting`, `counts.solutions`, `counts.pillars`, and the full `content_graph` namespace to all `docs/` markdown.
- **CI gates** — `Publish Docs` and `manifest-fence` workflows now build and validate the content graph and verify README/AGENTS counts before mkdocs build.
- **AGENTS.md `## Macros (since v1.5.0)`** — documents the macros convention; future contributors must use `{{ counts.* }}` in `docs/` rather than typing integers.

### Changed
- `docs/index.md` and `docs/start-here.md` — hand-typed counts (58, 243, 4) replaced with macro variables. Future control or playbook additions automatically propagate to the homepage hero, metric strip, architecture label, and orientation tables on the next build.

### Notes
- This release is doc/infrastructure only. No control or playbook content changed. No sister-repo coupling yet (planned for Phase X / sister `v0.6.0`).
- Phases W (eliminate `authored_content.py` Python override anti-pattern), X (sister-repo content-graph coupling), Y (automated playbook classifier), and Z (new control surfaces) are scoped in session plan files for follow-up releases.

---

## [Unreleased]

### Fixed
- **Drift correction:** `docs/index.md` now reports 243 playbooks (was 224). The framework actually publishes 225 control-implementation playbooks plus 18 cross-cutting playbooks (e.g., governance-operations, regulatory-modules) for a total of 243.
- **Citation remediation (regulator escalation):** Replaced rescinded/incorrect regulatory citations across multiple control and reference pages.
  - `controls/pillar-2-security/2.16-federated-connector-mcp-governance.md` — replaced 3 occurrences of rescinded **OCC Bulletin 2013-29** with current **OCC Bulletin 2023-17 (Third-Party Relationships: Risk Management)**.
  - `controls/pillar-4-operations/4.13-extensibility-governance.md` and `reference/fsi-use-case-risk-scenarios.md` and `playbooks/regulatory-modules/state-ai-laws-compliance-matrix.md` — corrected "OCC SR 11-7" attributions to the canonical paired citation **SR 11-7 / OCC Bulletin 2011-12** (SR 11-7 is a Federal Reserve issuance; OCC Bulletin 2011-12 is the OCC counterpart).
  - `playbooks/control-implementations/3.10/portal-walkthrough.md` and `verification-testing.md` — replaced "FTC Safeguards Rule" line items with the correct authority **GLBA §501(b)**. Reg S-P (SEC Rule 248.30) implements GLBA §501(b) for SEC-regulated broker-dealers; the FTC Safeguards Rule is a separate implementing regulation that applies only to FTC-jurisdiction institutions and is not the operative authority for SEC-regulated entities.
- **Dead URL:** `controls/pillar-3-compliance/3.8-model-risk-management.md` — replaced the dead Federal Reserve `sr1107.htm` URL with the live **SR 26-2** URL.

### Added
- **Regulatory update notice on Control 3.8 (Model Risk Management):** A prominent callout at the top of the control documents that on **April 17, 2026**, Federal Reserve / OCC / FDIC jointly issued **SR 26-2** and **OCC Bulletin 2026-13** (*Revised Guidance on Model Risk Management*), which supersede SR 11-7 / OCC Bulletin 2011-12. The revised interagency guidance **explicitly excludes generative and agentic AI models pending further regulatory consideration**. Because Microsoft 365 Copilot is a generative AI system, the operative MRM expectations for Copilot remain undefined under the revised framework; this control therefore continues to map to the SR 11-7 / OCC Bulletin 2011-12 principles as the most recent applicable guidance, supplemented by institution-specific policy. Organizations should monitor for forthcoming agency guidance on generative AI MRM.

### Notes
- Acknowledgement: the headline-counts drift (56/57/58 controls; 224/228/243 playbooks across README, AGENTS, and index pages) is a recurring class of issue caused by hand-typed metadata. A canonical content graph (Phase U.D.3-lite) is planned to render counts from a single source.
- A broader citation modernization sweep (replacing all SR 11-7 / OCC 2011-12 references with paired SR 26-2 / OCC 2026-13 citations) is **deferred** pending decision on whether to update the project's regulatory-citation canon (AGENTS.md). Tracked in session plan files.

---

## v1.4.0 — 2026-04-21

Major feature port from FSI-AgentGov bringing governance assessment parity for M365 Copilot.

### Added
- Manifest-driven assessment engine with Python scoring and YAML collectors (Phase B)
- Evidence drawer with verifyIn links and persistent notes (Phase D1)
- Facilitator mode with per-control ask/followUp prompts (Phase D1)
- Sector-calibration yes-bars per tier (Phase D1)
- Solution recommendation cards referencing FSI-CopilotGov-Solutions@v0.1.0-rc1 (Phase C2/D1)
- Collector evidence import (CSV/JSON drop) (Phase D2)
- Portal export envelope schema v0.1.0 (Phase E)
- Solutions catalog view with reverse-lookup and filters (Phase C3)
- Pre-session homework pages for 14 curated FSI roles (Phase F)
- Role-specific Excel checklists and governance dashboard (Phase G)
- Microsoft Learn URL monitoring (Phase I1)
- Regulatory monitoring (Federal Register + FINRA) (Phase I1)
- Solutions drift detection with weekly CI (Phase C4)
- Vitest harness with 60+ SPA tests across 11 files (Phase H1/H2)

### Changed
- Manifest validator accepts object-shaped solutions entries
- `merge_authored_content.py` now treats `solutions` as a replace-only field

### Reference
- [Phased rollout](docs/getting-started/phased-rollout.md)
- [Homework pages](docs/getting-started/homework-quickstart.md)

---

## v1.3.4 — 2026-04-17

### New Control, Playbooks, and Reference Content

- **2.16** Federated Copilot Connector and MCP Governance — new Baseline control for governing default-enabled federated connectors, user-credential authentication, data residency, and third-party risk (57 → 58 controls, Pillar 2: 15 → 16 controls)

#### New Playbooks
- **Agent Behavioral Incident Playbook** — incident response procedures for agent misuse, prompt injection, and runaway behavior
- **Teams Copilot Mode Governance** — governance playbook for Teams Copilot Mode group chat, covering FINRA 3110/4511, WSPs, retention, and communications compliance
- **State AI Laws Compliance Matrix** — regulatory module mapping Colorado, Texas, Utah, and Illinois AI laws to framework controls

#### New Reference Content
- **FSI Use Case Risk Scenarios** — risk matrix by use case (AML, client communications, research, financial reporting, meetings) with control mappings

#### Documentation Updates
- Updated control count from 57 to 58 across homepage, README, and AI instruction files
- Added Copilot surface coverage and playbook backlinks to multiple Pillar 2–4 controls
- Updated `docs/reference/copilot-surfaces-matrix.md` with new surface coverage entries

---

## v1.3.3 — 2026-04-15

### AI Council Deep Review — All 57 Controls

Comprehensive review of all 57 controls across 4 pillars using a multi-agent AI Council (GPT 5.4). Each control was reviewed for technical accuracy, regulatory accuracy, structural compliance, FSI language rules, and cross-reference integrity. Disagreements between council members were resolved through targeted research against authoritative sources.

**246 files changed, 458 insertions, 246 deletions across 12 commits.**

#### Critical Regulatory Corrections
- **1.1** Copilot Readiness Assessment — "Interagency AI Guidance (2023)" was misattributed; OCC Bulletin 2023-17 is about third-party risk management, not AI. Replaced with SR 11-7 / OCC Bulletin 2011-12 (model risk) and OCC Bulletin 2023-17 (third-party risk)
- **3.10** SEC Reg S-P Privacy — 72-hour breach notification direction was reversed; service providers must notify the firm, not the other way around
- **3.9** AI Disclosure & Transparency — SEC Marketing Rule was incorrectly described as prohibiting testimonials; it permits them with conditions and disclosures
- **1.5** Sensitivity Label Taxonomy — Copilot label inheritance was claimed as universal; behavior varies by workload

#### Recurring Pattern Fixes (All 57 Controls)
- **GLBA Safeguards Rule** → GLBA §501(b) — FTC Safeguards Rule applies to non-bank institutions only; bank/broker-dealer contexts require GLBA §501(b) and sector-specific implementing guidelines
- **OCC Bulletin 2013-29** → OCC Bulletin 2023-17 — 2013-29 was rescinded/superseded by 2023-17
- **OCC Heightened Standards** → 12 CFR part 30, appendix D (OCC Heightened Standards) — formal regulatory citation
- **FINRA Rule 3110** descriptions corrected — supervision rule for supervisory systems/WSPs, not a direct access-control or records-organization mandate
- **SOX 302/404** claims narrowed to ICFR-relevant scope
- **SR 11-7** dual citation — Federal Reserve SR 11-7 / OCC Bulletin 2011-12 (not "OCC SR 11-7")
- **Admin role names** standardized to canonical short forms across all playbooks (Entra Global Admin, SharePoint Admin, Purview Compliance Admin)
- **`Request-SPOReIndex`** replaced — not a valid SPO Management Shell cmdlet; replaced with PnP PowerShell `Invoke-PnPSiteSearchReindex`

#### Technical Accuracy Fixes
- **1.2** Fix `Register-PnPEntraIDAppForInteractiveLogin` invalid `-Interactive` parameter
- **1.2** Fix `$global:PnPConnection.Timeout` → `Connect-PnPOnline -RequestTimeout`
- **1.3** Fix RSS mode return value (`Restricted` → `Enabled`); fix RCD portal label
- **1.4** Fix Bookmarks/Acronyms admin path (Search & intelligence, not Copilot > Search)
- **1.5** Remove invalid `Get-MgReportSecurity` cmdlet; replace deprecated AIP unified labeling client
- **1.6** Fix hub site permissions claim (hub association does not inherit permissions)
- **1.8** Fix `-IncludePersonalSite` parameter (`$false` → `Exclude`)
- **2.3** Fix Adaptive Protection CA condition (`User risk` → `Insider risk`)
- **2.8** Fix PowerShell syntax error (`Get-DataEncryptionPolicy-ErrorAction`)
- **3.13** Remove invalid `Get-UnifiedAuditLogRetentionPolicy` cmdlet
- **4.11** Fix Sentinel connector name (`Microsoft 365` → `Office 365`)
- Multiple admin portal path corrections (SharePoint DAG, Copilot Security, Intune update channels)

#### Structural Improvements
- ~216 playbook backlinks added to parent control files across all 4 pillars
- Broken `**Related Controls:**[` formatting fixed in 11 Pillar 4 control files
- Plain text cross-references converted to markdown links across multiple playbooks

#### AI Instruction Updates
- Added regulatory citation conventions to `.github/copilot-instructions.md`
- Added regulatory accuracy rules to `.github/instructions/fsi-language-rules.instructions.md`

---

## v1.3.2 — 2026-04-14

### Microsoft Secure and Govern Blueprint Alignment

Aligned documentation with Microsoft's [Secure and Govern Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/secure-govern-copilot-foundational-deployment-guidance) deployment blueprint (published 2026-04-09).

#### Content Updates
- **1.2** SharePoint Oversharing Detection — aligned "oversharing assessment" terminology with Microsoft's canonical "data risk assessments" term
- **1.7** SharePoint Advanced Management — expanded SharePoint Admin Agent (Content Governance Agent) with Copilot governance capabilities; added SAM Content Management Assessment section; added Microsoft 365 Archive to SAM feature table
- **2.2** Sensitivity Labels — added Purview "Secure by Default" label derivation model (site-to-file label inheritance) with FSI scale considerations; added sensitivity labels for Teams/Groups/sites reference
- **3.2** Data Retention — added Microsoft 365 Archive for inactive content section with FSI regulatory preservation use case
- **3.12** Evidence Collection — expanded Compliance Manager AI governance guidance with improvement actions, remediation tracking workflow, and framework integration

#### Architecture
- **copilot-architecture.md** — added Microsoft Secure and Govern blueprint cross-reference with 3-pillar summary (Remediate Oversharing, Set Up Guardrails, Meet Regulations)

#### Reference Updates
- Added 18 new Microsoft Learn URLs across 8 sections (blueprint, DSPM, Compliance Manager, M365 Archive, SharePoint Admin Agent, eDiscovery, site sensitivity labels, Secure by Default)
- Added new Compliance Manager and Microsoft 365 Archive URL sections

#### AI Instruction Updates
- Fixed control count (56 → 57) in `.github/copilot-instructions.md`
- Added DSPM, Compliance Manager, SAM, and M365 Archive to platform areas

---

## v1.3.1 — 2026-04-09

### New Controls
- **1.16** Copilot Tuning Governance — new control for governing fine-tuned AI agents (5,000+ license orgs), covering data selection, audit trails, output supervision, and data residency (56 → 57 controls, Pillar 1: 15 → 16 controls)

### Feature Gap Remediation (7 High-Priority)
- **2.6** Web Search Controls — added domain exclusion for web grounding (block specific domains from Copilot responses)
- **1.4** Semantic Index Governance — added authoritative sources management (designate up to 100 SharePoint sites via admin center)
- **1.7** SharePoint Advanced Management — added Agent insight report (GA), Catalog management (Preview), SharePoint Admin Agent (Preview)
- **4.1** Admin Settings — added Baseline Security Mode (BSM, 18-20 settings, simulation mode) and expanded Entra AI Administrator with dedicated homepage
- **2.14** Declarative Agents Governance — added agent pinning controls (up to 3 agents per user, admin-enforced)
- **2.1** DLP Policies — made prompt-level DLP policy location explicit (Roadmap 548671, Public Preview March 2026, GA June 2026)
- **3.11** Record Keeping — added Cohasset Associates December 2024 compliance assessment reference (SEC 17a-4, FINRA 4511, CFTC 1.31)

### Feature Gap Remediation (5 Moderate)
- **4.5** Usage Analytics — added Copilot Dashboard satisfaction/intent metrics and high-usage user identification
- **4.8** Cost Allocation — added high-usage user monitoring and message pack tracking for PAYG governance
- **1.11** Change Management — added organizational branded footer for M365 Copilot app as user trust mechanism
- **1.8** Information Architecture — added AI in SharePoint (Knowledge Agent) advisory with security implications for metadata extraction
- **README** — added governance boundary clarification (CopilotGov vs AgentGov scope)

### Reference Updates
- Updated glossary with 5 new terms (AI in SharePoint, Authoritative Sources, Baseline Security Mode, Copilot Tuning, Domain Exclusion)
- Updated admin toggles with domain exclusion, BSM, and agent pinning controls
- Updated Microsoft Learn URLs with 7 new entries across 4 sections

---

## v1.3 — 2026-04-09

### Critical — Copilot Licensing Changes (April 15, 2026)
- Added Copilot Chat Basic vs Premium tier distinction across license requirements, Control 1.9, admin toggles, FAQ, glossary, and getting-started content
- Documented April 15, 2026 deadline: organizations >2,000 users lose embedded Copilot Chat in Word, Excel, PowerPoint, OneNote for unlicensed users
- Added Edit with Copilot (Agent Mode) governance — available to all M365 users regardless of license, web data only for unlicensed users
- Added third-party model provider support (Anthropic Claude, xAI) and recommended FSI posture (disabled by default)

### Platform & Architecture Updates
- Added **Agent 365** platform — centralized agent monitoring, management, and configuration across M365 apps, Copilot Studio, and third-party integrations
- Added **Entra Agent ID** — unique agent identities in Entra ID for security tracking, policy enforcement, and audit trails
- Added **Work IQ** — persistent organizational memory for prioritized and personalized Copilot assistance
- Added **Copilot Cowork** — multi-step business task delegation with user monitoring and intervention
- Added **Researcher** and **Analyst** as distinct Copilot Chat experiences to surfaces documentation
- Updated Copilot architecture diagram and surfaces matrix with Basic vs Premium access distinction
- Added Copilot security pivot in M365 Admin Center for data access policy creation

### Control Updates (Pillar 1 — Readiness & Assessment)
- **1.9** License Planning — added Copilot Chat Basic/Premium planning, Edit with Copilot governance gap, third-party model provider assessment
- **1.13** Extensibility Readiness — added Agent 365 platform assessment, Entra Agent ID readiness, third-party model provider readiness

### Control Updates (Pillar 2 — Security & Protection)
- **2.1** DLP Policies — added Mac endpoint DLP expansion (~40→100+ file types), adaptive scoping for SharePoint, AI-powered policy explanations via Security Copilot, web-grounding DLP restrictions
- **2.2** Sensitivity Labels — added auto-labeling override for files (April 2026), permission level renames (Reviewer→Restricted Editor, Co-author→Editor), default labeling for Teams meetings
- **2.10** Insider Risk — added content preview in IRM alerts, enhanced Copilot risky AI usage indicators
- **2.11** Copilot Pages Security — added Information Barriers NOT supported for SharePoint Embedded (critical for FSI Chinese wall requirements), Notebook sensitivity labeling limitations, departed user workflow, recycle bin status, group-owned workspace policy
- **2.14** Declarative Agents Governance — added Agent 365 governance surface, Entra Agent ID security controls, third-party model provider risk factors

### Control Updates (Pillar 3 — Compliance & Audit)
- **3.2** Data Retention — added Copilot Notebooks deletion bug (MC1213768) with workaround, retention via All SharePoint Sites scope, bulk/manual label limitations
- **3.3** eDiscovery — added unified Purview eDiscovery portal transition (classic Content Search retirement), deprecated export PowerShell cmdlets, case-centric access model
- **3.4** Communication Compliance — added content preview in IRM alerts, case creation without content, PAYG AI indicators, multicloud coverage (Azure, Fabric, third-party)

### Control Updates (Pillar 4 — Operations & Monitoring)
- **4.1** Admin Settings — added Agent 365 admin surface, third-party model provider toggles, Copilot security pivot
- **4.13** Extensibility Governance — added Agent 365 operational governance procedures with cadences, agent inventory dashboards, usage reporting

### Framework Updates
- Updated executive summary with Agent 365, third-party models, and Basic/Premium licensing considerations
- Updated regulatory framework with EU AI Act compliance tracking references and Agent 365/Entra Agent ID audit capabilities
- Updated governance fundamentals with Agent 365 governance surface and Basic/Premium governance model
- Updated adoption roadmap with Agent Mode rollout milestone, April 15 licensing deadline, and Agent 365 adoption steps

### Reference Updates
- Updated Microsoft Learn URLs reference — added 9 new URLs across 2 new sections (Agent Governance, Copilot Pages and Notebooks) and 2 existing sections; all 220 existing URLs validated (0 broken)
- Updated glossary with 10 new terms (Agent 365, Copilot Chat Basic/Premium, Copilot Cowork, Edit with Copilot, Entra Agent ID, Work IQ, Editor/Restricted Editor)
- Updated FAQ with 4 new entries (Basic vs Premium, Edit with Copilot licensing, third-party models, Information Barriers limitations)
- Updated portal paths quick reference with Agent 365, third-party model, and Copilot security paths
- Updated admin toggles with third-party model provider controls and Edit with Copilot row
- Updated license requirements with Basic/Premium tiers and third-party model providers

### Playbook Updates
- Updated eDiscovery playbooks (3.3) — unified portal transition, deprecated cmdlets, case-centric access
- Updated DLP playbooks (2.1) — Mac file types, adaptive scoping, AI-powered explanations
- Updated sensitivity labels playbooks (2.2) — auto-labeling overrides, permission renames, Teams meeting labels
- Updated Copilot Pages playbooks (2.11) — IB limitations, departed user workflow, Notebook labeling
- Updated agent governance playbooks (2.14) — Agent 365, Entra Agent ID, third-party models
- Updated getting-started checklist and quick-start guide with licensing, Agent 365, and third-party model items

### Metadata
- Updated all modified control `Last Verified:` dates to `2026-04-09`
- Updated version stamps across 84 files from `v1.2.1` to `v1.3`
- Validated all Microsoft Learn URLs (220 unique, 0 broken, 0 errors)

---

## v1.2.1 — 2026-03-17

### New Controls (Pillar 1 — Readiness & Assessment)
- **1.14** Item-Level Permission Scanning — new control for scanning and governing item-level permissions before Copilot deployment
- **1.15** SharePoint Permissions Drift Detection — new control for detecting and remediating permissions drift in SharePoint sites exposed to Copilot

### Metadata Updates
- Updated control and pillar counts across README and instruction files (54 → 56 controls, Pillar 1: 13 → 15 controls)

---

## v1.2 — March 2026

### Content Quality Improvements
- Enriched Governance Levels sections in 12 controls with specific portal paths, PowerShell cmdlets, configuration values, and regulatory thresholds (2.10, 3.1, 3.2, 3.6, 3.8, 3.10, 3.11, 3.13, 4.2, 4.3, 4.4, 4.8)
- Rewrote 6 thin PowerShell playbooks with real cmdlets replacing pseudo-code (3.7, 3.8, 3.9, 4.3, 4.7, 4.12)
- Improved 6 moderate PowerShell playbooks — replaced hardcoded data with parameterized scripts (2.11, 3.12, 3.13, 4.6, 4.9, 4.10)

### Research-Backed Updates
- Added Copilot-specific UAL RecordTypes and operations (CopilotInteraction, TeamCopilotInteraction, AgentAdminActivity) to audit logging controls and playbooks
- Added IRM "Risky AI usage (preview)" template and Generative AI indicators to insider risk control
- Added amended SEC Reg S-P timeline (Dec 3, 2025 compliance deadline) and 72-hour vendor notification details
- Added OCC Bulletin 2025-26 proportionality principle to model risk management control
- Added FFIEC AIO (2021) booklet examination procedures and examiner documentation request checklist
- Added Teams meeting default change (MC1139493, September 2025) to Teams meetings governance
- Added PAYG billing model details ($0.01/message) and Graph API usage endpoints to cost allocation control
- Added Viva Copilot per-app features and portal-only limitation documentation

### CI and Validation
- Fixed pre-existing FSI language rule violation in Control 4.2 ("guarantees" → "requires")
- Added FINRA 2210 control and playbooks to language rule scanner exemptions (intentional prohibited phrase examples)
- Added `.github/copilot-instructions.md` for Copilot session context

---

## v1.1 — February 2026

### Framework Updates
- Added FINRA 2026 agentic AI supervision guidance to regulatory framework
- Added SEC 2026 examination priorities (internal AI tool focus)
- Added OCC Bulletin 2025-26 MRM proportionality guidance
- Added SEC v. Delphia/Global Predictions enforcement precedent
- Fixed Colorado AI Act effective date to June 2026 (SB 25B-004 amendment)
- Added Copilot Control System section to architecture documentation
- Verified all Microsoft Learn URLs use current namespaces

### Control Updates (Pillar 3 — Compliance & Audit)
- **3.1** Copilot Audit Logging — restructured retention locations, threaded summaries
- **3.2** Data Retention Policies — updated retention location coverage
- **3.3** eDiscovery — unified experience update, enhanced Copilot content search
- **3.4** Communication Compliance — IRM integration, expanded Copilot surface coverage
- **3.5** FINRA 2210 — SEC v. Delphia enforcement precedent, AI disclosure requirements
- **3.6** Supervision and Oversight — FINRA 2026 agentic AI supervision, SEC 2026 exam focus
- **3.8** Model Risk Management — OCC Bulletin 2025-26 proportionality principle
- **3.10** SEC Reg S-P Privacy — 72-hour vendor notification requirement
- **3.11** Record Keeping — 17a-4(f)(2)(ii)(A) audit-trail alternative, off-channel enforcement

### Control Updates (Pillar 4 — Operations & Monitoring)
- **4.1** Admin Settings — Copilot Control System branding, Baseline Security Mode
- **4.2** Teams Meetings Governance — default Copilot behavior change (effective March 2026)
- **4.4** Viva Suite Governance — Copilot Chat insights, Engage-to-Teams migration
- **4.8** Cost Allocation — PAYG billing model ($0.01/message), budget cap governance

### Reference Updates
- Updated regulatory mappings with 7 new citations from Phase 3-4 controls
- Updated license requirements: SAM included with Copilot licenses, PAYG option, Frontline SKU availability
- Added cross-pillar Related Controls links to all 54 control documents

### Navigation and Build Fixes
- Rebuilt implementation checklist with correct control taxonomy (all 56 controls)
- Updated quick-start guide control references and playbook links
- Populated Pillar 3 and 4 playbook index tables (replacing "Coming soon" stubs)
- Fixed broken cross-references in playbook troubleshooting guides
- Fixed pillar deep-links in playbooks overview

### Repository Hygiene
- Added .gitignore for build artifacts, planning files, and research documents
- Removed internal planning artifacts from git tracking

---

## v1.0 — February 2026

### Initial Release
- 54 governance controls across 4 lifecycle pillars (Readiness, Security, Compliance, Operations)
- 216 implementation playbooks (portal walkthrough, PowerShell setup, verification, troubleshooting per control)
- 9 framework documents (executive summary, architecture, regulatory framework, operating model, adoption roadmap)
- 11 reference documents (regulatory mappings, license requirements, admin toggles, glossary, FAQ)
- MkDocs Material site with search, dark/light mode, and structured navigation
- Coverage for 12+ US financial regulations (FINRA, SEC, OCC, FFIEC, CFPB, GLBA, SOX)
