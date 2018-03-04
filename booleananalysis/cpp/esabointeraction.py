import sys
import numpy as np
import pandas as pd


def esabo_interaction(csvfile, threhold):
    data = pd.read_csv(csvfile, header=None)

    pos = np.where(data[data > threhold] > 0)
    neg = np.where(data[data < -threhold] < 0)

    posset = set(zip(pos[0], pos[1]))
    negset = set(zip(neg[0], neg[1]))

    # print("Positive interaction")
    # print(posset)
    # print("Negative interaction")
    # print(negset)
    return posset, negset


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {0} {1}".format(sys.argv[0], "threhold"))
        sys.exit(1)
    threhold = float(sys.argv[1])
    posset, negset = esabo_interaction("./result.csv", threhold)
    print((posset, negset))
