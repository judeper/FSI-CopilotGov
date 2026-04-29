# Security Policy

## Supported Versions

This is a documentation-first governance framework. Security maintenance is
provided for the active major release line and the most recent prior minor.

| Version | Supported |
|---------|-----------|
| 1.5.x   | :white_check_mark: |
| 1.4.x   | :white_check_mark: (security fixes only) |
| < 1.4   | :x: |

The repository ships no production runtime code. The "supply chain" for this
project consists of (a) the MkDocs documentation build, (b) the Python
assessment engine and PowerShell evidence collectors under `assessment/`, and
(c) the SPA bundle under `docs/javascripts/`. Vulnerability reports against any
of these components are in scope.

## Reporting a Vulnerability

If you discover a security vulnerability in this framework — for example,
exposed credentials, insecure configuration guidance, a vulnerable dependency,
a tampered link, or a security control that is materially incorrect — please
report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Use one of the following private channels:

1. **GitHub Private Vulnerability Reporting (preferred):**
   - Navigate to the [Security tab](https://github.com/judeper/FSI-CopilotGov/security)
   - Click **Report a vulnerability**
   - Provide a description, affected files/paths, reproduction steps, and
     potential impact.
2. **Email** the repository owner directly via the address listed on the
   GitHub profile of @judeper.

When reporting, include:

- A clear description of the issue and which file/path/control it affects.
- Reproduction steps or a minimal example.
- Whether you have already disclosed the issue elsewhere (we ask for an
  embargo until a fix or mitigation is in place).
- Optionally, a suggested remediation.

## Disclosure & Response Targets

| Activity | Target |
|----------|--------|
| Acknowledge receipt of report | within 2 business days |
| Initial triage / severity rating | within 5 business days |
| Fix or documented mitigation for High/Critical | within 30 days |
| Coordinated public disclosure | after fix is released, or 90 days from report (whichever is sooner) |

We follow [coordinated vulnerability disclosure](https://www.cisa.gov/coordinated-vulnerability-disclosure-process)
practices. Reporters who follow this policy will be credited in the changelog
and release notes unless they request anonymity.

## Scope

This security policy covers:

- **Configuration guidance** — playbooks, controls, or reference docs that
  recommend insecure configuration.
- **Credential exposure** — files containing live secrets, API keys, tokens,
  or service-principal credentials.
- **Vulnerable dependencies** — Python (`pip`), npm, or GitHub Actions
  components used by this repo's tooling.
- **Static-analysis findings** — Bandit (Python), PSScriptAnalyzer
  (PowerShell), CodeQL, or `npm audit` findings against repo-owned code.
- **Incorrect regulatory guidance** — security-relevant regulatory citations
  that are materially incorrect in a way that could lead to insecure
  deployments.
- **Link integrity** — external links that redirect to malicious or
  unintended destinations.
- **Supply-chain provenance** — issues with the SBOM, release artifacts, or
  generated `controls.json` / `content-graph.json`.

## Out of Scope

- Vulnerabilities in **Microsoft 365 Copilot itself**. Report those to
  Microsoft via the [Microsoft Security Response Center](https://msrc.microsoft.com/).
- Vulnerabilities in **third-party services or libraries** that this
  framework merely references (e.g., Microsoft Purview, Microsoft Sentinel,
  Power Platform). Report those upstream.
- Vulnerabilities in the **companion repositories** ([FSI-AgentGov](https://github.com/judeper/FSI-AgentGov),
  [FSI-CopilotGov-Solutions](https://github.com/judeper/FSI-CopilotGov-Solutions)).
  Use the security policy of those repos.
- Tenant configuration of an organization's own M365/Copilot deployment.

## Hardening Posture

The repository runs the following security hygiene in CI (see
`.github/workflows/`):

- **CodeQL** — Python + JavaScript SAST on every push/PR and weekly.
- **Security scan** — `pip-audit`, `bandit`, `npm audit`, and
  `Invoke-ScriptAnalyzer` against the PowerShell collectors.
- **Dependabot** — weekly dependency updates for `pip`, `npm`, and
  `github-actions`.
- **SBOM** — SPDX-JSON generated on each docs publish via
  `anchore/sbom-action` and attached to the GitHub Pages deploy artifact.
- **CODEOWNERS** — `/.github/CODEOWNERS` requires owner review for changes
  to security-sensitive paths (workflows, dependabot config, SECURITY.md).

## Disclaimer

This framework provides governance guidance for Microsoft 365 Copilot and
does not include executable production code, APIs, or services. Findings
about the regulatory accuracy or completeness of specific controls should be
filed as standard issues unless they have direct security implications.
