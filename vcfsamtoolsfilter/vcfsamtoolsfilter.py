from os import popen

import pandas as pd

samtoolsvcffile = "./family123.samtools.mpileup.vcf"
samtoolsvcffile = "./samtools.vcf"

cmdstr = 'cat ' + samtoolsvcffile + \
    '| grep -v "#" | awk -v OFS="\t" \'{ split($10, F, ":"); split($11, M, ":"); split($12, f, ":"); print($0,F[1],M[1], f[1], F[1]","M[1]","f[1])}\''

# print(cmdstr)
vcfdf = pd.read_table(popen(cmdstr, 'r'), header=None)#, nrows=10000)
vcfdf.columns = [
    "CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT",
    "Father", "Mother", "f", "F_GT", "M_GT", "f_GT", "GT"
]

casesstats = vcfdf.groupby(by=['GT']).count().CHROM
perstats = casesstats / casesstats.sum()
print(casesstats)
print(len(casesstats))
print(perstats)



"""

0/0     0/1     1/1

 F       M       f                      !f
---     ---     ---                    ---- 
0/0     0/0     0/0                     |     0/1     1/1
0/0     0/1     0/0     0/1             |     1/1
0/0     1/1     0/1                     |     0/1     1/1
0/1     0/1     0/0     0/1     1/1     |
0/1     1/1     0/1     1/1             |     1/1
1/1     1/1     1/1                     |     0/1     1/1
"""
