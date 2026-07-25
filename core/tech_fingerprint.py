import requests
from rich.table import Table
from utils.console import console


def get_tech_info(target):
    """
    Detect common web technologies from HTTP headers and page content.

    Returns:
        dict: Normalized technology information.
        None: If detection fails.
    """

    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    try:
        response = requests.get(target, timeout=5)
        response.raise_for_status()

        headers = response.headers
        html = response.text.lower()

        server = headers.get("Server", "")
        powered_by = headers.get("X-Powered-By", "")

        server_lower = server.lower()
        powered_by_lower = powered_by.lower()

        tech_data = {
            "target": target,
            "server": server,
            "powered_by": powered_by,
            "cloudflare": "cloudflare" in server_lower,
            "apache": "apache" in server_lower,
            "nginx": "nginx" in server_lower,
            "litespeed": "litespeed" in server_lower,
            "wordpress": "wp-content" in html,
            "php": "php" in powered_by_lower,
            "asp_net": "asp.net" in powered_by_lower,
            "react": (
                "react" in html
                or "data-reactroot" in html
                or "__next" in html
            ),
        }

        return tech_data

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
    table.add_column("Details", style="magenta")

    detections = [
        ("Cloudflare", tech_data["cloudflare"], "-"),
        ("Apache", tech_data["apache"], tech_data["server"] or "-"),
        ("Nginx", tech_data["nginx"], tech_data["server"] or "-"),
        ("LiteSpeed", tech_data["litespeed"], tech_data["server"] or "-"),
        ("WordPress", tech_data["wordpress"], "-"),
        ("PHP", tech_data["php"], tech_data["powered_by"] or "-"),
        ("ASP.NET", tech_data["asp_net"], tech_data["powered_by"] or "-"),
        ("React", tech_data["react"], "-"),
    ]

    for tech, detected, details in detections:
        status = "[green]Yes[/green]" if detected else "[red]No[/red]"
        table.add_row(tech, status, details)

    console.print(table)