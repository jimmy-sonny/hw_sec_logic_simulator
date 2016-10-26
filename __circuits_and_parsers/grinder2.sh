
## Author: Andrea Marcelli
## Verilog to custom convert
## Plus some utility functions

#!/bin/bash

#Controllo paremetri linea di comando
if [ "$#" -ne 1 ]; then
  echo "usage ./grinder.sh input_file"
  exit
fi

# Controllo che il file di input esista
FILE=$1
if [ ! -f $FILE ]; then
    echo "File not found!" $FILE
    exit
fi

# Compute the name of the output file
OUTPUT_FILE=`echo $FILE | cut -f1 -d"."`
OUTPUT_FILE=`echo $OUTPUT_FILE.in`
echo "OUTPUT_FILE: $OUTPUT_FILE"

cat $1 | grep -v "#" | sed 's/[= (,(,)]/ /g' | grep INPUT | sed 's/INPUT//g' > temp0.txt;
cat $1 | grep -v "#" | sed 's/[= (,(]/ /g' | sed 's/)/;/g' | grep -v -e INPUT -e OUTPUT > temp.txt;
circuit=`cat temp.txt`;

index=0;
for input in `cat temp0.txt`;
do
  circuit=`echo $circuit | sed "s/\b$input\b/I$index/g"`;
  index=$(($index+1));
done;

circuit=`echo $circuit | sed 's/; /;/g' | sed 's/U//g'`

IFS=$';';
for i in $circuit;
do
  echo $i;
done > tmp_output.txt;

index=0
IFS=$' ';
while read a b c;
do
  echo $a $b\_$index $b $c
  index=$(($index+1))
done < tmp_output.txt > $OUTPUT_FILE

rm tmp_output.txt
rm temp0.txt
rm temp.txt

#cat $OUTPUT_FILE
