## Evaluator for combinatorial logic circuits
## Author: Andrea Marcelli
#
##########################################
#  Note:
#
#  New logic ports are added at the end of the gate list, with a high id (>8000).
#  New inputs (keys) are added at the end of input list, with high id (>7000).
#
#  Useful commands:
#  ./__utility/utils_0_1.sh 41 100 > circuits/prefix_c499_100.txt
#  python3 evaluator.py ./circuits/input_ugp_c499.txt output_ugp.txt ./circuits/c499.in ./circuits/prefix_c499_10.txt False 10
#  python3 evaluator.py ./circuits/input_ugp_c17.txt output_ugp.txt ./circuits/c17.in ./circuits/prefix_c17.txt True
#  python3 evaluator.py ./circuits/input_ugp_c2670.txt output_ugp.txt ./circuits/c2670.in ./circuits/prefix_c2670_10.txt False 1

import sys
import time
import random
import os.path
import numpy as np
from gate import Gate # Logic gate simulation
from circuit import Circuit # Combinational logic simulation


def get_new_gate_length(ugp_input, circuit_length):
    new_gate_length = sum(np.clip(np.array(list(map(int, ugp_input))), 0, 1))
    return new_gate_length


def get_number_rare_signals(probabilities):
    number_rare_signals = 0
    for i in probabilities:
        if float(i) < 0.01 or float(i) > 0.99:
            number_rare_signals+=1
    return number_rare_signals


def check_correctness_alteratioin(ugp_input, circuit_length):
    correctness = True
    if len(ugp_input) != circuit_length:
        correctness = False
        print ("DEBUG:: it should be {1}, but is {0}".format(len(ugp_input), circuit_length) +"\n")
    return correctness


def get_safe_reverse(input):
    if input == 0:
        output = 999999999
    else:
        output = 1/input
    return output


def get_output_from_evaluation(circuit, base_circuit_outputs, evaluation):
    global circuit_outputs
    if len(circuit_outputs) == 0:
        for i in base_circuit_outputs:
            circuit_outputs.append(circuit.get_real_index(i))

    result = [evaluation[i] for i in circuit_outputs]
    return result


def get_hamming(new_evaluation, base_evaluation, base_circuit_outputs, circuit):

    base_evaluation_filtered = get_output_from_evaluation(circuit, base_circuit_outputs, base_evaluation)
    new_evaluation_filtered = get_output_from_evaluation(circuit, base_circuit_outputs, new_evaluation)

    if (len(base_evaluation_filtered) != len(base_circuit_outputs)) or (len(new_evaluation_filtered) != len(base_circuit_outputs)):
        print("ERROR: something bad happened!")
        sys.exit()
    result = [base_evaluation_filtered[i] ^ new_evaluation_filtered[i] for i in range(len(base_evaluation_filtered))]
    return sum(result)


def get_mean(array):
    # Non c'è la sottrazione di 0.5 perchè mi interessa solo la media
    exp_mean = np.mean(np.asarray(array, dtype=float))
    return exp_mean


def get_exp_mean(array):
    # Devo sottrarre 0.5 perchè cerco di minimizzare la distanza da 0.5
    exp_mean = np.mean(np.exp(np.absolute(np.asarray(array, dtype=float)-0.5)))
    return exp_mean


def get_dev_std(array):
    std = np.std(np.array(array))
    return std


def get_circuit_gate_length(circuit):
    gate_length = circuit.get_circuit_gate_length()
    # print ("INFO:: Get circuit gate_length: " + str(gate_length) + "\n")
    return gate_length


def get_cricuit_output(circuit):
    outputs = circuit.get_cricuit_output()
    # print ("INFO:: Get circuit outputs: " + str(outputs) + "\n")
    return outputs


def get_circuit_input_length(circuit):
    inputs_number = circuit.get_inputs_number()
    # print ("INFO:: Num of inputs: " + str(inputs_number) + "\n")
    return inputs_number


def alter_circuit(ugp_input, circuit):
    # print ("DEBUG:: Altering string: {0}".format(ugp_input))
    number_new_gates = circuit.modify_circuit(ugp_input)
    # print ("INFO:: Inserted {0} new gates\n".format(number_new_gates))
    return number_new_gates


def evaluate_signal_probabilities(circuit):
    # print ("INFO:: Evaluating signal probabilities")
    probs = circuit.get_output_probabilities()
    return probs


def evaluate_circuit(input_combination_array, circuit):
    # print("DEBUG:: input  {0}".format(str(input_combination_array)))
    evaluation_output = circuit.get_output_for_combination("", input_combination_array)
    # print("DEBUG:: output {0}".format(str(evaluation_output)))
    return evaluation_output


def recursive(circuit, prefix_array, step, input_combination_array, length_of_combination, all_combinations, base_evaluation, base_circuit_outputs):
    global hamming_distances
    if step == length_of_combination:
        if all_combinations == True or (all_combinations == False and random.randint(0, 1) == 1):

            ## Evaluate the circuit
            combination_array = prefix_array[:]
            combination_array.extend(input_combination_array)
            new_evaluation = evaluate_circuit(combination_array, circuit)
            hd = get_hamming(new_evaluation, base_evaluation, base_circuit_outputs, circuit)
            hamming_distances.append(hd)
        return

    input_combination_array.append(0)
    recursive(circuit, prefix_array, step+1, input_combination_array, length_of_combination, all_combinations, base_evaluation, base_circuit_outputs)
    input_combination_array.pop()
    input_combination_array.append(1)
    recursive(circuit, prefix_array, step+1, input_combination_array, length_of_combination, all_combinations, base_evaluation, base_circuit_outputs)
    input_combination_array.pop()


def main():
    global hamming_distances

    ## Parse command line arguments
    if len(sys.argv) < 5:
        print("ERROR:: number of arguments is incorrect")
        print("USAGE:: python3 evaluator input_ugp output_ugp circuit prefix_combination all_combinations [max_combinations]")
        print("USAGE::example: python3 evaluator.py input_ugp.txt output_ugp.txt circuits/c17.in c17_comb.txt True\n\n")
        sys.exit()

    file_ugp_input = sys.argv[1]
    file_ugp_output = sys.argv[2]
    file_circuit = sys.argv[3]
    file_prefix_combination = sys.argv[4]

    if sys.argv[5].lower() == 'true':
        all_combinations = True
    else:
        all_combinations = False

    ## At most evaluate 1 thousands of combinations
    max_combinations = 1000
    if len(sys.argv) >= 7:
        max_combinations = int(sys.argv[6])

    if all_combinations == False:
        if len(sys.argv) != 7:
            print("ERROR:: number of arguments is incorrect")
            print("USAGE:: python3 evaluator input_ugp output_ugp circuit prefix_combination all_combinations [max_combinations]")
            print("USAGE::example: python3 evaluator.py input_ugp.txt output_ugp.txt circuits/c17.in c17_comb.txt False 100\n\n")
            sys.exit()

    # print("DEBUG:: input_ugp:{0} output_ugp:{1} circuit{2} file_prefix_combination:{3}".format(file_ugp_input, file_ugp_output, file_circuit, file_prefix_combination))
    # print("DEBUG:: all_combinations:{0}".format(all_combinations))
    # print("DEBUG:: max_combinations:{0}".format(max_combinations))

    ## Check if the file exists
    if os.path.isfile(file_ugp_input) and os.path.isfile(file_circuit) and os.path.isfile(file_prefix_combination):

        ## Read the circuit configuration from the input file
        with open(file_prefix_combination, "r") as prefix_in:

            ## Read the circuit configuration from the input file
            with open(file_ugp_input, "r") as f_in:

                ## Create the BASE Circuit
                base_circuit = Circuit(file_circuit)

                ## Get circuit inputs and outputs
                base_circuit_input_length = get_circuit_input_length(base_circuit)
                base_circuit_gate_lenght = get_circuit_gate_length(base_circuit)
                base_circuit_outputs = get_cricuit_output(base_circuit)

                ## GET altering string
                ugp_input = f_in.readline().split();

                ## Check correctness
                if check_correctness_alteratioin(ugp_input, base_circuit_gate_lenght) == False:
                    print("ERROR:: uGP Input is not correct")
                    sys.exit()

                ## CREATE A NEW CIRCUIT.. THIS WILL BE MODIFIED
                new_circuit = Circuit(file_circuit)
                number_new_gates = alter_circuit(ugp_input, new_circuit)

                ## Evaluate the hamming distance
                exp_mean_hds_array = []
                mean_hds_array = []

                for prefix in prefix_in.readlines():
                    prefix_array = prefix.split()

                    if len(prefix_array) != base_circuit_input_length:
                        print("ERROR:: length is: " + str(len(prefix_array)) + " but should be " + str(base_circuit_input_length))
                        sys.exit()

                    # s = time.time()
                    base_circuit_evaluation = evaluate_circuit(prefix_array, base_circuit)
                    # print(time.time() -s)

                    if all_combinations == True:
                        recursive(new_circuit, prefix_array, 0, input_combination_array, number_new_gates, all_combinations, base_circuit_evaluation, base_circuit_outputs)
                    else:
                        s = time.time()
                        for i in range(max_combinations):
                            combination_array = prefix_array[:]
                            combination_array.extend([random.randint(0,1) for i in range(number_new_gates)])
                            new_evaluation = evaluate_circuit(combination_array, new_circuit)
                            hd = get_hamming(new_evaluation, base_circuit_evaluation, base_circuit_outputs, new_circuit)
                            hamming_distances.append(hd)
                        print(time.time() -s)
                        print()

                    hamming_distances = [i/len(base_circuit_outputs) for i in hamming_distances]
                    exp_mean_hd = get_exp_mean(hamming_distances)
                    exp_mean_hds_array.append(exp_mean_hd)

                    mean_hd = get_mean(hamming_distances)
                    mean_hds_array.append(mean_hd)
                    hamming_distances.clear()
                    input_combination_array.clear()

                exp_mean_hds = get_exp_mean(exp_mean_hds_array)
                mean_hds = get_mean(mean_hds_array)

                ## Evaluate the signal prob on BASE CIRCUIT
                base_probs = evaluate_signal_probabilities(base_circuit)
                number_rare_signals = get_number_rare_signals(base_probs)
                exp_mean_base_probs = get_exp_mean(base_probs)

                ## Evaluate the signal probabilities of NEW CIRCUIT
                new_probs = evaluate_signal_probabilities(new_circuit)
                print("TODO:: I am considering all the signals (new ones included!)")
                # new_probs_cutted = new_probs[:-number_new_gates]
                new_probs_cutted = new_probs[:]
                exp_mean_new_probs_cutted = get_exp_mean(new_probs_cutted)
                number_new_rare_signals = get_number_rare_signals(new_probs_cutted)
                mean_new_probs_cutted = get_mean(new_probs_cutted)

                ## New gates evaluation
                new_gate_length = get_new_gate_length(ugp_input, base_circuit_input_length)

                ## CALCULATE FITNESS
                first_fitness = get_safe_reverse(exp_mean_hds)
                second_fitness = get_safe_reverse(exp_mean_new_probs_cutted)
                third_fitness = get_safe_reverse(new_gate_length)

                ## SOME STATS & DEBUG
                # print("INFO:: HD mean: " + str(mean_hds)+ "\n")
                # print("INFO:: HD exponential mean: " + str(exp_mean_hds)+ "\n")

                # print("DEBUG:: Signals base probabilities: " + str(base_probs))
                # print("DEBUG:: Signals new probabilities: " + str(new_probs_cutted))
                # print("DEBUG:: Signals base exp mean: " + str(exp_mean_base_probs))
                # print("DEBUG:: Signals new exp mean prob: " + str(exp_mean_new_probs_cutted)+ "\n")

                # print("INFO:: first_fitness: " + str(first_fitness) + "\n")
                # print("INFO:: second_fitness: " + str(second_fitness) + "\n")
                # print("INFO:: third_fitness: " + str(third_fitness) + "\n")

                print("AVG_HD:" + str(mean_hds) + " AVG_SIG:" + str(mean_new_probs_cutted) + " N_RS:" +
                            str(number_rare_signals) + " NN_RS:" + str(number_new_rare_signals) + " LEN:" +
                            str(new_gate_length) + " NI:" + str(base_circuit_input_length))
                print(str(first_fitness) + " " + str(second_fitness) + " " + str(third_fitness))

                ## Write the fitness to the output file
                with open(file_ugp_output, "w") as f_out:
                    f_out.write(str(first_fitness) + " " + str(second_fitness) + " " + str(third_fitness) + "\n");

    # Otherwise, display an error.
    else:
        print("ERROR:: Cannot find file at the specified path")
        sys.exit()

## Call main function
circuit_outputs = [] # cache
input_combination_array = []
hamming_distances = []

# starttime = time.time()
main();
# print("TIME REQ : " +str(time.time() - starttime))
