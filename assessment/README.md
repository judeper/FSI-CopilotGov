# FSI-CopilotGov Assessment Engine

Python-based scoring engine and PowerShell collectors for the FSI-CopilotGov
governance framework.

> **Heritage.** The engine was ported from FSI-AgentGov v1.4 in v1.4.0 of this
> repository. PPAC (Power Platform Admin Center) collectors and evaluators
> have been removed because FSI-CopilotGov is scoped to Microsoft 365 Copilot
> surfaces (Word, Excel, PowerPoint, Outlook, Teams, OneDrive, SharePoint,
> Copilot Chat, Copilot Pages, declarative agents, Agents 365). Power Platform
> and Copilot Studio governance live in the companion FSI-AgentGov framework.
> A single dead-code constant (``LEGACY_AGENTGOV_COPILOT_STUDIO_APP_ID`` in
> ``engine/score.py``) is retained as a labelled quarantine block to preserve
> the AgentGov evaluator shape — see the inline comment for the rationale.

## Layout

| Path | Purpose |
|------|---------|
| `manifest/controls.json` | Control manifest consumed by the engine and SPA (count derived at load time) |
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
  used historically by FSI-AgentGov.
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
