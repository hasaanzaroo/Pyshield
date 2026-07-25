from scapy.all import sniff
from capture.parser import parse_packet
from capture.packet_queue import packet_queue


def handle_packet(pkt):
    parsed = parse_packet(pkt)

    if parsed:
        if not packet_queue.full():
            packet_queue.put(parsed)

        print(parsed)


def start_sniffer(interface=None):
    print("Starting packet capture...\n")

    sniff(
        iface=interface,
        prn=handle_packet,
        store=False
    )


if __name__ == "__main__":
    start_sniffer()