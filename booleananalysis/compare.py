import os

# arguments:

# ESABO:
# binary_threhold: (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)
# interaction_threhold: (0.5, 1, 1.5, 2)

# spearmanr:
# pvalue_threhold: (1e-1, 5e-2)
# coef_threhold: (3, 3.5, 4, 4.5, 5)

binary_threhold = (1e-1, 1e-2, 1e-3, 1e-4, 1e-5)
interaction_threhold = (0.5, 1, 1.5, 2)

pvalue_threhold = (1e-1, 5e-2)
coef_threhold = (3, 3.5, 4, 4.5, 5)

esabo_cmd = "./cpp/esabo"


def run(argc):
    print("argc {0}".format(argc))



for i in range(100):
    os.system("echo abc")
