# Evidence Analysis

## Purpose

This document separates the information explicitly supplied by the scenario from the analyst's interpretation and the additional evidence that would be required in a real investigation. Because this is a scenario-based exercise, no raw authentication or Sysmon logs are available for independent validation.

## 1. SSH Authentication Activity

**Scenario facts**
- At 09:12 UTC, an SSH brute-force alert was generated.
- The triage notes describe high-volume failed SSH logins from a single external IP address.
- At 10:05 UTC, a successful SSH login following repeated failures was reported.
- The incident report describes the suspected SSH activity as originating from an external IP address.

**Analytical interpretation**
The combination of repeated failed authentication attempts and a subsequent successful SSH login raises concern that an account may have been accessed through password guessing. This is a credible incident hypothesis and supports escalation.

**Evidence needed to confirm the hypothesis**
- Source IP for each failed and successful authentication event.
- Target hostname and username for each event.
- Exact timestamps and sequence of authentication attempts.
- Authentication method and result for each event.
- Whether the successful login was expected and authorized.
- Session activity following successful authentication.

**Current assessment:** Suspected SSH account compromise; not confirmed by the available scenario information.

## 2. Internal Failed-Login Activity

**Scenario facts**
- At 09:44 UTC, multiple failed logins were reported.
- The triage notes identify the source as a known internal asset.
- The activity did not exceed the alert threshold, and no automation was identified in the scenario.

**Analytical interpretation**
The internal asset context and lower activity level supported monitoring in the original triage decision. These factors do not independently prove that the activity was benign.

**Evidence needed for further assessment**
- Asset owner and expected function.
- Targeted account and destination system.
- Normal authentication baseline for the asset.
- Whether failures were followed by successful authentication.
- Whether the activity coincided with approved administrative work.

**Current assessment:** Monitored activity; no confirmed relationship to the suspected external SSH incident.

## 3. PowerShell Activity

**Scenario facts**
- At 09:27 UTC, a low-severity PowerShell execution alert was generated.
- The scenario describes it as routine administrative maintenance from an internal management host.
- The false-positive notes cite a known administrator account and an approved maintenance window.
- At 10:22 UTC, a separate medium-severity alert reported repeated PowerShell commands. No disposition was documented.

**Analytical interpretation**
The 09:27 alert was closed as benign in the scenario based on the stated administrative context. The 10:22 alert remains unresolved. Repeated PowerShell execution is not inherently malicious, but should not be closed without examining its execution context.

**Evidence needed for further assessment**
- PowerShell command line and script content, where available.
- Executing account and logon context.
- Hostname and host role.
- Parent and child process information.
- Maintenance approval and expected execution window.
- Related endpoint, authentication, and network activity.

**Current assessment:** 09:27 alert assessed as benign within the scenario; 10:22 alert requires investigation.

## 4. Correlation Assessment

The scenario provides a possible relationship between the 09:12 SSH brute-force alert and the 10:05 successful SSH login after failures. It does not provide the shared identifiers needed to confirm that relationship. Correlation should be validated by comparing source IP, username, destination host, and event timestamps.

The 09:44 internal failed-login activity and the two PowerShell alerts should be treated as separate alert streams unless additional evidence links them to the SSH activity.

## 5. Evidence Limitations

No raw logs, packet captures, endpoint artifacts, process trees, command lines, or forensic images were supplied. Accordingly, this case study does not claim to prove account compromise, privilege escalation, persistence, lateral movement, data exfiltration, or any other post-authentication activity.
