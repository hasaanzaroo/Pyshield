from firewall.rules import FirewallRule


def load_default_rules():
    return [
        FirewallRule(
            name="Block SSH",
            action="BLOCK",
            protocol="TCP",
            destination_port=22,
            priority=1,
        ),
        FirewallRule(
            name="Block Telnet",
            action="BLOCK",
            protocol="TCP",
            destination_port=23,
            priority=2,
        ),
        FirewallRule(
            name="Allow HTTPS",
            action="ALLOW",
            protocol="TCP",
            destination_port=443,
            priority=100,
        ),
    ]