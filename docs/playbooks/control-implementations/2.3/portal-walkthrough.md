# Control 2.3: Conditional Access Policies for Copilot Workloads — Portal Walkthrough

Step-by-step portal configuration for implementing Conditional Access policies that govern access to M365 Copilot.

## Prerequisites

- Entra ID Conditional Access Administrator or Security Administrator role
- Microsoft Entra ID P1 or P2 license
- Device compliance policies configured in Microsoft Intune
- Named locations defined for corporate network ranges

## Steps

### Step 1: Create Conditional Access Policy for Copilot

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > Create New Policy

Create a dedicated Conditional Access policy targeting Copilot workloads:
- **Name:** "FSI Copilot Access — Compliant Device Required"
- **Users:** Include Copilot deployment groups; exclude emergency access accounts
- **Target resources:** Office 365 (covers all Copilot-enabled workloads)
- **Conditions:** All client apps, any platform
- **Grant:** Require device compliance AND require MFA

### Step 2: Configure Device Compliance Requirements

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > [Policy] > Grant controls

Set grant controls requiring managed, compliant devices for Copilot access:
- Require device to be marked as compliant (Intune managed)
- Require multi-factor authentication
- Require both controls (AND operator, not OR)

This helps prevent Copilot access from unmanaged personal devices in FSI environments.

### Step 3: Define Location-Based Conditions

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > Named locations

Configure named locations for location-aware Copilot access:
- Define corporate office IP ranges as trusted locations
- Define VPN exit points as trusted locations
- Optionally block Copilot access from non-trusted locations for highly regulated roles

### Step 4: Configure Session Controls

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > [Policy] > Session controls

Add session controls for additional security:
- Sign-in frequency: Require re-authentication every 8 hours for Copilot sessions
- Persistent browser session: Disable for non-compliant devices
- App-enforced restrictions: Enable for SharePoint integration
- Conditional Access App Control: Route through Defender for Cloud Apps if configured

### Step 5: Test Policy in Report-Only Mode

**Portal:** Entra ID Admin Center
**Path:** Entra ID > Protection > Conditional Access > [Policy] > Enable policy > Report-only

Deploy the policy in report-only mode to evaluate impact before enforcement:
- Monitor the Conditional Access insights workbook for policy matches
- Review sign-in logs for users who would be blocked or challenged
- Verify no legitimate users are unexpectedly impacted
- After 1-2 weeks of clean results, switch to enforcement mode

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Require MFA for all Copilot access; compliant device required |
| **Recommended** | Location-based restrictions; session controls with 8-hour re-auth; report-only testing before enforcement |
| **Regulated** | Compliant device AND MFA AND trusted location required; session controls with app-enforced restrictions; Defender for Cloud Apps integration |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for Conditional Access automation
- See [Verification & Testing](verification-testing.md) to validate access controls
- Review Control 2.9 for Defender for Cloud Apps session controls
