# membership.py

MILLION_NUMBERS = list(range(1_000_000))
SET_OF_NUMBERS = set(MILLION_NUMBERS)

def test_for_loop(number):
    for item in MILLION_NUMBERS:
        if item == number:
            return True
    return False

def test_in(number):
    return number in MILLION_NUMBERS

MILLION_NUMBERS = set(range(1_000_000))

def test_in_set(number):
    return number in MILLION_NUMBERS
