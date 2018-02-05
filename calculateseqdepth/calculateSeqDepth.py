"""
jkfasdl;
"""
import os
import re

region_length = 1000

CHR_depth_dict = {}
# infilename = "./sample.discordants.bam"
infilename = "./samhead1"
# filein = open(infile)
chr_list = [str(i + 1) for i in range(29)]
filein = os.popen('samtools view {0}'.format(infilename))
for read in filein:
    read = read.strip('\n').split('\t')
    POS = read[3]
    CHR = read[2]
    if CHR not in chr_list:
        continue
    MQ = int(read[4])
    if MQ < 20:
        continue
    else:
        # sum_of_seq = sum([int(x) for x in re.findall('\d+', read[5])])
        sum_of_seq = 150
        if CHR not in CHR_depth_dict:
            CHR_depth_dict[CHR] = {}
        n_10k = str((int(POS)) / region_length)
        print(n_10k)
        if n_10k not in CHR_depth_dict[CHR]:
            CHR_depth_dict[CHR][n_10k] = 0
        CHR_depth_dict[CHR][n_10k] += sum_of_seq

for key1, value1 in sorted(CHR_depth_dict.items(), key=lambda x: x[1]):
    for key2, value2 in value1.items():
        # if value2 / region_length > 1:
            # print(key1, key2, value2/region_length)
        print(key1, key2, value2)
