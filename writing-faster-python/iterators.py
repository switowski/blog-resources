def generator(stop=1_000_000):
    for n in range(stop):
        yield n


def generator_yield_from(stop=1_000_000):
    yield from range(stop)


def generator_expression(stop=1_000_000):
    return (n for n in range(stop))


def iterator(stop=1_000_000):
    return iter(range(stop))


class iterator_protocol:
    def __init__(self, stop=1_000_000):
        self.stop = stop
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == self.stop:
            raise StopIteration
        self.num += 1
        return self.num


class get_item:
    def __init__(self, stop=1_000_000):
        self.numbers = range(stop)

    def __getitem__(self, index):
        # I'm not sure what would be a good implementation here
        return self.numbers[index]
