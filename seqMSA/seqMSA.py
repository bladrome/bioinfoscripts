from glob import glob
from os import mkdir, path

from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline
from Bio import Align
aligner = Align.PairwiseAligner()
aligner.mode = 'local'
aligner.query_left_open_gap_score = -10
aligner.query_internal_extend_gap_score = -20

seqdatadir = r"seq"
listfile = r"primer.txt"

threshold = 55

# clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2"
clustalw_exe = r"clustalw2"


def getseqfromfile(filename):
    fastafile = [i for i in SeqIO.parse(filename, "fasta")]
    if fastafile:
        return str(fastafile[0].seq)
    else:
        return open(filename).readlines()[0]


def MSA(primernum, primername, primerseq, primerresultfile, outputdir = "MSAoutdir"):
    # print(primernum, primername, primerseq, primerresultfile)
    if not path.exists(outputdir):
        mkdir(outputdir)

    outputfilename = "{}/{}_{}_1_MSA_clustalw2.fasta".format(outputdir, primernum, primername)
    with open(outputfilename, 'w') as f:
        primerseqid = ">{},{}".format(primernum, primername)
        f.write(primerseqid)
        f.write("\n")
        f.write(primerseq)
        f.write("\n")

        results1id = ">{}".format(path.basename(primerresultfile[0]))
        results1seq = getseqfromfile(primerresultfile[0])
        f.write(results1id)
        f.write("\n")
        f.write(results1seq)
        f.write("\n")
        print(primername, end='\t')
        # print(aligner.score(primerseq, results1seq), end='\t')
        score = aligner.score(results1seq, primerseq)
        # print(score, end='\t')s
        print("√", end='\t') if score > threshold else print("×", end='\t')
    cmdline = ClustalwCommandline(clustalw_exe, infile=outputfilename)
    cmdstdout, cmdstderr = cmdline()
    #print(cmdstdout) 
    outputfilename = "{}/{}_{}_2_MSA_clustalw2.fasta".format(outputdir, primernum, primername)
    with open(outputfilename, 'w') as f:
        primerseqid = ">{},{}".format(primernum, primername)
        f.write(primerseqid)
        f.write("\n")
        f.write(primerseq)
        f.write("\n")
    
        results2id = ">{}".format(path.basename(primerresultfile[1]))
        results2seq = getseqfromfile(primerresultfile[1])
        f.write(results2id)
        f.write("\n")
        f.write(results2seq)
        f.write("\n")
        print(primername, end='\t')
        # print(aligner.score(primerseq, results1seq), end='\t')
        # print(aligner.score(results2seq, primerseq))
        score = aligner.score(results2seq, primerseq)
        # print(score, end='\t')
        print("√") if score > threshold else print("×")
    cmdline = ClustalwCommandline(clustalw_exe, infile=outputfilename)
    cmdstdout, cmdstderr = cmdline()
   # print(cmdstdout) 

def printalnout(outputdir, allalnfile="allaln.txt"):
    alnfiles = glob(outputdir + "/*aln")
    alnfiles.sort()
    with open(allalnfile, 'w') as f:
        for alnfile in alnfiles:
            f.write("".join(open(alnfile).readlines()))
    

with open(listfile) as f:
    for line in f:
        primernum, primername, primerseq = line.split()
        primerresultfilepath = path.join(seqdatadir, primernum)
        primerresultfile = glob(primerresultfilepath + "*seq")
        MSA(primernum, primername, primerseq, primerresultfile)

printalnout("MSAoutdir")
