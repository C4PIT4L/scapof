from scapy.sendrecv import send
from src.packet_builder import PacketBuilder

class SpoofingEngine:
    def __init__(self):
        self.packet_builder = PacketBuilder()

    def send_arp_spoof(self, src_mac, dst_mac, src_ip, dst_ip, op=1):
        try:
            arp_packet = self.packet_builder.build_arp_packet(
                src_mac=src_mac,
                dst_mac=dst_mac,
                src_ip=src_ip,
                dst_ip=dst_ip,
                op=op
            )
            # Send the packet on the network
            send(arp_packet, verbose=False)
            print(f"ARP packet sent: {arp_packet.summary()}")
        except ValueError as e:
            print(f"Error: {e}")


    def build_preview(self, src_mac, dst_mac, src_ip, dst_ip, op=1):
        # Build ARP packet without sending it (for dry-run)
        try:
            arp_packet = self.packet_builder.build_arp_packet(
                src_mac=src_mac,
                dst_mac=dst_mac,
                src_ip=src_ip,
                dst_ip=dst_ip,
                op=op
            )
            return arp_packet
        except ValueError as e:
            print(f"Error: {e}")
            return None


