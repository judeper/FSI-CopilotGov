# Release Notes — v1.4.0 (April 2026)

## What's New

Version 1.4.0 is a major feature port from the sister **FSI-AgentGov** framework, bringing governance assessment parity to Microsoft 365 Copilot. The release introduces a manifest-driven assessment engine, an interactive evidence drawer, facilitator-led workshop mode, and a catalog of curated solution recommendations that help practitioners connect assessment findings to implementation guidance.

Content authors and facilitators gain pre-session homework pages for 14 curated FSI roles, role-specific Excel checklists, and a governance dashboard that supports both self-guided and facilitated adoption journeys. CI coverage expands with a Vitest harness (60+ SPA tests across 11 files), Microsoft Learn URL monitoring, regulatory monitoring against the Federal Register and FINRA, and solutions drift detection that runs weekly.

None of these additions replace existing controls, citations, or regulatory guidance — they are intended to aid in the workshops and self-assessments that organizations run to help meet their Copilot governance obligations.

## Features

- **Manifest-driven assessment engine** — Python scoring with YAML collectors (Phase B).
- **Evidence drawer** — verifyIn links and persistent notes tied to each control (Phase D1).
- **Facilitator mode** — per-control ask/followUp prompts to support workshops (Phase D1).
- **Sector-calibration yes-bars** — tiered guidance for Baseline, Recommended, Regulated (Phase D1).
- **Solution recommendation cards** — references to `FSI-CopilotGov-Solutions@v0.1.0-rc1` (Phase C2/D1).
- **Collector evidence import** — CSV/JSON drop into the SPA (Phase D2).
- **Portal export envelope** — schema v0.1.0 for downstream tooling (Phase E).
- **Solutions catalog view** — reverse-lookup and filters across the solution library (Phase C3).
- **Homework pages** — 14 curated FSI role-based pre-session primers (Phase F).
- **Role-specific Excel checklists + governance dashboard** (Phase G).
- **Microsoft Learn URL monitoring** — weekly CI job (Phase I1).
- **Regulatory monitoring** — Federal Register + FINRA feeds (Phase I1).
- **Solutions drift detection** — weekly CI (Phase C4).
- **Vitest harness** — 60+ tests across 11 files covering SPA behavior (Phase H1/H2).

## Upgrade Notes

- Run `python scripts/generate_solutions_lock.py` after pulling to regenerate the solutions lock against the sister repo.
- The `assessment-app.js` SPA uses new localStorage keys (`fsi-copilotgov:notes:*`, `fsi-copilotgov:facilitator-mode`, `fsi-copilotgov:collector-evidence:*`, `fsi-copilotgov:envelope:*`). Prior saved state is preserved but first-time facilitator-mode users will see defaults.

## Known Limitations

- 53 of 58 controls still have TODO markers in sector-calibration yes-bars, partial bars, and facilitator notes. Quick-start controls (1.2, 1.3, 2.1, 3.1, 4.1) are fully authored.
- Sister repo FSI-CopilotGov-Solutions is pinned at RC tag `v0.1.0-rc1`. Final `v0.1.0` tag will follow CopilotGov v1.4.0 release.

## See Also

- [CHANGELOG](https://github.com/judeper/FSI-CopilotGov/blob/main/CHANGELOG.md)

---

*FSI Copilot Governance Framework v1.4.0 - April 2026*
