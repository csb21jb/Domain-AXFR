import subprocess
import argparse
import os
import re
import sys
import time
import glob

def print_banner():
    print(r"""    
                                                                
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
     """)
    print("Written by CB")
    print("A domain transfer utility")
    print("Version 1.0")                                                                                                        

print_banner()
#print the banner
print("\nStarting the script...\n")
time.sleep(3)


# Run dig command and save output to file
def run_dig_command(domain, ip):
    
    try:
        print(f"Running dig for {domain} @ {ip}")
        result = subprocess.check_output(["dig", "axfr", domain, "@" + ip, "+all"], encoding='UTF-8')
        print(result)
        with open(f"{domain}_temp.txt", "a") as file:  # Write to a temporary file
            file.write(result)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error running dig for {domain}: {e}")
        return None

def extract_subdomains(dig_output):
    # Regular expression to match subdomains in dig output
    pattern = r"(\w+\.\w+\.\w+)\."
    subdomains = re.findall(pattern, dig_output)
    return subdomains

def main(domain, ip):
    subdomains = [domain]  # Start with the initial domain
    all_subdomains = set()
    new_subdomains = []

    for subdomain in subdomains:
        print(f"Querying subdomain: {subdomain}")
        output = run_dig_command(subdomain, ip)
        if output:
            new_subdomains.extend(extract_subdomains(output))
            all_subdomains.update(new_subdomains)

    subdomains.extend(new_subdomains)

    # Run final dig axfr command on all subdomains
    for subdomain in all_subdomains:
        print(f"Running final dig axfr for subdomain: {subdomain}")
        final_output = run_dig_command(subdomain, ip)
        if final_output:
            new_subdomains = extract_subdomains(final_output)

    # Extract subdomains and IPs from temporary file
    with open(f"{domain}_temp.txt", "r") as temp_file:
        lines = temp_file.readlines()

    # Write subdomains and IPs to final files
    with open(f"{domain}_subdomains_IP.txt", "w") as ip_file, open(f"{domain}_subdomainsonly.txt", "w") as subdomain_file:
        for line in lines:
            match = re.search(r"(\w+\.\w+\.\w+)\.\s+\d+\s+IN\s+A\s+(\d+\.\d+\.\d+\.\d+)", line)
            if match:
                subdomain, ip = match.groups()
                ip_file.write(f"{subdomain} @ {ip}\n")
                subdomain_file.write(f"{subdomain}\n")

 
        # Remove duplicates from subdomainsonly.txt
        with open(f"{domain}_subdomainsonly.txt", "r") as file:
            subdomains = set(file.readlines())
        with open(f"{domain}_subdomainsonly.txt", "w") as file:
            for subdomain in subdomains:
                file.write(subdomain)

        # Read the subdomainsonly.txt file and run dig command on each subdomain
        with open(f"{domain}_subdomainsonly.txt", "r") as file:
            subdomains = [line.strip() for line in file]
        for subdomain in subdomains:
            print(f"Running dig for subdomain: {subdomain}")
            output = run_dig_command(subdomain, ip)
            if output:
                new_subdomains = extract_subdomains(output)
                # Append new subdomains to the subdomainsonly.txt file
                with open(f"{domain}_subdomainsonly.txt", "a") as file:
                    for new_subdomain in new_subdomains:
                        file.write(f"{new_subdomain}\n")

        # Find all temporary files
        temp_files = glob.glob('*_temp.txt')

        # Create a new file to hold all the contents
        with open('all_domain_info.txt', 'w') as outfile:
            for fname in temp_files:
                with open(fname) as infile:
                    outfile.write(infile.read())

        # Run grep command to extract lines with IP addresses
        subprocess.run("grep -E \"\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b\" all_domain_info.txt | awk '{print $1}'", shell=True, stdout=open('domain_names.txt', 'w'))
        
        # Remove ';' character from domain_names.txt
        subprocess.run(["sed", "-i", "s/;//g", "domain_names.txt"])

        # Read domain_names.txt, remove blank lines and overwrite the file
        with open('domain_names.txt', 'r') as file:
            lines = [line for line in file if line.strip()]
        with open('domain_names.txt', 'w') as file:
            file.write(''.join(lines))
        
        # Read domain_names.txt, remove blank lines, trailing decimal and overwrite the file
        with open('domain_names.txt', 'r') as file:
            lines = [line.rstrip('.\n') for line in file if line.strip()]
        with open('domain_names.txt', 'w') as file:
            file.write('\n'.join(lines))

        # Delete all temporary files
        for fname in temp_files:
            os.remove(fname)  
        os.remove(f"{domain}_subdomainsonly.txt")
        
        print("Done!")
        print("Check the all_info.txt for all of the results and domain_names.txt for the domain names only.")

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Subdomain Discovery Script')
        parser.add_argument('domain', type=str, help='The domain to query')
        parser.add_argument('ip', type=str, help='The IP address to use for the query')

        args = parser.parse_args()

        main(args.domain, args.ip)   
