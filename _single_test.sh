## Author: Andrea Marcelli
## This script is used to (1) automatize the customization of ugp config file
## (2) then run the ugp experiment and (3) finally to plot the results.

#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "usage ./inner_script.sh circuit configuration experiment_number"
    exit
fi

p=`pwd`; name=`basename $p`
# echo "Current path: " $p
# echo "Current folder name: " $name
if [ ! $name = "HW_SEC_PACKAGE" ]
then
    echo "%% ERROR:: you are in the wrong folder" $$
    exit
else
    echo "%% Let's go on for this configuration" $$
fi


### create a new folder where to do the experiments
mkdir __exp/__exp_$3
cp __ugp_files/$1/* __exp/__exp_$3/

### HERE it is needed to change the configuration file
echo "%% UPDATE the config file" $$
cat __exp/__exp_$3/hwsec.constraints.xml.temp.xml  | sed "s/#MAXCOMB#/$2/g"> __exp/__exp_$3/hwsec.constraints.xml

# run Ugp and save the file
echo "%% RUN uGP" $$
(cd __exp/__exp_$3/; ugp3) > __exp/__exp_$3/$1.txt

# copy the finalizer script in the circuit folder
echo "%% COPY some useful stuff" $$
cp __utility/finalizer.sh __exp/__exp_$3/
cp __utility/plotter.py __exp/__exp_$3/
cp __utility/plotter2.py __exp/__exp_$3/
cp __utility/plotter3.py __exp/__exp_$3/

#Call the finalizer script in the folder
echo "%% CALL the finalizer" $$
(cd __exp/__exp_$3/; ./finalizer.sh $1.txt)

# remove all the stuff
echo "%% REMOVING some stuff" $$
rm __exp/__exp_$3/finalizer.sh
rm __exp/__exp_$3/plotter.py
rm __exp/__exp_$3/plotter2.py
rm __exp/__exp_$3/plotter3.py
rm __exp/__exp_$3/hwsec.constraints.xml

echo "%% FINISHED" $$
exit
