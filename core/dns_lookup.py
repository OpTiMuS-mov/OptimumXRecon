import dns.resolver
from utils.console import console

def get_dns_records(target):
    record_types = ["A", "MX", "NS"]

    for record in record_types:
        console.print(f"\n[blue]{record} Records:[/blue]")

        try:
            answers = dns.resolver.resolve(target, record)

            for answer in answers:
                console.print(f"[green]{answer}[/green]")

        except Exception:
            console.print(f"[red]No {record} records found[/red]")