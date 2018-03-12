import pandas as pd


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
    outputdata['CHROM'] = vcfdata['#CHROM']
    outputdata['POS'] = vcfdata['POS']

    vcfdata = vcfdata[sample_list]
    sampledata = vcfdata[sample_list]
    majorallele, minorallele = get_probobility_list(sampledata)
    outputdata['one_ratio'] = majorallele
    outputdata['zero_ratio'] = minorallele
    outputdata.to_csv(sys.argv[3], index=False)
