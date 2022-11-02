from random import sample

# List of 1 000 000 integers randomly shuffled
MILLION_RANDOM_NUMBERS = sample(range(1_000_000), 1_000_000)

def test_sort():
    random_list = MILLION_RANDOM_NUMBERS[:]
    return random_list.sort()

def test_sorted():
    random_list = MILLION_RANDOM_NUMBERS[:]
    return sorted(random_list)
