```
 ####      ####    ##   ##    ##      ####    ##  ##              ##     ##  ##   ######   #####   
 ## ##    ##  ##   ### ###   ####      ##     ### ##             ####    ##  ##   ##       ##  ##  
 ##  ##   ##  ##   #######  ##  ##     ##     ######            ##  ##     ###    ##       ##  ##  
 ##  ##   ##  ##   ## # ##  ######     ##     ######            ######     ##     ####     #####   
 ##  ##   ##  ##   ##   ##  ##  ##     ##     ## ###            ##  ##    ####    ##       ####    
 ## ##    ##  ##   ##   ##  ##  ##     ##     ##  ##            ##  ##   ##  ##   ##       ## ##   
 ####      ####    ##   ##  ##  ##    ####    ##  ##            ##  ##   ##  ##   ##       ##  ##
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
![image](https://github.com/csb21jb/Domain-AXFR/assets/94072917/2ea69b13-7093-4119-a19b-ed646c81bae6)

## Output
- all_domain_info.txt: Comprehensive list of subdomains and their respective DNS records.
- domain_names.txt: Simplified list of unique subdomain names.
![image](https://github.com/csb21jb/Domain-AXFR/assets/94072917/c98cd558-e5f5-4f09-82c9-de3046da8ff2)

### Creates 3 x files to conduct additional greps
![image](https://github.com/csb21jb/Domain-AXFR/assets/94072917/10678312-c6c7-453b-93a9-23078e27d776)

## Upcoming Features
- Integration with additional external DNS enumeration tools.
- Enhanced performance optimizations for large-scale domain enumeration.
- User interface improvements for a more interactive experience.
- Advanced error handling and logging capabilities.
