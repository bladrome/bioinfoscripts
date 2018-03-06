import sys
import numpy as np
import pandas as pd
import gffread

if len(sys.argv) < 4:
    print("Usage:{0} {1} {2} {3} {4}".format(sys.argv[0], "fst_file",
                                                          "gff_file",
                                                          "chr_list",
                                                          "outputfile"))
    sys.exit(1)

fstdata = pd.read_table(sys.argv[1], low_memory=False)
fstdata = fstdata.sort_values(by=['V7'], ascending=False)
fstdata = fstdata[0:int(len(fstdata)/100)]
gffdata = gffread.readgff(sys.argv[2])

fstdata.rename(columns={'CHROM': 'chromosome',
                        'BIN_START': 'fst_start',
                        'BIN_END': 'fst_end'}, inplace=True)
fstdata['chromosome'] = fstdata['chromosome'].astype(str)


annodata = pd.DataFrame()
for chromosome in set([sys.argv[i] for i in range(3, len(sys.argv) - 1)]):
    fst = fstdata[fstdata['chromosome'] == chromosome]
    gff = gffdata[gffdata['chromosome'] == chromosome]

    cross = fst.merge(gff, on="chromosome", copy=False)
    start = np.max((cross['fst_start'], cross['gff_start']), axis=0)
    end = np.min((cross['fst_end'], cross['gff_end']), axis=0)

    cutoff = end - start > 0
    start = start[cutoff]
    end = end[cutoff]
    cross = cross[cutoff]

    cross['intersection_start'] = (start)
    cross['intersection_end'] = (end)
    cross['intersection_length'] = (end - start)

    outcols = list(fstdata.columns)
    outcols.extend(['gff_start', 'gff_end',
                    'intersection_start',
                    'intersection_end',
                    'intersection_length',
                    'gene'])
    cross = cross[outcols]

    annodata = annodata.append(cross)


annodata = annodata[np.logical_not(annodata['gene'].isnull())]
annodata = annodata[np.logical_not(annodata.duplicated(('chromosome',
                                                        'fst_start',
                                                        'fst_end',
                                                        'gene')))]
annodata = annodata[np.logical_not(annodata.duplicated())]
annodata = annodata.sort_values(by=['fst_start'])
annodata.to_csv(sys.argv[len(sys.argv)-1], index=False)
