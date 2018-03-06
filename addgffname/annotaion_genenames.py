import sys
import numpy as np
import pandas as pd
import gffread

if len(sys.argv) < 4:
    print("Usage:{0} {1} {2} {3} {4}".format(sys.argv[0], "fst_file", "gff_file", "chr_list", "outputfile"))
    sys.exit(1)

fstdata = pd.read_table(sys.argv[1])
fstdata = fstdata.sort_values(by=['V7'], ascending=False)
fstdata = fstdata[0:int(len(fstdata)/100)]
gffdata = gffread.readgff(sys.argv[2])
#gffdata = gffread.readgff("./ASM_chr.gff")

fstdata.rename(columns={'CHROM': 'chromosome',
                        'BIN_START': 'fst_start',
                        'BIN_END': 'fst_end'}, inplace=True)
fstdata['chromosome'] = fstdata['chromosome'].astype(str)


annodata = pd.DataFrame()
# for chromosome in set(fstdata['chromosome']):
for chromosome in set([sys.argv[i] for i in range(3, len(sys.argv) - 1)]):
    fst = fstdata[fstdata['chromosome'] == chromosome]
    gff = gffdata[gffdata['chromosome'] == chromosome]

    cross = fst.merge(gff, on="chromosome", copy=False)
    start = np.max((cross['fst_start'], cross['gff_start']), axis=0)
    end = np.min((cross['fst_end'], cross['gff_end']), axis=0)
    #print((start))
    #print((end))

    print(len(cross))
    cutoff = end - start > 0
    start = start[cutoff]
    end = end[cutoff]
    cross = cross[cutoff]
    print(len(cutoff))
    print(len(cross))
    print(len(start))
    print(len(end))
    #print((start))
    #print((end))
    cross['intersection_start'] = (start)
    cross['intersection_end'] = (end)
    cross['intersection_length'] = (end - start)

    #print(cross['intersection_start'])
    #print(cross['intersection_end'])
    #print(cross['intersection_length'])

    outcols = list(fstdata.columns)
    outcols.extend(['gff_start', 'gff_end', 'intersection_start', 'intersection_end', 'intersection_length', 'gene'] )
    cross = cross[outcols]

    annodata = annodata.append(cross)


annodata = annodata[np.logical_not(annodata['gene'].isnull())]
annodata = annodata[np.logical_not(annodata.duplicated(('chromosome', 'fst_start', 'fst_end', 'gene')))]
annodata = annodata[np.logical_not(annodata.duplicated())]
annodata = annodata.sort_values(by=['fst_start'])
annodata.to_csv(sys.argv[len(sys.argv)-1], index=False)
# mergechr1 = d1chr1.merge(d2chr1, on="chromosome", copy=False)

# start = np.max((mergechr1['BIN_START'], mergechr1['start']), axis=0)
# end = np.min((mergechr1['BIN_END'], mergechr1['end']), axis=0)

# mergechr1 = mergechr1[end - start > 0]

# mergechr1[outcols].to_csv("name.csv", index=False)
