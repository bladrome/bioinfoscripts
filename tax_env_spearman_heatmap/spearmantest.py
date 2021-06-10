import numpy as np
import pandas as pd
from scipy.stats import spearmanr

top = 50
for filenum in  (str(i) for i in range(1, 7)):
    envdf = pd.read_csv("spearman_analysis/index-" +  filenum + ".csv", skiprows=1)
    taxdf = pd.read_csv("spearman_analysis/microbial-" + filenum + ".csv", skiprows=1)

    taxdf.iloc[:,0] = taxdf.iloc[:,0].map(lambda x: ";".join(x.split(";")[4:6]))
    taxdf['taxsum'] = np.sum(taxdf.iloc[:,1:], axis=1)
    taxdf = taxdf.sort_values('taxsum', ascending=False)
    taxdf = taxdf.drop('taxsum', axis=1)
    taxdf = taxdf.iloc[:top, :]

    print(envdf)
    print(taxdf)

    corrdf, pvaldf = spearmanr(taxdf.iloc[:,1:], envdf.iloc[:,1:], axis=1)
    pvaldf = pd.DataFrame(pvaldf[:taxdf.shape[0], -envdf.shape[0]:], index=taxdf.iloc[:,0], columns=envdf.iloc[:,0])
    corrdf = pd.DataFrame(corrdf[:taxdf.shape[0], -envdf.shape[0]:], index=taxdf.iloc[:,0], columns=envdf.iloc[:,0])

    print(corrdf.shape)
    print(pvaldf.shape)

    corrdf.to_csv("heatmap_corrdf_"  + filenum  + ".csv")
    pvaldf.to_csv("heatmap_pvaldf_"  + filenum  + ".csv")
