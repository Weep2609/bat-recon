#!/usr/bin/python3
import argparse
import subprocess
from pathlib import Path
# Note: Base on output of massdns

# color
class color():
    yellow = '\033[93m'
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

# logo
def logo():
    print(f"\n  {color.red}/(__M__)\\{color.end}\t{color.green}bat_brute.py{color.end}")
    print(f" {color.red}/, ,   , ,\\{color.end}")
    print(f"{color.red}/' ' 'V' ' '\\{color.end}\t{color.green}Written by weep2609{color.end}\n")

# Object Declaration
parse = argparse.ArgumentParser()
# Options
parse.add_argument('-d', '--domain', type=str, metavar='', required=True, help="A single domain (Exp: tesla.com)")
parse.add_argument('-w', '--wordlist', type=str, metavar='', required=True, help="A wordlist")
parse.add_argument('-o', '--output', type=str, metavar='', default='bruteforce_output.txt', help='Output (default: bruteforce_output.txt)')
parse.add_argument('--brute', help='Brute force subdomain with massdns', action='store_true')

# Execution options
args = parse.parse_args()

target = args.domain
wordlist = Path(args.wordlist)
output = Path(args.output)

# Check alive wordlist 
def check_wordlist():
    if wordlist.is_file():
        print(f"{color.cyan}[+] Brute force subdomain{color.end}")
        print(f"{color.cyan}[+] Target:{color.end} {color.red}{target}{color.end}")
        print(f"{color.cyan}[+] Wordlist:{color.end} {color.red}{wordlist}{color.end}")
        print(f"{color.cyan}[+] Output:{color.end} {color.red}{output}{color.end}\n")
    else:
        print(f"{color.red}[-] Error: {wordlist} is not found !{color.end}")
        print(f"{color.yellow}[-] Check the path of a file...{color.end}")
        exit()

# Brute force subdomain with massdns
def brute():
    print(f" {color.cyan}Starting massdns...{color.end} ".center(50, '-'))
    subprocess.call(f"./Tools/massdns/scripts/subbrute.py {wordlist} {target} \
        | ./Tools/massdns/bin/massdns -r ./Tools/massdns/lists/resolvers.txt -t A -o S -q -w ./massdns.txt && cat ./massdns.txt \
        | sed 's/A.*//' | sed 's/CN.*//' | sed 's/\..$//' | ./Tools/anew {output} && rm massdns.txt",shell=True)
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
    # Count lines
    count = 0 
    with open(f'{output}','rb') as f: 
        for line in f: 
            count+=1 
    print(f'{color.cyan}[+] Found{color.end} {color.red}{count}{color.end} {color.cyan}subdomains{color.end}\n')
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")

# Main function
def main():
    if args.brute:
        logo()
        check_wordlist()
        brute()
    else:
        print(f"{color.yellow}[*] Warning: Use -h option to show the program usage{color.end}")
        exit()
main()
