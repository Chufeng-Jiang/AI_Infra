
#include <pybind11/pybind11.h>

namespace py = pybind11;

// Native C++ function
int add(int i, int j) {
    return i + j;
}

// Expose C++ functions to Python
PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example plugin";

    m.def("add", &add, "A function that adds two numbers");
}
