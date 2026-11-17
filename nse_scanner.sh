
#!/bin/bash
echo "=================================="
echo "       NMAP NSE SCANNER"
echo "=================================="
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP_ADDRESS> <NSE_SCRIPT>"
    echo "Example: $0 192.168.1.1 http-title"
    exit 1
fi
IP_ADDRESS="$1"
NSE_SCRIPT="$2"
if ! [[ "$IP_ADDRESS" =~ ^([0-9]{1,3}\.){3}[0-9]{1,3}$ ]]; then
    echo "Error: Invalid IPv4 address format."
    exit 1
fi
if ! command -v nmap >/dev/null 2>&1; then
    echo "Error: Nmap is not installed."
    exit 1
fi
echo ""
echo "Target IP: $IP_ADDRESS"
echo "NSE Script: $NSE_SCRIPT"
echo "Starting Nmap scan..."
echo "----------------------------------"
nmap --script "$NSE_SCRIPT" "$IP_ADDRESS"
echo "----------------------------------"
echo "Nmap scan completed."
