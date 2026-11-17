#1
import socket
def port_scanner(target, start_port, end_port):
    print(f"\nScanning Target: {target}")
    print("-" * 40)
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()
    print("-" * 40)
    print("Scanning completed.")
if __name__ == "__main__":

    target = input("Enter Target IP: ")
    start_port = int(input("Enter Starting Port: "))
    end_port = int(input("Enter Ending Port: "))

    port_scanner(target, start_port, end_port)