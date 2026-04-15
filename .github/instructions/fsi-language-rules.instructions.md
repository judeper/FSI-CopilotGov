---
applyTo: "docs/**/*.md"
---

# FSI Regulatory Language Rules

When writing or editing documentation in this repository, follow these mandatory language guidelines to avoid legal liability.

## Prohibited Phrases (NEVER use)

| Prohibited | Risk |
|-----------|------|
| "ensures compliance" | Implies legal guarantee |
| "guarantees" | Creates liability |
| "will prevent" | Overclaim |
| "eliminates risk" | Unrealistic |

## Required Alternatives (ALWAYS use)

| Use This | Instead Of |
|----------|-----------|
| "supports compliance with" | "ensures compliance with" |
| "helps meet" | "guarantees compliance" |
| "required for" | "will ensure" |
| "recommended to" | "guarantees" |
| "aids in" | "eliminates the need for" |

## Examples

```markdown
# WRONG
This control ensures you meet SEC 17a-4 requirements.

# RIGHT
This control helps support SEC 17a-4 requirements. Implementation requires...
```

```markdown
# WRONG
Enabling audit logging guarantees regulatory compliance.

# RIGHT
Enabling audit logging aids in meeting regulatory record-keeping requirements. Organizations should verify configuration meets their specific obligations.
```

## Additional Rules

- Include implementation caveats where appropriate ("Implementation requires...", "Organizations should verify...")
- Reference specific regulations by name and section (e.g., "FINRA Rule 4511(a)")
- Do not claim that any single control satisfies a regulation in isolation
- Use "supports", "contributes to", "helps address" for regulatory mapping language

## Regulatory Citation Accuracy

Use validated citations to avoid legal/regulatory errors:

| Use This | NOT This | Reason |
|----------|----------|--------|
| OCC Bulletin 2023-17 | OCC Bulletin 2013-29 | 2013-29 was rescinded/superseded |
| GLBA §501(b) | GLBA Safeguards Rule | FTC Safeguards Rule is wrong authority for banks/broker-dealers |
| SR 11-7 / OCC Bulletin 2011-12 | OCC SR 11-7 | SR 11-7 is Federal Reserve; OCC counterpart is Bulletin 2011-12 |
| 12 CFR part 30, appendix D (OCC Heightened Standards) | OCC Heightened Standards | Use formal regulatory citation |
| FINRA Rule 3110 — supervisory systems/WSPs | FINRA Rule 3110 — access controls | 3110 is a supervision rule, not an access-control mandate |
| SOX §§302/404 — where applicable to ICFR | SOX 302/404 — blanket claims | Only applies where AI tools affect financial reporting |
| SEC Rule 17a-4 — required records only | SEC Rule 17a-4 — all artifacts | Applies to specific broker-dealer records, not all logs |

## Role Naming

Use canonical short names:

| Use This | NOT This |
|----------|----------|
| Entra Global Admin | Global Administrator |
| Purview Compliance Admin | Compliance Administrator |
| M365 Global Admin | Microsoft 365 Admin |
| Exchange Online Admin | Exchange Administrator |
| SharePoint Admin | SharePoint Administrator |
| Teams Admin | Teams Administrator |
