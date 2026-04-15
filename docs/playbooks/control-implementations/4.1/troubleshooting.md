# Control 4.1: Copilot Admin Settings and Feature Management — Troubleshooting

Common issues and resolution steps for Copilot administrative settings, agent governance, Cloud Policy, and billing controls.

## Common Issues

### Issue 1: Copilot Features Available to Unauthorized Users

- **Symptoms:** Users outside the approved population can access Copilot features.
- **Root Cause:** License assignment or Copilot user access settings don't align with the approved group model.
- **Resolution:**
  1. Review license assignment and Copilot user access together.
  2. Compare the effective user population with the approved rollout list.
  3. Remove direct assignments or incorrect group membership.

### Issue 2: Overview Dashboard Not Showing All Data

- **Symptoms:** Copilot overview is blank or incomplete.
- **Root Cause:** Reporting data is still populating or the reviewer lacks the necessary role.
- **Resolution:**
  1. Verify the reviewer has **AI Administrator** or **Global Reader** access as appropriate.
  2. Allow time for data population after major rollout or license changes.
  3. Confirm privacy settings are not suppressing the expected reporting view.

### Issue 3: Web Search Appears Enabled After It Was Disabled

- **Symptoms:** Users still receive web-grounded responses.
- **Root Cause:** Data access settings were changed, or the policy has not fully propagated.
- **Resolution:**
  1. Recheck **Copilot > Settings > Data access**.
  2. Review recent admin changes in the audit log.
  3. Validate behavior with a controlled user test after propagation time.

### Issue 4: Agent Controls Do Not Match the Approved Policy

- **Symptoms:** Users can install or share agents beyond the approved scope.
- **Root Cause:** Agent settings, registry state, or specific agent assignments were changed without updating the baseline.
- **Resolution:**
  1. Review **Agents > Settings** for allowed types, sharing, and user access.
  2. Review **Agents > All agents** for blocked, published, or ownerless agents.
  3. Update the governance register and correct any unauthorized settings.

### Issue 5: Copilot Pages Are Still Available After Being Disabled

- **Symptoms:** Users can still view or work with existing Pages after the Cloud Policy was changed.
- **Root Cause:** The policy blocks new creation but doesn't delete existing content, and policy propagation can take time.
- **Resolution:**
  1. Review the Cloud Policy scope and priority.
  2. Allow for Microsoft-documented propagation timing.
  3. Confirm whether Loop policy settings still permit the shared SharePoint Embedded container to exist.

### Issue 6: PAYG Costs Appear Without a Clear Owner

- **Symptoms:** Metered Copilot usage is visible but not tied to the expected department or billing policy.
- **Root Cause:** Billing policy scope or documentation is incomplete.
- **Resolution:**
  1. Review **Billing > Pay-as-you-go services**.
  2. Validate which users or groups are tied to each billing policy.
  3. Review **Cost Management** and update cost-owner documentation.

### Issue 7: Baseline Security Mode Conflicts with Existing Controls

- **Symptoms:** Organization-wide baseline settings overlap with existing custom security controls.
- **Root Cause:** Baseline Security Mode was treated as a direct replacement for Copilot-specific controls.
- **Resolution:**
  1. Review **Settings > Org settings > Security & privacy**.
  2. Compare baseline settings to the existing Purview, Conditional Access, and workload controls.
  3. Document which control is authoritative when overlap exists.

## Diagnostic Steps

1. **Check role assignments:** Confirm AI Administrator, Global Reader, and broader roles are assigned appropriately.
2. **Review Copilot settings:** Inspect **Copilot > Settings** across all current tabs.
3. **Review agent settings:** Inspect **Agents > Settings** and **All agents**.
4. **Review Cloud Policy:** Confirm Copilot Pages / Notebooks policy scope and priority.
5. **Review billing posture:** Inspect self-service purchase settings and any active PAYG policies.
6. **Audit recent changes:** Search for recent Copilot, agent, or billing changes in audit logs.

## Escalation

| Severity | Condition | Escalation Path |
|----------|-----------|-----------------|
| Critical | Unauthorized Copilot or agent access to sensitive data | IT Security + Compliance |
| High | Web search enabled in a regulated deployment | AI Administrator + Compliance |
| High | PAYG or self-service path active without approval | IT Finance + Governance Owner |
| Medium | Cloud Policy not reflecting expected Pages restrictions | Office Apps admin / SharePoint Admin |
| Medium | Overview or agent dashboard data unavailable | AI Administrator |
| Low | Evidence or documentation gaps | Governance Program Manager |

## Related Resources

- [Control 4.2: Copilot in Teams Meetings Governance](../4.2/portal-walkthrough.md)
- [Control 4.12: Change Management for Copilot Rollouts](../4.12/portal-walkthrough.md)
- Back to [Control 4.1](../../../controls/pillar-4-operations/4.1-admin-settings-feature-management.md)
