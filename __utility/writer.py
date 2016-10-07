## Author: Andrea Marcelli
## This script is used to create patterns of bits to evaluate the ICs
## made recursive!

## USAGE:
## Length: the length of the string of bits to Generate
## Random Sate: exploit randomness or not
## Max Count: the maximum number of string generated
## File Output: the filename where to print the output

import sys
import random

if len(sys.argv) != 5:
    print("USAGE:: python3 writer length random_state max_count file_output")
    print("USAGE::example: python3 writer 4 True 10 file.out")
    sys.exit()

length = int(sys.argv[1])
if sys.argv[2].lower() == 'true':
    random_state = True
else:
    random_state = False
max_number = int(sys.argv[3])
file_output = sys.argv[4]

print("\nDEBUG:: length:{0} random_state:{1} max_number:{2} file_output:{3}\n\n".format(length, random_state, max_number, file_output))

with open(file_output, 'w+') as f:

    def recursive(step, array):
        global counter
        if step == length:
            if random_state == False or (random_state == True and random.randint(0, 1) == 1):
                counter = counter + 1
                print(array)
                f.write(str(array) + "\n")
                if (counter >= max_number):
                    return True
            return False

        array.append(0)
        if recursive(step+1, array) == True:
            return True
        array.pop()
        array.append(1)
        if recursive(step+1, array) == True:
            return True
        array.pop()


    array = []
    counter = 0
    recursive(0, array)
    print("\n\nDEBUG:: generated {0} strings of bits\n".format(counter))
