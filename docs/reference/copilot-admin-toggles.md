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
| Self-service trials and purchases for Microsoft 365 Copilot | Settings > Org settings > Self-service trials and purchases | Allow unless disabled | Off | Off | Off | Prevents unmanaged user purchases or trials |
| PAYG billing policy | Billing > Pay-as-you-go services | Off until configured | Review | On for approved groups only | On for approved groups only | Required for metered Microsoft 365 Copilot Chat, SharePoint agents, and Retrieval API use |
| PAYG budget notifications | Billing policy / Cost Management | Off until configured | Review | Enabled | Enabled | Provides budget alerts for variable Copilot consumption |
| Cost monitoring | Cost Management | Available when PAYG is configured | Monthly review | Monthly review | Weekly review | Tracks spend, anomalies, and department allocation |

---

## Third-Party Model Provider Controls

| Control | Portal Path | Default | B | R | Reg | Impact |
|--------|------------|---------|---|---|-----|--------|
| Third-party model providers | Copilot > Settings > Other settings | Off | Off | Off | Off | Enables non-Microsoft AI models (Anthropic Claude, xAI) for Copilot experiences; introduces new data handling and residency considerations |

!!! note "Third-party models and FSI risk"
    Enabling third-party model providers introduces additional vendor risk, data residency, and model governance considerations. FSI organizations should complete a risk assessment under Control 1.10 (Vendor Risk Management) and Control 3.8 (Model Risk Management) before enabling any non-Microsoft models. The default is Off and should remain Off in Regulated environments unless a documented approval process is completed.

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
