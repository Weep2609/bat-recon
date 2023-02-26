#!/usr/bin/python3
import sys
import subprocess

class color():
    cyan = '\033[96m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'

if len(sys.argv) == 2:
    print(f"\n{color.yellow}- - - - - - - - - - - - - - - - - - - -{color.end}")
    print(f"{color.cyan}[+] Target:{color.end} {color.red}{sys.argv[1]}{color.end}")
    print(f"{color.yellow}- - - - - - - - - - - - - - - - - - - -{color.end}\n")
    subprocess.call(f'curl -s "https://crt.sh/?q=%25.{sys.argv[1]}" \
                        | grep -oE "[\.a-zA-Z0-9-]+\.{sys.argv[1]}" \
                        | sort -u',shell=True)
else:
    print(f"\n{color.red}[-] Warning: Error{color.end}")
    print(f"{color.cyan}[-] Usage: python3 crt.py [domain]{color.end}")
    exit()
