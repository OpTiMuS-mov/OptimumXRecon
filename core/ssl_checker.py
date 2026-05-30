import socket
import ssl
from utils.console import console
from rich.table import Table

def get_ssl_info(target):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.create_default_context()
    secure_sock = context.wrap_socket(sock, server_hostname=target)
    secure_sock.connect((target, 443))

    cert = secure_sock.getpeercert()
    issuer = dict(x[0] for x in cert["issuer"])
    subject = dict(x[0] for x in cert["subject"])

    table = Table(title="SSL/TLS Certificate Information")
    table.add_column("Fields")
    table.add_column("Value")

    table.add_row("Issuer Org", str(issuer.get('organizationName')))
    table.add_row("Subject Common Name", str(subject.get('commonName')))
    table.add_row("Not Before", str(cert['notBefore']))
    table.add_row("Not After", str(cert['notAfter']))
    table.add_row("Version", str(cert['version']))
    table.add_row("Serial Number", str(cert['serialNumber']))
    
    console.print(table)
    secure_sock.close()

