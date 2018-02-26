#ifndef READCSV_H
#define READCSV_H

#include <vector>
#include <iostream>
using namespace std;

vector< vector<double> > readcsv(char* filepath);
vector< vector<int> > binarize(vector< vector<double> >& data, double binary_shreshold);
vector< vector<int> > transpose(vector< vector<int> >& data);




#endif
