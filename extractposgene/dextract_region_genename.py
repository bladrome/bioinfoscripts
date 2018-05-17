import sys

import pandas as pd

posfile = "./postest.txt"
outputfile = "output.csv"
intputfile = "././GCF_001704415.1_ARS1_genomic_head500.gff"

if len(sys.argv) != 4:
    print("Usage: {0} {1} {2} {3}".format(sys.argv[0], "inputGFFfile",
                                          "posfile", "outputfile.csv"))
    sys.exit(1)

intputfile = sys.argv[1]
posfile = sys.argv[2]
outputfile = sys.argv[3]

chromosomemap = {
    "NC_030808.1": "1",
    "NC_030809.1": "2",
    "NC_030810.1": "3",
    "NC_030811.1": "4",
    "NC_030812.1": "5",
    "NC_030813.1": "6",
    "NC_030814.1": "7",
    "NC_030815.1": "8",
    "NC_030816.1": "9",
    "NC_030817.1": "10",
    "NC_030818.1": "11",
    "NC_030819.1": "12",
    "NC_030820.1": "13",
    "NC_030821.1": "14",
    "NC_030822.1": "15",
    "NC_030823.1": "16",
    "NC_030824.1": "17",
    "NC_030825.1": "18",
    "NC_030826.1": "19",
    "NC_030827.1": "20",
    "NC_030828.1": "21",
    "NC_030829.1": "22",
    "NC_030830.1": "23",
    "NC_030831.1": "24",
    "NC_030832.1": "25",
    "NC_030833.1": "26",
    "NC_030834.1": "27",
    "NC_030835.1": "28",
    "NC_030836.1": "29",
    "NW_017189516.1": "X1",
    "NW_017189517.1": "X2"
}

data = pd.read_table(
    intputfile, header=None, sep='\t', comment='#')#, nrows=50)

genenamelist = list()
for item in data.itertuples():
    description = item[9]
    description = description.split(';')
    genename = [i for i in description if i.startswith("gene=")]
    genename = genename[0].split('=')[1] if genename else ""
    # print(genename)
    genenamelist.append(genename)

data['genename'] = genenamelist

data['start'] = pd.np.min((data[3], data[4]), axis=0)
data['end'] = pd.np.max((data[3], data[4]), axis=0)
data.rename(columns={0: "chromosome", 2: 'region'}, inplace=True)



def read_pos(filename):
    pos = pd.read_table(filename, header=None, sep='\t')
    pos.rename(columns={0: 'chrnum', 1: "pos"}, inplace=True)
    pos.chrnum = pos.chrnum.astype('str')
    chromosome = pos.chrnum.copy()
    for key, value in chromosomemap.items():
        chromosome[ pos.chrnum == value ] = key
    pos['chromosome'] = chromosome
    return pos


pos = read_pos(posfile)
# print(pos.chrnum)

pos.chromosome = pos.chromosome.astype('str')
data.chromosome = data.chromosome.astype('str')

c = data.merge(pos, on=['chromosome'])

c = c[c.start <= c.pos]
c = c[c.pos <= c.end]
c = c[c.genename != '']

output = c[['chrnum', 'region', 'genename', 'start', 'end', 'pos']]
output.to_csv(outputfile, index=None)
