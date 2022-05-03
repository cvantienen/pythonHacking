# Created by: Cody Vantienen
# May 1 2022 
# python script for Subdomain Enumeration 



# **IMPORNTANT** 
# Need textfile list of subdomains named "subdomains.txt" 

#!/usr/bin/env python3
import requests 
import sys 

sub_list = open("subdomains.txt").read() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)