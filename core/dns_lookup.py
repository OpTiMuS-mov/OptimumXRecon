import dns.resolver
import dns.exception
from rich.table import Table
from utils.console import console


def get_dns_info(target):
    """
    Fetch common DNS records for a domain.
    Returns a normalized dictionary or None if an error occurs.
    """

    record_types = ["A", "AAAA", "MX", "NS", "TXT", "CNAME"]

    dns_data = {record: [] for record in record_types}

    for record in record_types:
        try:
            answers = dns.resolver.resolve(target, record)

            dns_data[record] = [
                answer.to_text() for answer in answers
            ]

        except (
            dns.resolver.NoAnswer,
            dns.resolver.NXDOMAIN,
            dns.resolver.NoNameservers,
            dns.exception.Timeout,
        ):
            continue

        except Exception as e:
            console.print(f"[red]DNS Error ({record}):[/red] {e}")

    return {
        "target": target,
        "records": dns_data,
    }


def display_dns_info(dns_data):
    """
    Display DNS records in a Rich table.
    """

    if dns_data is None:
        return

    table = Table(title=f"DNS Records - {dns_data['target']}")

    table.add_column("Record Type", style="cyan")
    table.add_column("Value", style="green")

    has_records = False

    for record_type, values in dns_data["records"].items():

        if values:
            has_records = True

            for value in values:
                table.add_row(record_type, value)

    if not has_records:
        table.add_row("No Records", "-")

    console.print(table)