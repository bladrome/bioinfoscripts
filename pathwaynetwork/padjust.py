import numpy as np


def p_adjust_bh(p):
    """Benjamini-Hochberg p-value correction for
    multiple hypothesis testing."""
    p = np.asfarray(p)
    by_descend = p.argsort()[::-1]
    by_orig = by_descend.argsort()
    steps = float(len(p)) / np.arange(len(p), 0, -1)
    q = np.minimum(1, np.minimum.accumulate(steps * p[by_descend]))
    return q[by_orig]


def padjust(P):
    X = np.zeros_like(P)
    for i in range(P.shape[1]):
        X[i] = p_adjust_bh(P[i])

    print("adjust p value:"),
    print(X)
    return np.array(X)
