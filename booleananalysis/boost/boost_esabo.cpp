#include <iostream>
#include <boost/python.hpp>
#include <boost/python/numpy.hpp>


namespace bp =  boost::python;
namespace np = boost::python::numpy;


int print_ndarray(np::ndarray& nd_data){
    int shape0 = nd_data.shape(0);
    int shape1 = nd_data.shape(1);

    for (int i = 0; i < shape0; ++i){
        for (int j = 0; j < shape1; ++j){
            std::cout << nd_data[i][j];
        }
        std::cout << "\n";
    }
}

BOOST_PYTHON_MODULE(boostesabo)
{
    using namespace boost::python;
    def("print_ndarray", &print_ndarray);

}

