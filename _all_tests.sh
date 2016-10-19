#!/bin/bash

# Check the folder in whick you run this script:
p=`pwd`; name=`basename $p`
echo "Current path: " $p
echo "Current folder name: " $name
if [ ! $name = "HW_SEC_PACKAGE" ]
then
    echo "ERROR:: you are in the wrong folder"
    exit
else
    echo "Let's go on"
fi

cat conf.csv | sed 's/;/ /g' > conf.txt

temp=1
while read circuit configs
do
    echo "CIRCUIT::" $circuit
    for conf in $configs
    do
        echo "CONF::" $conf
        
        ./_single_test.sh $circuit $conf &
        pid=`echo $!`
        echo "created process with PID: " $pid
        temp=$((temp+1))
    done
done < conf.txt

# wait for all the pids to finish:
#  TODO:
# pack all the results!
#  TODO:

# Delete previous files
rm conf.txt
