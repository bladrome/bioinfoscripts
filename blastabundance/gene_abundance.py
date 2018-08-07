from os import popen

import numpy as np
import pandas as pd


def get_fastafile(filepath):
    nrfileabstract = popen("grep '>' " + filepath)
    namelist = list()
    # descriptionlist = list()
    # flaglist = list()
    # multilist = list()
    lengthlist = list()
    for item in nrfileabstract:
        item = item.strip()[1:]
        namelist.append(item)
        # descriptionlist.append(item[1])
        # flaglist.append(item[2])
        # multilist.append(item[3])
        lengthlist.append(item.split('|')[5])
    nrfastadf = pd.DataFrame()
    nrfastadf['name'] = namelist
    nrfastadf['length'] = lengthlist
    nrfastadf.length = nrfastadf.length.astype(int)

    return nrfastadf


def get_blastfile(filepath):
    blastabstract = popen("cut -d '\t' -f 4,8 " + filepath)
    blastfidf = pd.read_csv(blastabstract, sep='\t', header=None)
    blastfidf.columns = ['length', 'name']
    blastfidf.length = blastfidf.length.astype(int)
    blastfidf = blastfidf.groupby(['name'])['length'].sum()
    blastfidf = pd.concat(
        [pd.DataFrame(blastfidf.index),
         pd.DataFrame(blastfidf.values)],
        axis=1)
    blastfidf.columns = ['name', 'length']

    return blastfidf


def get_gene_abundance(nrfastafilepath, blastfilepath):

    nrfastadf = get_fastafile(nrfastafilepath)
    blastfidf = get_blastfile(blastfilepath)
    unigenedf = blastfidf[blastfidf.length > 2]

    # Assure blastfile is common to nrfasta
    nrfastanameset = set(nrfastadf.name.tolist())
    unigenenameset = set(unigenedf.name.tolist())
    sampleuniqnameset = unigenenameset - nrfastanameset
    unigenenameset = unigenenameset - sampleuniqnameset

    blastcommondf = unigenedf[unigenedf.name.isin(unigenenameset)]
    blastcommondf = blastcommondf.sort_values(by=['name'])
    nrfastacommondf = nrfastadf[nrfastadf.name.isin(unigenenameset)]
    nrfastacommondf = nrfastacommondf.sort_values(by=['name'])

    sample_reads_num = np.array(blastcommondf.length)
    gene_length = np.array(nrfastacommondf.length)
    gene_abundance = sample_reads_num / gene_length
    relative_gene_abundance = gene_abundance / gene_abundance.sum()

    outputdf = pd.DataFrame()
    outputdf['name'] = blastcommondf.name
    outputdf['aboundance'] = relative_gene_abundance

    return outputdf

if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("nrfastafile")
    parser.add_argument("blastfile")
    parser.add_argument("-o", "--output", dest="gene_abundance", nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    # nrfastafilepath = "./all_nrtest_1000000.fa"
    # blastfilepath = "./11-hui_HFGMYALXX_L4_clean.blast"
    nrfastafilepath = args.nrfastafile
    blastfilepath = args.blastfile
    outputfile = args.gene_abundance

    Matabundance = get_gene_abundance(nrfastafilepath, blastfilepath)
    Matabundance.to_csv(outputfile, index=None, sep='\t')

# gb
# a = pd.read_csv("./gb", header=None)
# a = np.array(a)
# a = a.flatten()
# b = relative_gene_abundance
# b = np.array(b)
# a = sorted(a)
# b = sorted(b)
# a = np.array(a)
# b = np.array(b)
# Test results
# (a - b).max()
# -3.3881317890172014e-21
