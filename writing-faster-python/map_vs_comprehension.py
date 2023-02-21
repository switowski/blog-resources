from math import sqrt

NUMBERS = range(1_000_001)

# First we use a lambda function
def map_lambda():
    return sum(map(lambda x: x * x, NUMBERS))


def comprehension_lambda():
    return sum([x * x for x in NUMBERS])


# And for comparison, let's use a named function
def map_sqrt():
    return sum(map(sqrt, NUMBERS))


def comprehension_sqrt():
    return sum([sqrt(x) for x in NUMBERS])
