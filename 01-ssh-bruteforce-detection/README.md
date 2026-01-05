# SSH Brute Force Attack Simulation

## Overview
This project simulates a real-world SSH brute-force attack to understand how repeated authentication failures appear at the host level and how a SOC analyst would detect, investigate, and respond to the activity.

The lab was designed to mirror attacker and defender behavior using separate Linux systems in a controlled environment.

---

## Objectives
- Simulate an SSH brute-force attack using common attacker tooling
- Identify brute-force indicators within authentication logs
- Document the attack lifecycle from initial access attempt to containment
- Produce actionable mitigation recommendations

---

## Environment
- Attacker: Kali Linux
- Target: Ubuntu Linux
- Tooling: Hydra, SSH, Linux authentication logs

---

## Methodology
1. Generated repeated SSH login attempts using Hydra
2. Monitored authentication logs on the target system
3. Identified indicators of brute-force behavior (failed logins, source IP repetition)
4. Documented timeline, impact, and response actions
5. Proposed mitigation steps including access hardening

---

## Key Findings
- Repeated failed SSH login attempts from a single source
- Clear log indicators suitable for SIEM detection rules
- High risk if left unmitigated on internet-facing systems

---

## Skills Demonstrated
- Adversary simulation
- Log analysis
- Incident documentation
- Linux security fundamentals
- SOC-style reporting

---

## Disclaimer
This project was conducted in a controlled lab environment for educational purposes only.

