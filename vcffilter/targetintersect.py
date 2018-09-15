#!/usr/bin/env python
import argparse
import gzip


def get_snpset(targetsite):
    snpset = set()
    if targetsite.endswith("gz"):
        f = gzip.open(targetsite, 'rt')
    else:
        f = open(targetsite)
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
parser.add_argument("targetsitefile")
args = parser.parse_args()

# snpfile = "./DSW61968-V.vcf"
# targetsite = "./targetsite.vcf"
snpfile = args.snpfile
targetsite = args.targetsitefile

snpset = get_snpset(targetsite)

if snpfile.endswith("gz"):
    f = gzip.open(snpfile, 'rt')
else:
    f = open(snpfile)
for line in f:
    if line.startswith("#"):
        continue
    else:
        field = line.split()
        pos = '\t'.join([field[0], field[1]])
        if pos in snpset:
            print(line.strip())
f.close
