# taxid to lineage rank name


## dependencies
- ete3

## database
```
$ wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdmp.zip
$ unzip taxdmp.zip
$ wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/accession2taxid/prot.accession2taxid.gz
$ gunzip prot.accession2taxid.gz
```


## build sqldb
```python
$ python prot2taxiddf2sqldb.py prot.accession2taxid names.dmp
$ pip install ete3
$ python
>>> from ete3 import NCBITaxa
>>> 
>>> ncbi = NCBITaxa?
>>> ncbi = NCBITaxa("taxdump_file=taxdmp.zip")
>>> exit 
```
