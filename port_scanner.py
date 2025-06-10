import socket

def scan_ports(target, start, end):
    print(f"\n[+] Scanning {target} from port {start} to {end}...")
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"[+] Port {port} is open ({service.upper()})")
    print("[-] Scan completed.")