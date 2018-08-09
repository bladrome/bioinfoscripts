import sqlite3
from os import popen

import pandas as pd

from ete3 import NCBITaxa

ncbi = NCBITaxa()
gi2idconn = sqlite3.connect("protaccession2taxid.db")
id2naconn = sqlite3.connect("taxid2name.db")

gilist = [
    1168978, 116525, 116527, 17374148, 21903391, 116530, 116531, 1705937,
    116533
]

pcmd = "cat all_protein_protein.blast | cut -d '\t' -f 1-3"

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
