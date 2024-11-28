![Python](https://img.shields.io/badge/Python-3.x-blue)
![Dependencies](https://img.shields.io/badge/dependencies-Numpy-blue)
![License](https://img.shields.io/badge/license-GPL3-green)

# Fibonacci Functions Implementations

benchmark to determine the maximum number of iterations each can perform in 10 seconds.
Features

- Multiple Fibonacci sequence algorithms:
    - Iterative: A simple loop-based approach.
    - Recursive (brute force): A naive implementation using recursion.
    - Recursive with memoization: Optimized recursion using caching.
    - Matrix Exponentiation: A highly efficient algorithm with logarithmic complexity.
- A benchmarking system to compare the performance of each algorithm.

## Dependencies
* Python 3.x (ensure you have Python installed)
* Numpy (install it via ``pip install numpy`` if not already available)
## How to run
1. Clone this repo :
```sh
git clone https://github.com/yourusername/fibonacci-functions.git
cd fibonacci-functions-implementations
```
2. Execute the script :
python3 ./src/fibo.py

> Note: The brute-force recursive algorithm may appear significantly slower due to the lack of optimization and the overhead of memory heap operations.

## Example output
```
Function fibonacci_iterative completed 12021 iterations in 10.01 seconds.
Function fibonacci_recursive_brute completed 38 iterations in 15.77 seconds.
Function fibonacci_recursive_intelligent completed 390524 iterations in 10.01 seconds.
Function fibonacci_exponential_matrix completed 141438 iterations in 10.01 seconds.
```