## Author: Andrea Marcelli
## This script is used to (1) automatize the customization of ugp config file
## (2) then run the ugp experiment and (3) finally to plot the results.

#!/bin/bash

# Check input parameter
if [ "$#" -ne 4 ]; then
    echo "usage ./inner_script.sh circuit configuration experiment_number execution_time"
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


### Create a new folder where to do the experiments
mkdir __exp/__exp_$3
cp __ugp_files/$1/* __exp/__exp_$3/

### Update uGP the configuration file
echo "%% UPDATE the config file" $$
cat __exp/__exp_$3/hwsec.constraints.xml.temp.xml  | sed "s/#MAXCOMB#/$2/g"> __exp/__exp_$3/hwsec.constraints.xml
cat __exp/__exp_$3/hwsec.population.settings.xml.temp.xml  | sed "s/#MAXTIME#/$4/g"> __exp/__exp_$3/hwsec.population.settings.xml

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
(cd __exp/__exp_$3/; ./finalizer.sh $1.txt)

# remove all the stuff
echo "%% REMOVING some stuff" $$
rm -rf __exp/__exp_$3/utility

echo "%% FINISHED" $$
exit
