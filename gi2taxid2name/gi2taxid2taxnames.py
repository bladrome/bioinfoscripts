import argparse
import sqlite3
from os import popen

import pandas as pd

from ete3 import NCBITaxa

parser = argparse.ArgumentParser()
parser.add_argument("protaccession2taxiddb")
parser.add_argument("taxid2namedb")
parser.add_argument("blastfile")
args = parser.parse_args()

protaccession2taxid = args.protaccession2taxiddb
taxid2name = args.taxid2namedb
blastfile = args.blastfile

ncbi = NCBITaxa()
gi2idconn = sqlite3.connect(protaccession2taxid)
id2naconn = sqlite3.connect(taxid2name)

gilist = [
    1168978, 116525, 116527, 17374148, 21903391, 116530, 116531, 1705937,
    116533
]


def get_lineage_rank_name(taxid):
    ranknames = [
        "kingdom", "phylum", "class", "order", "family", "genus", "species"
    ]
    lineage = ncbi.get_lineage(taxid)
    rank = ncbi.get_rank(lineage)
    revrank = {i[0]:i[1] for i in zip(ranknames, ["Unknown"] * 7)}
    revrank.update({v: k for k, v in rank.items()})

    return \
    ("Unknown" if "Unknown" == revrank[ranknames[0]] else ncbi.translate_to_names([ revrank.get(ranknames[0]) ])[0] ) + " " + ranknames[0], \
    ("Unknown" if "Unknown" == revrank[ranknames[1]] else ncbi.translate_to_names([ revrank.get(ranknames[1]) ])[0] ) + " " + ranknames[1], \
    ("Unknown" if "Unknown" == revrank[ranknames[2]] else ncbi.translate_to_names([ revrank.get(ranknames[2]) ])[0] ) + " " + ranknames[2], \
    ("Unknown" if "Unknown" == revrank[ranknames[3]] else ncbi.translate_to_names([ revrank.get(ranknames[3]) ])[0] ) + " " + ranknames[3], \
    ("Unknown" if "Unknown" == revrank[ranknames[4]] else ncbi.translate_to_names([ revrank.get(ranknames[4]) ])[0] ) + " " + ranknames[4], \
    ("Unknown" if "Unknown" == revrank[ranknames[5]] else ncbi.translate_to_names([ revrank.get(ranknames[5]) ])[0] ) + " " + ranknames[5], \
    ("Unknown" if "Unknown" == revrank[ranknames[6]] else ncbi.translate_to_names([ revrank.get(ranknames[6]) ])[0] ) + " " + ranknames[6] 



def annotateGI(blastfile):
    pcmd = "cat " + blastfile + " | cut -d '\t' -f 1-3"
    with popen(pcmd) as f:
        for line in f:
            line = line.split()
            gene = line[0]
            gi = line[2].split("|")[1]
            for i in gi2idconn.execute(
                    "SELECT DISTINCT * FROM PROTACCESSION2TAXID WHERE gi={0}".
                    format(gi)):
                taxid = i[2]
                for j in id2naconn.execute(
                        "SELECT \"0\", \"2\" FROM TAXID2NAMES WHERE \"0\"={0}".
                        format(taxid)):
                    taxid = j[0]
                    name = j[1]
                    rank = ncbi.get_rank([taxid])[taxid]
                    print(",".join((gene, str(gi), str(taxid), name, rank)))
                    break


# annotateGI(blastfile)


def annotateTAXID(blastfile):
    ## genename, evalue, qhsc, taxid
    pcmd = "cat " + blastfile + " | cut -d '\t' -f 1,12,26,27"
    with popen(pcmd) as f:
        for line in f:
            line = line.split()
            # Without staxid
            if len(line) == 3:
                print(",".join(line), file="Unknowntaxid.csv")
                continue
            gene = line[0]
            evalue = line[1]
            taxid = line[3].split(";")[0]
            for j in id2naconn.execute(
                    "SELECT \"0\", \"2\" FROM TAXID2NAMES WHERE \"0\"={0}".
                    format(taxid)):
                taxid = j[0]
                name = j[1]
                print(",".join((gene, str(evalue), str(taxid), name,
                                *get_lineage_rank_name(taxid))))

                break


annotateTAXID(blastfile)
