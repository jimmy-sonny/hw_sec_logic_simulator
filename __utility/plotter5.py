import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

if len(sys.argv) != 9:
    print("The number of supplied arguments is wrong")
    sys.exit(1)
else:
    print("## I will use this data file: " + str(sys.argv[1]) + " " + str(sys.argv[2]) + " " + str(sys.argv[3]) + " " + str(sys.argv[4]))
    print("## I will plot a graph with this name: " + str(sys.argv[5]) + " " + str(sys.argv[6]) + " " + str(sys.argv[7]) + " " + str(sys.argv[8]))

def getColumn(filename, column, delimiter_input):
    results = csv.reader(open(filename), delimiter=delimiter_input)
    return [result[column] for result in results]

try:

    data = getColumn(sys.argv[1], 0, " ")
    length = getColumn(sys.argv[1], 1, " ")
    plt.xlabel("Key length")
    plt.ylabel("ABS AVG HD")
#    plt.scatter(length, data)
    plt.plot(length, data, 'g-')
    plt.savefig(sys.argv[5])
    plt.clf()

    data = getColumn(sys.argv[2], 0, " ")
    length = getColumn(sys.argv[2], 1, " ")
    plt.xlabel("Key length")
    plt.ylabel("ABS AVG signals probability")
    plt.plot(length, data, 'r-')
    plt.savefig(sys.argv[6])
    plt.clf()

    data = getColumn(sys.argv[3], 0, " ")
    length = getColumn(sys.argv[3], 1, " ")
    plt.xlabel("Key length")
    plt.ylabel("Number of rare signals (prob=0.20)")
    plt.plot(length, data, 'r-')
    plt.savefig(sys.argv[7])
    plt.clf()

    data = getColumn(sys.argv[4], 0, " ")
    length = getColumn(sys.argv[4], 1, " ")
    plt.xlabel("Key length")
    plt.ylabel("Number of rare signals (prob=0.01)")
    plt.plot(length, data, 'r-')
    plt.savefig(sys.argv[8])
    plt.clf()

    sys.exit(0)
except Exception as e:
    print("Sorry, something went wrong! (Maybe input files does not exist)")
    print(e)
    sys.exit(1)
