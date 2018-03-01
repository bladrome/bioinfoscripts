import numpy as np
import os
import cpp.esabointeraction as esabo
import correlation.corrinteraction as corr

# arguments:

# ESABO:
# binary_threhold: (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)
# interaction_threhold: (0.5, 1, 1.5, 2)
binary_threhold = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6)
entropy_threhold = (0.5, 1, 1.5, 2)

# spearmanr:
# pvalue_threhold: (1e-1, 5e-2)
pvalue_threhold = (1e-2, 5e-2)
coef_threhold = (0.2, 0.3, 0.4, 0.5)

csvfile = "./journal.pgen.1005846.s011.csv"
esabo_bin = "./cpp/esabo"


def jaccard_similarity(a, b):
    return 0.0 if len(a | b) == 0 else float(len(a & b)) / len(a | b)


pos_jaccard_index = []
neg_jaccard_index = []
for binary in binary_threhold:
    for entropy in entropy_threhold:
        esabo_cmd = esabo_bin + " " + csvfile + " {0}".format(binary) +\
                                " ./esaboresult.csv"
        os.system(esabo_cmd)
        esabo_posset, esabo_negset =\
            esabo.esabo_interaction("./esaboresult.csv", entropy)

        for pvalue in pvalue_threhold:
            for coef in coef_threhold:
                corr_posset, corr_negset =\
                    corr.coef_interaction(csvfile, pvalue, coef)

                # print(binary, entropy, pvalue, coef),
                print("{0} {1} {2} {3}".format(
                    len(esabo_posset),
                    len(esabo_negset),
                    len(corr_posset),
                    len(corr_negset))),
                pji = jaccard_similarity(esabo_posset, corr_posset)
                print("positive:{0}".format(pji))
                nji = jaccard_similarity(esabo_negset, corr_negset)
                print("negative:{0}".format(nji))

                pos_jaccard_index.append(pji)
                neg_jaccard_index.append(nji)

pos_jaccard_index = np.array(pos_jaccard_index)
neg_jaccard_index = np.array(neg_jaccard_index)
print(pos_jaccard_index)
print(neg_jaccard_index)
