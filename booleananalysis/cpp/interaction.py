import numpy as np
import pandas as pd

threhold = 0.5

data = pd.read_csv("result.csv", header=None)

pos = np.where(data[data > threhold] > 0)
neg = np.where(data[data < -threhold] < 0)

posset = set(zip(pos[0], pos[1]))
negset = set(zip(neg[0], neg[1]))

print("Positive interaction")
print(posset)
print("Negative interaction")
print(negset)


