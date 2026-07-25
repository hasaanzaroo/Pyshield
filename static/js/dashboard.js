let protocolChart = null;

async function loadDashboard() {

    try {

        const response = await fetch("/api/dashboard");
        const data = await response.json();

        document.getElementById("totalPackets").textContent = data.total_packets;
        document.getElementById("allowedPackets").textContent = data.allowed_packets;
        document.getElementById("blockedPackets").textContent = data.blocked_packets;
        document.getElementById("activeRules").textContent = data.active_rules;

        const tbody = document.getElementById("packetTable");
        tbody.innerHTML = "";

        data.packets.forEach(packet => {

            tbody.innerHTML += `
                <tr>
                    <td>${packet.id}</td>
                    <td>${packet.time}</td>
                    <td>${packet.source}</td>
                    <td>${packet.destination}</td>
                    <td>
                        <span class="badge bg-info">
                            ${packet.protocol}
                        </span>
                    </td>
                    <td>${packet.port}</td>
                    <td>
                        <span class="badge ${packet.decision === "ALLOW" ? "bg-success" : "bg-danger"}">
                            ${packet.decision}
                        </span>
                    </td>
                </tr>
            `;

        });

    }

    catch (err) {

        console.error(err);

    }

}



async function loadProtocols() {

    try {

        const response = await fetch("/api/protocols");
        const data = await response.json();

        if (protocolChart) {

            protocolChart.destroy();

        }

        protocolChart = new Chart(

            document.getElementById("protocolChart"),

            {

                type: "doughnut",

                data: {

                    labels: data.labels,

                    datasets: [

                        {

                            data: data.values

                        }

                    ]

                },

                options: {

                    responsive: true,

                    plugins: {

                        legend: {

                            position: "bottom"

                        }

                    }

                }

            }

        );

    }

    catch (err) {

        console.error(err);

    }

}



async function loadTopIPs() {

    try {

        const response = await fetch("/api/top_ips");
        const ips = await response.json();

        const table = document.getElementById("topIpsTable");

        table.innerHTML = "";

        ips.forEach(ip => {

            table.innerHTML += `
                <tr>
                    <td>${ip.ip}</td>
                    <td>${ip.count}</td>
                </tr>
            `;

        });

    }

    catch (err) {

        console.error(err);

    }

}



async function loadAlerts() {

    try {

        const response = await fetch("/api/alerts");

        const alerts = await response.json();

        const list = document.getElementById("alertsList");

        list.innerHTML = "";

        if (alerts.length === 0) {

            list.innerHTML =
                `<li class="list-group-item">
                    No security alerts.
                </li>`;

            return;

        }

        alerts.forEach(alert => {

            list.innerHTML += `
                <li class="list-group-item list-group-item-danger">
                    <strong>${alert.time}</strong><br>
                    ${alert.message}
                </li>
            `;

        });

    }

    catch (err) {

        console.error(err);

    }

}



async function refreshDashboard() {

    await loadDashboard();

    await loadProtocols();

    await loadTopIPs();

    await loadAlerts();

}



refreshDashboard();

setInterval(refreshDashboard, 2000);