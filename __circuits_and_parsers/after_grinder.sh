#! /bin/bash

# calculate the number of inputs and ports
inputs=`cat $1 | grep I | cut -f2 -d"I" | cut -f1  -d" " | sort -n | uniq | wc -l `
ports=$(wc -l < $1)

echo $1 inputs: $inputs ports: $ports

# Compute the name of the output file
OUTPUT_FILE=`echo $1 | cut -f1 -d"."`
echo "FILE: $OUTPUT_FILE"

# Create accessory files
../__utility/_else/utils_0_2.sh $ports > $OUTPUT_FILE\_ugp\_input.txt
python3 ../__utility/_else/writer.py $inputs True 10 tempppp.txt
cat tempppp.txt | sed "s/\[//g" | sed "s/\]//g" | sed "s/,//g" > $OUTPUT_FILE\_prefix.txt
rm tempppp.txt