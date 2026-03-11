import socket as Socket

from threading import Thread, Lock
from queue import Empty, Queue
from .config import MAX_THREADS, DEFAULT_PORT_RANGE_LOW, DEFAULT_PORT_RANGE_HIGH, MAX_PORT_RANGE_HIGH

lock = Lock()

def scan_tcp_port(ip, port, open_ports):
    """
    Scans a specified TCP port on the given IP address and appends it to a table if it is open.
    """
    try:
        with Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
        
        if (result == 0):
            with lock:
                open_ports.append(port)
    except Exception:
        # We will log socket errors here
        pass
  
def worker(ip, port_queue, open_ports):
    while True:
        try:
            port = port_queue.get_nowait()
        except Empty:
            break
        
        scan_tcp_port(ip, port, open_ports)
        port_queue.task_done()

def scan_range(target_ip, port_range: range):
    """
    Perform a scan on the target ip address in the given port range.
    Returns a sorted list of open ports.
    """
    
    if (target_ip == None or port_range == None):
        raise ValueError("Target IP and port range cannot be None.")
    
    port_range = [p for p in port_range if p <= MAX_PORT_RANGE_HIGH]
    
    port_queue = Queue()
    open_ports = []
    
    for port in port_range:
        port_queue.put(port)
    
    threads = []
    for _ in range(MAX_THREADS):
        thread = Thread(target=worker, args=(target_ip, port_queue, open_ports))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
        
    port_queue.join()
    
    return sorted(open_ports)