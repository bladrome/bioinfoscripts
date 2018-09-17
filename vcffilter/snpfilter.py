#!/usr/bin/env python
import argparse
import gzip
from os.path import basename, splitext


def get_snpset(snplibrary):
    snpset = set()
    if snplibrary.endswith("gz"):
        f = gzip.open(snplibrary, 'rt')
    else:
        f = open(snplibrary)
    for line in f:
        if line.startswith("#"):
            continue
        else:
            line = line.split()
            pos = '\t'.join([line[0], line[1]])
            snpset.add(pos)
    f.close()

    return snpset


def snplibfilter(snpfile, snplibrary, snpset):
    outputfilename = splitext(basename(snpfile))[0] + "_filter_" + basename(
        snplibrary).split(".")[0] + ".vcf"
    outputfile = open(outputfilename, 'w')
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
            print(line.strip(), file=outputfile)
    f.close()
    outputfile.close()
    return outputfilename


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("snpfile")
    parser.add_argument("snplibrary", nargs='+')
    args = parser.parse_args()

    snpfile = args.snpfile

    for snplibrary in args.snplibrary:
        snpset = get_snpset(snplibrary)
        snpfile = filterfile = snplibfilter(snpfile, snplibrary, snpset)
