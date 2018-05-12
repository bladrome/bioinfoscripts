
import pandas as pd
import sys
import re


threshold = 1
samplename = sys.argv[1]
# samplename = "AWGBGAA05782-4-38_bam_tviw_6_95419300_txt.csv"
# samplename = "AWGBGAA05771-2-35_bam_tviw_6_95419300_txt.csv"
sample = pd.read_csv(samplename, header=None, sep='\t')


indellist = list()
indelitemlist  = list()

# Pandas(Index=0, _1=0, _2='AAGCTCAAGGGGAGAAGCGCCT', _3=3485, _4=42.897587395371744, _5=2, _6="['A', 'A']", _7='[0, 1]')
for i in sample.itertuples():
    seq = i[2]
    seq.upper()
    seq = seq.replace("*", "-")
    seq = seq.replace("A", "*")
    seq = seq.replace("T", "*")
    seq = seq.replace("G", "*")
    seq = seq.replace("C", "*")
    indellist.append(seq)


sample['indelpattern'] = indellist
sample['pattern'] = 0
indelpatternset = set(sample.indelpattern)
ptcount = list()
for i, pt in enumerate(indelpatternset):
    # sample['pattern'][sample.indelpattern == pt] = i
    count = pd.np.sum(pd.np.array(sample.indelpattern == pt, dtype=int))
    ptcount.append(count)

ptcount = pd.np.array(ptcount, dtype=float)
ptcount /= float(pd.np.sum(ptcount))
# print(samplename)
samplename = samplename.split("_")
print("#" + " ".join((samplename[0], samplename[3], samplename[4])))
for i, item in enumerate(indelpatternset):
    ptstr = str(sample[1][sample.indelpattern == item][0:1])
    ptstr = ptstr.split()
    # for i in re.findall("-", item):
        # print(i.span())
    startposlist = [i.span()[0] for i in re.finditer("-", item)]
    startpos = int(samplename[4]) if not startposlist else int(samplename[4]) + startposlist[0]
    # print(str(i) + "\t" + str(startpos) + "\t" + str(item) + "\t" + ptstr[1] + "\t" + str(ptcount[i] * 100))
    indelitem = (str(i) + "\t" + str(startpos) + "\t" + str(item) + "\t" + ptstr[1] + "\t" + str(ptcount[i] * 100))
    indelitemlist.append(indelitem.split())


# print(indelitemlist)
dfindelmatrix = pd.DataFrame(indelitemlist)
dfindelmatrix[4] = pd.to_numeric(dfindelmatrix[4])
# print(dfindelmatrix)
allstarpattern = [i for i in dfindelmatrix[2] if i.count('-') == 0][0]
outputmatrix = dfindelmatrix[dfindelmatrix[4] > threshold] 
outputmatrix.append(dfindelmatrix[dfindelmatrix[2] == allstarpattern])
outputmatrix.to_csv(sys.stdout, sep='\t', header=None, index=None, columns=[1, 3, 4])

