DESCENDING_10_000 = list(range(10_000, 0, -1))

def bubble_sort():
    numbers = DESCENDING_10_000[:]
    changed = True
    while changed:
        changed = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                changed = True
    return numbers
