import numpy as np
import pandas as pd
import gffread

fstdata = pd.read_table("./D.S.ZFst.txt")
gffdata = gffread.readgff("./ASM_chr_10000.gff")

fstdata.rename(columns={'CHROM': 'chromosome',
                        'BIN_START': 'fst_start',
                        'BIN_END': 'fst_end'}, inplace=True)
fstdata['chromosome'] = fstdata['chromosome'].astype(str)


annodata = pd.DataFrame()
# for chromosome in set(fstdata['chromosome']):
for chromosome in set(['1']):
    fst = fstdata[fstdata['chromosome'] == chromosome]
    gff = gffdata[gffdata['chromosome'] == chromosome]

    cross = fst.merge(gff, on="chromosome", copy=False)
    start = np.max((cross['fst_start'], cross['gff_start']), axis=0)
    end = np.max((cross['fst_end'], cross['gff_end']), axis=0)
    cross = cross[end - start > 0]
    outcols = list(fstdata.columns)
    outcols.extend(['gff_start', 'gff_end', 'gene'])
    cross = cross[outcols]
    annodata = annodata.append(cross)


annodata = annodata[np.logical_not(annodata.duplicated())]
annodata.to_csv("result_anno.csv", index=False)
# mergechr1 = d1chr1.merge(d2chr1, on="chromosome", copy=False)

# start = np.max((mergechr1['BIN_START'], mergechr1['start']), axis=0)
# end = np.min((mergechr1['BIN_END'], mergechr1['end']), axis=0)

# mergechr1 = mergechr1[end - start > 0]

# mergechr1[outcols].to_csv("name.csv", index=False)
