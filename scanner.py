# scanner.py
import asyncio

async def scan_port(ip: str, port: int, timeout: float = 2) -> tuple:
    """
    Attempts to connect to the given ip:port.
    Returns a tuple (port, is_open, banner).
    """
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port), timeout
        )
        # Give the service a moment to send a banner
        await asyncio.sleep(0.1)
        try:
            data = await asyncio.wait_for(reader.read(1024), timeout=timeout)
        except asyncio.TimeoutError:
            data = b""
        banner = data.decode(errors='ignore').strip() if data else "No banner"
        writer.close()
        await writer.wait_closed()
        return (port, True, banner)
    except Exception as e:
        print(f"Port {port} is not open: {e}")
        return (port, False, "")

async def scan_ports(ip: str, start_port: int, end_port: int, max_concurrency: int = 100) -> list:
    """
    Scans ports in the range [start_port, end_port] concurrently.
    Returns a list of tuples (port, is_open, banner).
    """
    sem = asyncio.Semaphore(max_concurrency)
    async def sem_scan(port: int):
        async with sem:
            return await scan_port(ip, port)
    tasks = [sem_scan(port) for port in range(start_port, end_port + 1)]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Async Port Scanner")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("--start", type=int, default=1, help="Starting port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="Ending port (default: 1024)")
    args = parser.parse_args()

    results = asyncio.run(scan_ports(args.ip, args.start, args.end))
    for port, is_open, banner in results:
        if is_open:
            print(f"Port {port} is OPEN | Banner: {banner}")
    if all(not is_open for _, is_open, _ in results):
        print("No open ports found.")
