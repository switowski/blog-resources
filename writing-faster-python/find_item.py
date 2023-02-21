from itertools import count

def while_loop():
    item = 1
    while True:
        # You don't need to use brackets, but they improve readability
        if (item % 42 == 0) and (item % 43 == 0):
            return item
        item += 1

# If the element is earely on on list (1806th out of 10 000)
# 25% faster
def for_loop():
    for item in range(1, 10000):
        if (item % 42 == 0) and (item % 43 == 0):
            return item

def while_loop2():
    item = 1
    while True:
        if (item % 98 == 0) and (item % 99 == 0):
            return item
        item += 1

def for_loop2():
    for item in range(1, 10000):
        if (item % 98 == 0) and (item % 99 == 0):
            return item

def while_loop3():
    item = 1
    while True:
        if (item % 9999 == 0) and (item % 9998 == 0):
            return item
        item += 1

def for_loop3():
    for item in range(1, 100_000_000):
        if (item % 9999 == 0) and (item % 9998 == 0):
            return item

# If the element is at the end of the list (9702th out of 10 000)
# 25% faster for finding 1806th element from 10 000 elements
def test_while_loop2():
    item = 1
    while True:
        if (item % 98 == 0) and (item % 99 == 0):
            return item
        item += 1

# Still around 25% faster, so the number of items doesn't matter that much
def test_for_loop2():
    for item in range(1, 10000):
        if (item % 98 == 0) and (item % 99 == 0):
            return item

# More elements in the range doesn't make difference
def test_for_loop3():
    for item in range(1, 100000000):
        if (item % 98 == 0) and (item % 99 == 0):
            return item

# As fast as range, but you don't need to know the upper limit
from itertools import count

def count_numbers():
    for item in count(1):
        if (item % 42 == 0) and (item % 43 == 0):
            return item

# This is slow because we need to iterate over all items
def list_comprehension():
    return [item for item in range(1, 10000) if (item % 42 == 0) and (item % 43 == 0)][0]

# This is as fast as for loop, but much cleaner
def generator():
    return next(item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))

def for_loop_flat():
    items = []
    for item in count(1):
        if (item % 42 == 0) and (item % 43 == 0):
            items.append(item)
        if len(items) == 3:
            return items

def for_loop_3_items():
    items = []
    for item in count(1):
        if (item % 42 == 0) and (item % 43 == 0):
            items.append(item)
            if len(items) == 3:
                return items

def generator_3_items():
    gen = (item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))
    return [next(gen), next(gen), next(gen)]


# failed approaches


# This is even slower than everything else
def test_filter():
    return next(filter(lambda x: x % 42 == 0 and x % 43 == 0, count(1)))
