#!/usr/bin/env python
import argparse
import gzip


def get_snpset(snplibrary):
    snpset = set()
    if snplibrary.endswith("gz"):
        f = gzip.open(snplibrary, 'rt')
    else:
        f = open(snplibrary)
    for line in f:
        if line.startswith("#"):
            continue;
        else:
            line = line.split()
            pos = '\t'.join([line[0], line[1]])
            snpset.add(pos)
    f.close()

    return snpset


parser = argparse.ArgumentParser()
parser.add_argument("snpfile")
parser.add_argument("snplibrary")
args = parser.parse_args()

# snpfile = "./DSW61968-V.vcf"
# snplibrary = "./snplibrary.vcf"
snpfile = args.snpfile
snplibrary = args.snplibrary

snpset = get_snpset(snplibrary)

if snpfile.endswith("gz"):
    f = gzip.open(snpfile, 'rt')
else:
    f = open(snpfile)
for line in f:
    field = line.split()
    pos = '\t'.join([field[0], field[1]])
    if pos in snpset:
        continue
    else:
        print(line.strip())
f.close
