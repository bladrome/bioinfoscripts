#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string/join.hpp>
#include <boost/range/adaptor/transformed.hpp>

#include "csvutils.h"

using namespace std;


vector< vector<double> > readcsv(char* filepath)
{
    vector< vector<double> > ret;
    ifstream ifs(filepath);
    string line;
    while( getline(ifs, line) ){
        vector<double> vector_line;
        stringstream linestream(line);
        string cell;
        while( getline(linestream, cell, ',') ){
            double number = boost::lexical_cast<double>(cell);
            vector_line.push_back(number);
        }
        ret.push_back(vector_line);
    }

    return ret;
}


vector< vector<int> > binarize(vector< vector<double> >& data, double binary_shreshold)
{
    vector< vector<int> > ret;
    for(unsigned int i = 0; i < data.size(); ++i){
        vector<int> line;
        for(unsigned int j = 0; j < data[i].size(); ++j){
            int boolvalue = data[i][j] > binary_shreshold ? 1 : 0; 
            line.push_back(boolvalue);
        }
        ret.push_back(line);
    }

    return ret;
}

vector< vector<int> > transpose(vector< vector<int> >& data){
    vector< vector<int> > ret;
    for(unsigned int i = 0; i < data[0].size(); ++i){
        vector<int> line;
        for(unsigned int j = 0; j < data.size(); ++j)
            line.push_back(data[j][i]);
        ret.push_back(line);
    }

    return ret;
}

int writecsv(vector< vector<double> >& data, char* filepath){
    ofstream ofs;
    ofs.open(filepath, ios_base::out);
    for (unsigned int i = 0; i < data.size(); ++i){
        vector<string> stringline;
        for (unsigned int j = 0; j < data.size(); ++j){
            stringline.push_back(boost::lexical_cast<string>(data[i][j]));
        }
        ofs << boost::join(stringline, ", ") << endl;
        //vector<double> tmp = data.at(i);
        //cout << "line size(): " << tmp.size();
        //ofs << boost::join(tmp | boost::adaptors::transformed( static_cast<string(*)(double)>(std::to_string)), ", ") << endl;
    }
    ofs.close();

    return 0;
}

/*
int main(int argc, char* argv[])
{
    vector< vector<double> > data = readcsv((char*)"../abundance.cvs");
    vector< vector<int> > booldata = binarize(data, 0.001);
    vector< vector<int> > transdata = transpose(booldata);
    for(unsigned int i = 0; i < transdata.size(); ++i){
        for(unsigned int j = 0; j < transdata[i].size(); ++j){
            cout << transdata[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
*/
