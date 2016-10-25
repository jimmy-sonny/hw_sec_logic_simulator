# parse all the files
IFS=$'\n'; for file in `find . -name "*.bench"`; do echo $file; ./grinder2.sh $file; mv .in $file.in; done;

# create necessary files
find . -name "*.bench.in" -exec ./script.sh {} \;


## Collector
## To be launched in the evaluator folder

IFS=$'\n'; for file in `find ./circuits2/ -name “*.bench.in"`; do echo $file; python3 evaluator.py $file\_ugp_input.txt output_ugp.txt $file $file\_input.txt False 10 output_readable.txt output_fitness.txt; done;

## JUST A TEST CASE OF ONE CIRCUIT

IFS=$'\n'; for file in `find ./circuits2/ -name "b01_C.bench.in"`; do echo $file; python3 evaluator.py $file\_ugp_input.txt output_ugp.txt $file $file\_input.txt False 10 output_readable.txt output_fitness.txt; done;




### WORKING::

./circuits2//b01_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.4875 AVG_SIG:0.364300271739 N_RS_20:24 NN_RS_20:16 LEN:29 NI:5 N_RS_01:7 NN_RS_01:2
0.034482758620689655 0.847614758783 0.499153112423

./circuits2//b01_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.4925 AVG_SIG:0.329585705773 N_RS_20:26 NN_RS_20:16 LEN:19 NI:5 N_RS_01:5 NN_RS_01:2
0.05263157894736842 0.81671940611 0.480119424685

./circuits2//b02_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.365625 AVG_SIG:0.396829044118 N_RS_20:11 NN_RS_20:7 LEN:12 NI:4 N_RS_01:1 NN_RS_01:0
0.08333333333333333 0.844866626718 0.470788722411

./circuits2//b02_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.30625 AVG_SIG:0.420535714286 N_RS_20:10 NN_RS_20:6 LEN:14 NI:4 N_RS_01:0 NN_RS_01:0
0.07142857142857142 0.849015468875 0.462329475149

./circuits2//b03_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.615714285714 AVG_SIG:0.344624533582 N_RS_20:75 NN_RS_20:40 LEN:79 NI:34 N_RS_01:51 NN_RS_01:1
0.012658227848101266 0.838392928286 0.527723959494

./circuits2//b03_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.529285714286 AVG_SIG:0.340163010817 N_RS_20:62 NN_RS_20:43 LEN:67 NI:34 N_RS_01:21 NN_RS_01:0
0.014925373134328358 0.823162575584 0.562631880366

./circuits2//b04_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.472307692308 AVG_SIG:0.332770602986 N_RS_20:423 NN_RS_20:230 LEN:342 NI:77 N_RS_01:280 NN_RS_01:16
0.0029239766081871343 0.821802381443 0.581811532437

./circuits2//b05_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.48350877193 AVG_SIG:0.333630458914 N_RS_20:424 NN_RS_20:230 LEN:331 NI:35 N_RS_01:329 NN_RS_01:44
0.0030211480362537764 0.818651293481 0.554975228236

./circuits2//b07_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.554081632653 AVG_SIG:0.328452269499 N_RS_20:320 NN_RS_20:157 LEN:236 NI:50 N_RS_01:223 NN_RS_01:17
0.00423728813559322 0.819694870502 0.562932399896

./circuits2//b09_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.413214285714 AVG_SIG:0.337852903702 N_RS_20:92 NN_RS_20:50 LEN:93 NI:29 N_RS_01:68 NN_RS_01:1
0.010752688172043012 0.833697292591 0.548535826141

./circuits2//b09_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.458571428571 AVG_SIG:0.357394494743 N_RS_20:92 NN_RS_20:39 LEN:84 NI:29 N_RS_01:62 NN_RS_01:2
0.011904761904761904 0.833332253129 0.572518756141

./circuits2//b10_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.524705882353 AVG_SIG:0.339917634663 N_RS_20:128 NN_RS_20:68 LEN:113 NI:28 N_RS_01:65 NN_RS_01:4
0.008849557522123894 0.834596460621 0.554079114819

./circuits2//b10_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.59 AVG_SIG:0.35504466509 N_RS_20:108 NN_RS_20:63 LEN:105 NI:28 N_RS_01:51 NN_RS_01:5
0.009523809523809525 0.831392396041 0.537043239038

./circuits2//b11_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.574193548387 AVG_SIG:0.34528359978 N_RS_20:352 NN_RS_20:186 LEN:330 NI:38 N_RS_01:229 NN_RS_01:20
0.0030303030303030303 0.829697965158 0.548145890022

./circuits2//b13_opt_C.bench.in
TODO:: I am considering all the signals (new ones included!)
AVG_HD:0.487547169811 AVG_SIG:0.383890086207 N_RS_20:141 NN_RS_20:75 LEN:162 NI:62 N_RS_01:22 NN_RS_01:1
0.006172839506172839 0.850982637712 0.579215939292



### NOT WORKING:

./circuits2//b04_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 204, in main
    base_circuit = Circuit(file_circuit)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 16, in __init__
    self.__parse_circuit_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 116, in __parse_circuit_file
    self.__get_gates_from_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 151, in __get_gates_from_file
    data_fields.append(int(data[j]))
ValueError: invalid literal for int() with base 10: 'GTE_67_6'

./circuits2//b05_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 204, in main
    base_circuit = Circuit(file_circuit)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 16, in __init__
    self.__parse_circuit_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 116, in __parse_circuit_file
    self.__get_gates_from_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 151, in __get_gates_from_file
    data_fields.append(int(data[j]))
ValueError: invalid literal for int() with base 10: 'GT_138_8'

./circuits2//b06_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 209, in main
    base_circuit_outputs = get_cricuit_output(base_circuit)
  File "evaluator.py", line 103, in get_cricuit_output
    outputs = circuit.get_cricuit_output()
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 105, in get_cricuit_output
    input_ids.add(int(input))
ValueError: invalid literal for int() with base 10: 'CONT_I0'

./circuits2//b06_opt_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 209, in main
    base_circuit_outputs = get_cricuit_output(base_circuit)
  File "evaluator.py", line 103, in get_cricuit_output
    outputs = circuit.get_cricuit_output()
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 105, in get_cricuit_output
    input_ids.add(int(input))
ValueError: invalid literal for int() with base 10: 'CONT_I0'

./circuits2//b07_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 204, in main
    base_circuit = Circuit(file_circuit)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 16, in __init__
    self.__parse_circuit_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 116, in __parse_circuit_file
    self.__get_gates_from_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 151, in __get_gates_from_file
    data_fields.append(int(data[j]))
ValueError: invalid literal for int() with base 10: 'R182_4'


./circuits2//b08_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 209, in main
    base_circuit_outputs = get_cricuit_output(base_circuit)
  File "evaluator.py", line 103, in get_cricuit_output
    outputs = circuit.get_cricuit_output()
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 105, in get_cricuit_output
    input_ids.add(int(input))
ValueError: invalid literal for int() with base 10: 'STATI0'

./circuits2//b08_opt_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 209, in main
    base_circuit_outputs = get_cricuit_output(base_circuit)
  File "evaluator.py", line 103, in get_cricuit_output
    outputs = circuit.get_cricuit_output()
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 105, in get_cricuit_output
    input_ids.add(int(input))
ValueError: invalid literal for int() with base 10: 'STATI0'

./circuits2//b11_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 204, in main
    base_circuit = Circuit(file_circuit)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 16, in __init__
    self.__parse_circuit_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 116, in __parse_circuit_file
    self.__get_gates_from_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 151, in __get_gates_from_file
    data_fields.append(int(data[j]))
ValueError: invalid literal for int() with base 10: 'R229_4'

./circuits2//b12_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 204, in main
    base_circuit = Circuit(file_circuit)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 16, in __init__
    self.__parse_circuit_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 116, in __parse_circuit_file
    self.__get_gates_from_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 151, in __get_gates_from_file
    data_fields.append(int(data[j]))
ValueError: invalid literal for int() with base 10: 'R745_6'

./circuits2//b12_opt_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 209, in main
    base_circuit_outputs = get_cricuit_output(base_circuit)
  File "evaluator.py", line 103, in get_cricuit_output
    outputs = circuit.get_cricuit_output()
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 105, in get_cricuit_output
    input_ids.add(int(input))
ValueError: invalid literal for int() with base 10: 'NLOSI109'

./circuits2//b13_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 204, in main
    base_circuit = Circuit(file_circuit)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 16, in __init__
    self.__parse_circuit_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 116, in __parse_circuit_file
    self.__get_gates_from_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 151, in __get_gates_from_file
    data_fields.append(int(data[j]))
ValueError: invalid literal for int() with base 10: 'ADD_291_5'

./circuits2//b14_1_C.bench.in
Traceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 204, in main
    base_circuit = Circuit(file_circuit)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 16, in __init__
    self.__parse_circuit_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 116, in __parse_circuit_file
    self.__get_gates_from_file(file)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 151, in __get_gates_from_file
    data_fields.append(int(data[j]))
ValueError: invalid literal for int() with base 10: 'ADD_95_5'

./circuits2//b14_1_opt_C.bench.in
^CTraceback (most recent call last):
  File "evaluator.py", line 331, in <module>
    main();
  File "evaluator.py", line 245, in main
    new_evaluation = evaluate_circuit(combination_array, new_circuit)
  File "evaluator.py", line 129, in evaluate_circuit
    evaluation_output = circuit.get_output_for_combination("", input_combination_array)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 228, in get_output_for_combination
    gate_values = self.__calculate_outputs_for_combinations(combination)
  File "/Users/sonny/Desktop/eva_circuit_HW/__simulator/circuit.py", line 247, in __calculate_outputs_for_combinations
    if gate_values[self.gates_dicts[self.__gates[i].id]] != '':
KeyboardInterrupt

./circuits2//b14_C.bench.in
^CTraceback (most recent call last):
  File "evaluator.py", line 20, in <module>
    import numpy as np
  File "//anaconda/lib/python3.5/site-packages/numpy/__init__.py", line 184, in <module>
    from . import add_newdocs
  File "//anaconda/lib/python3.5/site-packages/numpy/add_newdocs.py", line 13, in <module>
    from numpy.lib import add_newdoc
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/__init__.py", line 8, in <module>
    from .type_check import *
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/type_check.py", line 11, in <module>
    import numpy.core.numeric as _nx
  File "//anaconda/lib/python3.5/site-packages/numpy/core/__init__.py", line 14, in <module>
    from . import multiarray
SystemError: initialization of multiarray raised unreported exception

./circuits2//b14_opt_C.bench.in
^CTraceback (most recent call last):
  File "evaluator.py", line 20, in <module>
    import numpy as np
  File "//anaconda/lib/python3.5/site-packages/numpy/__init__.py", line 184, in <module>
    from . import add_newdocs
  File "//anaconda/lib/python3.5/site-packages/numpy/add_newdocs.py", line 13, in <module>
    from numpy.lib import add_newdoc
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/__init__.py", line 8, in <module>
    from .type_check import *
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/type_check.py", line 11, in <module>
    import numpy.core.numeric as _nx
  File "//anaconda/lib/python3.5/site-packages/numpy/core/__init__.py", line 14, in <module>
    from . import multiarray
SystemError: initialization of multiarray raised unreported exception

./circuits2//b15_1_C.bench.in
^CTraceback (most recent call last):
  File "evaluator.py", line 20, in <module>
    import numpy as np
  File "//anaconda/lib/python3.5/site-packages/numpy/__init__.py", line 169, in <module>
    from numpy.__config__ import show as show_config
  File "<frozen importlib._bootstrap>", line 969, in _find_and_load
  File "<frozen importlib._bootstrap>", line 958, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 666, in _load_unlocked
  File "<frozen importlib._bootstrap>", line 583, in module_from_spec
  File "<frozen importlib._bootstrap>", line 36, in _new_module
KeyboardInterrupt

./circuits2//b15_1_opt_C.bench.in
^CTraceback (most recent call last):
  File "evaluator.py", line 20, in <module>
    import numpy as np
  File "//anaconda/lib/python3.5/site-packages/numpy/__init__.py", line 184, in <module>
    from . import add_newdocs
  File "//anaconda/lib/python3.5/site-packages/numpy/add_newdocs.py", line 13, in <module>
    from numpy.lib import add_newdoc
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/__init__.py", line 8, in <module>
    from .type_check import *
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/type_check.py", line 11, in <module>
    import numpy.core.numeric as _nx
  File "//anaconda/lib/python3.5/site-packages/numpy/core/__init__.py", line 14, in <module>
    from . import multiarray
SystemError: initialization of multiarray raised unreported exception

./circuits2//b15_C.bench.in
^CFailed to import the site module
Traceback (most recent call last):
  File "//anaconda/lib/python3.5/site.py", line 567, in <module>
    main()
  File "//anaconda/lib/python3.5/site.py", line 549, in main
    known_paths = addusersitepackages(known_paths)
  File "//anaconda/lib/python3.5/site.py", line 281, in addusersitepackages
    user_site = getusersitepackages()
  File "//anaconda/lib/python3.5/site.py", line 257, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "//anaconda/lib/python3.5/site.py", line 247, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "//anaconda/lib/python3.5/sysconfig.py", line 587, in get_config_var
    return get_config_vars().get(name)
  File "//anaconda/lib/python3.5/sysconfig.py", line 536, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "//anaconda/lib/python3.5/sysconfig.py", line 408, in _init_posix
    from _sysconfigdata import build_time_vars
  File "<frozen importlib._bootstrap>", line 969, in _find_and_load
  File "<frozen importlib._bootstrap>", line 958, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 673, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 661, in exec_module
  File "<frozen importlib._bootstrap_external>", line 757, in get_code
  File "<frozen importlib._bootstrap_external>", line 459, in _validate_bytecode_header
  File "<frozen importlib._bootstrap_external>", line 47, in _r_long
KeyboardInterrupt

./circuits2//b15_opt_C.bench.in
^CTraceback (most recent call last):
  File "evaluator.py", line 20, in <module>
    import numpy as np
  File "//anaconda/lib/python3.5/site-packages/numpy/__init__.py", line 184, in <module>
    from . import add_newdocs
  File "//anaconda/lib/python3.5/site-packages/numpy/add_newdocs.py", line 13, in <module>
    from numpy.lib import add_newdoc
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/__init__.py", line 8, in <module>
    from .type_check import *
  File "//anaconda/lib/python3.5/site-packages/numpy/lib/type_check.py", line 11, in <module>
    import numpy.core.numeric as _nx
  File "//anaconda/lib/python3.5/site-packages/numpy/core/__init__.py", line 14, in <module>
    from . import multiarray
SystemError: initialization of multiarray raised unreported exception
^C