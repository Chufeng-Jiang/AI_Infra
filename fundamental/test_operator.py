
from pathlib import Path

import torch
from torch.utils.cpp_extension import load

# Directory containing test_operator.py
BASE_DIR = Path(__file__).resolve().parent

# Absolute path to C++ source
CPP_SOURCE = BASE_DIR / "torch_operator.cpp"

print("Compiling:", CPP_SOURCE)

# Compile and load C++ operator
load(
    name="demo_ops_ext",
    sources=[str(CPP_SOURCE)],
    extra_cflags=["-O2"],
    is_python_module=False,
    verbose=True,
)

# CPU test
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.ops.demo_ops.add_one(x)

print("CPU result:", y)
torch.testing.assert_close(y, x + 1)

# GPU test
if torch.cuda.is_available():
    x_gpu = x.cuda()
    y_gpu = torch.ops.demo_ops.add_one(x_gpu)

    print("GPU result:", y_gpu)
    torch.testing.assert_close(y_gpu, x_gpu + 1)
