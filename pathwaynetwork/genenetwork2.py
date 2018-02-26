import pyximport
pyximport.install()
import numpy as np
import matplotlib.pyplot as plt
import esabo
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
# print(XL)
XH = X[:, 1::2]
# print(XH)

# print(X[0, ::2])
# print(X[0, 1::2])
XL = np.transpose(XL.copy())
XH = np.transpose(XH.copy())

csvhead = sample_name
# csvhead = csvhead.split()
print(csvhead)
plotbool = set(csvhead)

BXL = np.array(XL > 1, dtype=int)
BXH = np.array(XH > 1, dtype=int)

RBXH = esabo.esabo(BXH)
with open("esabo_high.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(RBXH)

RBXL = esabo.esabo(BXL)
with open("esabo_low.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(RBXL)

print("ESABO Done")
length = RBXL.shape[1]
species_pointers = np.array((np.random.normal(0, 200, (length, 2))), dtype=int)
# species_pointers = np.random.randint(0, 200, (length, 2))
# print(species_pointers)
plt.figure(figsize=(10, 8))
z_score_shreshold = 0
for i in range(length):
    for j in range(0, i):
        # ESABO
        if RBXL[i, j] > z_score_shreshold or RBXL[i, j] < z_score_shreshold:
            x1 = species_pointers[i][0]
            y1 = species_pointers[i][1]
            x2 = species_pointers[j][0]
            y2 = species_pointers[j][1]


            if csvhead[i] in plotbool:
                plt.annotate(s=csvhead[i], xy=(x1 + 5, y1 + 5))
                plotbool.remove(csvhead[i])
            if csvhead[j] in plotbool:
                plt.annotate(s=csvhead[j], xy=(x2 + 5, y2 + 5))
                plotbool.remove(csvhead[j])

            if RBXL[i, j] > z_score_shreshold:
                plt.plot([x1, x2], [y1, y2], 'bs-')
            if RBXL[i, j] < z_score_shreshold:
                plt.plot([x1, x2], [y1, y2], 'rs--')


plt.axis("off")
# plt.savefig("BXH.pdf")
plt.show()
