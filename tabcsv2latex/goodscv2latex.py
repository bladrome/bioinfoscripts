import pandas as pd
import os
import re

resg1 = re.compile(".*469.*")
resg2 = re.compile(".*480.*")
resg3 = re.compile(".*546.*")
resg4 = re.compile(".*280.*")

colorstrleft = "{\color{red}"
bluecolorstrleft = "{\color{blue}"
graycolorstrleft = "{\color{gray}"
colorstrright = "}"

sequencens_length = 25

pageheight= 80
pagewidth = 30

sgsepspace="\\vspace{0.5cm}"

def print_table(csvfile):

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
    tabindent.extend(['l'])
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
\\setmainfont{Courier New}\n\
\\author{blade\\_jack@163.com}\n\
\\begin{document}\n\
            ")

    # csvfiles = os.listdir(".")
    csvfiles = [
"AWGBGAA05771-2-35_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05771-2-35_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05771-2-35_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05771-2-35_bam_tviw_6_95419280_txt_filter.csv",
    
"AWGBGAA05772-2-36_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05772-2-36_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05772-2-36_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05772-2-36_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05773-2-37_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05773-2-37_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05773-2-37_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05773-2-37_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05782-4-38_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05782-4-38_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05782-4-38_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05782-4-38_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05780-4-36_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05780-4-36_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05780-4-36_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05780-4-36_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05781-4-37_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05781-4-37_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05781-4-37_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05781-4-37_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05775-3-35_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05775-3-35_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05775-3-35_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05775-3-35_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05777-3-37_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05777-3-37_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05777-3-37_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05777-3-37_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05778-3-38_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05778-3-38_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05778-3-38_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05778-3-38_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05776-3-36_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05776-3-36_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05776-3-36_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05776-3-36_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05779-4-35_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05779-4-35_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05779-4-35_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05779-4-35_bam_tviw_6_95419280_txt_filter.csv",
   
"AWGBGAA05774-2-38_bam_tviw_6_95419469_txt_filter.csv",
"AWGBGAA05774-2-38_bam_tviw_6_95419480_txt_filter.csv",
"AWGBGAA05774-2-38_bam_tviw_6_95419546_txt_filter.csv",
"AWGBGAA05774-2-38_bam_tviw_6_95419280_txt_filter.csv",

            ]

    print("\\noindent \\par {\\large sgRNA1}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('filter.csv') and resg1.match(csvfile):
            print_table(csvfile)
    
    print("\\noindent \\par {\\large sgRNA2}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('filter.csv') and resg2.match(csvfile):
            print_table(csvfile)


    print("\\noindent \\par {\\large sgRNA3}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('filter.csv') and resg3.match(csvfile):
            print_table(csvfile)

    print("\\noindent \\par {\\large sgRNA4}\\")
    for csvfile in csvfiles:
        if csvfile.endswith('filter.csv') and resg4.match(csvfile):
            print_table(csvfile)

    print("\\end{document} ")
main()

