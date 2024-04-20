import requests
import sys
import pyfiglet

print(pyfiglet.figlet_format("SUB ENUM TOOL"))

if len(sys.argv) !=2:
    print ("Invalid Argument")
    print (" {} <domain name>".format(sys.argv[0]))
    exit()

with open ("subdomains_wordlist.txt","r") as list:
    for wordlist in list:
        wordlist = wordlist.strip()
        subdomain = f"https://{wordlist}.{sys.argv[1]}"

        try:
            requests.get(subdomain)
            print ("Valid Domains: {} ".format(subdomain))
        except requests.ConnectionError:
            pass
        
            