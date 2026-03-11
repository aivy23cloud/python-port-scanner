from datetime import datetime
from scanner.input import get_scan_config
from scanner.scan import scan_range
from scanner.output import write_output_log
  
target_ip, port_range, output_file = get_scan_config()

print(f"\nScanning for open ports [{port_range.start} - {port_range.stop - 1}] on '{target_ip}'\n")

start_time = datetime.now()
open_ports = scan_range(target_ip, port_range)
end_time = datetime.now()

write_output_log(output_file, target_ip, port_range, open_ports, start_time, end_time)

print(f"\nScan completed in {end_time - start_time} seconds.")
print(f"Found {len(open_ports)} open port(s).")
print(f"Wrote output to '{output_file}'.")