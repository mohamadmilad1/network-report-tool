
# Network Report Tool

A simple tool for network administrators to monitor and report the status of network devices.

## Features

- Scans a range of IP addresses in your network.
- Pings each IP address and reports if it’s online or offline.
- Saves the report in a CSV file (`network_report.csv`) for easy review.

## Requirements

- Python 3.x
- Operating system with support for the `ping` command (Windows, Linux, or MacOS)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohamadmilad1/network-report-tool.git
   ```

2. Navigate to the project directory:

   ```bash
   cd network-report-tool
   ```

## Usage

1. Open the `main.py` file and ensure the network range is set correctly. By default, the IP range is set to `192.168.48.0` to `192.168.51.255`. You can adjust this range by modifying the `scan_network()` function if your network setup is different.

2. Run the script:

   ```bash
   python main.py
   ```

3. The program will scan the specified IP range and generate a report in `network_report.csv` with the status of each IP (online or offline).

## Example

After running the script, a file named `network_report.csv` will be created in the same directory, containing entries similar to:

| IP Address      | Status |
|-----------------|--------|
| 192.168.48.1    | Online |
| 192.168.48.2    | Offline|
| 192.168.48.3    | Online |
| ...             | ...    |

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.




