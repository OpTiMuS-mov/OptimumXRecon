import socket
from concurrent.futures import ThreadPoolExecutor
from utils.console import console


def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        console.print(f"[green]Port {port} is open[/green]")

    sock.close()


def scan_ports(target, ports):
    if "-" in ports:
        start, end = ports.split("-")
        start = int(start)
        end = int(end)
        ports = range(start, end + 1)
    else:
        ports = [int(ports)]

    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)