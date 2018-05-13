import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: {0} {1} {2}".format(sys.argv), "VCFfile", "MQ_threshold")
    sys.exit(1)

samplename = sys.argv[1]
threshold = float(sys.argv[2])

vcfdata = pd.read_table(samplename, header=None)

descriptioncol = vcfdata[7]

mqscorelist = list()
for i in descriptioncol:
    i = i.split(';')
    mqscore = [mq for mq in i if mq.startswith("MQ=")]
    if not mqscore:
        mqscore = ['MQ=0']
    mqscore = float(mqscore[0].split("=")[1])
    mqscorelist.append(mqscore)

mqscoreSeries = pd.Series(mqscorelist)
vcfdata = vcfdata[mqscoreSeries > float(threshold)]
vcfdata.to_csv(
    samplename.split('/')[-1].split('.')[0] + "_filter_MQ_" + str(round(threshold)) + ".vcf",
    header=None,
    sep='\t')
