#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : GeneratePro.py
# Author            : blkcat <blackwhitedoggie@163.com>
# Date              : 05.12.2017
# Last Modified Date: 06.12.2017
import numpy as np

linelist = list()
with open("./GCF_001704415.1_ARS1_assembly_report.txt") as f:
    for line in f.readlines():
        beginer = line.split()[0]
        if beginer in ['#', '##']:
            continue
        linesplit = line.split()
        linelist.append([(linesplit[2]), int(linesplit[9])])

linelist = np.array(linelist)
chrname = linelist[:, 0]
chrlength = linelist[:, 1]
chrlength = np.array(chrlength, dtype=int)
chrsum = np.sum(chrlength)
ratio = (chrlength / float(chrsum))
procount = np.array(ratio * 10000, dtype=int)

chrcount = list()
for i in range(len(chrlength)):
    a = np.random.randint(0, chrlength[i], procount[i])
    chrcount.append(a)

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
for i in range(len(chrlength)):
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

for i in range(len(chrlength)):
    for j in range(len(chrcount[i])):
        print(chrname[i], chrlength[i], chrcount[i][j], randommin[i][j])
        # print(chrname[i]),
        # print(chrlength[i]),
        # print(chrcount[i][j]),
        # print(randommin[i][j])
