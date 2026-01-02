# Phishing Response & Security Awareness Lab

## Overview

This lab focuses on **phishing detection, response, and user awareness** as part
of a SOC-aligned security operations workflow.

The project demonstrates how phishing emails are:
- Simulated for training purposes
- Analyzed by security teams
- Used to educate end users and reduce organizational risk

---

## Objectives

- Understand common phishing and social engineering techniques
- Analyze phishing email characteristics
- Demonstrate proper phishing response procedures
- Develop user-facing phishing awareness training materials

---

## MITRE ATT&CK Mapping

| Tactic | Technique | Technique ID | Description |
|------|----------|-------------|-------------|
| Initial Access | Phishing: Spearphishing Link | T1566.002 | Simulated phishing email attempts to entice the user to click a malicious link |
| Credential Access | Credentials from Phishing | T1056 | Demonstrates how attackers attempt to harvest login credentials |
| Defense Evasion | Masquerading | T1036 | Email impersonates a trusted organization to evade user suspicion |

This mapping reflects common techniques observed in real-world phishing campaigns
and aligns with SOC detection and response workflows.

## Lab Components

### 1. Sample Phishing Email

A simulated phishing email designed to replicate real-world credential
harvesting attempts.

📁 Location:  
`phishing-email/sample_phishing_email.md`

**Techniques Demonstrated:**
- Brand impersonation
- Urgency and fear-based messaging
- Malicious link placement

---

### 2. Phishing Awareness Training

A security awareness presentation designed to educate users on:
- What phishing is
- How to identify phishing emails
- Best practices for prevention and reporting

📁 Location:  
`training/phishing_awareness_training.pptx`

---

## Key Skills Demonstrated

- Phishing and social engineering analysis
- Security awareness training development
- Incident response fundamentals
- SOC documentation practices
- User education and risk reduction

---

## Disclaimer

All materials in this lab are intended for **educational and defensive
security purposes only**. Phishing examples are simulated and should never
be used outside of authorized training environments.
