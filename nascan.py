#!/usr/bin/env python3
import ipaddress
import socket
import subprocess

def print_intro():
    ascii_art = r"""
 _______      _____    _________                     
 \      \    /  _  \  /   _____/ ____ _____    ____  
 /   |   \  /  /_\  \ \_____  \_/ ___\\__  \  /    \ 
/    |    \/    |    \/        \  \___ / __ \|   |  \
\____|__  /\____|__  /_______  /\___  >____  /___|  /
        \/         \/        \/     \/     \/     \/                               
    """
    print(ascii_art)
    print("Welcome to NAScan - Network & Port Analyzer\n")

def is_alive(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "1", str(ip)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except:
        return False

def get_device_info(ip):
    try:
        hostname = socket.gethostbyaddr(str(ip))[0]
    except:
        hostname = "Unknown"

    try:
        output = subprocess.check_output(["ip", "neigh", "show", str(ip)], stderr=subprocess.DEVNULL).decode()
        parts = output.split()
        mac = parts[4] if len(parts) >= 5 else "Unknown"
    except:
        mac = "Unknown"

    return hostname, mac

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            if sock.connect_ex((str(ip), port)) == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                open_ports.append((port, service))
            sock.close()
        except:
            pass
    return open_ports

def main():
    print_intro()
    network = input("Enter IP/CIDR (e.g. 192.168.1.0/24): ").strip()
    ports = range(1, 1025)  # default scan range
    net = ipaddress.ip_network(network, strict=False)

    for ip in net.hosts():
        print(f"\nHost: {ip}")
        if is_alive(ip):
            hostname, mac = get_device_info(ip)
            print(f"  Status: Alive")
            print(f"  Hostname: {hostname}")
            print(f"  MAC: {mac}")
            open_ports = scan_ports(ip, ports)
            if open_ports:
                print("  Open Ports:")
                for port, service in open_ports:
                    print(f"    {port}/tcp ({service})")
            else:
                print("  No open ports found.")
        else:
            print("  Status: Inactive")

    print("\nScan complete. Developed by Reaper032")

if __name__ == "__main__":
    main()

