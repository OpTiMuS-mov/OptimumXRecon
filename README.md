# OptimumXRecon

A modular cybersecurity reconnaissance toolkit written in Python.

OptimumXRecon helps security enthusiasts, students, and researchers gather information about domains, websites, and network services through multiple reconnaissance modules integrated into a single command-line tool.

---

## Features

### Network Reconnaissance

* DNS Lookup
* Threaded Port Scanner
* SSL Certificate Analysis

### Web Security Analysis

* Security Header Analysis
* Technology Fingerprinting

### OSINT & Intelligence Gathering

* WHOIS Lookup
* Subdomain Enumeration
* VirusTotal Reputation Analysis

### User Experience

* Rich Console Interface
* Colored Output
* Structured Tables

---

## Screenshots

### WHOIS Lookup

![WHOIS Lookup](screenshots/whois.png)

### SSL Certificate Analysis

![SSL Certificate Analysis](screenshots/ssl.png)

### VirusTotal Analysis

![VirusTotal Analysis](screenshots/vt.png)

### Port Scanner

![Port Scanner](screenshots/port.png)

---

## Project Structure

```text
OptimumXRecon/
├── core/
│   ├── dns_lookup.py
│   ├── port_scanner.py
│   ├── ssl_checker.py
│   ├── whois_lookup.py
│   ├── header_analyzer.py
│   ├── tech_fingerprint.py
│   ├── subdomain_enum.py
│   └── virustotal_lookup.py
│
├── utils/
│   ├── console.py
│   ├── config.py
│   └── validators.py
│
├── reports/
├── tests/
├── db/
├── assets/
│   ├── whois.png
│   ├── ssl.png
│   ├── vt.png
│   └── ports.png
│
├── .env.example
├── requirements.txt
├── README.md
└── main.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/OpTiMuS-mov/OptimumXRecon.git
cd OptimumXRecon
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## VirusTotal Setup

Create a `.env` file in the project root:

```env
VT_API_KEY=YOUR_VIRUSTOTAL_API_KEY
```

You can obtain a free API key from VirusTotal.

---

## Usage Examples

### DNS Lookup

```bash
python main.py --target google.com --dns
```

### Port Scanning
![Port Scanner](screenshots/portscan.png)
```bash
python main.py --target scanme.nmap.org --ports 1-100
```

### WHOIS Lookup

![WHOIS Lookup](screenshots/whois.png)

```bash
python main.py --target google.com --whois
```

### SSL Certificate Analysis
![SSL Analysis](screnshots/ssl.png)
```bash
python main.py --target google.com --ssl
```

### Security Header Analysis

```bash
python main.py --target https://google.com --headers
```

### Technology Fingerprinting

```bash
python main.py --target https://google.com --tech
```

### Subdomain Enumeration

```bash
python main.py --target google.com --subdomains
```

### VirusTotal Analysis
![VirusTotal](screenshots/vt.png)
```bash
python main.py --target google.com --vt
```

---

## Technologies Used

* Python
* Socket Programming
* Requests
* Rich
* dnspython
* python-whois
* python-dotenv
* VirusTotal API

---

## Future Improvements

* Report Generation
* Banner Grabbing
* SQLite Scan History
* JSON Export
* HTML Reports
* Advanced Subdomain Enumeration
* Additional Threat Intelligence Integrations

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Always obtain proper authorization before scanning systems you do not own.

---

## Author

**Avinash Kotarya**

Cybersecurity Student | Python Developer | Security Enthusiast

GitHub: https://github.com/OpTiMuS-mov
