# Control 1.12: Training and Awareness Program — Portal Walkthrough

Step-by-step portal procedures for establishing and managing the Copilot training and awareness program.

## Prerequisites

- Microsoft 365 Admin Center access
- Microsoft Viva Learning license (optional, for integrated learning)
- Learning Management System (LMS) access for compliance training
- Training content development resources

## Steps

### Step 1: Access Microsoft Copilot Training Resources

**Portal:** Microsoft Adoption Center
**Path:** adoption.microsoft.com > Copilot > Training

Review the Microsoft-provided Copilot training resources including:
- Microsoft 365 Copilot user training modules
- Administrator training for Copilot governance
- Prompt engineering best practices
- Role-specific use case guides

Download or bookmark resources for integration into your training program.

### Step 2: Configure Viva Learning for Copilot Content

**Portal:** Microsoft Viva Learning (via Teams)
**Path:** Teams > Viva Learning > Admin Settings > Content Sources

If Viva Learning is deployed, configure it to include Copilot training content:
- Add Microsoft Learn as a content source (includes Copilot modules)
- Upload custom FSI-specific governance training modules
- Create learning paths combining Microsoft content with organizational policies
- Assign learning paths to Copilot deployment groups

### Step 3: Develop FSI-Specific Governance Training

Create organization-specific training modules covering:
- **Data governance obligations:** What content Copilot can access and why labeling matters
- **Acceptable use policy:** Approved and prohibited Copilot use cases for your organization
- **Sensitive data handling:** How to verify Copilot responses do not expose restricted content
- **Reporting obligations:** How to report governance concerns or data exposure incidents
- **Supervisory requirements:** Copilot interaction review obligations for supervised roles

### Step 4: Configure Training Completion Tracking

**Portal:** Learning Management System or Microsoft 365 Admin Center
**Path:** LMS > Reports > Completion tracking

Set up completion tracking for required Copilot training:
- Make governance training a prerequisite for Copilot license activation
- Track completion rates by department and deployment wave
- Configure reminder notifications for incomplete training
- Generate compliance evidence reports for audit

### Step 5: Establish Ongoing Awareness Program

Plan recurring awareness activities:
- Monthly Copilot tips and governance reminders via email or Teams
- Quarterly lunch-and-learn sessions on new Copilot features
- Annual refresher training on governance policies
- Incident-driven awareness communications when relevant

## FSI Recommendations

| Tier | Recommendation |
|------|---------------|
| **Baseline** | Assign Microsoft Copilot training to all licensed users; include basic governance awareness |
| **Recommended** | Custom FSI governance training module; training prerequisite for Copilot activation; monthly awareness communications |
| **Regulated** | Mandatory annual compliance training with documented completion; role-specific modules for supervised activities; training effectiveness assessment |

## Next Steps

- Proceed to [PowerShell Setup](powershell-setup.md) for training tracking automation
- See [Verification & Testing](verification-testing.md) to validate training program
- Review Control 1.11 for Change Management context
- Back to [Control 1.12](../../../controls/pillar-1-readiness/1.12-training-awareness.md)
