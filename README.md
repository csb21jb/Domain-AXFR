```
MMMMMMMb                                      68b                       dM       MM        M   MMMMMMM  MMMMMMMb
MM     Mb                                     Y89                       MMb       MM      d    MM       MM     Mb  
MM     MM                                                              d YM        MM    d     MM       MM     MM  
MM     MM  6MMMMMb   MM 6MMb  6MMb   6MMMMb    MM  MM 6MMb             P  Mb        MM  d      MM       MM     MM  
MM     MM 6M     Mb  MM69  MM69  Mb 8M    Mb   MM  MMM9  Mb           d   YM         MMd       MMMMMM   MM     M9  
MM     MM MM     MM  MM    MM    MM      oMM   MM  MM    MM           P    Mb        dMM       MM       MMMMMMM9   
MM     MM MM     MM  MM    MM    MM  6MM9 MM   MM  MM    MM          d     YM       d  MM      MM       MM  \M\    
MM     MM MM     MM  MM    MM    MM MM    MM   MM  MM    MM          MMMMMMMMb     d    MM     MM       MM   \M\   
MM     M9 YM     M9  MM    MM    MM MM    MM   MM  MM    MM         d       YM    d      MM    MM       MM    \M\  
MMMMMMM9   YMMMMM9   MM    MM    MM  YMMM9'Yb  MM  MM    MM        dM       dMM  M        MM   MM       MM     \M\
```
# Domain-AXFR

A robust tool for automated DNS zone transfer and subdomain enumeration!

## Summary
Domain AXFR is a powerful Python-based tool that automates the process of DNS zone transfer and subdomain enumeration using the 'dig' command. Ideal for network administrators and cybersecurity professionals, it simplifies the task of discovering subdomains and associated IP addresses for a given domain. The tool recursively queries subdomains, extracting vital DNS information and streamlining the reconnaissance phase of security assessments.

## Features
- Automated DNS Zone Transfer: Utilizes the 'dig' command for DNS zone transfers.
- Recursive Subdomain Enumeration: Discovers and lists all subdomains of a target domain.
- IP Address Extraction: Captures IP addresses associated with each subdomain.
- Efficient Data Aggregation: Consolidates DNS data into easily readable text files.
- Dig command (commonly available on Unix-based systems)


### Installation
Ensure you have Python 3 and the dig tool installed on your system:
```
sudo apt update
sudo apt install python3 -y
```
## Usage
Run the script from the command line, specifying the target domain and IP address:
```
python3 DomainAXFR.py <domain> <IP>
```

## Output
- all_domain_info.txt: Comprehensive list of subdomains and their respective DNS records.
- domain_names.txt: Simplified list of unique subdomain names.

## Upcoming Features
- Integration with additional external DNS enumeration tools.
- Enhanced performance optimizations for large-scale domain enumeration.
- User interface improvements for a more interactive experience.
- Advanced error handling and logging capabilities.
