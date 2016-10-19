#!/bin/bash

if [[ "$#" -ne 1 ]]
then
  echo "USAGE:: ./finalizer output_uGP.txt"
  exit
fi

echo "# I will parse this file: " $1

line_number=`cat $1 | grep -n "Evolution terminated" | cut -f1 -d":"`
echo "start_line:" $line_number
end_of_file=`wc -l $1 | sed 's/ //g' | sed "s/$1//g"`
echo "end_line:" $end_of_file

sed -n $(($line_number+2)),$(($end_of_file-1))p $1 | cut -f2 -d "{" | sed 's/}//g' > data.txt
echo "CALL PLOTTER"
python3 plotter.py data.txt plot1.png plot2.png

cat $1 | grep "^0." > data2_t.txt
echo "CALL PLOTTER 2"
python3 plotter2.py data.txt output_fitness.txt plot1_t.png plot2_t.png

echo "CALL PLOTTER 3"
python3 plotter3.py output_readable.txt plot3.png plot4.png plot5.png
