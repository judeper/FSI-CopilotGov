#!/usr/bin/env python3
"""
Extract assessment data from FSI-CopilotGov control markdown files.

Generates docs/javascripts/assessment-data.json for the Governance Readiness
Assessment Tool. Parses every control file under docs/controls/ to extract
metadata, verification criteria, governance level requirements, and role
assignments (control count is derived at runtime, not hard-coded).

Also parses:
- docs/reference/regulatory-mappings.md   → regulation-to-control matrix

Usage:
    python scripts/extract_assessment_data.py
    python scripts/extract_assessment_data.py --verbose
    python scripts/extract_assessment_data.py --output path/to/output.json
"""

import json
import os
import re
import sys
from pathlib import Path

# Handle Windows encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
BASE_DIR = SCRIPT_DIR.parent
DOCS_DIR = BASE_DIR / "docs"
CONTROLS_DIR = DOCS_DIR / "controls"
OUTPUT_PATH = DOCS_DIR / "javascripts" / "assessment-data.json"

PILLARS = {
    1: {"name": "Readiness & Assessment", "folder": "pillar-1-readiness", "count": 16},
    2: {"name": "Security & Protection", "folder": "pillar-2-security", "count": 17},
    3: {"name": "Compliance & Audit", "folder": "pillar-3-compliance", "count": 15},
    4: {"name": "Operations & Monitoring", "folder": "pillar-4-operations", "count": 14},
}

# Role-to-control assignments (hardcoded — CopilotGov has no structured role sections)
ROLE_CONTROLS = {
    "M365 Global Admin": ["1.9", "1.11", "1.12", "4.1", "4.2", "4.3", "4.4", "4.5", "4.7", "4.8", "4.12"],
    "Purview Compliance Admin": ["1.5", "2.1", "2.2", "2.5", "2.10", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10", "3.11", "3.12"],
    "SharePoint Admin": ["1.1", "1.2", "1.3", "1.6", "1.7", "1.8", "1.14", "1.15", "2.11", "2.12"],
    "Entra Global Admin": ["2.3", "2.4", "2.15"],
    "Exchange Online Admin": ["2.8"],
    "Teams Admin": ["4.2", "4.3"],
    "Security Admin": ["2.6", "2.7", "2.9", "2.13", "2.14", "2.16", "4.9", "4.10", "4.11"],
    "AI Governance Lead": ["1.4", "1.10", "1.13", "1.16", "3.13", "4.6", "4.13"],
}

# Adoption phase mappings (from adoption roadmap)
PHASE_CONTROLS = {
    "0": {
        "name": "Governance Setup",
        "duration": "0-30 days",
        "controls": {
            "1.1": "Critical", "1.2": "Critical", "1.3": "Critical",
            "1.5": "Critical", "1.6": "Critical", "1.9": "Critical",
            "2.1": "Critical", "2.2": "Critical", "2.3": "Critical",
            "3.1": "Critical", "3.2": "Critical",
            "4.1": "Critical",
        },
    },
    "1": {
        "name": "Pilot Deployment",
        "duration": "1-3 months",
        "controls": {
            "1.4": "High", "1.7": "High", "1.8": "High",
            "1.10": "High", "1.11": "High", "1.12": "High",
            "2.4": "High", "2.5": "High", "2.6": "High",
            "2.7": "High", "2.8": "High",
            "3.3": "High", "3.4": "High", "3.5": "High", "3.6": "High",
            "4.2": "High", "4.5": "High",
        },
    },
    "2": {
        "name": "Expansion",
        "duration": "3-12 months",
        "controls": {
            "1.13": "Medium", "1.14": "Medium", "1.15": "Medium", "2.9": "Medium", "2.10": "Medium",
            "2.11": "Medium", "2.12": "Medium", "2.13": "Medium",
            "2.14": "Medium", "2.15": "Medium",
            "3.7": "Medium", "3.8": "Medium", "3.9": "Medium",
            "3.10": "Medium", "3.11": "Medium", "3.12": "Medium", "3.13": "Medium",
            "4.3": "Medium", "4.4": "Medium", "4.6": "Medium",
            "4.7": "Medium", "4.8": "Medium", "4.9": "Medium",
            "4.10": "Medium", "4.11": "Medium", "4.12": "Medium", "4.13": "Medium",
        },
    },
}

# Regulatory priority by institution type
INSTITUTION_REGULATORY_PRIORITY = {
    "broker-dealer": {
        "label": "Broker-Dealer (FINRA/SEC)",
        "primary_regulations": ["FINRA 4511", "FINRA 3110", "FINRA 2210", "SEC 17a-3/4"],
        "priority_controls": ["3.1", "3.2", "3.4", "3.5", "3.6", "3.11"],
    },
    "bank": {
        "label": "Bank (OCC/Fed)",
        "primary_regulations": ["OCC 2011-12", "FFIEC IT Handbook", "GLBA 501(b)"],
        "priority_controls": ["1.1", "1.2", "2.1", "3.8", "3.13"],
    },
    "adviser": {
        "label": "Investment Adviser (SEC)",
        "primary_regulations": ["SEC Reg S-P", "SEC Reg BI", "SEC 17a-3/4"],
        "priority_controls": ["2.5", "3.6", "3.10"],
    },
    "dual-registered": {
        "label": "Dual-Registered (FINRA + SEC)",
        "primary_regulations": ["FINRA 4511", "FINRA 3110", "SEC 17a-3/4", "SEC Reg BI"],
        "priority_controls": ["3.1", "3.4", "3.5", "3.6", "3.11"],
    },
    "insurance": {
        "label": "Insurance Company",
        "primary_regulations": ["GLBA 501(b)", "State Insurance Regulations"],
        "priority_controls": ["1.1", "2.1", "2.2", "3.10"],
    },
    "credit-union": {
        "label": "Credit Union (NCUA)",
        "primary_regulations": ["GLBA 501(b)", "NCUA Part 748"],
        "priority_controls": ["1.1", "2.1", "3.1"],
    },
}

VERBOSE = False


def log(msg):
    if VERBOSE:
        print(f"  {msg}")


def find_control_files(pillar_num):
    """Find all control markdown files in a pillar folder (excluding index.md)."""
    folder = CONTROLS_DIR / PILLARS[pillar_num]["folder"]
    if not folder.exists():
        print(f"  ERROR: Pillar folder not found: {folder}")
        return []
    files = sorted(folder.glob("*.md"))
    return [f for f in files if f.name != "index.md"]


def find_control_file(pillar_num, ctrl_num):
    """Find the markdown file for a specific control."""
    folder = CONTROLS_DIR / PILLARS[pillar_num]["folder"]
    pattern = f"{pillar_num}.{ctrl_num}-*.md"
    matches = list(folder.glob(pattern))
    if not matches:
        return None
    return matches[0]


def extract_section(content, heading, next_heading_pattern=r"^## "):
    """Extract content between a heading and the next same-level heading."""
    pattern = rf"^{re.escape(heading)}\s*$"
    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(next_heading_pattern, content[start:], re.MULTILINE)
    if next_match:
        return content[start:start + next_match.start()].strip()
    return content[start:].strip()


def parse_metadata(content):
    """Extract metadata fields from the top of a control file."""
    meta = {}

    # Control title: "# Control 1.1: Copilot Readiness Assessment..."
    title_match = re.search(
        r"^#\s+Control\s+(\d+\.\d+[a-z]?)[:\-]\s*(.+)$", content, re.MULTILINE
    )
    if title_match:
        meta["id"] = title_match.group(1)
        meta["title"] = title_match.group(2).strip()

    # Standard metadata fields
    fields = {
        "pillar": r"\*\*Pillar:\*\*\s*(.+)",
        "regulatoryReference": r"\*\*Regulatory Reference:\*\*\s*(.+)",
        "governanceLevels": r"\*\*Governance Levels:\*\*\s*(.+)",
    }
    for key, pattern in fields.items():
        match = re.search(pattern, content)
        if match:
            meta[key] = match.group(1).strip()

    return meta


def parse_objective(content):
    """Extract the Objective section text."""
    section = extract_section(content, "## Objective")
    # Clean up markdown formatting
    section = re.sub(r"\*\*([^*]+)\*\*", r"\1", section)  # Remove bold
    # Take first paragraph only for summary
    paragraphs = section.split("\n\n")
    return paragraphs[0].strip() if paragraphs else section


def generate_question_text(objective):
    """Transform an imperative objective into a question for assessment.

    Converts statements like "Configure and maintain comprehensive audit logging..."
    into "Has your organization configured and maintained comprehensive audit logging...?"
    """
    if not objective:
        return None

    text = objective.strip()
    text = text.rstrip(".")

    # Compound verb patterns (check first — "Configure and maintain", etc.)
    compound_transforms = [
        (r"^Configure and maintain\b", "Has your organization configured and maintained"),
        (r"^Conduct a comprehensive\b", "Has your organization conducted a comprehensive"),
        (r"^Establish and maintain\b", "Has your organization established and maintained"),
        (r"^Develop and implement\b", "Has your organization developed and implemented"),
        (r"^Design and implement\b", "Has your organization designed and implemented"),
        (r"^Deploy and configure\b", "Has your organization deployed and configured"),
        (r"^Implement and maintain\b", "Has your organization implemented and maintained"),
        (r"^Define and enforce\b", "Has your organization defined and enforced"),
        (r"^Create and maintain\b", "Has your organization created and maintained"),
        (r"^Review and update\b", "Has your organization reviewed and updated"),
        (r"^Monitor and enforce\b", "Does your organization monitor and enforce"),
        (r"^Assess and remediate\b", "Has your organization assessed and remediated"),
    ]

    for pattern, replacement in compound_transforms:
        match = re.match(pattern, text, re.IGNORECASE)
        if match:
            result = replacement + text[match.end():]
            return result + "?"

    # Single verb-to-question prefix mappings (first match wins)
    transforms = [
        (r"^Ensure\b", "Does your organization ensure"),
        (r"^Restrict\b", "Has your organization restricted"),
        (r"^Implement\b", "Has your organization implemented"),
        (r"^Establish\b", "Has your organization established"),
        (r"^Define\b", "Has your organization defined"),
        (r"^Configure\b", "Has your organization configured"),
        (r"^Deploy\b", "Has your organization deployed"),
        (r"^Enable\b", "Has your organization enabled"),
        (r"^Enforce\b", "Does your organization enforce"),
        (r"^Monitor\b", "Does your organization monitor"),
        (r"^Maintain\b", "Does your organization maintain"),
        (r"^Require\b", "Does your organization require"),
        (r"^Apply\b", "Has your organization applied"),
        (r"^Create\b", "Has your organization created"),
        (r"^Assign\b", "Has your organization assigned"),
        (r"^Validate\b", "Does your organization validate"),
        (r"^Track\b", "Does your organization track"),
        (r"^Review\b", "Does your organization review"),
        (r"^Automate\b", "Has your organization automated"),
        (r"^Document\b", "Has your organization documented"),
        (r"^Integrate\b", "Has your organization integrated"),
        (r"^Protect\b", "Does your organization protect"),
        (r"^Limit\b", "Has your organization limited"),
        (r"^Manage\b", "Does your organization manage"),
        (r"^Control\b", "Does your organization control"),
        (r"^Prevent\b", "Does your organization prevent"),
        (r"^Detect\b", "Does your organization detect"),
        (r"^Extend\b", "Has your organization extended"),
        (r"^Provide\b", "Does your organization provide"),
        (r"^Identify\b", "Does your organization identify"),
        (r"^Leverage\b", "Does your organization leverage"),
        (r"^Govern\b", "Does your organization govern"),
        # Additional verbs for CopilotGov
        (r"^Conduct\b", "Has your organization conducted"),
        (r"^Assess\b", "Has your organization assessed"),
        (r"^Prepare\b", "Has your organization prepared"),
        (r"^Remediate\b", "Has your organization remediated"),
        (r"^Capture\b", "Has your organization captured"),
        (r"^Align\b", "Has your organization aligned"),
    ]

    for pattern, replacement in transforms:
        match = re.match(pattern, text, re.IGNORECASE)
        if match:
            result = replacement + text[match.end():]
            return result + "?"

    # Fallback for unmatched verbs
    return "Has your organization addressed the following: " + text + "?"


def parse_governance_levels(content):
    """Extract governance level requirements from both table and H3 formats.

    Returns:
        dict with keys "baseline", "recommended", "regulated", each containing:
            {"requirements": [...], "rationale": "..."}
    """
    section = extract_section(content, "## Governance Levels")
    if not section:
        return {}

    levels = {}

    # Try TABLE FORMAT first: | Level | Requirement | Rationale |
    table_rows = re.findall(
        r"\|\s*\*\*(\w+)\*\*\s*\|\s*([^|]+)\|\s*([^|]+)\|",
        section,
    )
    if table_rows:
        for level_name, requirement, rationale in table_rows:
            key = level_name.strip().lower()
            if key in ("baseline", "recommended", "regulated"):
                req_text = requirement.strip()
                # Split requirements on sentence boundaries or semicolons
                reqs = _split_requirements(req_text)
                levels[key] = {
                    "requirements": reqs,
                    "rationale": rationale.strip(),
                }
        if levels:
            return levels

    # Try H3 FORMAT: ### Baseline, ### Recommended, ### Regulated
    for level_name in ("Baseline", "Recommended", "Regulated"):
        h3_pattern = rf"^###\s+{level_name}\s*$"
        h3_match = re.search(h3_pattern, section, re.MULTILINE)
        if not h3_match:
            continue

        start = h3_match.end()
        # Find next ### or end of section
        next_h3 = re.search(r"^###\s+", section[start:], re.MULTILINE)
        if next_h3:
            block = section[start:start + next_h3.start()]
        else:
            block = section[start:]

        # Extract bullet list items (- [ ] or - or *)
        reqs = []
        for bullet_match in re.finditer(r"^[-*]\s+(?:\[.\]\s+)?(.+)$", block, re.MULTILINE):
            item = bullet_match.group(1).strip()
            # Clean markdown
            item = re.sub(r"\*\*([^*]+)\*\*", r"\1", item)
            if item:
                reqs.append(item)

        key = level_name.lower()
        levels[key] = {
            "requirements": reqs,
            "rationale": "",
        }

    return levels


def _split_requirements(text):
    """Split a requirement cell into individual requirements.

    Handles semicolons and sentence-like splits while preserving coherent items.
    """
    # Split on semicolons or period-space patterns that start a new requirement
    parts = re.split(r";\s*|\.\s+(?=[A-Z])", text)
    result = []
    for p in parts:
        p = p.strip().rstrip(".")
        # Clean markdown
        p = re.sub(r"\*\*([^*]+)\*\*", r"\1", p)
        if p:
            result.append(p)
    return result


def parse_verification_criteria(content):
    """Extract verification criteria from both numbered list and table formats.

    Returns list of dicts: [{"text": "...", "governanceLevel": "..." or None}]
    """
    section = extract_section(content, "## Verification Criteria")
    if not section:
        return []

    criteria = []

    # Try TABLE FORMAT: | # | Verification Step | Expected Outcome | Governance Level |
    # or: | # | Verification Step | Expected Result |
    has_table = bool(re.search(r"\|[-\s]+\|[-\s]+\|", section))

    if has_table:
        for line in section.split("\n"):
            line = line.strip()
            if not line.startswith("|"):
                continue
            # Strip leading/trailing pipes and split
            inner = line.strip("|")
            cells = [c.strip() for c in inner.split("|")]
            if len(cells) < 3:
                continue
            # Skip header and separator rows
            if cells[0].startswith("-") or cells[0] == "#" or cells[1].startswith("-"):
                continue
            if not cells[0].isdigit():
                continue

            step = re.sub(r"\*\*([^*]+)\*\*", r"\1", cells[1].strip())
            outcome = re.sub(r"\*\*([^*]+)\*\*", r"\1", cells[2].strip()) if len(cells) > 2 else ""
            level_text = cells[3].strip() if len(cells) > 3 else None

            text = f"{step} — {outcome}" if outcome else step
            gov_level = _normalize_governance_level(level_text) if level_text else None

            criteria.append({"text": text, "governanceLevel": gov_level})
        if criteria:
            return criteria

    # NUMBERED LIST FORMAT: 1. Text\n2. Text\n...
    items = re.split(r"\n\d+\.\s+", "\n" + section)
    for item in items[1:]:
        text = item.strip()
        text = re.sub(r"\n\s+", " ", text)  # Join wrapped lines
        text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # Remove bold
        if text:
            criteria.append({"text": text, "governanceLevel": None})

    return criteria


def _normalize_governance_level(text):
    """Normalize governance level text to standard keys."""
    if not text:
        return None
    text = text.strip().lower()
    if "baseline" in text:
        return "baseline"
    if "recommended" in text:
        return "recommended"
    if "regulated" in text:
        return "regulated"
    return None


def parse_regulations(reg_string):
    """Parse regulatory reference string into list of regulation codes."""
    if not reg_string:
        return []
    regs = [r.strip() for r in reg_string.split(",")]
    return [r for r in regs if r]


def parse_roles_from_content(content):
    """Extract roles from Roles & Responsibilities table if present."""
    section = extract_section(content, "## Roles & Responsibilities")
    roles = []

    for match in re.finditer(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", section):
        role = match.group(1).strip()
        responsibility = match.group(2).strip()
        if role in ("Role", "---", "----", "------") or role.startswith("-"):
            continue
        if role:
            roles.append({"role": role, "responsibility": responsibility})

    return roles


def get_roles_for_control(control_id):
    """Return list of role names assigned to this control."""
    roles = []
    for role_name, ctrl_ids in ROLE_CONTROLS.items():
        if control_id in ctrl_ids:
            roles.append(role_name)
    return roles


def get_phase_for_control(control_id):
    """Return the adoption phase and priority for this control, or None."""
    for phase_num, phase_data in PHASE_CONTROLS.items():
        if control_id in phase_data["controls"]:
            return {
                "phase": int(phase_num),
                "phaseName": phase_data["name"],
                "priority": phase_data["controls"][control_id],
            }
    return None


def parse_control(pillar_num, ctrl_num):
    """Parse a single control file and return structured data."""
    control_id = f"{pillar_num}.{ctrl_num}"
    filepath = find_control_file(pillar_num, ctrl_num)
    if not filepath:
        print(f"  ERROR: No file found for control {control_id}")
        return None

    log(f"Parsing {control_id} from {filepath.name}")
    content = filepath.read_text(encoding="utf-8")

    meta = parse_metadata(content)
    if not meta.get("id"):
        print(f"  ERROR: Could not extract ID from {filepath.name}")
        return None

    objective = parse_objective(content)
    level_reqs = parse_governance_levels(content)
    verification = parse_verification_criteria(content)
    roles = parse_roles_from_content(content)
    regulations = parse_regulations(meta.get("regulatoryReference", ""))
    phase_info = get_phase_for_control(control_id)
    assigned_roles = get_roles_for_control(control_id)
    question_text = generate_question_text(objective)

    # Build playbook paths
    playbooks = {
        "portalWalkthrough": f"playbooks/control-implementations/{control_id}/portal-walkthrough/",
        "powershellSetup": f"playbooks/control-implementations/{control_id}/powershell-setup/",
        "verificationTesting": f"playbooks/control-implementations/{control_id}/verification-testing/",
        "troubleshooting": f"playbooks/control-implementations/{control_id}/troubleshooting/",
    }

    return {
        "id": control_id,
        "pillar": pillar_num,
        "pillarName": PILLARS[pillar_num]["name"],
        "title": meta.get("title", f"Control {control_id}"),
        "objective": objective,
        "questionText": question_text,
        "regulations": regulations,
        "governanceLevels": meta.get("governanceLevels", ""),
        "levelRequirements": level_reqs,
        "verificationCriteria": verification,
        "roles": roles,
        "assignedRoles": assigned_roles,
        "adoptionPhase": phase_info,
        "playbooks": playbooks,
    }


def parse_regulatory_mappings():
    """Parse regulatory-mappings.md into regulation-to-control matrix."""
    filepath = DOCS_DIR / "reference" / "regulatory-mappings.md"
    if not filepath.exists():
        print("  WARNING: regulatory-mappings.md not found, skipping")
        return {}

    content = filepath.read_text(encoding="utf-8")
    mappings = {}

    sections = re.split(r"^## (.+)$", content, flags=re.MULTILINE)

    for i in range(1, len(sections), 2):
        heading = sections[i].strip()
        body = sections[i + 1] if i + 1 < len(sections) else ""

        # Skip non-regulation sections
        if heading.startswith("How to Use") or heading.startswith("Cross-Regulation"):
            continue

        reg_key = heading.split(" — ")[0].strip() if " — " in heading else heading.strip()

        # Find all control references in table rows
        controls = []
        for match in re.finditer(r"Control\s+(\d+\.\d+)", body):
            ctrl_id = match.group(1)
            if ctrl_id not in controls:
                controls.append(ctrl_id)

        if controls:
            mappings[reg_key] = {
                "label": heading,
                "controls": sorted(controls, key=lambda x: [int(p) for p in x.split(".")]),
            }

    return mappings


def build_output():
    """Build the complete assessment data JSON."""
    controls = []
    errors = []

    for pillar_num, pillar_data in PILLARS.items():
        folder = CONTROLS_DIR / pillar_data["folder"]
        files = sorted(folder.glob(f"{pillar_num}.*-*.md"))
        ctrl_nums = []
        for f in files:
            # Filename like "3.8a-generative-ai-model-governance.md" -> ctrl_num "8a"
            stem = f.stem  # e.g. "3.8a-generative-ai-model-governance"
            head = stem.split("-", 1)[0]  # "3.8a"
            if "." not in head:
                continue
            _, cn = head.split(".", 1)
            ctrl_nums.append(cn)

        for ctrl_num in ctrl_nums:
            control = parse_control(pillar_num, ctrl_num)
            if control:
                controls.append(control)
            else:
                errors.append(f"{pillar_num}.{ctrl_num}")

    # Validate we got all 62 controls
    if len(controls) != 62:
        print(f"\nERROR: Expected 62 controls, got {len(controls)}")
        if errors:
            print(f"  Missing: {', '.join(errors)}")
        return None

    # Validate required fields
    for ctrl in controls:
        missing = []
        for field in ["id", "pillar", "title", "objective", "verificationCriteria"]:
            val = ctrl.get(field)
            if val is None or val == "" or val == []:
                missing.append(field)
        if missing:
            print(f"  WARNING: Control {ctrl['id']} missing fields: {', '.join(missing)}")

    # Parse regulatory mappings
    reg_mappings = parse_regulatory_mappings()

    output = {
        "version": "1.0.0",
        "generatedAt": None,  # Set at write time
        "frameworkVersion": "1.1",
        "totalControls": len(controls),
        "pillars": {
            str(k): {"name": v["name"], "controlCount": v["count"]}
            for k, v in PILLARS.items()
        },
        "controls": controls,
        "regulatoryMappings": reg_mappings,
        "institutionTypes": INSTITUTION_REGULATORY_PRIORITY,
        "adoptionPhases": PHASE_CONTROLS,
        "roleAssignments": ROLE_CONTROLS,
    }

    return output


def main():
    global VERBOSE
    import argparse
    from datetime import datetime, timezone

    parser = argparse.ArgumentParser(
        description="Extract assessment data from FSI-CopilotGov controls"
    )
    parser.add_argument("--verbose", action="store_true", help="Show detailed output")
    parser.add_argument("--output", type=str, help="Output file path")
    args = parser.parse_args()

    VERBOSE = args.verbose
    output_path = Path(args.output) if args.output else OUTPUT_PATH

    print("FSI-CopilotGov Assessment Data Extraction")
    print("=" * 45)

    data = build_output()
    if data is None:
        print("\nFAILED: Could not build assessment data")
        sys.exit(1)

    data["generatedAt"] = datetime.now(timezone.utc).isoformat()

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nGenerated {output_path}")
    print(f"  Controls: {data['totalControls']}")
    print(f"  Regulations: {len(data['regulatoryMappings'])}")

    # Summary stats
    with_phase = sum(1 for c in data["controls"] if c["adoptionPhase"])
    with_levels = sum(1 for c in data["controls"] if c["levelRequirements"])
    avg_criteria = sum(len(c["verificationCriteria"]) for c in data["controls"]) / len(data["controls"])

    print(f"  Controls with adoption phase: {with_phase}")
    print(f"  Controls with governance levels: {with_levels}")
    print(f"  Avg verification criteria: {avg_criteria:.1f}")

    # Validate generated playbook URLs
    bad_urls = []
    for ctrl in data["controls"]:
        for key, url in ctrl.get("playbooks", {}).items():
            if url.endswith(".md"):
                bad_urls.append(f"  {ctrl['id']}.playbooks.{key}: {url}")
    if bad_urls:
        print(f"\nFAILED: {len(bad_urls)} playbook URLs end in .md (MkDocs uses directory URLs)")
        for b in bad_urls:
            print(b)
        sys.exit(1)

    print("\nSUCCESS")


if __name__ == "__main__":
    main()
