# annotaion_genenames
## Run
Usage:annotaion_genenames.py fst_file gff_file chr_list
## gffread.py
return gffdata dataframe
##  annotaion_genenames.py
### steps
- read
- filter
- merge
- filter
- to_csv
## file format
1. fst_file
>   CHROM	BIN_START	BIN_END	N_VARIANTS	WEIGHTED_FST	MEAN_FST	V7
    1	1	50000	277	0.0180669	0.0122867	0.62292850701185
    1	10001	60000	310	0.0200716	0.0132517	0.699722259261611
    1	20001	70000	345	0.0135304	0.00898398	0.449149459233607
    1	30001	80000	344	0.0113693	0.00631634	0.366364514859407
    1	40001	90000	353	0.000311578	-0.00175141	-0.0572220385973388
    1	50001	100000	359	-0.00426312	-0.00495997	-0.232464331623467
    1	60001	110000	395	-0.0104346	-0.011306	-0.468874321215106
    1	70001	120000	415	-0.00941871	-0.0136693	-0.429958770273314
    1	80001	130000	425	-0.00463959	-0.0106566	-0.246885713331188
2. gff_file
> \##gff-version 3
\#!gff-spec-version 1.21
\#!processor NCBI annotwriter
\#!genome-build ASM170441v1
\#!genome-build-accession NCBI_Assembly:GCF_001704415.1
\##sequence-region NC_030808.1 1 157403528
\##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=9925
    1	RefSeq	region	1	157403528	.	+	.	ID=id0;Dbxref=taxon:9925;Name=1;breed=San Clemente;chromosome=1;dev-stage=adult;gbkey=Src;genome=chromosome;mol_type=genomic DNA;sex=male;tissue-type=blood
    1	tRNAscan-SE	gene	60028	60099	.	+	.	ID=gene0;Dbxref=GeneID:108636924;Name=TRNAC-GCA;gbkey=Gene;gene=TRNAC-GCA;gene_biotype=tRNA
    1	tRNAscan-SE	tRNA	60028	60099	.	+	.	ID=rna0;Parent=gene0;Dbxref=GeneID:108636924;Note=transfer RNA cysteine (anticodon GCA);anticodon=(pos:60061..60063);gbkey=tRNA;gene=TRNAC-GCA;product=tRNA-Cys
    1	tRNAscan-SE	exon	60028	60099	.	+	.	ID=id1;Parent=rna0;Dbxref=GeneID:108636924;Note=transfer RNA cysteine (anticodon GCA);anticodon=(pos:60061..60063);gbkey=tRNA;gene=TRNAC-GCA;product=tRNA-Cys
    1	Gnomon	gene	72191	79644	.	+	.	ID=gene1;Dbxref=GeneID:102170632;Name=ATP5O;gbkey=Gene;gene=ATP5O;gene_biotype=protein_coding
    1	Gnomon	mRNA	72191	79644	.	+	.	ID=rna1;Parent=gene1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;Name=XM_005674665.3;gbkey=mRNA;gene=ATP5O;model_evidence=Supporting evidence includes similarity to: 13 mRNAs%2C 448 ESTs%2C 3 Proteins%2C and 99%25 coverage of the annotated genomic feature by RNAseq alignments%2C including 36 samples with support for all annotated introns;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
    1	Gnomon	exon	72191	72309	.	+	.	ID=id2;Parent=rna1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;gbkey=mRNA;gene=ATP5O;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
    1	Gnomon	exon	73696	73746	.	+	.	ID=id3;Parent=rna1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;gbkey=mRNA;gene=ATP5O;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
    1	Gnomon	exon	74679	74789	.	+	.	ID=id4;Parent=rna1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;gbkey=mRNA;gene=ATP5O;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
    1	Gnomon	exon	76942	77071	.	+	.	ID=id5;Parent=rna1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;gbkey=mRNA;gene=ATP5O;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
    1	Gnomon	exon	77760	77872	.	+	.	ID=id6;Parent=rna1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;gbkey=mRNA;gene=ATP5O;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
    1	Gnomon	exon	79089	79175	.	+	.	ID=id7;Parent=rna1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;gbkey=mRNA;gene=ATP5O;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
    1	Gnomon	exon	79463	79644	.	+	.	ID=id8;Parent=rna1;Dbxref=GeneID:102170632,Genbank:XM_005674665.3;gbkey=mRNA;gene=ATP5O;product=ATP synthase%2C H+ transporting%2C mitochondrial F1 complex%2C O subunit;transcript_id=XM_005674665.3
3. result file
>   chromosome,fst_start,fst_end,N_VARIANTS,WEIGHTED_FST,MEAN_FST,V7,gff_start,gff_end,gene
    1,1,50000,277,0.0180669,0.012286700000000001,0.62292850701185,60028,60099,TRNAC-GCA
    1,1,50000,277,0.0180669,0.012286700000000001,0.62292850701185,72191,79644,ATP5O
    1,1,50000,277,0.0180669,0.012286700000000001,0.62292850701185,89963,333854,ITSN1
    1,10001,60000,310,0.0200716,0.0132517,0.6997222592616109,60028,60099,TRNAC-GCA
    1,10001,60000,310,0.0200716,0.0132517,0.6997222592616109,72191,79644,ATP5O
    1,10001,60000,310,0.0200716,0.0132517,0.6997222592616109,89963,333854,ITSN1
    1,20001,70000,345,0.0135304,0.00898398,0.44914945923360705,60028,60099,TRNAC-GCA
    1,20001,70000,345,0.0135304,0.00898398,0.44914945923360705,72191,79644,ATP5O
    1,20001,70000,345,0.0135304,0.00898398,0.44914945923360705,89963,333854,ITSN1
