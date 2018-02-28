import cpp.esabointeraction as esabo
import correlation.corrinteraction as corr
import os

# arguments:

# ESABO:
# binary_threhold: (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)
# interaction_threhold: (0.5, 1, 1.5, 2)
binary_threhold = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)
entropy_threhold = (0.5, 1, 1.5, 2)

# spearmanr:
# pvalue_threhold: (1e-1, 5e-2)
pvalue_threhold = (1e-1, 5e-2)
coef_threhold = (3, 3.5, 4, 4.5, 5)

csvfile = "./abundance.csv"
esabo_bin = "./cpp/esabo"


def jaccard_similarity(a, b):
    return 0 if len(a | b) == 0 else float(len(a & b)) / len(a | b)


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

                print(binary, entropy, pvalue, coef),
                print("positive:{0}".format(
                    jaccard_similarity(esabo_posset, corr_posset)))
                print("negative:{0}".format(
                    jaccard_similarity(esabo_negset, corr_negset)))
