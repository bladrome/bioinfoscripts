import sys

if len(sys.argv) != 3:
    print("Usage: {0} {1} {2}".format(sys.argv[0], "originalfile",
                                      "outputfile"))
    sys.exit(1)

with open(sys.argv[1], 'r') as fr:
    with open(sys.argv[2], 'w') as fw:
        # for j in (i.split()[0]+('\n') if i.startswith('>') else i for i in fr):fw.write(j)
        for i in fr:
            if i.startswith('>'):
                i = i.split()[0] + '\n'
            else:
                pass
            fw.write(i)
