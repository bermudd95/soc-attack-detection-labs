# SSH Brute-Force Attack and Credential Discovery

## Overview

This project documents a controlled SSH brute-force simulation conducted on March 5, 2025. A Kali Linux system used Hydra to attempt dictionary-based authentication against an Ubuntu Linux virtual machine. The exercise resulted in successful password discovery for the targeted account, `bob_victim`.

The project focuses on how repeated SSH authentication failures can indicate password-guessing activity, how a successful authentication changes the incident assessment, and how a SOC analyst can investigate and recommend containment and hardening measures.

> **Lab scope:** This was a controlled educational exercise using virtual machines. It was not a production incident. The available project notes establish successful password discovery by Hydra, but do not include the raw authentication-log excerpts, exact attempt count, discovery timestamp, or evidence of post-authentication activity. Those details are intentionally not inferred.

## Objectives

- Simulate SSH password guessing from a separate Linux attacker system.
- Observe authentication activity on the Ubuntu target.
- Identify repeated authentication failures and successful credential validation.
- Assess the security significance of discovering a valid password.
- Document investigation steps, detection opportunities, and remediation recommendations.

## Lab Environment

| Component | Details |
|---|---|
| Attacker system | Kali Linux |
| Target system | Ubuntu Linux virtual machine |
| Target IP address | `192.168.226.130` |
| Target account | `bob_victim` |
| Attack tool | Hydra |
| Authentication service | SSH |
| Password source | Custom weak-password dictionary |
| Exercise date | March 5, 2025 |

## Attack Execution

The documented Hydra command was:

```bash
hydra -l bob_victim -P password_list.txt ssh://192.168.226.130 -V
```

The command supplied one target username and a password list to Hydra's SSH module. During execution, Hydra successfully discovered a password accepted by the target's SSH authentication service.

The recovered password is deliberately not reproduced in this repository. Avoid committing real or reusable credentials, even when they originate in a lab.

## Key Findings

- Repeated SSH authentication attempts were generated from the Kali Linux system.
- The exercise resulted in successful password discovery for `bob_victim`.
- The successful authentication response demonstrates that password guessing progressed beyond unsuccessful attempts and identified a credential accepted by the target service.
- A valid credential discovery should be treated as a potential account compromise and investigated accordingly.

The available notes do not establish the exact number of attempts, the precise time of password discovery, whether an interactive shell was opened, or whether any commands were executed after authentication. These remain evidence gaps rather than assumed outcomes.

## Investigation and Detection Focus

A defender reviewing this activity should correlate:

1. Repeated SSH authentication failures.
2. The source address associated with those failures.
3. The targeted username and destination host.
4. A subsequent successful authentication for the same account and source, where supported by the logs.
5. Any post-authentication activity, such as new processes, privilege changes, account changes, or persistence mechanisms.

See [`evidence/authentication-log-analysis.md`](evidence/authentication-log-analysis.md) for the evidence review framework and [`detection/ssh-bruteforce-detection.md`](detection/ssh-bruteforce-detection.md) for a conceptual detection approach.

## Response and Hardening

Recommended response actions include preserving authentication logs, confirming the account and source involved, disabling or resetting the affected credential as appropriate, reviewing post-authentication activity, and restricting SSH exposure. See [`remediation/ssh-hardening-recommendations.md`](remediation/ssh-hardening-recommendations.md).

These are recommendations for the scenario. The original notes do not document that these remediation actions were performed.

## Skills Demonstrated

- Controlled adversary simulation
- Linux SSH authentication concepts
- Authentication-log investigation methodology
- Password-guessing detection concepts
- Incident assessment and response recommendations
- Security documentation

## MITRE ATT&CK Context

- **T1110.001 – Brute Force: Password Guessing:** Hydra attempted passwords from a dictionary against the SSH service.
- **T1078 – Valid Accounts:** The exercise discovered a password accepted for the targeted account. This mapping describes the valid-credential outcome; it does not independently establish what actions were taken after authentication.

## Limitations

This repository documents the lab as recorded, not a fully instrumented forensic investigation. Raw log excerpts, exact attempt counts, timestamps for individual events, and post-authentication command history were not included in the source materials. Detection logic in this project is therefore presented as a proposed approach unless explicitly identified as having been tested.

## Disclaimer

This project was conducted in a controlled lab environment for educational purposes only. The techniques were not directed at systems outside the lab.
