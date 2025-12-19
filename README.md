# SSH Log Analyzer

Python tool to detect SSH brute-force attempts from Linux authentication logs.

---

## What it does

- Parses SSH authentication logs
- Detects failed login attempts using regex
- Extracts attacker IPs
- Counts attempts per IP
- Outputs structured results
- Includes automated tests for parser robustness

This project focuses on **defensive security**, log analysis, and detection logic.

---

## Quickstart

### Requirements

- Python 3.11+
- Linux / WSL
- Git

---

## Setup

```bash
git clone https://github.com/sauldmorales/ssh-log-analyzer.git
cd ssh-log-analyzer

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

## Run analyzer

python -m src.ssh_analyzer sample_data/auth.log

## Example output

Attacks detected: 40
Top attacker: 192.168.1.5 (12 attempts)

## Run tests

python -m pytest -q

## Generate sample logs

python generate_dummy_logs.py

##Security notes

Do NOT upload real server logs

Do NOT commit secrets or credentials

Only use dummy or sanitized data in sample_data/

## This repository is for educational and defensive security purposes only.
