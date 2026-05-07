import socket
import threading
import queue
import json
import time
from datetime import datetime
from flask import Flask, render_template, request, Response, jsonify
 
app = Flask(__name__)
 
SERVICES = {
    20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 67: "DHCP Server", 68: "DHCP Client", 69: "TFTP", 80: "HTTP",
    110: "POP3", 119: "NNTP", 123: "NTP", 135: "MS RPC", 137: "NetBIOS NS",
    138: "NetBIOS DG", 139: "NetBIOS Session", 143: "IMAP", 161: "SNMP",
    194: "IRC", 389: "LDAP", 443: "HTTPS", 445: "SMB/CIFS", 465: "SMTPS",
    514: "Syslog", 515: "LPD/LPR", 587: "SMTP Submit", 636: "LDAPS",
    993: "IMAPS", 995: "POP3S", 1080: "SOCKS Proxy", 1433: "MS SQL Server",
    1521: "Oracle DB", 1723: "PPTP VPN", 2049: "NFS", 2181: "Zookeeper",
    3000: "Node.js Dev", 3306: "MySQL", 3389: "RDP", 4200: "Angular Dev",
    5000: "Flask Dev", 5432: "PostgreSQL", 5900: "VNC", 6379: "Redis",
    6443: "Kubernetes API", 7077: "Apache Spark", 8080: "HTTP Alt",
    8443: "HTTPS Alt", 8888: "Jupyter Notebook", 9000: "PHP-FPM",
    9090: "Prometheus", 9200: "Elasticsearch", 9300: "Elasticsearch Cluster",
    11211: "Memcached", 27017: "MongoDB", 27018: "MongoDB Shard",
    50070: "Hadoop NameNode",
}
 
active_scans = {}

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")

        sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to server.")

def main():
    print("Simple Python Port Scanner")
    print("--------------------------")

    target = input("Enter target IP address: ")

    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}")
    print("Started at:", datetime.now())
    print("--------------------------")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("--------------------------")
    print("Scan completed.")

if __name__ == "__main__":
    main()
