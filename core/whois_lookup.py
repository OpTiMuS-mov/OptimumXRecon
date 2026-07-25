import whois
from rich.table import Table
from utils.console import console


def normalize_date_whois(date):
    if date is None:
        return None
    elif isinstance(date, list):
        return date[0].strftime("%Y-%m-%d") if date else None
    return date.strftime("%Y-%m-%d")


def normalize_string_field_whois(field):
    if field is None:
        return None
    elif isinstance(field, list):
        return field[0] if field else None
    return field


def normalize_list_field_whois(field):
    if field is None:
        return []
    elif isinstance(field, list):
        return field
    return [field]


def get_whois_info(domain):
    try:
        w = whois.whois(domain)

        return {
            "domain": normalize_string_field_whois(w.domain_name),
            "registrar": normalize_string_field_whois(w.registrar),
            "creation_date": normalize_date_whois(w.creation_date),
            "expiration_date": normalize_date_whois(w.expiration_date),
            "updated_date": normalize_date_whois(w.updated_date),
            "name_servers": normalize_list_field_whois(w.name_servers),
            "status": normalize_list_field_whois(w.status),

            # Optional fields
            "registrant_email": getattr(w, "registrant_email", None),
            "registrant_name": getattr(w, "registrant_name", None),
            "registrant_organization": getattr(w, "registrant_organization", None),
            "registrant_country": getattr(w, "registrant_country", None),
            "registrant_state": getattr(w, "registrant_state", None),
            "registrant_city": getattr(w, "registrant_city", None),
        }

    except Exception as e:
        console.print(f"[red]Error fetching WHOIS info for {domain}: {e}[/red]")
        return None


def display_whois_table(whois_data):
    if whois_data is None:
        return

    table = Table(title="WHOIS Information")

    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Domain", str(whois_data["domain"]))
    table.add_row("Registrar", str(whois_data["registrar"]))
    table.add_row("Creation Date", str(whois_data["creation_date"]))
    table.add_row("Expiration Date", str(whois_data["expiration_date"]))
    table.add_row("Updated Date", str(whois_data["updated_date"]))

    table.add_row(
        "Name Servers",
        "\n".join(whois_data["name_servers"])
        if whois_data["name_servers"]
        else "None",
    )

    table.add_row(
        "Status",
        "\n".join(whois_data["status"])
        if whois_data["status"]
        else "None",
    )

    console.print(table)

    optional_fields = [
        ("Registrant Email", "registrant_email"),
        ("Registrant Name", "registrant_name"),
        ("Registrant Organization", "registrant_organization"),
        ("Registrant Country", "registrant_country"),
        ("Registrant State", "registrant_state"),
        ("Registrant City", "registrant_city"),
    ]

    for label, key in optional_fields:
        if whois_data[key]:
            console.print(f"[blue]{label}:[/blue] {whois_data[key]}")