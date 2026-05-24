# Rusty — FSI-CopilotGov Override

> Thin override for FSI-CopilotGov. Full charter in `judeper/OceanSquad/.squad/agents/rusty/charter.md`.

## Repo-Specific Instructions
- Read `.squad/skills/repo-context.md` for repo structure and validation commands
- This repo has a Python assessment engine, PowerShell collectors, manifest pipeline, and vitest SPA tests
- After code changes, run the full local gate sweep (see repo-context.md)
- Respect the manifest pipeline order: generate → harvest → merge → validate

## What I Can Edit
- `assessment/engine/` — scoring engine (score.py, report.py)
- `assessment/collectors/` — PowerShell evidence collectors
- `assessment/manifest/` — manifest generation and authored content
- `scripts/` — validation, monitoring, and build scripts
- `.github/workflows/` — CI/CD pipelines
- `mkdocs.yml` — site config (with care)
- `package.json` — npm dependencies
- `requirements.txt` — Python dependencies

## What I Must NOT Edit
- `docs/controls/**/*.md` — control content (linus's domain)
- `docs/playbooks/**/*.md` — playbooks (linus's domain)
- `docs/framework/**/*.md` — framework pages (linus's domain)
