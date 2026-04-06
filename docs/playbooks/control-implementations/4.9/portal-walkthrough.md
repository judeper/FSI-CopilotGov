# Control 4.9: Incident Reporting and Root Cause Analysis — Portal Walkthrough

Step-by-step portal configuration for establishing incident reporting and root cause analysis procedures for Copilot-related incidents in financial services environments.

## Prerequisites

- **Role:** Purview Compliance Admin, IT Security Administrator
- **License:** Microsoft 365 E5 with Copilot add-on, Microsoft Sentinel (recommended)
- **Access:** Microsoft Purview, Microsoft Defender portal

## Steps

### Step 1: Define Copilot Incident Categories

**Portal:** Internal incident management system / Microsoft Purview
**Path:** Organization incident classification framework

1. Define incident categories specific to Copilot usage:
   - **Data exposure** — Copilot surfaces sensitive data to unauthorized users
   - **Content accuracy** — Copilot generates materially incorrect financial information
   - **Compliance violation** — Copilot-assisted communication violates regulatory requirements
   - **Unauthorized usage** — Copilot used outside approved scope or by unauthorized users
   - **Service disruption** — Copilot service outage affecting business operations
2. Assign severity levels (Critical, High, Medium, Low) per category.
3. Document the classification criteria in the incident response playbook.

### Step 2: Configure Alert Policies for Copilot Incidents

**Portal:** Microsoft Purview portal
**Path:** Policies > Alert policies

1. Create alert policies for Copilot-specific incidents:
   - **Unusual Copilot activity volume** — Threshold: 500+ interactions per user per day
   - **DLP violation in Copilot** — Trigger: DLP policy match in Copilot interaction
   - **Copilot access from restricted location** — Trigger: Conditional access failure for Copilot
2. Set alert severity aligned with the incident categories.
3. Configure notification recipients: IT Security team, Compliance team.
4. Enable real-time alerts for Critical and High severity incidents.

### Step 3: Establish Root Cause Analysis Workflow

**Portal:** Internal workflow / Microsoft Purview
**Path:** Incident investigation workflow

1. Create a standard RCA template for Copilot incidents:
   - Incident timeline (detection, containment, resolution)
   - Impact assessment (users affected, data exposed, regulatory implications)
   - Root cause identification (configuration, user error, model behavior, system failure)
   - Corrective actions (immediate, short-term, long-term)
   - Lessons learned and preventive measures
2. Assign RCA ownership to the incident response team.
3. Set RCA completion deadlines: 5 business days for High, 10 for Medium, 30 for Low.

### Step 4: Configure Regulatory Notification Workflow

**Portal:** Internal compliance workflow
**Path:** Regulatory notification procedures

1. Document when Copilot incidents require regulatory notification:
   - Data breach affecting customer NPI — notify per SEC Reg S-P, state breach notification laws
   - Supervisory system failure — assess FINRA 4530 reporting obligation
   - Material compliance violation — assess self-reporting obligations
2. Establish notification timelines per regulatory requirement.
3. Assign the Chief Compliance Officer as the approval authority for regulatory notifications.

## FSI Recommendations

| Setting | Baseline | Recommended | Regulated |
|---------|----------|-------------|-----------|
| Incident categories | Generic IT | Copilot-specific | Copilot-specific with regulatory mapping |
| Alert response time | 24 hours | 4 hours | 1 hour for Critical |
| RCA completion | 30 days | 10 business days | 5 business days for High |
| Regulatory notification review | As needed | Documented workflow | Documented with CCO approval |

## Regulatory Alignment

- **FINRA Rule 4530** — Supports compliance with incident reporting obligations
- **SEC Reg S-P** — Helps meet breach notification requirements
- **FFIEC IT Handbook** — Supports IT incident response and root cause analysis requirements

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for incident detection automation
- See [Verification & Testing](verification-testing.md) to validate incident response
