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
<img width="1288" height="562" alt="Screenshot (521)" src="https://github.com/user-attachments/assets/8f9fa591-9f79-4cfd-97d8-ca55bf15fed6" /><img width="1286" height="573" alt="Screenshot (522)" src="https://github.com/user-attachments/assets/1df32d2b-0069-465a-9f49-b82c649984b0" />
