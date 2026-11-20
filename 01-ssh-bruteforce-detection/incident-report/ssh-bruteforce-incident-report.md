# Incident Report: SSH Brute-Force Simulation with Successful Password Discovery

**Exercise date:** March 5, 2025  
**Target system:** Ubuntu Linux virtual machine  
**Attacker system:** Kali Linux  
**Target account:** `bob_victim`  
**Target IP address:** `192.168.226.130`  
**Attack tool:** Hydra  
**Incident classification:** Successful password guessing in a controlled lab

---

## 1. Executive Summary

A controlled SSH password-guessing exercise was conducted against an Ubuntu Linux virtual machine. Hydra was executed from a Kali Linux system using a custom weak-password dictionary and the target account `bob_victim`. The exercise resulted in successful password discovery: Hydra identified a password accepted by the target's SSH authentication service.

This outcome is more significant than a sequence of failed login attempts alone. It demonstrates that the targeted account's password was present in the supplied dictionary and accepted by the service. The account should therefore be treated as potentially compromised within the scenario.

The source materials do not establish whether an interactive SSH session was subsequently opened or whether activity occurred after authentication. Those outcomes are not claimed in this report.

## 2. Scope and Environment

| Attribute | Recorded detail |
|---|---|
| Exercise date | March 5, 2025 |
| Attacker | Kali Linux |
| Target | Ubuntu Linux virtual machine |
| Target IP | `192.168.226.130` |
| Target username | `bob_victim` |
| Service | SSH |
| Tool | Hydra |
| Password list | Custom weak-password dictionary |

## 3. Attack Execution

The following command was documented in the original lab report:

```bash
hydra -l bob_victim -P password_list.txt ssh://192.168.226.130 -V
```

The command instructed Hydra to attempt SSH authentication against the target using the specified username and password list. The exercise notes confirm that Hydra successfully discovered a password accepted by the SSH service.

The recovered password is not included in this report. Credentials should not be exposed in public documentation or committed to source control.

## 4. Findings and Evidence Assessment

### Confirmed by the exercise notes

- SSH password-guessing activity was generated from Kali Linux against the Ubuntu target.
- The target account was `bob_victim`.
- Hydra used a custom weak-password dictionary.
- Password discovery was successful; the target SSH service accepted a password supplied by Hydra.

### Not established by the available evidence

- The exact number of failed authentication attempts.
- The exact timestamp of the successful password discovery.
- The source IP address as recorded in the target's authentication logs.
- The specific authentication-log entries and their event sequence.
- Whether an interactive SSH session was opened after discovery.
- Whether commands were executed, privileges changed, or persistence was established.

These details should be added only if supported by retained lab output or authentication logs.

## 5. Incident Assessment

**Assessment:** Successful password guessing against the targeted account.

The successful credential discovery indicates that the account used a password weak enough to be found in the supplied dictionary. In an operational environment, this would warrant treating the credential as exposed and investigating whether it was used to access the host.

The evidence supports a successful password discovery, but does not independently prove post-authentication activity or broader system compromise. The investigation should therefore distinguish credential compromise from confirmed interactive access and from any further actions on the host.

## 6. Recommended Investigation Steps

A defender responding to this activity should:

1. Preserve the relevant SSH and system authentication logs.
2. Identify the source address, targeted account, and destination host associated with the failed and successful authentication events.
3. Establish whether the successful event followed repeated failures from the same source and targeted the same account.
4. Review session records and process or audit telemetry, if available, to determine whether an interactive session was established.
5. Examine subsequent activity for privilege changes, new accounts, modified SSH keys, unusual processes, scheduled tasks, or other persistence indicators.
6. Determine whether other accounts or hosts were targeted.

## 7. Recommended Containment and Remediation

The following actions are recommended for the scenario; the original notes do not confirm that they were executed:

- Reset the affected account's password and invalidate active sessions where feasible.
- Temporarily restrict or disable the account if business requirements permit.
- Restrict SSH access to approved source networks or administrative access paths.
- Review and remove unauthorized SSH keys, if any are found.
- Review authentication and system activity for evidence of post-authentication actions.
- Enable or enforce multi-factor authentication where supported by the environment.
- Disable password-based SSH authentication where key-based access is operationally appropriate and securely managed.
- Apply rate limiting or intrusion-prevention controls to reduce repeated password-guessing attempts.

## 8. MITRE ATT&CK Mapping

| Technique | Relevance to this exercise |
|---|---|
| **T1110.001 – Brute Force: Password Guessing** | Hydra attempted passwords from a dictionary against the SSH service. |
| **T1078 – Valid Accounts** | The exercise identified a password accepted for the targeted account. This does not establish what the account was used to do afterward. |

## 9. Lessons Learned

- Repeated authentication failures should be evaluated as a pattern, not only as isolated events.
- A successful authentication following password-guessing activity materially increases the severity of the event.
- Detection should correlate source, destination, account, and event sequence when telemetry supports those fields.
- Credential discovery and confirmed post-authentication activity are separate investigative conclusions and should be reported separately.
- Preserving raw authentication logs and exact tool output improves reproducibility and supports defensible incident reporting.

## 10. Conclusion

The lab successfully demonstrated SSH password guessing and discovery of a valid password for `bob_victim`. It illustrates why repeated authentication failures followed by successful authentication deserve investigation and why weak passwords create account-compromise risk.

The available evidence supports successful password discovery. Additional authentication logs or session telemetry would be required to determine whether the credential was used for interactive access and whether any post-authentication activity occurred.
