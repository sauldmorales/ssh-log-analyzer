# SSH Log Analyzer

Python tool to detect and analyze SSH brute-force attempts from Linux auth logs.

## What this project does
- Parses SSH authentication logs
- Detects failed login attempts using regex
- Extracts attacker IPs
- Counts attempts per IP
- Outputs a structured JSON report
- Includes unit tests for the parser logic

## Why this matters
SSH brute-force attacks are one of the most common entry points in compromised servers.
This tool demonstrates basic threat detection, log analysis, and defensive thinking.

## Technologies used
- Python 3
- Regex
- Git
- pytest

## How to run
```bash
python src/ssh_analyzer.py
Note: This project uses sample log files for demonstration purposes only.
