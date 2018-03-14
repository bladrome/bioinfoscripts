import numpy as np
import pandas as pd


def sweedsmooth(filepath, windows_size=50000, step_size=10000):

    chromosome_name = filepath.split('chr')[1].split('.')[0]
    sweeddata = pd.read_table(filepath, comment='/')

    # sweeddata.Position = sweeddata.Position.astype(int, copy=False)
    # Add 5 seconds on chr1 and ch2 dataset
    sweeddata.sort_values(by=['Position'])
    posi_max = sweeddata.Position.max()

    start = list()
    sweedsmooth_list = list()

    for i in range(0, int(posi_max) - windows_size, step_size):
        a = i <= sweeddata.Position
        b = sweeddata.Position < i + windows_size
        masksubset = np.logical_and(a, b)
        windows = sweeddata[masksubset]
        start.append(i)
        sweedsmooth_list.append(0 if len(windows) == 0 else
                                windows.Alpha.sum() / len(windows))

    sweedsmooth = pd.DataFrame()
    sweedsmooth['chromosome'] = [
        chromosome_name for i in range(len(sweedsmooth_list))
    ]
    sweedsmooth['start'] = start
    sweedsmooth['end'] = [i + windows_size for i in start]
    sweedsmooth['sweed'] = sweedsmooth_list

    return sweedsmooth


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
        print("Usage: {0} {1} {2}".format(sys.argv, "sample_list",
                                          "output.csv"))
        sys.exit(1)

    sweed = pd.DataFrame()
    chr_file_dir = dirname(sys.argv[1])
    for i in read_chromosome_list(sys.argv[1]):
        sweedfile = join(chr_file_dir, i)
        chrsweed = sweedsmooth(sweedfile)
        sweed = sweed.append(chrsweed)
    sweed.to_csv(sys.argv[2], index=False)
