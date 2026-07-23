import dns.resolver
import dns.exception
from rich.table import Table
from utils.console import console


def get_subdomains(target):
    
    #Enumerate common subdomains using a built-in wordlist.
    #Returns a normalized dictionary or None if an error occurs.
    

    wordlist = [
        "www",
        "mail",
        "ftp",
        "admin",
        "test",
        "dev",
        "api",
        "blog",
        "shop",
        "staging",
    ]

    found_subdomains = []

    for word in wordlist:
        hostname = f"{word}.{target}"

        try:
            answers = dns.resolver.resolve(hostname, "A")

            ips = [answer.to_text() for answer in answers]

            found_subdomains.append({
                "hostname": hostname,
                "ip": ", ".join(ips)
            })

        except (
            dns.resolver.NXDOMAIN,
            dns.resolver.NoAnswer,
            dns.resolver.NoNameservers,
            dns.exception.Timeout,
        ):
            continue

        except Exception as e:
            console.print(f"[red]Error resolving {hostname}: {e}[/red]")

    return {
        "target": target,
        "subdomains": found_subdomains,
    }


def display_subdomains(data):
    
    #Display discovered subdomains in a Rich table.
    

    if data is None:
        return

    table = Table(title=f"Subdomain Enumeration - {data['target']}")

    table.add_column("Hostname", style="cyan")
    table.add_column("IP Address", style="green")

    if data["subdomains"]:
        for subdomain in data["subdomains"]:
            table.add_row(
                subdomain["hostname"],
                subdomain["ip"],
            )
    else:
        table.add_row("No subdomains found", "-")

    console.print(table)