#!/bin/bash
if [ "$#" -ne 1 ]; then
  echo "usage ./utils.sh number"
  exit
fi
python -c "import random; print([random.randint(0,2) for i in range($1)])" | sed 's/,//g' | sed 's/\[//g' | sed 's/\]//g'
