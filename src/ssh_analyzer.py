import re
import json
import sys
import argparse
from datetime import datetime

# PATRONES REGEX (Filtros)
LOG_PATTERN = re.compile(r'^(?P<timestamp>\w{3}\s+\d+\s\d{2}:\d{2}:\d{2})\s+(?P<host>\S+)\s+sshd\[(?P<pid>\d+)\]:\s+(?P<message>.*)$')
FAILED_PATTERN = re.compile(r'Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\S+) port')

def parse_logs(log_file, output_file):
    report = {
        "generated_at": datetime.now().isoformat(),
        "total_lines_scanned": 0,
        "failed_attempts": 0,
        "attackers_ip": {},
        "target_users": {}
    }

    print(f"[*] Analizando {log_file}...")

    try:
        with open(log_file, 'r') as f:
            for line in f:
                report["total_lines_scanned"] += 1
                line = line.strip()

                # Filtro 1: Estructura base
                match = LOG_PATTERN.match(line)
                if not match: continue
                
                message = match.group('message')

                # Filtro 2: Fallos de password
                fail_match = FAILED_PATTERN.search(message)
                if fail_match:
                    report["failed_attempts"] += 1
                    data = fail_match.groupdict()
                    
                    # Contadores
                    ip = data['ip']
                    user = data['user']
                    report["attackers_ip"][ip] = report["attackers_ip"].get(ip, 0) + 1
                    report["target_users"][user] = report["target_users"].get(user, 0) + 1

        # Exportar JSON
        with open(output_file, 'w') as out:
            json.dump(report, out, indent=4)
            
        print(f"✅ Reporte generado: {output_file}")
        print(f"   -> Ataques detectados: {report['failed_attempts']}")

    except FileNotFoundError:
        print(f"❌ No encuentro el archivo: {log_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True)
    parser.add_argument("--outfile", required=True)
    args = parser.parse_args()
    parse_logs(args.infile, args.outfile)
