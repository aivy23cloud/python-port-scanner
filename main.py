import sys as Sys
import socket as Socket
import ipaddress
import time

from threading import Thread, Lock
from queue import Empty, Queue

#Basic Config Settings
MAX_THREADS = 100

DEFAULT_PORT_RANGE_LOW = 1
DEFAULT_PORT_RANGE_HIGH = 1024

open_ports = []
lock = Lock()
port_queue = Queue()

def scan_tcp_port(ip, port):
    try:
        with Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
        
        if (result == 0):
            with lock:
                open_ports.append(port)
    except Exception:
        exit()
        return
    
def print_open_ports():
    if (len(open_ports) == 0):
        print("No open ports found.")
        return
    
    print("Open Ports:")
    
    for port in sorted(open_ports):
        print(f"Port {port} OPEN")
        
def get_scan_config():
    try:
        ip = Sys.argv[1]
    except IndexError:
        ip = input("Enter the target IP address: ")
        
    try:
       ipaddress.ip_address(ip)
    except ValueError:
        print("Invalid IP Address")
        exit()
        
    try:
        port_range_low = int(Sys.argv[2])
    except IndexError:
        raw = input(f"Enter the lowest port to scan (Default: {DEFAULT_PORT_RANGE_LOW}): ").strip()
        port_range_low = int(raw) if raw else DEFAULT_PORT_RANGE_LOW
    except ValueError:
        port_range_low = DEFAULT_PORT_RANGE_LOW
        
    try:
        port_range_high = int(Sys.argv[3])
    except IndexError:
        raw = input(f"Enter the lowest port to scan (Default: {DEFAULT_PORT_RANGE_HIGH}): ").strip()
        port_range_high = int(raw) if raw else DEFAULT_PORT_RANGE_HIGH
    except ValueError:
        port_range_high = DEFAULT_PORT_RANGE_HIGH
        
    if (port_range_low > port_range_high):
        print("Invalid Port Range: High must be greater than low")
        exit()
        
    if (port_range_low < 0):
        print("Invalid Port Range: Low must be greater than 0")
        exit()
        
    if (port_range_high > 65535):
        print("Invalid Port Range: High must be lower than 65,535")
        exit()
        
    return ip, range(port_range_low, port_range_high + 1)

def worker(ip):
    while True:
        try:
            port = port_queue.get_nowait()
        except Empty:
            break
        
        scan_tcp_port(ip, port)
        port_queue.task_done()

target_ip, port_range = get_scan_config()

for port in port_range:
    port_queue.put(port)

print(f'\nScanning for open ports [{port_range.start} - {port_range.stop - 1}] on "{target_ip}"...\n')
start = time.time()

threads = []
for _ in range(MAX_THREADS):
    thread = Thread(target=worker, args=(target_ip,))
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
    
port_queue.join()

print_open_ports()
print(f"\nScan completed in {time.time() - start:.2f} seconds...")