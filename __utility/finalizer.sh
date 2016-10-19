#!/bin/bash

if [[ "$#" -ne 1 ]]
then
  echo "USAGE:: ./finalizer output_uGP.txt"
  exit
fi

echo "INFO:: I will parse this file: " $1

# Check if plotter file EXIST
if [ ! -f "plotter.py" ]
then
    echo "ERROR:: plotter.py does not exist"
    exit
fi

line_number=`cat $1 | grep -n "Evolution terminated" | cut -f1 -d":"`
echo "start_line:" $line_number
end_of_file=`wc -l $1 | sed 's/ //g' | sed "s/$1//g"`
echo "end_line:" $end_of_file

sed -n $(($line_number+2)),$(($end_of_file-1))p $1 | cut -f2 -d "{" | sed 's/}//g' > data.txt
echo "INFO:: call plotter"
python3 plotter.py data.txt plot1.png plot2.png

#Check if some files exist
if [ ! -f "output_fitness.txt" ]
then
    echo "ERROR:: output_fitness.txt does not exist"
    exit
fi

if [ ! -f "output_readable.txt" ]
then
    echo "ERROR:: output_readable.txt does not exist"
    exit
fi

if [ ! -f "plotter2.py" ] || [ ! -f "plotter3.py" ]
then
echo "ERROR:: plotter2.py or plotter3.py does not exist"
exit
fi

cat $1 | grep "^0." > data2_t.txt
echo "INFO:: call plotter 2"
python3 plotter2.py data.txt output_fitness.txt plot1_t.png plot2_t.png

echo "INFO:: call plotter 3"
python3 plotter3.py output_readable.txt plot3.png plot4.png plot5.png

echo "INFO:: Creating and compressing PF folder"
mkdir PF; mv PF_* ./PF/; tar -zcvf PF.tar.gz PF; rm -rf ./PF

sort -n -k1 -k4 -r  output_readable.txt > sorted_hd_len.txt
sort -n -k3 -k4 -r  output_readable.txt > sorted_nsr_len.txt

echo "INFO:: Best HD, minimum length" >> __final_notes.txt
cat sorted_hd_len.txt | grep "^0.5 " | tail -n 1 | cut -f1,4 -d" " >> __final_notes.txt

echo "INFO:: Number of rare signals, minimum length" >> __final_notes.txt
cat sorted_nsr_len.txt | tail -n 1 | cut -f3,4  -d" " >> __final_notes.txt

#Check if some files exist
echo "INFO:: Moving some files"

rm -rf ./plots
rm -rf ./temps

mkdir plots
mkdir temps

mv *.png ./plots
mv sorted_nsr_len.txt ./temps/
mv sorted_hd_len.txt ./temps/
mv data2_t.txt ./temps/
mv data.txt ./temps/


echo "INFO:: FINISHED"