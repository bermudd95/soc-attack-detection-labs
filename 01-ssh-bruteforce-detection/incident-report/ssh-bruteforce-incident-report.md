# Incident Report: Unauthorized SSH Brute-Force Attack Simulation

**Date of Incident:** March 5, 2025  
**Reporter:** Danny Bermudez  
**Target System:** Linux Virtual Machine (Ubuntu)  
**Attack Method:** SSH Brute-Force Attack  

---

## Summary

On March 5, 2025, a simulated SSH brute-force attack was conducted against a Linux virtual machine to evaluate the effectiveness of SSH security controls. The attack leveraged Hydra, a password-cracking utility, to attempt unauthorized access using a dictionary-based password list.

---

## Technical Details

- **Target IP Address:** 192.168.226.130  
- **Attack Origin:** Kali Linux (Attacker Machine)  
- **User Account Targeted:** `bob_victim`  
- **Tool Used:** Hydra  
- **Password List:** Custom weak-password dictionary  

### Command Executed

```bash
hydra -l bob_victim -P password_list.txt ssh://192.168.226.130 -V
