# Control 2.14: Declarative Agents from SharePoint Governance — Troubleshooting

Common issues and resolution steps for declarative, SharePoint-backed, and Registry-governed agent security.

## Common Issues

### Issue 1: Users Creating Agents Without Governance Approval

- **Symptoms:** Declarative agents discovered in the tenant without governance approval or documentation
- **Root Cause:** Agent creation restrictions may not be properly configured, or users may have found alternative creation paths.
- **Resolution:**
  1. Review agent settings in Admin Center > Agents > Settings
  2. Restrict creation to approved security groups
  3. Audit existing agents and require retroactive governance approval
  4. Set up monitoring (Script 3) to detect new agent creation

### Issue 2: Agent Accessing Overshared Source Content

- **Symptoms:** A declarative agent returns sensitive content that the querying user should not have access to
- **Root Cause:** The agent's source SharePoint site has oversharing — content is accessible to more users than intended.
- **Resolution:**
  1. Immediately restrict the source site sharing settings
  2. Run an oversharing assessment (Control 1.2) on the source site
  3. Remediate permissions before re-enabling the agent
  4. Consider suspending the agent until remediation is complete

### Issue 3: Agent Providing Inaccurate or Stale Responses

- **Symptoms:** Agent responses reference outdated content or provide incorrect information
- **Root Cause:** Source content may be outdated, or the semantic index may not have processed recent updates to the source site.
- **Resolution:**
  1. Verify source content is current and accurately maintained
  2. Request a re-index of the source site if recent updates are not reflected
  3. Add content freshness indicators to the agent description
  4. Establish a content review cadence for agent source sites

### Issue 4: Agent Governance Process Slowing Deployment

- **Symptoms:** Business teams report agent approval takes too long
- **Root Cause:** Governance process may be overly complex for low-risk agents.
- **Resolution:**
  1. Create tiered governance based on data sensitivity and audience scope
  2. Fast-track agents referencing already-approved, properly governed sites
  3. Pre-approve common agent patterns with standardized templates
  4. Define clear SLAs for governance review

### Issue 5: Third-Party Model Provider Enabled Without Governance Approval

- **Symptoms:** Agents are using non-Microsoft AI model providers to process organizational data without the compliance team's knowledge.
- **Root Cause:** The third-party model provider setting in the M365 Admin Center was enabled without governance review. By default this setting is disabled, but it may have been enabled during initial configuration.
- **Resolution:**
  1. Review the third-party model provider setting in M365 Admin Center > Copilot > Settings.
  2. If enabled without governance approval, disable it immediately and notify the compliance team.
  3. Audit whether any agents used third-party model providers while the setting was enabled — review audit logs for non-Microsoft model invocations.
  4. Complete a vendor risk assessment for any third-party model provider before re-enabling.
  5. Document the approved third-party model provider policy and communicate to agent creators.

## Diagnostic Steps

1. **Check agent inventory:** Review Admin Center > Agents > All agents / Registry (or Agent 365 dashboard)
2. **Verify source security:** Run Script 2 on agent data sources
3. **Review creation policies:** Verify agent creation restrictions in admin settings
4. **Check third-party model providers:** Verify the setting is disabled in M365 Admin Center > Copilot > Settings
5. **Monitor activity:** Run Script 3 for recent agent events
6. **Test agent scope:** Query the agent to verify content boundaries

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|----------------|
| **Low** | Governance process improvement needed | Governance team |
| **Medium** | Unauthorized agent creation detected | Security Operations for review |
| **High** | Agent exposing sensitive content | Security Operations and site owner |
| **Critical** | Regulated data exposed through ungoverned agent | CISO and Compliance Officer immediately |

## Related Resources

- [Portal Walkthrough](portal-walkthrough.md) — Agent governance configuration
- [PowerShell Setup](powershell-setup.md) — Agent management scripts
- [Verification & Testing](verification-testing.md) — Governance validation
