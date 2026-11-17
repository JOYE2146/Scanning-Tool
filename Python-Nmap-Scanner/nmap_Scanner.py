#2
import nmap
def port_scanner(target, start_port, end_port):

    scanner = nmap.PortScanner()

    print("=" * 50)
    print("       PYTHON NMAP PORT SCANNER")
    print("=" * 50)

    print(f"Target IP: {target}")

    port_range = f"{start_port}-{end_port}"

    scanner.scan(
        hosts=target,
        ports=port_range,
        arguments="-sT"
    )

    for host in scanner.all_hosts():

        print(f"\nHost: {host}")
        print(f"State: {scanner[host].state()}")

        for protocol in scanner[host].all_protocols():

            print(f"\nProtocol: {protocol}")

            for port in sorted(scanner[host][protocol].keys()):

                info = scanner[host][protocol][port]

                print(f"Port: {port}")
                print(f"State: {info['state']}")
                print(f"Service: {info['name']}")
                print("-" * 30)

    print("Scanning completed.")


if __name__ == "__main__":

    target = input("Enter Target IP: ")

    start_port = int(input("Enter Starting Port: "))

    end_port = int(input("Enter Ending Port: "))

    if 1 <= start_port <= end_port <= 65535:

        port_scanner(target, start_port, end_port)

    else:

        print("Invalid port range.")
