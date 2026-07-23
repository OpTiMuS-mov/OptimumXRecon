import os
import requests
from dotenv import load_dotenv
from rich.table import Table
from utils.console import console

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")


def get_virustotal_info(domain):
    """
    Fetch VirusTotal analysis for a domain.
    Returns a normalized dictionary or None if an error occurs.
    """

    if not API_KEY:
        console.print("[red]VirusTotal API key not found.[/red]")
        return None

    url = f"https://www.virustotal.com/api/v3/domains/{domain}"

    headers = {
        "x-apikey": API_KEY
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        attributes = response.json()["data"]["attributes"]

        stats = attributes.get("last_analysis_stats", {})

        return {
            "domain": domain,
            "reputation": attributes.get("reputation"),
            "harmless": stats.get("harmless", 0),
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "undetected": stats.get("undetected", 0),
            "timeout": stats.get("timeout", 0),
        }

    except requests.RequestException as e:
        console.print(f"[red]VirusTotal Error:[/red] {e}")
        return None


def display_virustotal_info(vt_data):
    """
    Display VirusTotal analysis in a Rich table.
    """

    if vt_data is None:
        return

    table = Table(title=f"VirusTotal Analysis - {vt_data['domain']}")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="magenta")

    rows = [
        ("Reputation", vt_data["reputation"]),
        ("Harmless", vt_data["harmless"]),
        ("Malicious", vt_data["malicious"]),
        ("Suspicious", vt_data["suspicious"]),
        ("Undetected", vt_data["undetected"]),
        ("Timeout", vt_data["timeout"]),
    ]

    for field, value in rows:
        table.add_row(field, str(value))

    console.print(table)