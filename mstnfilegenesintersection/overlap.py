import sys

import numpy as np
import pandas as pd

if len(sys.argv) != 4:
    print("Usage: {0} {1} {2} {3}".format(sys.argv[0], "MSTN_file1.txt",
                                          "MSTN_file2.txt", "output.csv"))
    sys.exit(1)

a = pd.read_table(sys.argv[1], header=None)
a = a.sort_values(by=[1])
a['a_end'] = a[2] + 23
a = a.rename(columns={1: 'chromosome'})
a = a.rename(columns={2: 'a_start'})

b = pd.read_table(sys.argv[2])
b['chromosome'] = [i.split(':')[0] for i in b['# Location']]
b['b_start'] = [i.split(':')[1].split('-')[0] for i in b['# Location']]
b['b_end'] = [i.split(':')[1].split('-')[1] for i in b['# Location']]
b.b_start = b.b_start.astype(int)
b.b_end = b.b_end.astype(int)

c = a.merge(b, on=['chromosome'])

max_start = np.max((c.a_start, c.b_start), axis=0)
min_end = np.min((c.a_end, c.b_end), axis=0)
overlaplength = min_end - max_start
subsetmask = overlaplength > 0

c['intersection_start'] = max_start
c['intersecton_end'] = min_end
c['overlaplength'] = overlaplength

c = c[subsetmask > 0]

c.to_csv(sys.argv[3], index=None)
