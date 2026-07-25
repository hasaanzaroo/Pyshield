from flask import Flask, render_template, jsonify

from config import Config
from database.db import db
from database.models import PacketLog, FirewallRule
import database.models

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def dashboard():

    packets = PacketLog.query.order_by(PacketLog.id.desc()).limit(100).all()

    total_packets = PacketLog.query.count()

    allowed_packets = PacketLog.query.filter_by(decision="ALLOW").count()

    blocked_packets = PacketLog.query.filter_by(decision="BLOCK").count()

    tcp_packets = PacketLog.query.filter_by(protocol="TCP").count()

    return render_template(
        "dashboard.html",
        packets=packets,
        total_packets=total_packets,
        allowed_packets=allowed_packets,
        blocked_packets=blocked_packets,
        tcp_packets=tcp_packets
    )


@app.route("/api/packets")
def api_packets():

    packets = PacketLog.query.order_by(PacketLog.id.desc()).limit(100).all()

    data = []

    for packet in packets:
        data.append({
            "id": packet.id,
            "timestamp": str(packet.timestamp),
            "source_ip": packet.source_ip,
            "destination_ip": packet.destination_ip,
            "protocol": packet.protocol,
            "port": packet.port,
            "decision": packet.decision
        })

    return jsonify(data)


@app.route("/rules")
def rules():

    rules = FirewallRule.query.order_by(FirewallRule.priority).all()

    return render_template(
        "rules.html",
        rules=rules
    )


@app.route("/logs")
def logs():
    return render_template("logs.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)