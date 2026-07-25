from scapy.all import sniff

from capture.parser import parse_packet
from capture.packet_queue import packet_queue

from firewall.engine import FirewallEngine
from firewall.default_rules import load_default_rules


engine = FirewallEngine()

for rule in load_default_rules():
    engine.add_rule(rule)


def handle_packet(pkt):
    parsed = parse_packet(pkt)

    if parsed:
        decision, matched_rule = engine.evaluate(parsed)

        if not packet_queue.full():
            packet_queue.put(parsed)

        print(
            f"[{decision}] "
            f"{parsed.protocol} "
            f"{parsed.source_ip}:{parsed.source_port} -> "
            f"{parsed.destination_ip}:{parsed.destination_port} "
            f"Rule: {matched_rule}"
        )


def start_sniffer(interface=None):
    print("PyShield Firewall Simulator Started...\n")

    sniff(
        iface=interface,
        prn=handle_packet,
        store=False
    )


if __name__ == "__main__":
    start_sniffer()