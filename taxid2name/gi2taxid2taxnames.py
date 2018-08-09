import pandas as pd
import sqlite3
from ete3 import NCBITaxa

ncbi = NCBITaxa()

gilist = pd.read_table("./gi_list")

gi2idconn = sqlite3.connect("protaccession2taxid.db")
id2naconn = sqlite3.connect("taxid2name.db")

for gi in gilist.itertuples(index=False):
    for i in gi2idconn.execute("SELECT DISTINCT * FROM PROTACCESSION2TAXID WHERE gi={0}".format(gi[0])):
        taxid = i[2]
        for j in id2naconn.execute("SELECT \"0\", \"2\" FROM TAXID2NAMES WHERE \"0\"={0}".format(taxid)):
            taxid = j[0]
            name = j[1]
            rank = ncbi.get_rank([taxid])[taxid]
            print(",".join((str(taxid), name, rank)))
            break
