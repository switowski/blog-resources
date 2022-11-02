MILLION_NUMBERS = list(range(1_000_000))

def for_loop():
    output = []
    for element in MILLION_NUMBERS:
        if not element % 2:
            output.append(element)
    return output

def list_comprehension():
    return [number for number in MILLION_NUMBERS if not number % 2]
