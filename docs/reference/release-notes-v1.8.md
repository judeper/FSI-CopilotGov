# Release Notes — v1.8.0 (July 2026)

## Release Summary

Version 1.8.0 delivers the Cowork GA governance refresh, adds Control 4.16 (Microsoft Scout Governance), and regenerates all canonical derived assets after integrating shared-doc wiring, cross-control links, monitor repairs, and authored-content overlays.

Verification date for this release train: **2026-07-10**.

## Highlights

- **Control 4.16 — Microsoft Scout Governance** added in Pillar 4 with a **Regulated** overall governance tier and a full 4-playbook implementation set.
- **Control 4.15 — Copilot Cowork Governance** refreshed for GA operating posture, with updated cross-control supervision and records-linking guidance.
- **Canonical counts regenerated and reconciled**:
  - Controls: **64**
  - Pillars: **16 / 17 / 15 / 16**
  - Tier totals: **Baseline 18**, **Recommended 33**, **Regulated 13**
  - Playbooks: **272 total** (**253** control implementations + **19** cross-cutting)
- **Manifest and template regeneration** completed across content graph, manifest, assessment data, and role-checklist workbooks (canonical + homework-linked roles; no placeholder `.xlsx` artifacts).
- **Monitor attribution/configuration repairs** carried into this release baseline and reflected in regenerated outputs.

## Data and Authoring Notes

- Manifest TODO markers were re-measured during regeneration:
  - Baseline before regeneration: **211**
  - Final after merge/rebuild: **208**
  - Net delta: **-3**
- One explicit Scout sector TODO remains by design for preview-era evidence limits.

## Monitoring Operational Caveat

- Newly added **Scout Microsoft Learn URLs** are seeded into monitor drift baselines by the first scheduled monitor run after this release.
- If you need immediate deterministic baselines (for example, before the next scheduler window), intentionally refresh current monitor state first; otherwise expect first-run deltas.

## Important Preview Caveat

Scout remains a Frontier preview capability and Cowork feature behavior can continue to evolve. This release documents the governance posture verified as of the date above; organizations should re-verify Microsoft documentation, policy surfaces, and evidence paths before relying on controls for production regulatory attestations.

## See Also

- [CHANGELOG](https://github.com/judeper/FSI-CopilotGov/blob/main/CHANGELOG.md)
- [Control 4.16 — Microsoft Scout Governance](../controls/pillar-4-operations/4.16-microsoft-scout-governance.md)
- [Control 4.15 — Copilot Cowork Governance](../controls/pillar-4-operations/4.15-copilot-cowork-governance.md)

---

*FSI Copilot Governance Framework v1.8.0 - July 2026*
