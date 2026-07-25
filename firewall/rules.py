from dataclasses import dataclass


@dataclass
class FirewallRule:
    name: str
    action: str
    protocol: str | None = None
    source_ip: str | None = None
    destination_ip: str | None = None
    source_port: int | None = None
    destination_port: int | None = None
    enabled: bool = True
    priority: int = 100