from IPython.core.magic import register_cell_magic


@register_cell_magic("mypy")
def typechecker(line, cell):
    """Run mypy on a block of code.

    Usage:
    %%mypy [PARAMETERS]
    BLOCK_OF_CODE

    Example:
    In [1]: %%mypy
    ...: def greet(name: str) -> str:
    ...:     return f"hello {name}"
    ...: greet('Bob')
    ...:
    ...:
    Out[1]: 0
    """

    try:
        from mypy.api import run
    except ImportError:
        return "'mypy' not installed. Did you run 'pip install mypy'?"

    args = []
    if line:
        args = line.split()

    result = run(["-c", cell, *args])

    if result[0]:
        print("\nType checking report:\n")
        print(result[0])  # stdout

    if result[1]:
        print("\nError report:\n")
        print(result[1])  # stderr

    # Return the mypy exit status
    return result[2]
