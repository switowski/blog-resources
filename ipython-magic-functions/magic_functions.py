from collections import deque

from IPython.core.magic import register_line_magic


def interpret(tokens):
    token = tokens.popleft()
    if token == "+":
        return interpret(tokens) + interpret(tokens)
    elif token == "-":
        return interpret(tokens) - interpret(tokens)
    elif token == "*":
        return interpret(tokens) * interpret(tokens)
    elif token == "/":
        return interpret(tokens) / interpret(tokens)
    else:
        return int(token)


@register_line_magic
def pn(line):
    return interpret(deque(line.split()))
