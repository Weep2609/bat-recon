import subprocess
import argparse
from pathlib import Path

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
logo()

# Object Declaration
parse = argparse.ArgumentParser()
# Options
parse.add_argument('-l', '--list', type=str, metavar='List', required=True, help="List Domains (Exp: subdomain.txt)")
parse.add_argument('-o', '--output', type=str, metavar='output', default='output.txt', help='Output (default: output.txt)')

# Execution options
args = parse.parse_args()

target = Path(args.list)
output = Path(args.output)

# Check alive file
def check_file():
    if target.is_file():
        print(f"{color.cyan}[+] Target:{color.end} {color.red}{target}{color.end}\n")
    else:
        print(f"{color.red}[-] Error: {target} is not found !{color.end}")
        print(f"{color.yellow}[-] Check the path of a file...{color.end}")
        exit()
check_file()

# Find subdomain from wildcards
def sub():
    print(f" {color.cyan}Starting findomain...{color.end} ".center(50, '-'))
    subprocess.call(f'\n./Tools/findomain -f {target} -q | ./Tools/anew {output}',shell=True)
    print("\n" + f" {color.cyan}Starting Assetfinder...{color.end} ".center(50, '-') + "\n")
    subprocess.call(f'cat {target} | ./Tools/assetfinder --subs-only | ./Tools/anew {output}\n',shell=True)
    print("\n" + f" {color.cyan}Starting subfinder...{color.end} ".center(50, '-') + "\n")
    subprocess.call(f'./Tools/subfinder -dL {target} -silent | ./Tools/anew {output}',shell=True)
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -\n{color.end}")
    # Count lines
    count = 0 
    with open(f'{output}','rb') as f: 
        for line in f: 
            count+=1 
    print(f'{color.cyan}[+] Found{color.end} {color.red}{count}{color.end} {color.cyan}subdomains{color.end}\n')
    print(f'{color.cyan}[+] Output saved to{color.end} {color.red}{str(Path.cwd())}/{output}{color.end}')
    print(f"{color.yellow}\n- - - - - - - - - - - - - - - - - - -{color.end}")
sub()
