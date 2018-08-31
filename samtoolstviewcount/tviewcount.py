import argparse


tviewfile = "./1392.FGF5_sg1.txt.ref"
seqlength = 23

parser = argparse.ArgumentParser()
parser.add_argument("tviewfile")
parser.add_argument("seqlength", type=int)
args = parser.parse_args()
tviewfile = args.tviewfile
seqlength = args.seqlength


def complementaryseq(refseq, seq):
    retseq = ""
    for index, item in enumerate(seq):
        if item == ' ':
            retseq += refseq[index]
        else:
            retseq += item

    return retseq


count = 0
indelcount = 0
wtcount = 0
otherscount = 0

with open(tviewfile) as f:
    # Position
    f.readline()
    # refseq or NNN
    refseq = f.readline()[0:seqlength]
    # ...
    f.readline()
    for line in f:
        seq = line[:seqlength]
        if seq:
            count += 1
            seq = complementaryseq(refseq, seq)
            if '*' in seq:
                indelcount += 1
            elif seq == refseq:
                wtcount += 1
            else:
                otherscount += 1
            # print(seq)

    print("COV:\t{0}\t{1}".format(tviewfile, count))
    print("INDEL:\t{0}\t{1}".format(indelcount, indelcount / count * 100))
    print("WT:\t{0}\t{1}".format(wtcount, wtcount / count * 100))
    print("OTHERS:\t{0}\t{1}".format(otherscount, otherscount / count * 100))

