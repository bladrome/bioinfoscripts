import numpy as np
import pandas as pd


def ihssmooth(filepath, windows_size=50000, step_size=10000):

    ihsdata = pd.read_table(filepath, header=None)
    ihsdata.sort_values(by=[1])

    posi_max = ihsdata[1].max()

    index_start_list = list()
    ihssmooth_list = list()
    for i in range(0, posi_max - windows_size, step_size):
        a = (i <= ihsdata[1])
        b = (ihsdata[1] < i + windows_size)
        masksubset = np.logical_and(a, b)
        windows = ihsdata[masksubset]
        index_start_list.append(i)
        ihssmooth_list.append(0 if len(windows) == 0 else
                              windows[5].sum() / len(windows))

    ihssmooth = pd.DataFrame()
    ihssmooth['chromosome'] = [
        ihsdata[0][0].split(':')[0] for i in range(len(index_start_list))
    ]
    ihssmooth['start'] = index_start_list
    ihssmooth['end'] = [i + windows_size for i in index_start_list]
    ihssmooth['ihs'] = ihssmooth_list

    return ihssmooth


def read_chromosome_list(filepath):
    chromosome_list = list()
    with open(filepath) as f:
        for i in f:
            chromosome_list.append(i.strip())

    return chromosome_list


if __name__ == "__main__":
    import sys
    from os.path import dirname
    from os.path import join
    if len(sys.argv) != 3:
        print("Usage:{0} {1} {2}".format(sys.argv[0], "sample_list",
                                         "output.csv"))
        sys.exit(1)

    ihs = pd.DataFrame()
    chr_file_dir = dirname(sys.argv[1])
    for i in read_chromosome_list(sys.argv[1]):
        ihsfile = join(chr_file_dir, i)
        chrihs = ihssmooth(ihsfile)
        ihs = ihs.append(chrihs)
    ihs.to_csv(sys.argv[2], index=False)
