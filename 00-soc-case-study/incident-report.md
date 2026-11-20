# Incident Report: Suspected SSH Account Compromise

## Report Context

This report documents the response plan for a simulated SOC incident. The scenario describes a successful SSH login following repeated authentication failures. The report does not represent a confirmed production compromise or verified forensic investigation.

## Executive Summary

At 10:05 UTC, a high-severity alert reported a successful SSH login following repeated authentication failures. The original scenario describes the suspected activity as originating from an external IP address. This pattern may indicate that an account was accessed after password-guessing activity and warrants incident escalation.

An earlier SSH brute-force alert was recorded at 09:12 UTC. The available scenario information does not establish whether the earlier alert and later successful login involved the same source IP, account, or destination host. Correlation is therefore a priority investigative task.

## Incident Classification

- **Incident type:** Suspected account compromise / suspicious SSH authentication
- **Severity:** High, as assigned in the scenario
- **Status:** Escalated for investigation
- **Confidence:** Suspicious activity is reported; compromise is not confirmed

## Known Scenario Information

- A 09:12 UTC alert described high-volume failed SSH logins from a single external IP address.
- A 10:05 UTC alert described successful SSH authentication following repeated failures.
- The original incident summary identifies an external IP address as the origin of the suspected SSH activity.
- No source address, account name, hostname, raw authentication events, or post-login activity details are provided.

## Potential Impact

If the successful login was unauthorized, the affected account and Linux server may have been exposed to unauthorized access. The available information does not establish whether the account had elevated privileges or whether the system was modified, used for lateral movement, or accessed for sensitive data.

## Recommended Investigation

1. Retrieve the relevant Linux authentication records and establish the exact sequence of failed and successful SSH attempts.
2. Compare source IP, username, destination host, and timestamps across the 09:12 and 10:05 alerts.
3. Determine whether the successful login was expected and authorized by the account owner or system administrator.
4. Review the SSH session and subsequent activity for unexpected commands, privilege changes, new accounts, persistence mechanisms, or access to sensitive files.
5. Review relevant endpoint and network telemetry for activity associated with the session.
6. Preserve relevant logs and investigation notes according to the organization's evidence-handling procedures.

## Proposed Containment and Recovery Actions

The original scenario lists the following response actions. For this case study, they are presented as **proposed or simulated actions**, not as verified actions performed on a live host:

1. **Restrict access to the affected host if warranted.** Consider host isolation or limiting SSH access based on business impact and incident-response procedures.
2. **Block or restrict the suspected source IP when justified.** Validate the source and assess the risk of blocking shared or legitimate infrastructure.
3. **Secure the potentially affected account.** Reset credentials or disable the account as appropriate, and review related credentials or keys if evidence indicates exposure.
4. **Review post-authentication activity.** Examine relevant system and authentication records for unauthorized changes or continued access.
5. **Restore normal operations only after validation.** Confirm that the threat has been contained and that required recovery checks are complete.

## MITRE ATT&CK Mapping

| Technique | Relevance to scenario | Qualification |
|---|---|---|
| T1110.001 – Brute Force: Password Guessing | The scenario describes high-volume failed SSH authentication attempts consistent with password guessing. | Scenario-supported behavior; underlying authentication records are not available. |
| T1078 – Valid Accounts | A successful SSH login followed repeated failures, raising the possibility that valid credentials were used. | Potential mapping only; the scenario does not confirm that the credentials were compromised or used maliciously. |

## Outstanding Questions

- Did the 09:12 and 10:05 events share the same source IP, account, and destination host?
- Was the successful SSH login authorized?
- What activity occurred during and after the SSH session?
- Were there privilege changes, new accounts, persistence, lateral movement, or access to sensitive data?
- Were containment actions necessary, approved, and effective?

## Conclusion

The successful SSH login following repeated authentication failures is a high-priority indicator that justifies escalation and further investigation. The scenario supports a suspected account-compromise hypothesis, but does not provide enough evidence to confirm compromise or determine impact. Response actions should be selected and validated based on the results of the proposed investigation.
