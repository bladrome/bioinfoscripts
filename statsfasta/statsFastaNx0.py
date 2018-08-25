def get_fasta_length(args):
    fastafile = args.fastafile
    fastafile = SeqIO.parse(fastafile, format="fasta")

    seqlengthlist = list()
    for item in fastafile:
        seqlength = len(item.seq)
        seqlengthlist.append(seqlength)

    return seqlengthlist


if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("fastafile")
    parser.add_argument("-l", dest="len_threshold", nargs='?', type=int, default=100)
    parser.add_argument(
        "-o",
        "--output",
        dest="outputfile",
        type=argparse.FileType('w'))
    args = parser.parse_args()
    lenthreshold = args.len_threshold
    # fastafilepath = "/media/bladrome/drome/Biodata/contigs/11-hui_HFGMYALXX_L4_clean.contigs.fa"
    import pandas as pd
    from Bio import SeqIO
    lengths = pd.Series(get_fasta_length(args))
    length_cuts = lengths[lengths > lenthreshold]
    length_cuts = length_cuts.sort_values(ascending=False)
    lensum = length_cuts.sum()
    cumsum = length_cuts.cumsum()
    Nx0 = cumsum / lensum
    print("-" * 30)
    print("Summary:")
    print("Sum length:\t{0}".format(lensum))
    print("# of seq:\t{0}".format(len(length_cuts)))
    print("Avg length:\t{0}".format(lensum / len(length_cuts)))
    print(length_cuts.describe())
    print("-" * 30)
    print("Nx0")
    for n in pd.np.arange(0.0, 1.1, 0.05):
        for item in Nx0.iteritems():
            if item[1] >= n:
                print("N{0}\t{1}".format(int(n * 100), length_cuts[item[0]]))
                break
