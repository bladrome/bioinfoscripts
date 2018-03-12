import pandas as pd
import numpy as np


def read_sample_list(samplelistfilepath):
    sample_list = list()
    with open(samplelistfilepath) as f:
        for sample in f:
            sample_list.append(sample.strip())

    return sample_list


def get_probobility_list(vcfsample):
    zerolist = list()
    onelist = list()
    for line in vcfdata.iterrows():
        none = 0
        nzero = 0
        for site in line[1]:
            number = site.split(':')[0]
            number = number.split('/')
            if number[0] == '1':
                none += 1
            elif number[0] == '0':
                nzero += 1
            if number[1] == '1':
                none += 1
            elif number[1] == '0':
                nzero += 1
        sum_one_zero = none + nzero
        if sum_one_zero == 0:
            sum_one_zero = 1
        zerolist.append(float(nzero) / sum_one_zero)
        onelist.append(float(none) / sum_one_zero)

    return onelist, zerolist


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: {0} {1} {2} {3}".format(sys.argv[0],
                                              "vcffile",
                                              "sample_list",
                                              "output.csv"))
    sample_list = read_sample_list(sys.argv[2])
    chr_pos = ['#CHROM', 'POS']
    chr_pos.extend(sample_list)
    output_list = chr_pos

    vcfdata = pd.read_table(sys.argv[1])
    outputdata = pd.DataFrame()
    outputdata['chromosome'] = vcfdata['#CHROM']
    outputdata['position'] = vcfdata['POS']

    vcfdata = vcfdata[sample_list]
    sampledata = vcfdata[sample_list]
    majorallele, minorallele = get_probobility_list(sampledata)
    outputdata['one_ratio'] = majorallele
    outputdata['zero_ratio'] = minorallele
    dropzero = np.logical_not(np.logical_and(outputdata.one_ratio == 1,
                                             outputdata.zero_ratio == 0))
    outputdata = outputdata[dropzero]
    outputdata.to_csv(sys.argv[3], index=False)
