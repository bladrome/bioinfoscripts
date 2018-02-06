# add species to to fafile


## format
1. fafile
>seq_name
>sequences
2. pyhum
>species
>seq_names

## function
**Find species in pylum file for each seqname belongs to and add them before each seqname**

3. output
>species_seq_name
>sequences
4. file format:

    11-L_HFGMYALXX_L3.unigene.fa
>\>7-L_HFGMYALXX_L3.gap_remove.scatigs.500_seq_GI_0017323
AATATAATTAATTATAATAATAATTTAAATAATAGCCAAATTTTAATGAATGACCGGAAAAAAA......
>\>9-L_HGVHNALXX_L4.gap_remove.scatigs.500_seq_GI_0068425
CAACAAAATAATGAAAATACTTTAATAAAGCCAAAATTTGTTGGTGATGAAAGCTCATTTTTAA......
    11-L_HFGMYALXX_L3.pyhum_1
>"Bacteroides caccae"	4-L_HFGMYALXX_L3.gap_remove.scatigs.500_seq_GI_0009630	4-L_HFGMYALXX_L3.gap_remove.scatigs.500_seq_GI_0009653	9-L_HGVHNALXX_L4.gap_remove.scatigs.500_seq_GI_0047285	......
>"Bacteroides cellulosilyticus"	4-L_HFGMYALXX_L3.gap_remove.scatigs.500_seq_GI_0094369	4-L_HFGMYALXX_L3.gap_remove.scatigs.500_seq_GI_0064375	5-L_HFGMYALXX_L3.gap_remove.scatigs.500_seq_GI_0080770	5-L_HFGMYALXX_L3.gap_remove.scatigs.500_seq_GI_0080785	......

