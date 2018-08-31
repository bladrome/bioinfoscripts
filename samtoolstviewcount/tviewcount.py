import argparse


tviewfile = "./1392.FGF5_sg1.txt.ref"
seqlength = 23

parser = argparse.ArgumentParser()
parser.add_argument("tviewfile")
parser.add_argument("seqlength", type=int)
# parser.add_argument("refseq")
args = parser.parse_args()
tviewfile = args.tviewfile
seqlength = args.seqlength
# refseq = args.refseq


def complementaryseq(refseq, seq):
    retseq = ""
    for index, item in enumerate(seq):
        if item == ' ':
            retseq += refseq[index]
        else:
            retseq += item

    return retseq


def desnp(snpseqfeatures, refseq, seq):
    retseq = seq
    for snp in snpseqfeatures:
        i, base = snp
        retseq = retseq[0:i] + refseq[i] + retseq[i+1:]
    return retseq


count = 0
indelcount = 0
wtcount = 0
otherscount = 0
completecount = 0
uncompletecount = 0

with open(tviewfile) as f:
    # Position
    f.readline()
    # refseq or NNN
    refseq = f.readline()[:seqlength]
    refseq = refseq.upper()
    # ...
    snpseq = f.readline()[:seqlength]
    snpseqfeatures = [ (i, base) for i,base in enumerate(snpseq) if base != '.' ]
    for line in f:
        seq = line[:seqlength]
        if seq:
            count += 1
            if ' ' in seq:
                uncompletecount += 1
            else: 
                completecount += 1
                seq = seq.upper()
                # seq = complementaryseq(refseq, seq)
                seq = desnp(snpseqfeatures, refseq, seq)
                if '*' in seq:
                    indelcount += 1
                elif seq == refseq:
                    wtcount += 1
                else:
                    otherscount += 1
                # print(seq)

    print("COV:\t{0}\t{1}".format(count, count / count * 100))
    print("COMPLETE:\t{0}\t{1}".format(completecount, completecount / count * 100))
    print("UNCOMPLETE:\t{0}\t{1}".format(uncompletecount, uncompletecount / count * 100))
    print("INDEL:\t{0}\t{1}\t{2}".format(indelcount, indelcount / count * 100, indelcount / completecount))
    print("WT:\t{0}\t{1}\t{2}".format(wtcount, wtcount / count * 100, wtcount / completecount))
    print("OTHERS:\t{0}\t{1}\t{2}".format(otherscount, otherscount / count * 100, otherscount / completecount))

