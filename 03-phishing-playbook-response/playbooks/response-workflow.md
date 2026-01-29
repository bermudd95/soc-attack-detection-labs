# Phishing Incident Response Workflow

## Purpose
This document provides a simplified, step-by-step workflow to guide SOC analysts through the response process following a suspected phishing incident.

It is intended for operational use during triage and response.

---

## Step 1: Intake & Triage
- Receive phishing report from user, email gateway, or monitoring alert
- Review email content, sender address, and embedded links
- Determine whether the email matches known phishing indicators

---

## Step 2: Impact Assessment
- Identify recipients of the phishing email
- Determine whether any users clicked links or submitted credentials
- Prioritize response based on affected user role and access level

---

## Step 3: Containment
- Block malicious sender addresses, domains, and URLs
- Remove phishing emails from user inboxes where possible
- Reset credentials for affected accounts
- Revoke active authentication sessions

---

## Step 4: Investigation
- Review authentication logs for suspicious login activity
- Identify logins from new locations or devices
- Check for follow-on activity such as mailbox access or data downloads

---

## Step 5: Recovery
- Restore user access after credentials are secured
- Confirm MFA enforcement
- Continue monitoring affected accounts for abnormal behavior

---

## Step 6: Documentation & Lessons Learned
- Document timeline and actions taken
- Identify detection or response gaps
- Recommend improvements to controls or user training

---

## Roles & Ownership
- SOC Analyst: Triage and investigation
- Incident Response: Containment and recovery
- IAM / IT Teams: Credential management
- Security Awareness: User follow-up and training
