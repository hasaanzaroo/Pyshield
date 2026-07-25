from datetime import datetime

from scapy.layers.inet import IP, TCP, UDP, ICMP

from capture.packet import Packet


def parse_packet(pkt):
    if IP not in pkt:
        return None

    protocol = "OTHER"
    source_port = None
    destination_port = None

    if TCP in pkt:
        protocol = "TCP"
        source_port = pkt[TCP].sport
        destination_port = pkt[TCP].dport

    elif UDP in pkt:
        protocol = "UDP"
        source_port = pkt[UDP].sport
        destination_port = pkt[UDP].dport

    elif ICMP in pkt:
        protocol = "ICMP"

    return Packet(
        timestamp=datetime.now(),
        source_ip=pkt[IP].src,
        destination_ip=pkt[IP].dst,
        protocol=protocol,
        source_port=source_port,
        destination_port=destination_port,
        length=len(pkt)
    )