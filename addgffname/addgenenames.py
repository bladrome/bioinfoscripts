import numpy as np
import pandas as pd

file1data = pd.read_table("./D.S.ZFst.txt")
file2data = pd.read_table("./GCF_001704415.1_ASM170441v1_feature_table.txt")

file1data.rename(columns={'CHROM': 'chromosome'}, inplace=True)

file1data['chromosome'] = file1data['chromosome'].astype(str)
file2data['chromosome'] = file2data['chromosome'].astype(str)
file2data = file2data[np.logical_not(file2data['name'].isna())]


d1chr1 = file1data[file1data['chromosome'] == '1']
d2chr1 = file2data[file2data['chromosome'] == '1']

# reduce
# d1chr1 = d1chr1.head()
# d2chr1 = d2chr1.head()
d1chr1 = d1chr1[0:5]
d2chr1 = d2chr1[0:5]
# print(len(d1chr1))
# print(len(d2chr1))
mergechr1 = d1chr1.merge(d2chr1, on="chromosome", copy=False)

start = np.max((mergechr1['BIN_START'], mergechr1['start']), axis=0)
end = np.min((mergechr1['BIN_END'], mergechr1['end']), axis=0)

mergechr1 = mergechr1[end - start > 0]

outcols = list(d1chr1.columns)
outcols.append('name')
mergechr1[outcols].to_csv("name.csv", index=False)
