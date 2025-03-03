// frontend/src/App.js
import React, { useState } from 'react';
import './App.css'; // Apply the modern styling

function App() {
  const [ip, setIp] = useState("127.0.0.1");
  const [startPort, setStartPort] = useState(1);
  const [endPort, setEndPort] = useState(1024);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleScan = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ip, start_port: startPort, end_port: endPort })
      });
      const data = await response.json();
      console.log("Received data:", data);
      setResults(data);
    } catch (error) {
      console.error("Error:", error);
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <h1 className="title">NextGen Port Scanner Dashboard</h1>
      <div className="input-container">
        <input 
          type="text" 
          value={ip} 
          onChange={e => setIp(e.target.value)} 
          placeholder="Enter IP address"
          className="input-field"
        />
        <input 
          type="number" 
          value={startPort} 
          onChange={e => setStartPort(Number(e.target.value))} 
          placeholder="Start Port"
          className="input-field small"
        />
        <input 
          type="number" 
          value={endPort} 
          onChange={e => setEndPort(Number(e.target.value))} 
          placeholder="End Port"
          className="input-field small"
        />
        <button onClick={handleScan} className="scan-button">
          {loading ? "Scanning..." : "Scan"}
        </button>
      </div>
      <div className="results-container">
        {results ? (
          <div>
            <h2 className="results-title">Scan Results for {results.ip}</h2>
            {results.open_ports.length > 0 ? (
              <ul className="results-list">
                {results.open_ports.map((portInfo) => (
                  <li key={portInfo.port} className="result-item">
                    <strong>Port {portInfo.port}:</strong> {portInfo.banner} | 
                    Analysis: {portInfo.analysis.vulnerability}
                  </li>
                ))}
              </ul>
            ) : (
              <p className="no-results">No open ports found.</p>
            )}
          </div>
        ) : (
          <p className="no-results">Please run a scan.</p>
        )}
      </div>
    </div>
  );
}

export default App;
