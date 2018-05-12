#!/bin/bash

#sg1 6:95419471
#sg2 6:95419482
#sg3 6:95419548
#sg4 6:95419282

referencefa=/media/bladrome/drome/Biodata/ASMreference/ASM.fa
#pos="6:95419275"
#bamfile=./test/AWGBGAA05771-2-35.bam
pos="6:95419280"
interestlen=25

generate_csv(){

    for bamfile in `ls *.bam`
        #for bamfile in `ls ./AWGBGAA05774-2-38.bam`
    do
        pos="6:95419469"
        bash ./run_tview_composition_filter.sh ${referencefa} ${bamfile} ${pos} ${interestlen}
        pos="6:95419480"
        bash ./run_tview_composition_filter.sh ${referencefa} ${bamfile} ${pos} ${interestlen}
        pos="6:95419546"
        bash ./run_tview_composition_filter.sh ${referencefa} ${bamfile} ${pos} ${interestlen}
        pos="6:95419280"
        bash ./run_tview_composition_filter.sh ${referencefa} ${bamfile} ${pos} ${interestlen}
    done

}


python ./csv2latex.py > ./latexfiles/document.tex &&  cd latexfiles && xelatex document.tex && evince document.pdf && cd .. &
python ./goodscv2latex.py > ./latexfiles/gooddocument.tex && cd latexfiles && xelatex gooddocument.tex && evince gooddocument.pdf && cd .. &
