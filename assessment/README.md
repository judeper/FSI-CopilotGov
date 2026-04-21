# FSI-CopilotGov Assessment Engine

Python-based scoring engine and PowerShell collectors for the FSI-CopilotGov
governance framework. Adapted from FSI-AgentGov v1.4 with Power Platform
Admin Center (PPAC) collectors and evaluators removed — this repository is
scoped to Microsoft 365 Copilot surfaces.

## Layout

| Path | Purpose |
|------|---------|
| `manifest/controls.json` | 58-control manifest (engine + SPA fields) |
| `manifest/generate_manifest.py` | Engine-schema generator (idempotent) |
| `manifest/authored_content.py` | Hand-authored SPA-extension content |
| `engine/score.py` | Scoring engine — emits `scores.json` |
| `engine/report.py` | Report generator — emits prefilled MD + summary JSON |
| `collectors/Collect-Graph.ps1` | Microsoft Graph telemetry collector |
| `collectors/Collect-Purview.ps1` | Purview / IPPSSession collector |
| `collectors/Collect-SharePoint.ps1` | SharePoint PnP collector |
| `collectors/Collect-Sentinel.ps1` | Sentinel / Az collector |
| `tests/` | pytest suite (engine smoke tests) |
| `requirements.txt` | Python deps for the engine + tests |

## Quick start

```powershell
# 1. Install Python deps
pip install -r assessment/requirements.txt

# 2. Generate / validate the manifest
python assessment/manifest/generate_manifest.py
python scripts/harvest_manifest_extension.py
python scripts/merge_authored_content.py
python scripts/validate_manifest.py --strict --allow-todo

# 3. Run the collectors (each writes a JSON file under .\collected\)
mkdir collected
.\assessment\collectors\Collect-Graph.ps1     -OutputPath .\collected\graph.json
.\assessment\collectors\Collect-Purview.ps1   -OutputPath .\collected\purview.json
.\assessment\collectors\Collect-SharePoint.ps1 -OutputPath .\collected\sharepoint.json
.\assessment\collectors\Collect-Sentinel.ps1  -OutputPath .\collected\sentinel.json

# 4. Score the assessment for a given zone
python assessment/engine/score.py `
    --manifest assessment/manifest/controls.json `
    --collected .\collected `
    --zone 2 `
    --output .\scores.json

# 5. Generate the customer-ready report
python assessment/engine/report.py `
    --scores .\scores.json `
    --manifest assessment/manifest/controls.json `
    --customer "Contoso Bank" `
    --zone 2 `
    --output-dir .\reports
```

## Engine behaviour

* The engine accepts both manifest shapes — a flat JSON list (CopilotGov
  current shape) and the `{"version": ..., "controls": [...]}` envelope
  used historically by AgentGov.
* Controls with empty `checks[]` (most CopilotGov controls today) score
  maturity 0 with confidence "low" — this is expected until per-control
  check authoring lands in a follow-up sprint.
* Evaluators are pluggable. To add one, define `_eval_<name>(collected,
  source_key) -> (passed, evidence)` in `engine/score.py` and register
  it in the `EVALUATORS` dict.

## Tests

```powershell
pip install -r assessment/requirements.txt
pytest assessment/tests -v
```

The smoke suite verifies the live manifest scores cleanly across all
three zones, both manifest shapes are accepted, and the maturity
threshold logic behaves as designed.
