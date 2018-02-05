import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import padjust
import csv


def readdata(filepath):
    global csvhead
    global sample_name
    datalist = list()
    sample_name = list()
    with open(filepath) as f:
        csvhead = f.readline()
        for line in f.readlines():
            line = line.strip('\n').split(",")
            sample_name.append(line[0])
            line = np.array(line[1:], dtype=float)
            datalist.append(line)

    return np.array(datalist)


X = readdata("./journal.pgen.1005846.s011.csv")
print("READ DONE")

XL = X[:, ::2]
XH = X[:, 1::2]
XL = np.transpose(XL.copy())
XH = np.transpose(XH.copy())


X = XL
length = X.shape[1]
species_names = sample_name
corelation = np.zeros((length, length), np.float64)
pvalue = np.zeros((length, length), np.float)
for i in range(length):
    for j in range(length):
        corelation[i][j], pvalue[i][j] = stats.spearmanr(X[:, i], X[:, j])

print(corelation)
pvalue = padjust.padjust(pvalue)
corelation[pvalue > 5e-2] = 0
with open("BL.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(corelation)

X = XH
length = X.shape[1]
species_names = sample_name
corelation = np.zeros((length, length), np.float64)
pvalue = np.zeros((length, length), np.float)
for i in range(length):
    for j in range(length):
        corelation[i][j], pvalue[i][j] = stats.spearmanr(X[:, i], X[:, j])

print(corelation)
pvalue = padjust.padjust(pvalue)
corelation[pvalue > 5e-2] = 0
with open("BH.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(corelation)
