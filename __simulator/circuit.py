## Author Andrea Marcelli
## Copyright to Byron Phung

import time
from itertools import *
from gate import Gate   # Logic gate simulation
from system import *

class Circuit(object):
    """Simulate combinational logic circuits.

    Keyword arguments:
    file -- Circuit file to read
    """
    def __init__(self, file):
        self.__parse_circuit_file(file)

    def get_input_counter(self):
        return self.inputs_dicts_counter+1

    def check_logic_modifier_string(self, array):
        if len(array) != inputs_dicts_counter+1:
            return False
        counter = 0;
        for i in array:
            if i != 0 and i!= 1 and i!=2:
                return False
            if i != 0:
                counter=counter+1
        if counter > (inputs_dicts_counter+1/2):
            return False
        return True

    def __find_available_gate_number(self, currentid):
        return currentid+7000

    def modify_circuit(self, array):
        """
        - controllare il tipo di porta per 1 e 2
        """
        counter_insertion = 0

        for i in range(len(array)):
            # print("array[i]: "+ array[i])
            if int(array[i]) != 0:

                # This is the maximum gate id, increment and use it to assign a new id
                gate_number = self.__find_available_gate_number(i)

                # The inputs for the new gate are the key and the output of the preeciding
                new_gate_inputs = ["I{0}".format(self.key_counter)]

                self.inputs_dicts[self.key_counter] = self.inputs_dicts_counter
                self.inputs_dicts_counter = self.inputs_dicts_counter+1

                # Add a new gate
                new_gate_inputs.append(str(self.__gates[i].id))
                # Increment the key number for indexing
                self.key_counter += 1

                # print("DEBUG:: new gate inputs: " + str(new_gate_inputs))

                # Sostituisci tutti i riferimenti al vecchio id con il nuovo
                for this_gate in self.__gates:
                    for input_index in range(len(this_gate.input)):
                        #print("DEBUG: comapare {0} with {1}".format(this_gate.input[input_index], self.__gates[i].id))
                        if this_gate.input[input_index] == str(self.__gates[i].id):
                            old_input = this_gate.input[input_index]
                            this_gate.input[input_index] = str(gate_number)
                            # print("DEBUG:: in {0} sostituito {1} con {2}".format(this_gate.name, old_input, this_gate.input[input_index]))

                if int(array[i]) == 1:
                    # print("DEBUG:: adding port type 1")
                    # Aggiungo il nuovo gate : # id, name, type, input, score, sorting
                    self.__gates.append(Gate(gate_number, "type1_"+str(gate_number), "xor", new_gate_inputs, 1, self.__gates[i].id+1))
                    counter_insertion+=1

                if int(array[i]) == 2:
                    # print("DEBUG:: adding port type 2")
                    # Aggiungo il nuovo gate : # id, name, type, input, score, sorting
                    self.__gates.append(Gate(gate_number, "type2_"+str(gate_number), "xnor", new_gate_inputs, 1, self.__gates[i].id+1))
                    counter_insertion+=1

                self.gates_dicts[gate_number] = self.gates_dicts_counter
                self.gates_dicts_counter = self.gates_dicts_counter +1

        self.__gates.sort(key = lambda x: x.sorting)
        return counter_insertion


    def get_real_index(self, index):
        return self.gates_dicts[index]


    def get_circuit_gate_length(self):
        return len(self.__gates)


    def get_cricuit_output(self):
        ids = set(self.gates_dicts.keys())
        input_ids = set([])
        for gate in self.__gates:
            for input in gate.input:
                if not input.startswith("I"):
                    input_ids.add(int(input))
        output_ids = ids.difference(input_ids)
        return output_ids


    def __parse_circuit_file(self, file):
        """Parse the circuit file.

        Keyword arguments:
        file -- Circuit file to read
        """
        self.__get_gates_from_file(file)
        self.__gates.sort(key = lambda x: x.id)
        # print("DEBUG:: circuit input map: " + str(self.inputs_dicts))
        # print("DEBUG:: circuit gate map: " + str(self.gates_dicts) + "\n")


    def __get_gates_from_file(self, file):
        """Get all the gates from the circuit file and store it in the circuit.

        Keyword arguments:
        file -- Circuit file to read
        """
        # Initialize a private list to hold logic gates.
        self.__gates = []
        self.inputs_dicts = {}
        self.inputs_dicts_counter = 0
        self.gates_dicts = {}
        self.gates_dicts_counter = 0
        self.key_counter = 8000

        # Read the .in file and get each line.
        file_content = read_file(file)
        file_content_lines = file_content.splitlines()

        # Parse each line for gate information.
        for i in range(len(file_content_lines)):
            # Get the gate information separated by whitespaces.
            data = file_content_lines[i].split()
            data_fields = []
            gate_inputs = []

            # Temporarily store each data field.
            for j in range(len(data)):
                # If j is 0, then store an int for the gate ID.
                if j == 0:
                    data_fields.append(int(data[j]))

                # Else if j is greater than 2, then store the gate inputs.
                elif j > 2:
                    gate_inputs.append(data[j].upper())

                # Otherwise, simply store either the name or type.
                else:
                    data_fields.append(data[j].upper())

            # Merge the gate inputs into the data fields list.
            data_fields.append(gate_inputs)

            score = 2
            for gate_input in gate_inputs:
                if gate_input.startswith("I"):
                    score -= 1
                    gate_input_row = self.__get_int_of_general_value(gate_input)
                    if gate_input_row not in self.inputs_dicts:
                        self.inputs_dicts[gate_input_row] = self.inputs_dicts_counter
                        self.inputs_dicts_counter = self.inputs_dicts_counter+1
            self.gates_dicts[data_fields[0]] = self.gates_dicts_counter
            self.gates_dicts_counter = self.gates_dicts_counter +1

            # Add the score to the data_fields
            data_fields.append(score)

            # Create a new Gate object and store it.
            # id, name, type, input, score, sorting
            self.__gates.append(Gate(data_fields[0], data_fields[1], data_fields[2], data_fields[3], data_fields[4], data_fields[0]))

    def print_gates(self):
        """Print the gates in the current circuit sorted by ID.

        Keyword arguments:
        <None>
        """
        # Print the table headers and a border.
        print("ID    Name    Type    Inputs")
        print("-" * 80)

        # Print each gate.
        for gate in self.__gates:
            # Print the gate's ID, name, and type.
            print(str(gate.id).ljust(2) + " " * 4 + gate.name.ljust(12)
                  + gate.type.ljust(4) + " " * 4, end="")

            # Print the gate's inputs.
            for input in gate.input:
                print(input.ljust(2) + "  ", end="")
            print()


    def get_output_for_combination(self, selected_outputs, combination):
        """Print the output of the circuit with the selected outputs
        (if applicable) and for the specified combination.

        Keyword arguments:
        selected_outputs -- List of selected outputs
        selected_outputs -- List of input combination
        """
        # Get the number of general input values.
        num_general_values = self.__get_num_of_general_input_values()

        # Print the truth table headers.
        #self.__print_truth_table_headers(num_general_values, selected_outputs)

        # Check the combination input.
        if (len(combination) != num_general_values):
            raise Exception('combination input is wrong')
        for i in combination:
            if (int(i) != 1 and int(i) != 0):
                print (i)
                raise Exception('combination input is wrong')

        # Calculate the values of each gate and print the outputs of the
        # selected gates (if applicable) in the truth table.
        gate_values = self.__calculate_outputs_for_combinations(combination)
        return gate_values


    def __calculate_outputs_for_combinations(self, combination):
        """Calculate the outputs for the current bit combination.

        Keyword arguments:
        combination -- Current bit combination
        """
        # Create and initialize an empty list of gate values.
        gate_values = [''] * len(self.__gates)

        # While all the gate values are not found, determine the gate values.
        while not self.__are_all_gate_values_found(gate_values):
            # Parse each gate value.
            for i in range(len(self.__gates)):

                # If the gate value has already been determined, then skip the current iteration.
                if gate_values[self.gates_dicts[self.__gates[i].id]] != '':
                    continue

                # If all the required inputs for the current gate are available, then calculate the gate value.
                if self.__are_all_required_inputs_available(self.__gates[i], gate_values):

                    # Get the int input values for the current gate.
                    inputs = []
                    for input in self.__gates[i].input:
                        if input.startswith("I"):
                            inputs.append(combination[self.inputs_dicts[self.__get_int_of_general_value(input)]])
                        else:
                            inputs.append(gate_values[self.gates_dicts[int(input)]])

                    # Assign the gate value to the current index of the list of block values.
                    gate_values[self.gates_dicts[self.__gates[i].id]] = self.__gates[i].logic_output(inputs)

        # Return the combinatorial output for the circuit
        return gate_values


    def get_output_probabilities(self):
            """Print the probabilities of the selected outputs (if applicable).

            If no outputs are selected, then all gate probabilities will be printed.

            Keyword arguments:
            selected_outputs -- List of selected outputs
            """
            # Get the number of input values.
            num_input_values = self.__get_num_of_general_input_values()

            input_probabilities = ['0.5'] * num_input_values
            # print ("DEBUG:: input_probabilities " + str(input_probabilities))

            gate_probabilities = self.__calculate_output_probabilities(input_probabilities)
            return gate_probabilities


    def __calculate_output_probabilities(self, input_probabilities):
        """Calculate the outputs probabilities for each gate.

        Keyword arguments:
        input_probabilities -- Probability in input to the circuit
        """
        # Create and initialize an empty list of gate values.
        gate_values = [''] * len(self.__gates)

        # While all the gate values are not found, determine the gate values.
        while not self.__are_all_gate_values_found(gate_values):
            for i in range(len(self.__gates)):

                # If the gate value has already been determined, then skip the current iteration.
                if gate_values[self.gates_dicts[self.__gates[i].id]] != '':
                    continue

                # Check if the required inputs for the current gate are available
                if self.__are_all_required_inputs_available(self.__gates[i], gate_values):

                    # Get the int input values for the current gate.
                    inputs = []
                    for input in self.__gates[i].input:
                        if input.startswith("I"):
                            inputs.append(input_probabilities[self.inputs_dicts[self.__get_int_of_general_value(input)]])
                        else:
                            inputs.append(gate_values[self.gates_dicts[int(input)]])

                        # print("DEBUG:: GATE: {0} inputs: {1}".format(self.__gates[i].name, str(inputs)))

                    # Assign the gate value to the current index of the list of block values.
                    gate_values[self.gates_dicts[self.__gates[i].id]] = self.__gates[i].output_probability(inputs)

        # Return the calculated gate values.
        return gate_values


    def __print_gate_outputs(self, combination, selected_outputs, gate_values):
        """Print the outputs of the selected gates in the truth table.

        Keyword arguments:
        selected_outputs -- List of selected outputs
        gate_values      -- List of values for each gate
        """
        # Print the current general input combination.
        for bit in combination:
            print(str(bit).ljust(2) + " " * 4, end="")

        # If outputs were selected, then only print the values for those
        # outputs.
        if len(selected_outputs) > 0:
            for output in selected_outputs:
                print(str(gate_values[int(output)]).ljust(8), end="")

        # Otherwise, print values for all outputs.
        else:
            for gate in self.__gates:
                # old
                # print(str(gate_values[gate.id]).ljust(8), end="")
                # new one
                print(str(gate_values[self.gates_dicts[gate.id]]).ljust(8), end="")
        print()

    def get_inputs_number(self):
        return self.__get_num_of_general_input_values()

    def __get_num_of_general_input_values(self):
        """Get the number of general input values.

        Keyword arguments:
        <None>
        """
        # Track the number of general input values.
        num_general_values = 0

        #new
        general_values = []

        # Parse each gate to determine the maximum number of general input
        # values.
        for gate in self.__gates:
            # Parse each gate input.
            for input in gate.input:
                # If the current input starts with an I, then get its general
                # position.
                if input.startswith("I"):
                    # Get only the integer value of the general input value.
                    general_value = self.__get_int_of_general_value(input)

                    #new
                    inserisco = True
                    for i in general_values:
                        if i == general_value:
                            inserisco = False
                    if inserisco == True:
                        general_values.append(general_value)


                    # If its general position is greater than the current stored
                    # number of general values, then store that position.
                    #old
                    # if general_value + 1 > num_general_values:
                    #     num_general_values = general_value + 1

        # Return the number of general input values.
        return len(general_values)

    def __get_int_of_general_value(self, general_value):
        """Get the integer component of the general value formatted I0, I1, etc.

        Keyword arguments:
        general_value -- General value formatted I0, I1, etc.
        """
        general_values = general_value.split("I")
        return int(general_values[1])

    def __are_all_gate_values_found(self, gate_values):
        """Check if all the gate values are found.

        This is using a developer-chosen definition of empty being ''.

        Keyword arguments:
        gate_values -- List of gate values
        """
        # Return False if any gate values are empty.
        for value in gate_values:
            if value == '':
                return False

        # Otherwise, return True.
        return True

    def __are_all_required_inputs_available(self, gate, gate_values):
        """Check if all the required inputs for the current gate are available.

        Keyword arguments:
        gate        -- Current logic gate
        combination -- List of general input values
        gate_values -- List of gate values
        """
        # Return False if any required gate values are empty.
        for input in gate.input:
            if not input.startswith("I"):
                if gate_values[self.gates_dicts[int(input)]] == '':
                    return False

        # Otherwise, return True.
        return True
