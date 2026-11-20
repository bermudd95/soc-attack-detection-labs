# Alert Triage Decisions

This document records the alert dispositions stated in the scenario and identifies where the available information is insufficient for a definitive conclusion.

## Alert 1: SSH Brute-Force Attempt

**Time:** 09:12 UTC  
**Severity:** Medium  
**Decision:** Escalated

**Scenario information:**
- High volume of failed SSH logins from a single external IP address.
- The pattern was described as consistent with automated brute-force behavior.
- The activity presented a risk of credential compromise.

**Triage rationale:** Repeated authentication failures from one external source warrant review and escalation, particularly when the activity is consistent with password guessing. The available scenario details do not include the number of attempts, time window, targeted account, or destination host.

**Follow-up needed:** Review individual authentication records, identify the targeted account and host, determine whether attempts continued, and compare the source and target details with the later successful SSH login.

## Alert 2: PowerShell Execution

**Time:** 09:27 UTC  
**Severity:** Low  
**Decision:** Closed as benign in the scenario

**Scenario information:**
- Command execution was assessed as matching known administrative behavior.
- Activity originated from an internal management host.
- The scenario states that no additional suspicious indicators were observed.
- The false-positive notes cite a known administrator account and an approved maintenance window.

**Triage rationale:** The stated administrative context supports a benign assessment. However, the scenario does not include the command line, process tree, user identity, or maintenance record used to validate the activity. The closure is therefore a scenario disposition rather than an independently verifiable finding.

**Follow-up needed:** In a real investigation, validate the account, host, command line, parent process, maintenance approval, and surrounding endpoint activity before closing the alert.

## Alert 3: Multiple Failed Logins

**Time:** 09:44 UTC  
**Severity:** Low  
**Decision:** Monitored

**Scenario information:**
- Failed logins did not exceed the alert threshold.
- The source IP was described as matching a known internal asset.
- The scenario states that no automation was identified.

**Triage rationale:** The internal-asset context and lower activity volume supported monitoring rather than immediate escalation in the scenario. An internal source should not automatically be considered trustworthy; compromised internal systems and unauthorized use remain possible.

**Follow-up needed:** Confirm asset ownership, identify the targeted account and destination, compare the activity with normal authentication patterns, and monitor for increases or related successful logins.

## Alert 4: Successful SSH Login After Failures

**Time:** 10:05 UTC  
**Severity:** High  
**Decision:** Escalated to incident

**Scenario information:**
- A successful SSH authentication followed repeated failed attempts.
- The original incident report describes the activity as originating from an external IP address.
- The activity raised concern about possible credential compromise.

**Triage rationale:** A successful authentication following repeated failures can indicate that password guessing resulted in access. The sequence warrants urgent investigation and incident escalation. The scenario does not provide enough detail to confirm that the successful login came from the same source, targeted the same account, or reached the same host as the earlier brute-force activity.

**Follow-up needed:** Correlate source IP, account, destination host, and timestamps; validate whether the login was authorized; review subsequent session activity; and assess possible privilege changes, persistence, lateral movement, or data access.

## Alert 5: Repeated PowerShell Commands

**Time:** 10:22 UTC  
**Severity:** Medium  
**Decision:** Requires investigation; disposition not provided in original scenario

**Scenario information:**
- Repeated PowerShell commands were detected by Sysmon.
- The original materials do not describe the commands, executing account, host, process lineage, or outcome of triage.

**Triage rationale:** Repeated command execution alone is not sufficient to determine malicious intent. The alert should remain open for review until the command content and execution context are understood.

**Follow-up needed:** Examine command-line details, parent and child processes, user context, host role, execution frequency, and related endpoint or network activity. Do not classify this alert as benign or malicious without supporting context.
