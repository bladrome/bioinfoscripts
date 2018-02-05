# Compare coefficient with ESABO
- [ESABO](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005361)

## Data
- journal.pgen.1005846.s011.csv
Aboundance matrix of two groups: group low and group high
\# of samples:300

## Source
- esabo.py  
function esabo:Calculate the esabo score for a given binary abundance matrix.


- spearman.py
Calculate the coefficient of the data above using spearman rank.
Output *BL.csv* for group low.
Output *BH.csv* for group high.


- genenetwork.py
Calculate the coefficient of the data above using ESABO
Output *esabo_low.csv* for group low.
Output *esabo_high.csv* for group high.

## Run
```sh
$ python genenetwork.py
$ python spearman.py
```

BL.csv, BH.csv, esabo_low.csv and esabo_high.csv could be used for further analysis.
