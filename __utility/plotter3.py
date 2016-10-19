import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

if len(sys.argv) != 5:
    print("The number of supplied arguments is wrong")
    sys.exit(1)
else:
    print("## I will use this data file: " + str(sys.argv[1]))
    print("## I will plot a graph with this name: " + str(sys.argv[2]) + " " + str(sys.argv[3]) + " " + str(sys.argv[4]))

def getColumn(filename, column, delimiter_input):
    results = csv.reader(open(filename), delimiter=delimiter_input)
    return [result[column] for result in results]

try:
    hda = getColumn(sys.argv[1], 0, " ")
    sa = getColumn(sys.argv[1], 1, " ")
    rs = getColumn(sys.argv[1], 2, " ")
    length = getColumn(sys.argv[1], 3, " ")

    plt.xlabel("Length")
    plt.ylabel("Avg HD")

    plt.plot(length, hda, 'g.')
    plt.savefig(sys.argv[2])

    plt.clf()

    plt.xlabel("Length")
    plt.ylabel("Avg Signal Probability")

    plt.plot(length, sa, 'r.')
    plt.savefig(sys.argv[3])

    plt.clf()

    plt.xlabel("Length")
    plt.ylabel("Number of Rare Signal")

    plt.plot(length, rs, 'r.')
    plt.savefig(sys.argv[4])

    sys.exit(0)
except Exception as e:
    print("Sorry, something went wrong! (Maybe input files does not exist)")
    print(e)
    sys.exit(1)
