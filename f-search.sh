#!/bin/bash
target=$1

red='\033[91m'
green='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
violet='\033[95m'
end='\033[0m'

grep -HroiE "[a-z0-9_\\-]+: .*" $target | grep ".headers" \
| sed 's/headers://g' | rev | cut -d "." -f 1 | rev\
| grep -E "[A-Za-z0-9_\\-]+:" > all_header.txt

for line in $(cat all_header.txt | sed "s/ //g") 
do 
	header=$(echo "$line" | cut -d ":" -f 1)
	value=$(echo "$line" | sed -E 's/[A-Za-z0-9_\\-]+://g')
	echo -e "$cyan$header$end: $violet$value$end"
done && rm all_header.txt


