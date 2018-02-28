import sys
import numpy as np
import scipy.stats as stats
import pandas as pd


def coef_interaction(csvfile, pvalue_threhold, coef_threhold):
    data = pd.read_csv(csvfile, header=None)
    coef, pvalue = stats.spearmanr(data, axis=0)
    coef = pd.DataFrame(coef)

    # pvlaue cutoff
    coef[pvalue > pvalue_threhold] = 0

    # coef cutoff
    pos = np.where(coef[coef > coef_threhold] > 0)
    neg = np.where(coef[coef < -coef_threhold] < 0)

    posset = set(zip(pos[0], pos[1]))
    negset = set(zip(neg[0], neg[1]))

    # print("Positive interaction")
    # print(posset)
    # print("Negative interaction")
    # print(negset)

    return posset, negset




if __name__ == "__main__":

    def print_usage():
        print("Usage:{0} {1} {2} {3}".format(sys.argv[0],
              "csvfile", "pvalue_threhold", "ceof_threhold"))

    pvalue_threhold = 0.05
    coef_threhold = 0.5
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)
    elif len(sys.argv) == 3:
        pvalue_threhold = float(sys.argv[2])
    elif len(sys.argv) == 4:
        pvalue_threhold = float(sys.argv[2])
        coef_threhold = float(sys.argv[3])

    print("pvalue_cutoff:{0}".format(pvalue_threhold))
    print("coef_cutoff:{0}".format(coef_threhold))
    coef_interaction(sys.argv[1], pvalue_threhold, coef_threhold)
