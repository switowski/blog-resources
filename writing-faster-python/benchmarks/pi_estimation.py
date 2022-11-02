from random import random
from math import sqrt

# Total number of darts to throw.
TOTAL = 100_000_000

def estimate_pi():
    # Number of darts that land inside the circle.
    inside = 0

    for _ in range(TOTAL):
        x2 = random()**2
        y2 = random()**2
        # Check if the x and y points lie inside the circle
        if sqrt(x2 + y2) < 1.0:
            inside += 1
    return (float(inside) / TOTAL) * 4
