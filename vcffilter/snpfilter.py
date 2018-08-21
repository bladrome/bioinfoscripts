#!/usr/bin/env python

snpfile = "./DSW61968-V.vcf"
snplibrary = "./snplibrary.vcf"


def get_snpset(snplibrary):
    snpset = set()
    with open(snplibrary) as f:
        for line in f:
            if line.startswith("#"):
                continue;
            else:
                line = line.split()
                pos = '\t'.join([line[0], line[1]])
                snpset.add(pos)

    return snpset



snpset = get_snpset(snplibrary)
with open(snpfile) as f:
    for line in f:
        field = line.split()
        pos = '\t'.join([field[0], field[1]])
        if pos in snpset:
            continue
        else:
            print(line.strip())
