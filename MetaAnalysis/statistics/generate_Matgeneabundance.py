import pandas as pd
from os import listdir
from os import popen


def get_genesname_list(genefiledir):
    pfile = popen("cut -d '\t' -f 1 " + genefiledir + "*.csv" + " | sort | uniq")
    df = pd.read_csv(pfile, header=None)
    df = df[df[0] != 'name']
    df.columns = ['genenames']

    return df


geneabundancedir="./"
Matgeneabundance = get_genesname_list(geneabundancedir)

for samplega in listdir(geneabundancedir):
    if samplega.endswith("csv"):
        df = pd.read_csv(samplega, sep='\t')
        print(len(df))
        newcol = samplega.split(".")[0]
        Matgeneabundance[newcol] = 0
        print("Next:")
        print(sum(Matgeneabundance.genenames.isin(df.name.tolist())))
        Matgeneabundance.at[Matgeneabundance.genenames.isin(df.name.tolist()), newcol] = df.aboundance
        # Matgeneabundance[Matgeneabundance.name.isin(df.name.tolist())][newcol] = df.aboundance
        # print(df.head())
        # print(Matgeneabundance.head())

geneabulist = Matgeneabundance[ Matgeneabundance.columns.tolist()[1:] ].sum(axis=1)
Matgeneabundance['rowsum'] = geneabulist
Matgeneabundance.sort_values(by=['rowsum'], ascending=False)
Matgeneabundance.to_csv("abc.csv", index=None)
