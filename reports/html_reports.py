from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def generate_html_report(results, filename):
    """
    Generate an HTML report from scan results.

    Args:
        results (dict): Dictionary containing scan results.
        filename (str): Output HTML filename.
    """

    template_dir = Path(__file__).parent / "templates"

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )

    template = env.get_template("report.html")

    whois = results.get("whois")
    dns = results.get("dns")
    ssl = results.get("ssl")
    headers = results.get("headers")
    technology = results.get("technology")
    ports = results.get("ports")
    subdomains = results.get("subdomains")
    virustotal = results.get("virustotal")

    dns_count = 0
    if dns and "records" in dns:
        dns_count = sum(len(v) for v in dns["records"].values() if v)

    open_port_count = 0
    if ports and "open_ports" in ports:
        open_port_count = len(ports["open_ports"])

    tech_count = 0
    if technology:
        tech_count = sum(
            1 for k, v in technology.items()
            if isinstance(v, bool) and v
        )

    subdomain_count = 0
    if subdomains and "subdomains" in subdomains:
        subdomain_count = len(subdomains["subdomains"])

    vt_reputation = None
    vt_malicious = 0
    if virustotal:
        vt_reputation = virustotal.get("reputation")
        vt_malicious = virustotal.get("malicious", 0)

    html = template.render(
        target=results.get("target", "Unknown"),
        generated=datetime.now().strftime("%d %B %Y %H:%M:%S"),
        whois=whois,
        dns=dns,
        ssl=ssl,
        headers=headers,
        technology=technology,
        ports=ports,
        subdomains=subdomains,
        virustotal=virustotal,
        dns_count=dns_count,
        open_port_count=open_port_count,
        tech_count=tech_count,
        subdomain_count=subdomain_count,
        vt_reputation=vt_reputation,
        vt_malicious=vt_malicious,
    )

    output_dir = Path("output/reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / filename

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html)

    return output_file