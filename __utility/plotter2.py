import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

if len(sys.argv) != 5:
    print("The number of supplied arguments is wrong")
    sys.exit(1)
else:
    print("## I will use this data file: " + str(sys.argv[1]) + " " + sys.argv[2])
    print("## I will plot a graph with this name: " + str(sys.argv[3]) + " " + str(sys.argv[4]))

def getColumn(filename, column, delimiter_input):
    results = csv.reader(open(filename), delimiter=delimiter_input)
    return [result[column] for result in results]

try:
    hd = [np.absolute(np.log(float(i))) for i in getColumn(sys.argv[1], 0, " ")]
    sr = [np.absolute(np.log(float(i))) for i in getColumn(sys.argv[1], 1, " ")]
    length = [1/(float(i)) for i in getColumn(sys.argv[1], 2, " ")]

    hd_t = [np.absolute(np.log(float(i))) for i in getColumn(sys.argv[2], 0, " ")]
    sr_t = [np.absolute(np.log(float(i))) for i in getColumn(sys.argv[2], 1, " ")]
    length_t = [1/(float(i)) for i in getColumn(sys.argv[2], 2, " ")]

    plt.xlabel("Key length")
    plt.ylabel("ExpAVG HD")

    plt.plot(length_t, hd_t, 'g.', length, hd, 'b.')
    plt.savefig(sys.argv[3])
    # plt.show()

    plt.clf()

    plt.xlabel("Key length")
    plt.ylabel("ExpAVG signals probability")

    plt.plot(length_t, sr_t, 'r.', length, sr, 'b.')
    plt.savefig(sys.argv[4])
    # plt.show()

    sys.exit(0)
except Exception as e:
    print("Sorry, something went wrong! (Maybe input files does not exist)")
    print(e)
    sys.exit(1)
