from datetime import datetime

def write_output_log(filename, target_ip, port_range, open_ports, start_time, end_time):
    """
    Writes a detailed output log on the scan and its results.
    """
    
    with open(filename, "a") as f:
        f.write(f"SCAN STARTED AT: {start_time}\n")
        f.write(f"SCAN ENDED AT: {end_time}\n")
        f.write(f"TOTAL TIME RUNNING: {end_time - start_time}\n\n")
        
        f.write(f"TARGET IP: {target_ip}\n")
        f.write(f"TARGET PORTS: {port_range.start}-{port_range.stop - 1}\n\n")
        
        f.write(f"SCAN FOUND {len(open_ports)} OPEN PORT(S):\n")
        
        for port in open_ports:
            f.write(f"PORT {port} OPEN\n")
            
        f.write(f"\n")
        
    