import argparse
from utils.validators import validate_target
from core.dns_lookup import get_dns_records
from core.port_scanner import scan_ports 
from core.whois_lookup import get_whois_info
from core.ssl_checker import get_ssl_info
from core.header_analyzer import get_header_info
from core.tech_fingerprint import get_tech_info
from core.subdomain_enum import get_subdomains
from core.virustotal_lookup import get_virustotal_info

def main():
    parser = argparse.ArgumentParser(
        prog="OptimumXRecon",
        description="Cybersecurity Reconnaissance Toolkit"
    )

    parser.add_argument("--target", help="Target domain, IP, or URL")
    parser.add_argument("--dns", action="store_true", help="Run DNS lookup")
    parser.add_argument("--ports", help="scan ports")
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
        get_dns_records(args.target)
    if args.ports:
        scan_ports(args.target,args.ports)
    if args.vt:
        get_virustotal_info(args.target)
    if args.ssl:
        get_ssl_info(args.target)
    if args.whois:
        get_whois_info(args.target)
    if args.headers:
        get_header_info(args.target)
    if args.tech:
        get_tech_info(args.target)
    if args.subdomains:
        get_subdomains(args.target)

if __name__ == "__main__":
    main()