import numpy as np
import csv

def readdata(filepath):
    X = list()
    with open(filepath) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            X.append(row)

    return np.array(X, dtype=np.float64)

XBH = readdata("./BH.csv")
XBL = readdata("./BL.csv")
XEH = readdata("./esabo_high.csv")
XEL = readdata("./esabo_low.csv")

# print(XBH)
# print(XBL)
# print(XEH)
# print(XEL)

spearman_coef_threshold = 0.3
esabo_score_threshold = 0

XBLset = set(tuple(map(tuple, np.argwhere(np.abs(XBL) > spearman_coef_threshold))))
XBHset = set(tuple(map(tuple, np.argwhere(np.abs(XBH) > spearman_coef_threshold))))
XELset = set(tuple(map(tuple, np.argwhere(np.abs(XEL) > esabo_score_threshold))))
XEHset = set(tuple(map(tuple, np.argwhere(np.abs(XEH) > esabo_score_threshold))))

# print(len(XBLset))
# print(len(XBHset))
# print(len(XELset))
# print(len(XEHset))

# print(len(XBLset.intersection(XELset)))
# print(len(XBHset.intersection(XEHset)))

XBLPset = set(tuple(map(tuple, np.argwhere((XBL) > +spearman_coef_threshold))))
XBLNset = set(tuple(map(tuple, np.argwhere((XBL) < -spearman_coef_threshold))))

XBHPset = set(tuple(map(tuple, np.argwhere((XBH) > +spearman_coef_threshold))))
XBHNset = set(tuple(map(tuple, np.argwhere((XBH) < -spearman_coef_threshold))))

XELPset = set(tuple(map(tuple, np.argwhere((XEL) > +esabo_score_threshold))))
XELNset = set(tuple(map(tuple, np.argwhere((XEL) < -esabo_score_threshold))))

XEHPset = set(tuple(map(tuple, np.argwhere((XEH) > +esabo_score_threshold))))
XEHNset = set(tuple(map(tuple, np.argwhere((XEH) < -esabo_score_threshold))))



print("### Group Low")
print("Positive interaction:")
print("\t" + str(len((XBLPset.intersection(XELPset)))))
print("\tXBLP:" + str(len(XBLPset)) + "\tXELP:" + str(len(XELPset)))
print("Negative interaction:")
print("\t" + str(len(XBLNset.intersection(XELNset))))
print("\tXBLN:" + str(len(XBLNset)) + "\tXELN:" + str(len(XELNset)))

print("### Group High")
print("Positive interaction:")
print("\t" + str(len((XBHPset.intersection(XEHPset)))))
print("\tXBHP:" + str(len(XBHPset)) + "\tXEHP:" + str(len(XEHPset)))
print("Negative interaction:")
print("\t" + str(len(XBHNset.intersection(XEHNset))))
print("\tXBHN:" + str(len(XBHNset)) + "\tXEHN:" + str(len(XEHNset)))




