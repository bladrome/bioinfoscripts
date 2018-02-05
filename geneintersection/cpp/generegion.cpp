/**
 * ./GeneRegion v0.1
 * 2017年 12月 04日 星期一 16:42:27 CST
 *
 * Usage:./GeneRegion > result.csv
 * TODO:
 * 1.Read the whole datafile rather than a certain number of lines.
 * 2.Parse arguments.
 * 3.Use a better strategy to find similar genes, such as a good distance.
 *
 */
#include <algorithm>
#include <fstream>
#include <iostream>
#include <unistd.h>
#include <vector>

using namespace std;

/* Parameters:
 * LENGTHOFFILE:
 *      The last part data  of python_test_data is not integrated.
 * RATIO:
 *      Min Ratio of intersect length.
 * DISTANCETHRESHOLD:
 *      The distance of three gene region SHOULD be small.
 *
*/
const int LENGTHOFFILE = 870;
const float RATIO = 0.9;
const int DISTANCETHRESHOLD = 5000;

// Nearest N Neighbor strategy.
// const int SIMILAR_NEIGHBOR = 3;

string str_header[] = {
    "sample1_Chr1",          "sample1_start(Pos1)",   "sample1_end(Pos2)",
    "sample2_Chr1",          "sample2_start(Pos1)",   "sample2_end(Pos2)",
    "sample3_Chr1",          "sample3_start(Pos1)",   "sample3_end(Pos2)",
    "sample1 region length", "sample2 region length", "sample3 region length",
    "ratio of sample1",      "ratio of sample2",      "ratio of sample3"};

vector<string> sample1_chromosome_name;
vector<int> sample1_region_start;
vector<int> sample1_region_end;

vector<string> sample2_chromosome_name;
vector<int> sample2_region_start;
vector<int> sample2_region_end;

vector<string> sample3_chromosome_name;
vector<int> sample3_region_start;
vector<int> sample3_region_end;

vector<string> header(str_header,
                      str_header + int(sizeof(str_header) / sizeof(string)));

void print_header();
void print_help(int argc, char *argv[]);
int read_csvfile(char *filepath);
float distance_three_region(int, int, int, int, int, int);

int main(int argc, char *argv[]) {

  /* TODO parse argument
  if ( argc == 1 ){
      print_help(argc, argv);
      exit(1);
  }
  */

  // TODO:check the existence of datafile.
  // read_csvfile((char*)argv[1]);
  read_csvfile((char *)"./python_test_data.csv");
  print_header();

  for (int i = 0; i < LENGTHOFFILE; ++i) {
    for (int j = 0; j < LENGTHOFFILE; ++j) {

      if (sample1_chromosome_name[i] != sample2_chromosome_name[j]) {
        continue;
      }
      if (min(sample1_region_end[i], sample2_region_end[j]) <
          max(sample1_region_start[i], sample2_region_start[j])) {
        continue;
      }

      for (int k = 0; k < LENGTHOFFILE; ++k) {

        if (sample1_chromosome_name[i] != sample3_chromosome_name[k] &&
            sample2_chromosome_name[j] != sample3_chromosome_name[k]) {
          continue;
        }
        if (min(sample1_region_end[i], sample3_region_end[k]) <
            max(sample2_region_start[j], sample3_region_start[k])) {
          continue;
        }
        int max_start =
            max(max(sample1_region_start[i], sample2_region_start[j]),
                sample3_region_start[k]);
        int min_end = min(min(sample1_region_end[i], sample2_region_end[j]),
                          sample3_region_end[k]);
        int intersect_length = min_end - max_start;
        int sample1_region_length =
            sample1_region_end[i] - sample1_region_start[i];
        int sample2_region_length =
            sample2_region_end[j] - sample2_region_start[j];
        int sample3_region_length =
            sample3_region_end[k] - sample3_region_start[k];
        float sample1_ratio = float(intersect_length) / sample1_region_length;
        float sample2_ratio = float(intersect_length) / sample2_region_length;
        float sample3_ratio = float(intersect_length) / sample3_region_length;

        if (distance_three_region(
                sample1_region_start[i], sample1_region_end[i],
                sample2_region_start[j], sample2_region_end[j],
                sample3_region_start[k],
                sample3_region_end[k]) <= DISTANCETHRESHOLD)
          if (min(min(sample1_ratio, sample2_ratio), sample3_ratio) > RATIO) {
            cout << sample1_chromosome_name[i] << ',' << sample1_region_start[i]
                 << ',' << sample1_region_end[i] << ','

                 << sample2_chromosome_name[j] << ',' << sample2_region_start[j]
                 << ',' << sample2_region_end[j] << ','

                 << sample3_chromosome_name[k] << "," << sample3_region_start[k]
                 << ',' << sample3_region_end[k] << ','

                 << sample1_region_length << ',' << sample2_region_length << ','
                 << sample3_region_length << ','

                 << sample1_ratio << ',' << sample2_ratio << ','
                 << sample3_ratio << endl;
            // cout << "(i, j, k):(" << i << "," << j << "," << k  << ")"<<
            // endl;
            /*
            if (sample1_chromosome_name[i] == "X1"){
                cout << sample1_region_start[i] << " " <<  sample1_region_end[i]
            << endl;
            }
            */
          }
      }
    }
  }

  return 0;
}

void print_header() {
  for (vector<string>::iterator it = header.begin(); it != header.end(); ++it) {
    cout << *it << ',';
  }
  cout << endl;

  return;
}

void print_help(int argc, char *argv[]) {
  cout << "argc: " << argc << endl;
  cout << "Usage: " << argv[0] << "  "
       << "datafile.csv" << endl;
}

int read_csvfile(char *filepath) {
  ifstream ifs(filepath);
  string orgin_header;
  getline(ifs, orgin_header);
  for (int i = 0; i < LENGTHOFFILE; ++i) {

    string chromosome_name;
    int region_start;
    int region_end;

    getline(ifs, chromosome_name, ',');
    ifs >> region_start;
    ifs.get();
    getline(ifs, chromosome_name, ',');
    ifs >> region_end;
    ifs.get();
    sample1_chromosome_name.push_back(chromosome_name);
    sample1_region_start.push_back(region_start);
    sample1_region_end.push_back(region_end);

    getline(ifs, chromosome_name, ',');
    ifs >> region_start;
    ifs.get();
    getline(ifs, chromosome_name, ',');
    ifs >> region_end;
    ifs.get();
    sample2_chromosome_name.push_back(chromosome_name);
    sample2_region_start.push_back(region_start);
    sample2_region_end.push_back(region_end);

    getline(ifs, chromosome_name, ',');
    ifs >> region_start;
    ifs.get();
    getline(ifs, chromosome_name, ',');
    ifs >> region_end;
    ifs.get();
    sample3_chromosome_name.push_back(chromosome_name);
    sample3_region_start.push_back(region_start);
    sample3_region_end.push_back(region_end);
  }

  return 1;
}

float distance_three_region(int s1, int e1, int s2, int e2, int s3, int e3) {
  float d12 = abs(s1 - s2) + abs(e1 - e2);
  float d13 = abs(s1 - s3) + abs(e1 - e3);
  float d23 = abs(s2 - s3) + abs(e2 - e3);

  return d12 + d13 + d23;
}
