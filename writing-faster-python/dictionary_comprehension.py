# dictionary_comprehension.py

NUMBERS = list(range(1000))


def for_loop():
    powers = {}
    for number in NUMBERS:
        powers[number] = number * number
    return powers


def dict_from_tuples():
    return dict([(n, n * n) for n in NUMBERS])


def dict_comprehension():
    return {i: i * i for i in NUMBERS}


######################### Benchmark more operations ###########################

MORE_NUMBERS = list(range(1_000_000))


def for_loop2():
    powers = {}
    for number in MORE_NUMBERS:
        powers[number] = number * number
    return powers


def dict_from_tuples2():
    return dict([(n, n * n) for n in MORE_NUMBERS])


def dict_comprehension2():
    return {i: i * i for i in MORE_NUMBERS}


###################### Combining 2 iterables together #########################
KEYS = list(range(1_000_000))
VALUES = [x * x for x in range(1_000_000)]


def comprehension_with_zip():
    return {key: value for key, value in zip(KEYS, VALUES)}


def just_zip():
    return dict(zip(KEYS, VALUES))
