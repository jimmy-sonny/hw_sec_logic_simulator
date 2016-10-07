## Evaluator for combinatorial logic circuits
## Author: Andrea Marcelli
#
##########################################
#  Note:
#
#  USAGE:: python3 evaluator input_ugp output_ugp circuit all_combinations [max_combinations]
#  USAGE::example: python3 evaluator.py input_ugp.txt output_ugp.txt circuits/c17.in True
#
#  New logic ports are added at the end of the gate list, with a high id (>8000).
#  New inputs (keys) are added at the end of input list, with high id (>7000).
# 


import sys
import time
import random
import os.path
import numpy as np
from gate import Gate # Logic gate simulation
from circuit import Circuit # Combinational logic simulation

def get_new_gate_length(ugp_input, circuit_length):
    new_gate_length = min(sum(np.clip(np.array(list(map(int, ugp_input))), 0, 1)), int(circuit_length/2))
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

def get_hamming(output_evaluation, base_evaluation, base_circuit_outputs, circuit):
    global circuit_outputs
    if len(circuit_outputs) == 0:
        for i in base_circuit_outputs:
            circuit_outputs.append(circuit.get_real_index(i))
    return sum([base_evaluation[i] ^ output_evaluation[i] for i in circuit_outputs])

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

def recursive(circuit, prefix_array, step, input_combination_array, length_of_combination, all_combinations, max_combinations, base_evaluation, base_circuit_outputs):
    global combination_counter
    global hamming_distances
    if step == length_of_combination:
        if all_combinations == True or (all_combinations == False and random.randint(0, 1) == 1):

            combination_counter += 1

            ## Evaluate the circuit
            combination_array = prefix_array[:]
            combination_array.extend(input_combination_array)
            #print(combination_array)
            output_evaluation = evaluate_circuit(combination_array, circuit)
            hd = get_hamming(output_evaluation, base_evaluation, base_circuit_outputs, circuit)
            # print("DEBUG:: hamming_distance: {0}".format(hd) + "\n")
            hamming_distances.append(hd)

            if (combination_counter >= max_combinations):
                return True
        return False

    input_combination_array.append(0)
    if recursive(circuit, prefix_array, step+1, input_combination_array, length_of_combination, all_combinations, max_combinations, base_evaluation, base_circuit_outputs) == True:
        return True
    input_combination_array.pop()
    input_combination_array.append(1)
    if recursive(circuit, prefix_array, step+1, input_combination_array, length_of_combination, all_combinations, max_combinations, base_evaluation, base_circuit_outputs) == True:
        return True
    input_combination_array.pop()


def main():
    global hamming_distances

    ## Parse command line arguments
    if len(sys.argv) < 5:
        print("ERROR:: number of arguments is incorrect")
        print("USAGE:: python3 evaluator input_ugp output_ugp circuit all_combinations [max_combinations]")
        print("USAGE::example: python3 evaluator.py input_ugp.txt output_ugp.txt circuits/c17.in True\n\n")
        sys.exit()

    file_ugp_input = sys.argv[1]
    file_ugp_output = sys.argv[2]
    file_circuit = sys.argv[3]

    if sys.argv[4].lower() == 'true':
        all_combinations = True
    else:
        all_combinations = False

    ## At most evaluate 1 million of combinations
    max_combinations = 1000000
    if len(sys.argv) >= 6:
        max_combinations = int(sys.argv[5])

    if all_combinations == False:
        if len(sys.argv) != 6:
            print("ERROR:: number of arguments is incorrect")
            print("USAGE:: python3 evaluator input_ugp output_ugp circuit all_combinations [max_combinations]")
            print("USAGE::example: python3 evaluator.py input_ugp.txt output_ugp.txt circuits/c17.in False 100\n\n")
            sys.exit()

    # print("DEBUG:: input_ugp:{0} output_ugp:{1} circuit{2}".format(file_ugp_input, file_ugp_output, file_circuit))
    # print("DEBUG:: all_combinations:{0}".format(all_combinations))
    # print("DEBUG:: max_combinations:{0}".format(max_combinations))

    ## Check if the file exists
    if os.path.isfile(file_ugp_input) and os.path.isfile(file_circuit):

        ## Read the circuit configuration from the input file
        with open(file_ugp_input, "r") as f_in:

            ## Create the BASE Circuit
            base_circuit = Circuit(file_circuit)
            # base_circuit.print_gates()
            # print()
            # print("TIME STEP1")

            ## Get circuit inputs and outputs
            base_circuit_input_length = get_circuit_input_length(base_circuit)
            base_circuit_gate_lenght = get_circuit_gate_length(base_circuit)
            base_circuit_outputs = get_cricuit_output(base_circuit)
            # print("TIME STEP2")

            ## Create a random combination and evaluate the BASE circuit:
            prefix_array = [random.randint(0,1) for i in range(base_circuit_input_length)]
            base_circuit_evaluation = evaluate_circuit(prefix_array, base_circuit)
            # print("TIME STEP3")

            ## GET altering string
            ugp_input = f_in.readline().split();

            ## Check correctness
            if check_correctness_alteratioin(ugp_input, base_circuit_gate_lenght) == False:
                print("ERROR:: uGP Input is not correct")
                sys.exit()
            # print("TIME STEP4")

            ## CREATE A NEW CIRCUIT.. THIS WILL BE MODIFIED
            new_circuit = Circuit(file_circuit)
            number_new_gates = alter_circuit(ugp_input, new_circuit)
            # new_circuit.print_gates()
            # print()
            # print("TIME STEP5")

            # Evaluate Hamming Distance
            recursive(new_circuit, prefix_array, 0, input_combination_array, number_new_gates, all_combinations, max_combinations, base_circuit_evaluation, base_circuit_outputs)
            # print("\nDEBUG:: generated {0} combinations of bits\n".format(combination_counter))
            hamming_distances = [i/len(base_circuit_outputs) for i in hamming_distances]
            exp_mean_new_hd = get_exp_mean(hamming_distances)
            mean_new_hd = get_mean(hamming_distances)
            # print("TIME STEP6")

            ## Evaluate the signal prob on BASE CIRCUIT
            base_probs = evaluate_signal_probabilities(base_circuit)
            number_rare_signals = get_number_rare_signals(base_probs)
            exp_mean_base_probs = get_exp_mean(base_probs)
            # print("TIME STEP7")

            ## Evaluate the signal probabilities of NEW CIRCUIT
            new_probs = evaluate_signal_probabilities(new_circuit)
            print("TODO:: I am considering all the signals (new ones included!)")
            # new_probs_cutted = new_probs[:-number_new_gates]
            new_probs_cutted = new_probs[:]
            exp_mean_new_probs_cutted = get_exp_mean(new_probs_cutted)
            number_new_rare_signals = get_number_rare_signals(new_probs_cutted)
            mean_new_probs_cutted = get_mean(new_probs_cutted)
            # print("TIME STEP8")

            ## New gates evaluation
            new_gate_length = get_new_gate_length(ugp_input, base_circuit_input_length)

            ## CALCULATE FITNESS
            first_fitness = get_safe_reverse(new_gate_length)
            second_fitness = get_safe_reverse(exp_mean_new_hd)
            third_fitness = get_safe_reverse(exp_mean_new_probs_cutted)

            ## SOME STATS
            # print("INFO:: first_fitness: " + str(first_fitness) + "\n")

            # print("DEBUG:: hamming_distances: " + str(hamming_distances))
            # print("INFO:: exponential mean: " + str(exp_mean_new_hd)+ "\n")

            # print("INFO:: second_fitness: " + str(second_fitness) + "\n")

            # print("DEBUG:: base output probabilities: " + str(base_probs))
            # print("DEBUG:: new output probabilities: " + str(new_probs_cutted))
            # print("DEBUG:: base exponential mean: " + str(exp_mean_base_probs))
            # print("DEBUG:: new exponential mean probabilites: " + str(exp_mean_new_probs_cutted)+ "\n")

            # print("INFO:: third_fitness: " + str(third_fitness) + "\n")

            print(str(new_gate_length) + " AVG_HD:" + str(mean_new_hd) + " AVG_SIG:" + str(mean_new_probs_cutted) + " N_RS:" + str(number_rare_signals) + " NN_RS:" + str(number_new_rare_signals))
            print(str(first_fitness) + " " + str(second_fitness) + " " + str(third_fitness))

            ## Write the fitness to the output file
            with open(file_ugp_output, "w") as f_out:
                f_out.write(str(first_fitness) + " " + str(second_fitness) + " " + str(third_fitness) + "\n");

    # Otherwise, display an error.
    else:
        print("ERROR:: Cannot find file at path \"" + file_ugp_input + "\"")
        sys.exit()

## Call main function
circuit_outputs = [] # cache
input_combination_array = []
hamming_distances = []
combination_counter = 0

starttime = time.time()
main();
print("TIME REQ : " +str(time.time() - starttime))
