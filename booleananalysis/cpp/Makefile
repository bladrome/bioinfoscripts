


all:run

esabo:esabo.cpp csvutils.cpp
	g++ -o $@ $^ -std=c++11 -g

.PHONY:clean run
clean:
	rm esabo

run:esabo
	./esabo ./journal.pgen.1005846.s011.csv 0.01 result.csv
