import os
import csv

def ping_device(ip):
    response = os.system(f"ping -c 1 {ip}")
    return response == 0

def scan_network():
    devices = []

    print("Scanning network...")
    for i in range(48, 52):  # Range of 48 to 51
        for j in range(0, 256):  # Range of 0 to 255
            ip = f"192.168.{i}.{j}"
            if ping_device(ip):
                print(f"{ip} is online")
                devices.append({"IP Address": ip, "Status": "Online"})
            else:
                print(f"{ip} is offline")
                devices.append({"IP Address": ip, "Status": "Offline"})
    
    return devices

def save_report(devices):
    with open("network_report.csv", "w", newline="") as csvfile:
        fieldnames = ["IP Address", "Status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(devices)

    print("Report saved as 'network_report.csv'")

if __name__ == "__main__":
    devices = scan_network()
    save_report(devices)
