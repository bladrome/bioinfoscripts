import sys
import argparse


## samtools mpileup bamfile | scipts vcffile | ...

parser = argparse.ArgumentParser()
parser.add_argument("vcffile")
args = parser.parse_args(()

vcffile = args.vcffile


def vcfposset(vcffile):
    posset = set()
    with open(vcffile) as f:
        for i in f:
            i = i.split("\t")
            pos = "{0}\t{1}".format(i[0], i[1])
            posset.add(pos)
            
    return posset


posset = vcfposset(vcffile)

for line in sys.stdin:
    i = line.split("\t")
    pos = "{0}\t{1}".format(i[0], i[1])
    if pos in posset:
        print(line.strip())


