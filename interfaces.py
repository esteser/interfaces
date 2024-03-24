#!/usr/bin/env python3
import yaml

def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines

def generate_interfaces(port_list, ip_list):
    interfaces = []
    for port_number, ip_address in zip(port_list, ip_list):
        interface = {
            "interface_type": "routed",
            "name": "ethernet",
            "security_zone": "",
            "details": {
                "description": "link to leaf",
                "port": port_number,
                "bandwidth": "100G",
                "ip_mtu": 9100,
                "ip_unnumbered": None,
                "ipv4_prefix": {
                    "primary": ip_address + "/24",
                    "secondary": "",
                    "virtual": ""
                },
                "mtu": 9100,
                "speed": "100G",
                "shutdown": False,
                "sub": None,
                "vrf": "gen"
            }
        }
        interfaces.append(interface)
    return interfaces

def write_to_yaml(interfaces):
    with open('interfaces.yml', 'w') as file:
        yaml.dump({"interfaces": interfaces}, file, default_flow_style=False)

def main():
    # Read IP addresses from file
    ip_addresses_file = 'ip_addresses.txt'
    ip_addresses = read_file_lines(ip_addresses_file)

    # Read port numbers from file
    port_numbers_file = 'port_numbers.txt'
    port_numbers = read_file_lines(port_numbers_file)

    interfaces = generate_interfaces(port_numbers, ip_addresses)

    write_to_yaml(interfaces)

if __name__ == "__main__":
    main()
