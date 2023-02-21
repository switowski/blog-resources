import math

def compute_result():
    # Bunch of dummy math operations
    result = 0
    for number in range(1_000_000):
        double = number * 2
        result += math.sqrt(double) + double
    return result


import math
from numba import jit

@jit
def compute_result_jit():
    # Bunch of dummy math operations
    result = 0
    for number in range(1_000_000):
        double = number * 2
        result += math.sqrt(double) + double
    return result


@jit(nopython=True)
def compute_result_jit_nopython():
    # Bunch of dummy math operations
    result = 0
    for number in range(1_000_000):
        double = number * 2
        result += math.sqrt(double) + double
    return result
