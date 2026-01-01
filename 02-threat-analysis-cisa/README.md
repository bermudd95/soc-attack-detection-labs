# Threat Analysis & Vulnerability Assessment (CISA‑Aligned)

## Overview

This lab focuses on **threat intelligence analysis and vulnerability assessment**
using publicly disclosed advisories from the **Cybersecurity and Infrastructure
Security Agency (CISA)** and widely exploited real‑world vulnerabilities.

The objective of this project is to simulate a SOC‑level threat analysis workflow by:
- Assessing technical and business risk
- Communicating vulnerabilities to stakeholders
- Demonstrating controlled analysis techniques used during incident response and
  malware investigations

---

## Objectives

- Review active and historically significant CISA advisories
- Identify affected systems, software components, and attack vectors
- Assess likelihood, impact, and potential business risk
- Provide actionable mitigation and remediation guidance
- Demonstrate supporting analysis techniques using Python in a controlled environment

---

## Methodology

1. Reviewed selected CISA vulnerability advisories
2. Analyzed vulnerability characteristics and exploitation methods
3. Assessed organizational and operational impact
4. Mapped applicable techniques to the **MITRE ATT&CK framework**
5. Drafted a formal security advisory for internal stakeholders
6. Demonstrated a controlled forensic analysis technique using Python

---

## Security Advisory Deliverable

This lab includes a **sample internal security advisory** modeled after enterprise
SOC communications, using the Apache Log4j (Log4Shell) vulnerability as a case study.

- Audience: Product Development / Engineering
- Focus: Risk awareness, severity classification, and remediation guidance
- Frameworks Referenced: CVSS, CISA guidance

📁 **Advisory Location:**  
`advisory/log4j_security_advisory.md`

---

## Python Demonstration Script

This project includes a **Python‑based decryption demonstration script** used to
illustrate how analysts may recover encrypted artifacts during malware analysis
or incident response investigations.

- Purpose: Educational and defensive analysis only
- Environment: Isolated, sandboxed, non‑production
- Scope: Demonstrates brute‑force techniques against encrypted ZIP files as part
  of forensic analysis

📁 **Script Location:**  
`scripts/zip_password_bruteforce.py`

> No malware samples or password lists are included in this repository.

---

## Key Skills Demonstrated

- Threat intelligence analysis
- Vulnerability and risk assessment
- Executive and technical security communication
- Incident response and malware analysis concepts
- Python scripting for security analysis
- Alignment with **CISA** and **MITRE ATT&CK** frameworks
- Ethical handling of security tools and data

---

## Disclaimer

All scripts, analyses, and documentation in this repository are intended
**strictly for educational purposes** and execution within
**authorized, controlled environments**.

No testing should be performed on systems or data without explicit permission.

