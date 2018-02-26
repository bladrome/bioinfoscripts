#include <iostream>
#include <algorithm>
#include <random>
#include <cmath>
#include <chrono>
#include <array>
#include <vector>
#include "readcsv.h"

using namespace std;

int count_one(vector<int> a);
int count_zero(vector<int> a);
double entlog(double x);
vector<double> jaccardindex(vector<int> a, vector<int> b);
double boolean_operation_entropy(vector<int> a, vector<int> b);
double entropy(vector<int> a, vector<int> b, int random_times = 1);
double vector_entropy(vector<double> p);

int main(int argc, char *argv[]) {

    //vector< vector<double> > data = readcsv((char*)"../abundance.cvs");
    vector< vector<double> > data = readcsv((char*)"./journal.pgen.1005846.s011.csv");
    cout << " 111 \n";
    vector< vector<int> > booldata = binarize(data, 0.0001);
    cout << " 222 \n";
    vector< vector<int> > transdata = transpose(booldata);
    cout << " 333 \n";
    for(unsigned int i = 0; i < transdata.size(); ++i){
        for(unsigned int j = 0; j < transdata.size(); ++j){
            cout << entropy(transdata[i], transdata[j]) << " ";
        }
        cout << endl;
    }


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
