#!/bin/bash

if [[ "$#" -ne 1 ]]
then
  echo "USAGE:: ./finalizer output_uGP.txt"
  exit
fi

echo "# I will parse this file: " $1

line_number=`cat $1 | grep -n "Evolution terminated" | cut -f1 -d":"`
end_of_file=`wc -l $1 | sed "s/[$1,' ']//g"`
sed -n $(($line_number+2)),$(($end_of_file-1))p $1 | cut -f2 -d "{" | sed 's/}//g' > data.txt
python3 plotter.py data.txt plot1.png plot2.png
