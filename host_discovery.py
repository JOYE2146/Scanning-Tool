
import socket
import ipaddress
import psutil
import subprocess
import platform
def get_local_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        return local_ip

    except Exception:
        return "127.0.0.1"

    finally:
        sock.close()


def get_gateway():
    gateways = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    try:
        if platform.system() == "Windows":
            output = subprocess.check_output(
                ["ipconfig"],
                text=True
            )

            for line in output.splitlines():
                if "Default Gateway" in line:
                    gateway = line.split(":")[-1].strip()

                    if gateway:
                        return gateway

        else:
            output = subprocess.check_output(
                ["ip", "route", "show", "default"],
                text=True
            )

            for line in output.splitlines():
                if line.startswith("default"):
                    return line.split()[2]

    except Exception:
        pass

    return "Gateway not found"


def get_ip_class(ip):

    first_octet = int(ip.split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"

    elif first_octet == 127:
        return "Loopback"

    elif 128 <= first_octet <= 191:
        return "Class B"

    elif 192 <= first_octet <= 223:
        return "Class C"

    elif 224 <= first_octet <= 239:
        return "Class D"

    elif 240 <= first_octet <= 255:
        return "Class E"

    return "Invalid IP"


def discover_hosts(network):

    print("\nHOST DISCOVERY STARTED")
    print("-" * 50)

    system = platform.system()

    for ip in network.hosts():

        if system == "Windows":
            command = ["ping", "-n", "1", "-w", "500", str(ip)]
        else:
            command = ["ping", "-c", "1", "-W", "1", str(ip)]

        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print(f"[ACTIVE] {ip}")


def main():

    print("=" * 50)
    print("       PYTHON HOST DISCOVERY TOOL")
    print("=" * 50)

    local_ip = get_local_ip()

    gateway = get_gateway()

    print("\nNETWORK INFORMATION")
    print("-" * 50)

    print("Local IP Address:", local_ip)

    print("Gateway IP Address:", gateway)

    try:
        ip = ipaddress.IPv4Address(local_ip)

        print("IP Class:", get_ip_class(local_ip))

    except ipaddress.AddressValueError:
        print("Invalid local IP address")
        return

    if local_ip == "127.0.0.1":
        print("Cannot determine the connected network.")
        return

    print("\nHOST DISCOVERY")

    try:
        network_input = input(
            "Enter network CIDR (e.g. 192.168.1.0/24): "
        )

        network = ipaddress.IPv4Network(
            network_input,
            strict=False
        )

        discover_hosts(network)

    except ValueError:
        print("Invalid network address.")


if __name__ == "__main__":
    main()
#Host Discovery Tool – Short Theory Notes
# 1. What is Host Discovery?
# Host discovery is the process of identifying active devices connected to a network.

# Purpose:
# - Identify active devices.
# - Discover network IP addresses.
# - Check network availability.
# - Support network administration.
# 2. What is an IP Address?
# An IP address is a logical numerical address used to identify devices on a network.

# Example: 192.168.1.100
# 3. What is IPv4?
# IPv4 (Internet Protocol Version 4) uses a 32-bit address divided into four octets.

# Example: 192.168.1.1
# 4. IP Address Classes
# Class	First octet	Default subnet mask
# A	1–126	                255.0.0.0
# B	128–191	                255.255.0.0
# C	192–223	                255.255.255.0
# D	224–239	                  Multicast
# E	240–255	                Experimental

# 5. What is a Default Gateway?
# A default gateway is usually a router that forwards data from a local network to other networks or the internet.

# Example: 192.168.1.1
# 6. What is a Subnet Mask?
# A subnet mask separates the network portion and host portion of an IP address.

# Example: 255.255.255.0
# 7. What is CIDR?
# CIDR (Classless Inter-Domain Routing) represents a network using a prefix length.

# Example: 192.168.1.0/24.
# 8. What is Ping?
# Ping is a network command used to test connectivity between devices using ICMP.
# ping 192.168.1.1


# 9. What is ICMP?
# ICMP (Internet Control Message Protocol) is used to exchange network error and diagnostic messages.
# 10. What is TCP?
# TCP (Transmission Control Protocol) is a connection-oriented protocol that provides reliable and ordered data transmission.
# 11. What is UDP?
# UDP (User Datagram Protocol) is a connectionless protocol that provides low-overhead data transmission without guaranteed delivery.
# 12. Difference Between TCP and UDP
# TCP	UDP
# Connection-oriented	Connectionless
# Reliable	No guaranteed delivery
# Uses acknowledgments	No acknowledgments
# More overhead	Less overhead

# 13. What is Python Socket?
# The socket library is a built-in Python module used for network communication.
# import socket



# 14. What is Python IPAddress?
# The ipaddress library is used to validate and manipulate IPv4 and IPv6 addresses.
# import ipaddress



# 15. What is PSUtil?
# PSUtil is a Python library used to retrieve system and network interface information.
# py -m pip install psutil


# 16. What is the Difference Between Host Discovery and Port Scanning?
# Host Discovery	           Port Scanning
# Identifies active devices  	Identifies accessible ports
# Checks host availability	    Checks port status
# Focuses on devices	       Focuses on services

# 17. Private IP Address Ranges
# Class	Private IP range
# A	10.0.0.0/8
# B	172.16.0.0/12
# C	192.168.0.0/16

# 18. Common Windows Networking Commands
# Command	             Purpose
# ipconfig	            Displays IP configuration
# ipconfig /all	        Displays detailed network information
# ping	                Tests connectivity
# arp -a	             Displays ARP cache
# route print	        Displays routing table
# tracert	             Traces network route#