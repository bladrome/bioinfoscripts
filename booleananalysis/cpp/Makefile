all:run

esabo:esabo.cpp csvutils.cpp
	g++ -o $@ $^ -std=c++0x -static-libstdc++ -g

.PHONY:clean run
clean:
	rm esabo

run:esabo
	./esabo ../journal.pgen.1005846.s011.csv 0.01 result.csv
