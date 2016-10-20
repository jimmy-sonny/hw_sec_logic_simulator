#!/bin/bash
if [ "$#" -ne 2 ]; then
  echo "usage ./utils.sh length repetitions"
  exit
fi
for i in `seq $2`
do
python -c "import random; print([random.randint(0,1) for i in range($1)])" | sed 's/,//g' | sed 's/\[//g' | sed 's/\]//g'
done
