# SSH Brute-Force Attack Simulation & Detection

## Overview

This lab simulates an unauthorized SSH brute-force attack against a Linux
virtual machine in a controlled lab environment. The objective is to identify
brute-force indicators through log analysis, document the incident lifecycle,
and propose mitigation strategies.

This project mirrors real-world SOC workflows from detection to remediation.

---

## Lab Objectives

- Simulate an SSH brute-force attack using Hydra
- Analyze Linux authentication logs for attack indicators
- Identify escalation and credential compromise patterns
- Document root cause and remediation actions

---

## Environment

| Role        | System        |
|------------|---------------|
| Attacker   | Kali Linux VM |
| Defender   | Ubuntu Linux VM |
| Protocol   | SSH |

---

## Attack Simulation

- **Attack Type:** SSH Brute Force
- **Tool Used:** Hydra
- **Target Account:** `bob_victim`
- **Password Method:** Dictionary-based brute force
- **MITRE ATT&CK Technique:**  
  - T1110 – Brute Force

---

## Detection & Analysis

Detection was performed using Linux authentication logs:

- `/var/log/auth.log`
- Repeated failed login attempts
- High-frequency authentication failures
- Eventual successful login following failures

---

## Incident Report

A full SOC-style incident report is included, documenting:

- Timeline of attack activity
- Indicators of compromise (IOCs)
- Root cause analysis
- Mitigation and hardening recommendations

📄 **Report Location:**  
`incident-report/ssh-bruteforce-root-cause.md`

---

## Key Takeaways

- Weak passwords significantly increase exposure to brute-force attacks
- SSH logging provides clear detection opportunities
- Preventive controls such as Fail2Ban and SSH key authentication are critical

---

> **Disclaimer:**  
> This lab was conducted in an isolated environment for educational purposes only.
