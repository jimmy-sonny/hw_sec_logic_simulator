from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

if len(sys.argv) != 3:
    print("The number of supplied arguments is wrong")
    sys.exit(1)
else:
    print("## I will use this data file: " + str(sys.argv[1]))
    print("## I will plot a graph with this name: " + str(sys.argv[2]))

def getColumn(filename, column, delimiter_input):
    results = csv.reader(open(filename), delimiter=delimiter_input)
    return [result[column] for result in results]

try:
    hda = getColumn(sys.argv[1], 0, " ")
    sa = getColumn(sys.argv[1], 1, " ")
    rs = getColumn(sys.argv[1], 2, " ")
    length = getColumn(sys.argv[1], 3, " ")

    # Type conversion

    hda = list(map(lambda x: float(x),hda))
    sa = list(map(lambda x: float(x),sa))
    rs = list(map(lambda x: float(x),rs))
    length = list(map(lambda x: float(x),length))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

#    ax.scatter(hda, sa, length, c='b', marker='.')
    ax.scatter(hda, rs, length, c='b', marker='.')

    ax.set_xlabel('Avg HD')
    ax.set_ylabel('Number of Rare Signal')
#    ax.set_ylabel('Avg Signal Probability')
    ax.set_zlabel('Key Length')

    plt.savefig(sys.argv[2])
    sys.exit(0)

except Exception as e:
    print("Sorry, something went wrong! (Maybe input files does not exist)")
    print(e)
    sys.exit(1)
