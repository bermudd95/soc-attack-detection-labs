# Detection and Response Improvements

The following recommendations are derived from the simulated scenario. They are design suggestions, not detection rules that were deployed or validated against actual telemetry in this project.

## 1. SSH Failed-Then-Successful Authentication Correlation

**Scenario motivation:** The 09:12 SSH brute-force alert and 10:05 successful SSH login after failures suggest a sequence worth investigating.

**Recommendation:** Develop a correlation analytic that identifies repeated failed SSH authentication attempts followed by a successful login within a defined time window.

**Useful fields, where available:**
- Source IP address
- Destination host
- Username
- Authentication result
- Event timestamp

**Validation considerations:**
- Confirm that failed and successful events are associated with the same source, account, and destination where the analytic requires it.
- Test expected administrative activity and legitimate user lockout/recovery patterns.
- Tune the threshold and time window against representative authentication behavior.
- Avoid treating a successful login after failures as proof of compromise; use it as a prioritization signal for investigation.

## 2. Internal Authentication Anomaly Review

**Scenario motivation:** The 09:44 alert was monitored because the source was a known internal asset and activity remained below the alert threshold.

**Recommendation:** Enrich authentication alerts with asset ownership, host role, expected account usage, and historical authentication patterns where those data sources are available.

**Validation considerations:** Internal systems can be compromised or misused. Tuning should not suppress activity solely because its source is internal.

## 3. PowerShell Execution Context

**Scenario motivation:** The 09:27 alert was assessed as authorized maintenance, while the 10:22 repeated-command alert remained without a documented disposition.

**Recommendation:** Improve endpoint triage by reviewing command-line content, executing identity, parent process, child processes, host role, and maintenance context. Where appropriate, build detections around suspicious execution patterns rather than PowerShell execution alone.

**Validation considerations:** Test both authorized administrative activity and suspicious execution patterns. Any exclusions should be narrow, documented, and periodically reviewed.

## 4. Alert Disposition and Case Documentation

**Scenario motivation:** The original timeline included an alert without a documented investigation outcome.

**Recommendation:** Require each alert or case record to include:
- Severity and current status.
- Relevant host, account, source, and destination identifiers when available.
- Evidence reviewed and its source.
- Analyst rationale and confidence.
- Escalation or closure decision.
- Follow-up actions and unresolved questions.

## 5. Future Technical Validation

To turn these recommendations into tested detection engineering work, a future lab iteration could:

1. Generate representative Linux authentication and Windows Sysmon events in a controlled lab.
2. Preserve the raw events and document the lab configuration.
3. Write and test correlation queries against those events.
4. Include positive test cases and benign/negative test cases.
5. Record expected results, actual results, tuning changes, and known blind spots.

Until that validation is completed, the recommendations in this document should be presented as proposed detection improvements rather than implemented or production-tested detections.
