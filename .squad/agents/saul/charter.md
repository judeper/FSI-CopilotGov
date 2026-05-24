# Saul — FSI-CopilotGov Override

> Thin override for FSI-CopilotGov. Full charter in `judeper/OceanSquad/.squad/agents/saul/charter.md`.

## Repo-Specific Instructions
- Read `.squad/skills/repo-context.md` for repo structure and validation commands
- Run the full local gate sweep to verify changes
- Check both Python tests (`pytest`) and SPA tests (`vitest`) after any change
- Verify manifest consistency after control doc edits

## Verification Commands
```bash
mkdocs build --strict
python scripts/verify_controls.py
python scripts/verify_language_rules.py
python scripts/validate_manifest.py --strict --allow-todo
python -m pytest assessment/tests scripts -q
npm test
```
