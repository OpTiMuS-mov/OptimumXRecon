import requests
from utils.console import console


def get_tech_info(target):
    if not target.startswith("http"):
        target = "http://" + target
    response = requests.get(target)
    headers = response.headers
    html = response.text

    if "cloudflare" in headers.get("Server", "").lower():
        console.print(f"[blue]Cloudflare is being used[/blue]")
    else:
        console.print(f"[red]Cloudflare is not being used[/red]")

    if "apache" in headers.get("Server", "").lower():
        console.print(f"[blue]Apache is being used[/blue]")
    else:
        console.print(f"[red]Apache is not being used[/red]")

    if "nginx" in headers.get("Server", "").lower():
        console.print(f"[blue]nginx is being used[/blue]")
    else:
        console.print(f"[red]nginx is not being used[/red]")

    if "litespeed" in headers.get("Server", "").lower():
        console.print(f"[blue]LiteSpeed is being used[/blue]")
    else:
        console.print(f"[red]LiteSpeed is not being used[/red]")

    if "wp-content" in html.lower():
        console.print(f"[blue]WordPress is being used[/blue]")
    else:
        console.print(f"[red]WordPress is not being used[/red]")
    if "php" in headers.get("X-Powered-By", "").lower():
        console.print(f"[blue]PHP detected[/blue]")
    else:
        console.print(f"[red]PHP is not being used[/red]")
    if "asp.net" in headers.get("X-Powered-By", "").lower():
        console.print(f"[blue]ASP.NET detected[/blue]")
    else:        
        console.print(f"[red]ASP.NET is not being used[/red]")    
    if "react" in html.lower() or "data-reactroot" in html.lower():
        console.print(f"[blue]React detected[/blue]")
    else:
        console.print(f"[red]React is not being used[/red]")
