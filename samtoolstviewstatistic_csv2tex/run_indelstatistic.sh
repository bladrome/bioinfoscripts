
samplelist(){
    AWGBGAA05771
    AWGBGAA05772
    AWGBGAA05773
    AWGBGAA05774
    AWGBGAA05775
    AWGBGAA05776
    AWGBGAA05777
    AWGBGAA05778
    AWGBGAA05779
    AWGBGAA05780
    AWGBGAA05781
    AWGBGAA05782
}

for sample in \
    AWGBGAA05771\
    AWGBGAA05772\
    AWGBGAA05773\
    AWGBGAA05774\
    AWGBGAA05775\
    AWGBGAA05776\
    AWGBGAA05777\
    AWGBGAA05778\
    AWGBGAA05779\
    AWGBGAA05780\
    AWGBGAA05781\
    AWGBGAA05782
do
    #echo $sample
    for samplepos in `ls $sample*_txt.csv`
    do
        #echo $samplepos
        python ./indelstatistic.py $samplepos > $samplepos.output
    done
    paste -d ',' *.output > output.$sample
    rm *.output
done
cat output* > INDELBLOCK
rm output*

#for i in `ls *txt.csv`
#do
#python ./indelstatistic.py $i > $i.output
#done
#paste *.output > outputall
#rm *.output
