# Log and Threat Analyser
A beginner-friendly Python project that reads login logs, detects suspicious IP addresses using a simple brute-force rule, saves a CSV report, and shows the results on a Streamlit dashboard.
 
 **Note:** All logs and IP addresses in this project are **fictional** and randomly generated. None of them belong to a real person or system.
 
---
 
## What it does
 
1. **Generates fake login logs** (successful logins, failed logins, accidental failures, and attacker activity) and saves them to `logs.txt`.
2. **Reads the log file** and counts failed login attempts per IP address.
3. **Flags suspicious IPs** based on how many times they failed to log in.
4. **Saves a CSV report** (`log_report.csv`) with each IP, its failed attempts, and its status.
5. **Displays a dashboard** with status cards, a data table, and a bar chart.
