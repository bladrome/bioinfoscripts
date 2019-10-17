#!/bin/bash

ASCPOPTS='-QT -l 300G -P33001'
ASCPURLPREFIX=era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq
download(){
    for f in `cat filelist`
    do
        echo ${f}
        sample_prefix=${f:0:6}/${f}/${f}
        if test ! -e ${f}_1.fastq.gz
        then
            ~/.aspera/connect/bin/ascp \
                $ASCPOPTS \
                -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh \
                $ASCPURLPREFIX/${sample_prefix}_1.fastq.gz .
        fi
        if test ! -e ${f}_2.fastq.gz
        then
            ~/.aspera/connect/bin/ascp \
                $ASCPOPTS \
                -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh \
                $ASCPURLPREFIX/${sample_prefix}_2.fastq.gz .
        fi
    done
}

main(){
    while true
    do
        download
        sleep 5
    done
}

main

#~/.aspera/connect/bin/ascp -QT -l 300m -P33001 -i ~/.aspera/connect/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:/vol1/fastq/SRR949/SRR949627/SRR949627_1.fastq.gz
