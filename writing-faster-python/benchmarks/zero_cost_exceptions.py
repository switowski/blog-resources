from random import random, sample
from math import sqrt

########################### Filter list example ###############################
MILLION_NUMBERS = list(range(1_000_000))


def for_loop():
    output = []
    for element in MILLION_NUMBERS:
        if not element % 2:
            try:
                output.append(element)
            except Exception:
                pass
    return output


########################### Pi estimation example #############################
# Total number of darts to throw.
TOTAL = 100_000_000


def estimate_pi():
    # Number of darts that land inside the circle.
    inside = 0

    for _ in range(TOTAL):
        x2 = random() ** 2
        y2 = random() ** 2
        # Check if the x and y points lie inside the circle
        if sqrt(x2 + y2) < 1.0:
            try:
                inside += 1
            except Exception:
                pass
    return (float(inside) / TOTAL) * 4


########################## Bubble sort examplee ###############################
DESCENDING_10_000 = list(range(10_000, 0, -1))


def bubble_sort():
    numbers = DESCENDING_10_000[:]
    changed = True
    while changed:
        changed = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                try:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    changed = True
                except Exception:
                    pass
    return numbers
