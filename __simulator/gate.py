## Author: Andrea Marcelli
## Copyright to Byron Phung

from itertools import *

class Gate(object):
    """Simulate logic gates.

    Keyword arguments:
    id    -- Block ID
    name  -- Block name
    type  -- Logic gate type
    input -- List of input names
    """
    def __init__(self, id, name, type, input, score, sorting):
        self.id = id
        self.name = name.upper()
        self.type = type.upper()
        self.input = input
        self.score = score
        self.sorting = sorting

    def logic_output(self, input):
        """Evaluate the output of the current gate based on its type.

        Keyword arguments:
        input -- Input value; could be a list (all) or a single int (NOT gate)
        """
        if self.type == "NOT":
            return self.__not(input)
        elif self.type == "OR":
            return self.__or(input)
        elif self.type == "AND":
            return self.__and(input)
        elif self.type == "XOR":
            return self.__xor(input)
        elif self.type == "NAND":
            return self.__not(self.__and(input))
        elif self.type == "NOR":
            return self.__not(self.__or(input))
        elif self.type == "XNOR":
            return self.__not(self.__xor(input))
        else:
            print("ERROR:: Invalid gate type (type = \"" + self.type + "\")")
            print("        Use a valid gate type (NOT, OR, AND, XOR, NAND, NOR, or XNOR).")
            return 0

    def output_probability(self, input):
        """Evaluate the output probability of the current gate based on its type.

        Keyword arguments:
        input -- Input value; could be a list (all) or a single int (NOT gate)

        Note:
        The probabilities are inteneded as the probabilities of the input being one
        """
        if self.type == "NOT":
            probab = self.__not_probability(input)
            # print("DEBUG:: probability: " + str(probab))
            return probab
        elif self.type == "OR":
            probab = self.__or_probability(input)
            # print("DEBUG:: probability: " + str(probab))
            return probab
        elif self.type == "AND":
            probab = self.__and_probability(input)
            # print("DEBUG:: probability: " + str(probab))
            return probab
        elif self.type == "XOR":
            probab = self.__xor_probability(input)
            # print("DEBUG:: probability: " + str(probab))
            return probab
        elif self.type == "NAND":
            probab = self.__not_probability(self.__and_probability(input))
            # print("DEBUG:: probability: " + str(probab))
            return probab
        elif self.type == "NOR":
            probab = self.__not_probability(self.__or_probability(input))
            # print("DEBUG:: probability: " + str(probab))
            return probab
        elif self.type == "XNOR":
            probab =  self.__not_probability(self.__xor_probability(input))
            # print("DEBUG:: probability: " + str(probab))
            return probab
        else:
            print("ERROR:: Invalid gate type (type = \"" + self.type + "\")")
            print("        Use a valid gate type (NOT, OR, AND, XOR, NAND, NOR, or XNOR).")
            return 0

    def truth_table(self, bit_size):
        """Print out the truth table of the logic gate.

        This is designed primarily for verifygateclass.py and debugging
        purposes to verify each logic implementation.

        Keyword arguments:
        bit_size -- Maximum number of bits to test
        """

        # If the gate is a NOT gate, then simply do a basic inverter test for
        # 2 inputs.
        if self.type == "NOT":
            print("I0 OUT")
            for i in range(2):
                print(str(i).rjust(2) + " ", end="")
                print(str(self.logic_output(i)).rjust(2))

        # Otherwise, generate a truth table with the specified bit size.
        else:
            # Create the table headers (I for input and OUT for output).
            for i in range(bit_size):
                print("I" + str(i) + " ", end="")
            print("OUT")

            # Generate 2^n bit combinations.
            combinations = list(product([0, 1], repeat=bit_size))

            # Generate the output for each bit combination.
            for combination in combinations:
                for bit in combination:
                    print(str(bit).rjust(2) + " ", end="")
                print(str(self.logic_output(combination)).rjust(2))

    def print_info(self):
        """Print the stored gate information.

        This is designed primarily for verifygateclass.py and debugging
        purposes to verify the accuracy of each logic implementation.

        Keyword arguments:
        <None>
        """
        print("Gate " + str(self.id))
        print("    * Name   : " + self.name)
        print("    * Type   : " + self.type)
        print("    * Inputs : " + str(self.input))

    def __not(self, input):
        """Perform a logic NOT on the input value.

        Keyword arguments:
        input -- Input value
        """
        final_input = None

        # If the input is a list, then take the first element.
        if type(input) is list:
            final_input = input[0]

        # Otherwise, take the input as is.
        else:
            final_input = input

        # If the input was still not assigned, then display an error.
        if final_input is None:
            print("ERROR:: Invalid input to NOT gate (input = \"" + input + "\"")

        # Otherwise, evaluate the NOT logic.
        else:
            # If input is logic 1, then return a logic 0.
            if final_input is 1:
                return 0

            # Otherwise, return a logic 1.
            else:
                return 1

    def __not_probability(self, input):
        """Calculate the probability of a logic NOT on the input value.

        Keyword arguments:
        input -- Input value
        """
        # if (len(input) > 1 ):
        #     raise Exception('not_prob input > 1 not supported')

        final_input = None

        # If the input is a list, then take the first element.
        if type(input) is list:
            final_input = input[0]

        # Otherwise, take the input as is.
        else:
            final_input = input

        # If the input was still not assigned, then display an error.
        if final_input is None:
            print("ERROR:: Invalid input to NOT gate (input = \"" + input + "\"")

        # The probabilty of logic not is the same of the input
        else:
            return final_input;

    def __and(self, input):
        """Perform a logic AND on all the input values.

        Keyword arguments:
        input -- List of input values
        """
        # If there is a logic 0 at any moment, then simply return a logic 0.
        for value in input:
            if value is 0:
                return 0

        # Otherwise, return 1 if no logic 0 is found.
        return 1

    def __and_probability(self, input):
        """Calculate the probability of a logic AND on all the input values.

        Keyword arguments:
        input -- List of input values
        """
        # if (len(input) > 2 ):
        #     raise Exception('and input > 2 not supported')

        final_value = 1

        # The probaility of logic and is the multiplication of the input
        # probabilties of being one (e.g. 0.5 * 0.5 = 0.25)
        for value in input:
            final_value *= float(value);

        return final_value

    def __or(self, input):
        """Perform a logic OR on all the input values.

        Keyword arguments:
        input -- List of input values
        """
        # If there is a logic 1 at any moment, then simply return a logic 1.
        for value in input:
            if value is 1:
                return 1

        # Otherwise, return 0 if no logic 1 is found.
        return 0

    def __or_probability(self, input):
        """Calculate the probbility of a logic OR on all the input values.

        Keyword arguments:
        input -- List of input values
        """

        # multiple inputs are supported!
        # if (len(input) > 2 ):
        #     print("DEBUG:: probability input: " + str(input))
        #     raise Exception('or_prob input > 2 not supported')

        # The probaility of logic or is the multiplication of the input
        # probabilties of being 0 (1 - prob_of_being_1) (e.g. (1-0.5) * (1-0.5) = 0.25)
        temp_value = 1

        for value in input:
            temp_value *= (1 - float(value))

        return 1 - temp_value

    def __xor(self, input):
        """Perform a logic XOR on all the input values.

        Keyword arguments:
        input -- List of input values
        """
        value = input[0]
        for i in range(1, len(input)):
            # If the stored value is the same as the current input, then set the
            # value to logic 0.
            if value is input[i]:
                value = 0

            # Otherwise, set the value to logic 1.
            else:
                value = 1

        # Return the calculated logic value.
        return value

    def __xor_probability(self, input):
        """Calculate the probability a logic XOR on all the input values.

        Keyword arguments:
        input -- List of input values
        """

        if (len(input) > 2 ):
            raise Exception('xor_prob input > 2 not supported')

        temp_value = 1
        final_value = 0
        for i in input:
            final_value += float(i)
            temp_value *= float(i)

        return final_value - 2 * temp_value
