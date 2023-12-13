import scapy.all as scspy
from argparse import ArgumentParser
from art import tprint
import re
from manuf import manuf
import requests

def options():
    parser = ArgumentParser()
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        help="Target IP address"
    )

    options = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify an IP address, use --help for more info.")

    if not re.match(r"^\d{1,3}(\.\d{1,3}){3}(\/24)?$", options.target):
        parser.error("[-] Invalid IP address, use --help for more info.")

    if not re.search(r"/24$", options.target):
        options.target += "/24"

    return options.target

def scan(ip):
    arp_request = scspy.ARP(pdst=ip)
    broadcast = scspy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scspy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        mac_address = element[1].hwsrc
        try:
            vendor = requests.get(f'https://api.macvendors.com/{mac_address}').text
        except requests.exceptions.RequestException:
            vendor = "Unknown"
        client_dict = {"ip": element[1].psrc, "mac": mac_address, "vendor": vendor}
        clients_list.append(client_dict)

    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\t\tCompany\n---------------------------------------------------------")
    for client in results_list:
        print(f'{client["ip"]}\t\t{client["mac"]}\t{client["vendor"]}')

tprint("NetScanner", font="slant")

target_ip = options()

if not re.search(r"/24$", target_ip):
    target_ip += "/24"

scan_result = scan(target_ip)
print_result(scan_result)
