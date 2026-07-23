import requests
from rich.table import Table
from utils.console import console


def get_tech_info(target):
    
    #Detect common web technologies from HTTP headers and page content.
    #Returns a normalized dictionary or None if an error occurs.
    

    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    try:
        response = requests.get(target, timeout=5)

        headers = response.headers
        html = response.text.lower()

        server = headers.get("Server", "").lower()
        powered_by = headers.get("X-Powered-By", "").lower()

        return {
            "Cloudflare": "cloudflare" in server,
            "Apache": "apache" in server,
            "Nginx": "nginx" in server,
            "LiteSpeed": "litespeed" in server,
            "WordPress": "wp-content" in html,
            "PHP": "php" in powered_by,
            "ASP.NET": "asp.net" in powered_by,
            "React": (
                "react" in html
                or "data-reactroot" in html
                or "__next" in html
            ),
        }

    except requests.RequestException as e:
        console.print(f"[red]Technology Detection Error:[/red] {e}")
        return None


def display_tech_info(tech_data):
    """
    Display detected technologies in a Rich table.
    """

    if tech_data is None:
        return

    table = Table(title="Technology Fingerprinting")

    table.add_column("Technology", style="cyan")
    table.add_column("Detected", justify="center")

    for tech, detected in tech_data.items():
        status = "[green]Yes[/green]" if detected else "[red]No[/red]"
        table.add_row(tech, status)

    console.print(table)