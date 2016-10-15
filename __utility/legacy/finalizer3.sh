#!/bin/bash

if [[ "$#" -ne 1 ]]
then
  echo "USAGE:: ./finalizer2 processed3.txt"
  exit
fi

sort -n -k1 -k4 -r  processed3.txt > sorted_hd_len.txt
sort -n -k3 -k4 -r  processed3.txt > sorted_nsr_len.txt

echo "best HD, minimum length" >> __final_notes.txt
cat sorted_hd_len.txt | grep "^0.5 " | tail -n 1 | cut -f1,4 -d" " >> __final_notes.txt

echo "number of rare signals, minimum length" >> __final_notes.txt
cat sorted_nsr_len.txt | tail -n 1 | cut -f3,4  -d" " >> __final_notes.txt
