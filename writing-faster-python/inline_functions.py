# Dummy functions
def calculate_a():
    return 1


def calculate_b():
    return sum([calculate_a() for _ in range(100)])


def calculate_c():
    return sum([calculate_b() for _ in range(100)])


def calculate_d():
    return sum([calculate_c() for _ in range(100)])


# Actual functions to benchmark
def separate_functions():
    return calculate_d()


def inline_functions():
    return sum([sum([sum([1 for _ in range(100)]) for _ in range(100)]) for _ in range(100)])


def inline_variables():
    a = 1
    b = sum([a for _ in range(100)])
    c = sum([b for _ in range(100)])
    d = sum([c for _ in range(100)])
    return d
