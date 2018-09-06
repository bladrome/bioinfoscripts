#!/bin/bash
gibin="./gi2taxid2taxnames.py"
protdb=$1
taxdb=$2
blastfile=$3


#split -l 300000 $blastfile $blastfile_
split -l 300000 $blastfile ${blastfile}_

mkdir tmp
mkdir scripts_template
for file in `ls ${blastfile}_*`
do
cat > scripts_template/run_${file}_tax.sh << EOF
#!/bin/bash
python $gibin $protdb $taxdb $file > tmp/${file}_anntmp
EOF
~/software/submitjynodequeue scripts_template/run_${file}_tax.sh 2 5000000
done
