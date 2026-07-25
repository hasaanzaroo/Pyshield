from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for,
    Response,
)

from config import Config
from database.db import db
from database.models import PacketLog, FirewallRule, AppSettings
from datetime import datetime
import random

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


# -----------------------------
# Dashboard
# -----------------------------

@app.route("/")
def dashboard():

    packets = PacketLog.query.order_by(PacketLog.id.desc()).limit(100).all()

    total_packets = PacketLog.query.count()
    allowed_packets = PacketLog.query.filter_by(decision="ALLOW").count()
    blocked_packets = PacketLog.query.filter_by(decision="BLOCK").count()
    active_rules = FirewallRule.query.filter_by(enabled=True).count()

    return render_template(
        "dashboard.html",
        packets=packets,
        total_packets=total_packets,
        allowed_packets=allowed_packets,
        blocked_packets=blocked_packets,
        active_rules=active_rules,
    )


# -----------------------------
# Dashboard APIs
# -----------------------------

@app.route("/api/packets")
def api_packets():

    packets = PacketLog.query.order_by(PacketLog.id.desc()).limit(100).all()

    return jsonify([
        {
            "id": p.id,
            "timestamp": str(p.timestamp),
            "source_ip": p.source_ip,
            "destination_ip": p.destination_ip,
            "protocol": p.protocol,
            "port": p.port,
            "decision": p.decision,
        }
        for p in packets
    ])


@app.route("/api/dashboard")
def api_dashboard():

    packets = PacketLog.query.order_by(PacketLog.id.desc()).limit(10).all()

    return jsonify({
        "total_packets": PacketLog.query.count(),
        "allowed_packets": PacketLog.query.filter_by(decision="ALLOW").count(),
        "blocked_packets": PacketLog.query.filter_by(decision="BLOCK").count(),
        "active_rules": FirewallRule.query.filter_by(enabled=True).count(),
        "packets": [
            {
                "timestamp": str(p.timestamp),
                "source_ip": p.source_ip,
                "destination_ip": p.destination_ip,
                "protocol": p.protocol,
                "port": p.port,
                "decision": p.decision,
            }
            for p in packets
        ],
    })


@app.route("/api/protocols")
def api_protocols():

    labels = []
    values = []

    protocols = db.session.query(
        PacketLog.protocol,
        db.func.count(PacketLog.id)
    ).group_by(PacketLog.protocol).all()

    for protocol, count in protocols:
        labels.append(protocol)
        values.append(count)

    return jsonify({
        "labels": labels,
        "values": values
    })


@app.route("/api/top_ips")
def api_top_ips():

    top = db.session.query(
        PacketLog.source_ip,
        db.func.count(PacketLog.id)
    ).group_by(PacketLog.source_ip).limit(10).all()

    return jsonify([
        {
            "ip": ip,
            "count": count
        }
        for ip, count in top
    ])


@app.route("/api/alerts")
def api_alerts():

    alerts = (
        PacketLog.query
        .filter_by(decision="BLOCK")
        .order_by(PacketLog.id.desc())
        .limit(10)
        .all()
    )

    return jsonify([
        {
            "time": str(a.timestamp),
            "source": a.source_ip,
            "protocol": a.protocol,
            "port": a.port,
        }
        for a in alerts
    ])


# -----------------------------
# Rules
# -----------------------------

@app.route("/rules")
def rules():

    rules = FirewallRule.query.order_by(FirewallRule.priority).all()

    return render_template(
        "rules.html",
        rules=rules
    )


@app.route("/rules/add", methods=["GET", "POST"])
def add_rule():

    if request.method == "POST":

        rule = FirewallRule(
            name=request.form["name"],
            action=request.form["action"],
            protocol=request.form["protocol"],
            destination_port=request.form["destination_port"] or None,
            priority=request.form["priority"],
            enabled=True,
        )

        db.session.add(rule)
        db.session.commit()

        return redirect(url_for("rules"))

    return render_template("add_rule.html")


@app.route("/rules/edit/<int:rule_id>", methods=["GET", "POST"])
def edit_rule(rule_id):

    rule = FirewallRule.query.get_or_404(rule_id)

    if request.method == "POST":

        rule.name = request.form["name"]
        rule.action = request.form["action"]
        rule.protocol = request.form["protocol"]
        rule.destination_port = request.form["destination_port"]
        rule.priority = request.form["priority"]

        db.session.commit()

        return redirect(url_for("rules"))

    return render_template(
        "edit_rule.html",
        rule=rule
    )


@app.route("/rules/delete/<int:rule_id>")
def delete_rule(rule_id):

    rule = FirewallRule.query.get_or_404(rule_id)

    db.session.delete(rule)
    db.session.commit()

    return redirect(url_for("rules"))


@app.route("/rules/toggle/<int:rule_id>")
def toggle_rule(rule_id):

    rule = FirewallRule.query.get_or_404(rule_id)

    rule.enabled = not rule.enabled

    db.session.commit()

    return redirect(url_for("rules"))


# -----------------------------
# Logs
# -----------------------------

@app.route("/logs")
def logs():

    packets = (
        PacketLog.query
        .order_by(PacketLog.id.desc())
        .all()
    )

    return render_template(
        "logs.html",
        packets=packets
    )


@app.route("/logs/export")
def export_logs():

    packets = (
        PacketLog.query
        .order_by(PacketLog.id.desc())
        .all()
    )

    csv = "ID,Timestamp,Source IP,Destination IP,Protocol,Port,Length,Decision,Matched Rule\n"

    for p in packets:

        csv += (
            f"{p.id},"
            f"{p.timestamp},"
            f"{p.source_ip},"
            f"{p.destination_ip},"
            f"{p.protocol},"
            f"{p.port},"
            f"{p.length},"
            f"{p.decision},"
            f"{p.matched_rule}\n"
        )

    return Response(
        csv,
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=pyshield_logs.csv"
        }
    )


# -----------------------------
# Settings
# -----------------------------

@app.route("/settings", methods=["GET", "POST"])
def settings():

    settings = AppSettings.query.first()

    if settings is None:

        settings = AppSettings(
            default_policy="ALLOW",
            capture_interface="eth0"
        )

        db.session.add(settings)
        db.session.commit()

    if request.method == "POST":

        settings.default_policy = request.form["default_policy"]
        settings.capture_interface = request.form["capture_interface"]

        db.session.commit()

        return redirect(url_for("settings"))

    total_rules = FirewallRule.query.count()
    enabled_rules = FirewallRule.query.filter_by(enabled=True).count()
    total_logs = PacketLog.query.count()

    return render_template(
        "settings.html",
        settings=settings,
        total_rules=total_rules,
        enabled_rules=enabled_rules,
        total_logs=total_logs,
    )


@app.route("/demo/load")
def load_demo():

    FirewallRule.query.delete()
    PacketLog.query.delete()

    db.session.commit()

    rules = [

        FirewallRule(
            name="Allow HTTP",
            action="ALLOW",
            protocol="TCP",
            destination_port=80,
            priority=1,
            enabled=True
        ),

        FirewallRule(
            name="Allow HTTPS",
            action="ALLOW",
            protocol="TCP",
            destination_port=443,
            priority=2,
            enabled=True
        ),

        FirewallRule(
            name="Block Telnet",
            action="BLOCK",
            protocol="TCP",
            destination_port=23,
            priority=3,
            enabled=True
        ),

        FirewallRule(
            name="Block FTP",
            action="BLOCK",
            protocol="TCP",
            destination_port=21,
            priority=4,
            enabled=True
        )

    ]

    db.session.add_all(rules)

    protocols = ["TCP", "UDP", "ICMP"]

    for i in range(100):

        protocol = random.choice(protocols)

        decision = random.choice(["ALLOW", "BLOCK"])

        packet = PacketLog(

            timestamp=datetime.now(),

            source_ip=f"192.168.1.{random.randint(2,254)}",

            destination_ip=f"10.0.0.{random.randint(2,254)}",

            protocol=protocol,

            port=random.choice([22,53,80,443,8080]),

            length=random.randint(64,1500),

            decision=decision,

            matched_rule=random.choice([
                "Allow HTTP",
                "Allow HTTPS",
                "Block FTP",
                "Block Telnet"
            ])

        )

        db.session.add(packet)

    db.session.commit()

    return redirect(url_for("dashboard"))

# -----------------------------
# Database
# -----------------------------

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)