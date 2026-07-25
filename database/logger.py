from database.db import db
from database.models import PacketLog


def log_packet(packet, decision, matched_rule):
    log = PacketLog(
        timestamp=packet.timestamp,
        source_ip=packet.source_ip,
        destination_ip=packet.destination_ip,
        protocol=packet.protocol,
        port=packet.destination_port,
        length=packet.length,
        decision=decision,
        matched_rule=matched_rule,
    )

    db.session.add(log)
    db.session.commit()