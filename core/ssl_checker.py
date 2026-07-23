import socket
import ssl
from rich.table import Table
from utils.console import console


def get_ssl_info(target):
    
    #Fetch SSL/TLS certificate information from the target.
    #Returns a normalized dictionary or None if an error occurs.
    

    context = ssl.create_default_context()

    try:
        with socket.create_connection((target, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=target) as secure_sock:

                cert = secure_sock.getpeercert()

                issuer = dict(x[0] for x in cert.get("issuer", []))
                subject = dict(x[0] for x in cert.get("subject", []))

                return {
                    "issuer_org": issuer.get("organizationName"),
                    "subject_cn": subject.get("commonName"),
                    "not_before": cert.get("notBefore"),
                    "not_after": cert.get("notAfter"),
                    "version": cert.get("version"),
                    "serial_number": cert.get("serialNumber"),
                }

    except Exception as e:
        console.print(f"[red]SSL Error:[/red] {e}")
        return None


def display_ssl_info(ssl_data):
    """
    Display SSL certificate information in a Rich table.
    """

    if ssl_data is None:
        return

    table = Table(title="SSL/TLS Certificate Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    rows = [
        ("Issuer Organization", ssl_data["issuer_org"]),
        ("Subject Common Name", ssl_data["subject_cn"]),
        ("Valid From", ssl_data["not_before"]),
        ("Valid Until", ssl_data["not_after"]),
        ("Version", ssl_data["version"]),
        ("Serial Number", ssl_data["serial_number"]),
    ]

    for field, value in rows:
        table.add_row(field, str(value))

    console.print(table)