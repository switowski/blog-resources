MILLION_NUMBERS = list(range(1_000_000))


def for_loop():
    output = []
    for element in MILLION_NUMBERS:
        if not element % 2:
            output.append(element)
    return output


def list_comprehension():
    return [number for number in MILLION_NUMBERS if not number % 2]


def test_generator_expression():
    return (number for number in MILLION_NUMBERS if not number % 2)


def filter_function():
    return filter(lambda x: not x % 2, MILLION_NUMBERS)


def filter_return_list():
    return list(filter(lambda x: not x % 2, MILLION_NUMBERS))


from itertools import filterfalse


def filterfalse_list():
    return list(filterfalse(lambda x: x % 2, MILLION_NUMBERS))


def fizz_buzz():
    output = []
    for number in MILLION_NUMBERS:
        if number % 3 == 0 and number % 5 == 0:
            output.append("fizzbuzz")
        elif number % 3 == 0:
            output.append("fizz")
        elif number % 5 == 0:
            output.append("buzz")
        else:
            output.append(number)
    return output


def transform(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    return number


def fizz_buzz2():
    output = []
    for number in MILLION_NUMBERS:
        output.append(transform(number))
    return output


def fizz_buzz2_comprehension():
    return [transform(number) for number in MILLION_NUMBERS]


def fizz_buzz_comprehension():
    return [
        "fizzbuzz" if x % 3 == 0 and x % 5 == 0
        else "fizz" if x % 3 == 0
        else "buzz" if x % 5 == 0
        else x
        for x in MILLION_NUMBERS
    ]
