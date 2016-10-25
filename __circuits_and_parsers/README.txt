# parse all the files
IFS=$'\n'; for file in `find . -name "*.bench"`; do echo $file; ./grinder2.sh $file; mv .in $file.in; done;

# create necessary files
find . -name "*.bench.in" -exec ./after_grinder.sh {} \;



##### (ISCAS 85) #####
######################

## To create accessory files for the evaluation 
cd __circuits_and_parsers/
for file in `find ./ISCAS_85_Custom -name "*.in"`; do echo $file; ./after_grinder.sh $file; done

## To test the evaluation
cd __simulator/
IFS=$'\n'; for file in `find ./circuits2/ -name "*.in"`; do echo $file; file=`basename $file | cut -f1 -d"."`; python3 evaluator.py ./circuits2/$file\_ugp_input.txt output_ugp.txt ./circuits2/$file.in ./circuits2/$file\_prefix.txt False 10 output_readable.txt output_fitness.txt; done





## To be launched in the evaluator folder

IFS=$'\n'; for file in `find ./circuits2/ -name “*.bench.in"`; do echo $file; python3 evaluator.py $file\_ugp_input.txt output_ugp.txt $file $file\_input.txt False 10 output_readable.txt output_fitness.txt; done;

## JUST A TEST CASE OF ONE CIRCUIT

IFS=$'\n'; for file in `find ./circuits2/ -name "b01_C.bench.in"`; do echo $file; python3 evaluator.py $file\_ugp_input.txt output_ugp.txt $file $file\_input.txt False 10 output_readable.txt output_fitness.txt; done;