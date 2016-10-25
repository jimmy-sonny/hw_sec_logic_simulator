#! /bin/bash

inputs=`cat $1 | grep I | cut -f2 -d"I" | cut -f1  -d" " | sort -n | uniq | wc -l `
ports=$(wc -l < $1)
echo $1 inputs: $inputs ports: $ports
./utils_0_2.sh $ports > $1\_ugp\_input.txt
python3 writer.py $inputs True 10 tempppp.txt
filename=$1
filename=`echo $filename | sed 's/\.benc\.in//g'`
cat tempppp.txt | sed "s/\[//g" | sed "s/\]//g" | sed "s/,//g" > $filename\_input.txt
rm tempppp.txt