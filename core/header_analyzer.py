import requests
from utils.console import console
from rich.table import Table


def get_header_info(target):
    if not target.startswith("http"):
       target = "https://" + target
    response = requests.get(target)

    headers = response.headers

    table = Table(title="Header Information")
    table.add_column("Header")
    table.add_column("Value")

    if "X-Frame-Options" in headers:
        table.add_row("X-Frame-Options", "[blue]Present[/blue]")
    else:
        table.add_row("X-Frame-Options", "[red]Absent[/red]")
    if "Content-Security-Policy" in headers:
        table.add_row("Content-Security-Policy", "[blue]Present[/blue]")
    else:
        table.add_row("Content-Security-Policy", "[red]Absent[/red]")
    if "Strict-Transport-Security" in headers:
        table.add_row("Strict-Transport-Security", "[blue]Present[/blue]")
    else:
        table.add_row("Strict-Transport-Security", "[red]Absent[/red]")
    if "X-Content-Type-Options" in headers:
        table.add_row("X-Content-Type-Options", "[blue]Present[/blue]")
    else:
        table.add_row("X-Content-Type-Options", "[red]Absent[/red]")
    console.print(table)