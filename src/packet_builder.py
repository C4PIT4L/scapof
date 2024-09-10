import re
from scapy.layers.l2 import ARP


class PacketBuilder:
    def __init__(self):
        pass

    @staticmethod
    def validate_mac(mac):
        mac_pattern = r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$"
        return re.match(mac_pattern, mac) is not None

    @staticmethod
    def validate_ip(ip):

        ip_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
                     r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
                     r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
                     r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        return re.match(ip_pattern, ip) is not None

    def build_arp_packet(self, src_mac, dst_mac, src_ip, dst_ip, op=1):
        if not self.validate_mac(src_mac):
            raise ValueError(f"Invalid source MAC address: {src_mac}")
        if not self.validate_mac(dst_mac):
            raise ValueError(f"Invalid destination MAC address: {dst_mac}")

        # Validate IP addresses
        if not self.validate_ip(src_ip):
            raise ValueError(f"Invalid source IP address: {src_ip}")
        if not self.validate_ip(dst_ip):
            raise ValueError(f"Invalid destination IP address: {dst_ip}")

        # Validate operation type (op)
        if op not in [1, 2]:
            raise ValueError(f"Invalid ARP operation: {op}. Use 1 for request, 2 for reply.")

        # Build the ARP packet using Scapy
        arp_packet = ARP(psrc=src_ip, pdst=dst_ip, hwsrc=src_mac, hwdst=dst_mac, op=op)

        return arp_packet
