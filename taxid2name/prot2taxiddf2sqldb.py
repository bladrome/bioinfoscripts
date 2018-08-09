import sqlite3
import pandas as pd
conn = sqlite3.connect("protaccession2taxid.db")

prot2taxiddf = pd.read_table("./prot.accession2taxid10000", iterator=True)

while True:
    try:
        chunk = prot2taxiddf.get_chunk(10)
        print(chunk)
        chunk.to_sql("PROTACCESSION2TAXID", conn, if_exists="append", index=False)
        print("Looping")
    except StopIteration:
        break

for i in conn.execute("SELECT DISTINCT * FROM PROTACCESSION2TAXID WHERE gi=1168978"):
    print(i)

