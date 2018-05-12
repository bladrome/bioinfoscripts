#!/bin/bash

SAMTOOLS=./samtools
PYTHON=python
COMPOSITIONFILTERPY=./tview_composition_filter.py

#referencefa=/media/bladrome/drome/Biodata/ASMreference/ASM.fa
#bamfile=./AWGBGAA05771-2-35.bam
#pos="6:95419275"
#interestlen=30

sort_index_bam(){
    bamfile=$1

    ${SAMTOOLS} sort ${bamfile} -o ${bamfile}
    ${SAMTOOLS} index ${bamfile}
}

sam_tview_to_txt(){
    pos=$1
    bamfile=$2
    referencefa=$3
    output=$4

    echo "${SAMTOOLS} tview -d T -p ${pos} ${bamfile} ${referencefa} > ${output}"
    ${SAMTOOLS} tview -d T -p ${pos} ${bamfile} ${referencefa} > ${output}
}


composition_filter(){
    referenceseq=$1
    tviewtxtfile=$2
    output=$3

    echo "${PYTHON} ${COMPOSITIONFILTERPY} ${referenceseq} ${tviewtxtfile} ${output}"
    ${PYTHON} ${COMPOSITIONFILTERPY} ${referenceseq} ${tviewtxtfile} ${output}
}


#referenceseq=TGGAGCAGAGCAGCTTCCAGTGG 

main(){

    referencefa=$1
    bamfile=$2
    pos=$3
    interestlen=$4

    tviewoutput=${bamfile##*/}
    tviewoutput=${tviewoutput//./_}_tviw_${pos/:/_}.txt
    compositionfilteroutput=${tviewoutput//./_}.csv

    if [ ! -e ${bamfile}.bai ]
    then
        sort_index_bam ${bamfile}
    fi

    sam_tview_to_txt $pos $bamfile $referencefa $tviewoutput
    referenceseq=$(head -n 2 ${tviewoutput} | tail -n 1)
    lenreferenceseq=$(echo ${referenceseq:0:${interestlen}} | tr -cd '*' | wc -c)
    echo ${lenreferenceseq}
    echo ${interestlen}
    if [ ${lenreferenceseq} -gt 0 ]
    then
        i=0
        while((i < interestlen))
        do
            if [ ${referenceseq:$i:$((i+1))} == '*' ]
            then
                echo ${referenceseq:$i:$((i+1))}
                referenceseq=${referencefa:0:$i}*${referenceseq:$i}
            fi
            ((i=i+1))
        done
    fi
    lenreferenceseq=$((interestlen+lenreferenceseq))
    referenceseq=${referenceseq:0:$lenreferenceseq}
    composition_filter ${referenceseq} ${tviewoutput} ${compositionfilteroutput}

}

referencefa=$1
bamfile=$2
pos=$3
interestlen=$4

main ${referencefa} ${bamfile} ${pos} ${interestlen}
