import socket
from datetime import datetime

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