import argparse
from utils.validators import validate_target
from core.dns_lookup import get_dns_info , display_dns_info
from core.port_scanner import scan_ports , display_ports
from core.whois_lookup import get_whois_info, display_whois_table
from core.ssl_checker import get_ssl_info , display_ssl_info
from core.header_analyzer import get_header_info , display_header_info
from core.tech_fingerprint import get_tech_info , display_tech_info
from core.subdomain_enum import get_subdomains , display_subdomains
from core.virustotal_lookup import get_virustotal_info , display_virustotal_info

def main():
    parser = argparse.ArgumentParser(
        prog="OptimumXRecon",
        description="Cybersecurity Reconnaissance Toolkit"
    )

    parser.add_argument("--target", help="Target domain, IP, or URL")
    parser.add_argument("--dns", action="store_true", help="Run DNS lookup")
    parser.add_argument("--ports", help="Scan ports")
    parser.add_argument("--whois", action="store_true", help="Run WHOIS lookup")
    parser.add_argument("--ssl", action="store_true", help="Run SSL/TLS check")
    parser.add_argument("--headers", action="store_true", help="Run HTTP header analysis")
    parser.add_argument("--tech", action="store_true", help="Run technology fingerprinting")
    parser.add_argument("--subdomains", action="store_true", help="Run subdomain enumeration")
    parser.add_argument("--vt", action="store_true", help="Run VirusTotal lookup")

    args = parser.parse_args()
    if not validate_target(args.target):
        print("Invalid Target Provided")
        return

    print("Target:", args.target)

    if args.dns:
        dns_data = get_dns_info(args.target)
        display_dns_info(dns_data)
    if args.ports:
        scan_data = scan_ports(args.target,args.ports)
        display_ports(scan_data)
    if args.vt:
        vt_data = get_virustotal_info(args.target)
        display_virustotal_info(vt_data)
    if args.ssl:
        ssl_data = get_ssl_info(args.target)
        display_ssl_info(ssl_data)
    if args.whois:
        whois_data = get_whois_info(args.target)
        display_whois_table(whois_data)
    if args.headers:
        header_data = get_header_info(args.target)
        display_header_info(header_data)
    if args.tech:
        tech_data = get_tech_info(args.target)
        display_tech_info(tech_data)
    if args.subdomains:
        subdomain_data = get_subdomains(args.target)
        display_subdomains(subdomain_data)

if __name__ == "__main__":
    main()