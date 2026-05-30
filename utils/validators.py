import re
import ipaddress
from urllib.parse import urlparse


def is_valid_domain(domain):
    pattern = r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(pattern, domain) is not None


def is_valid_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def is_valid_url(target):
    try:
        result = urlparse(target)
        return all([result.scheme, result.netloc])
    
    except:
        return False


def validate_target(target): 
    if not target:
        return False

    if is_valid_domain(target):
        return True

    if is_valid_ip(target):
        return True

    if is_valid_url(target):
        return True

    return False