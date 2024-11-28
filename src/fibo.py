def fibonacci_iterative(n) :
    a = 0
    b = 1
    for _ in range(n) :
        a, b = b, a + b
    return a

def fibonacci_recursive_brute(n) :
    if n==1 or n==2 :
        return 1
    else :
        return fibonacci_recursive_brute(n-1)+fibonacci_recursive_brute(n-2)

def fibonacci_recursive_intelligent(n, solutions: dict = {}) :
    if n==1 or n==2 :
        return 1
    else :
        if n not in solutions :
            solution = fibonacci_recursive_intelligent(n-1, solutions)+fibonacci_recursive_intelligent(n-2, solutions)
            solutions[n] = solution
            return solution
        else :
            return solutions[n]

import numpy as np
def fibonacci_exponential_matrix(n, matrix: np.array = [[1, 1], [1, 0]]) :
    if n == 0 : return 0
    if n == 1 : return 1
    matrix = np.linalg.matrix_power(matrix, n-1)
    return int(matrix[0, 0])


from bench import fibonacci_benchmark
t = 10
fibonacci_benchmark(fibonacci_iterative, t)
fibonacci_benchmark(fibonacci_recursive_brute, t)
fibonacci_benchmark(fibonacci_recursive_intelligent, t)
fibonacci_benchmark(fibonacci_exponential_matrix, t)