# Taxid to lineage rank name


## Dependencies
- ete3
- sqlite3
- pandas

## Database
```
$ wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip
$ unzip taxdmp.zip
$ wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/prot.accession2taxid.gz
$ gunzip prot.accession2taxid.gz
```


## Build sqldb
```python
$ python prot2taxiddf2sqldb.py prot.accession2taxid names.dmp
$ pip install ete3
$ python -q
>>> from ete3 import NCBITaxa
>>> ncbi = NCBITaxa("taxdump_file=taxdmp.zip")
>>> # waiting...
Loading node names...
1818050 names loaded.
202404 synonyms loaded.
Loading nodes...
1818050 nodes loaded.
Linking nodes...
Tree is loaded.
Updating database: $HOME/.etetoolkit/taxa.sqlite ...
 1818000 generating entries...
Uploading to $HOME/.etetoolkit/taxa.sqlite

Inserting synonyms:      200000
Inserting taxid merges:  50000
Inserting taxids:       1815000

>>> exit()
```

## Usage

### gi2taxid2taxnames.py
```python
def get_taxid(gi):
    ...

def get_lineage_rank_name(taxid):
    ...

def get_name_from_taxid(taxid):
    ...

def annotateGI(blastfile):
    ... 

def annotateTAXID(blastfile):
    ...
```

### rewirte your annotateGI or annotateTAXID

``` python

def annotateGI(blastfile):
    pcmd = "cat " + blastfile + " | cut -d '\t' -f 1-3"
    with popen(pcmd) as f:
        for line in f:
            line = line.split()
            gene = line[0]
            gi = line[2].split("|")[1]
            taxid = get_taxid(gi)
            name = get_name_from_taxid(taxid)
            rank = ncbi.get_rank([taxid])[taxid]
            print(",".join((gene, str(gi), str(taxid), name, rank)))


def annotateTAXID(blastfile):
    # genename, evalue, qhsc, taxid
    pcmd = "cat " + blastfile + " | cut -d '\t' -f 1,12,26,27"
    with popen(pcmd) as f, open("Unknowntaxid.csv", 'w') as ukf:
        for line in f:
            line = line.split()
            # Without staxid
            if len(line) == 3:
                print(",".join(line), file=ukf)
                continue
            gene = line[0]
            evalue = line[1]
            taxid = line[3].split(";")[0]
            name = get_name_from_taxid(taxid)
            print(",".join((gene, str(evalue), str(taxid), name,
                            *get_lineage_rank_name(taxid))))


#annotateTAXID(blastfile)
```
