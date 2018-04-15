import sys

intputfile = sys.argv[1]
outputfile1 = intputfile + "_1.fa"
outputfile2 = intputfile + "_2.fa"
with open(intputfile) as fr:
    with open(outputfile1, "w") as fw1:
        with open(outputfile2, "w") as fw2:
            for line in fr:
                if line.startswith('>') and line.endswith("1\n"):
                    line += (fr.readline())
                    fw1.write(line)
                else:
                    line += (fr.readline())
                    fw2.write(line)
