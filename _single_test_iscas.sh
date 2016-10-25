## Author: Andrea Marcelli
## This script is used to (1) automatize the customization of ugp config file
## (2) then run the ugp experiment and (3) finally to plot the results.

#!/bin/bash

# Check input parameter
if [ "$#" -ne 4 ]; then
    echo "usage ./_single_test_iscas.sh circuit configuration experiment_number execution_time"
    exit
fi

# Check the current folder
p=`pwd`; name=`basename $p`
if [ $name = "HW_SEC_PACKAGE" ] || [ $name = "hw_sec_logic_simulator" ]
then
    echo "%% Let's go on for this configuration" $$
else
    echo "%% ERROR:: you are in the wrong folder" $$
    exit
fi

# Check if the __exp folder exists
if [ ! -d "__exp" ]
then
    echo "ERROR:: __exp folder does not exist"
    exit
fi

# Check if the __exp/collector folder exists
if [ ! -d "__exp/collector" ]
then
    mkdir __exp/collector
    echo "INFO:: __exp/collector folder created"
else
    #check if a folder is empty
    if [ -n "$(ls -A __exp/collector)" ]
    then
        echo "ERROR:: __exp/collector folder is not empty"
        exit
    fi
fi

# Define two dictionary with the configuration:

input_number=`python3 -c "circuit_inputs={'c17':5, 'c432':36, 'c499':41, 'c880':60, 'c1355':41 'c1908':51 'c2670':18 'c3540':37 'c5315':178 'c6288':32}; print(circuit_inputs[\"$1\"])"`
number_combination=`python3 -c "circuit_inputs={'c17':10, 'c432':10, 'c499':10, 'c880':10, 'c1355':5 'c1908':5 'c2670':5 'c3540':5 'c5315':5 'c6288':5}; print(circuit_inputs[\"$1\"])"`

### Create a new folder where to do the experiments
mkdir __exp/__exp_$3
cp __ugp_files/* __exp/__exp_$3/

### Update uGP the configuration file
echo "%% UPDATE the config file" $$
echo "#MAXCOMB#" $2 " #PORT_NUMBER#" $input_number " #MAXTIME#" $4 " #INPUT_UGP#" $1\_input_ugp.txt " #CIRCUIT#" iscas85\/$1.in " #PREFIX#" iscas85\/$1_prefix.txt " #NUMBER_COMBINATIONS#" $number_combination

cat __exp/__exp_$3/hwsec.constraints.xml.temp.xml  | sed "s/#MAXCOMB#/$2/g" | sed "s/#PORT_NUMBER#/$input_number/g" > __exp/__exp_$3/hwsec.constraints.xml
cat __exp/__exp_$3/hwsec.population.settings.xml.temp.xml  | sed "s/#MAXTIME#/$4/g" | sed "s/#INPUT_UGP#/$1\_input\_ugp.txt/g" | sed "s/#CIRCUIT#/iscas85\/$1.in/g" | sed "s/#PREFIX#/iscas85\/$1_prefix.txt/g" |  | sed "s/#NUMBER_COMBINATIONS#/$number_combination/g" > __exp/__exp_$3/hwsec.population.settings.xml

# Run uGP and save the output to a file
echo "%% RUN uGP" $$
(cd __exp/__exp_$3/; ugp3) > __exp/__exp_$3/$1.txt

# Copy the finalizer script in the circuit folder
echo "%% COPY some useful stuff" $$
cp __utility/finalizer.sh __exp/__exp_$3/
cp __utility/plotter.py __exp/__exp_$3/
cp __utility/plotter2.py __exp/__exp_$3/
cp __utility/plotter3.py __exp/__exp_$3/
cp __utility/plotter5.py __exp/__exp_$3/
cp __utility/_sources/converter.c __exp/__exp_$3/
cp __utility/_sources/print_best.c __exp/__exp_$3/

# Compile c files and delete the sources
(cd __exp/__exp_$3/; gcc converter.c -o converter; gcc print_best.c -o print_best; rm converter.c print_best.c)

#Call the finalizer script in the folder
echo "%% CALL the finalizer" $$
(cd __exp/__exp_$3/; ./finalizer.sh $1.txt;)

# Copy all the stuff in the collector folder
(cd __exp/__exp_$3/;
cp ./temps/best_hd.txt ../collector/$1_$3_best_hd.txt;
cp ./temps/best_01.txt ../collector/$1_$3_best_01.txt;
cp ./temps/best_20.txt ../collector/$1_$3_best_20.txt;
cp ./temps/best_sig_prob.txt ../collector/$1_$3_best_sig_prob.txt;)


# remove all the stuff
echo "%% REMOVING some stuff" $$
rm -rf __exp/__exp_$3/utility

echo "%% FINISHED" $$
exit
