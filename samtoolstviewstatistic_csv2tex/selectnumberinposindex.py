import sys

import pandas as pd

if len(sys.argv) != 3:
    print("Usage: {0} {1} {2}".format(sys.argv[0], "samplename", "pos"))
    sys.exit(1)

samplename = sys.argv[1]
pos = int(sys.argv[2])
# pos = 6
# samplename = "./18D124_S2.bam.txt.cs"
data = pd.read_table(samplename, header=None)
positionlist = data[6]
chooseposlist = list()
for position in positionlist:
    position = position.strip("[]")
    position = position.split(",")
    if position[0]:
        numpositionlist = [int(i) for i in position if position]
    else:
        numpositionlist = list()

    chooseposlist.append(True if pos in numpositionlist else False)

# chooseposSeries = pd.Series(chooseposlist)
data = data[chooseposlist]

data.to_csv(
    samplename.split("/")[-1].replace(".", "_") + "_pos_" + str(pos) + ".csv",
    sep='\t',
    index=None,
    header=None)
readscountssum = data[2].sum()
frequencysum = data[3].sum()
print(samplename, pos, readscountssum, frequencysum)
