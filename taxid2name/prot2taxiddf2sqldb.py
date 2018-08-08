import sqlite3
import pandas as pd
conn = sqlite3.connect("protaccession2taxid.db")
prot2taxiddf = pd.read_table("./prot.accession2taxid10000")
prot2taxiddf.to_sql("PROTACCESSION2TAXID", conn, if_exists="append", index=False)
for i in conn.execute("SELECT DISTINCT * FROM PROTACCESSION2TAXID WHERE gi=1168978"):
    print(i)

