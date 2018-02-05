
def readfafile(fafilepath):
    with open(fafilepath) as f:
        x = f.readlines()
    name = x[::2]
    seq = x[1::2]
    fafiledict = {name[i].strip()[1:]: seq[i].strip() for i in range(len(name))}

    return fafiledict

def readphylumfile(phylumfilepath):
    phylumdict = {}
    with open(phylumfilepath) as f:
        for row in f:
            x = row
            x = x.split('\t')
            x[0] = "_".join(x[0].strip("\"").split())
            value = x[0]
            key = x[1:]
            phylumdict.update({key[i]: value for i in range(len(key))})

    return phylumdict


def output():

    fa = readfafile("./11-L_HFGMYALXX_L3.unigene.fa")
    phylum = readphylumfile("./11-L_HFGMYALXX_L3.pyhum_1")

    for name, seq in fa.items():
        if name in phylum:
            print("_".join((phylum[name], name)) + "\n" + seq)

output()
