#!/usr/bin/env python
import numpy as np

chrname = list()
chrcount = list()
with open("./sampleTimestest.txt") as f:
    for line in f.readlines():
        index = (line.split()[0])
        chrname.append(index)
        numlist = list()
        for strnum in line.split()[1:]:
            numlist.append(int(strnum))
        chrcount.append(numlist)

mergeresultlist = list()
with open("./merge.offtarget.txt") as f:
    for line in f.readlines():
        if line.split()[0] in ['#']:
            continue
        line = line.split()[0].split('-')[0]
        name = line.split(':')
        mergeresultlist.append(name)

mergeresultlist = np.array(mergeresultlist)
mergechrname = mergeresultlist[:, 0]
mergereulststart = mergeresultlist[:, 1]
mergereulststart = np.array(mergereulststart, dtype=int)

randommin = list()
distance = dict()
for i in range(len(chrname)):
    randommin.append(list())

    for randomnum in chrcount[i]:
        distance = list()
        for j in range(len(mergechrname)):
            if chrname[i] == mergechrname[j]:
                if randomnum < mergereulststart[j]:
                    distance.append(mergereulststart[j] - randomnum)
                elif randomnum > mergereulststart[j] + 23:
                    distance.append(randomnum - (mergereulststart[j] + 23))
                else:
                    distance.append(0)

        randommin[i].append(np.min(np.array(distance)))

for i in range(len(chrname)):
    for j in range(len(chrcount[i])):
        print(chrname[i], chrcount[i][j], randommin[i][j])
