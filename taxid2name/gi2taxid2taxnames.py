import sqlite3
from os import popen
import argparse

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



def annotateGI(blastfile):
    pcmd = "cat " + blastfile  + " | cut -d '\t' -f 1-3"
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


annotateGI(blastfile)
