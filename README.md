# SOC Attack Detection & Incident Response Labs

## 📌 Overview
This repository contains a structured set of hands-on cybersecurity labs focused on Security Operations Center (SOC) detection, analysis, and incident response workflows.

Each project simulates realistic attack scenarios or analyst responsibilities commonly encountered in enterprise security environments. The work emphasizes not only technical execution, but also quantitative data analysis, SIEM engineering, documentation, communication, and decision-making aligned with real SOC and Blue Team operations.

---

## 🎯 Portfolio Objectives
*   Demonstrate practical SOC analyst skills through hands-on, project-based labs.
*   Simulate common adversary techniques and defender logging responses.
*   Apply industry frameworks such as MITRE ATT&CK mapping and CISA advisories.
*   Develop clear, executive-ready security and human risk documentation.
*   Show progression from SIEM threat detection to active incident response and mitigation.

---

## 📁 Project Structure

### 00 — SOC Case Study
A foundational case study providing context for the broader set of labs. Includes analytical scenarios, hypotheses, and analysis frameworks used across the subsequent technical projects.

### 01 — SSH Brute Force Detection
Simulates a brute‑force attack against SSH and focuses on identifying evidence in Linux authentication logs, reconstructing the attack timeline, and documenting mitigation recommendations.
*   **Skills Demonstrated:** Linux log analysis, adversary behavior simulation, mitigation strategies, analyst timeline documentation.

### 02 — Phishing Live Response Lab
Analyzes a live phishing simulation to identify technical phishing indicators, document malicious email attack artifacts, and guide effective response actions.
*   **Skills Demonstrated:** Phishing investigation, evidence collection, triage response tactics.

### 03 — Phishing Playbook & Response
Develops a structured phishing incident response playbook that outlines detection, containment, eradication, communication, and remediation steps.
*   **Skills Demonstrated:** Incident Response (IR) playbook creation, IR planning and documentation, cross‑team coordination concepts.

### 04 — EDR & Sysmon Detection
Leverages Windows Sysmon telemetry to detect and analyze suspicious host activity (e.g., PowerShell misuse), reconstruct process timelines, and produce incident reports following SOC escalation workflows.
*   **Skills Demonstrated:** Host telemetry analysis, event correlation, incident reconstruction.

### 05 — Threat Intelligence Brief
Produces a comprehensive threat intelligence brief focused on an advanced persistent threat (APT) adversary or campaign. Translates external threat data into actionable detection priorities and recommendations.
*   **Skills Demonstrated:** Threat synthesis, risk communication, MITRE ATT&CK mapping.

### 06 — Threat Analysis (CISA)
Assesses a publicly released vulnerability or security advisory (e.g., CISA) to determine technical risk, business impact, and patching/mitigation guidance. 
*   **Skills Demonstrated:** Vulnerability analysis, advisory interpretation, defensive detection guidance.

### 07 — Detection & Response Use Case
Documents a composite SOC detection and response use case, correlating multiple signals (e.g., phishing activity with login anomalies), designing alert logic, and outlining triage response actions.
*   **Skills Demonstrated:** Detection engineering concepts, alert logic formulation, triage workflows.

### 08 — Multi-Stage Attack Detection
Simulates an end-to-end multi-stage cyber attack (Reconnaissance → Initial Access → Credential Access → Execution) using a Kali Linux/Ubuntu deployment. Collects network and host security telemetry via Elastic Agent to perform alert triage, timeline reconstruction, and SIEM incident investigation in Kibana.
*   **Skills Demonstrated:** SIEM deployment (Elastic Security), alert validation, timeline reconstruction, MITRE ATT&CK mapping (`T1110`, `T1078`), log correlation.

### 09 — Phishing Risk Assessment
Architects and analyzes a 500-user phishing simulation database log using advanced spreadsheet data engineering. Evaluates multi-stage user exploitation cycles to isolate critical departmental vulnerabilities and delivers a strategic C-suite mitigation roadmap.
*   **Skills Demonstrated:** Human risk modeling, data aggregation (`COUNTIFS`), behavioral metrics visualization, identity theft blast-radius mitigation.

---

## 🛠️ Tools & Frameworks Used
Across the labs you’ll see:
*   **SIEM & Visualization:** Elastic Security, Kibana, Elastic Agent
*   **Operating Systems:** Linux (Kali Linux, Ubuntu) & Windows Environment Architectures
*   **Telemetry & Logs:** Sysmon, Windows Event Logging (`EVTX`), Linux Authentication Logs, Syslog, Network Connections
*   **Analysis & Logic:** Python scripting, regular expressions, advanced data arrays
*   **Frameworks:** MITRE ATT&CK mapping, threat intelligence sources (CISA advisories)

---

## 📄 Documentation Standards
Each project includes:
*   Defined objectives, scope, and threat modeling
*   Environment setup, configurations, and data assumptions
*   Step‑by‑step technical methodology and SIEM/log investigation
*   Analysis, granular findings, and strategic outcomes
*   Professional narration, executive summaries, and defense disclaimers

This uniform structure mirrors standard documentation practices expected in professional enterprise and federal analyst roles.

---

## 👥 Who This Is For
*   **Hiring Managers & Technical Interviewers** looking for metric-driven project proof and SIEM proficiency.
*   **SOC Analysts, Blue Team practitioners, & Incident Responders.**
*   **Detection Engineers** looking at alert correlation logic and playbook design.

---

## ⚠️ Disclaimer
All labs were conducted in sandbox, virtual, or controlled demonstration environments for educational and validation purposes only. No production systems or live corporate assets were impacted.

---

## 👤 Author

**Danny Bermudez**  
*Cybersecurity Analyst & Blue Team Practitioner*  
Focused on enterprise SOC operations, SIEM monitoring, threat data analytics, network detection, and tactical incident response.

---

## 🔗 Contributions
Contributions, feedback, and improvements are welcome via GitHub Issues or Pull Requests!
