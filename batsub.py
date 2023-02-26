import subprocess
import argparse
from pathlib import Path
# Note: include subfinder, assetfinder, findomain, anew tools >> Tools folder 

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
parse.add_argument('-l', '--list', type=str, metavar='', required=True, help="List Domains (Exp: subdomain.txt)")
parse.add_argument('-o', '--output', type=str, metavar='', default='output.txt', help='Output (default: output.txt)')
parse.add_argument('--enum', help='Get subdomains from assetfinder, findomain, subfinder', action='store_true')

# Execution options
args = parse.parse_args()

list = Path(args.list)
output = Path(args.output)

# Check alive file
def check_file():
    if list.is_file():
        print(f"{color.cyan}[+] Subdomain enumeration{color.end}")
        print(f"{color.cyan}[+] Target:{color.end} {color.red}{list}{color.end}")
        print(f"{color.cyan}[+] Output:{color.end} {color.red}{output}{color.end}\n")
    else:
        print(f"{color.red}[-] Error: {list} is not found !{color.end}")
        print(f"{color.yellow}[-] Check the path of a file...{color.end}")
        exit()

# Find subdomain from wildcards
def sub():
    print(f" {color.cyan}Starting findomain...{color.end} ".center(50, '-'))
    subprocess.call(f'\n./Tools/findomain -f {list} -q | ./Tools/anew {output}',shell=True)
    print("\n" + f" {color.cyan}Starting Assetfinder...{color.end} ".center(50, '-') + "\n")
    subprocess.call(f'cat {list} | ./Tools/assetfinder --subs-only | ./Tools/anew {output}\n',shell=True)
    print("\n" + f" {color.cyan}Starting subfinder...{color.end} ".center(50, '-') + "\n")
    subprocess.call(f'./Tools/subfinder -dL {list} -silent | ./Tools/anew {output}',shell=True)
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
    # Count lines
    count = 0 
    with open(f'{output}','rb') as f: 
        for line in f: 
            count+=1 
    print(f'{color.cyan}[+] Found{color.end} {color.red}{count}{color.end} {color.cyan}subdomains{color.end}\n')
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")

def main():
    if args.enum:
        logo()
        check_file()
        sub()
    else:
        print(f"{color.yellow}[*] Warning: Use -h option to show the program usage{color.end}")
        exit()

main()
