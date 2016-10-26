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
- matplotlib



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
[Note: the configuration with all the range_of_integers parameters for each circuit to test, is located in cons.csv file. Please, refer to prob_calculator.xlsx for possible values.]


—-To run a single experiment —-

1) go in the root folder of the project (hw_sec_logic_simulator)
2) run:: ./_all_tests_iscas.sh circuit range_of_integers experiment_number seconds
example:: ./_single_test_iscas.sh c499 20 1 10000
[note: the second script modifies several variables inside uGP configuration files]


—-To run the experiments: low level way [legacy] [not working anymore.. it is required to change some parameters in the config files] —-

1) Go in the __upg_files folder and select the circuit you want to test
2) Run:: ugp3 > circuit.txt
3) Run the finalizer script (from __utility folder) to get the plots:: ./finalizer.sh circuit.txt
[Note: plotter*.py must be in the same folder of finalizer.sh]



—-If you simply want to run the evaluator:—-

1) Go in the __simulator folder
2) run one of the following commands (with necessary variations):
python3 evaluator.py ./iscas85/c7552_ugp_input.txt output_ugp.txt ./iscas85/c7552.in ./iscas85/c7552_prefix.txt False 1 output_readable.txt output_fitness.txt


Note:
The file passed as third parameters contains all the input combinations that will be tested on the circuit.
If the number of circuit inputs is small (like in the c17), it is possible to make exhaustive experiments, trying all the possible combinations.

In the same way, for the new inputs added in the circuit, if the number is small it is possible to try all the combinations using the True flag in the command string. Otherwise, set it to False and use a specified number of random pattern.

In order to create a new files with input patterns (from __simulator folder) use the following command:
../__utility/utils_0_1.sh 41 100 > circuits/prefix_c499_100.txt



