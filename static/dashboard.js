async function loadPackets() {

    try {

        const response = await fetch("/api/packets");

        const packets = await response.json();

        console.clear();

        console.log("========== PYSHIELD LIVE PACKETS ==========");

        console.log("Packets Loaded:", packets.length);

        console.table(packets);

    } catch (error) {

        console.error("Failed to load packets:", error);

    }

}

// Load immediately
loadPackets();

// Refresh every 2 seconds
setInterval(loadPackets, 2000);