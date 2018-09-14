#!/bin/bash


numsamples=10
#python3  generatecfg.py ./reads-for-assembly/examples/files sample conffile $numsamples
# align
referenceall=all.fa
for i in $(seq $numsamples)
do
    sample=sample_${i}
    bwa mem -t 24 -M -R '@RG\tID:${sample}\tLB:${sample}\tPL:ILLUMINA\tSM:${sample}' ${referenceall} ${sample}-R1.fastq ${sample}-R2.fastq | samtools view -Sbh - > ${sample}.bam
    samtools sort ${sample}.bam ${sample}_sorted
    samtools index ${sample}_sorted.bam
    bedtools genomecov -ibam ${sample}_sorted.bam > ${sample}_sorted.cov
    
done

