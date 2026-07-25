from firewall.rules import FirewallRule


def match_rule(packet, rule: FirewallRule):
    """
    Returns True if the packet matches the rule.
    """

    if not rule.enabled:
        return False

    if rule.protocol and packet.protocol != rule.protocol:
        return False

    if rule.source_ip and packet.source_ip != rule.source_ip:
        return False

    if rule.destination_ip and packet.destination_ip != rule.destination_ip:
        return False

    if rule.source_port and packet.source_port != rule.source_port:
        return False

    if rule.destination_port and packet.destination_port != rule.destination_port:
        return False

    return True