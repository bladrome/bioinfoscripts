import pandas as pd
import sqlite3


prot2taxifile = "./prot.accession2taxid10000"
def build_protacc2taxid(prot2taxidfile):
    conn = sqlite3.connect("protaccession2taxid.db")
    prot2taxiddf = pd.read_table(prot2taxidfile, iterator=True)

    while True:
        try:
            chunk = prot2taxiddf.get_chunk(10)
            print(len(chunk))
            chunk.to_sql("PROTACCESSION2TAXID", conn, if_exists="append", index=False)
        except StopIteration:
            break

taxid2namefile = "./names.dmp"
def build_taxid2name(taxid2namefile):
    conn = sqlite3.connect("taxid2name.db")
    # prot2taxiddf = pd.read_table(taxid2namefile, iterator=True)
    taxi2dnamesdf = pd.read_table(taxid2namefile, sep='\t',header=None, usecols=[0, 2, 4, 6], iterator=True)
    taxi2dnamesdf.columns = ["tax_id", "name_txt", "unique_name", "name"]
    print(taxi2dnamesdf.columns)

    while True:
        try:
            chunk = taxi2dnamesdf.get_chunk(200000)
            print(chunk.columns)
            print(len(chunk))
            chunk.to_sql("TAXID2NAMES", conn, if_exists="append", index=False)
        except StopIteration:
            break

# test
# for i in conn.execute("SELECT DISTINCT * FROM PROTACCESSION2TAXID WHERE gi=1168978"):
    # print(i)


build_taxid2name(taxid2namefile)
