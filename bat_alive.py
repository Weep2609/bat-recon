#!/usr/bin/python3
import subprocess
import argparse
from pathlib import Path

# create color for output
class color():
    yellow = '\033[93m'
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

def logo():
    print(f"\n  {color.red}/(__M__)\\{color.end}\t{color.green}bat_alive.py{color.end}")
    print(f" {color.red}/, ,   , ,\\{color.end}")
    print(f"{color.red}/' ' 'V' ' '\\{color.end}\t{color.green}Written by weep2609{color.end}\n")

parse = argparse.ArgumentParser()

parse.add_argument('--httprobe', action='store_true', help='checks for HTTP on port 80, 8080 and HTTPS on port 443, 8443')
parse.add_argument('--httpx', action='store_true', help='Check for HTTPS and return title, status code, content length, content type')
parse.add_argument('-l', '--list', type=str, help='List raw subdomain')
parse.add_argument('-o', '--output', type=str, help='Output saved to', default='alive_subdomain.txt')

args = parse.parse_args()

list = Path(args.list)
output = Path(args.output)

def check_file():
    if list.is_file():
        print(f"{color.cyan}[+] Check alive subdomain{color.end}")
        print(f"{color.cyan}[+] Target:{color.end} {color.red}{list}{color.end}")
        print(f"{color.cyan}[+] Output:{color.end} {color.red}{output}{color.end}\n")
    else:
        print(f"{color.red}[-] Error: {list} is not found !{color.end}")
        print(f"{color.yellow}[-] Check the path of a file...{color.end}")
        exit()

def main():
    if args.httprobe:
        logo()
        check_file()
        print(f" {color.cyan}Starting httprobe...{color.end} ".center(50, '-'))
        subprocess.call(f'cat {list} | ./Tools/httprobe -p http:8080 -p https:8443 | tee {output}',shell=True)
        print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
        # Count lines
        count = 0 
        with open(f'{output}','rb') as f: 
            for line in f: 
                count+=1 
        print(f'{color.cyan}[+] Found{color.end} {color.red}{count}{color.end} {color.cyan}alive subdomains{color.end}\n')
        print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
        print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")
    elif args.httpx:
        logo()
        check_file()
        print(f" {color.cyan}Starting httpx...{color.end} ".center(50, '-'))
        subprocess.call(f'./Tools/httpx -title -status-code -content-length -silent -l {list} -o {output}',shell=True)
        print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
        # Count lines
        count = 0 
        with open(f'{output}','rb') as f: 
            for line in f: 
                count+=1 
        print(f'{color.cyan}[+] Found{color.end} {color.red}{count}{color.end} {color.cyan}alive subdomains{color.end}\n')
        print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
        print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")
    else:
        print(f"{color.red}\n[-] Error: You did chose --httprobe or --httpx flag{color.end}")
        print(f"{color.yellow}[-] Warning:{color.end} {color.cyan}Please use -h option to show the program usage{color.end}")
        exit()
main() 
