# 🛡️ PyShield

**PyShield** is an educational firewall management and network monitoring dashboard built with **Flask**, **SQLAlchemy**, **Bootstrap**, and **SQLite**. It provides an intuitive web interface for managing firewall rules, viewing packet logs, monitoring network statistics, and demonstrating core firewall concepts.

> **Project Status:** Active Development 🚧

---

# 📖 Overview

PyShield was developed as an educational cybersecurity project to demonstrate how a firewall management system can be designed using modern web technologies.

The project focuses on:

* Firewall rule management
* Packet logging
* Dashboard visualization
* Network monitoring concepts
* REST API development
* Database management

PyShield is intended for learning and demonstration purposes and is **not** a replacement for operating system firewalls such as Windows Defender Firewall, iptables, or nftables.

---

# ✨ Features

## 📊 Dashboard

* Live dashboard statistics
* Total packets
* Allowed packets
* Blocked packets
* Active firewall rules
* Recent network activity

---

## 🛡 Firewall Rule Management

* Create firewall rules
* Edit rules
* Delete rules
* Enable or disable rules
* Rule priority management

---

## 📜 Packet Logging

Packet logs include:

* Timestamp
* Source IP
* Destination IP
* Protocol
* Destination Port
* Packet Length
* Decision (ALLOW/BLOCK)
* Matched Rule

---

## 🔍 Log Management

* Search logs
* View packet history
* Export logs as CSV

---

## ⚙ Settings

* Default firewall policy
* Capture interface configuration
* Firewall statistics
* Rule statistics
* Log statistics

---

## 🌐 REST API

PyShield exposes REST endpoints for dashboard integration.

| Endpoint         | Description            |
| ---------------- | ---------------------- |
| `/api/dashboard` | Dashboard statistics   |
| `/api/packets`   | Latest packets         |
| `/api/protocols` | Protocol statistics    |
| `/api/top_ips`   | Top source IPs         |
| `/api/alerts`    | Recent blocked packets |

---

## 🧪 Demo Data

Generate realistic sample firewall rules and packet logs for testing, demonstrations, and development.

---

# ⚠ Current Limitations

PyShield currently focuses on **firewall management and visualization**.

At the present stage, it **does not**:

* Perform real-time network scanning
* Discover devices on the local network
* Continuously monitor all network traffic
* Block or allow packets at the operating system level
* Perform intrusion detection
* Replace a production firewall

Packet information displayed in the application is intended for educational demonstrations and application-level logging.

---

# 🚀 Planned Features

Future versions of PyShield are planned to include:

* ✅ Real-time network scanning
* ✅ Automatic device discovery
* ✅ Live packet capture
* ✅ Traffic analysis
* ✅ Network topology visualization
* ✅ Intrusion detection alerts
* ✅ Port scanning (authorized environments only)
* ✅ Bandwidth monitoring
* ✅ Protocol usage graphs
* ✅ Packet filtering and rule enforcement
* ✅ Multi-user authentication
* ✅ Dark mode
* ✅ Dashboard customization

---

# 🏗 Project Structure

```text
PyShield/
│
├── app.py
├── config.py
├── requirements.txt
│
├── database/
│   ├── db.py
│   └── models.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── rules.html
│   ├── add_rule.html
│   ├── edit_rule.html
│   ├── logs.html
│   └── settings.html
│
├── static/
│   ├── css/
│   └── js/
│
└── README.md
```

---

# 🛠 Built With

* Python
* Flask
* SQLAlchemy
* SQLite
* Bootstrap 5
* HTML5
* CSS3
* JavaScript

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/PyShield.git
cd PyShield
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 📸 Screenshots

Include screenshots of:

* Dashboard
* Firewall Rules
* Packet Logs
* Settings
* Demo Data

---

# 🎯 Educational Objectives

This project demonstrates concepts including:

* Firewall rule management
* Network traffic visualization
* Packet logging
* Flask web development
* SQLAlchemy ORM
* REST API development
* Bootstrap UI design
* Database-driven applications

---

# 🤝 Contributing

Contributions, bug reports, feature requests, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Mohammad Kashif**

B.Tech Computer Science Engineering

Cybersecurity Enthusiast • Python Developer • Network Security Learner

---

## ⭐ Support

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub.
