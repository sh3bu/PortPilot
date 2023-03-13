import socket
import argparse
import threading

def scan_port(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except:
        pass

def scan(ip_address, start_port, end_port, scan_type):
    print(f"Scanning {ip_address}...")
    for port in range(start_port, end_port + 1):
        if scan_type == "tcp":
            t = threading.Thread(target=scan_port, args=(ip_address, port))
            t.start()
        elif scan_type == "udp":
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            result = sock.sendto(b"SYN", (ip_address, port))
            try:
                recv, svr = sock.recvfrom(255)
                print(f"Port {port} is open")
            except:
                pass
            sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Port Scanner Tool")
    parser.add_argument("ip_address", help="IP address to scan")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    parser.add_argument("scan_type", choices=["tcp", "udp"], help="Scan type (tcp or udp)")
    args = parser.parse_args()

    scan(args.ip_address, args.start_port, args.end_port, args.scan_type)
