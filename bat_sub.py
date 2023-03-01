#!/usr/bin/python3
import subprocess
import argparse
from pathlib import Path

# Note: 


# color
class color():
    yellow = '\033[93m'
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

# logo
def logo():
    print(f"\n  {color.red}/(__M__)\\{color.end}\tbatsub.py")
    print(f" {color.red}/, ,   , ,\\{color.end}\tVersion 1.1")
    print(f"{color.red}/' ' 'V' ' '\\{color.end}\tWrite by weep2609\n")

# Object Declaration
parse = argparse.ArgumentParser()
# Options
parse.add_argument('-l', '--list', type=str, metavar='List', help="List Domains (Exp: subdomain.txt)")
parse.add_argument('-d', '--domain', type=str, metavar='Domain', help="A single domain (Exp: tesla.com)")
parse.add_argument('-o', '--output', type=str, metavar='Output', default='output.txt', help='Output (default: output.txt)')
parse.add_argument('-w', '--wordlist', type=str, metavar='Wordlist', help="A wordlist")
parse.add_argument('--enum', help='Get subdomains from assetfinder, findomain, subfinder', action='store_true')
parse.add_argument('--brute', help='Brute force subdomain with massdns', action='store_true')
parse.add_argument('--httprobe', action='store_true', help='checks for HTTP on port 80 and HTTPS on port 443')
parse.add_argument('--httpx', action='store_true', help='Check for HTTPS and return title, status code, content length, content type')
parse.add_argument('--get_url', action='store_true', help='Get all urls with waybackurls or gau')
parse.add_argument('--extract_js', action='store_true', help='Extract all JavaScript files from host')
parse.add_argument('--endpoint', action='store_true', help='Extract all endpoints from JavaScript file')
parse.add_argument('--fff', action='store_true', help='Get all header and body of response (use fff of tomnomnom)')
parse.add_argument('--meg', action='store_true', help='Fetching one path for all hosts (use meg of tomnomnom) - default output save to "out" folder')

# Execution options
args = parse.parse_args()

domain = args.domain
wordlist = args.wordlist
list = args.list
output = args.output

# Check alive file
def check_file():
    if Path(args.list).is_file():
        print(f"{color.cyan}[+] Target:{color.end} {color.red}{list}{color.end}")
        print(f"{color.cyan}[+] Output:{color.end} {color.red}{output}{color.end}\n")
    else:
        print(f"{color.red}[-] Error: {list} is not found !{color.end}")
        print(f"{color.yellow}[-] Check the path of a file...{color.end}")
        exit()

# Check wordlist
def check_wordlist():
    if Path(args.wordlist).is_file():
        print(f"{color.cyan}[+] Brute force subdomain{color.end}")
        print(f"{color.cyan}[+] Target:{color.end} {color.red}{domain}{color.end}")
        print(f"{color.cyan}[+] Wordlist:{color.end} {color.red}{wordlist}{color.end}")
        print(f"{color.cyan}[+] Output:{color.end} {color.red}{output}{color.end}\n")
    else:
        print(f"{color.red}[-] Error: {wordlist} is not found !{color.end}")
        print(f"{color.yellow}[-] Check the path of a file...{color.end}")
        exit()

# output
def output_of_program(word):
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
    # Count lines
    count = 0 
    with open(f'{output}','rb') as f: 
        for line in f: 
            count+=1 
    print(f'{color.cyan}[+] Found{color.end} {color.red}{count}{color.end} {color.cyan}{word}{color.end}\n')
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")

# Find subdomain from wildcards
def sub():
    print(f" {color.cyan}Starting findomain...{color.end} ".center(50, '-'))
    subprocess.call(f'\n./Tools/findomain -f {list} -q | ./Tools/anew {output}',shell=True)
    print("\n" + f" {color.cyan}Starting Assetfinder...{color.end} ".center(50, '-') + "\n")
    subprocess.call(f'cat {list} | ./Tools/assetfinder --subs-only | ./Tools/anew {output}\n',shell=True)
    print("\n" + f" {color.cyan}Starting subfinder...{color.end} ".center(50, '-') + "\n")
    subprocess.call(f'./Tools/subfinder -dL {list} -silent | ./Tools/anew {output}',shell=True)
    output_of_program('subdomains')

# Brute force single subdomain
def brute():
    print(f" {color.cyan}Starting massdns...{color.end} ".center(50, '-'))
    subprocess.call(f"./Tools/massdns/scripts/subbrute.py {wordlist} {domain} \
        | ./Tools/massdns/bin/massdns -r ./Tools/massdns/lists/resolvers.txt -t A -o S -q -w ./massdns.txt && cat ./massdns.txt \
        | sed 's/A.*//' | sed 's/CN.*//' | sed 's/\..$//' | ./Tools/anew {output} && rm massdns.txt",shell=True)
    output_of_program('subdomains')

# Check alive subdomain with httprobe
def httprobe():
    print(f" {color.cyan}Starting httprobe...{color.end} ".center(50, '-'))
    subprocess.call(f'cat {list} | ./Tools/httprobe | tee {output}',shell=True)
    output_of_program('alive subdomains')

# Check alive subdomain with httprobe
def httpx():
    print(f" {color.cyan}Starting httpx...{color.end} ".center(50, '-'))
    subprocess.call(f'./Tools/httpx -title -status-code -content-length -silent -l {list} -o {output}',shell=True)
    output_of_program('alive subdomains')

# Get all urls from wayback machine
def url():
    if args.list:
        check_file()
        print(f" {color.cyan}Starting gau...{color.end} ".center(50, '-'))
        subprocess.call(f'cat {list} | ./Tools/gau | tee {output}',shell=True)
        output_of_program('urls')
    else:
        print(f"{color.cyan}[+] Target:{color.end} {color.red}{domain}{color.end}")
        print(f"{color.cyan}[+] Output:{color.end} {color.red}{output}{color.end}\n")
        print(f" {color.cyan}Starting waybackurls...{color.end} ".center(50, '-'))
        subprocess.call(f'echo {domain} | ./Tools/waybackurls | tee {output}',shell=True)
        output_of_program('urls')

# Extract JavaScript file from host
def js():
    print(f" {color.cyan}Starting subjs...{color.end} ".center(50, '-'))
    subprocess.call(f'cat {list} | ./Tools/subjs | tee {output}',shell=True)
    print('')
    print(f" {color.cyan}Starting hakcheckurl...{color.end} ".center(50, '-'))
    subprocess.call(f'cat {output} | ./Tools/hakcheckurl | grep "200" | cut -d " " -f2 | sort -u | tee alive_{output}',shell=True)
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
    # Count lines
    count1 = 0 
    with open(f'{output}','rb') as f: 
        for line in f: 
            count1+=1 
    count2 = 0
    with open(f'alive_{output}','rb') as a: 
        for line in a: 
            count+=1
    print(f'{color.cyan}[+] Found{color.end} {color.red}{count1}{color.end} {color.cyan}raw JS files{color.end}\n')
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
    print(f'{color.cyan}[+] Found{color.end} {color.red}{count2}{color.end} {color.cyan}alive JS files{color.end}\n')
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/alive_{output}{color.end}')
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")

# Extract endpoint from JavaScript file
def endpoint():
    print(f" {color.cyan}Starting linkfinder.py...{color.end} ".center(50, '-'))
    with open(f'{list}','r') as js_files:
        for js in js_files:
            print(f"\n{color.green}[*] ---->{color.end}{color.cyan} Target:{color.end} {color.red}{js}{color.end} {color.green}<----{color.end}")
            subprocess.call(f'python -W ignore ./Tools/LinkFinder/linkfinder.py -i {js} -o cli | ./Tools/anew {output}',shell=True)
    output_of_program('endpoints')
        
# review header and body of response
def fff():
    print(f" {color.cyan}Starting fff...{color.end} ".center(50, '-'))
    subprocess.call(f'cat {list} | ./Tools/fff -s 200 -o {output}',shell=True)
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
    print(f"{color.yellow}[*] Note:{color.end} {color.cyan}you can use command{color.end}") 
    print(f'\t{color.green}(grep -hroiE "[a-z0-9_\\-]+: .*" {output} | sort -u){color.green} {color.cyan}to get all header{color.end}')
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")

# Fetching one path for all hosts
def meg():
    print(f" {color.cyan}Starting meg...{color.end} ".center(50, '-'))
    subprocess.call(f'./Tools/meg --verbose ./Lists/content-wordlist/tomnomnom-short-wordlist.txt {list}',shell=True)
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/out/index{color.end}')
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")

def main():
    if args.enum:
        logo()
        print(f"{color.cyan}[+] Subdomain enumeration{color.end}")
        check_file()
        sub()
    elif args.brute:
        logo()
        check_wordlist()
        brute()
    elif args.httprobe:
        logo()
        print(f"{color.cyan}[+] Check alive subdomain{color.end}")
        check_file()
        httprobe()
    elif args.httpx:
        logo()
        print(f"{color.cyan}[+] Check alive subdomain{color.end}")
        check_file()
        httpx()
    elif args.get_url:
        logo()
        print(f"{color.cyan}[+] Get all urls{color.end}")
        url()
    elif args.extract_js:
        logo()
        print(f"{color.cyan}[+] Extract all JavaScript files{color.end}")
        check_file()
        js()
    elif args.endpoint:
        logo()
        print(f"{color.cyan}[+] Extract all endpoints{color.end}")
        check_file()
        endpoint()
    elif args.fff:
        logo()
        print(f"{color.cyan}[+] Get all headers vs body of response{color.end}")
        check_file()
        fff()
    elif args.meg:
        logo()
        print(f"{color.cyan}[+] Fetching lots of URLs{color.end}")
        check_file()
        meg()
    else:
        print(f"{color.yellow}[*] Warning: Use -h option to show the program usage{color.end}")
        exit()
main()
