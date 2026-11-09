
#include <ATen/ATen.h>
#include <torch/library.h>

// Actual C++ implementation
at::Tensor add_one(const at::Tensor& x) {
    return x + 1;
}

// 1. Declare the operator schema
TORCH_LIBRARY(demo_ops, m) {
    m.def("add_one(Tensor x) -> Tensor");
}

// 2. Register CPU implementation
TORCH_LIBRARY_IMPL(demo_ops, CPU, m) {
    m.impl("add_one", &add_one);
}

// 3. Register CUDA implementation
TORCH_LIBRARY_IMPL(demo_ops, CUDA, m) {
    m.impl("add_one", &add_one);
}
