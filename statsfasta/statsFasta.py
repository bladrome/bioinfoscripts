def stats_fasta(args):
    fastafile = args.fastafile
    outputfile = args.output_table
    fastafile = SeqIO.parse(fastafile, format="fasta")
    outputitem = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format("fastaid", "length",
                                                       "#A", "#T", "#T", "#C")
    print(outputitem, file=outputfile)
    for item in fastafile:
        # print(item.id)
        # print(item.seq)
        # print(item.description)
        iddescription = str(item.description)
        iddescription = iddescription.replace(" ", '_')
        seqlength = len(item.seq)
        outputitem = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(
            iddescription, seqlength, item.seq.count("A"), item.seq.count("T"),
            item.seq.count("G"), item.seq.count("C"))
        print(outputitem, file=outputfile)


if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("fastafile")
    parser.add_argument(
        "-o", "--output", dest="output_table", type=argparse.FileType('w'))
    args = parser.parse_args()
    # fastafilepath = "/media/bladrome/drome/Biodata/contigs/11-hui_HFGMYALXX_L4_clean.contigs.fa"
    from Bio import SeqIO
    stats_fasta(args)
