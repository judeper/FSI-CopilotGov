#!/usr/bin/env python3
"""Generate the FSI-CopilotGov engine-facing manifest (controls.json).

This file produces the *engine-facing* portion of the manifest:

* Per-control identity (id, title, pillar, source_file).
* Automation hints (automation, collection_methods, manual_question).
* Initial empty ``checks`` list and ``zone_thresholds`` stub.
* Initial empty ``solutions`` list (filled by Phase C tooling).

The *SPA-facing* extension fields (name, zonesApplicable, roles,
regulatory, priority, yesBar, partialBar, noBar, verifyIn,
verifyPowerShell, evidenceExpected, controlDocUrl, portalPlaybookUrl,
collectorField, sectorYesBar, facilitatorNotes) are appended additively
by ``scripts/harvest_manifest_extension.py`` (Phase A2). This generator
deliberately *does not* overwrite those fields if the manifest already
exists — see ``MERGE_KEYS_PRESERVED``.

Schema mirrors the FSI-AgentGov v1.4 manifest with adjustments for
M365 Copilot scope:

* No PPAC / Power Platform collectors (Copilot stack only).
* Pillar names: Readiness, Security, Compliance, Operations.
* 62 controls across 4 pillars (16 / 17 / 15 / 14).
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS_BASE = ROOT / "docs" / "controls"
OUTPUT = ROOT / "assessment" / "manifest" / "controls.json"

PILLAR_DIRS = {
    1: ("pillar-1-readiness", "Readiness & Assessment"),
    2: ("pillar-2-security", "Security & Data Protection"),
    3: ("pillar-3-compliance", "Compliance & Records"),
    4: ("pillar-4-operations", "Operations & Lifecycle"),
}

# Fields preserved from any pre-existing manifest entry (additive harvest
# output from Phase A2). Re-running this generator MUST NOT clobber them.
MERGE_KEYS_PRESERVED = (
    "name", "zonesApplicable", "roles", "regulatory", "priority",
    "yesBar", "partialBar", "noBar", "verifyIn", "verifyPowerShell",
    "evidenceExpected", "controlDocUrl", "portalPlaybookUrl",
    "collectorField", "sectorYesBar", "facilitatorNotes", "solutions",
    "checks",  # checks may be authored manually; preserve if present
)

# (id, filename, pillar, automation, collection_methods, manual_question)
#
# automation: full | partial | manual
#   full    — fully evidence-collectable via API/PowerShell
#   partial — collector returns config state but human attestation needed
#             for cadence/effectiveness
#   manual  — policy / process control; collector returns no evidence
#
# collection_methods is the *intended* set of collectors that may emit
# evidence for this control. The Python engine uses this to decide
# which collector outputs to inspect. Empty for manual-only controls.
CONTROLS = [
    # ---------------------------------------------------------------
    # Pillar 1 — Readiness & Assessment (16)
    # ---------------------------------------------------------------
    ("1.1",  "1.1-copilot-readiness-assessment.md",            1, "manual",  [], "Has a comprehensive pre-deployment readiness assessment of the data environment been completed and documented within the last 12 months?"),
    ("1.2",  "1.2-sharepoint-oversharing-detection.md",        1, "partial", ["SharePoint_Graph", "M365Admin"], "Have oversharing scans been reviewed and remediation tracked in the last 30 days?"),
    ("1.3",  "1.3-restricted-sharepoint-search.md",            1, "full",    ["SharePoint_Graph"], None),
    ("1.4",  "1.4-semantic-index-governance.md",               1, "partial", ["SharePoint_Graph"], "Are semantic-index inclusion/exclusion rules reviewed on a documented schedule?"),
    ("1.5",  "1.5-sensitivity-label-taxonomy-review.md",       1, "partial", ["Purview_PowerShell"], "Has the sensitivity-label taxonomy been reviewed for AI-readiness in the last 12 months?"),
    ("1.6",  "1.6-permission-model-audit.md",                  1, "partial", ["SharePoint_Graph"], "Has a least-privilege permission audit covering Copilot-grounded sites been completed in the last 90 days?"),
    ("1.7",  "1.7-sharepoint-advanced-management.md",          1, "full",    ["SharePoint_Graph"], None),
    ("1.8",  "1.8-information-architecture-review.md",         1, "manual",  [], "Has the information architecture (IA) been reviewed for Copilot-grounding suitability and findings tracked to remediation?"),
    ("1.9",  "1.9-license-planning.md",                        1, "full",    ["M365Admin"], None),
    ("1.10", "1.10-vendor-risk-management.md",                 1, "manual",  [], "Has third-party / vendor risk assessment (per OCC Bulletin 2023-17) been completed for Copilot, plug-ins, and connectors used in production?"),
    ("1.11", "1.11-change-management-adoption.md",             1, "manual",  [], "Is a documented change-management and adoption plan in place for Copilot rollout, with executive sponsorship?"),
    ("1.12", "1.12-training-awareness.md",                     1, "manual",  [], "Have all in-scope users completed Copilot training and acceptable-use acknowledgement in the last 12 months?"),
    ("1.13", "1.13-extensibility-readiness.md",                1, "manual",  [], "Has an extensibility / agent governance framework (declarative agents, plug-ins, MCP) been formally adopted before enabling extensibility surfaces?"),
    ("1.14", "1.14-item-level-permission-scanning.md",         1, "partial", ["SharePoint_Graph"], "Are item-level permissions on Copilot-grounded knowledge sources scanned and reviewed on a documented cadence?"),
    ("1.15", "1.15-sharepoint-permissions-drift.md",           1, "partial", ["SharePoint_Graph"], "Is SharePoint permissions drift monitored and reconciled on a documented cadence (RAC / Site Lifecycle Management)?"),
    ("1.16", "1.16-copilot-tuning-governance.md",              1, "manual",  [], "Is Copilot Tuning subject to a model-governance review (model risk management, evaluation harness) before publishing tuned models?"),
    # ---------------------------------------------------------------
    # Pillar 2 — Security & Data Protection (16)
    # ---------------------------------------------------------------
    ("2.1",  "2.1-dlp-policies-for-copilot.md",                2, "full",    ["Purview_PowerShell"], None),
    ("2.2",  "2.2-sensitivity-labels-classification.md",       2, "full",    ["Purview_PowerShell"], None),
    ("2.3",  "2.3-conditional-access-policies.md",             2, "full",    ["Graph_API"], None),
    ("2.4",  "2.4-information-barriers.md",                    2, "full",    ["Purview_PowerShell"], None),
    ("2.5",  "2.5-data-minimization-grounding-scope.md",       2, "manual",  [], "Has data minimization been applied to Copilot grounding scope (per-agent/site limits) and reviewed on a documented cadence?"),
    ("2.6",  "2.6-web-search-controls.md",                     2, "full",    ["M365Admin"], None),
    ("2.7",  "2.7-data-residency.md",                          2, "full",    ["M365Admin", "Graph_API"], None),
    ("2.8",  "2.8-encryption.md",                              2, "full",    ["Graph_API", "Purview_PowerShell"], None),
    ("2.9",  "2.9-defender-cloud-apps.md",                     2, "partial", ["Defender"], "Are Defender for Cloud Apps Copilot session policies and anomaly alerts reviewed on a documented cadence?"),
    ("2.10", "2.10-insider-risk-detection.md",                 2, "partial", ["Purview_PowerShell"], "Have any insider-risk alerts touching Copilot interactions been reviewed and dispositioned this quarter?"),
    ("2.11", "2.11-copilot-pages-security.md",                 2, "full",    ["M365Admin", "SharePoint_Graph"], None),
    ("2.12", "2.12-external-sharing-governance.md",            2, "full",    ["SharePoint_Graph"], None),
    ("2.13", "2.13-plugin-connector-security.md",              2, "partial", ["M365Admin", "Graph_API"], "Is the plug-in / connector inventory reviewed and approved on a documented cadence, with un-approved connectors blocked?"),
    ("2.14", "2.14-declarative-agents-governance.md",          2, "partial", ["M365Admin", "Graph_API"], "Are declarative agents subject to a publishing-approval workflow with a maintained inventory?"),
    ("2.15", "2.15-network-security.md",                       2, "full",    ["Graph_API"], None),
    ("2.16", "2.16-federated-connector-mcp-governance.md",     2, "partial", ["M365Admin", "Graph_API"], "Are federated connectors and MCP endpoints subject to a documented approval, allow-list, and review cycle?"),
    ("2.17", "2.17-cross-tenant-agent-federation.md",          2, "manual",  [], "Are cross-tenant Entra Agent ID trust relationships, MCP federated server attestations, and Copilot Studio multi-tenant publishings subject to documented approval and review?"),
    # ---------------------------------------------------------------
    # Pillar 3 — Compliance & Records (13)
    # ---------------------------------------------------------------
    ("3.1",  "3.1-copilot-audit-logging.md",                   3, "full",    ["Purview_PowerShell"], None),
    ("3.2",  "3.2-data-retention-policies.md",                 3, "full",    ["Purview_PowerShell"], None),
    ("3.3",  "3.3-ediscovery-copilot-content.md",              3, "full",    ["Purview_PowerShell"], None),
    ("3.4",  "3.4-communication-compliance.md",                3, "partial", ["Purview_PowerShell"], "Has the communication-compliance review queue covering Copilot interactions been reviewed in the last 30 days?"),
    ("3.5",  "3.5-finra-2210-compliance.md",                   3, "manual",  [], "Are Copilot outputs used in FINRA Rule 2210 communications subject to documented principal review before use?"),
    ("3.6",  "3.6-supervision-oversight.md",                   3, "manual",  [], "Is there a designated supervisory principal for Copilot use in regulated workflows, with a documented review cadence (FINRA Rule 3110)?"),
    ("3.7",  "3.7-regulatory-reporting.md",                    3, "manual",  [], "Are Copilot-related regulatory reports (e.g., book/record certifications, AI disclosures) produced on the required cadence?"),
    ("3.8",  "3.8-model-risk-management.md",                   3, "manual",  [], "Has a model-risk-management review aligned to SR 11-7 / OCC Bulletin 2011-12 been completed for Copilot deployments touching regulated functions?"),
    ("3.8a", "3.8a-generative-ai-model-governance.md",         3, "manual",  [], "Has a generative-AI model-governance review (NIST AI RMF 1.0 / ISO/IEC 42001, addressing the SR 26-2 / OCC 2026-13 generative-AI exclusion) been completed for Copilot?"),
    ("3.9",  "3.9-ai-disclosure-transparency.md",              3, "manual",  [], "Is AI disclosure language presented to customers / counterparties before any Copilot-generated content is shared externally?"),
    ("3.10", "3.10-sec-reg-sp-privacy.md",                     3, "partial", ["Purview_PowerShell"], "Have SEC Reg S-P / GLBA §501(b) privacy controls been reviewed for Copilot processing of customer NPI?"),
    ("3.11", "3.11-record-keeping.md",                         3, "partial", ["Purview_PowerShell"], "Are Copilot interactions captured into the firm's books-and-records system per SEC Rule 17a-4 (where applicable)?"),
    ("3.12", "3.12-evidence-collection.md",                    3, "manual",  [], "Is there a documented evidence-collection runbook used for Copilot-related audits and exam responses?"),
    ("3.13", "3.13-ffiec-alignment.md",                        3, "manual",  [], "Has FFIEC IT Handbook alignment (Information Security, Outsourcing, Architecture) been reviewed for Copilot deployment?"),
    ("3.14", "3.14-copilot-pages-notebooks-retention.md",      3, "partial", ["Purview_PowerShell"], "Are branch-aware Copilot Pages, Notebook section-level coverage, and Loop component provenance addressed in retention and records-management policies?"),
    # ---------------------------------------------------------------
    # Pillar 4 — Operations & Lifecycle (13)
    # ---------------------------------------------------------------
    ("4.1",  "4.1-admin-settings-feature-management.md",       4, "full",    ["M365Admin"], None),
    ("4.2",  "4.2-teams-meetings-governance.md",               4, "full",    ["Teams"], None),
    ("4.3",  "4.3-teams-phone-queues.md",                      4, "full",    ["Teams"], None),
    ("4.4",  "4.4-viva-suite-governance.md",                   4, "partial", ["VivaInsights", "M365Admin"], "Is Viva-suite Copilot integration (Insights, Engage, Topics) reviewed on a documented governance cadence?"),
    ("4.5",  "4.5-usage-analytics.md",                         4, "partial", ["M365Admin"], "Are Copilot usage analytics reported to leadership on a documented cadence with anomalies flagged?"),
    ("4.6",  "4.6-viva-insights-measurement.md",               4, "partial", ["VivaInsights"], "Are Viva Insights Copilot impact reports reviewed on a documented cadence with caveats applied?"),
    ("4.7",  "4.7-feedback-telemetry.md",                      4, "partial", ["M365Admin"], "Is Copilot feedback / thumb-rating telemetry reviewed on a documented cadence and routed to product owners?"),
    ("4.8",  "4.8-cost-allocation.md",                         4, "manual",  [], "Is Copilot license cost allocation reviewed and chargeback / showback executed on a documented cadence?"),
    ("4.9",  "4.9-incident-reporting.md",                      4, "manual",  [], "Is there a documented incident-response process covering Copilot-specific incidents (oversharing, hallucination, prompt injection) with reporting paths?"),
    ("4.10", "4.10-business-continuity.md",                    4, "manual",  [], "Has a business-continuity plan for Copilot-dependent workflows been documented and tested in the last 12 months?"),
    ("4.11", "4.11-sentinel-integration.md",                   4, "partial", ["Defender"], "Are Sentinel detections covering Copilot misuse reviewed and tuned on a documented cadence?"),
    ("4.12", "4.12-change-management-rollouts.md",             4, "manual",  [], "Are Copilot feature releases (Microsoft-managed and tenant-managed) tracked and risk-reviewed before user enablement?"),
    ("4.13", "4.13-extensibility-governance.md",               4, "manual",  [], "Are extensibility surfaces (declarative agents, MCP, plug-ins) governed by an approval and inventory process before publication?"),
    ("4.14", "4.14-copilot-studio-agent-lifecycle.md",         4, "manual",  [], "Is the Copilot Studio agent lifecycle (authoring → testing → publishing → versioning → deprecation) governed with documented evidence at each gate?"),
]


def _extract_title(filepath: Path) -> str | None:
    """Pull the H1 title from a control markdown file."""
    try:
        with filepath.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    title = line.lstrip("# ").strip()
                    title = re.sub(
                        r"^Control\s+\d+\.\d+\s*[\u2013\u2014\-]\s*",
                        "",
                        title,
                    )
                    title = re.sub(
                        r"^\d+\.\d+\s*[\u2013\u2014\-]\s*", "", title
                    )
                    return title
                m = re.match(r"title:\s*(.+)", line, re.IGNORECASE)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
    except OSError:
        return None
    return None


def _zone_thresholds_stub(num_checks: int) -> dict:
    """Default zone-threshold ramp based on number of authored checks."""
    if num_checks == 0:
        return {
            "zone1": {"min_checks_passed": 0, "maturity_score": 0},
            "zone2": {"min_checks_passed": 0, "maturity_score": 0},
            "zone3": {"min_checks_passed": 0, "maturity_score": 0},
        }
    if num_checks == 1:
        return {
            "zone1": {"min_checks_passed": 1, "maturity_score": 1},
            "zone2": {"min_checks_passed": 1, "maturity_score": 2},
            "zone3": {"min_checks_passed": 1, "maturity_score": 4},
        }
    if num_checks == 2:
        return {
            "zone1": {"min_checks_passed": 1, "maturity_score": 1},
            "zone2": {"min_checks_passed": 2, "maturity_score": 2},
            "zone3": {"min_checks_passed": 2, "maturity_score": 4},
        }
    z2 = max(1, int(num_checks * 0.65))
    return {
        "zone1": {"min_checks_passed": 1, "maturity_score": 1},
        "zone2": {"min_checks_passed": z2, "maturity_score": 2},
        "zone3": {"min_checks_passed": num_checks, "maturity_score": 4},
    }


def _build_engine_entry(cid, filename, pillar, automation, methods, manual_q):
    pillar_dir, pillar_name = PILLAR_DIRS[pillar]
    source_file = f"docs/controls/{pillar_dir}/{filename}"
    title = _extract_title(DOCS_BASE / pillar_dir / filename) or filename
    checks: list = []
    return {
        "id": cid,
        "title": title,
        "pillar": pillar,
        "pillar_name": pillar_name,
        "source_file": source_file,
        "automation": automation,
        "collection_methods": methods,
        "checks": checks,
        "zone_thresholds": _zone_thresholds_stub(len(checks)),
        "manual_question": manual_q,
    }


def _load_existing(path: Path) -> dict[str, dict]:
    """Load existing manifest as id -> entry map (empty if not present)."""
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return {c.get("id"): c for c in data if isinstance(c, dict)}
    except (json.JSONDecodeError, OSError):
        pass
    return {}


def main() -> int:
    existing = _load_existing(OUTPUT)

    out: list[dict] = []
    for row in CONTROLS:
        engine = _build_engine_entry(*row)
        cid = engine["id"]
        if cid in existing:
            # Preserve any harvested SPA fields & authored checks
            merged = dict(engine)
            for k in MERGE_KEYS_PRESERVED:
                if k in existing[cid]:
                    merged[k] = existing[cid][k]
            # If checks were preserved, regenerate zone_thresholds from them
            if isinstance(merged.get("checks"), list):
                merged["zone_thresholds"] = _zone_thresholds_stub(
                    len(merged["checks"])
                )
            out.append(merged)
        else:
            out.append(engine)

    # Counts
    by_pillar = {p: 0 for p in PILLAR_DIRS}
    by_auto: dict = {}
    for c in out:
        by_pillar[c["pillar"]] += 1
        by_auto[c["automation"]] = by_auto.get(c["automation"], 0) + 1

    print(f"Generated {len(out)} controls")
    for p, (_d, name) in PILLAR_DIRS.items():
        print(f"  Pillar {p} ({name}): {by_pillar[p]}")
    for a, n in sorted(by_auto.items()):
        print(f"  {a}: {n}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"\nWritten {OUTPUT.relative_to(ROOT)} ({os.path.getsize(OUTPUT):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
