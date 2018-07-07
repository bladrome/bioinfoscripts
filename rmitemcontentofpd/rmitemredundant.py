import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: {0} {1} {2}".format(sys.argv[0], "inputfile", "outputfile"))

inputfile = sys.argv[1]
outputfile = sys.argv[2]


df = pd.read_csv(inputfile, sep='\t')
dflist = list()
for line in df.itertuples(index=False):
    tmplist = list()
    for item in line:
        if isinstance(item, str) and ':' in item:
            item = item[0:3]
        tmplist.append(item)
    dflist.append(tmplist)

puredf = pd.DataFrame(dflist)
puredf.columns = df.columns
puredf.to_csv(outputfile, index=None, sep='\t')
