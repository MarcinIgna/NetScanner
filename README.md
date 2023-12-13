# NetScanner

NetScanner is a Python application that scans the network for connected devices and displays their IP and MAC addresses, as well as the company that manufactured the device.

## Installation

Before you can run NetScanner, you need to install the required Python packages. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage

To use NetScanner, navigate to the directory where you have saved the script and run the following command:

```bash
python NetScanner.py --target 192.168.0.0/24
```

This will scan all devices in the IP range 192.168.0.0 to 192.168.0.255. You can replace `192.168.0.0/24` with the IP range you want to scan.
## Note

Due to varying internet connections and device connectivity, you may need to run the scan multiple times to get a complete list of all devices in the specified IP range. If a device is not showing up, try running the scan again.