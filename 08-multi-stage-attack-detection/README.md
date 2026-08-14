# Multi-Stage Attack Detection & Incident Response Lab

## Overview

This project simulates a real-world Security Operations Center (SOC) investigation using the Elastic Stack to detect, analyze, and respond to a multi-stage cyber attack. The objective was to gain hands-on experience with security monitoring, threat detection, incident response, and attack analysis in a controlled lab environment.

The lab leverages attacker and victim virtual machines to generate realistic security telemetry that is collected and analyzed through Elastic Security and Kibana.

---

## Project Objectives

* Simulate attacker behavior in a controlled environment
* Generate security telemetry for analysis
* Detect malicious activity using Elastic Security
* Perform alert triage and incident investigation
* Reconstruct attacker timelines
* Map activity to the MITRE ATT&CK Framework
* Develop SOC investigation and documentation skills

---

## Lab Environment

### Infrastructure

| System        | Role                          |
| ------------- | ----------------------------- |
| Kali Linux    | Attacker                      |
| Ubuntu Linux  | Victim                        |
| Elastic Stack | SIEM Platform                 |
| Kibana        | Visualization & Investigation |
| Elastic Agent | Log Collection                |

### Data Sources

* Linux Authentication Logs
* Syslog Events
* Process Activity
* Network Connections
* Security Events
* Elastic Security Alerts

---

## Attack Scenario

### Stage 1: Reconnaissance

The attacker identifies accessible services and potential attack vectors.

### Stage 2: Initial Access

A brute-force attack is conducted against exposed services to gain access to the target system.

### Stage 3: Credential Access

Authentication activity is analyzed to identify successful account compromise following repeated failed login attempts.

### Stage 4: Execution

Commands are executed on the compromised system to simulate post-exploitation activity.

### Stage 5: Detection & Investigation

Security telemetry is reviewed within Elastic Security to identify:

* Failed login spikes
* Successful authentication after repeated failures
* Suspicious process execution
* Potential indicators of compromise (IOCs)

---

## Detection Methodology

### Authentication Monitoring

The following behaviors were monitored:

* Multiple failed login attempts
* Password spraying indicators
* Brute-force activity
* Successful logins following repeated failures
* Abnormal authentication behavior

### Alert Investigation Workflow

1. Review alert metadata
2. Validate alert legitimacy
3. Correlate related events
4. Determine scope and impact
5. Identify affected assets
6. Document findings
7. Escalate when appropriate

---

## Example Investigation Process

### Alert

Multiple failed authentication attempts detected against a Linux host.

### Investigation Steps

* Review source IP addresses
* Analyze authentication logs
* Identify successful login attempts
* Correlate user activity
* Review executed commands
* Determine attacker actions
* Assess potential impact

### Findings

* Repeated failed login attempts observed
* Successful authentication achieved after multiple failures
* Evidence of unauthorized access
* Incident escalated for containment and remediation

---

## MITRE ATT&CK Mapping

| Technique                         | ID        |
| --------------------------------- | --------- |
| Brute Force                       | T1110     |
| Password Spraying                 | T1110.003 |
| Command and Scripting Interpreter | T1059     |
| Valid Accounts                    | T1078     |
| Account Discovery                 | T1087     |

---

## Skills Demonstrated

### Security Operations

* Alert Triage
* Incident Investigation
* Incident Response
* Security Monitoring
* Threat Detection
* Log Correlation

### Security Platforms

* Elastic Security
* Kibana
* Elastic Agent

### Operating Systems

* Kali Linux
* Ubuntu Linux

### Frameworks & Methodologies

* MITRE ATT&CK
* Incident Response Lifecycle
* Threat Hunting Methodologies

---

## Key Takeaways

This project provided hands-on experience investigating attack activity from initial access through post-exploitation. It reinforced the importance of log correlation, attack timeline reconstruction, and structured incident response procedures when handling security incidents.

---

## Future Enhancements

* Integrate Windows endpoints using Sysmon
* Develop custom Elastic detection rules
* Simulate phishing-based initial access
* Implement automated alerting workflows
* Expand MITRE ATT&CK coverage
* Add threat hunting queries
* Incorporate malware analysis scenarios

---


## Author

**Danny Bermudez**

Cybersecurity Analyst | SOC Analyst Candidate

*Back to the [Main Repository](https://github.com/bermudd95/elastic-siem-attack-lab)*
