from dataclasses import dataclass
from datetime import datetime


@dataclass
class Packet:
    timestamp: datetime
    source_ip: str
    destination_ip: str
    protocol: str
    source_port: int | None
    destination_port: int | None
    length: int