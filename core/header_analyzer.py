import requests
from rich.table import Table
from utils.console import console


def get_header_info(target):
    
    #Fetch important HTTP security headers from the target.
    #Returns a normalized dictionary or None if an error occurs.
    

    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    try:
        response = requests.get(target, timeout=5)

        headers = response.headers

        return {
            "Server": headers.get("Server"),
            "Content-Type": headers.get("Content-Type"),
            "X-Powered-By": headers.get("X-Powered-By"),
            "X-Frame-Options": headers.get("X-Frame-Options"),
            "Content-Security-Policy": headers.get("Content-Security-Policy"),
            "Strict-Transport-Security": headers.get("Strict-Transport-Security"),
            "X-Content-Type-Options": headers.get("X-Content-Type-Options"),
        }

    except requests.RequestException as e:
        console.print(f"[red]Header Lookup Error:[/red] {e}")
        return None


def display_header_info(header_data):
    
    #Display HTTP security headers in a Rich table.
    

    if header_data is None:
        return

    table = Table(title="HTTP Security Headers")

    table.add_column("Header", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Value", style="green")

    security_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "Strict-Transport-Security",
        "X-Content-Type-Options",
    ]

    for header in security_headers:
        value = header_data.get(header)

        if value:
            status = "[green]Present[/green]"
        else:
            status = "[red]Absent[/red]"
            value = "-"

        table.add_row(header, status, str(value))

    console.print(table)