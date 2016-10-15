#!/bin/bash

if [[ "$#" -ne 1 ]]
then
  echo "USAGE:: ./finalizer2 output_uGP.txt"
  exit
fi

echo "# I will parse this file: " $1

cat $1 | grep "NN_RS:" > data3.txt;

# while read a
# do
#   ahd=`echo $a | cut -f2 -d":" | cut -f1 -d" "`
#   as=`echo $a | cut -f3 -d":" | cut -f1 -d" "`
#   len=`echo $a| cut -f6 -d":" | cut -d" " -f1`
#   rs=`echo $a| cut -d":" -f5 | cut -d" " -f1`
#   echo $ahd" "$as" "$rs" "$len
# done < data3.txt > processed3.txt

while read a
do
  echo $a | cut -f2,3,5,6 -d":" | sed 's/[AVG_SIG:,N_RS:,LEN:]//g';
done < data3.txt > processed3.txt

python3 plotter3.py processed3.txt plot3.png plot4.png plot5.png
