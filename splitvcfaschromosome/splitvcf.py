import sys

common = list()
chromosome = dict()


def common_data(line):
    global common
    common.append(line)


def chromosome_data(chromosome_name, line):
    global chromosome
    if chromosome_name not in chromosome:
        chromosome[chromosome_name] = list()
    else:
        chromosome[chromosome_name].append(line)


def distribution(vcffile, chromosome_name_list):
    with open(vcffile) as vf:
        for l in vf:
            if l.startswith('#'):
                common_data(l)
            else:
                chr_name = l.split()[0]
                if chr_name in chromosome_name_list:
                    chromosome_data(chr_name, l)


def output(chromosome_name):
    outputfilename = "chromosome_" + chromosome_name + ".vcf"
    with open(outputfilename, 'w') as of:
        for i in common:
            of.write(i)
        for i in chromosome[chromosome_name]:
            of.write(i)

    # print(chromosome_name)
    # for i in common:
        # print(i, end='')
    # for i in chromosome[chromosome_name]:
        # print(i, end='')


chromosome_name_list = [sys.argv[i] for i in range(2, len(sys.argv))]
distribution(sys.argv[1], chromosome_name_list)
for i in chromosome_name_list:
    output(i)
