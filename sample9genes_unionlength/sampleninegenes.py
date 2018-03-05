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


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage:\n\t {0} csvfile {1}".format(sys.argv[0], "sampletimes"))
    else:
        samples = readdata(sys.argv[1])
        sample_times = int(sys.argv[2])
        for i in range(sample_times):
            printlist = list()
            for i in range(1, len(samples)):
                index = np.random.randint(0, len(samples) - 1, i)
                sapset = samples[0]
                for i in index:
                    sapset = sapset.union(samples[i])
                    # sapset = sapset & samples[i]
                    # sapset = sapset | samples[i]
                printlist.append(str(len(sapset)))
            print(",".join(printlist))
