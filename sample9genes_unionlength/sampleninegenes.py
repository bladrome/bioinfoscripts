import numpy as np
import csv


def readdata(filepath):
    samples = [set() for i in range(9)]
    with open(filepath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for line in csvreader:
            for i in range(len(line)):
                samples[i].add(line[i])

    return samples

samples = readdata("ninegenes.csv")

if __name__ == "__main__":
    import sys
    sample_times = int(sys.argv[1])
    for i in range(sample_times):
        printlist = list()
        for i in range(1, 9):
            index = np.random.randint(0, 8, i)
            sapset = set()
            for i in index:
                sapset = sapset.union(samples[i])
            printlist.append(str(len(sapset)))
        print(",".join(printlist))
