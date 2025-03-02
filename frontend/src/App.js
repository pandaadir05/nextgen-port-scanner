import React, { useState } from 'react';

function App() {
  const [ip, setIp] = useState("");
  const [startPort, setStartPort] = useState(1);
  const [endPort, setEndPort] = useState(1024);
  const [results, setResults] = useState(null);

  const handleScan = async () => {
    try {
      const response = await fetch("http://localhost:8000/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ip,
          start_port: startPort,
          end_port: endPort,
        }),
      });
      const data = await response.json();
      setResults(data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>NextGen Port Scanner</h1>
      <div>
        <input
          type="text"
          placeholder="Target IP"
          value={ip}
          onChange={(e) => setIp(e.target.value)}
        />
        <input
          type="number"
          placeholder="Start Port"
          value={startPort}
          onChange={(e) => setStartPort(Number(e.target.value))}
        />
        <input
          type="number"
          placeholder="End Port"
          value={endPort}
          onChange={(e) => setEndPort(Number(e.target.value))}
        />
        <button onClick={handleScan}>Start Scan</button>
      </div>
      {results && (
        <div>
          <h2>Results for {results.ip}</h2>
          <ul>
            {results.open_ports.map((p) => (
              <li key={p.port}>
                Port {p.port}: {p.banner} – {p.analysis.vulnerability}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
