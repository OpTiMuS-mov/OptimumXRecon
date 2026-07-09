import whois
from rich.table import Table
from utils.console import console


def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        table = Table(title="WHOIS information")

        table.add_column("Fields")
        table.add_column("value")
        

        table.add_row("Registrar", str(w.registrar))
        table.add_row("Creation Date", str(w.creation_date))
        table.add_row("Expiration Date", str(w.expiration_date))
        table.add_row("Name Servers", str(w.name_servers))
        table.add_row("Status", str(w.status))
        table.add_row("Domain Name", str(w.domain_name))
        
        if w.registrant_email:
           console.print(f"[blue]Registrant Email: {w.registrant_email}[/blue]")
        
        if w.registrant_name:
           console.print(f"[blue]Registrant Name: {w.registrant_name}[/blue]")
        
        if w.registrant_organization:
           console.print(f"[blue]Registrant Organization: {w.registrant_organization}[/blue]")
        
        if w.registrant_country:
           console.print(f"[blue]Registrant Country: {w.registrant_country}[/blue]")
        
        if w.registrant_state:
           console.print(f"[blue]Registrant State: {w.registrant_state}[/blue]")
        
        if w.registrant_city:
           console.print(f"[blue]Registrant City: {w.registrant_city}[/blue]")
        
        console.print(table)

        return w
    except Exception as e:
        console.print(f"[red]Error fetching WHOIS info for {domain}: {e}[/red]")
        return None