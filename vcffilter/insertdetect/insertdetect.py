import argparse
import re
import io

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("sequencefile")
parser.add_argument("indexvcffile")
parser.add_argument("outputfile")
args = parser.parse_args()

# seqfile = "./1_seq"
# vcffile = "./2_indel.vcf"

seqfile = args.sequencefile
vcffile = args.indexvcffile
outputfile = args.outputfile

sequence = ""
with open(seqfile) as f:
    for i in f:
        sequence += i

vcfdata = pd.read_table(vcffile, header=None, comment='#')
outputstritem = ""
for item in vcfdata.itertuples(index=False):
    if len(item[3]) < len(item[4]):
        pos = re.finditer(item[4], sequence)
        pos = [str(i.start()) for i in pos]
        # print(item[4])
        # print(pos)
        if pos:
            stritem = "\t".join(str(i) for i in item)
            stritem = stritem + "\t" + ",".join(pos) + "\t" + str(len(item[4])) + "\n"
            outputstritem += stritem

outdf = pd.read_table(io.StringIO(outputstritem), header=None, sep='\t')
outdf = outdf.sort_values(by=[11])
outdf.to_csv(args.outputfile, sep='\t', index=None, header=None)
