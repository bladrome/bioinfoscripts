#!/bin/bash


if [ ! -e all.hmm.ps.len ]
then
    wget http://csbl.bmb.uga.edu/dbCAN/download/all.hmm.ps.len
fi

if [ ! -e dbCAN-fam-HMMs.txt ]
then
    wget http://csbl.bmb.uga.edu/dbCAN/download/dbCAN-fam-HMMs.txt
fi

if [ ! -e hmmscan-parser.sh ]
then
    wget http://csbl.bmb.uga.edu/dbCAN/download/hmmscan-parser.sh
    chmod 755 hmmscan-parser.sh
fi


if [ -e *.h3f ]
then
    rm dbCAN-fam-HMMs.txt.h3f
fi
if [ -e *.h3i ]
then
    rm dbCAN-fam-HMMs.txt.h3i
fi
if [ -e *.h3m ]
then
    rm dbCAN-fam-HMMs.txt.h3m
fi
if [ -e *.h3p ]
then
    rm dbCAN-fam-HMMs.txt.h3p
fi

hmmerbin/hmmpress dbCAN-fam-HMMs.txt

hmmerbin/hmmscan --domtblout $1.out.dm dbCAN-fam-HMMs.txt $1 > $1.dbCAN

sh hmmscan-parser.sh $1.out.dm > $1.annotation
