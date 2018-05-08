import pandas as pd
import os
import re

resg1 = re.compile(".*sgRNA1.*")
resg2 = re.compile(".*sgRNA2.*")
resg3 = re.compile(".*sgRNA3.*")
resg4 = re.compile(".*sgRNA4.*")

colorstrleft = "{\color{red}"
colorstrright = "}"
sequencens_length = 30

pageheight=60
pagewidth =10

sgsepspace="\\vspace{0.5cm}"


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

    if poslist:
        sequencens = [i for i in sequencens]
        for i in poslist:
            sequencens[i] = colorstrleft + sequencens[i] + colorstrright

    sequencens = '&'.join(sequencens)

    return sequencens

def csv2latextab(filename):
    texitemlist = list()
    sg1 = pd.read_csv(
        filename, sep='\t')
    sg1 = sg1[ sg1[' .3'] != 0 ]

    for item in sg1.itertuples():
        sequencens = item[2]

        posstr = item[7]
        posstr = posstr.strip('[]')
        if  posstr:
            poslist = [int(i) for i in posstr.split(',')]
        else:
            poslist = list()
        # print(color_at_position(sequencens, poslist))

        # print(item)
        stritem = list()
        stritem.append(color_at_position(sequencens, poslist))
        stritem.append(str(round(item[4])))
        texitem = "&".join(stritem)
        texitemlist.append(texitem)
                        
    return texitemlist

# namesdict
namesdict = dict()
with open("./tt.samples.ID") as f:
    for i in f:
        i = i.strip().split()
        namesdict[i[0]] = i[1]

sequencensindent = 'c' * (sequencens_length)
sequencensindent = '@{}'.join(sequencensindent)
# print(sequencensindent)
# tabindent = ['c'] * (len(sg1.columns) - 1)
# tabindent.insert(1, sequencensindent)
# tabindent = ''.join(tabindent)
tabindent = list()
tabindent.append(sequencensindent)
tabindent.extend(['l'])
tabindent = ''.join(tabindent)


# print(csv2latextab("./AWGBGAA05771-2-35.bam.sgRNA1.tview.bam.txt.csv.ok2.csv"))

def main():
    print("\
\\documentclass[12pt,a4paper]{article}\n\
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
\\setmainfont{Arial}\n\
\\author{blade\\_jack@163.com}\n\
\\begin{document}\n\
            ")

    csvfiles = os.listdir(".")


    print("\\noindent \\par {\\large sgRNA1}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('csv') and resg1.match(csvfile):
            samplename = csvfile.split('.')[0]
            header = namesdict[samplename] + '\\\\'
            print("\\noindent \\par ", end='')
            print(header)
            print("\\begin{tabular}{" + tabindent + "}")
            # print('\\\\'.join(texitemlist))
            print('\\\\'.join(csv2latextab(csvfile)))
            print("\\end{tabular} ")
            print(sgsepspace)
    
    print("\\noindent \\par {\\large sgRNA2}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('csv') and resg2.match(csvfile):
            samplename = csvfile.split('.')[0]
            header = namesdict[samplename] + '\\\\'
            print("\\noindent \\par ", end='')
            print(header)
            print("\\begin{tabular}{" + tabindent + "}")
            # print('\\\\'.join(texitemlist))
            print('\\\\'.join(csv2latextab(csvfile)))
            print("\\end{tabular} ")
            print(sgsepspace)


    print("\\noindent \\par {\\large sgRNA3}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('csv') and resg3.match(csvfile):
            samplename = csvfile.split('.')[0]
            header = namesdict[samplename] + '\\\\'
            print("\\noindent \\par ", end='')
            print(header)
            print("\\begin{tabular}{" + tabindent + "}")
            # print('\\\\'.join(texitemlist))
            print('\\\\'.join(csv2latextab(csvfile)))
            print("\\end{tabular} ")
            print(sgsepspace)

    print("\\noindent \\par {\\large sgRNA4}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('csv') and resg4.match(csvfile):
            samplename = csvfile.split('.')[0]
            header = namesdict[samplename] + '\\\\'
            print("\\noindent \\par ", end='')
            print(header)
            print("\\begin{tabular}{" + tabindent + "}")
            # print('\\\\'.join(texitemlist))
            print('\\\\'.join(csv2latextab(csvfile)))
            print("\\end{tabular} ")
            print(sgsepspace)

    print("\\end{document} ")
main()
