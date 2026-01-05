# Phishing Incident Response Playbook

## Purpose
This playbook outlines the standardized response procedures for identifying,
analyzing, and responding to suspected phishing incidents within an organization.

---

## Detection Sources
- User-reported suspicious emails
- Email security gateway alerts
- SOC analyst review of inbound messages

---

## Initial Triage
1. Confirm whether the email is phishing
2. Identify sender address and domain
3. Inspect URLs and attachments
4. Check for urgency, impersonation, or credential harvesting language

---

## Analysis Steps
- Review email headers (SPF, DKIM, DMARC)
- Analyze embedded URLs using reputation tools
- Identify impersonated brands or internal departments
- Determine whether credentials were submitted

---

## Containment Actions
- Remove the email from user inboxes
- Block sender domain and IP addresses
- Disable affected user accounts if compromise is suspected
- Reset passwords and revoke active sessions

---

## Eradication & Recovery
- Educate affected users on phishing indicators
- Restore accounts and verify no further malicious activity
- Monitor for follow-on attacks

---

## Communication
- Notify impacted users
- Provide security awareness guidance
- Escalate to management if widespread impact is observed

---

## Post-Incident Review
- Document indicators of compromise
- Identify gaps in detection or user training
- Update email filtering rules and awareness materials
