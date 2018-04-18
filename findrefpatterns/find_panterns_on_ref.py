import sys

if len(sys.argv) != 3:
    print("Usage: {0} {1} {2}".format(sys.argv[0], "reference.fa", "PATTERN"))
    sys.exit(1)

reffile = sys.argv[1]
pattern = sys.argv[2]

import re
reference=dict()
chromosome_list = list()
with open(reffile) as ref:
    current_chromosome = 0
    for line in ref:
        if line.startswith('>'):
            current_chromosome = line.strip().split('>')[1]
            chromosome_list.append(current_chromosome)
            reference[current_chromosome] = ""
        else:
            reference[current_chromosome] += (line.strip().upper())

for chromosome in chromosome_list:
    sequences = reference[chromosome]
    for i in re.finditer(pattern.upper(), sequences):
        print(chromosome, *i.span())
