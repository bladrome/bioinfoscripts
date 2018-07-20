import pandas as pd

def blastheader():
    '''
    qseqid means Query Seq - id
    qlen means Query sequence length
    sseqid means Subject Seq - id
    sallseqid means All subject Seq - id(s), separated by a ';'
    slen means Subject sequence length
    qstart means Start of alignment in query
    qend means End of alignment in query
    sstart means Start of alignment in subject
    send means End of alignment in subject
    qseq means Aligned part of query sequence
    sseq means Aligned part of subject sequence
    evalue means Expect value
    bitscore means Bit score
    score means Raw score
    length means Alignment length
    pident means Percentage of identical matches
    nident means Number of identical matches
    mismatch means Number of mismatches
    positive means Number of positive - scoring matches
    gapopen means Number of gap openings
    gaps means Total number of gaps
    ppos means Percentage of positive - scoring matches
    qframe means Query frame
    stitle means Subject Title
    salltitles means All Subject Title(s), separated by a '<>'
    qcovhsp means Query Coverage Per HSP

    List here
    qseqid qlen sseqid sallseqid slen qstart qend sstart send qseq 
    sseq evalue bitscore score length pident nident mismatch 
    positive gapopen gaps ppos qframe stitle salltitles qcovhsp 

    '''
    header =[ 
    "qseqid", "qlen","sseqid", "sallseqid", "len", "start", "end", "start", "end", "seq", 
    "sseq", "evalue", "bitscore", "score", "length", "pident", "nident", "mismatch", 
    "positive", "gapopen", "aps", "ppos", " qframe", "stitle", "salltitles", "qcovhsp"]

    return header


def blastfilter_evalue(data):
    header = blastheader()
    data.columns = header
    evaluegrounpmin = data.groupby(['qseqid'])['evalue'].min()
    evaluegrounpmin *= 10
    evaluegrounpmin = pd.DataFrame([evaluegrounpmin.index, evaluegrounpmin.values]).T


    filteddata = pd.DataFrame()
    for item in evaluegrounpmin.itertuples(index=False):
        tmpdf = data[ (data.qseqid == item[0]) & (data.evalue < item[1]) ]
        filteddata = filteddata.append(tmpdf)

    return filteddata

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="filter diamond blast by evalue (evalue < group_min_evalue * 10)")
    parser.add_argument('blastfile', type=str)
    parser.add_argument('filtedfile', type=str)
    args = parser.parse_args()

    data = pd.read_table(args.blastfile, header=None)
    filteddata = blastfilter_evalue(data)
    filteddata.to_csv(args.filtedfile, sep='\t', index=None)
