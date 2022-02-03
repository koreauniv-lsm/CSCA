#!/bin/bash

argument_of_target=${1}
username=$(whoami)

echo Step 1: Flush+Reload.c is running ... 
gcc -o target Flush+Reload.c

echo Step 2: Output the latency of probe array per cache line to log.txt
./target ${argument_of_target} > log.txt
head -n 1 log.txt

echo Step 3: The result of Flush+Reload by username is intuitively drawn and saved as result.png.
python3 plot.py Flush+Reload.c ${username} 

echo Step 4: Send result.png to the user email
read -p "- Enter the user email: " email
mutt -s "FR_result" ${email} -a result.png
