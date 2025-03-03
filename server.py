# server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import scanner
import ai_analysis

app = FastAPI(title="NextGen Port Scanner API")

# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust as needed or use ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScanRequest(BaseModel):
    ip: str
    start_port: int = 1
    end_port: int = 1024

@app.post("/scan")
async def scan_endpoint(request: ScanRequest):
    results = await scanner.scan_ports(request.ip, request.start_port, request.end_port)
    open_ports = []
    for port, is_open, banner in results:
        if is_open:
            analysis = ai_analysis.analyze_banner(banner)
            open_ports.append({
                "port": port,
                "banner": banner,
                "analysis": analysis,
            })
    return {"ip": request.ip, "open_ports": open_ports}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
