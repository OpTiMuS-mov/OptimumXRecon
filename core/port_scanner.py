import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.table import Table
from utils.console import console


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            return port
        return None
    finally:
        sock.close()


def scan_ports(target, ports):
    try:
        if "-" in ports:
            parts = ports.split("-")
            if len(parts) != 2:
                console.print("[red]Invalid port format.[/red] Use PORT or START-END.")
                return {
                    "target": target,
                    "scan_type": "TCP Connect",
                    "ports_scanned": 0,
                    "open_ports": []
                }
            start, end = int(parts[0]), int(parts[1])
            if start < 1 or end > 65535 or start > end:
                console.print("[red]Invalid port range.[/red] Use 1-65535.")
                return {
                    "target": target,
                    "scan_type": "TCP Connect",
                    "ports_scanned": 0,
                    "open_ports": []
                }
            ports = range(start, end + 1)
        else:
            port = int(ports)
            if port < 1 or port > 65535:
                console.print("[red]Invalid port.[/red] Use 1-65535.")
                return {
                    "target": target,
                    "scan_type": "TCP Connect",
                    "ports_scanned": 0,
                    "open_ports": []
                }
            ports = [port]
    except ValueError:
        console.print("[red]Invalid port input.[/red] Use PORT or START-END (e.g. 80 or 1-1000).")
        return {
            "target": target,
            "scan_type": "TCP Connect",
            "ports_scanned": 0,
            "open_ports": []
        }

    open_ports = []

    with ThreadPoolExecutor(max_workers=min(100, len(ports))) as executor:
        futures = [executor.submit(scan_port, target, port) for port in ports]

        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                open_ports.append(result)

    open_ports.sort()

    return {
        "target": target,
        "scan_type": "TCP Connect",
        "ports_scanned": len(ports),
        "open_ports": open_ports
    }


def display_ports(scan_data):
    table = Table(title=f"Open Ports - {scan_data['target']}")

    table.add_column("Port", justify="center")
    table.add_column("State", justify="center")

    if scan_data["open_ports"]:
        for port in scan_data["open_ports"]:
            table.add_row(str(port), "OPEN")
    else:
        table.add_row("No open ports found", "-")

    console.print(table)