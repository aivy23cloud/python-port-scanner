import socket as Socket

from threading import Thread, Lock

open_ports = []
closed_ports = []

lock = Lock()

def scan_port(ip, port):
    try:
        sock = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((ip, port))
        sock.close()
        
        with lock:
            if (result == 0):
                open_ports.append(port)
            else:
                closed_ports.append(port)
    except:
        with lock:
            closed_ports.append(port)
    
def display_port_lists():
    print("Open Ports:")
    for port in open_ports:
        print(port)

target_ip = input("Enter the target IP address: ")
port_range = range(1, 1025)

threads = []
for port in port_range:
    thread = Thread(target=scan_port, args=(target_ip, port))
    threads.append(thread)
    
for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

display_port_lists()