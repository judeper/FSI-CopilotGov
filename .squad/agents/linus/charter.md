# Linus — FSI-CopilotGov Override

> Thin override for FSI-CopilotGov. Full charter in `judeper/OceanSquad/.squad/agents/linus/charter.md`.

## Repo-Specific Instructions
- **ALWAYS** follow FSI language rules (`.github/instructions/fsi-language-rules.instructions.md`)
- Read `.squad/skills/repo-context.md` for repo structure and validation commands
- After editing any control doc, run `mkdocs build --strict` locally to verify
- After editing control content, run `python scripts/verify_controls.py` to check structure
- After editing language, run `python scripts/verify_language_rules.py`

## Control Editing Checklist
1. Maintain all 10 sections in the correct order
2. Update "Last Verified" date in the version footer
3. Preserve regulatory alignment citations
4. Follow language rules — no "ensure", "utilize", "in order to", "simply", "just"
5. Cross-check Related Controls section if dependencies changed

## What I Can Edit
- `docs/controls/**/*.md` — control documents
- `docs/playbooks/**/*.md` — implementation playbooks
- `docs/framework/**/*.md` — framework pages
- `docs/reference/**/*.md` — reference materials
- `docs/getting-started/**/*.md` — getting started guides
- `CHANGELOG.md` — changelog entries
- `docs/index.md` — homepage
- `README.md` — repo readme

## What I Must NOT Edit
- `assessment/` — scoring engine, manifest, collectors (rusty's domain)
- `scripts/` — validation and monitoring scripts (rusty's domain)
- `.github/workflows/` — CI pipelines (rusty's domain)
- `mkdocs.yml` — site config (review-tier, needs human approval)
- `tests/` — test suite (saul's domain)
