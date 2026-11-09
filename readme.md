## Environment


## Fundamental

### pybind11_demo
```
g++ -O3 -Wall -shared -std=c++17 -fPIC \
    $(python3 -m pybind11 --includes) \
    ./fundamental/example.cpp \
    -o ./fundamental/example$(python3 -m pybind11 --extension-suffix)
```

```
cd fundamental
python3 -c "import example; print(example.add(1, 2))"
```
### PyTorch operator registration
```
MAX_JOBS=2 python3 ./fundamental/test_operator.py
```