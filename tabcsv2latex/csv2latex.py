import pandas as pd
import os

colorstrleft = "{\color{red}"
bluecolorstrleft = "{\color{blue}"
graycolorstrleft = "{\color{gray}"
sgsepspace="\\vspace{0.5cm}"
colorstrright = "}"
sequencens_length = 25

pageheight=45
pagewidth = 12

def print_table2(csvfile):

    tmpfile = open(csvfile)
    tmpfile.readline()
    line = tmpfile.readline()
    if line != '':
        line = line.split()[1]
        sequencens_length=len(line)
    else:
        sequencens_length = 25
    tmpfile.close()

    sequencensindent = 'c' * (sequencens_length)
    sequencensindent = '@{}'.join(sequencensindent)
    tabindent = list()
    tabindent.append(sequencensindent)
    tabindent.extend(['l', 'l', 'l', 'l', 'l', 'l'])
    tabindent = ''.join(tabindent)

    samplename = csvfile.split('_')[0]
    header = namesdict[samplename] + '\\\\'
    print("\\noindent \\par ", end='')

    # print("SCVSDVSDFSDFASDF:")
    # print(csv2latextab(csvfile))
    if csv2latextab(csvfile):
        print("\\textbf{")

    print("\\textbf{")
    print(header + " " + samplename)
    print("\\\\")
    print(csvfile.replace("_", "\_"))
    # print(header)
    print("}")
    print("\\begin{tabular}{" + tabindent + "}")
    print('\\\\\n'.join(csv2latextab(csvfile)))
    print("\\end{tabular} ")

    if csv2latextab(csvfile):
        print("}")

    print(sgsepspace)

# def print_table(cscfile):
    # samplename = cscfile.split('_')[0]
    # header = samplename + "/" +  namesdict[samplename] + '\\\\'
    # print("\\noindent \\par ", end='')
    # print("\\textbf{")
    # print(header)

    # tmpfile = open(cscfile)
    # tmpfile.readline()
    # line = tmpfile.readline().split()[1]
    # sequencens_length=len(line)
    # tmpfile.close()

    # sequencensindent = 'c' * (sequencens_length)
    # sequencensindent = '@{}'.join(sequencensindent)
    # tabindent = ['c']
    # tabindent.append(sequencensindent)
    # tabindent.extend(['l', 'l', 'l', 'l', 'l'])
    # tabindent = ''.join(tabindent)

    # print("\\begin{tabular}{" + tabindent + "}")
    # # print('\\\\'.join(texitemlist))
    # print('\\\\\n'.join(csv2latextab(cscfile)))
    # print("\\end{tabular} ")
    # print("}")
    # print("\\vspace{0.2cm}")

def color_at_position(sequencens, poslist):
    '''
    # sequencens_split_index = poslist.copy()
    # sequencens_split_index.insert(0, -1)
    # sequencens_split_index.append(len(sequencens))

    # sequencens_split = [sequencens[sequencens_split_index[i] + 1:sequencens_split_index[i + 1]] for i in range(len(sequencens_split_index) - 1)]
    # # print(sequencens_split)

    # print(sequencens_split_index)

    # for pos in poslist:
        # sequencens = sequencens[0:pos] + colorstrleft +
            # sequencens[pos] + colorstrright + sequencens[pos + 1:]

    # return sequencens_split
    '''

    sequencens = [i for i in sequencens]

    sequencens[0] = graycolorstrleft + sequencens[0] + colorstrright
    sequencens[1] = graycolorstrleft + sequencens[1] + colorstrright

    sequencens[-1] = bluecolorstrleft + sequencens[-1] + colorstrright
    sequencens[-2] = bluecolorstrleft + sequencens[-2] + colorstrright
    sequencens[-3] = bluecolorstrleft + sequencens[-3] + colorstrright

    if poslist:
        for i in poslist:
            sequencens[i] = colorstrleft + sequencens[i] + colorstrright
    


    sequencens = '&'.join(sequencens)

    return sequencens

def csv2latextab(filename):
    texitemlist = list()
    sg1 = pd.read_csv(
        filename, sep='\t')

    for item in sg1.itertuples():
        # print(item)
        sequencens = item[2]
        sequencens_length=len(sequencens)

        posstr = item[7]
        posstr = posstr.strip('[]')
        if  posstr:
            poslist = [int(i) for i in posstr.split(',')]
        else:
            poslist = list()
        # print(color_at_position(sequencens, poslist))

        stritem = [str(i) for i in item][1:]
        stritem[1] = color_at_position(sequencens, poslist)
        # print(stritem)
        texitem = "&".join(stritem)
        texitemlist.append(texitem)
        # print(texitem)
    return texitemlist

# namesdict
namesdict = dict()
with open("./tt.samples.ID") as f:
    for i in f:
        i = i.strip().split()
        namesdict[i[0]] = i[1]


sequencensindent = 'c' * (sequencens_length)
sequencensindent = '@{}'.join(sequencensindent)
tabindent = ['c']
tabindent.append(sequencensindent)
tabindent.extend(['l', 'l', 'l', 'l', 'l'])
tabindent = ''.join(tabindent)

print("\
\\documentclass[10pt,a4paper]{article}\n\
\\usepackage{geometry}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{amsmath}\n\
\\usepackage{amsfonts}\n\
\\usepackage{amssymb}\n\
\\usepackage{makeidx}\n\
\\usepackage{graphicx}\n\
\\usepackage{xcolor}\n\
\\usepackage{fontspec}\n\
\\special{papersize=" + str(pagewidth) + "in," + str(pageheight) +"in}\n\
\\textwidth " + str(pagewidth-1)  + " true in\n\
\\textheight " + str(pageheight-1)  + " true in\n\
\\setlength\paperheight {" + str(pageheight) + "in}\n\
\\setlength\paperwidth {" + str(pagewidth) + "in}\n\
\\setmainfont{Courier New}\n\
\\author{blade\\_jack@163.com}\n\
\\begin{document}\n\
        ")


for cscfile in os.listdir("."):
    if cscfile.endswith("_txt.csv"):
        print_table2(cscfile)



print("\\end{document} ")

