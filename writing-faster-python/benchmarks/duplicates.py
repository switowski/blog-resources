from random import randrange

DUPLICATES = [randrange(100) for _ in range(1_000_000)]

def test_for_loop():
    unique = []
    for element in DUPLICATES:
        if element not in unique:
            unique.append(element)
    return unique

def test_set():
    return list(set(DUPLICATES))
