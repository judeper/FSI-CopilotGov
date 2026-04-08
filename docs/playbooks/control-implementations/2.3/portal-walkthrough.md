# Control 2.3: Conditional Access Policies for Copilot Workloads — Portal Walkthrough

Step-by-step portal configuration for implementing Conditional Access policies that govern access to Microsoft 365 Copilot.

## Prerequisites

- Entra ID Conditional Access Administrator or Security Administrator role
- Microsoft Entra ID P1 or P2 license
- Device compliance policies configured in Microsoft Intune
- Named locations defined for corporate network ranges
- **Action required by May 13, 2026:** If your organization uses "All resources" CA policies with exclusions, audit and remediate before the enforcement change takes effect (see Step 2)

## Steps

### Step 1: Verify Enterprise Copilot Platform App ID

**Portal:** Microsoft Entra Admin Center
**Path:** Microsoft Entra admin center > Protection > Conditional Access > Policies

Before creating or modifying any Copilot CA policy, confirm you are using the correct Enterprise Copilot Platform App ID:

- **Correct App ID:** `fb8d773d-7ef8-4ec0-a117-179f88add510`

Search existing policies for any references to the Copilot app. Use the CA optimization agent to identify policies that may need updating. A misconfigured app ID causes the policy to miss Copilot traffic entirely.

### Step 2: Audit for May 2026 CA Enforcement Change

**Portal:** Microsoft Entra Admin Center
**Path:** Microsoft Entra admin center > Protection > Conditional Access > Optimization

Starting May 13, 2026, Entra ID will enforce MFA and device compliance even for resources excluded in "All resources" policies. This closes a bypass path that previously allowed Copilot access without full enforcement.

1. Open the Conditional Access optimization agent
2. Review all policies scoped to "All resources" that include resource exclusions
3. Identify any policy that excludes the Enterprise Copilot Platform (`fb8d773d-7ef8-4ec0-a117-179f88add510`)
4. Deploy remediated policies in report-only mode to assess user impact
5. Switch remediated policies to enforcement mode at least 2 weeks before May 13, 2026

### Step 3: Create Conditional Access Policy for Copilot

**Portal:** Microsoft Entra Admin Center
**Path:** Microsoft Entra admin center > Protection > Conditional Access > New policy

Create a dedicated Conditional Access policy targeting Copilot workloads:
- **Name:** "FSI Copilot Access — Compliant Device Required"
- **Users:** Include Copilot deployment groups; exclude emergency access accounts
- **Target resources:** Enterprise Copilot Platform (App ID: `fb8d773d-7ef8-4ec0-a117-179f88add510`)
- **Conditions:** All client apps, any platform
- **Grant:** Require device compliance AND require MFA

### Step 4: Configure Device Compliance Requirements

**Portal:** Microsoft Entra Admin Center
**Path:** Microsoft Entra admin center > Protection > Conditional Access > [Policy] > Grant controls

Set grant controls requiring managed, compliant devices for Copilot access:
- Require device to be marked as compliant (Intune managed)
- Require multi-factor authentication
- Require both controls (AND operator, not OR)

This helps prevent Copilot access from unmanaged personal devices in FSI environments.

### Step 5: Define Location-Based Conditions

**Portal:** Microsoft Entra Admin Center
**Path:** Microsoft Entra admin center > Protection > Conditional Access > Named locations

Configure named locations for location-aware Copilot access:
- Define corporate office IP ranges as trusted locations
- Define VPN exit points as trusted locations
- Optionally block Copilot access from non-trusted locations for highly regulated roles

### Step 6: Configure Session Controls

**Portal:** Microsoft Entra Admin Center
**Path:** Microsoft Entra admin center > Protection > Conditional Access > [Policy] > Session controls

Add session controls for additional security:
- Sign-in frequency: Require re-authentication every 8 hours for Copilot sessions (4 hours for Regulated)
- Persistent browser session: Disable for non-compliant devices
- App-enforced restrictions: Enable for SharePoint integration
- Conditional Access App Control: Route through Defender for Cloud Apps if configured

### Step 7: Enable Adaptive Protection Integration

**Portal:** Microsoft Purview > Insider Risk Management > Adaptive Protection
**Path:** Microsoft Purview > Insider Risk Management > Adaptive Protection settings

Configure IRM Adaptive Protection to feed real-time risk signals into Conditional Access:
1. Enable Adaptive Protection in IRM settings
2. Configure risk level thresholds (Recommended: High risk triggers CA block; Regulated: Medium risk triggers CA block)
3. Return to Entra ID Conditional Access and create a policy that responds to IRM risk levels:
   - **Condition:** User risk — tied to IRM Adaptive Protection signal
   - **Grant:** Block access (Regulated) or require re-authentication (Recommended)
4. When a user's IRM risk level is elevated, the CA policy automatically restricts their next Copilot authentication without requiring manual intervention

### Step 8: Test Policy in Report-Only Mode

**Portal:** Microsoft Entra Admin Center
**Path:** Microsoft Entra admin center > Protection > Conditional Access > [Policy] > Enable policy > Report-only

Deploy the policy in report-only mode to evaluate impact before enforcement:
- Monitor the Conditional Access insights workbook for policy matches
- Review sign-in logs for users who would be blocked or challenged
- Verify no legitimate users are unexpectedly impacted
- After 1-2 weeks of clean results, switch to enforcement mode

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Require MFA for all Copilot access; compliant device required; audit CA policies for Copilot exclusions before May 2026; enable Adaptive Protection in audit mode |
| **Recommended** | Location-based restrictions; session controls with 8-hour re-auth; remove Copilot-specific exclusions from "All resources" policies and test in report-only before May 2026; enable Adaptive Protection dynamic blocking for high-risk users |
| **Regulated** | Compliant device AND MFA AND trusted location required; session controls with 4-hour re-auth and app-enforced restrictions; Defender for Cloud Apps integration; CA policy remediation complete by April 2026; Adaptive Protection dynamic blocking at medium-risk threshold |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Conditional Access automation
- See [Verification & Testing](verification-testing.md) to validate access controls
- Review Control 2.9 for Defender for Cloud Apps session controls
- Review Control 2.10 for IRM Adaptive Protection configuration
