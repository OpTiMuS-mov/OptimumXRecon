from core.dns_lookup import get_dns_info, display_dns_info
from core.port_scanner import scan_ports, display_ports
from core.whois_lookup import get_whois_info, display_whois_table
from core.ssl_checker import get_ssl_info, display_ssl_info
from core.header_analyzer import get_header_info, display_header_info
from core.tech_fingerprint import get_tech_info, display_tech_info
from core.subdomain_enum import get_subdomains, display_subdomains
from core.virustotal_lookup import get_virustotal_info, display_virustotal_info


def run_full_scan(target):
    """
    Run all reconnaissance modules and return collected results.

    Args:
        target (str): Target domain, IP, or URL.

    Returns:
        dict: Dictionary containing all scan results.
    """

    results = {"target": target}

    print("\n[*] Starting full scan...\n")

    print("[*] Running WHOIS lookup...")
    whois_data = get_whois_info(target)
    display_whois_table(whois_data)
    results["whois"] = whois_data

    print("[*] Running DNS lookup...")
    dns_data = get_dns_info(target)
    display_dns_info(dns_data)
    results["dns"] = dns_data

    print("[*] Running SSL/TLS check...")
    ssl_data = get_ssl_info(target)
    display_ssl_info(ssl_data)
    results["ssl"] = ssl_data

    print("[*] Running HTTP header analysis...")
    header_data = get_header_info(target)
    display_header_info(header_data)
    results["headers"] = header_data

    print("[*] Running technology fingerprinting...")
    tech_data = get_tech_info(target)
    display_tech_info(tech_data)
    results["technology"] = tech_data

    print("[*] Running port scan (1-1000)...")
    scan_data = scan_ports(target, "1-1000")
    display_ports(scan_data)
    results["ports"] = scan_data

    print("[*] Running subdomain enumeration...")
    subdomain_data = get_subdomains(target)
    display_subdomains(subdomain_data)
    results["subdomains"] = subdomain_data

    print("[*] Running VirusTotal lookup...")
    vt_data = get_virustotal_info(target)
    display_virustotal_info(vt_data)
    results["virustotal"] = vt_data

    print("\n[+] Full scan complete.\n")

    return results
