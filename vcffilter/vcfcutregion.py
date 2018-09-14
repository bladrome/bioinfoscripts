#!/usr/bin/env python
import argparse
import gzip


def get_generegion(snplibrary, chromosome, genestart, geneend):
    if snplibrary.endswith("gz"):
        f = gzip.open(snplibrary, 'rt')
    else:
        f = open(snplibrary)

    CHROMPASS = False
    for line in f:
        if line.startswith("#"):
            continue;
        else:
            items = line.split()
            chrom = items[0]
            site = int(items[1])
            if chrom == chromosome and genestart <= site <= geneend:
                CHROMPASS = True
                print(line.strip())
            if CHROMPASS and site > geneend:
                break
    f.close()
    return None



parser = argparse.ArgumentParser()
parser.add_argument("snplibrary")
parser.add_argument("chromosome")
parser.add_argument("genestart", type=int)
parser.add_argument("geneend", type=int)
args = parser.parse_args()

snplibrary = args.snplibrary
chromosome = args.chromosome
genestart = args.genestart
geneend = args.geneend

get_generegion(snplibrary, chromosome, genestart, geneend)
