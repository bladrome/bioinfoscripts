#!/bin/bash

# Runing in docker

numsamples=10
python3  generatecfg.py ./reads-for-assembly/examples/files sample conffile $numsamples
for i in $(seq $numsamples)
do
    python3 ./reads-for-assembly/gen-paired-end-reads conffile_${i}
done
