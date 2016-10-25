
## Author: Andrea Marcelli
## Verilog to custom convert
## Plus some utility functions

#!/bin/bash

# Controllo paremetri linea di comando
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

# Calculate the offsets of the inputs and outputs of the cirtuits
start_input=`cat $FILE | grep input -n | cut -f1 -d":"`
start_output=`cat $FILE | grep output -n | cut -f1 -d":"`
start_wire=`cat $FILE | grep wire -n | cut -f1 -d":"`

# Get all the circuits inputs
inputs=`sed -n $start_input,$(($start_output-1))p $FILE`
inputs=`echo $inputs | sed 's/input//g' | sed 's/,/ /g' | cut -f1 -d";"`

# Inputs number
inputs_number=`echo $inputs | awk '{printf "%s\n", NF};'`
echo "inputs_number: $inputs_number"

outputs=`sed -n $start_output,$(($start_wire-2))p $FILE`
outputs=`echo $outputs | sed 's/output//g' | sed 's/,/ /g' | cut -f1 -d";"`

# Outputs number
outputs_number=`echo $outputs | awk '{printf "%s\n", NF};'`
echo "outputs_number: $outputs_number"

# Findout where is the circuit description
start_parsing=`cat $FILE | grep -E 'not|and|or|nand|nor|xor|xnor' -n | cut -f1 -d ":" | sort -n | sed -n 1,1p`
end_of_parsing=`cat $FILE | grep -n endmodule | cut -f1 -d":"`
#echo "Start parsing at line: " $start_parsing
#echo "End of parsing at line: " $end_of_parsing

# Save to a local variable the circuit description
circuit=`sed -n $start_parsing,$(($end_of_parsing-1))p $FILE`

# Substitute all the inputs with I... to be consistent with the custom representation
for i in $inputs
do
  j=`echo $i | sed 's/G/I/g'`
  circuit=`echo $circuit | sed "s/$i,/$j,/g"`
  circuit=`echo $circuit | sed "s/$i)/$j)/g"`
done

# Some textual manipulation for further operation
circuit=`echo $circuit | sed 's/; /;/g' | sed 's/G//g'`

# Change the delimiter. Save everything to a temp file
IFS=$';'
for i in $circuit
do
  echo $i
done > temp.txt

# Get all the variables and print them in the new format
IFS=$' '
while read port_type details
do
  port_name=`echo $details | cut -f1 -d"("`
  port_inputs_and_output=`echo $details | cut -f2 -d"(" | sed 's/)//g'`
  port_output=`echo $port_inputs_and_output | cut -f1 -d","`
  port_inputs=`echo $port_inputs_and_output | awk -F, '{for(i=2;i<=NF;i++){printf "%s ", $i}; printf "\n"}'`
  echo $port_output $port_name $port_type $port_inputs
done < temp.txt > $OUTPUT_FILE

# Delete the temporary file
rm temp.txt

# Count the signal number
signals_number=`wc -l $OUTPUT_FILE | awk '{printf "%d\n", $1}'`
signals_number=$(( $signals_number-$outputs_number ))
echo "signals_number: $signals_number"
