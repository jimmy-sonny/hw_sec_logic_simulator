## README file ##

AUTHOR: andrea marcelli
EMAIL: andrea(dot)marcelli(at)polito(dot)it
PROJECT: Combinatorial circuit evaluator

This project was developed from a "Combinational Logic Simulator" by Byron Phung.
Some files (were specified) are under Copyright of Byron Phung.


{} REQUIRED SOFTWARE {}

— uGP [http://ugp3.sourceforge.net]
- python3
- numpy for python3




{} FOLDERS {}

__utility: contains utility script to create input and evaluation strings
__ugp_files: contains all the files needed to run ugp. In each folder there is a specific configuration for the circuit
__simulator: it is the circuit evaluator written in python
__circuits_and_parsers: contains the circuits and the utility script for the format conversion of the circuit
__exp: where the results of the experiments are stored



{} INSTRUCTIONS {}

—-To run all the experiments —-
1) go in the root folder of the project (hw_sec_logic_simulator)
2) run:: ./_all_tests.sh
[Note: the configuration with all the range_of_integers parameters for each circuit is located in cons.csv file. Please, refer to prob_calculator.xlsx for possible values.]


—-To run a single experiment —-
1) go in the root folder of the project (hw_sec_logic_simulator)
2) run:: ./_single_test.sh circuit range_of_integers experiment_number seconds
example:: ./_single_test.sh c499 20 1 10000
[Note: range of integers affects the configuration of uGP: it is a way to configure the length of the new key to test]


—-To run the experiments: low level way [legacy] [not recommended] —-

1) Go in the __upg_files folder and select the circuit you want to test
2) Run:: ugp3 > circuit.txt
3) Run the finalizer script (from __utility folder) to get the plots:: ./finalizer.sh circuit.txt
[Note: plotter.py must be in the same folder of finaliser.sh]



—-If you simply want to run the evaluator:—-

1) Go in the __simulator folder
2) run one of the following commands (or meaningful variations):

python3 evaluator.py ./circuits/input_ugp_c17.txt output_ugp.txt ./circuits/c17.in ./circuits/prefix_c17.txt True output_readable.txt output_fitness.txt
python3 evaluator.py ./circuits/input_ugp_c499.txt output_ugp.txt ./circuits/c499.in ./circuits/prefix_c499.txt False 10 output_readable.txt output_fitness.txt
python3 evaluator.py ./circuits/input_ugp_c880.txt output_ugp.txt ./circuits/c880.in ./circuits/prefix_c880.txt False 10 output_readable.txt output_fitness.txt
python3 evaluator.py ./circuits/input_ugp_c1355.txt output_ugp.txt ./circuits/c1355.in ./circuits/prefix_c1355.txt False 10 output_readable.txt output_fitness.txt
python3 evaluator.py ./circuits/input_ugp_c2670.txt output_ugp.txt ./circuits/c2670.in ./circuits/prefix_c2670.txt False 1 output_readable.txt output_fitness.txt
python3 evaluator.py ./circuits/input_ugp_c5315.txt output_ugp.txt ./circuits/c5315.in ./circuits/prefix_c5315.txt False 1 output_readable.txt output_fitness.txt
python3 evaluator.py ./circuits/input_ugp_c6288.txt output_ugp.txt ./circuits/c6288.in ./circuits/prefix_c6288.txt False 1 output_readable.txt output_fitness.txt

Note:
The file passed as third parameters contains all the input combinations that will be tested on the circuit.
If the number of circuit inputs is small (like in the c17), it is possible to make exhaustive experiments, trying all the possible combinations.

In the same way, for the new inputs added in the circuit, if the number is small it is possible to try all the combinations using the True flag in the command string. Otherwise, set it to False and use a specified number of random pattern.

In order to create a new files with input patterns (from __simulator folder) use the following command:
../__utility/utils_0_1.sh 41 100 > circuits/prefix_c499_100.txt



