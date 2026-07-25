from firewall.matcher import match_rule
from firewall.policy import DEFAULT_POLICY


class FirewallEngine:

    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)
        self.rules.sort(key=lambda r: r.priority)

    def evaluate(self, packet):

        for rule in self.rules:

            if match_rule(packet, rule):
                return rule.action, rule.name

        return DEFAULT_POLICY, "Default Policy"