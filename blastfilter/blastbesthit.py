import pandas as pd
import io
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("blastfile")
parser.add_argument("outputfile")
args = parser.parse_args()


# blastfile = "./nr10000.blast"

blastfile = args.blastfile
outputfile = args.outputfile


besthitdf = pd.DataFrame()

strtmp = ""
count = 0
with open(blastfile) as f:
    lastline = f.readline()
    strtmp += lastline
    for line in f:
        if line.split()[0] == lastline.split()[0]:
            strtmp += line
        else:
            # if strtmp:
            hitsdf = pd.read_table(io.StringIO(strtmp), sep='\t', header=None)
            hit = hitsdf[hitsdf[11] == hitsdf[11].min()]
            # if len(hit) != 1:
                # print(hit)
            besthitdf = besthitdf.append(hit[0:1])
            count += len(hitsdf)

            lastline = line
            # clear strtmp
            strtmp = ""
            strtmp += lastline
    hitsdf = pd.read_table(io.StringIO(strtmp), sep='\t', header=None)
    hit = hitsdf[hitsdf[11] == hitsdf[11].min()]
    # if len(hit) != 1:
        # print((hit))
    besthitdf =  besthitdf.append(hit[0:1])
    count += len(hitsdf)


besthitdf.to_csv(outputfile, header=None, sep='\t', index=None)

print(len(besthitdf))
print(count)
