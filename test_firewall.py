from datetime import datetime

from capture.packet import Packet
from firewall.engine import FirewallEngine
from firewall.rules import FirewallRule


engine = FirewallEngine()

engine.add_rule(
    FirewallRule(
        name="Block SSH",
        action="BLOCK",
        protocol="TCP",
        destination_port=22,
        priority=1,
    )
)

packet = Packet(
    timestamp=datetime.now(),
    source_ip="192.168.1.10",
    destination_ip="192.168.1.20",
    protocol="TCP",
    source_port=54321,
    destination_port=22,
    length=64,
)

decision, rule = engine.evaluate(packet)

print(f"Decision: {decision}")
print(f"Matched Rule: {rule}")