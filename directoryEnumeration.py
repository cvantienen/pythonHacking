### Created By: Cody Vantienen
### May 1 2020
## Python script for automated Directory Enumeration

#** REQUIRESCA FILE OF NAMES LABELED "WORDLIST.TXT" IN CURRENT DIRECTORY 
 

#!/usr/bin/env python3
import requests 
import sys 

sub_list = open("wordlist.txt").read() 
directories = sub_list.splitlines()

for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        pass
    else:
        print("Valid directory:" ,dir_enum)