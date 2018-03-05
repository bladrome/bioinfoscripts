import numpy as np
import pandas as pd


def get_genename_list(annotation):
    genelist = list()
    for i, item in annotation.items():
        item = item.split(';')
        gene = [j.split('=')[1] for j in item if j.startswith("gene=", 0, 5)]
        genelist.append(gene[0] if gene else None)

    return genelist


def readgff(filepath):
    gffdata = pd.read_table(filepath, skiprows=7, header=None,
                            comment="#")
    # filter
    gffdata = gffdata[gffdata[2] != "cDNA_match"]

    annotation = gffdata[8]
    genenamelist = get_genename_list(annotation)
    genenamedf = pd.Series(genenamelist)
    gffdata[9] = genenamedf
    gffdata = gffdata[[0, 3, 4, 9]]
    gffdata[0] = gffdata[0].astype(str)
    gffdata.rename(columns={0: "chromosome", 3: "gff_start",
                            4: "gff_end", 9: "gene"}, inplace=True)
    #gffdata = gffdata[np.logical_not(gffdata['gene'].isna())]

    return gffdata
