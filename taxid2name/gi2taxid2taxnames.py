import pandas as pd
import sqlite3
from ete3 import NCBITaxa

ncbi = NCBITaxa()

gilist = [ 1168978, 116525, 116527, 17374148, 21903391, 116530, 116531, 1705937, 116533 ]

gi2idconn = sqlite3.connect("protaccession2taxid.db")
id2naconn = sqlite3.connect("taxid2name.db")

for gi in gilist:
    for i in gi2idconn.execute("SELECT DISTINCT * FROM PROTACCESSION2TAXID WHERE gi={0}".format(gi)):
        taxid = i[2]
        for j in id2naconn.execute("SELECT \"0\", \"2\" FROM TAXID2NAMES WHERE \"0\"={0}".format(taxid)):
            taxid = j[0]
            name = j[1]
            rank = ncbi.get_rank([taxid])[taxid]
            print(",".join((str(gi), str(taxid), name, rank)))
            break
