import sys

import numpy as np
import pandas as pd

if len(sys.argv) != 4:
    print("Usage: {0} {1} {2} {3}".format(sys.argv[0], "reference_sequence",
                                          "tview_bam", "outputbamtype.csv"))
    sys.exit(1)

# reference = 'TGGAGCAGAGCAGCTTCCAGTGG'
reference = sys.argv[1]
reference = reference.upper()

alignmatrix = pd.read_table(sys.argv[2], skiprows=2, header=None)
# alignmatrix = pd.read_table("./AWGBGAA05774-2-38.bam.sgRNA1.tview.bam.txt", skiprows=2, header=None)
aligndepth = len(alignmatrix)

alignlist = list()

for i in alignmatrix.itertuples():
    align = str(i[1])[0:len(reference)]
    align = align.replace(' ', '>')
    align = align.replace('<', '>')
    align = align.replace('-', '>')
    alignlist.append(align)

# Replace > with ref
for i, item in enumerate(alignlist):
    for j, base in enumerate(item):
        if base == '>':
            alignlist[i] = alignlist[i][0:j] + \
                reference[j] + alignlist[i][j+1:]
    alignlist[i] = alignlist[i].upper()

alignmatrix = pd.Series(alignlist)
aligncounts = alignmatrix.value_counts()
alignmatrix = pd.DataFrame(data=[i for i in aligncounts.items()])

# alignmatrix = alignmatrix[alignmatrix[0] != reference]
# print(alignmatrix)

diffbaselist = list()
diffcountlist = list()
diffindexlist = list()
for i in alignmatrix.itertuples():
    align = i[1]
    count = 0
    base = list()
    index = list()
    for i in range(len(align)):
        if align[i] != reference[i]:
            count += 1
            base.append(align[i])
            index.append(i)
            # print(align[i], reference[i], count, base)

    diffindexlist.append(index)
    diffbaselist.append(base)
    diffcountlist.append(count)

# print(len(set((tuple(i) for i in diffindexlist))))

alignmatrix[2] = alignmatrix[1] / float(aligncounts.sum() / 100)
alignmatrix[3] = diffcountlist
alignmatrix[4] = diffbaselist
alignmatrix[5] = diffindexlist
# print(alignmatrix)
alignmatrix.to_csv(sys.argv[3], sep='\t', header=None)

# a = pd.Series((tuple(i) for i in diffindexlist))
# b = a.value_counts()
# print(b)


def read_name_dict(namesdictfile):
    namesdict = dict()
    with open(namesdictfile) as f:
        for i in f:
            i = i.strip().split()
            namesdict[i[0]] = i[1]

    return namesdict


namesdict = read_name_dict("./tt.samples.ID")
alignmatrix = alignmatrix[alignmatrix[2] > 1]
alignmatrix = alignmatrix[alignmatrix[3] != 0]
header = list()
samplename = sys.argv[3].split('_')[0]
header.append(samplename + "/" + namesdict[samplename])
header.extend([' '] * (len(alignmatrix.columns) - 1))
alignmatrix.to_csv(
    # sys.argv[3].split('.')[0] + "_filter.csv", sep='\t', header=header, index=False)
    sys.argv[3].split('.')[0] + "_filter.csv", sep='\t', header=header)
