import asyncio
from celery import Celery
import ai_analysis
import scanner

celery_app = Celery("tasks", broker="amqp://guest:guest@rabbitmq:5672//")

@celery_app.task
def distributed_scan(ip: str, start_port: int, end_port: int):
    results = asyncio.run(scanner.scan_ports(ip, start_port, end_port))
    open_ports = []
    for port, is_open, banner in results:
        if is_open:
            analysis = ai_analysis.analyze_banner(banner)
            open_ports.append({
                "port": port,
                "banner": banner,
                "analysis": analysis,
            })
    return {"ip": ip, "open_ports": open_ports}
