#ifndef CSVUTILS_H
#define CSVUTILS_H

#include <vector>
#include <iostream>
using namespace std;

vector< vector<double> > readcsv(char* filepath);
vector< vector<int> > binarize(vector< vector<double> >& data, double binary_shreshold);
vector< vector<int> > transpose(vector< vector<int> >& data);
int writecsv(vector< vector<double> >& data, char* filepath);


#endif
