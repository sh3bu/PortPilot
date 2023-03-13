# PortPilot

PortPilot is a Python-based port scanning tool that allows users to quickly and efficiently scan a target machine for open ports. Built using socket programming, this tool supports both TCP and UDP scans and provides verbose output to make it easy for users to interpret the scan results.

#### Usage
To use PortPilot, simply run the portpilot.py file from the command line with the appropriate arguments:

```python portpilot.py <ip_address> <start_port> <end_port> <scan_type>```

Where:

- <ip_address> is the IP address of the target machine
- <start_port> is the starting port number for the scan
- <end_port> is the ending port number for the scan
- <scan_type> is the type of scan to perform (either tcp or udp)

For example, to scan the IP address 192.168.1.1 for open TCP ports between 1 and 1024, run the following command:

```python portpilot.py 192.168.1.1 1 1024 tcp```

#### Features
PortPilot includes the following features:

- Support for TCP and UDP scans
- Multi-threading for improved scan speed
- Verbose output for easy interpretation of scan results
- Ability to specify a range of ports to scan

#### Installation
To install PortPilot, simply clone the repository and install the required dependencies:

```
git clone https://github.com/sh3bu/PortPilot.git
cd PortPilot
pip install -r requirements.txt
```

