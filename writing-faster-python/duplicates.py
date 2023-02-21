from random import randrange

DUPLICATES = [randrange(100) for _ in range(1_000_000)]

def test_for_loop():
    unique = []
    for element in DUPLICATES:
        if element not in unique:
            unique.append(element)
    return unique

def test_comprehension():
    unique = []
    [unique.append(num) for num in DUPLICATES if num not in unique]
    return unique

def test_set():
    return list(set(DUPLICATES))

def test_dict():
    return list(dict.fromkeys(DUPLICATES))

from collections import OrderedDict

def test_ordereddict():
    return list(OrderedDict.fromkeys(DUPLICATES))
