# Python Port Scanner

A lightweight multithreaded port scanner written in Python that detects open ports on a target host. This project was made to gain a better understanding of core networking concepts and techniques such as sockets, port scanning, and multithreaded execution.

## Features

- Scan a range of TCP ports on a target IP address
- Detect open ports using Python sockets
- Multithreaded execution for quicker execution time
- Clean output and result display

## Example Output:

> Enter the target IP address: 192.168.1.1 <br>
> Enter the lowest port to scan (Default: 1): 1 <br>
> Enter the highest port to scan (Default: 1024): 1024 <br>
>
> Scanning for open ports [1 - 1024] on "192.168.1.1"...
> 
> Open Ports: <br>
> Port 53 OPEN
>
> Scan completed in 11.09 seconds...

## Installation Instructions:

Clone the repository: <br>
`git clone https://github.com/aivy23cloud/python-port-scanner.git`

Navigate to the project folder: <br>
`cd python-port-scanner`

#### Requires Python 3.8+

## Usage

### Executing with command line arguments

#### Execute the `main.py` file as so: <br>
`python main.py TARGET_IP PORT_RANGE_LOW PORT_RANGE_HIGH`
Failure to provide specific arguments will result in additional prompting
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

- Implement banner grabbing
- Quicker execution time


## Disclaimer

This tool is strictly intended for learning purposes on systems you are permitted to test or own.

![Python](https://img.shields.io/badge/python-3.13-blue)
![License](https://img.shields.io/badge/license-MIT-green)