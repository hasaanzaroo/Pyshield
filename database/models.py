from database.db import db


class FirewallRule(db.Model):
    __tablename__ = "firewall_rules"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    action = db.Column(db.String(10), nullable=False)

    protocol = db.Column(db.String(20))

    source_ip = db.Column(db.String(50))

    destination_ip = db.Column(db.String(50))

    source_port = db.Column(db.Integer)

    destination_port = db.Column(db.Integer)

    enabled = db.Column(db.Boolean, default=True)

    priority = db.Column(db.Integer, default=100)


class PacketLog(db.Model):
    __tablename__ = "packet_logs"

    id = db.Column(db.Integer, primary_key=True)

    timestamp = db.Column(db.DateTime)

    source_ip = db.Column(db.String(50))

    destination_ip = db.Column(db.String(50))

    protocol = db.Column(db.String(20))

    port = db.Column(db.Integer)

    length = db.Column(db.Integer)

    decision = db.Column(db.String(20))

    matched_rule = db.Column(db.String(100))


class AppSettings(db.Model):
    __tablename__ = "settings"

    id = db.Column(db.Integer, primary_key=True)

    default_policy = db.Column(
        db.String(10),
        default="ALLOW"
    )

    capture_interface = db.Column(
        db.String(100)
    )