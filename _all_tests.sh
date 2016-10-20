#!/bin/bash

# Check the folder in whick you run this script:
p=`pwd`; name=`basename $p`
echo "INFO:: Current path: " $p
echo "INFO:: Current folder name: " $name

if [ $name = "HW_SEC_PACKAGE" ] || [ $name = "hw_sec_logic_simulator" ]
then
    echo "%% Let's go on for this configuration" $$
else
    echo "%% ERROR:: you are in the wrong folder" $$
    exit
fi

# Create a new temp file with the configuration
cat conf.csv | sed 's/;/ /g' > conf.txt

# Check if the folder __exp exists
if [ ! -d "__exp" ]
then
    echo "INFO:: create __exp folder"
    mkdir __exp
else
    #check if a folder is empty
    if [ -n "$(ls -A __exp)" ]
    then
        echo "ERROR:: __exp folder is not empty"
        exit
    fi
fi

exp_number=1
exec_time=250
while read circuit configs
do
    echo "INFO:: circuit:" $circuit
    for conf in $configs
    do
        echo "INFO:: conf:" $conf

        ./_single_test.sh $circuit $(($conf-1)) $exp_number $exec_time &
        pid=`echo $!`
        echo "created process with PID: " $pid
        exp_number=$(($exp_number+1))
    done
done < conf.txt

# wait for all the pids to finish:
#  TODO:
# pack all the results!
#  TODO:

# Delete previous files
rm conf.txt
