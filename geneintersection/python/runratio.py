#!/usr/bin/env python
# coding=utf-8

import os

import numpy as np

x = np.linspace(0.5, 1, 11)

print(x)

for rate in x:
    print(rate)
    cmd = "time python ./intersectGeneRegion.py {} > ratio{}".format(
        rate, rate)
    print(cmd)
    os.system(cmd)
