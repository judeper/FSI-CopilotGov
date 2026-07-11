# Copilot Admin Toggles

Current inventory of the highest-value Microsoft 365 Copilot administrative controls for FSI governance. This reference focuses on the settings surfaces that materially affect Copilot access, grounding, agents, billing, and Copilot Pages / Copilot Notebooks.

!!! warning "Disclaimer"
    This framework is provided for informational purposes only and does not constitute legal, regulatory, or compliance advice. See [full disclaimer](../disclaimer.md).

---

## How to Use This Reference

- **Default** = Microsoft's out-of-box or service default behavior when documented
- **Baseline (B)** = Minimum FSI governance recommendation
- **Recommended (R)** = Best practice for most FSI production environments
- **Regulated (Reg)** = Stricter control posture for higher-risk deployments
- Paths are current as of April 2026; Microsoft can move or relabel controls by license, region, and rollout stage

---

## Primary Admin Surfaces

| Surface | Primary Path | Why It Matters |
|---------|--------------|----------------|
| Copilot overview | M365 Admin Center > Copilot > Overview | Readiness, adoption, security links, and recommended actions |
| Copilot settings | M365 Admin Center > Copilot > Settings | Tenant controls grouped under User access, Data access, Copilot actions, and Other settings |
| Agents | M365 Admin Center > Agents > Overview / All agents / Settings | Agent inventory, sharing, templates, and user access |
| Billing and cost | M365 Admin Center > Billing > Pay-as-you-go services / Cost Management | PAYG setup, billing policies, budgets, and spend visibility |
| Copilot Pages / Notebooks policy | `https://config.office.com` > Customization > Policy Management | Cloud Policy controls for creation and code previews |

---

## Tenant Access and Billing Controls

| Control | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Microsoft 365 Copilot access | Copilot > Settings > User access | On for licensed users | On for approved users/groups | On for approved users/groups | On for approved users/groups | Primary control for who can use Copilot scenarios; note that Copilot Chat (Basic) is available to all M365 users via web and Outlook regardless of this toggle — this controls Premium (paid) Copilot access |
| Edit with Copilot (Agent Mode) | Copilot > Settings > User access (when available) | On for all users | Review | Review | Review or Off | Available to all M365 users regardless of Copilot license; uses web data only for unlicensed users — review whether to restrict for regulated populations |
| Copilot Cowork — usage-based billing | Copilot > Cost management (usage-based billing on Copilot Credits) | Off until configured | Review | On for approved groups only | On for approved groups with documented use-case inventory | Cowork reached general availability in June 2026; access is now gated by usage-based billing on Copilot Credits (model responses, tools/skills, image generation, browser tasks). Enable per approved group after cost governance is in place. |
| Copilot Cowork — discovery | Copilot > Settings > AI experiences enabled by usage-based billing | Off until configured | Off | On for approved groups only | Off unless a request-to-enable workflow exists | Discovery lets users request access when billing is not yet enabled for them; keep off for groups where request-based onboarding is not desired. |
| Copilot Cowork — Anthropic model family | Copilot > Settings > View all > Cowork settings (model policy) | Enabled | Review | Review — document acceptance of Claude Opus 4.8, Sonnet 5, Advisor pairing | Review — restrict Claude Fable 5 (Preview) and Anthropic family per model-risk decision | Cowork ships Claude Opus 4.8, Sonnet 5, a Sonnet+Opus Advisor pairing, GPT 5.5, Imagen 2, and Claude Fable 5 (Preview, off by default and requires provider data retention). Admins can disable the Anthropic model family. |
| Copilot Cowork — Cowork Browsing (local browser) | Copilot > Settings > View all > Cowork settings > Allow browser access | Off | Off during pilot | Review per group — depends on browser management policy and site allow/block/view-only rules | Off unless a documented decision exists | When on, Cowork drives the user's local Microsoft Edge and inherits Conditional Access, Purview DLP, browser management policy, and site allow/block/view-only rules; every browser task is recorded in the unified audit log. |
| Microsoft Scout (Frontier preview) — Frontier scoping | Copilot > Settings > View all > Copilot Frontier (No access / All users / Specific users) | Off for the tenant until enrolled | Off during pilot planning | Scoped to approved pilot group only | Scoped to approved pilot group only | First of three independent admin gates. Frontier scoping selects which users and admin accounts in the tenant have Frontier access; Scout admin surfaces and user entitlement only resolve after Frontier is enabled and change propagation completes (Microsoft cites up to about three hours). |
| Microsoft Scout (Frontier preview) — endpoint policy (**Allow Microsoft Scout Frontier access**) | Intune (or equivalent MDM): imported Windows ADMX/ADML (`microsoft-scout.admx` / `.adml`, **Microsoft Scout > Capabilities > Allow Microsoft Scout Frontier access**, i.e. `AllowScoutFrontierAccess`); macOS `.mobileconfig` custom device profile | Not deployed | Not deployed | Deployed to approved device groups only | Deployed to approved device groups only, with documented device-group scope | Second admin gate. Combined with the admin attestation and opt-in step (Microsoft's Frontier organization sign-up form); installing the Scout app alone grants nothing. See [Control 4.16](../controls/pillar-4-operations/4.16-microsoft-scout-governance.md). |
| Microsoft Scout — endpoint installation privilege | Endpoint / Intune app deployment; `microsoft-scout` installer requires local Administrator permissions to install (per Microsoft's [Get started with Microsoft Scout](https://learn.microsoft.com/microsoft-scout/get-started)) | User-driven install requires local admin | Prefer system-context managed deployment (Intune) so users never need local admin | System-context managed deployment (Intune) or just-in-time elevation; standing local admin not granted for installation | System-context managed deployment (Intune) or just-in-time elevation with documented exception, compensating controls, and duration; standing local admin not granted for installation | Install-time privilege is distinct from ongoing use privilege. Do not grant permanent local Administrator rights to end users solely to install Scout. |
| Microsoft Scout (Frontier preview) — GitHub Copilot entitlement | GitHub — user must hold a **GitHub Copilot Business or Enterprise** entitlement on a linked GitHub account | No default | Reconciled to approved pilot list | Reconciled to approved pilot list; not entitled outside the pilot | Reconciled to approved pilot list; not entitled outside the pilot | Third admin gate. Determines whether an individual user can sign in to Scout after Frontier scoping and endpoint policy are in place. Users also need an active Microsoft 365 Copilot license — see [Control 1.9 License Planning](../controls/pillar-1-readiness/1.9-license-planning.md). |
| Microsoft Scout — Windows ADMX admin controls (documented policy settings under `HKLM\SOFTWARE\Policies\Scout`) | Intune Windows ADMX policy: `DisabledServers`, `DisabledPermissions`, `ForcePrompt`, `DisabledModels`, `DisabledProviders`, `DisableHeartbeat`, `DisableWorkflows`, `RestrictToWorkspace`, `BrowserEgressBlockedOrigins`, `PolicyVersion` | Verify each setting's shipped default against current [Microsoft documentation](https://learn.microsoft.com/microsoft-scout/manage-group-policy) before pilot | Pilot posture documented for each setting with citation to current Microsoft docs; where feasible, `ForcePrompt` on and `DisabledServers` / `DisabledPermissions` reflect the pilot's approved-MCP inventory | Pilot posture documented; `ForcePrompt` on for non-read tool actions; `DisabledServers` / `DisabledPermissions` reflect approved-MCP inventory; `DisableWorkflows` on unless a separate unattended-execution decision exists; `RestrictToWorkspace` on unless a documented broader-scope decision exists; `BrowserEgressBlockedOrigins` reflects the approved browser destination posture | All Recommended settings, plus `DisabledProviders` / `DisabledModels` reflect the third-party-inference exclusion decision; `DisableHeartbeat` reviewed against monitoring/telemetry posture; policy snapshots retained as evidence | Device-scoped policy; standard users can't modify. Verify names and defaults against current Microsoft documentation before treating as configured evidence. |
| Microsoft Scout — shell command permission mode | Scout endpoint app (per-command permission modes: auto-approve / prompt / deny) | Verify Microsoft's shipped default against current Scout documentation before pilot | Prompt (pilot default); where feasible, backed by the documented `ForcePrompt` ADMX setting | Prompt; any auto-approve list is explicitly approved and low-risk; where feasible, backed by `ForcePrompt` | Prompt; do not auto-approve destructive commands; `ForcePrompt` on where feasible | Auto-approve is an elevated permission with material blast-radius implications; document and approve the default posture and any auto-approve list. |
| Microsoft Scout — autonomous modes | Scout endpoint app (autonomous mode settings) | Off / opt-in per session | Off during pilot | Off unless separately approved low-risk scoping decision exists | Off — do not enable for regulated populations without a separately approved low-risk scoping decision covering workspace, shell, browser, network, and M365 scope | Optional autonomous modes relax approval friction and are a higher-risk governance decision. |
| Microsoft Scout — unattended (scheduled/triggered) automations | Scout endpoint app (automations) | Off / opt-in per automation | Off during pilot | Off unless separately approved | Off — do not permit unattended execution for regulated populations without a separately approved decision | Unattended execution should be a distinct, explicit governance decision — do not treat it as included by default. |
| Microsoft Scout — MCP-server inventory | Approved-MCP-server inventory (out-of-portal governance artifact); Scout endpoint app manages installed MCP servers | No inventory by default | Documented inventory | Approvals capture data path, authentication, and external egress | Approvals capture data path, authentication, and external egress; documented as extensibility under [Control 4.13](../controls/pillar-4-operations/4.13-extensibility-governance.md) and MCP governance under [Control 2.16](../controls/pillar-2-security/2.16-federated-connector-mcp-governance.md) | MCP servers are third-party extensibility; treat MCP output stored locally as outside the M365 DPA. |
| Microsoft 365 Copilot Search | Copilot > Settings > User access; Settings > Search & intelligence | On for licensed users | On for approved groups | On for approved groups | On for approved groups | AI-enriched search within the Copilot app; grounding scope governed by Restricted SharePoint Search configuration |
| Copilot Tuning (preview) | Copilot > Settings > View all > Copilot Tuning | Off until eligible tenant opts in | Off | Review — document risk assessment | Review — requires model-risk inventory entry (Control 3.8) | Available only to tenants with 5,000+ Copilot licenses during preview; requires explicit admin activation, tuning corpus review, and model-risk documentation |
| Self-service trials and purchases for Microsoft 365 Copilot | Settings > Org settings > Self-service trials and purchases | Allow unless disabled | Off | Off | Off | Prevents unmanaged user purchases or trials |
| PAYG billing policy | Billing > Pay-as-you-go services | Off until configured | Review | On for approved groups only | On for approved groups only | Required for metered Microsoft 365 Copilot Chat, SharePoint agents, and Retrieval API use |
| PAYG budget notifications | Billing policy / Cost Management | Off until configured | Review | Enabled | Enabled | Provides budget alerts for variable Copilot consumption |
| Cost monitoring | Cost Management | Available when PAYG is configured | Monthly review | Monthly review | Weekly review | Tracks spend, anomalies, and department allocation |

---

## Third-Party Model Provider Controls

| Control | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Anthropic models (Microsoft subprocessor) | Copilot > Settings > View all > AI providers operating as Microsoft subprocessors | On for most commercial-cloud tenants (excluding EU/EFTA and UK, where it is Off and opt-in) | Review and document decision; restrict via user/group access if enabled | Restrict to approved users or groups; document data flow and DPIA impact | Off unless a documented Control 1.10 / Control 3.8a exception is approved | Anthropic is a Microsoft 365 Copilot subprocessor since January 7, 2026 (full availability expected by end of March 2026). Anthropic models are provided under the Microsoft Product Terms and DPA, but are **out of scope for the EU Data Boundary and in-country LLM processing commitments**. Available across Microsoft 365 Copilot, Researcher, Copilot Studio, Power Platform, Agent Mode in Excel, and Word/Excel/PowerPoint agents. |
| xAI models (independent provider) | Copilot > Settings > View all > AI providers for other large language models | Off (opt-in only) | Off | Off | Off | xAI is hosted by xAI **outside Microsoft-managed environments and audit controls**. Microsoft Product Terms, DPA, data residency commitments, audit and compliance requirements, SLAs, and the Customer Copyright Commitment **do not apply**; usage is governed by xAI's separate Terms of Service and Data Processing Addendum. Currently scoped to Copilot Studio. |

!!! warning "Third-party models and FSI risk"
    Anthropic and xAI are governed under different commercial frameworks and require separate FSI risk decisions:

    - **Anthropic** is a Microsoft subprocessor under the Microsoft Product Terms and DPA, but is excluded from the EU Data Boundary and in-country LLM processing commitments. Even though Anthropic is on by default for most US commercial-cloud tenants, FSI organizations should still complete a Control 1.10 (Vendor Risk Management) and Control 3.8a (Generative AI Model Governance) review, document the residency posture, and decide whether to restrict access by user or group. EU/EFTA and UK tenants receive the toggle Off by default and may need to opt in deliberately if business requires it.
    - **xAI** is an independent provider — data shared with xAI is processed outside Microsoft-managed environments. The Microsoft DPA, data residency commitments, and Customer Copyright Commitment do not apply. xAI should remain Off in Regulated FSI environments unless a documented vendor risk and legal review (Control 1.10, Control 3.8a) and a separate xAI Data Processing Addendum review are completed first. Grok-4.1 Fast (Non-Reasoning) is identified by Microsoft as Experimental and is not recommended for production use.

    Confirm the current toggle state for each tenant region — Microsoft enables and disables Anthropic on a phased rollout per region, and the default state may differ across commercial-cloud and EU/EFTA/UK tenants.

---

## Data Access and Grounding Controls

| Control | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Web search in Copilot | Copilot > Settings > Data access > Web search | On | Off | Off by default, exceptions documented | Off | Controls Bing/public web grounding in Copilot responses |
| Search in the Copilot app | Settings > Search & intelligence | On | On | On | Review | Controls Microsoft Search experiences surfaced in the Copilot app |
| Graph connectors / external knowledge sources | Settings > Integrated apps, Search admin center, or agent-specific configuration | Varies | Review | Review | Off until approved | Expands the data available to Copilot or agents |
| Domain exclusion for web grounding | Copilot > Settings > Data access > Web search > Domain exclusion | None configured | Review | Configure for competitor and unverified sources | Configure and review quarterly | Blocks specific external domains from Copilot web grounding responses |

---

## Security Baseline

| Control | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Baseline Security Mode | Settings > Org Settings > Security & Privacy > Baseline Security Mode | Off (opt-in) | On (simulation first) | On | On | Enforces minimum security baseline across 18-20 settings for Office, Exchange, Teams, SharePoint, Entra |

---

## Copilot Pages and Copilot Notebooks

| Control | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Create and view Copilot Pages and Copilot Notebooks | Cloud Policy > Create and view Copilot Pages and Copilot Notebooks | Enabled | Review / approved groups only | Approved groups only | Review or disable for high-risk populations | Governs whether users can create these SharePoint Embedded-backed artifacts |
| Code previews in Copilot Chat and Copilot Pages | Cloud Policy > Enable code previews for AI-generated content in Microsoft 365 Copilot Chat and Copilot Pages | Enabled | Off | Review | Off | Controls embedded code preview execution experiences |
| Retention coverage | Purview > Data lifecycle management > Retention policies > All SharePoint Sites | Not automatic | On | On | On | Copilot Pages / Notebooks are stored in SharePoint Embedded, not OneDrive |
| eDiscovery / legal hold workflow | Purview eDiscovery + manual SharePoint Embedded container targeting | Manual | Document | Test | Test quarterly | Legal hold requires manual container handling per user |

!!! note "Pages storage correction"
    Copilot Pages and Copilot Notebooks are stored in user-owned **SharePoint Embedded** containers that also support Loop My workspace. They are not governed as standard OneDrive storage even though the cleanup lifecycle resembles OneDrive after user departure.

---

## Agents and Extensibility

| Control | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Allowed agent types | Agents > Settings > Allowed agent types | Microsoft, org, and external agent types can be available | Microsoft only or approved org agents | Microsoft plus approved org/partner agents | Minimum approved types only | Controls which classes of agents users can install |
| Agent sharing | Agents > Settings > Sharing | Varies by agent type | Restrict broad sharing | Approved groups only | Restricted with documented exceptions | Governs who can share Agent Builder agents broadly in the tenant |
| Agent user access | Agents > Settings > User access | All users | Approved groups only | Approved groups only | Approved groups only | Limits who can access agents at all |
| Agent Registry lifecycle review | Agents > All agents / Registry | Available | Monthly | Monthly | Weekly | Inventory, block, publish, assign owner, or remove agents |
| Integrated apps / plugins | Settings > Integrated apps | Available | Off unless approved | Review | Off unless approved | Governs add-ins, plugins, and integrated app deployment |
| Agent pinning | Copilot > Agents > Manage pinned agents | No agents pinned | Review | Pin sanctioned agents for approved groups | Pin sanctioned agents; document pinning policy | Controls which agents are prominently surfaced to users; up to 3 per user |

!!! note "Researcher and Analyst nuance"
    Researcher and Analyst coexist with agents and inherit agent-related governance capabilities, but Microsoft documents them as part of the core Copilot chat experience. They do **not** fall under agent-related settings in the same way as installable agents.

---

## Workload-Specific Controls

| Workload | Primary Path | FSI Note |
|----------|--------------|----------|
| Teams meetings | Teams admin center > Meetings > Meeting policies | Review recap, transcript, and in-meeting Copilot availability |
| Teams chat and channels | Teams admin center > Messaging policies | Pair Copilot availability with supervision and DLP controls |
| Outlook, Word, Excel, PowerPoint | Copilot > Settings > User access plus workload-specific admin controls when surfaced | Validate rollout by user group and regulated use case |
| Viva Insights analytics | Viva Insights / role assignment | Limit access to designated analysts and governance personnel |

---

## Implementation Notes

1. Prefer **AI Administrator** for Copilot and agent administration. Use **M365 Global Admin** only where Microsoft still requires broader privileges.
2. Use **Global Reader** for read-only review and evidence collection where possible.
3. Cloud Policy changes can take up to 90 minutes when policies already exist and up to 24 hours in new policy scenarios.
4. New Copilot and agent settings continue to appear over time. Review Message Center updates and re-check this control surface monthly.
