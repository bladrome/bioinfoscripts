import numpy as np
import csv

header = ""
def readdata(filepath):
    global header
    samples = list()
    with open(filepath) as csvfile:
        header = csvfile.readline().strip()
        csvreader = csv.reader(csvfile, delimiter=',')
        for line in csvreader:
            samples.append(line)
    return samples

data = np.array(readdata("./data.csv"))
varx = np.array(data[:, 1:], dtype=float)
varsum = np.sum(varx, axis=0)
res = varx / varsum

res = np.column_stack((data[:, 0].reshape(len(res), 1), res))

print(header)
for i in res:
    print(",".join(i))

