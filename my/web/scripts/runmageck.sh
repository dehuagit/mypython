#!/bin/bash


# The old "run" command will be discontinued.
# mageck run --fastq test1.fastq test2.fastq -l library.txt -n demo --sample-label L1,CTRL -t L1 -c CTRL


source /home/rnaicore/python3/NGS_MAGECKO/bin/activate

if [ "$#" -ne 6 ]; then
	echo "Error parameter, "
	echo "please type: $0 Library label1name input_fastq1 label2name  input_fastq2 outputName"
	exit 1
fi

LIB=$1
LABEL1=$2
INPUTFASTQ1=$3
LABEL2=$4
INPUTFASTQ2=$5
OUTPUTNAME=$6

# instead, execute "count" command first to generate read count tables
#mageck count -l Mageck.csv -n rnaiCore --sample-label L1,CTRL  --fastq test1.fastq test2.fastq 
cmd="mageck count -l ${LIB} -n ${OUTPUTNAME} --sample-label ${LABEL1},${LABEL2}  --fastq ${INPUTFASTQ1} ${INPUTFASTQ2}"

echo $cmd
eval $cmd

#mkdir -p ${OUTPUTNAME}
mkdir -p RESULT
mv ${OUTPUTNAME}.* ./RESULT
mv ${OUTPUTNAME}_* ./RESULT

touch workdone


