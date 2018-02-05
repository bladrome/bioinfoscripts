SRC+=generegion.cpp
OBJECT=GeneRegion

all:${OBJECT}

${OBJECT}:${SRC}
	g++ generegion.cpp -o $@

.PHONY:run clean

run:${OBJECT}
	./${OBJECT} ./python_test_data.csv > result.csv

clean:
	rm ${OBJECT} result.csv
