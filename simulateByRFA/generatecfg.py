# [general]
# output_sample_name = test_sample
# insert_size = 30
# insert_size_std = 1
# short_read_length = 100
# error_rate = 0.005

# [files/fasta_01.fa]
# coverage = 10

# [files/fasta_02.fa]
# coverage = 20

# [files/fasta_03.fa]
# coverage = 5

# [files/fasta_04.fa]
# coverage = 15

# [files/fasta_05.fa]
# coverage = 5

import argparse
import random
import os

insertsize = 30
insertsizestd = 10
shortreadslength = 100
errorrate = 0.005

parser = argparse.ArgumentParser()
parser.add_argument("fastadir")
parser.add_argument("samplename")
parser.add_argument("cfgname")
parser.add_argument("numsamples", type=int)
args = parser.parse_args()

fastadir = args.fastadir
samplename = args.samplename
cfgname = args.cfgname
numsamples = args.numsamples

for i in range(1, numsamples + 1):
    outputcfgfile = open("{0}_{1}".format(cfgname, i), 'w')
    print("[general]", file=outputcfgfile)
    print("output_sample_name = {0}_{1}".format(samplename, i), file=outputcfgfile)
    print("insert_size = {0}".format(insertsize), file=outputcfgfile)
    print("insert_size_std = {0}".format(insertsizestd), file=outputcfgfile)
    print("short_read_length = {0}".format(shortreadslength), file=outputcfgfile)
    print("error_rate = {0}".format(errorrate), file=outputcfgfile)
    for fastafile in os.listdir(fastadir):
        if fastafile.endswith("fa") or fastafile.endswith("fasta"):
            coverage = random.randint(1, 5)
            print("[{0}/{1}]".format(fastadir, fastafile), file=outputcfgfile)
            print("coverage = {0}".format(coverage), file=outputcfgfile)
