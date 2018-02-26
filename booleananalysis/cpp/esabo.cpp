#include <iostream>
#include <algorithm>
#include <random>
#include <string>
#include <cmath>
#include <chrono>
#include <boost/program_options.hpp>
#include <array>
#include <vector>
#include "csvutils.h"

using namespace std;
namespace po = boost::program_options;

int count_one(vector<int> a);
int count_zero(vector<int> a);
double entlog(double x);
vector<double> jaccardindex(vector<int> a, vector<int> b);
double boolean_operation_entropy(vector<int> a, vector<int> b);
double entropy(vector<int> a, vector<int> b, int random_times = 1);
double vector_entropy(vector<double> p);

int main(int argc, char *argv[]) {

    /* program_options
    po::option_description desc("Options");
    desc.add_options()
        ("csvfile", po::value<char*>(), "set csv file path")
        ("threhold", po::value<double>(), "set binarize threhold")
        ;
    po::variables_map vm; po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    if( vm.count("threhold") ){
        cout << "threhold" << vm["threhold"].as<double>() << endl;
        return 1;
    }
    if ( vm.count("csvfile") ){
        cout << "CSVfile" << vm["csvfile"] << endl;
        return 1;
    }
    */

    if (argc != 4){
        cout << "Usage: " << argv[0] << " " <<  "inputfile.csv " <<  "threhold " << " outputfile.csv" << endl;
        return 1;
    }

    vector< vector<double> > data = readcsv(argv[1]);
    vector< vector<int> > booldata = binarize(data, atof(argv[2]));
    vector< vector<int> > transdata = transpose(booldata);

    vector< vector<double> > result;
    vector<double> resline(transdata[0].size(), 0);
    for(unsigned int i = 0; i < transdata.size(); ++i)
        result.push_back(resline);
    
    for(unsigned int i = 0; i < transdata.size(); ++i){
        for(unsigned int j = i; j < transdata.size(); ++j){
            result[i][j] = result[j][i] = entropy(transdata[i], transdata[j]);
        }
    }

    writecsv( result, argv[3]);
    
    /* stardard output
    for(unsigned int i = 0; i < result.size(); ++i){
        for(unsigned int j = 0; j < result.size(); ++j)
            cout << result[i][j] << " ";
        cout << endl;
    }
    */

  return 0;
}

double vector_entropy(vector<double> p) {
  double res = 0;
  for (unsigned int i = 0; i < p.size(); ++i) {
    res += p[i] * entlog(p[i]);
  }

  return -res;
}

double binary_entropy(vector<int> v) {
  double p1 = count_one(v) / double(v.size());
  double p0 = count_zero(v) / double(v.size());
  vector<double> p;
  p.push_back(p1);
  p.push_back(p0);

  return vector_entropy(p);
}

double boolean_operation_entropy(vector<int> a, vector<int> b) {
  double res = 0.0;
  vector<int> c = vector<int>(a.size());
  if (a.size() == b.size()) {
    for (unsigned int i = 0; i < a.size(); ++i) {
      // Boolean operation
      // AND
      c[i] = a[i] & b[i];
    }
    res = binary_entropy(c);
  }

  return res;
}


double entropy(vector<int> a, vector<int> b, int random_times)
{
    random_times =  random_times == 1 ? a.size() : random_times;
    double x = boolean_operation_entropy(a, b);
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();   
    vector<double> varx;
    for(int i = 0; i < random_times; ++i){
       shuffle(b.begin(), b.end(), default_random_engine(seed));
       double t =  boolean_operation_entropy(a, b);
       varx.push_back(t);

    }

    double sum = std::accumulate(std::begin(varx), std::end(varx), 0.0);  
    double mean =  sum / varx.size();
  
    double accum  = 0.0;  
    std::for_each (std::begin(varx), std::end(varx), [&](const double d) {  
        accum  += (d-mean)*(d-mean);  
    });  
    double stdev = sqrt( accum / (varx.size()-1) );


    //cout << "mean:" << mean << endl;
    //cout << "sum:" << sum << endl;
    //cout << "accum:" << accum << endl;
    //cout << "x - mean:" << x - mean << endl;
    //cout << "stdev:" << stdev << endl;


    return accum == 0 ? 0 : (x - mean) / stdev;
}




int count_zero(vector<int> a) {
  int res = 0;
  for (unsigned int i = 0; i < a.size(); ++i) {
    if (a[i] == 0)
      ++res;
  }

  return res;
}

int count_one(vector<int> a) {
  int res = 0;
  for (unsigned int i = 0; i < a.size(); ++i) {
    if (a[i] == 1)
      ++res;
  }

  return res;
}

double entlog(double x) { return (x - 0.0) < 1e-30 ? 0 : log(x); }

vector<double> jaccardindex(vector<int> a, vector<int> b) {
  if (a.size() != b.size()) {
    return vector<double>(4, 0.0f);
  } else {
    double length = a.size();
    double a1 = count_one(a) / length;
    double a0 = count_zero(a) / length;
    double b1 = count_one(b) / length;
    double b0 = count_zero(b) / length;

    double p00 = a0 * b0;
    double p01 = a0 * b1;
    double p10 = a1 * b0;
    double p11 = a1 * b1;

    vector<double> res;
    res.push_back(p00);
    res.push_back(p01);
    res.push_back(p10);
    res.push_back(p11);

    return res;
  }
}

double entropy_jaccardindex(vector<int> a, vector<int> b) {
  vector<double> p = jaccardindex(a, b);
  double ent = vector_entropy(p);

  return ent;
}
