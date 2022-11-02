from itertools import count

def count_numbers():
    for item in count(1):
        if (item % 42 == 0) and (item % 43 == 0):
            return item

def generator():
    return next(item for item in count(1) if (item % 42 == 0) and (item % 43 == 0))
