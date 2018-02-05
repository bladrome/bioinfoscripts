import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import esabo

species = ""
def readdata(filepath):
    global species
    datalist = list()
    sample_name = list()
    with open(filepath) as f:
        species = f.readline()
        for line in f.readlines():
            line = line.strip('\n').split("\t")
            sample_name.append(line[0])
            line = np.array(line[1:], dtype=float)
            datalist.append(line)

    return np.array(datalist)


X = readdata("./abundance")

length = X.shape[1]
species_names = species.split()


corelation = np.zeros((length, length), np.float)
pvalue = np.zeros((length, length), np.float)
for i in range(length):
    for j in range(length):
        corelation[i][j], pvalue[i][j] = stats.spearmanr(X[:, i], X[:, j])
        # ESABO

pvalueshreshold = 1e-1
corelation[pvalue > pvalueshreshold] = 0

spearmanpositive = set()
spearmannegative = set()

for i in range(length):
    for j in range(0, i):
        if corelation[i][j] > 0:
            print(i, j)
            print(species_names[i] + " +++ " + species_names[j])
            spearmanpositive.add((i, j))
        if corelation[i][j] < 0:
            print(i, j)
            print(species_names[i] + " --- " + species_names[j])
            spearmannegative.add((i, j))
