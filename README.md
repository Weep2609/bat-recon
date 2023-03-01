# bat-recon
usage: batsub.py [-h] [-l List] [-d Domain] [-o Output] [-w Wordlist] [--enum] [--brute] [--httprobe] [--httpx] [--get_url] [--extract_js]
                 [--endpoint] [--fff] [--meg]

options:
  -h, --help            show this help message and exit
  -l List, --list List  List Domains (Exp: subdomain.txt)
  -d Domain, --domain Domain
                        A single domain (Exp: tesla.com)
  -o Output, --output Output
                        Output (default: output.txt)
  -w Wordlist, --wordlist Wordlist
                        A wordlist
  --enum                Get subdomains from assetfinder, findomain, subfinder
  --brute               Brute force subdomain with massdns
  --httprobe            checks for HTTP on port 80 and HTTPS on port 443
  --httpx               Check for HTTPS and return title, status code, content length, content type
  --get_url             Get all urls with waybackurls or gau
  --extract_js          Extract all JavaScript files from host
  --endpoint            Extract all endpoints from JavaScript file
  --fff                 Get all header and body of response (use fff of tomnomnom)
  --meg                 Fetching one path for all hosts (use meg of tomnomnom) - default output save to "out" folder
