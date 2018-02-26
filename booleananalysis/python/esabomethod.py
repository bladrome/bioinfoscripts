import numpy as np
# import matplotlib
# matplotlib.use("Agg")
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


X = readdata("../abundance")
ABX = np.array(X > 1e-4, dtype=int)
# print(ABX)
IM = esabo.esabo(ABX)
# print(IM)

esabopositive = set()
esabonegative = set()


length = IM.shape[1]
# species_pointers = np.random.randint(0, 200, (length, 2))
species_pointers = np.array((np.random.normal(0, 200, (length, 2))), dtype=int)
species_names = species.split()
plotbool = set(species_names)
# print(species_pointers)
plt.figure(figsize=(10, 8))
z_score_shreshold = 0
for i in range(length):
    for j in range(0, i):
        # ESABO
        if IM[i, j] > z_score_shreshold or IM[i, j] < z_score_shreshold:
            x1 = species_pointers[i][0]
            y1 = species_pointers[i][1]
            x2 = species_pointers[j][0]
            y2 = species_pointers[j][1]

            if species_names[i] in plotbool:
                plt.annotate(s=species_names[i], xy=(x1 + 5, y1 + 5))
                plotbool.remove(species_names[i])
            if species_names[j] in plotbool:
                plt.annotate(s=species_names[j], xy=(x2 + 5, y2 + 5))
                plotbool.remove(species_names[j])

            if IM[i, j] > z_score_shreshold:
                plt.plot([x1, x2], [y1, y2], 'bs-')
                esabopositive.add((i, j))
                print(i, j)
                print(species_names[i] + " +++ " + species_names[j])
            if IM[i, j] < z_score_shreshold:
                plt.plot([x1, x2], [y1, y2], 'rs--')
                esabonegative.add((i, j))
                print(i, j)
                print(species_names[i] + " --- " + species_names[j])


plt.axis("off")
# plt.savefig("abc.pdf")
plt.show()
