import requests
import os
from dotenv import load_dotenv
from rich.table import Table
from utils.console import console

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")


def get_virustotal_info(domain):
    headers = {
        "x-apikey": API_KEY
    }

    url = f"https://www.virustotal.com/api/v3/domains/{domain}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        console.print("[red]Error fetching data from VirusTotal API[/red] ")
        return
    
    
    data = response.json()
    reputation = data["data"]["attributes"]["reputation"]
    stats = data["data"]["attributes"]["last_analysis_stats"]
    
    table = Table(title="VirusTotal Analysis Stats")

    table.add_column("Fields")
    table.add_column("Value", style="magenta")

    table.add_row("[cyan]reputation", str(reputation))
    table.add_row("[red]Malicious", str(stats["malicious"]))
    table.add_row("[yellow]Suspicious", str(stats["suspicious"]))
    table.add_row("[green]Harmless", str(stats["harmless"]))

    console.print(table)

