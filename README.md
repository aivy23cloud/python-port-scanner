# Python Port Scanner

A lightweight multithreaded port scanner written in Python that detects open ports on a target host. This project was made to gain a better understanding of core networking concepts and techniques such as sockets, port scanning, and multithreaded execution.

## Features

- Scan a range of TCP ports on a target IP address
- Detect open ports using Python sockets
- Multithreaded execution for quicker execution time
- Detailed output logs of scan results
- Config file for easy customization
- Easy to use CLI arguments

## Example Output:

> Enter target IP address: 192.168.1.1 <br>
> Enter lowest port to scan (Default: 1): 1 <br>
> Enter highest port to scan (Default: 1024): 1024 <br>
> Enter output filename (Default: 'logs/port_scan_log.txt'): logs/log01.txt
>
> Scanning for open ports [1 - 1024] on '192.168.1.1'...
> 
> Scan completed in 0:00:02.022091 seconds. <br>
> Found 1 open port(s).
> Wrote output to 'logs/log01.txt'.

## Installation Instructions:

Clone the repository: <br>
`git clone https://github.com/aivy23cloud/python-port-scanner.git`

Navigate to the project folder: <br>
`cd python-port-scanner`

#### Requires Python 3.8+

## Usage

### Executing with command line arguments

#### Executing with command line arguments: <br>
You can provide the target IP, port range, and output filename directly. <br>
`python main.py --ip 192.168.1.1 --ports 1-1024 --out logs/log01.txt`
- `--ip`: Target IP address
- `--ports`: Port range in the form `low-high`
- `--out`: Output filename
- `--use-defaults`: Use the defaults from the config file where applicable

Any argument omitted without the `--use-defaults` flag will result in additional prompting.
<br>

### Executing without command line arguments

#### Execute the `main.py` file: <br>
`python main.py` <br>
Answer prompted questions unless a default is stated

## Learning Objectives

This project was built to strengthen my understanding of:

- Basic python syntax and usage
- Utilization of multithreading for improved performance
- Basic networking concepts such as sockets and ports
- Secure input validation and error handling

## Future Improvements

- Implement banner grabbing and service detection


## Disclaimer

This tool is strictly intended for learning purposes on systems you are permitted to test or own.

![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)