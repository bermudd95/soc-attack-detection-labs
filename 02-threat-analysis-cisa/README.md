# Threat Analysis & Vulnerability Assessment (CISA‑Aligned)

## Overview

This lab demonstrates **threat intelligence analysis and vulnerability assessment**
using publicly disclosed advisories from the **Cybersecurity and Infrastructure
Security Agency (CISA)** and real-world vulnerabilities.

The project simulates a SOC/DFIR workflow to:
- Assess technical and business risk
- Communicate vulnerabilities to stakeholders
- Demonstrate controlled forensic and malware analysis techniques

---

## Objectives

- Review active and historically significant CISA advisories
- Identify affected systems, software components, and threat actors
- Assess likelihood, impact, and business risk
- Provide actionable mitigation and remediation guidance
- Demonstrate supporting analysis techniques using Python in a controlled environment

---

## Methodology

1. Reviewed selected CISA vulnerability advisories
2. Analyzed vulnerability characteristics and exploitation methods
3. Assessed organizational and operational impact
4. Mapped applicable threats to the **MITRE ATT&CK framework**
5. Drafted formal security advisories for internal stakeholders
6. Demonstrated controlled forensic and malware analysis techniques

---

## Security Advisory Deliverable

This lab includes a **sample internal security advisory** modeled after enterprise
SOC communications, using the Apache Log4j (Log4Shell) vulnerability as a case study.

- Audience: Product Development / Engineering
- Focus: Risk awareness, severity classification, and remediation guidance
- Frameworks Referenced: **CVSS, CISA guidance**

📁 **Advisory Location:**  
`advisory/log4j_security_advisory.md`

---

## Python Demonstration Script

This project includes a **Python-based decryption demonstration script** used to
illustrate how analysts may recover encrypted artifacts during malware analysis
or incident response investigations.

- Purpose: Educational and defensive analysis only  
- Environment: Isolated, sandboxed, non-production  
- Scope: Demonstrates brute-force techniques against encrypted ZIP files as part
  of forensic analysis

📁 **Script Location:**  
`scripts/zip_password_bruteforce.py`

> No malware samples or password lists are included in this repository.

---

## MITRE ATT&CK Mapping

| Tactic | Technique | Technique ID | Notes |
|--------|-----------|--------------|-------|
| Initial Access | Exploit Public-Facing Application | T1190 | Log4j (Log4Shell) vulnerability exploitation scenario |
| Execution | Command and Scripting Interpreter | T1059 | Demonstrated via Python decryption script (ethical sandbox) |
| Impact | Data Manipulation | T1565 | Understanding potential consequences of encrypted malware payloads |

---

## Key Skills Demonstrated

- Threat intelligence analysis  
- Vulnerability and risk assessment  
- Executive and technical security communication  
- Incident response and malware analysis concepts  
- Python scripting for forensic/security analysis  
- Alignment with **CISA** and **MITRE ATT&CK** frameworks  
- Ethical handling of security tools and data  

---

## Disclaimer

All scripts, analyses, and documentation in this repository are intended
**strictly for educational purposes** and execution within
**authorized, controlled environments**.

No testing should be performed on systems or data without explicit permission.
