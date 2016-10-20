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
sed -n $(($line_number+2)),$(($end_of_file-1))p $1 | cut -f2 -d "{" | sed 's/}//g' > best_output_fitness.txt

echo "INFO:: call plotter"
python3 plotter.py best_output_fitness.txt expHD.png expPROB.png

#Check if some files exist
if [ ! -f "output_fitness.txt" ] || [ ! -f "output_readable.txt" ]
then
    echo "ERROR:: output_fitness.txt or output_readable.txt do not exist"
    exit
fi

if [ ! -f "plotter2.py" ] || [ ! -f "plotter3.py" ]
then
echo "ERROR:: plotter2.py or plotter3.py does not exist"
exit
fi

echo "INFO:: call plotter 2"
python3 plotter2.py best_output_fitness.txt output_fitness.txt expHD_evaluations.png expPROB_evaluations.png

echo "INFO:: call plotter 3"
python3 plotter3.py output_readable.txt HD_Len_evaluations.png PROB_Len_evaluations.png NR20_len_evaluations.png


#Check if some files exist
if [ ! -f "print_best" ] || [ ! -f "converter" ] || [ ! -f "plotter5.py" ]
then
echo "ERROR:: print_best or converter or plotter5.py do not exist"
exit
fi

echo "INFO:: Call plotter 5"
./converter
sort -n -k4 -k1 output_readable_proc.txt > output_readable_proc_sorted_k4k1.txt
sort -n -k4 -k2 output_readable_proc.txt > output_readable_proc_sorted_k4k2.txt
sort -n -k4 -k3 output_readable_proc.txt > output_readable_proc_sorted_k4k3.txt
sort -n -k4 -k5 output_readable_proc.txt > output_readable_proc_sorted_k4k5.txt
./print_best
python3 plotter5.py best_hd.txt best_sig_prob.txt best_20.txt best_01.txt HD_Len.png PROB_Len.png NR20_len.png NR01_len.png


# Some statistical info
rm __final_notes.txt
echo "BEST HD [Note: 0.0 best, 0.5 worst] over key length:" `sort -k1 -k4 -n output_readable_proc.txt | head -n 1 | cut -f1,4 -d" "` >> __final_notes.txt
echo "BEST SIG PROB [Note: 0.0 best, 0.5 worst] over key length:" `sort -k2 -k4 -n output_readable_proc.txt | head -n 1 | cut -f2,4 -d" "` >> __final_notes.txt
echo "MIN RARE SIGNAL (0.20) over key length:" `sort -k3 -k4 -n output_readable_proc.txt | head -n 1 | cut -f3,4 -d" "`  >> __final_notes.txt
echo "MIN RARE SIGNAL (0.01) over key length: [note: reverse order]" `sort -k5 -k4 -n output_readable_proc.txt | head -n 1 | cut -f5,4 -d" "`  >> __final_notes.txt
echo "key length range:" `head -n1 output_readable_proc_sorted_k4k1.txt | cut -f4 -d" "` - `tail -n 1 output_readable_proc_sorted_k4k1.txt | cut -f4 -d" "` >> __final_notes.txt


#Check if some files exist
echo "INFO:: Moving some files"

echo "INFO:: Creating and compressing PF folder"
mkdir PF; mv PF_* ./PF/; tar -zcvf PF.tar.gz PF; rm -rf ./PF

rm -rf ./plots
rm -rf ./temps
rm -rf ./inputs
rm -rf ./utility

mkdir plots
mkdir temps
mkdir inputs
mkdir utility

mv *.png ./plots
mv best_* ./temps/
mv output_readable_proc* ./temps/

#rm output_readable_proc*

#rm -rf ./temps/

mv plotter* ./utility/
mv finalizer.sh ./utility/
mv converter ./utility/
mv print_best ./utility/

mv $1 ./inputs/
mv output_fitness.txt ./inputs/
mv output_readable.txt ./inputs/

echo "INFO:: FINISHED"
