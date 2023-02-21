# sorting.py
from random import sample

# List of 1 000 000 integers randomly shuffled
# MILLION_RANDOM_NUMBERS = sample(range(1_000_000), 1_000_000)
# MILLION_RANDOM_NUMBERS = list(range(1_000_000))
# MILLION_RANDOM_NUMBERS = list(range(1_000_000,0, -1))
# 10% of numbers are random
MILLION_RANDOM_NUMBERS = [*range(900_000), *sample(range(1_000_000), 100_000)]


def test_sort():
    random_list = MILLION_RANDOM_NUMBERS[:]
    return random_list.sort()

def test_sorted():
    random_list = MILLION_RANDOM_NUMBERS[:]
    return sorted(random_list)

# import numpy as np

# MILLION_RANDOM_NUMPY_NUMBERS = np.random.randint(low=1, high=1_000_000, size=100_000_000)

# def test_numpy():
#     return np.sort(MILLION_RANDOM_NUMPY_NUMBERS)
