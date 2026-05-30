import dns.resolver
from utils.console import console

def get_subdomains(target):
    subdomains = ["admin", "mail", "ftp", "test", 
                  "dev", "www", "api", "blog", "shop", 
                  "staging"]
    for word in subdomains:
        subdomain = f"{word}.{target}"
        try:
                answers = dns.resolver.resolve(subdomain, 'A')
                console.print(f"[green]Found subdomain: {subdomain} -> {answers[0].to_text()}[/green]")
        except (dns.resolver.NXDOMAIN,
                dns.resolver.NoAnswer,
                dns.resolver.Timeout):
            console.print(f"[red]Subdomain not found: {subdomain}[/red]")