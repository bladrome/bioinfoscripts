#!/usr/bin/env python
# coding=utf-8
"""
intersection > THRESHOLD

Usage:
THRESHOLD:
    python argv[0] > outputfile
RATIO
    python runratio.py

It takes ~20-30s to run.

"""
import sys

import numpy as np
import pandas

# sys.path.append("./")

THRESHOLD = 50
RATIO = float(sys.argv[1])
SIMILAR_NEIGHBOR = 3

data = pandas.read_csv("./python_test_data.csv")

data = data[0:935]
data = data.fillna(0)

dataSE = pandas.DataFrame(
    data,
    columns=[
        "sample1_Pos1", "sample1_Pos2", "sample2_Pos1", "sample2_Pos2",
        "sample3_Pos1", "sample3_Pos2"
    ])
dataSE = dataSE.astype(int)

Sam1S = np.array(dataSE["sample1_Pos1"], dtype=int)
Sam1E = np.array(dataSE["sample1_Pos2"], dtype=int)
Sam2S = np.array(dataSE["sample2_Pos1"], dtype=int)
Sam2E = np.array(dataSE["sample2_Pos2"], dtype=int)
Sam3S = np.array(dataSE["sample3_Pos1"], dtype=int)
Sam3E = np.array(dataSE["sample3_Pos2"], dtype=int)

metadata = list()


def extractRegion(Sample1, Sample2, Sample3):
    for i in range(len(Sample1)):
        for j in range(len(Sample2)):

            if data["sample1_Chr1"][i] != data["sample2_Chr1"][j]:
                continue

            if min(Sam1E[i], Sam2E[j]) < max(Sam1S[i], Sam2S[j]):
                continue

            for k in range(len(Sample3)):

                # Some CHR
                if data["sample1_Chr1"][i] != data["sample3_Chr1"][k] or\
                   data["sample2_Chr1"][j] != data["sample3_Chr1"][k]:
                    continue

                if min(Sam1E[i], Sam3E[k]) < max(Sam1S[i], Sam3S[k]) or \
                        min(Sam2E[j], Sam3E[k]) < max(Sam2S[j], Sam3S[k]):
                    continue
                else:
                    maxS = np.max((Sam1S[i], Sam2S[j], Sam3S[k]), axis=0)
                    minE = np.min((Sam1E[i], Sam2E[j], Sam3E[k]), axis=0)

                    # if (minE - maxS) > THRESHOLD:
                    intersect_length = minE - maxS
                    sample1_length = Sam1E[i] - Sam1S[i]
                    sample2_length = Sam2E[j] - Sam2S[j]
                    sample3_length = Sam3E[k] - Sam3S[k]
                    sample1_ratio = float(intersect_length) / sample1_length
                    sample2_ratio = float(intersect_length) / sample2_length
                    sample3_ratio = float(intersect_length) / sample3_length
                    if sample1_ratio == 1.0 and min(sample1_ratio,
                                                    sample2_ratio,
                                                    sample3_ratio) > RATIO:
                        metadata.append([
                            data["sample1_Chr1"][i], Sam1S[i], Sam1E[i],
                            data["sample2_Chr1"][j], Sam2S[j], Sam2E[j],
                            data["sample3_Chr1"][k], Sam3S[k], Sam3E[k],
                            Sam1E[i] - Sam1S[i], Sam2E[j] - Sam2S[j],
                            Sam3E[k] - Sam3S[k], sample1_ratio, sample2_ratio,
                            sample3_ratio
                        ])


header = [
    "sample1_Chr1",
    "sample1_start(Pos1)",
    "sample1_end(Pos2)",
    "sample2_Chr1",
    "sample2_start(Pos1)",
    "sample2_end(Pos2)",
    "sample3_Chr1",
    "sample3_start(Pos1)",
    "sample3_end(Pos2)",
    "sample1 region length",
    "sample2 region length",
    "sample3 region length",
    "ratio of sample1",
    "ratio of sample2",
    "ratio of sample3",
]

extractRegion(Sam1S, Sam2S, Sam3S)

print(header)

for i in metadata:
    print(i)
# metadata = np.array(metadata)
# metadata = pandas.DataFrame(metadata)
# metadata.to_csv("intersectRegionResult.csv", header=header, index=False)
