import random

# Simula formato estándar de Ubuntu
TEMPLATE_FAIL = "Dec 14 {time} PREDATORF4 sshd[{pid}]: Failed password for {user_type}{user} from {ip} port {port} ssh2"
TEMPLATE_ACCEPT = "Dec 14 {time} PREDATORF4 sshd[{pid}]: Accepted password for {user} from {ip} port {port} ssh2"

ips = ["192.168.1.5", "10.0.0.2", "45.33.22.11", "211.12.33.44"]
users = ["root", "admin", "saul", "support", "ubuntu"]

with open("sample_data/ssh_logs.txt", "w") as f:
    for i in range(50):
        h = f"{random.randint(0,23):02}"
        m = f"{random.randint(0,59):02}"
        s = f"{random.randint(0,59):02}"
        pid = random.randint(1000, 9999)
        ip = random.choice(ips)
        port = random.randint(1024, 65535)
        
        if random.random() < 0.8:
            user = random.choice(users)
            user_type = "invalid user " if random.random() < 0.5 else ""
            line = TEMPLATE_FAIL.format(time=f"{h}:{m}:{s}", pid=pid, user_type=user_type, user=user, ip=ip, port=port)
        else:
            line = TEMPLATE_ACCEPT.format(time=f"{h}:{m}:{s}", pid=pid, user="saul", ip="192.168.1.50", port=port)
            
        f.write(line + "\n")

print("✅ sample_data/ssh_logs.txt generado con éxito.")
