#!/bin/bash

target=${1}
argument_of_target=${2}
username=$(whoami)

echo Target file is ${target}
gcc -o target ${target}
./target ${argument_of_target} > log.txt
python3 plot.py ${target} ${username} 
read -p "Enter the user email: " email
mutt -s "FR_result" ${email} -a result.png
