import ipaddress
import argparse

from .config import DEFAULT_PORT_RANGE_LOW, DEFAULT_PORT_RANGE_HIGH, MAX_PORT_RANGE_HIGH, DEFAULT_OUTPUT_FILENAME

def parse_args():
    """
    Parse CLI Arguments.
    Returning a dictionary with [ ip, port_low, and port_high ]
    """
    
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    
    parser.add_argument(
        "-i", "--ip",
        help="Target IP address"
    )
    
    parser.add_argument(
        "-p", "--ports",
        help="Port range to scan in the form low-high"
    )
    
    parser.add_argument(
        "-o", "--out",
        help="Name of output file"
    )
    
    parser.add_argument(
        "-d", "--use-defaults",
        help="Use default port ranges to bypass prompting",
        action="store_true"
    )
    
    args = parser.parse_args()
    return vars(args)
    
def get_ip(cli_ip=None):
    """
    Get the target IP from either CLI or by prompting the user.
    """
    
    ip = cli_ip
    while (not ip):
        ip = input("Enter target IP address: ").strip()
    
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"Invalid IP Address: {ip}")
        return get_ip(None)
    
    return ip

def get_port_range(cli_ports=None, use_defaults=False):
    """
    Get the target port range from either CLI or by prompting the user.
    """
    if (use_defaults and cli_ports is None):
        return range(DEFAULT_PORT_RANGE_LOW, DEFAULT_PORT_RANGE_HIGH+1)
    
    if (cli_ports):
        try:
            low_str, high_str = cli_ports.split("-")
            low, high = int(low_str), int(high_str)
        except Exception:
            print(f"Invalid port range or format: {cli_ports}")
            return get_port_range(None, False)
    else:
        try:
            low = int(input(f"Enter lowest port to scan (Default: {DEFAULT_PORT_RANGE_LOW}): ") or DEFAULT_PORT_RANGE_LOW)
            high = int(input(f"Enter highest port to scan (Default: {DEFAULT_PORT_RANGE_HIGH}): ") or DEFAULT_PORT_RANGE_HIGH)
        except ValueError:
            print("Invalid port number entered")
            return get_port_range(None, False)
        
    if (low < 0 or high > MAX_PORT_RANGE_HIGH or low > high):
        print(f"Invalid Port Range. Must be 0-{MAX_PORT_RANGE_HIGH} and low <= high.")
        return get_port_range(None, False)
    
    return range(low, high+1)

def get_output_filename(cli_out=None, use_defaults=False):
    """
    Get the output file name from either CLI or by prompting the user.
    """
    
    if (use_defaults and cli_out is None):
        return DEFAULT_OUTPUT_FILENAME
    
    out = cli_out
    
    if (not out):
        out = input(f"Enter output filename (Default: '{DEFAULT_OUTPUT_FILENAME}'): ").strip() or DEFAULT_OUTPUT_FILENAME
    
    if not out.endswith(".txt"):
        out += ".txt"
    
    return out

def get_scan_config():
    """
    Main function to fetch necessary arguments for scan. Returns (ip, port_range)
    """
    args = parse_args()
    ip = get_ip(args.get("ip"))
    port_range = get_port_range(args.get("ports"), args.get("use_defaults"))
    out = get_output_filename(args.get("out"), args.get("use_defaults"))
    
    return ip, port_range, out
